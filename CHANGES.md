# CHANGES.md — Task 1 & 2 migration

Refactor of the flat 13-file repo into layered `brain / sources / crm / content / ops`. Tasks 3–4 not executed (need real transcripts).

## Task 1 — deduplication (merges)

* **`brain/positioning.md`** ← `positioning.md` + `sales_brain.md` + `founder_beliefs.md`. All 20 founder beliefs preserved as the "Core Beliefs" section. Duplicate market-shift / never-position / problem statements collapsed to one.
* **`brain/voice.md`** (new) ← `style.md` + `writting_guidelines.md` (typo in filename dropped). Now the single home for tone + **all banned/preferred vocabulary** (previously scattered across 4 files).
* **`brain/outreach.md`** (new) ← `outreach_library.md` + `conversation_patterns.md`. Holds the **single canonical** "We're increasingly seeing candidates…" opener (grep = 1). CTA phrase bank + short-response library consolidated here.
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

## Open question (unresolved)
HireSignal = StepUp rebrand, or separate service play? Affects only `proof.md` + `offer.md` content.
