# 2026-08-26 - Outbound ledger (F7 Odd-Precision Money Ledger)

- Status: PARKED 2026-08-26 - same root cause. Subject is Alexey's own outbound funnel, not
  the reader's hiring problem. Narrative pillar at best; will not produce sellable inbound.
- Formula: F7 Odd-Precision Money Ledger | Pillar: Narrative | 1,611 chars / 292 words
- Data source: crm/events.csv cohort read, 2026-08-26. 496 ever invited, 110 accepted (22.2%),
  median 4 days to accept, 166 never accepted and withdrawn, 319 ever contacted, 21 replied (6.6%),
  0 of the invited cohort reached meeting.
- Segment reply rates (contacted >= 10): partner 3/21 14.3%, rec-fractional 3/39 7.7%,
  rec-agency-tech 8/111 7.2%, needs-icp 2/33 6.1%, rec-staff-aug 1/18 5.6%,
  smb-inhouse 3/60 5.0%, rec-agency-small 0/29 0.0%

---

496 connection requests.
110 accepted.
21 replied.
0 meetings.

That is the whole outbound ledger since July. It lives in a 1,043-row CSV in a git repo, not a CRM, so every number here has a row behind it.

The interesting part is not the drop from 496 to 21. Everyone loses that much.

The interesting part is the last line.

Twenty one people wrote back. Not one of them turned into a call. So the funnel is not leaking at the top. It leaks in the step nobody logs, between "sure, tell me more" and a slot in a calendar.

Then I broke the replies down by segment and it got worse.

Partners and referrers: 14.3%. Best reply rate in the base by a wide margin. Also the only group with no budget and no roles to fill.

Technical recruiting agencies: 7.2% across 111 conversations.

Small companies hiring engineers themselves: 5.0%.

Generalist agencies: 0 out of 29.

Twenty nine conversations. Zero. I kept that segment alive for five weeks because it felt like the right buyer. It felt right and it was empty, and the only reason I know is that I wrote every touch down.

Reply rate rewards the people who are pleasant to talk to. It says nothing about who can sign.

One more line from the same file. Of those 496 invites, 166 were never accepted at all. I withdrew them this month. A third of the effort produced nothing and quietly pulled the account's acceptance rate down while it sat there.

None of this makes me want to send fewer messages. It makes me want to stop counting replies as progress.

If you run outbound: what is the first number after "replied" that you actually track?

#buildinpublic
