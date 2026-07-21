#!/usr/bin/env python3
"""Reply-rate report for the outreach funnel.

Joins crm/leads.csv (master, for icp_segment) with crm/outreach_funnel.csv (sidecar,
for stage + variant + outcomes) on linkedin_url, then answers the two questions that
drive text optimization:

  1. Which opener variant converts best? (reply rate + positive rate + won rate)
  2. Which ICP segments respond? (same metrics sliced by icp_segment)

No network, no LinkedIn, no external deps. Read-only. Run:
    python3 scripts/funnel_report.py
"""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEADS = REPO / "crm" / "leads.csv"
FUNNEL = REPO / "crm" / "outreach_funnel.csv"

# a reply_class counts as "replied" for reply-rate; blank/no_reply does not
REPLIED_CLASSES = {"positive", "neutral", "decline"}


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        sys.exit(f"missing {path.relative_to(REPO)}")
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def normalize_url(url: str) -> str:
    """Mirror leads.py normalize_url so both files key the same way."""
    url = (url or "").strip().split("?")[0].rstrip("/")
    if url.startswith("http://"):
        url = "https://" + url[len("http://") :]
    if url.startswith("https://linkedin.com"):
        url = "https://www." + url[len("https://") :]
    return url.lower()


def slug_of(url: str) -> str:
    """Last path segment of a /in/ URL, lowercased. '' when not a profile URL."""
    url = normalize_url(url)
    return url.rsplit("/in/", 1)[1] if "/in/" in url else ""


def segment_index(leads: list[dict[str, str]]) -> tuple[dict[str, str], list[str]]:
    """Return (lookup, profile_slugs).

    lookup maps every key a sidecar row might use to an icp_segment:
      - the normalized profile URL
      - 'account:<name>' derived from the contact_file column
    profile_slugs backs the prefix match for truncated LinkedIn URNs.
    """
    lookup: dict[str, str] = {}
    slugs: list[str] = []
    for row in leads:
        seg = (row.get("icp_segment") or "unknown").strip() or "unknown"
        url = normalize_url(row.get("linkedin_url") or "")
        if url:
            lookup[url] = seg
            slug = slug_of(url)
            if slug:
                slugs.append(slug)
                lookup[f"slug:{slug}"] = seg
        contact = (row.get("contact_file") or "").strip()
        if contact:
            stem = Path(contact).stem.lower()
            if stem:
                lookup[f"account:{stem}"] = seg
    return lookup, slugs


def resolve_segment(key: str, lookup: dict[str, str], slugs: list[str]) -> str | None:
    """Resolve a sidecar linkedin_url to an icp_segment, or None if unmatched."""
    key = (key or "").strip()
    if not key:
        return None
    if key.lower().startswith("account:"):
        return lookup.get(key.lower())
    url = normalize_url(key)
    if url in lookup:
        return lookup[url]
    # LinkedIn URNs get truncated by hand-editing; match on a shared prefix.
    slug = slug_of(url)
    if slug:
        hits = {s for s in slugs if s.startswith(slug) or slug.startswith(s)}
        if len(hits) == 1:
            return lookup.get(f"slug:{hits.pop()}")
    return None


def pct(num: int, den: int) -> str:
    return f"{(100 * num / den):.0f}%" if den else "—"


def tally(rows: list[dict[str, str]], key_fn) -> dict:
    agg = defaultdict(lambda: {"opener_sent": 0, "replied": 0, "positive": 0, "won": 0})
    for r in rows:
        if not (r.get("opener_sent_at") or "").strip():
            continue  # only openers can have a reply rate
        bucket = agg[key_fn(r)]
        bucket["opener_sent"] += 1
        rc = (r.get("reply_class") or "").strip().lower()
        if rc in REPLIED_CLASSES:
            bucket["replied"] += 1
        if rc == "positive":
            bucket["positive"] += 1
        if (r.get("won_at") or "").strip() or (r.get("stage") or "").strip() == "won":
            bucket["won"] += 1
    return agg


def print_table(title: str, agg: dict) -> None:
    print(f"\n=== {title} ===")
    if not agg:
        print("  (no opener_sent rows yet — populate crm/outreach_funnel.csv)")
        return
    header = f"{'bucket':<28}{'sent':>6}{'reply%':>8}{'pos%':>7}{'won%':>7}"
    print(header)
    print("-" * len(header))
    rows = sorted(agg.items(), key=lambda kv: (-kv[1]["opener_sent"], kv[0]))
    for name, b in rows:
        sent = b["opener_sent"]
        print(
            f"{name[:27]:<28}{sent:>6}"
            f"{pct(b['replied'], sent):>8}"
            f"{pct(b['positive'], sent):>7}"
            f"{pct(b['won'], sent):>7}"
        )


def print_funnel(rows: list[dict[str, str]]) -> None:
    order = ["connect_sent", "connect_accepted", "opener_sent", "replied", "won", "dead"]
    counts = defaultdict(int)
    for r in rows:
        for col, stage in (
            ("connect_sent_at", "connect_sent"),
            ("connect_accepted_at", "connect_accepted"),
            ("opener_sent_at", "opener_sent"),
            ("replied_at", "replied"),
            ("won_at", "won"),
            ("dead_at", "dead"),
        ):
            if (r.get(col) or "").strip():
                counts[stage] += 1
    print("\n=== funnel (cumulative reach) ===")
    for stage in order:
        print(f"  {stage:<20}{counts[stage]:>5}")


def main() -> None:
    leads = load_csv(LEADS)
    funnel = load_csv(FUNNEL)
    lookup, slugs = segment_index(leads)
    unmatched: list[str] = []
    for r in funnel:
        key = (r.get("linkedin_url") or "").strip()
        seg = resolve_segment(key, lookup, slugs)
        if seg is None:
            unmatched.append(key or "(blank key)")
            seg = "unmatched"
        r["_segment"] = seg

    print(f"leads: {len(leads)}   funnel rows: {len(funnel)}")
    if unmatched:
        print(
            f"\n!! {len(unmatched)} funnel row(s) not joined to leads.csv "
            f"- these are invisible to leads.csv status and to funnel.py:"
        )
        for key in unmatched:
            print(f"   {key}")
    print_funnel(funnel)
    print_table("reply rate by opener variant", tally(funnel, lambda r: (r.get("opener_variant") or "unlabeled").strip() or "unlabeled"))
    print_table("reply rate by ICP segment", tally(funnel, lambda r: r["_segment"]))
    print_table("variant × segment", tally(funnel, lambda r: f"{(r.get('opener_variant') or '?').strip()} / {r['_segment']}"))


if __name__ == "__main__":
    main()
