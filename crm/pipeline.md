# PIPELINE.md

> How the CRM works: what lives in the Google Sheet vs. what lives in this repo, the funnel stages, and the per-account file schema.

---

# Sheet vs. Repo — the split

**Google Sheet = the live pipeline.** It is the source of truth for *movement*: which account is at which stage, when it moved, and pipeline-level rollups. Fast to update, sortable, filterable.

* Sheet ID: `1WTbK6Zmha5EttAs3m0RsbPlOXq3lh_0t-v4AdMhGQfI`

**This repo = durable account intelligence.** It is the source of truth for *depth*: what was actually said, the pains heard, objections raised, verbatim quotes, and the reasoning behind next actions. Slow-changing, high-context, feeds `brain/` and `content/`.

Rule of thumb: **if it changes every touch → Sheet. If it accumulates understanding → repo.** The account file's `status` field mirrors the Sheet stage; the Sheet never holds the qualitative detail.

---

# Funnel Stages

> These must mirror the stage column in the Sheet. Reconcile the list below with the actual Sheet values — **TODO: confirm exact Sheet stage names.**

1. **Target Identified** — fits ICP, not yet researched. (Most current leads sit here.)
2. **Researched** — account profile built, angle chosen, opener drafted.
3. **Contacted** — first message sent.
4. **Engaged** — prospect replied / conversation live.
5. **Discovery** — pain confirmed, needs/authority/timeline being mapped.
6. **Sample Delivered** — free-sample wedge run on their data.
7. **Proposal** — commercial discussion open.
8. **Won** / **Lost** — closed, with reason logged.

---

# Per-Account File Schema

One file = one account: `crm/accounts/<account-slug>.md`. Use the template in `crm/accounts/_template.md`.

Each account file holds, in order:

1. **Profile** — company, size, segment, ICP priority, ATS/stack, why they fit, known risk flags.
2. **Contact log** — dated entries: `YYYY-MM-DD | channel | gist`.
3. **Pains heard** — real pains surfaced (feeds `brain/pains.md`, anonymized).
4. **Objections** — objections raised (feeds `brain/objections.md`, anonymized).
5. **Quotes** — verbatim lines worth keeping (never leave this file un-anonymized).
6. **Status** — current stage, mirroring the Sheet.
7. **Next action** — the single next move.

---

# Anonymization Rule

Client/company/person **names live only in `crm/accounts/` and `sources/`.** Everything promoted into `brain/` or `content/` must be stripped of identifying detail. See `ops/extraction.md`.
