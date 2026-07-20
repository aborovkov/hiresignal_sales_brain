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


def segment_by_url(leads: list[dict[str, str]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for row in leads:
        url = (row.get("linkedin_url") or "").strip()
        if url:
            out[url] = (row.get("icp_segment") or "unknown").strip() or "unknown"
    return out


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
    seg = segment_by_url(leads)
    for r in funnel:
        r["_segment"] = seg.get((r.get("linkedin_url") or "").strip(), "unknown")

    print(f"leads: {len(leads)}   funnel rows: {len(funnel)}")
    print_funnel(funnel)
    print_table("reply rate by opener variant", tally(funnel, lambda r: (r.get("opener_variant") or "unlabeled").strip() or "unlabeled"))
    print_table("reply rate by ICP segment", tally(funnel, lambda r: r["_segment"]))
    print_table("variant × segment", tally(funnel, lambda r: f"{(r.get('opener_variant') or '?').strip()} / {r['_segment']}"))


if __name__ == "__main__":
    main()
