# CLAUDE.md

> Read this first. It routes you to the right layer. This repo is the HireSignal sales brain + light CRM + content machine.

---

# Layers

```
brain/      What we know & how we sound. The durable intelligence.
sources/    Raw call transcripts & notes (may contain names).
crm/        Per-account intelligence + working action list. Names allowed here.
content/    LinkedIn content pipeline: pillars → ideas → drafts → published → log.
ops/        The engines: how transcripts become assets, how we run sales.
```

## brain/ — strategy, voice, knowledge

* `positioning.md` — what HireSignal is, market thesis, differentiation, **core beliefs**. Strategy layer.
* `icp.md` — who we sell to (priority-ordered).
* `voice.md` — tone, **banned/preferred vocabulary**, sentence craft, CTA style, LinkedIn writing rules.
* `pains.md` — operational pains (deep). `signals.md` — interview signal taxonomy.
* `objections.md` — objection handling.
* `competitors.md` — competitor cards + battlecards. Maps named competitors onto `positioning.md`; anticipated objections live here until a real prospect raises one, then they move to `objections.md`.
* `outreach.md` — opener patterns, conversation arc, soft-CTA/short-response libraries.
* `proof.md` — ⚠️ **CRITICAL, mostly TODO.** Credibility anchor, cases, metrics.
* `offer.md` — ⚠️ **TODO.** What we sell, pricing, free-sample wedge.

## crm/

* `pipeline.md` — how the CRM works, funnel stages, per-account schema.
* **Live pipeline is the "leads" Google Sheet** (`1T5tG05WGGpwjyR05Z-Xu4vDe1knlBY_IVOdBT3MiQjg`), one row per person keyed by LinkedIn URL - the single source of truth for lead status and movement. There is no `crm/leads.csv` any more (removed 2026-08-03). Claude works against a local cache of it (`leads.csv` + `events.csv`) and never writes the Sheet itself - see the write path below.
* `accounts/<slug>.md` — one file per account (use `accounts/_template.md`).
* `_next_actions.md` — who to contact / reply to next.

## sources/

* `_index.md` — transcript registry. Files: `calls/`, `notes/`. Naming: `YYYY-MM-DD__<account-slug>__<type>.md`.

## content/

* `pillars.md` → `ideas.md` → `drafts/` → `published/` → `post_log.md`.
* `amplification.md` — the 4-stage distribution cycle (source → hijack → reframe → hand-off) every post goes through; plan stages 2-4 at draft time.
* `links.md` — external links worth keeping: competitor pages, articles, tools, own posts that performed. Links only, analysis links out to `brain/`.

## ops/

* `extraction.md` — transcript → CRM + brain + content engine (**stub, Task 3**).
* `sales_process.md` — how to run outreach & first calls.

---

# Conventions

* **Live pipeline is the "leads" Google Sheet** (`1T5tG05WGGpwjyR05Z-Xu4vDe1knlBY_IVOdBT3MiQjg`) - the single source of truth for lead status and movement. The old `crm/leads.csv` was **removed on 2026-08-03** - do not recreate it as a store. The separate "(StepUP) Data Room навигация" Sheet (`1WTbK6Zmha5EttAs3m0RsbPlOXq3lh_0t-v4AdMhGQfI`) stays **retired** - never read it for leads. See `crm/pipeline.md`.
* **The write path: local cache by day, one handoff a day.** Claude NEVER writes the leads Sheet - not through the browser, not through a connector, not one cell. It exports the workbook (xlsx, which carries both tabs) into a local pair `leads.csv` + `events.csv`, makes every change there via a `sheet_writer.py` plan + `scripts/apply_plan.py` (which verifies row identity against `expect_url` and aborts on a mismatch), and once a day hands both files back for **the human to paste into the Sheet**. Always hand the pair together - `leads.csv` without `events.csv` breaks the cohort funnel. The `text/csv` export only ever returns the first tab, so it can never reach `events`; use xlsx. Browser automation stays allowed for LinkedIn, never for the Sheet.
* **Anonymization:** names live only in `crm/` and `sources/`. Never promote identifying detail into `brain/` or `content/`.
* **One fact, one home.** If two files would state the same thing, one owns it and the other links. Canonical outreach opener lives only in `brain/outreach.md`.
* Content voice is governed by `brain/voice.md`. Content flows via `/linkedin-post-writer` → `/linkedin-humanizer` audit → Publora (Tue–Thu, 07:30–09:00 Tbilisi).

---

# Open question

**Is HireSignal a rebrand of StepUp, or a separate service play?** This decides the content of `brain/proof.md` and `brain/offer.md` (whether StepUp product metrics can be cited directly). Structure is unaffected either way.
