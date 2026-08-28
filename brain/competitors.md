# COMPETITORS.md

> Competitor cards and battlecards. Differentiation itself is owned by `positioning.md` - this file only maps competitors onto it. Objection wording is owned by `objections.md`: anticipated objections live here until a real prospect raises one, then the verbatim version moves to `objections.md` with the answer that worked.
>
> Format per competitor: what they are, overlap, where we win, where they win, how to position, anticipated objections, watch list with a review date.

---

## Lovelio (lovelio.ai)

* **Added:** 2026-08-04
* **Source:** `sources/notes/2026-08-04__lovelio__competitor-research.md` (verbatim site quotes)
* **Category:** agency ATS / CRM with AI screening bundled in. Not a standalone evaluation product.
* **Threat level:** **medium.** Not a head-on competitor to the evaluation layer. The pressure is commercial: they make screening feel free.
* **Next review:** 2026-11-04

### What they are

AI-driven recruitment software for recruitment agencies. They position explicitly as the replacement for **Bullhorn, JobAdder and Vincere**, aimed at the low end of that market: *"Small to medium agencies deserve the very best software."*

Commercials: one plan, **$105 per user / month**, *"No tiers, no modules, no add-ons, no implementation fee, no annual contract."* Free to start, no card, cancel anytime.

Team and traction: *"Built by founders with two decades of experience building hiring software, and running and growing businesses."* They claim *"Major product enhancements released every single week."* No public funding, team size, geography, customer logos or G2/Capterra presence found as of 2026-08-04. Read as early stage, pre-review-volume.

### Where they overlap with us

Two surfaces, both inside the flat $105 plan.

**AI phone screening.** *"Lovelio can call and screen all strong candidates automatically. Imagine reviewing an applicant list and they have all been screened, ranked, sorted, and have detailed notes."* Questions are *"intelligent questions generated per candidate"* built from the CV, the job description and their *"Client DNA"*. The candidate joins via an email link, no scheduling. The recruiter gets transcript, answers, notes, and *"You approve every score."*

**Recruiter-led video screening.** The sharper overlap, because it is our own shape: *"Video call any client or contact - built in and native. Lovelio prompts you to ask questions, probe more, drill in."* Live transcript with speaker identification, auto write-up with strengths, watch-outs, salary and notice period, client-ready summary *"in minutes"*.

They also rank applicants on *"two axes"* with configurable score thresholds for auto-advance or auto-park.

### Where they do NOT compete

* No outreach sending. Their business-development module builds call lists of companies likely to hire and stops there, deliberately.
* Agencies only. In-house engineering teams and fractional CTOs (ICP P2 and P3) are not their stated target.
* Nothing public on question provenance, rubric calibration, evaluation methodology or scoring validity.

### Where we win

1. **Question quality is an asset, not a feature.** Their questions are generated per candidate from a CV and a JD. Ours are bank-grounded, built to discriminate between engineering levels, and carry an authored junior / mid / senior / red-flag rubric. Weekly releases close feature gaps, not content gaps.
2. **They test whether an answer appeared. We extract signal.** Auto-generated questions plus an LLM verdict is `positioning.md`'s "generic screening" with a phone attached. Our line holds unchanged: we do not score answers, we score how a candidate thinks.
3. **Their model produces exactly the enemy we named.** Ranked lists with detailed notes and no calibration is **false confidence** at scale, and its cost is a false positive on the shortlist.
4. **No migration.** Buying Lovelio means replacing the system of record - a slow, risky, whole-agency decision. We slot into the existing ATS and the existing workflow.
5. **Defensibility.** They publish nothing on how scores are produced or validated. Screening for employment is a high-risk use case under the EU AI Act, and "the AI called them and ranked them" is hard to defend to a client or a regulator without documented evaluation. Our line: built with AI Act requirements in mind, eval-documented, audit-ready architecture. (Never "AI Act compliant".)

### Where they win

1. **Bundling economics.** At $105 all-in, screening is a line item the buyer already paid for. Against an agency owner counting tools, "good enough and already included" beats "better and separate" on non-technical, high-volume roles. **This is the real threat, not their screening quality.**
2. **Fully automated first pass.** Zero recruiter time on the phone screen. At volume that is genuinely attractive and we should not pretend otherwise.
3. **Single pane of glass.** Sourcing, CRM, screening, client management, Slack, WhatsApp, Xero, job boards, API in one place. Integration friction is our tax, not theirs.
4. **Price transparency.** Public flat price, free start, no contract. Very low friction to try.

### How to position against them

* **Never compete on breadth.** We are not an ATS and must not be sold as one (`positioning.md`, Never / Instead). The moment the comparison becomes feature-count, we lose.
* **Pick the ground: roles where a false positive is expensive.** Their model is optimized for volume triage across every vacancy an agency runs. Ours is optimized for the vacancies where a wrong hire means a failed placement, a refund and a damaged client.
* **Lead with the false-positive cost, not with features.** The separating question: what happens when the automated screen passes someone who memorized the answer?
* **Coexistence is a legitimate sale.** An agency can keep Lovelio as the system of record and use us on the technical roles it cannot afford to get wrong. We do not need them to churn.
* **Keep the screening promise in the approved three-tier form.** *"You'll never read an obviously unqualified resume again - and the borderline calls stay yours."* Their pitch is that the machine sorts everything; ours is that the machine removes the obvious and leaves judgment where it belongs. That contrast IS the argument - do not blur it by over-promising automation.

### Anticipated objections

Not yet raised by a real contact. Move to `objections.md` verbatim, with the answer that actually worked, the first time a live prospect says one.

* *"Our ATS already has AI screening included."* -> Ask what the screen is made of: who wrote the questions, and how the score is defended when a client asks why a candidate was rejected. Included screening is priced at zero because it is generic. On roles where a bad placement costs a refund, generic is the expensive option.
* *"Why pay separately when it comes bundled?"* -> You are not buying a screening feature, you are buying the difference between candidates who sound right and candidates who are right. Compare on placements that stuck, not on tools consolidated.
* *"An AI already calls our candidates."* -> Keep it for volume triage. The question is what happens on the shortlist. Automated calls with auto-generated questions surface who answers fluently, and that is exactly where memorized answers pass.
* *"$105 for everything vs your price."* -> Do not enter this comparison. Reframe to the cost of one failed technical placement against a year of evaluation. Pricing discussion only after a live conversation or a demo (`outreach.md`).

### Watch list

* Do they publish anything on rubrics, question provenance or evaluation methodology? That is them moving onto our ground.
* Do they open up beyond agencies to in-house teams?
* Funding, logos, first G2/Capterra reviews - the signal they are past early stage.
* **Do they unbundle screening and sell it standalone?** That turns a medium threat into a direct one.


---

# ATS landscape - integration targets, not competitors

These are systems of record we sit on top of, not products we win or lose against. Kept here because
the integration list is a positioning decision: "which ATS do you plug into" is now a live question in
first calls, and answering it with a single niche name is a weak answer.

**Current state: StepUP integrates with Teamtailor only.**

## Field evidence - 2026-08-06, small agency in the middle of an ATS selection

A hands-on agency recruiter (see `../crm/nataly-lalova.md`) was mid-selection on the call. Her team
compared roughly 14 systems and had settled on **Skyler**, connecting from September. Her read on the
field, in her words and worth treating as one data point rather than a market verdict:

| System | Her note |
|---|---|
| **Skyler** | Chosen. Fit for a small team; the others priced or scoped for bigger orgs. |
| **Greenhouse** | "Жирная, дорогая" - too heavy and too expensive for a small agency. |
| **Teamtailor** | She looked it up during the call: reviews she found reported the system being slow, recurring errors, mediocre overall, and expensive. She had not encountered it on her own shortlist. |
| **Lever / LeverX** | On the compared list, not chosen. |
| **Huntflow, Zoho, BambooHR** | On the compared list, not chosen. |

## What this changes

* **Teamtailor is a thin bet.** It is popular in the US, but it did not surface on a European small-agency
  shortlist at all, and the first thing this prospect found about it was negative. Leading with
  "we integrate with Teamtailor" answers the integration question badly for this segment.
* **The selection moment is the opening.** A team switching ATS in September is rebuilding its workflow
  anyway - the one moment when switching cost, the objection that killed this deal, is temporarily zero.
  Track prospects who mention choosing or migrating an ATS as a timing signal, the same way we track
  vacancy spikes.
* **Skyler is the concrete ask on the table.** She asked directly whether the list of ATSs recruiters
  actually use was useful to us. It is. Decide whether a Skyler connector is worth building before her
  September migration, or the ingestion work lands outside her new system of record.
* **The ATS is not the competitor - the recruiter's own LLM folder is.** Note that she rejected the ATS
  as an answer to screening entirely ("И че? Он теперь не проскорит АТСка") while already running her
  own scoring in an LLM. The system of record and the evaluation layer are separate purchases in her
  head, which is exactly the hiring-intelligence-layer thesis - and also why the layer has to be
  demonstrably better than a well-prompted folder.

---

# Ценовой бенчмарк interview-as-a-service (собран 2026-08-28)

Публичных прайсов почти нет: **BarRaiser, Intervue.io, InCruiter, FloCareer,
InterviewVector** прячут цену за "book a demo" и custom quote. Ниже - всё, что
удалось вытащить из открытых источников.

| вендор | за интервью | примечание |
|---|---|---|
| RiseBird | ₹1000 ≈ $12 | это то, что платят **интервьюерам**, не клиентская цена |
| HireHunch | ₹2499 ≈ **$30** | единственный, кто публикует; индийский объёмный тир |
| **StepUP → CTRL+** | **75 EUR ≈ $81** | наш реальный чек, пакет 10 за 750 |
| **StepUP → Keilian (озвучено)** | **$200-350** | не продано |
| Karat, пилот 30-100/год | **$350-400** | $10.5K-40K в год |
| Karat, 100-400/год | $280-340 | |
| Karat, 400-1500/год | $220-290 | |
| Karat, enterprise 1500+ | $190-260 | |
| Karat, specialist premium | $350-500+ | любой объём |

В цену Karat входит: время интервьюера, инфраструктура платформы,
стандартизованная рубрика, письменный отчёт, доступ к записи интервью. То есть
**ровно наш состав поставки.**

Альтернативная оценка Karat в $100-150 встречается в блоге HireHunch - это
материал конкурента, цифра занижена, полагаться на неё не стоит.

## Главный вывод: рынок расколот надвое, между тирами пусто

- **Офшорный объёмный тир: $12-40 за интервью.**
- **Западный премиальный тир: $200-400 за интервью.**
- Между ними пусто, потому что там нет позиционирования: для объёма дорого,
  для премиума дёшево.

**Наши 75 EUR стоят ровно в этой пустоте**: в 2.5 раза дороже HireHunch и
вчетверо дешевле Karat при премиальной поставке. Разбор и решение по цене -
в `gtm.md`, раздел 5.

## Ориентир для ROI-аргумента

Собственный инженер на телефонном скрине обходится компании в **$185-220**
загруженного времени; загруженный час senior-инженера - **$80-150**. BarRaiser
строит весь свой ROI-нарратив на этом: инженер, тратящий 10 часов в неделю на
интервью, стоит компании $40-78K в год. Аргумент рабочий и применим к нам, но
он работает только против цены в премиальном тире: при 75 EUR за интервью
сравнение перестаёт звучать как экономия и начинает звучать как подозрительно
дёшево.

Источники: interviewcost.com/karat-cost, blogs.hirehunch.com (обзор площадок
Индии 2026), barraiser.com/interview-outsourcing, intervue.io/pricing,
glassdoor (тред про ставку интервьюера RiseBird).
