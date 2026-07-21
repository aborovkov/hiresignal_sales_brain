#!/usr/bin/env python3
"""Log a sent outreach batch into crm/outreach_funnel.csv.

Fixes the survivorship hole: the sidecar historically only got rows for people who
replied, so every reply-rate came out 100%. This writes one row per lead AT SEND TIME
with a blank reply_class, which the report treats as no_reply until a reply lands.

Run after each hand-sent batch from crm/reports/today_send_queue_<date>.md:

    python3 scripts/log_sent.py --variant C              # log the whole C batch
    python3 scripts/log_sent.py --variant A2 --only 12   # log just the first 12 of A2
    python3 scripts/log_sent.py --variant C --dry-run

Already-logged URLs are skipped, so re-running after a partial send is safe.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FUNNEL = REPO / "crm" / "outreach_funnel.csv"
QUEUE = REPO / "crm" / "reports" / "send_queue_2026-07-21.json"

VARIANT_LABEL = {"C": "C_cv_callback", "A2": "A2_volume_refresh"}

COLUMNS = [
    "linkedin_url", "stage", "opener_variant", "connect_sent_at", "connect_accepted_at",
    "opener_sent_at", "replied_at", "reply_class", "won_at", "dead_at", "notes",
]


def load_queue() -> list[dict]:
    if not QUEUE.exists():
        sys.exit(f"missing {QUEUE.relative_to(REPO)} - regenerate the send queue first")
    return json.loads(QUEUE.read_text(encoding="utf-8"))


def load_funnel() -> list[dict]:
    if not FUNNEL.exists():
        return []
    with FUNNEL.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", required=True, choices=sorted(VARIANT_LABEL))
    ap.add_argument("--only", type=int, help="log only the first N of this variant")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    batch = [lead for lead in load_queue() if lead["variant"] == args.variant]
    if args.only:
        batch = batch[: args.only]
    if not batch:
        sys.exit(f"no leads for variant {args.variant}")

    existing = load_funnel()
    seen = {(r.get("linkedin_url") or "").strip().lower() for r in existing}

    new_rows, skipped = [], 0
    for lead in batch:
        url = lead["linkedin_url"] if "linkedin_url" in lead else lead["url"]
        if url.strip().lower() in seen:
            skipped += 1
            continue
        new_rows.append({
            "linkedin_url": url,
            "stage": "opener_sent",
            "opener_variant": VARIANT_LABEL[args.variant],
            "connect_sent_at": "",
            "connect_accepted_at": "",
            "opener_sent_at": args.date,
            "replied_at": "",
            "reply_class": "",
            "won_at": "",
            "dead_at": "",
            "notes": f"{lead['name']} ({lead['company']}); accepted-invite reactivation batch {args.date}",
        })
        seen.add(url.strip().lower())

    print(f"variant {args.variant}: {len(new_rows)} to log, {skipped} already present")
    if args.dry_run:
        for r in new_rows:
            print("  would log:", r["linkedin_url"], "|", r["notes"])
        return

    with FUNNEL.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        for r in existing:
            w.writerow({c: r.get(c, "") for c in COLUMNS})
        w.writerows(new_rows)
    print(f"wrote {len(new_rows)} rows to {FUNNEL.relative_to(REPO)} (total {len(existing) + len(new_rows)})")


if __name__ == "__main__":
    main()
