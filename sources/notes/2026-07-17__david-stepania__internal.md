# 2026-07-17 - David Stepania (ThirstySprout) - design-partner test session (WhatsApp)

> Type: internal (advisor / design-partner chatter). Contains names - stays in `sources/` and `crm/`, never promoted un-anonymized to `brain/` or `content/`.
> Context: David test-drove StepUP against a live Ashby role (Senior Software Engineer, Customer Experience Platform, 746 applications). He bulk-uploaded candidates - the ones ThirstySprout already submitted plus Ashby's top AI recommendations - and compared StepUP's output against Ashby's AI assistant and Claude side by side. Screenshots shared: Gmail (StepUP match-report emails in Primary), Ashby AI review criteria + candidate ranking, and a Claude chat ranking/fake-flagging the same batch.

## Assets produced

- `crm/accounts/david-stepania.md` (new account file)
- `brain/objections.md` - 2 field entries (input-conflation; "inbound is dead")
- `content/snippets.md` - 3 snippets (recruiter proof-quote; fraud/trust opener; defensibility line)
- `brain/positioning.md` - "AI-Era Identity Fraud" section + "Technical agency owners / design partners" segment pattern
- `brain/icp.md` - Priority 1 common-problem bullet (inbound fraud)

## Thread (verbatim, times in Asia/Tbilisi)

- 18:22 Alexey: working on, stay tuned
- 18:44 Alexey: can you accept the invite? david@thirstysprout.com
- 18:51 David: it says expired / or already used
- 18:54 Alexey: damn...
- 18:56 Alexey: [new credentials sent for david@thirstysprout.com]
- 18:57 Alexey: processing, will let you know
- 19:42 Alexey: bulk upload.. makes me crazy / uploaded, you can check
- 20:32 David: ok i see candidates in there / now what? / do i add a job?
- 20:32 Alexey: Copy paste or pdf or doc on /hiring-board / Yes
- 20:39 Alexey: And then you will see plus button to add candidates on uploaded job
- 20:39 David: seems like there is a lag between the time u upload something / and before it actually appears on the platform
- 20:41 David: there should be a select all button to add them all
- 20:42 David: a little choppy because of the lag / i added some then it disappeared, not sure if it was added or not / it looks like some were added / then had to re add them / i think now they are all added
- 20:43 Alexey: Yes, the lag is something i need to work on
- 20:45 David: i got one good news / all your emails are hitting my primary inbox / instead of spam/promo
- 20:46 Alexey: Oh wow :) all? / Do i spam you a lot?
- 20:48 David: No but usually its hard to land in someone inbox / Especially with new domain
- 21:54 David: i sent you all the ones that we have submitted / and the top ones recommended by ashby / the problem is a lot of them that ashby recommended are for sure fake / also check this out
- 21:55 Alexey: Quality is low
- 21:58 David: they are all fake profiles / im almost 100% sure
- 21:59 Alexey: I need to read them and think / Will ping you
- 22:04 David: one of the easy ways to detect a fake profile: they apply with a LinkedIn and the LinkedIn is gone a few days later. Second: mismatching LinkedIn profiles. Third: the resume just doesn't make sense.
- 22:06 David: im gonna connect to ashby with mcp and see how that works
- 22:06 Alexey: Will explore that also
- 22:07 David: u want access to ashby?
- 22:07 Alexey: Not now, maybe later / Thx
- 22:18 David: my recruiter says the fake ones are always the best matches
- 22:18 Alexey: I saw it in my system also..
- 22:18 David: my guess is that there are some chinese companies that just make fake profiles and tailor it to these ats systems
- 22:19 Alexey: I am yet to understand if fake is bad unless he can stand for himself
- 22:20 Alexey: Like if i can tell a story and it can be defended its not a fake anymore / But yeah, i am working on pulling data from github by the link
- 22:20 David: fake means someone in china trying to apply as if they are american with mostly fake info
- 22:22 David: this is all some AI bs / inbound is freakin dead lol
- 22:23 Alexey: I see.. its not an inflation of profile but a geo problem
- 22:23 David: ai generated spam

## Fake-profile evidence from the shared screenshots (Ashby + Claude passes)

- Cross-candidate templating: near-verbatim "35M+ medical publications RAG" bullet in both Kevin Chen and Jeffrey Brown, both at the same employer (OpenEvidence) - strong resume-farm signal.
- Email patterns with random tokens: `kevin.js.chen@gmail.com`, `jeffrey.brown.gru@gmail.com`.
- Fantasy-density metrics: "100% USMLE", "$100M revenue", "2,000% YoY", "$237B+ quarterly", stacked FAANG-hop chains with flawless numbers.
- Timeline inconsistencies (e.g. back-to-back 5-month stints at highly selective companies overlapping a master's).
- David's manual tells: LinkedIn present at apply, gone days later; LinkedIn <-> resume mismatch; resume that "doesn't make sense".

## Product feedback (routed to product, not brain)

- Upload -> display lag is the core UX problem; it cascades into the flaky add-candidates flow.
- Add-candidates is non-idempotent / no clear saved-state: items appeared to vanish, had to be re-added.
- Missing "select all" (and range select) for bulk add.
- Keep protecting email deliverability (Primary-inbox landing on a new domain).

## Open strategic thread

- Alexey's stance: "fake" is not automatically bad if the person can defend the story live; the unfixable case is the one who cannot. -> supports flag-then-verify, not remove-all. Recorded in `brain/positioning.md` (AI-Era Identity Fraud).
- Alexey building GitHub-by-link data pull for verification.
