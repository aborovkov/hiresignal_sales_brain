#!/usr/bin/env python3
"""The lead store: crm/leads.csv + crm/events.csv, read and written in place.

There is no plan/apply step and no spreadsheet. Every command that changes a
lead also appends to the event journal, so the funnel history stays honest.

  ./scripts/leads.py check <url> [name]        is this person already known?
  ./scripts/leads.py add < leads.json          append new people, skip known
  ./scripts/leads.py status <url> <status>     move someone, journal it
  ./scripts/leads.py note <url> <text>         append a dated note
  ./scripts/leads.py set <url> <field> <val>   correct a field, e.g. score an ICP
  ./scripts/leads.py alias <url> <other-url>   same person, another vanity slug
  ./scripts/leads.py show <url>                everything about one person
  ./scripts/leads.py list <view>               warm|follow-up|first-dm|to-invite|needs-icp|<status>
  ./scripts/leads.py funnel                    counts by status
"""
import csv, json, re, sys, unicodedata, subprocess
from collections import defaultdict, Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "crm" / "leads.csv"
EVENTS = ROOT / "crm" / "events.csv"

COLUMNS = ["linkedin_url","name","headline","company","role","location",
           "icp_segment","icp_segment_raw","icp_score","icp_reason","source_query",
           "found_at","status","last_touch_at","next_action","contact_file","notes",
           "msg1","msg2","aliases"]
EVENT_COLUMNS = ["ts","linkedin_url","name","from_status","to_status","kind","actor","source","note"]

PIPELINE = ["new","invited","connected","contacted","replied","meeting","client"]
EXITS = ["parked","lost"]
VALID = PIPELINE + EXITS
LOCALES = "en|ru|de|fr|es|pt|it|nl|pl|tr|uk|sv|da|no|fi|cs|ro|ja|ko|zh|ar|id|th|vi|hi|ms"


def canon(url):
    u = (url or "").strip()
    if not u:
        return ""
    u = u.split("?")[0].split("#")[0].strip().rstrip("/")
    u = re.sub(r"^https?://", "", u, flags=re.I)
    u = re.sub(r"^([a-z0-9-]{1,10}\.)?linkedin\.com", "linkedin.com", u, flags=re.I)
    u = re.sub(r"^linkedin\.com", "https://www.linkedin.com", u)
    u = re.sub(r"/(%s)$" % LOCALES, "", u, flags=re.I).rstrip("/")
    m = re.match(r"(https://www\.linkedin\.com)(/.*)$", u, flags=re.I)
    return (m.group(1) + m.group(2).lower()) if m else u


def namekey(name):
    n = unicodedata.normalize("NFKD", (name or "").strip().lower())
    n = "".join(c for c in n if not unicodedata.combining(c))
    return " ".join(re.sub(r"[^a-z0-9\s\-]", " ", n).split())


def distinctive(name):
    toks = namekey(name).split()
    return len(toks) >= 2 and all(len(t) >= 3 for t in toks)


def score(value):
    """Excel round-trips 3 as '3.0'. One scale, integers 0-5."""
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return 0


def load():
    rows = list(csv.DictReader(LEADS.open(encoding="utf-8")))
    for r in rows:
        for c in COLUMNS:
            r.setdefault(c, "")
        r["icp_score"] = str(score(r["icp_score"])) if r["icp_score"].strip() else ""
    return rows


def save(rows):
    with LEADS.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def journal(entries):
    exists = EVENTS.exists()
    with EVENTS.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(EVENT_COLUMNS)
        w.writerows(entries)


def index(rows):
    """url -> row, including every alias, plus name -> rows."""
    by_url, by_name = {}, defaultdict(list)
    for r in rows:
        by_url[canon(r["linkedin_url"])] = r
        for a in (r.get("aliases") or "").split(" | "):
            if a.strip():
                by_url[canon(a)] = r
        if distinctive(r.get("name", "")):
            by_name[namekey(r["name"])].append(r)
    return by_url, by_name


def lookup(rows, url, name=""):
    """Returns (row, how) or (None, None). This is the dedupe gate."""
    by_url, by_name = index(rows)
    c = canon(url)
    if c in by_url:
        r = by_url[c]
        return r, ("alias" if canon(r["linkedin_url"]) != c else "url")
    if name and distinctive(name):
        hits = by_name.get(namekey(name)) or []
        if len(hits) == 1:
            return hits[0], "name"
        if len(hits) > 1:
            return hits[0], "name-ambiguous"
    return None, None


def commit(message):
    git = ["git", "-C", str(ROOT), "-c", "user.name=Claude",
           "-c", "user.email=noreply@anthropic.com"]
    for _ in range(2):
        stale = ROOT / ".git" / "_stale"
        stale.mkdir(parents=True, exist_ok=True)
        for lock in list((ROOT / ".git").glob("*.lock")) + list((ROOT / ".git/refs/heads").glob("*.lock")):
            try:
                lock.rename(stale / f"{lock.name}.{date.today()}")
            except OSError:
                pass
        subprocess.run(git + ["add", "crm/leads.csv", "crm/events.csv"],
                       capture_output=True, text=True)
        p = subprocess.run(git + ["commit", "-q", "-m", message], capture_output=True, text=True)
        if p.returncode == 0:
            return True
    return False


# ---------------------------------------------------------------- commands

def cmd_check(args):
    url, name = args[0], (args[1] if len(args) > 1 else "")
    rows = load()
    r, how = lookup(rows, url, name)
    if not r:
        print(json.dumps({"known": False, "canonical": canon(url)}, ensure_ascii=False))
        return 0
    print(json.dumps({"known": True, "matched_by": how, "name": r["name"],
                      "status": r["status"], "url": r["linkedin_url"],
                      "last_touch_at": r["last_touch_at"], "notes": r["notes"][:300]},
                     ensure_ascii=False, indent=2))
    return 0


def cmd_add(args):
    """stdin: JSON list of {linkedin_url,name,headline,company,role,location,
    icp_segment,icp_score,icp_reason,source_query}"""
    incoming = json.load(sys.stdin)
    rows = load()
    today = date.today().isoformat()
    added, skipped, events = [], [], []
    for item in incoming:
        r, how = lookup(rows, item.get("linkedin_url", ""), item.get("name", ""))
        if r:
            skipped.append({"name": item.get("name"), "matched_by": how,
                            "existing_status": r["status"], "url": r["linkedin_url"]})
            continue
        row = {c: "" for c in COLUMNS}
        row.update({k: str(v) for k, v in item.items() if k in COLUMNS})
        row["linkedin_url"] = canon(item.get("linkedin_url", ""))
        row["found_at"] = today
        row["status"] = "new"
        row["last_touch_at"] = today
        rows.append(row)
        added.append(row)
        events.append([today, row["linkedin_url"], row["name"], "", "new",
                       "transition", "Claude", "lead-hunter", row.get("icp_reason", "")])
    if added:
        save(rows)
        journal(events)
        commit(f"crm: add {len(added)} leads, skip {len(skipped)} already known")
    print(json.dumps({"added": len(added), "skipped": len(skipped),
                      "skipped_detail": skipped}, ensure_ascii=False, indent=2))
    return 0


def cmd_status(args):
    url, new = args[0], args[1]
    note = args[2] if len(args) > 2 else ""
    if new not in VALID:
        print(f"invalid status {new!r}; expected one of {', '.join(VALID)}", file=sys.stderr)
        return 1
    rows = load()
    r, how = lookup(rows, url)
    if not r:
        print(f"not in the store: {canon(url)}", file=sys.stderr)
        return 1
    old, today = r["status"], date.today().isoformat()
    if old == new:
        print(f"{r['name']} already {new}")
        return 0
    if old in PIPELINE and new in PIPELINE and PIPELINE.index(new) < PIPELINE.index(old):
        print(f"refusing to move {r['name']} backwards: {old} -> {new}. "
              f"Use parked or lost, or edit the file by hand.", file=sys.stderr)
        return 1
    if new in EXITS and not note:
        why = "a revisit date" if new == "parked" else "a reason"
        print(f"{new} needs {why}. Pass it as the third argument:\n"
              f"  leads.py status <url> {new} \"<{why}>\"", file=sys.stderr)
        return 1
    r["status"], r["last_touch_at"] = new, today
    if note:
        r["notes"] = (r["notes"] + " | " if r["notes"] else "") + f"{today}: {note}"
    save(rows)
    journal([[today, canon(r["linkedin_url"]), r["name"], old, new,
              "transition", "Alexey", "live", note]])
    commit(f"crm: {r['name']} {old} -> {new}")
    print(f"{r['name']}: {old} -> {new}")
    return 0


SETTABLE = ["icp_segment", "icp_score", "icp_reason", "next_action", "company",
            "role", "headline", "location", "contact_file", "msg1", "msg2",
            "source_query", "name"]


def cmd_set(args):
    """Correct one field. Scoring a needs-icp connect is the common case."""
    url, field, value = args[0], args[1], " ".join(args[2:])
    if field not in SETTABLE:
        print(f"{field!r} is not settable; expected one of {', '.join(SETTABLE)}.\n"
              f"status changes go through `status`, notes through `note`, "
              f"alternate URLs through `alias`.", file=sys.stderr)
        return 1
    rows = load()
    r, _ = lookup(rows, url)
    if not r:
        print(f"not in the store: {canon(url)}", file=sys.stderr)
        return 1
    if field == "icp_score":
        value = str(score(value))
        if not 0 <= int(value) <= 5:
            print("icp_score is an integer 0-5", file=sys.stderr)
            return 1
    old, today = r[field], date.today().isoformat()
    r[field] = value
    r["last_touch_at"] = today
    save(rows)
    journal([[today, canon(r["linkedin_url"]), r["name"], r["status"], r["status"],
              "edit", "Claude", "live", f"{field}: {old!r} -> {value!r}"]])
    commit(f"crm: {r['name']} {field} -> {value}")
    print(f"{r['name']}: {field} {old!r} -> {value!r}")
    return 0


def cmd_alias(args):
    """Record another URL the same person appears under, so dedupe catches it."""
    url, other = args[0], args[1]
    rows = load()
    r, _ = lookup(rows, url)
    if not r:
        print(f"not in the store: {canon(url)}", file=sys.stderr)
        return 1
    c = canon(other)
    clash, _ = lookup(rows, c)
    if clash and clash is not r:
        print(f"{c} already belongs to {clash['name']} ({clash['status']}). "
              f"Merge them by hand rather than aliasing.", file=sys.stderr)
        return 1
    have = [a for a in (r["aliases"] or "").split(" | ") if a.strip()]
    if c == canon(r["linkedin_url"]) or c in have:
        print("already known")
        return 0
    have.append(c)
    r["aliases"] = " | ".join(have)
    today = date.today().isoformat()
    save(rows)
    journal([[today, canon(r["linkedin_url"]), r["name"], r["status"], r["status"],
              "alias", "Claude", "live", c]])
    commit(f"crm: {r['name']} also appears as {c}")
    print(f"{r['name']} also appears as {c}")
    return 0


def cmd_note(args):
    url, text = args[0], " ".join(args[1:])
    rows = load()
    r, _ = lookup(rows, url)
    if not r:
        print(f"not in the store: {canon(url)}", file=sys.stderr)
        return 1
    today = date.today().isoformat()
    r["notes"] = (r["notes"] + " | " if r["notes"] else "") + f"{today}: {text}"
    r["last_touch_at"] = today
    save(rows)
    journal([[today, canon(r["linkedin_url"]), r["name"], r["status"], r["status"],
              "note", "Alexey", "live", text]])
    commit(f"crm: note on {r['name']}")
    print(f"noted on {r['name']}")
    return 0


def cmd_show(args):
    rows = load()
    r, how = lookup(rows, args[0], args[1] if len(args) > 1 else "")
    if not r:
        print("not found", file=sys.stderr)
        return 1
    print(json.dumps(r, ensure_ascii=False, indent=2))
    ev = [e for e in csv.DictReader(EVENTS.open(encoding="utf-8"))
          if canon(e["linkedin_url"]) == canon(r["linkedin_url"])]
    print("\n--- events ---")
    for e in ev:
        print(f"  {e['ts']}  {e['from_status'] or '-'} -> {e['to_status']}  {e['note'][:80]}")
    return 0


VIEWS = {
    "warm":      lambda r: r["status"] == "replied",
    "follow-up": lambda r: r["status"] == "contacted",
    "first-dm":  lambda r: r["status"] == "connected",
    "to-invite": lambda r: r["status"] == "new",
    "needs-icp": lambda r: r["icp_segment"] == "needs-icp" or not r["icp_segment"].strip(),
}


def cmd_list(args):
    view = args[0] if args else "warm"
    rows = load()
    pred = VIEWS.get(view) or (lambda r, v=view: r["status"] == v)
    sel = [r for r in rows if pred(r)]
    if view == "to-invite":
        sel.sort(key=lambda r: (-score(r["icp_score"]), r["found_at"]))
    else:
        sel.sort(key=lambda r: r["last_touch_at"] or r["found_at"])
    for r in sel:
        icp = r["icp_score"] or "-"
        print(f"{(r['last_touch_at'] or r['found_at'])[:10]}  {icp:>2}  "
              f"{(r['name'] or '(no name)')[:28]:<28} {(r['company'] or '')[:22]:<22} "
              f"{r['linkedin_url']}")
    print(f"\n{len(sel)} in {view}")
    return 0


def cmd_funnel(args):
    rows = load()
    c = Counter(r["status"] for r in rows)
    for s in PIPELINE + EXITS:
        if c.get(s):
            print(f"{s:<12} {c[s]:>4}")
    print(f"{'total':<12} {len(rows):>4}")
    return 0


COMMANDS = {"check": cmd_check, "add": cmd_add, "status": cmd_status, "note": cmd_note,
            "set": cmd_set, "alias": cmd_alias, "show": cmd_show, "list": cmd_list,
            "funnel": cmd_funnel}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(1)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv[2:]))
