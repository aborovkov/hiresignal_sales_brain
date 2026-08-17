# The lead store

One store, on disk, in this repo. There is no spreadsheet, no plan/apply step,
and no manual paste. Anything that touches a lead goes through the CLI.

```
crm/leads.csv     one row per person, keyed by canonical linkedin_url
crm/events.csv    append-only journal of every status change and note
scripts/leads.py  the only sanctioned way to read and write the two
```

## Finding the repo

Two situations, one rule: resolve the path first, then use it for everything.

- Cowork running **on the user's computer**, or any local shell:
  `/Users/aborovkov/src/stepup/src/hiresignal-sales-brain`
- Cowork running **in the cloud**: the folder is mounted into the device VM, so
  every command goes through `device_bash`, and the path is
  `/sessions/*/mnt/hiresignal-sales-brain`. Resolve the glob once with
  `cd /sessions/*/mnt/hiresignal-sales-brain && pwd`.

If neither resolves, the desktop app is not connected. Say so and stop. Do not
fall back to the Google Sheet - it is a frozen archive as of 2026-08-17 and
reading it will produce stale statuses.

## The columns (A..T)

```
linkedin_url  name  headline  company  role  location
icp_segment   icp_segment_raw  icp_score  icp_reason  source_query
found_at      status  last_touch_at  next_action  contact_file  notes
msg1          msg2   aliases
```

`icp_score` is an integer 0-5, the single scale for the whole stack; never A/B/C.
`aliases` holds other LinkedIn URLs the same person has appeared under,
separated by " | ". `notes` is an append-only dated log, same separator.

## Status vocabulary

```
new -> invited -> connected -> contacted -> replied -> meeting -> client
```

plus `parked` (temporary hold, needs a revisit date in the note) and `lost`
(terminal, needs a reason). The CLI refuses to move anyone backwards through the
pipeline; use `parked` or `lost` instead. Forward movement requires evidence the
user stated - never advance on assumption.

## Identity, and why it matters

A person is not their URL. They rename their vanity slug, and LinkedIn serves
localized addresses like `/in/name/en`. Matching on the raw URL is what used to
resurface people we had already written to, as if they were fresh leads.

`leads.py` matches in three passes: canonical URL, then `aliases`, then
distinctive full name (two or more tokens, no initials). **Never insert a lead
without going through `check` or `add`** - they are the gate, and they are the
reason the same person stops coming back twice.

## Commands

```bash
python3 scripts/leads.py check <url> [name]   # known already? matched how?
python3 scripts/leads.py add < leads.json     # append new, skip known, journal
python3 scripts/leads.py status <url> <status> [note]
python3 scripts/leads.py note <url> <text>
python3 scripts/leads.py show <url>           # the row plus its full history
python3 scripts/leads.py list warm|follow-up|first-dm|to-invite|<status>
python3 scripts/leads.py funnel
```

`add` takes a JSON list of objects with any of the column names; `linkedin_url`
and `name` are the ones that matter. Every mutating command appends to
`crm/events.csv` and makes its own git commit, so the funnel history is real and
any mistake is one `git revert` away.

Read the store directly with pandas or csv when a question is easier answered
that way. Only **write** through the CLI.
