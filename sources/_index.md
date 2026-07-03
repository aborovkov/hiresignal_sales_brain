# _INDEX.md — Transcript Registry

> Registry of raw call/note sources. Naming: `YYYY-MM-DD__<account-slug>__<type>.md`.
> Types: `call` | `discovery` | `demo` | `internal` (team/alumni chatter) | `custdev` (research note, lives in `notes/`).
> Raw sources may contain names — they live here and in `crm/`, never promoted un-anonymized to `brain/` or `content/`.
>
> ⚠️ Dates below are **ingestion dates (2026-07-02)**, not verified call dates — correct when real dates are known (`git mv`).

| Date | File | Account / Who | Type | Processed? | Assets produced |
|------|------|---------------|------|------------|-----------------|
| 2026-07-02 | `calls/2026-07-02__david-stepania__discovery.md` | David Stepania (advisor) | discovery | ☐ | |
| 2026-07-02 | `calls/2026-07-02__muhammad-umair__demo.md` | Muhammad Umair (dev, Dubai) | demo | ☐ | |
| 2026-07-02 | `calls/2026-07-02__nick-clark__discovery.md` | Nic Clark (BairesDev, LATAM staffing) | advisor¹ | ✅ | `crm/accounts/bairesdev.md`; pains.md field note; objections.md Obj 2 + GDPR note; 3 ideas; ⚠️ ICP strategy flag |
| 2026-07-02 | `calls/2026-07-02__sheldon-quadros__discovery.md` | Sheldon Quadros (Unix; SDR chat) | discovery | ☐ | |
| 2026-07-02 | `calls/2026-07-02__sofia-recalde__demo.md` | Sofi Recalde (referral interest) | demo | ☐ | |
| 2026-07-02 | `calls/2026-07-02__vladi-benesova__discovery.md` | Vladi Benešová (LinkedIn/marketing, RU) | discovery | ☐ | |
| 2026-07-02 | `calls/2026-07-02__internal-team__internal.md` | Internal / Turing alumni | internal | ☐ | |
| 2026-07-02 | `notes/2026-07-02__recruiter-pains__custdev.docx` | Recruiter-pains research (⚠️ empty file) | custdev | ☐ | |

Processing an entry runs `ops/extraction.md`. Mark "Processed?" once CRM + brain + content assets exist.

¹ Logged on ingestion as `discovery`; on processing it was reclassified **advisor / referral** (contact won't buy — see `crm/accounts/bairesdev.md`). Filename left unchanged to avoid churn; rename via `git mv` if desired.
