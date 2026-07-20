# OUTREACH.md

> Outreach and conversation mechanics: the field-tested first-touch template, opener variants, the conversation arc, the transition phrase bank, and short-response lines.
> Tone rules and banned vocabulary live in `voice.md`. Strategy and beliefs live in `positioning.md`.
> Locked messaging rules (approved DM structure, prohibitions) come from the sales-brain skill and win over anything here unless explicitly updated.

---

# 00. Grounding gate - hard rules before ANY draft (added 2026-07-19, Fer Eillman incident)

Context: Fernando Eillman (TalentCross) replied to the 27 May opener with "we have our CTO in the team, who take care about it". Two minutes later an AI auto-reply lectured him that his own setup was unsustainable ("the bar stays high - but so does the cost. Curious whether that's sustainable...") - invented pain, abstract register, no offer, thread died. Alexey's verdict: "полная чушь, так больше писать не надо." Full log: `../crm/accounts/fernando-eillman.md`; objection filed in `objections.md`. Separately, the May-July campaigns ran off a stale Google Sheet with unlogged statuses/WAS SENT, producing double-sends (OnHires, reQruitz, Talenteek). These rules exist so neither can recur.

1. **Thread first.** For any lead with status `replied` or later, or with any prior message in the thread: do not draft until the actual LinkedIn thread text is in front of you (paste or live browser read). Drafting from a CRM row or spreadsheet stage alone is forbidden. Thread unavailable = stop and ask for it.
2. **Source per claim.** Every personalized statement in a draft shown for review carries its source in brackets: [their post, date], [thread, date], [profile headline]. No source = cut the claim or fall back to the plain volume question.
3. **No bulk to warm.** Leads with status `replied` or later are excluded from every batch, template, or mass-send run. They get an individually written reply, human-reviewed before send, every time.
4. **Check the log before any touch.** Read last_touch_at + notes in `crm/leads.csv` (or the thread itself) before composing. A blank tracking column means "not logged", never "not contacted".
5. **Log at send time.** Any sent message is written back to the CRM in the same session, before the next lead is opened.

---

# 0. What actually converts (field evidence, 2026-07)

First outbound wave (15-17 Jul). Two structures, both landed. Evidence cross-checked against `content/winning-messages.md` and the `crm/accounts/` files.

**Structure A - standard volume opener** ("how many CVs land on your desk for one technical role..." + Turing line + free offer + "you keep the conversations" close): 3 replies in ~24h, and one demo booked. Dina Veprikova (fractional technical recruiter) replied "I would like to try" in 11 minutes, demo booked in 16. Sean Hassell (in-house TA) replied warm same evening. See `crm/accounts/dina-veprikova.md`, `crm/accounts/sean-hassell.md`.

**Structure B - role-anchored variant** (drops the Turing credential, names their exact seat and weekly cost): converted to a trial in the Focused-inbox batch. Roman Ostroushko (Head of Engineering):

> Roman, as Head of Engineering - how much of your team's week goes to screening resumes and first-round interviews? We built an evaluation layer that scores how a candidate thinks, not just the answer. I can set you up with 100 resume screenings + 5 AI interviews to try, free, expires on use not calendar. You keep the conversations, we handle the reading.

Reply in 10 minutes: "yes, I would like to take part in this." See `crm/accounts/roman-ostroushko.md`.

Both winners share the same DNA - that DNA is the canonical first touch (section 1). Five reasons it works, all reusable:

1. Named the exact role and tied the pain to THEIR time ("as Head of Engineering - your team's week"). Not abstract industry commentary - their calendar.
2. Right ICP: a person who personally owns the pain and can say yes.
3. Value in one line ("scores how a candidate thinks, not just the answer"). No feature list.
4. Zero-friction offer ("free, expires on use not calendar") kills the "no time for a trial" objection.
5. Asked them to TRY, not to MEET. No call request. Yes was cheap to give.

**What lost:**
- Asking for a call up front ("would you be open to a short chat?") got a polite "we're fine as-is" (Julia Fokina). Offer the sample, never the meeting.
- Wrong persona (business development, non-tech, tiny team) replied but went nowhere - Mariam, Gleb. Filter ICP before sending.
- The strong "seed a vacancy under your own live role" asset was spent on cold no-repliers (Elisaveta, Natalia, Liz): 0 replies. Save that asset for people who already engaged.

**Highest engagement move (even without a sale):** sending the recipient THEIR OWN CV/profile run through StepUP. Soumya returned 5 points of product feedback; Julia forwarded the link to a colleague. Show the product on their data; do not describe it.

---

# 1. The canonical first touch (use this by default)

Structure (this is the skill's approved DM structure, now with the field-tested role hook):

1. **Role-anchored pain question.** "[First name], as [their exact role/seat] - [time or volume question tied to their week]?"
2. **One-line value.** "We built an evaluation layer that scores how a candidate thinks, not just the answer."
3. **Volume-framed free offer.** "I can set you up with 100 resume screenings + 5 AI interviews to try, free, expires on use not calendar."
4. **Close.** "You keep the conversations, we handle the reading."

Fill-in template:

> [First name], as [role] - [how much of your week / how many resumes per role / how many hours] goes to [screening resumes and first-round interviews]? We built an evaluation layer that scores how a candidate thinks, not just the answer. I can set you up with 100 resume screenings + 5 AI interviews to try, free, expires on use not calendar. You keep the conversations, we handle the reading.

Constraints: under ~500 characters. One question, one CTA. No em dash. No "quick question" opener. No exclamation marks in first touch. The Turing "1,700 interviews" line is optional here and overused - default to leaving it out (see prohibitions).

---

# 2. Role-anchored hook bank (the variable part of line 1)

The hook must name their seat and hit a cost they personally feel. Real examples from the wave:

- **Head of Engineering:** "how much of your team's week goes to screening resumes and first-round interviews?"
- **Eng leadership / high-load:** "when you're hiring for high-load work, how do you keep interview signal consistent across whoever runs the loop?"
- **HRBP scaling remote teams:** "scaling global and remote teams at [Co] - how are you keeping technical interview quality consistent across timezones and interviewers?"
- **Agency / TA for startups:** "building TA for EMEA tech startups - what's the resume volume per eng hire across your clients right now?"
- **Niche staffing (iGaming/crypto/gamedev):** "resume volume in those niches gets brutal fast - how many are you reading per role?"
- **In-house TA lead:** "how many CVs typically land on your desk for one technical role? Curious if it's gotten worse this year."

Rule: if there is nothing real to anchor on, fall back to the plain volume question. Never fake personalization.

---

# 3. Pilot start (when they say yes)

Immediately, no calendar friction:

> Perfect. To kick it off: send me one open role (JD) plus a batch of CVs you'd otherwise read yourself. You get scored reports back - the obvious no's filtered out, the borderline calls kept for you to decide, and the ones actually worth a conversation surfaced. What are you hiring for right now?

This is the demo. Do not route a warm yes into a scheduling link.

---

# 4. Assets to offer (order by warmth)

1. **Cold, right ICP:** free trial (100 screenings + 5 AI interviews).
2. **Replied / curious:** their own profile or CV run through StepUP ("here's what it looks like in practice" + link). Highest-engagement asset.
3. **Engaged / considering:** seed a vacancy under one of their OWN live roles, run 3-5 anonymized candidates. Only for people who already replied - never a cold touch.

---

# 5. Follow-up cadence

- **FU1: +3-4 days.** New angle or a new asset, never "just bumping this". Good FU1 = offer the "your own CV through StepUP" asset.
- **FU2: +7 days after FU1.** Shorter, give an easy out.
- Then **park +60 days** unless there is a live trigger (vacancy spike, relevant post).
- **Reply in their thread beats any new message.** If they commented or reacted anywhere, engage there first.
- Do not stack a third asset on someone who never answered the first two (that is what failed with the "seed a vacancy" sends).

---

# 6. ICP filter BEFORE sending (gate, not afterthought)

Send only to people who personally own screening or interviews:
- Heads of Engineering / eng leads, technical recruiters, staffing-agency owners, in-house TA leads with steady eng hiring.

Skip / deprioritize:
- Business development, sales, non-technical roles (Mariam = business dev, went nowhere).
- Tiny teams with little interview volume (Gleb = mid-size, "we don't run a lot of interviews").

Grade the person A/B/C (see `crm-format.md` ICP scoring) before the DM, not after.

---

# 7. Locked prohibitions (from skill, do not violate)

- No subscription pricing or COGS logic in first outreach. Pricing only after a live conversation or a demo.
- Screening promise only in the approved three-tier form: obvious "no" removed, "worth a conversation" surfaced, borderline calls stay with the recruiter. Approved wording: "You'll never read an obviously unqualified resume again - and the borderline calls stay yours." Never "we cut all unsuitable candidates".
- EU AI Act: never "AI Act compliant". Use "built with AI Act requirements in mind".
- Cost-savings claim ("$65k/year per team, $5,700 per recruiter") allowed on LinkedIn and to agency owners only.
- Turing "1,700 interviews" anchor is overused - default off, use only on explicit request or the one sanctioned first-touch slot.
- No em dash "-" anywhere. No fake personalization.

---

# 8. Transition / soft-CTA bank (once in dialogue)

Preferred once a conversation is live:
- "Want me to set that up for one role?"
- "Send me one JD plus a batch of CVs and I'll run it."
- "Curious how you handle this today."
- "Would be interesting to compare notes."

Avoid as a first move:
- "Book a call" / "Book a demo" / "Quick 15-minute call?"
- "Would love to connect" / "Can I show you our platform?"

Note: earlier this file taught an abstract "industry shift observation" opener (Patterns 1-10). Those were never used in the live wave and are not what converted. The role-anchored volume question + free-sample offer is the tested default. The abstract patterns are kept below only as a fallback register for peer-to-peer threads with senior technical buyers who bristle at anything offer-shaped.

---

# 9. Fallback register - analytical peer opener (use sparingly)

For senior technical buyers (CTOs, VPEs) where an offer-first DM reads as selling, open with observation instead of offer, then let them pull:

> One thing becoming increasingly noticeable is how much harder it is to distinguish strong interview performance from actual engineering depth once conversations move past rehearsed architecture into production tradeoffs. Curious whether you're seeing similar patterns internally.

Move to the offer only after they engage. This register trades conversion speed for credibility; do not use it as the default.

---

# 10. Emotional tone

Calm, analytical, operator-to-operator. Never hype, never salesy, never over-friendly. Trust comes from accurate problem articulation and a frictionless offer, not from credentials or persuasion. See `voice.md`.
