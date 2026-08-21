# LinkedIn account health - hard limits for every skill that touches the browser

**Set 2026-08-21 by Alexey.** Trigger: LinkedIn showed a warning about excessive
profile viewing after a day with ~14 automated profile opens, three deep scrolls
of Connections / Messaging, and 27 first-touch DMs. These limits apply to
lead-sync, lead-hunter, sales-brain, invite-sweeper and any ad-hoc browser use.
They are floors on caution, not targets.

## Profile views (the thing LinkedIn flagged)

- **Max 5 profile opens per day via automation**, never back-to-back; only when
  there is no other way to get what is needed.
- Default source for ICP scoring and openers is the **headline from the
  Connections list or the Messaging row**, plus whatever Alexey pastes into the
  chat (About, posts, a thread). Pasted text = zero views. Ask for a paste
  before opening a profile.
- Never open profiles in a loop "to check locations". Location comes from the
  Connections card when visible, from the paste, or stays blank.

## List pages (Connections, Messaging, Sent invitations)

- **lead-sync at most once per day**, one page per pass by default (Connections
  OR Messaging). Read the top 20-30 rows; the deep 10-day reconcile of
  2026-08-21 was a one-off and is not to be repeated routinely.
- Scroll with real wheel events, small steps, pauses of 1.5-2 s; never
  programmatic jumps, never more than ~10 scroll steps per page per day.
- If the page goes blank or LinkedIn shows any throttling notice, stop the run
  and report; do not reload and retry.

## Outbound (existing rule, restated)

- **15-20 first-touch DMs per day**, spread across the day, never one block.
  20-25 is the absolute ceiling; 27 on 2026-08-21 was over it.
- 15-20 follow-ups per day max, same spreading rule.
- One message per person per pass; no bump inside 3 full days.

## Escalation

- **After any LinkedIn warning: next full day = no first-touch DMs and no
  automated browser use at all.** Live threads only, by hand.
- **After a second warning or any restriction: browser off for 7 days** for all
  skills. Work only from pasted content and the on-disk store. Alexey decides
  when to switch it back on.
- Log every warning here with the date, so the pattern is visible.

## Warning log

- 2026-08-21 - "too many profile views" notice. Same day: ~14 automated profile
  opens, 3 list-page passes, 27 first DMs. Action: 2026-08-22 is a no-outbound,
  no-browser day; limits above introduced.
