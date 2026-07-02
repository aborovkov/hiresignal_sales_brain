# EXTRACTION.md — Transcript → Assets Engine

> **STUB — to be completed in Task 3** (requires a real transcript to test against).
> The repeatable process that turns every call into CRM + brain + content assets.

## Input
A transcript file in `sources/calls/`, named `YYYY-MM-DD__<account-slug>__<type>.md` (type = call | discovery | demo).

## Step 1 — CRM
Extract into `crm/accounts/<slug>.md`: pains, objections, buying signals, verbatim quotes, next action, status.

## Step 2 — BRAIN
Append real pain/objection phrasings to `brain/pains.md` and `brain/objections.md`, tagged "heard in call", **no names**.

## Step 3 — CONTENT
Add 2–3 anonymized post ideas to `content/ideas.md` (patterns + economic consequences, per `brain/voice.md`).

## Anonymization
Names live only in `crm/accounts/` and `sources/`. Nothing identifying goes into `brain/` or `content/`.

## Close
Mark the transcript "Processed" in `sources/_index.md`.

## Done-criterion (Task 3)
One test transcript yields: a filled account file + ≥2 ideas in `ideas.md` + appended pains/objections.
