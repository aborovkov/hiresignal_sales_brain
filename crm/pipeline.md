# PIPELINE.md

> How the CRM works: where the pipeline lives, the funnel stages, and the per-account file schema.

---

# Repo = the single source of truth

**`crm/leads.csv` = the live pipeline.** One row per person, keyed by LinkedIn URL. It is the source of truth for *movement*: who is at which status, when they were touched, and what the next action is. Managed via the lead-hunter tooling (`leads.py add / mark / next / stats`).

**Account files (`crm/accounts/`) = durable account intelligence.** The source of truth for *depth*: what was actually said, the pains heard, objections raised, verbatim quotes, and the reasoning behind next actions. Slow-changing, high-context, feeds `brain/` and `content/`.

**The Google Sheet ("(StepUP) Data Room навигация", ID `1WTbK6Zmha5EttAs3m0RsbPlOXq3lh_0t-v4AdMhGQfI`) is RETIRED as a lead source.** Its lead lists (tabs "Leads" and "TeamTailor") were fully imported into `crm/leads.csv` on 2026-07-19. Do NOT read the Sheet for lead analysis, lead status, or pipeline questions — it is stale from that date forward. It remains only as a historical archive (it still holds the original M1–M3 outreach message texts, which were not copied over).

---

# Funnel Stages

> The status vocabulary of `crm/leads.csv` (shared with the lead-hunter and sales-brain tooling):

`new → queued → contacted → replied → conversation → demo → trial → client`, plus `lost` (requires a reason in notes) and `parked` (requires a revisit date in notes).

Forward movement requires evidence stated by the user — never advance a status on assumption.

---

# Per-Account File Schema

One file = one account: `crm/accounts/<account-slug>.md`. Use the template in `crm/accounts/_template.md`.

Each account file holds, in order:

1. **Profile** — company, size, segment, ICP priority, ATS/stack, why they fit, known risk flags.
2. **Contact log** — dated entries: `YYYY-MM-DD | channel | gist`.
3. **Pains heard** — real pains surfaced (feeds `brain/pains.md`, anonymized).
4. **Objections** — objections raised (feeds `brain/objections.md`, anonymized).
5. **Quotes** — verbatim lines worth keeping (never leave this file un-anonymized).
6. **Status** — current stage, mirroring the `status` column in `crm/leads.csv`.
7. **Next action** — the single next move.

---

# Anonymization Rule

Client/company/person **names live only in `crm/accounts/` and `sources/`.** Everything promoted into `brain/` or `content/` must be stripped of identifying detail. See `ops/extraction.md`.
