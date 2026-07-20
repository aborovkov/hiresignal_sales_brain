# LinkedIn Sent-Invites Cleanup — Plan

_Last updated: 2026-07-20 11:09 +04_

## Why
Pending sent connection invitations had grown to ~1,149. A large stale
queue signals low engagement to LinkedIn, throttles the weekly invite
limit, and drags acceptance rate down. Goal: shrink the queue safely.

## Decisions (set by Alexey)
- **Execution:** automated, oldest-first, in daily batches.
- **Criterion:** withdraw the OLDEST pending invites first; SPARE anyone
  whose profile is in the CRM (`crm/leads.csv`, 399 profiles) — see
  `keep_urls.txt`.
- **Pace:** ~40–50 per day, spread out (never bulk-withdraw everything at
  once — that trips spam detection).
- **Target:** bring the queue from ~1,149 down to ~350.
- **Re-invite rule:** after a withdrawal you cannot re-send to that person
  for ~3 weeks. CRM profiles are spared precisely to avoid this.

## How the daily batch works
1. Open LinkedIn > My Network > Manage invitations > Sent > People.
2. Scroll the list fully (newest first, so OLDEST are at the bottom).
3. From the bottom up, withdraw the oldest invites whose profile URL is
   NOT in `keep_urls.txt`, ~40–50 per run, with a short pause between each.
4. Log the run in `log.md` (date, count withdrawn, new remaining total).
5. Stop for the day. Repeat next day until remaining <= ~350.

## Known constraints (important)
- Requires: LinkedIn logged in + the browser reachable. When run
  unattended on a schedule, the Mac must be awake, the Claude desktop app
  open, and LinkedIn still logged in — otherwise the run self-skips.
- Withdrawals get slower as the list grows heavy in the browser; batches
  are time-budgeted so a run always finishes cleanly.
- Mass automation of LinkedIn actions is against LinkedIn's User
  Agreement; the conservative pace (~40–50/day) is the mitigation.

## Files
- `keep_urls.txt` — normalized CRM profile URLs that are never withdrawn.
- `log.md` — per-day progress log.
