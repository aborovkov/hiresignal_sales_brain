# SNIPPETS.md

> Reusable proof fragments for outreach and content. Everything here is anonymized (see `../CLAUDE.md`); the trail back to the source lives in the Source line.

## Proof snippet: CIS IT recruiter volume (anonymized)

RU:

"Рекрутёр, закрывающий IT по СНГ, получает 370-400 откликов в день, до 1000+ в первый день после публикации. Около половины - нерелевантны. Прочитать это адекватно невозможно."

EN version for outreach:

"A recruiter covering IT roles across the CIS gets 370-400 applications a day, spiking past 1000 on day one after posting. About half are irrelevant. No human can read that properly."

* Source: `../crm/accounts/sofiia-harasaian.md`, 2026-07-15

## Proof snippet: the ATS AI ranks fakes highest (anonymized)

> The buyer's own words, agency-side. Powerful because it indicts the incumbent's AI without us having to attack it.

RU:

"Рекрутёр говорит: фейковые профили всегда оказываются лучшими матчами. AI внутри ATS ранжирует подделки выше всех - его главная фича работает против клиента."

EN version for outreach:

"An agency recruiter put it plainly: the fake profiles always come back as the best matches. The AI inside the ATS ranks fabricated candidates highest - the feature is working against the buyer."

* Source: `../crm/accounts/david-stepania.md`, 2026-07-17

## Opener: fraud/trust hook for agencies (alt to the volume question)

> Use when the segment is drowning in AI-generated inbound. Question-first, no pitch. Test against the standard volume opener.

EN:

"Quick one - of the candidates your ATS ranked as top matches last month, how many turned out to be fake? Most agency owners I talk to are finding the AI-generated ones score highest."

* Source: `../crm/accounts/david-stepania.md`, 2026-07-17

## Framing line: defensibility (real vs fake)

> Aligns with the "we score how a candidate thinks" one-liner and the flag-then-verify promise. Avoids promising removal of all fakes.

EN:

"We don't try to delete every fake. We surface the ones who can actually defend their work - and flag the ones who can't, so your team spends time only where it pays off."

* Source: `../crm/accounts/david-stepania.md`, 2026-07-17

---

## Partner-program first-touch DMs (EN, model A only) - ACTIVE since 2026-08-18

Canonical source: `../brain/partner-program.md` (pitch text v1, segmentation
rule, and the three variants below). Rules: one variant per person, rotate
across a batch, one real personalization line each, max 20-25 first DMs/day,
`leads.py check` before every send. Never mention the reseller/markup model or
any transfer price in writing.

**V1 - "we pay recruiters" hook (default):**
Hi {Name}, we started paying recruiters a cut of every interview we run. The mechanics: you know companies where staff engineers interview candidates themselves. You make one intro, our engineers take those interviews over - recorded, structured report per candidate - and you get 10% of every interview we run for that client, for as long as they stay. We do zero sourcing, so the client stays yours. Want the short one-pager?

**V2 - pain-first (client engineers' time):**
Hi {Name}, most hiring stalls I see have one cause: the engineers who run tech interviews have no time for them. We take that load - our engineers interview the client's candidates, record everything, send a structured report on each. New part: we opened a partner program. You intro us to a client, we handle the sale and delivery, you earn 10% of every interview we run for them. Sourcing stays 100% yours. Worth a look?

**V3 - anti-competition (agency owners):**
Hi {Name}, we opened a partner track I think fits your agency. StepUP runs technical interviews as a service: practicing engineers interview the client's candidates, recorded, structured report on each. You bring the client, keep the relationship, and take 10% of every interview we run for them. We sell no recruiting services at all, so there is nothing for us to compete with you on. Open to details?

* Target pool: `rec-fractional` + `partner` segments first, then agency founders. Buyer-ICP leads (staff-aug CTOs etc.) keep the standard buyer opener.
* Known gap: V1 promises a one-pager that does not exist yet - build before first V1 send, or send V2/V3 meanwhile.
