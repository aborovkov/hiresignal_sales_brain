# 2026-08-26 - Memory is a file format (F10 Contrarian + Receipts)

- Status: PARKED 2026-08-26 by Alexey - "this is not my product, this is my outreach machine".
  Post reads as if the CRM/agent tooling is the thing he sells. Wrong positioning: attracts
  AI-workflow builders, not hiring buyers. Do not publish as is.
- Formula: F10 Contrarian + Historical Receipts | Pillar: Authority | 1,558 chars / 282 words
- No Turing credential anchor (per brain/voice.md, 2026-08-26 rule)
- Receipts, all read from the store on 2026-08-26: crm/leads.csv 1,043 rows / 20 columns;
  crm/events.csv 3,873 events (2,362 transition, 914 added, 411 edit, 139 touch, 43 note,
  4 alias); earliest event 2026-05-16; 876 commits; 10 rows carry aliases.
- The lead in the story is Antonio Marino (Emma), deliberately NOT named in the post:
  added 2026-07-28, invited 2026-07-28, withdrawn 2026-08-22, resurfaced 2026-08-26 in a
  lead-hunter batch at score 5 and was caught by the dedupe pass.

---

Every AI product now advertises memory. Mine has none, and that turned out to be the point.

This morning an agent handed me the best lead in the batch. Co-founder and CTO at a fintech, headline literally says hiring engineers. Scored 5 out of 5. I was ready to send.

Then it checked the file and stopped.

Same person. Invited in July. Never accepted. I withdrew that invite four days ago.

Nothing in the model knew this. The model had never seen July. What knew it was a 1,043-row CSV in a git repo where every status change since May 16 has its own line. 2,362 transitions. 914 people added. 4 merges where somebody renamed their LinkedIn URL and would otherwise have walked back in as a stranger.

876 commits. No database.

For months I thought the hard part was the model. It is not. The hard part is that a conversation ends and takes everything with it. Give the thing a file it can read and the intelligence stops being the constraint, because now it has a yesterday.

Two rules made it work. Both are boring.

Write the event, not the state. "Invited July 28, withdrawn August 22" survives. "Status: lost" tells the next session nothing it can act on.

Make identity survive renaming. People change their LinkedIn slug and come back looking new. Ten rows in my file carry an alias for that reason, and each one is a message I did not send to somebody twice.

Memory sounds like a model feature. In practice it is a file format.

If you run agents on your own work: where does what they learned actually live after the tab closes?

#buildinpublic
