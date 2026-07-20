# OUTREACH_FUNNEL.md

Sidecar to `leads.csv`, keyed by `linkedin_url`. One row per lead that entered outreach.
Keeps the fragile master CSV untouched. The `outreach-runner` skill writes here at send
time (grounding-gate rule 5: log before opening the next lead). `funnel_report.py` reads here.

## Stages (linear; a lead sits at its furthest-reached stage)

| stage | meaning |
|-------|---------|
| `sourced` | in leads.csv, not yet actioned (default; may be omitted from sidecar) |
| `connect_sent` | connection request fired |
| `connect_accepted` | they accepted the request |
| `opener_sent` | first-touch DM sent |
| `replied` | any reply received (see `reply_class`) |
| `won` | trial / demo / explicit "yes I'll try" |
| `dead` | declined hard or thread died, no path forward |

## opener_variant

Ties each opener_sent to a structure in `content/winning-messages.md` so reply rate is
measurable per text. Known variants:

- `A_volume_turing` — volume question + Turing credential + volume-based free offer + "you keep the conversations"
- `B_role_anchored` — names their exact seat + weekly cost, drops Turing credential
- add new labels as new structures are tested; never reuse a label for a changed text

## reply_class

`positive` | `neutral` | `decline` | `no_reply`. Set when `replied_at` is populated.
`no_reply` is the resting state for `opener_sent` rows that never got a response — leave
`replied_at` blank and `reply_class` blank until a reply lands; the report treats blank as no_reply.

## Hard rules (mirror brain/outreach.md §00 grounding gate)

- A lead at `replied` or later is **warm** — excluded from every batch/template run. Individual replies only.
- Every row is written at send time, same session, before the next lead opens.
- Timestamps are ISO dates (`YYYY-MM-DD`).
