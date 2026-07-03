# EXTRACTION.md — Transcript → Assets Engine

> The repeatable process that turns every call into CRM + brain + content assets.
> Run it once per unprocessed entry in `sources/_index.md`. One transcript in → four artifacts out.

---

# When to run

Any row in `sources/_index.md` with `Processed? = ☐`. Process one transcript at a time, oldest useful signal first, ICP-priority accounts first.

# Inputs

A transcript in `sources/calls/`, named `YYYY-MM-DD__<account-slug>__<type>.md`
(type = `call` | `discovery` | `demo` | `internal` | `custdev`).

Transcripts are raw ASR: expect misspelled names, wrong speaker labels, and garbled company names. **Correct the account slug and call type if the transcript contradicts the filename** (`git mv` the file, update `_index.md`). A "discovery" that turns out to be an advisor giving feedback is not discovery — relabel it.

---

# The 4 steps

## Step 0 — Classify the call (do this first)

Before extracting, decide what this call actually *is*, because it changes where the output goes:

* **Buyer call** (prospect could pay) → full CRM account file, pipeline stage applies.
* **Advisor / peer / referral call** (won't buy, but gives GTM signal or intros) → account file flagged **non-buyer / referral**, no pipeline stage. Their *feedback* still feeds `brain/`.
* **Internal / alumni** → no account file; harvest pains/ideas only.
* **Custdev / research** → no account file; feeds `brain/pains.md` + `content/ideas.md` only.

Write the classification into the account file's `Segment / ICP priority` line.

## Step 1 — CRM  → `crm/accounts/<slug>.md`

Use `crm/accounts/_template.md`. Fill, in order: Profile, Contact log (dated), Pains heard, Objections, Quotes (verbatim, stays in this file), Status (mirror the Sheet), Next action (single move). Names are allowed here.

If a buyer, set `Status` to the correct funnel stage from `crm/pipeline.md` and add the account to `crm/_next_actions.md`.

## Step 2 — BRAIN  → `brain/pains.md`, `brain/objections.md`

Append **only genuinely new** pain/objection phrasings heard on the call, **stripped of all names/company detail**, tagged `[heard in call — YYYY-MM]`. If the call only re-confirms an existing pain, don't duplicate it — add a one-line "confirmed in the wild" note under the existing entry instead. New objections not yet covered get their own section.

## Step 3 — CONTENT  → `content/ideas.md`

Add 2–3 anonymized post ideas using the `content/ideas.md` template block. Prefer: a pattern + its economic consequence (per `brain/voice.md` §5). No names, no company detail. Tag each with a pillar from `content/pillars.md` and a candidate formula (F1–F10).

## Step 4 — STRATEGY escalation (new — don't skip)

If the call contradicts the strategy layer — ICP, pricing anchor, offer shape, or a `brain/positioning.md` belief — **do not silently absorb it.** Flag it to Alexey in the run summary as a decision, and drop a dated `> ⚠️ STRATEGY SIGNAL:` note at the top of the affected `brain/` file. Extraction updates knowledge; it does not get to quietly rewrite strategy.

---

# Close-out

1. Mark the row `Processed? = ✅` in `sources/_index.md` and fill `Assets produced` (list the files touched).
2. In the run summary to Alexey: state the account file created, what was appended to `brain/`, the ideas added, and any Step-4 strategy flags.

# Anonymization gate (hard rule)

Names/company/person detail live **only** in `crm/accounts/` and `sources/`. Nothing identifying is ever promoted into `brain/` or `content/`. Grep the diff for the account name before committing brain/content changes — if it appears there, stop and scrub.

# Done-criterion

One transcript yields: a filled account file + ≥2 ideas in `ideas.md` + appended/confirmed pains/objections + any strategy flags raised + the index row closed.
