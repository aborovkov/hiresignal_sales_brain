#!/usr/bin/env python3
"""One-shot cleanup of the imported lead store.

Canonicalizes linkedin_url, merges rows that are the same person, and adds an
`aliases` column so a profile re-found under a different vanity URL still
matches. Ambiguous merges are reported, never applied.
"""
import csv, re, sys, unicodedata
from collections import defaultdict, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEADS = ROOT / "crm" / "leads.csv"
EVENTS = ROOT / "crm" / "events.csv"
REPORT = ROOT / "crm" / "_migration_report.md"

LOCALES = "en|ru|de|fr|es|pt|it|nl|pl|tr|uk|sv|da|no|fi|cs|ro|ja|ko|zh|ar|id|th|vi|hi|ms"

COLUMNS = ["linkedin_url","name","headline","company","role","location",
           "icp_segment","icp_segment_raw","icp_score","icp_reason","source_query",
           "found_at","status","last_touch_at","next_action","contact_file","notes",
           "msg1","msg2","aliases"]

DEPTH = {"new":0,"invited":1,"connected":2,"contacted":3,"replied":4,"meeting":5,"client":6}
TERMINAL = {"parked","lost"}


def canon(url):
    u = (url or "").strip()
    if not u:
        return ""
    u = u.split("?")[0].split("#")[0].strip().rstrip("/")
    u = re.sub(r"^https?://", "", u, flags=re.I)
    u = re.sub(r"^([a-z0-9-]{1,10}\.)?linkedin\.com", "linkedin.com", u, flags=re.I)
    u = re.sub(r"^linkedin\.com", "https://www.linkedin.com", u)
    u = re.sub(r"/(%s)$" % LOCALES, "", u, flags=re.I)
    u = u.rstrip("/")
    # lowercase only the path, percent-escapes included
    m = re.match(r"(https://www\.linkedin\.com)(/.*)$", u, flags=re.I)
    return (m.group(1) + m.group(2).lower()) if m else u


def namekey(name):
    n = unicodedata.normalize("NFKD", (name or "").strip().lower())
    n = "".join(c for c in n if not unicodedata.combining(c))
    n = re.sub(r"[^a-z0-9\s\-]", " ", n)
    return " ".join(n.split())


def distinctive(name):
    """A name safe to merge on. Two+ real tokens, no initials."""
    toks = namekey(name).split()
    if len(toks) < 2:
        return False
    return all(len(t) >= 3 for t in toks)


def sortdate(row):
    return (row.get("last_touch_at") or row.get("found_at") or "")[:10]


def pick_status(rows):
    """Chronology wins for terminal decisions; otherwise furthest along."""
    latest = max(rows, key=sortdate)
    if latest["status"] in TERMINAL:
        return latest["status"]
    live = [r for r in rows if r["status"] not in TERMINAL]
    if not live:
        return latest["status"]
    return max(live, key=lambda r: DEPTH.get(r["status"], -1))["status"]


def merge(rows):
    """Fold duplicate rows into one, losing no information."""
    rows = sorted(rows, key=sortdate)
    out = OrderedDict((c, "") for c in COLUMNS)
    for c in COLUMNS:
        for r in rows:                      # earliest non-empty wins for identity
            if (r.get(c) or "").strip():
                out[c] = r[c].strip()
                break
    for c in ("headline", "company", "role", "location", "next_action", "icp_score",
              "icp_segment", "icp_reason", "msg1", "msg2", "contact_file"):
        for r in reversed(rows):            # freshest wins for mutable facts
            if (r.get(c) or "").strip():
                out[c] = r[c].strip()
                break
    out["linkedin_url"] = canon(rows[0]["linkedin_url"])
    out["status"] = pick_status(rows)
    out["found_at"] = min((r.get("found_at") or "")[:10] for r in rows if r.get("found_at")) or ""
    out["last_touch_at"] = max((r.get("last_touch_at") or "")[:10] for r in rows if r.get("last_touch_at")) or ""
    notes = []
    for r in rows:
        for part in (r.get("notes") or "").split(" | "):
            if part.strip() and part.strip() not in notes:
                notes.append(part.strip())
    out["notes"] = " | ".join(notes)
    aliases = []
    for r in rows:
        c = canon(r["linkedin_url"])
        raw = (r["linkedin_url"] or "").strip()
        for u in (c, raw):
            if u and u != out["linkedin_url"] and u not in aliases:
                aliases.append(u)
    out["aliases"] = " | ".join(aliases)
    return out


def main():
    src = list(csv.DictReader(LEADS.open(encoding="utf-8")))
    src = [r for r in src if (r.get("linkedin_url") or "").strip()]

    # pass 1 - group by canonical URL
    by_url = defaultdict(list)
    for r in src:
        by_url[canon(r["linkedin_url"])].append(r)
    url_merges = {u: rs for u, rs in by_url.items() if len(rs) > 1}

    # pass 2 - group by distinctive name across different URLs
    staged = {u: (merge(rs) if len(rs) > 1 else rs[0]) for u, rs in by_url.items()}
    by_name = defaultdict(list)
    for u, r in staged.items():
        if distinctive(r.get("name", "")):
            by_name[namekey(r["name"])].append(r)
    name_merges = {n: rs for n, rs in by_name.items() if len(rs) > 1}
    ambiguous = []
    seen_names = defaultdict(list)
    for u, r in staged.items():
        nk = namekey(r.get("name", ""))
        if nk and not distinctive(r.get("name", "")):
            seen_names[nk].append(r)
    for nk, rs in seen_names.items():
        if len(rs) > 1:
            ambiguous.append(rs)

    final = {}
    merged_away = set()
    for nk, rs in name_merges.items():
        m = merge(rs)
        final[m["linkedin_url"]] = m
        for r in rs:
            merged_away.add(canon(r["linkedin_url"]))
    for u, r in staged.items():
        if u in merged_away:
            continue
        row = dict(r)
        row.setdefault("aliases", row.get("aliases", ""))
        row["linkedin_url"] = u
        final.setdefault(u, {c: (row.get(c) or "").strip() for c in COLUMNS})

    rows = sorted(final.values(), key=lambda r: (r.get("found_at") or "", r.get("name") or ""))
    with LEADS.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    # rewrite event urls to canonical so they still join
    ev = list(csv.reader(EVENTS.open(encoding="utf-8")))
    head, body = ev[0][:9], [r for r in ev[1:] if any(x.strip() for x in r)]
    for r in body:
        if len(r) > 1:
            r[1] = canon(r[1])
    with EVENTS.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(r[:9] for r in body)

    nameless = [r for r in rows if not (r.get("name") or "").strip()]
    lines = ["# Migration report", "",
             f"Source rows: {len(src)}", f"Rows after merge: {len(rows)}",
             f"People folded together: {len(src) - len(rows)}", "",
             "## Merged on identical canonical URL", ""]
    for u, rs in sorted(url_merges.items()):
        lines.append(f"- `{u}` <- " + ", ".join(f"`{r['linkedin_url']}` ({r['status']})" for r in rs))
    lines += ["", "## Merged on matching name across different URLs", ""]
    for nk, rs in sorted(name_merges.items()):
        lines.append(f"- **{rs[0]['name']}** -> `{merge(rs)['status']}` <- " +
                     ", ".join(f"`{canon(r['linkedin_url'])}` ({r['status']})" for r in rs))
    lines += ["", "## Left alone - name too ambiguous to merge automatically", ""]
    for rs in ambiguous:
        lines.append(f"- **{rs[0]['name']}**: " +
                     ", ".join(f"`{canon(r['linkedin_url'])}` ({r['status']})" for r in rs))
    lines += ["", f"## Rows with no name: {len(nameless)}", "",
              "These cannot be matched by name, so a vanity-URL change makes them",
              "invisible to dedupe. Worth backfilling from LinkedIn.", ""]
    for r in nameless[:40]:
        lines.append(f"- `{r['linkedin_url']}` ({r['status']})")
    if len(nameless) > 40:
        lines.append(f"- ... and {len(nameless) - 40} more")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"rows in:  {len(src)}")
    print(f"rows out: {len(rows)}")
    print(f"merged:   {len(src) - len(rows)}")
    print(f"url-merge groups: {len(url_merges)}, name-merge groups: {len(name_merges)}, ambiguous: {len(ambiguous)}")
    print(f"nameless rows: {len(nameless)}")
    print(f"events rewritten: {len(body)}")


if __name__ == "__main__":
    main()
