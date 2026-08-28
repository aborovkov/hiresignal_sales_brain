#!/usr/bin/env python3
"""Ресегментация базы по рамке GTM от 2026-08-28 (brain/gtm.md).

Две роли вместо девяти сегментов:
  BUYER   - владеет технической оценкой в компании, которая нанимает инженеров сама
  CHANNEL - работает с нанимающими компаниями, но оценку не ведёт; источник рекомендаций

Плюс два служебных состояния: NEEDS-DATA (нет headline, нечем классифицировать)
и OUT (осознанно вне работы).

Read-only. Ничего не пишет в стор.
  python3 scripts/resegment.py                 # сводка
  python3 scripts/resegment.py --untouched     # только те, кому не писали
  python3 scripts/resegment.py --out f.csv     # выгрузка
"""
import argparse, csv, re, sys, collections

NEVER_WRITTEN = ("new", "invited", "connected")

# Владеет технической оценкой. Порядок важен: более специфичное выше.
BUYER = [
    (5, r"\bcto\b|chief technology|chief technical"),
    (5, r"head of (vetting|talent quality)|vp (of )?vetting|vp supply"),
    (4, r"(vp|head|director|chief)[^,|]{0,24}\bengineering\b"),
    (4, r"engineering (manager|lead|leader|leadership)"),
    (4, r"\bvp eng\b|head of eng\b"),
    (3, r"tech(nical)? lead\b"),
    (3, r"chief product officer|\bcpo\b"),
    (3, r"director of (technology|development)"),
    (2, r"\bcoo\b|chief operating"),
]
# Работает с нанимающими компаниями, оценку не ведёт.
CHANNEL = [
    (5, r"recruit(er|ment|ing)|headhunt|head-hunt"),
    (5, r"talent acquisition|\bta\b partner|talent partner"),
    (5, r"sourc(er|ing) specialist|technical sourcer"),
    (4, r"\bhr\b|human resources|hrbp|hr business partner"),
    (4, r"people (ops|operations|partner|lead|director|manager)"),
    (4, r"executive search|staffing"),
    (3, r"career (coach|strategist|consultant)"),
    (3, r"talent (lead|manager|director|specialist|advisor)"),
    (2, r"\bpeople\b|\btalent\b"),
    # рекрутерская речь без слова "recruiter" - частый случай в этой базе
    (3, r"job board|connecting (ambitions|people|talent)|roles with|"
        r"help(ing)? (companies|startups|teams) (hire|scale|grow their team)|"
        r"placement|candidates for|hiring partner|we place|find(ing)? (you )?(the )?(best )?(engineers|developers|talent)"),
]
# Основатель/CEO сам по себе неоднозначен: у рекрутингового агентства это канал,
# у продуктовой компании - покупатель. Решается наличием рекрутерских слов рядом.
FOUNDER = r"founder|co-founder|\bceo\b|owner|managing (director|partner)|entrepreneur"
# Vetting - их продукт: покупают интервью и одновременно мультипликатор.
DUAL = r"staff aug|staffing augmentation|nearshore|offshore|dev shop|software house|talent marketplace|outstaff"

SEG_PRIOR = {
    "smb-inhouse": ("BUYER", 2), "rec-staff-aug": ("BUYER", 2),
    "rec-agency-tech": ("CHANNEL", 2), "rec-fractional": ("CHANNEL", 2),
    "rec-agency-small": ("CHANNEL", 2), "rec-agency-large": ("CHANNEL", 1),
    "partner": ("CHANNEL", 2),
}


def score(pats, t):
    return sum(w for w, p in pats if re.search(p, t))


def classify(r):
    """-> (role, confidence 1-5, why)"""
    seg = (r.get("icp_segment") or "").strip().lower()
    if seg == "out-of-icp":
        return "OUT", 5, "помечен out-of-icp"
    t = " ".join([(r.get("headline") or ""), (r.get("role") or ""),
                  (r.get("company") or "")]).lower()
    if not t.strip():
        return "NEEDS-DATA", 0, "нет headline/role/company"

    b, c = score(BUYER, t), score(CHANNEL, t)
    why = []
    if b: why.append(f"buyer-сигналы {b}")
    if c: why.append(f"channel-сигналы {c}")

    dual = bool(re.search(DUAL, t))
    if dual:
        b += 3; why.append("vetting = их продукт")

    if re.search(FOUNDER, t):
        # Основатель сам по себе ничего не решает. Рекрутинговый бизнес -> канал,
        # нанимающая компания -> покупатель. Когда своих сигналов нет, старая
        # метка rec-* весит больше, чем слово "founder": так рекрутеры, у которых
        # в заголовке нет слова recruiter, не уезжают в покупатели.
        if c >= 4:
            c += 2; why.append("основатель рекрутингового бизнеса")
        elif b >= 3:
            b += 3; why.append("основатель нанимающей компании")
        elif seg.startswith("rec-") or seg == "partner":
            c += 3; why.append(f"основатель, старая метка {seg} -> рекрутинговый бизнес")
        else:
            b += 3; why.append("основатель, рекрутерских признаков нет")

    if b == 0 and c == 0:
        role, prior = SEG_PRIOR.get(seg, (None, 0))
        if role:
            return role, 1, f"только по старой метке {seg}"
        return "NEEDS-DATA", 0, "нет распознанных сигналов"

    role = "BUYER" if b > c else ("CHANNEL" if c > b else "NEEDS-DATA")
    if role == "NEEDS-DATA":
        why.append("сигналы поровну")
        return role, 0, "; ".join(why)
    conf = min(5, max(1, abs(b - c)))
    if dual and role == "BUYER":
        role = "BUYER+"          # покупатель и мультипликатор одновременно
    return role, conf, "; ".join(why)


def load():
    with open("crm/leads.csv", newline="", encoding="utf-8") as f:
        return [{k: v for k, v in r.items() if k} for r in csv.DictReader(f)]


def icp(r):
    v = str(r.get("icp_score") or "").strip()
    try: return int(float(v))
    except ValueError: return -1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--untouched", action="store_true",
                    help="только те, кому ни разу не писали (new/invited/connected)")
    ap.add_argument("--role", help="фильтр: BUYER, BUYER+, CHANNEL, NEEDS-DATA, OUT")
    ap.add_argument("--out", help="выгрузить CSV")
    a = ap.parse_args()

    rows = load()
    for r in rows:
        r["role"], r["conf"], r["why"] = classify(r)

    sel = rows
    if a.untouched:
        sel = [r for r in sel if (r.get("status") or "").strip() in NEVER_WRITTEN]
    if a.role:
        sel = [r for r in sel if r["role"] == a.role.upper()]

    # сводка: роль x статус
    order = ["BUYER+", "BUYER", "CHANNEL", "NEEDS-DATA", "OUT"]
    stat_order = ["new", "invited", "connected", "contacted", "replied",
                  "meeting", "client", "parked", "lost"]
    grid = collections.Counter((r["role"], (r.get("status") or "").strip()) for r in sel)
    stats = [s for s in stat_order if any(k[1] == s for k in grid)]
    w = max(len("роль"), *(len(o) for o in order))
    print(f"{'роль':<{w}}  " + "  ".join(f"{s[:9]:>9}" for s in stats) + f"  {'ВСЕГО':>7}")
    print("-" * (w + 2 + 11 * len(stats) + 9))
    for o in order:
        n = [grid.get((o, s), 0) for s in stats]
        if not sum(n): continue
        print(f"{o:<{w}}  " + "  ".join(f"{x:>9}" for x in n) + f"  {sum(n):>7}")
    print("-" * (w + 2 + 11 * len(stats) + 9))
    tot = [sum(grid.get((o, s), 0) for o in order) for s in stats]
    print(f"{'ВСЕГО':<{w}}  " + "  ".join(f"{x:>9}" for x in tot) + f"  {sum(tot):>7}")

    if a.out:
        cols = ["role", "conf", "status", "name", "headline", "company",
                "icp_segment", "icp_score", "why", "linkedin_url"]
        sel.sort(key=lambda r: (order.index(r["role"]) if r["role"] in order else 9,
                                -r["conf"], -icp(r), r.get("name") or ""))
        with open(a.out, "w", newline="", encoding="utf-8") as f:
            wr = csv.writer(f); wr.writerow(cols)
            for r in sel:
                wr.writerow([r.get(c, "") for c in cols])
        print(f"\nwritten: {a.out} ({len(sel)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
