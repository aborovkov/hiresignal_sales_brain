# stats_raw/ — messy capture drop zone

> Mirrors `sources/` for the content engine: **capture messy, normalize later.**

Because `linkedin-thread-monitor` and `linkedin-engager-analytics` aren't installed (see `pillars.md`), stats collection is manual. Dump raw numbers here the moment you have them — don't stop to format.

## What lands here

* Screenshots: `YYYY-MM-DD__<slug>__stats.png`
* Text / running files: paste whatever LinkedIn shows (impressions, reactions, comments, profile views, DMs).

## The flow

1. **Capture** — drop the screenshot or raw text here, named by date + slug.
2. **Messy is fine** — no schema, no cleanup at capture time.
3. **Normalize later** — during the weekly pass, transcribe into one clean row per post in `../post_log.md` (with T+48h / T+14d checkpoints), then the raw file can stay as the audit trail.

Never promote identifying detail into `brain/` or `content/*.md`. Raw stats about our own posts are fine here.
