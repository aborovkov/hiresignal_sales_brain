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
* `outreach.md` — opener patterns, conversation arc, soft-CTA/short-response libraries.
* `proof.md` — ⚠️ **CRITICAL, mostly TODO.** Credibility anchor, cases, metrics.
* `offer.md` — ⚠️ **TODO.** What we sell, pricing, free-sample wedge.

## crm/

* `pipeline.md` — **Sheet-vs-repo split**, funnel stages, per-account schema.
* `accounts/<slug>.md` — one file per account (use `accounts/_template.md`).
* `_next_actions.md` — who to contact / reply to next.

## sources/

* `_index.md` — transcript registry. Files: `calls/`, `notes/`. Naming: `YYYY-MM-DD__<account-slug>__<type>.md`.

## content/

* `pillars.md` → `ideas.md` → `drafts/` → `published/` → `post_log.md`.

## ops/

* `extraction.md` — transcript → CRM + brain + content engine (**stub, Task 3**).
* `sales_process.md` — how to run outreach & first calls.

---

# Conventions

* **Live pipeline is in the Google Sheet** (`1WTbK6Zmha5EttAs3m0RsbPlOXq3lh_0t-v4AdMhGQfI`). The repo holds depth, not stage-movement. See `crm/pipeline.md`.
* **Anonymization:** names live only in `crm/` and `sources/`. Never promote identifying detail into `brain/` or `content/`.
* **One fact, one home.** If two files would state the same thing, one owns it and the other links. Canonical outreach opener lives only in `brain/outreach.md`.
* Content voice is governed by `brain/voice.md`. Content flows via `/linkedin-post-writer` → `/linkedin-humanizer` audit → Publora (Tue–Thu, 07:30–09:00 Tbilisi).

---

# Open question

**Is HireSignal a rebrand of StepUp, or a separate service play?** This decides the content of `brain/proof.md` and `brain/offer.md` (whether StepUp product metrics can be cited directly). Structure is unaffected either way.
