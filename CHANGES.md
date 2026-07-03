# CHANGES.md — Task 1, 2 & 2b migration

Refactor of the flat 13-file repo into layered `brain / sources / crm / content / ops`. Tasks 3–4 not executed (need real transcripts).

## Task 1 — deduplication (merges)

* **`brain/positioning.md`** ← `positioning.md` + `sales_brain.md` + `founder_beliefs.md`. All 20 founder beliefs preserved as the "Core Beliefs" section. Duplicate market-shift / never-position / problem statements collapsed to one.
* **`brain/voice.md`** (new) ← `style.md` + `writting_guidelines.md` (typo in filename dropped). Now the single home for tone + **all banned/preferred vocabulary** (previously scattered across 4 files).
* **`brain/outreach.md`** (new) ← `outreach_library.md` + `conversation_patterns.md`. Holds the **single canonical** cold opener — it appears exactly once repo-wide (grep = 1, in this file only). CTA phrase bank + short-response library consolidated here.
* Moved unchanged: `icp.md`, `signals.md`, `objections.md`.
* `pains.md`: moved, one line reworded so it no longer restates the canonical opener (points to `outreach.md`).
* Deleted: empty `init`.

### Consolidation judgment calls (reversible — flag if you disagree)
* **Vocabulary/banned-language** lists lived in 4 files; now owned solely by `voice.md`.
* **`sales_brain.md` "Ideal Customers"** (per-persona pain one-liners) was dropped rather than relocated — judged already covered by `icp.md` + `pains.md`. If you want the persona framing kept, it should move into `icp.md`.
* "Response Cadence" heading → folded into `outreach.md` "Short Response Library" (content intact).

## Task 2 — structure + CRM

* New tree: `brain/`, `sources/{calls,notes}/`, `crm/accounts/`, `content/{drafts,published}/`, `ops/`.
* New stubs: `brain/proof.md` ⚠️, `brain/offer.md` ⚠️, `crm/pipeline.md`, `crm/_next_actions.md`, `crm/accounts/_template.md`, `sources/_index.md`, `content/{pillars,ideas,post_log}.md`, `ops/extraction.md` (stub for Task 3).
* `sales_prep_outreach_first_call.md` → **adapted** to `ops/sales_process.md` (HireSignal-specific; generic Notion/Stripe examples removed).
* `CLAUDE.md` created as the entry-point router.

## Task 2b — content layer (skill-vocabulary refinement)
Reworked `content/` to speak the installed LinkedIn skills' language so its stats are legible, not noise.
* **`content/pillars.md`** rewritten to the `linkedin-content-planner` 3-pillar discipline — Authority 40–50% / Personal Narrative 30–40% / Community 20–30% / Product ≤10–15% (max 1/wk). Pains/signals themes demoted from "pillars" to the **Authority topic bank**. Added formula→pillar mapping (F1–F10 from `linkedin-post-writer`) and cadence rules (3–5 posts/wk, one format per pillar per week, 10–20 comments/day, Tue–Thu 07:30–09:00 Tbilisi).
* **`content/post_log.md`** rewritten: Hook column = formula code `F1`–`F10`, plus pillar + format (text|carousel|poll) + impressions/reactions/comments/inbound. Two measurement checkpoints per post (**T+48h**, **T+14d**). Added a separate **comments-engine table** (comments made / author replies / profile views / inbound-from-comments). **North star = inbound**, not reactions.
* **`content/stats_raw/`** added (mirrors `sources/`) with `_README.md` — capture-messy-normalize-later drop zone for screenshots (`YYYY-MM-DD__<slug>__stats.png`) and raw text.
* **Tooling gap flagged** (in `pillars.md` + `stats_raw/_README.md`): `linkedin-thread-monitor` and `linkedin-engager-analytics` are referenced by `linkedin-content-planner` but **not installed** → stats collection is manual for now.

## Resolved open question
**HireSignal is NOT a rebrand of StepUp** — it stands as its own positioning. Consequence: the Turing anchor (1,700+ interviews / 28 countries) is a shared, valid credibility anchor and is filled in `proof.md`. StepUp product metrics are **not** cited as HireSignal's own without explicit attribution — product-specific metrics remain TODO in `proof.md` + `offer.md`.

## Not executed (out of scope — need real inputs)
* **Task 3** (`ops/extraction.md`) — stub only; needs a real call transcript.
* **Task 4** — content finalization; needs a first published post + stats.
