# ICP Decision — standing choice for lead hunts

**Decided:** 2026-07-18, by Alexey (lead-hunter run).

**Active hunt ICP: Priority 1 — Technical Recruiting Agencies** (as defined in `icp.md`).

Context: `icp.md` carries a three-way contradiction (agencies vs. enterprise 1,000+ vs. early-stage 20-40 + VC/PE portfolio channel, surfaced on the GTM advisor call). For lead hunting, Alexey chose to run on agencies despite the known tool-saturation risk ("we have 90 tools, 5 ATS").

Scope for hunts under this decision:

- Target: owners, founders, managing partners, and senior delivery leads of technical recruiting / IT staffing agencies.
- Strong fit signals: tech-focused desk (engineering roles), client-side interview dependence, inbound fraud pain (fake / geo-masked applicants), CIS or EU/US remote markets.
- Disqualifiers: generic non-technical staffing, pure volume shops, enterprise in-house TA teams.
- **Hard disqualifier (2026-07-18, Alexey, personal): no leads based in Ukraine.** Drop at scoring time regardless of fit; never write them to `crm/leads.csv`.
- **Hard disqualifier (2026-07-25, Alexey): no leads based in Russia (RU) - under sanctions.** Drop at scoring time regardless of fit; never write them to `crm/leads.csv`.

If the strategy question in `icp.md` gets resolved differently later, update this file — lead-hunter reads it before every run.

---

## Update 2026-07-28, by Alexey (lead-hunter run): open a SECOND front — Priority 2, Small Engineering-Led Startups.

Both fronts are now active. P1 (agencies) continues via the hands-on / champion cut; P2 is a new DIRECT-BUYER front.

Rationale surfaced in practice, not theory: the entire pipeline had become recruiters/agencies (the middleman). Funnel evidence this session - of ~83 people ever messaged, ~93% ghosted, ~3% explicit no, and the only ones who engaged were hands-on operators, never delegating owners. Agencies also hit the known tool-saturation wall ("90 tools, 5 ATS"), so a cold "another screening tool" offer drowns. Companies that hire engineers feel the pain first-hand (one bad senior costs a quarter) and are not tool-saturated the same way. This is exactly `icp.md` P2 (small engineering-led startups) / P3 (fractional CTOs) and the GTM advisor's push.

Scope for the P2 front:

- Target: founders, co-founders, CTOs, VP Engineering, Heads of Engineering, and technical hiring managers at engineering-led startups (~10-50 engineers), founder-led or eng-led, remote hiring, no mature interviewing infrastructure.
- Strong fit signals: actively scaling the eng team, founder still in the loop on hiring, inconsistent/ad-hoc interviewing, "engineering quality matters" framing, recent funding (seed to Series B).
- Messaging angle: engineering signal quality / "we score how a candidate thinks" - NOT the screening-volume / cost-per-CV framing (that is the recruiter angle and does not resonate with a buyer who hires, not screens).
- Disqualifiers: large enterprises (slow procurement, relationship-heavy), non-technical startups, pure recruiters (those belong on the P1 front).
- **Hard disqualifiers unchanged: no leads based in Ukraine (UA) or Russia (RU).** Drop at scoring, never write.

Note on execution: P2 targets are harder to keyword-filter than recruiters (a founder/CTO does not put "I feel hiring pain" in their headline), so hunts lean on signals - recent-funding + hiring, founder/CTO at <50-person tech startups, posts about engineering hiring - and warm-up before DM matters even more here.


## Update 2026-07-28, by Alexey (lead-hunter run): investor-bigtech front + VC-firm-insiders sub-angle.

A third, experimental front was opened this session at Alexey's direction: **investor-bigtech** - the VC/PE portfolio-channel multiplier from the GTM advisor push. The target is not a direct buyer but a multiplier who recommends StepUP to their portfolio or their company's engineering org.

Segment tag in crm/leads.csv: `investor-bigtech`.

Definition: an English-speaking person who (a) invests (angel / scout / syndicate / LP / corporate VC), (b) is tied to engineering hiring (eng manager / VP Eng / head of engineering / head of talent / tech recruiting), and ideally (c) sits inside or close to a large tech company. Goal: get them to push StepUP to their portfolio or their own eng org, not to sell them a seat.

Messaging angle: "you see engineering hiring at scale; we score how a candidate actually thinks; worth showing your portfolio companies" - multiplier framing, NOT the recruiter cost-per-CV framing.

### Sharpest cut - make this the PRIORITY sub-angle next time: VC-firm insiders.
In practice the purest multipliers were not "an investor who happens to work in bigtech" but people employed inside venture firms and tied to talent / engineering:
- VC scouts (e.g. Scout @ Sequoia)
- Talent / network / platform partners at funds (e.g. Talent & Network @ Index Ventures)
- Corporate-VC investors (e.g. Angel Investor @ Intel Capital)
They have a direct, standing channel to many portfolio companies' engineering hiring at once. Prioritize them over solo angels.

### Search angles that worked (LinkedIn people search)
- `"angel investor" "engineering manager"` / `"VP of Engineering"` / `"head of engineering"` - best signal-to-noise; pulls the investor + eng-leader combo directly.
- Geo-scoped variants for English hubs: append `London` / `Toronto` (also try Dublin, Sydney) - clean English-speaking results.
- VC-firm-insider seeds: `"Scout @ Sequoia"`, `"Talent" "Ventures"`, `"Intel Capital"`, `"venture partner" engineering` - go after fund insiders directly.

### Angles that were weak
- `"angel investor" "technical recruiting"` - pulls generic HR / recruiters without the bigtech-eng tie.
- `"venture scout" "software engineer"` - mostly junior individual-contributor engineers, not multipliers.

Hard disqualifiers unchanged: no leads based in Ukraine (UA) or Russia (RU). Drop at scoring, never write.

Status of the front as of 2026-07-28: 58 investor-bigtech leads in crm/leads.csv (40 contacted via a connect push, 18 new from a London / Toronto / scout batch). Note: hunt output lands in crm/leads.csv (local); accepted connections are reconciled into the Google "leads" sheet by lead-sync.


---

## Update 2026-07-29, by Alexey: kill the fraud angle, re-point to the capability axis, new SPEARHEAD = staff-aug / talent-marketplaces / dev shops.

Field verdict this session: the **identity-fraud / legitimacy angle does not work — the product does not reliably detect fraud.** It is dropped from outreach, the offer, the wedge, and content (the `positioning.md` section is DEMOTED/PARKED). We do not promise a detector we cannot deliver — it would fail live in the free wedge, and one missed fake kills the case and the credibility.

**New primary axis (the one we can prove): capability evaluation.** "Interviews well, collapses in production" (false positives) + interviewer calibration, anchored on the 1,700-interview credibility. Founder expertise, not an algorithm promise.

**New SPEARHEAD front (priority over the others): vetted-talent marketplaces / staff-augmentation firms / dev shops.**

- Why: vetting *quality* (= capability, not fraud) is literally their product; a false positive hits their margin and their client directly; they are NOT tool-saturated the way recruiting agencies are ("90 tools, 5 ATS"); and Alexey is a domain insider from Turing.
- Target: Head of Talent Quality / VP Vetting / co-founder / delivery lead at talent marketplaces (Toptal / Andela / Lemon.io / Arc-type), nearshore/offshore staff-aug firms, and software houses that bill engineers to clients.
- Messaging angle: capability signal / "we score how a candidate actually reasons under ambiguity, so your placements hold up in production" — plus white-label / "independently verified" framing. NOT fraud, NOT cost-per-CV.
- Segment tag in crm/leads.csv: `staff-aug`.

**Second echelon (keep, do not lead):**

- P2 small engineering-led startups (capability angle) — continues.
- P1 technical recruiting agencies — only the hands-on owner/champion cut; deprioritized vs staff-aug given saturation.
- Non-technical founders making a first/critical eng hire — reachable via accelerators; queue behind the spearhead.
- AI/ML-role hiring cut — overlay on any segment; angle is "depth of live reasoning," NOT "catch the AI cheater."

**Deprioritized until we have proof (2-3 anonymized case studies):**

- investor-bigtech / VC-firm-insider channel — a multiplier play that needs credibility we do not yet have; pause the push, keep the 58 existing leads warm.
- web3 / crypto — it only made sense as a fraud play; dropped with the fraud angle.

**Offer motion:** service-led / done-with-you near-term (see `offer.md`) — sell the founder's evaluation, the product assists.

**Hard disqualifiers unchanged: no leads based in Ukraine (UA) or Russia (RU).** Drop at scoring, never write.


---

## Update 2026-07-29 (b), by Alexey: LOCKED active target set + seed hunting queries.

Set chosen by Alexey from the untried-ICP shortlist. Split by motion — do NOT sell channels like direct buyers.

### DIRECT BUYERS (feel the pain + own the budget → revenue, Phase 1-2). Hunt these first.

**1. Staff-aug / nearshore-offshore / software houses + talent marketplaces** — tag `staff-aug` (PRIMARY spearhead, per 2026-07-29 update above).
Why: vetting *quality* = their product; false positive hits margin + client directly; not tool-saturated; Alexey is a Turing insider. Buyer: Head of Talent Quality / VP Vetting / VP Supply / delivery lead / co-founder.
Seed queries (English hubs + warm CIS non-RU/UA; keep overlap low, geo-scope one per metro):
1. `"VP of Engineering" ("staff augmentation" OR "nearshore")`
2. `"delivery director" ("IT staffing" OR "software house")` — London / Amsterdam
3. `"Head of Vetting" OR "Head of Talent Quality" OR "VP Supply"` — marketplace supply-quality owners
4. `"co-founder" "nearshore software"` — Poland / Portugal / LATAM
5. `"Head of Engineering" ("software consultancy" OR "dev shop")`
6. `"software house" founder` — Warsaw / Krakow / Lisbon / Tbilisi / Yerevan
7. `"talent marketplace" "engineering" ("quality" OR "vetting")`

**2. Mid-market NON-tech building an eng team** — tag `mid-market`.
Why: real budgets, no interview infra, not tool-saturated. Buyer: Head of Eng / VP Eng / Head of Talent. Harder to keyword — lean on industry filter + title + scaling signal.
Seed queries (use LinkedIn Industry filter, one vertical per query):
1. `"Head of Engineering"` — Industry: Insurance / Insurtech
2. `"VP of Engineering"` — Industry: Logistics / Supply Chain
3. `"Head of Talent" ("digital health" OR healthtech)`
4. `"Director of Engineering" (proptech OR "real estate technology")`
5. `"VP Engineering" (manufacturing OR industrial OR automotive)`
6. `"Head of Engineering"` — Stockholm / Copenhagen / Helsinki / Amsterdam

**3. Eng-led startups — founders / CTO** — tag `startup-p2` (existing P2, capability angle, NOT cost-per-CV).
Harder to keyword (a CTO does not headline "hiring pain") — lean on recent-funding + hiring + founder-in-loop + posts about eng hiring; warm up before DM.
Seed queries:
1. `"co-founder & CTO"` — London / Berlin / Amsterdam
2. `"CTO" "Series A"` / `"CTO" "Series B"`
3. `"Founder" "we're hiring engineers"` (recent-post signal)
4. `"Head of Engineering" "remote-first"`

### CHANNELS / MULTIPLIERS (seed now with low effort, convert AFTER first case studies — Phase 2-3). Do not treat as Phase-1 revenue.

- **Accelerators** — door to non-technical founders' first eng hire. YC / Techstars / Antler / Entrepreneur First + regional (Startup Wise Guys, Baltics/Caucasus). Needs a founder-facing wedge + one case first.
- **Fractional-CTO networks / CTO-as-a-service** — one CTO evaluates hiring for several client cos = multiplier. Seed: `"fractional CTO"`, `"CTO as a service"`.
- **IC / PE-VC operating (technical due diligence)** — DIFFERENT product use (assess a whole team on a deal, not screen one hire); relationship/credibility-heavy. Channel experiment for later, NOT a Phase-1 revenue line. Seed: `"operating partner" engineering`, `"technical due diligence"`.

### Hunt order for revenue: `staff-aug` + `mid-market` first, `startup-p2` continues; channels seeded in parallel at low effort.

**Hard disqualifiers (restated): no leads based in Ukraine (UA) or Russia (RU).** Drop at scoring, never write.

---

## Update 2026-08-06, by Alexey: закрыт старый тёплый слой + чистка вне-locked сегментов.

Решение принято Алексеем устно шесть раз и до сих пор нигде не было записано — из-за
этого при каждом свежем чтении таблицы эти люди снова всплывали наверх очереди как
"самые горячие". Фиксируем в файле, чтобы больше не возвращалось.

**Тёплый слой от июля закрыт. Не поднимать в очереди, не предлагать follow-up.**
Переведены в `lost` (06.08.2026):

- Dina Veprikova (`meeting`, бронь демо 45 мин) — independent/fractional
- Sofiia Harasaian (`meeting`) — amplifier
- Ron Krönen — agency-generic (11-50)
- Alan Stein (interviewing.io) — agency-generic (11-50)
- Erik Avendaño Martinez — p2-inhouse-TA
- Egor Yatsenko — partner-channel

Причина: ни один из них не входит в locked-набор от 2026-07-29. Статусы `meeting` /
`replied` делали их формально приоритетными, но это наследие фронтов, снятых с
приоритета (agency-generic, investor-multiplier, partner-channel).

**Правило на будущее:** статус в воронке НЕ перебивает сегмент. Человек вне
locked-набора не попадает в очередь касаний, даже если он ответил или назначил
встречу. Сначала проверяем `icp_segment`, потом `status`.

**Сегменты вне locked-набора** — не хантить, не писать, при появлении в `contacted`
переводить в `parked` с revisit +2 месяца:

`p2-inhouse-TA`, `inhouse-recruiter`, `in-house TA (IT)`, `out-of-icp`, `investor`,
`partner-channel`, `amplifier`, `unclassified`, `recruiter-misc (verify)`

По этому правилу 06.08.2026 переведены в `parked` 42 человека из слоя `contacted`
(просроченные с баллом <4 и все недатированные).

**Активными остаются только:** `staff-aug` (spearhead), `mid-market`, `startup-p2` /
`p2-startup`, и `agency-tech` в срезе hands-on owner/champion.

**Hard disqualifiers без изменений: никаких лидов из Украины (UA) и России (RU).**

---

## Update 2026-08-06 (b), by Alexey: personal-network denylist — НЕ добавлять в CRM.

При сверке инбокса LinkedIn обнаружились активные переписки с людьми, которых нет в
таблице `leads`. Алексей решил: это не лиды, это личная сеть / переписка вне воронки.
**Никогда не заводить на них строки, не размечать сегмент, не включать в очередь
касаний.** Если всплывут при следующей сверке — игнорировать молча, не переспрашивать.

Malisa Ncube, Vijay Krishnan, Anthony Njimogu, Brandon Esse, Alexey Taraskov,
Soumya Madan, Vatul Parakh, Muhammad Hasan Zahid, Nikita Kaczynski,
Kristina Klasić, Sara Pratas, Joanna Sitarz, Sohaib Kazmi (добавлен 2026-08-07 решением
Алексея: написал в LinkedIn, лидом не является)

Правило шире частного случая: наличие живого диалога в LinkedIn само по себе НЕ
основание завести лид. Лид заводится только если человек проходит locked-ICP.

---

## Update 2026-08-07, by Alexey: география открыта (кроме RU/UA), фракциональные рекрутеры - активный фронт.

Два исправления, продиктованные Алексеем напрямую. Оба снимают ограничения, которые
до сих пор действовали молча и уже успели создать расхождение между тем, что
записано, и тем, что делает аутбаунд.

### 1. Географии как фильтра больше нет

Формулировка "Nordic / UK / EU" в `icp-priority.md` (пиннута 2026-07-29) **отменена**.
Правильная рамка одна:

> **Гео - любое, КРОМЕ России и Украины.**

Жёсткие дисквалификаторы по UA (2026-07-18) и RU (2026-07-25) остаются без
изменений: снимать на скоринге независимо от фита, в таблицу не писать.

Всё остальное - США, Канада, LATAM, Европа, UK, Австралия, Азия, Кавказ - равноправно.
Не деприоритизировать по рынку, не понижать score за "не тот регион". Если у человека
подходящий десk и он сам руками в скрининге, география значения не имеет.

Практическое следствие: в таблице 191 строка вообще без `location`, и ещё десятки
с LATAM / USA / Canada / Australia. Раньше часть из них могла проседать в очереди
как "не тот регион" - теперь не должна.

### 2. Фракциональные / фрилансящие рекрутеры - в наборе, и это отдельный активный фронт

Тег `independent-fractional (P1)` появился из двух прогонов lead-hunter 2026-07-31
и до сих пор не был закреплён ни одним решением - формально он находился вне
залоченного набора, хотя аутбаунд по нему шёл. Противоречие закрыто:

**Фракциональный / фрилансящий / соло технический рекрутер - полноценная цель.**
Основание: partner-network fit. Такой человек одновременно и пользователь, и канал
к своим клиентам.

- Это **активный фронт для хантинга**, наравне со `staff-aug`, `mid-market`,
  `startup-p2` и `agency-tech`. Запросы под соло/фриланс/контрактных технических
  рекрутеров идут в каждый прогон lead-hunter, а не по остаточному принципу.
- **Оговорка "со своей клиентской базой" НЕ является гейтом.** Работаем всех
  фракциональных независимо от того, подтверждена книга клиентов или нет.
  Score 2 не повод не касаться человека.

Тег в таблице остаётся `independent-fractional (P1)`.

### Что это меняет в залоченном наборе

Активные сегменты теперь: `staff-aug` (спирхед), `mid-market`, `startup-p2` /
`p2-startup`, `agency-tech` (срез hands-on владельца / чемпиона) и
**`independent-fractional`**.

В цифрах на 2026-08-07: было 353 строки из 775 в наборе, стало 393. Сразу
возвращаются в работу 9 человек в `connected` (первый DM) и 11 в `contacted`
(очередь follow-up), плюс 14 в `invited` и 3 в `new`.

### Что НЕ изменилось

Список сегментов вне набора от 2026-08-06 действует как был, за вычетом
`independent-fractional`: `p2-inhouse-TA`, `inhouse-recruiter`, `in-house TA (IT)`,
`out-of-icp`, `investor`, `partner-channel`, `amplifier`, `unclassified`,
`recruiter-misc (verify)`. Правило "статус в воронке не перебивает сегмент" тоже
остаётся.

Снятые углы остаются снятыми: identity-fraud, web3/crypto как фронт,
investor-bigtech на паузе до появления кейсов.

### Расхождение в скилле, которое это объясняет

`sales-brain/references/crm-format.md` уже описывал фракционального рекрутера со
своей базой как score 5 ("partner-network fit") - то есть справочник скилла был
ПРАВ, а репозиторий отставал. Теперь они согласованы, и именно оттуда брались
score 4-5 у соло-рекрутеров при прогонах 31 июля.

### Гардрейл из `icp-priority.md` - на всякий случай

Это решение принято Алексеем как владельцем стратегии, а НЕ выведено из
статистики ответов. Правило "не переруливай ICP на горстке ответов" остаётся в
силе: два ответа от фракциональных 2026-08-06 - это не доказательство, и ссылаться
на них как на обоснование не нужно.

---

## Update 2026-08-07 (b), by Alexey: `p2-inhouse-TA` возвращается в активный набор.

Решение Алексея, принято при разборе входящего коннекта (Senior TA Partner в продуктовой
компании, Стокгольм). Отменяет исключение сегмента, введённое 2026-08-06.

**`p2-inhouse-TA` снова активен.** Внутренние рекрутеры и TA-партнёры в продуктовых
компаниях - валидная цель, их можно хантить и им можно писать.

### Что это меняет

Активные сегменты теперь: `staff-aug` (спирхед), `mid-market`, `startup-p2` / `p2-startup`,
`agency-tech` (срез hands-on владельца / чемпиона), `independent-fractional` и
**`p2-inhouse-TA`**.

В таблице на 2026-08-07 это 24 строки. Они возвращаются в очереди касаний и в хантинг
lead-hunter. Те из них, кто был запаркован 2026-08-06 по правилу "сегмент важнее статуса",
подлежат разбору: парковка была следствием исключения, которого больше нет.

### Известное возражение по этому сегменту - учитывать при написании

`icp-priority.md` фиксирует, почему сегмент когда-то вывели: внутренний рекрутер в крупной
компании **боль чувствует, но решение не принимает** ("I'm not the right person for the
decision" - реальный ответ из поля, см. `objections.md`, mariam-tsitelashvili).

Это не отменяет решение, но задаёт форму сообщения: **не продавать в лоб, а разговаривать
как с практиком.** Вопрос про то, где их скрин перестаёт быть надёжным, работает лучше
питча. Путь к сделке здесь через внутреннего чемпиона, а не через прямую покупку - и это
надо держать в голове, оценивая конверсию по сегменту: ответы будут, быстрых сделок может
не быть.

### Список исключённых сегментов после этого решения

Вне набора остаются: `inhouse-recruiter`, `in-house TA (IT)`, `out-of-icp`, `investor`,
`partner-channel`, `amplifier`, `unclassified`, `recruiter-misc (verify)`, `agency-generic`.

Обрати внимание: `inhouse-recruiter` и `in-house TA (IT)` - отдельные теги от
`p2-inhouse-TA`, и они НЕ возвращаются этим решением. Если имелись в виду и они,
это надо записать отдельно.

---

## Update 2026-08-17, by Alexey: НОВАЯ КАРТА СЕГМЕНТОВ - 9 слагов вместо 24 меток.

Решение Алексея: две недели гоним аутбаунд по сегментам и меряем отклик по каждому;
если отклика нет - меняем сегменты. Для этого 24 накопившиеся метки `icp_segment`
схлопнуты в 9 канонических слагов. 17.08.2026 вся таблица (899 строк, 832 правки)
переразмечена по этой карте; старое значение каждой строки сохранено в
`icp_segment_raw`. Карта сегментов (слаг, название, описание, приоритет, отклик)
живёт в новом табе `segments` той же Google-таблицы.

### Словарь - ЕДИНСТВЕННЫЕ допустимые значения `icp_segment` для новых рядов

Проверяемые гипотезы: **H1** - внешние (не-инхаус) рекрутеры покупают;
**H2** - малые компании с небольшим инженерным отделом (тип Control Plus) покупают.

| слаг | кто это | гипотеза | приоритет |
|---|---|---|---|
| `rec-agency-tech` | тех. рекрутинговое агентство (срез hands-on владельца/чемпиона) | H1 | A - активно гнать |
| `rec-fractional` | независимый / фракционный / соло тех. рекрутер | H1 | A - активно гнать |
| `smb-inhouse` | малая компания, нанимающая инженеров себе (founder/CTO/TA) | H2 | A - активно гнать |
| `rec-agency-small` | универсальное агентство до ~50 чел | H1 | B - второй эшелон |
| `rec-staff-aug` | аутстафф / dev shop / talent marketplace (vetting = их продукт) | H1 | B - второй эшелон |
| `rec-agency-large` | универсальное агентство 51+ | - | C - морозить (0% reply) |
| `partner` | инвесторы, канальные партнёры, усилители | - | C - не для продаж |
| `needs-icp` | не отскорен / требует проверки | - | скоринг до любого касания |
| `out-of-icp` | осознанно исключён | - | не трогать |

Старые метки в `icp_segment` больше НЕ ПИШУТСЯ. Тонкая деталь (размер агентства,
подтип p2-startup vs p2-inhouse-TA, источник TeamTailor и т.п.) при скоринге нового
лида записывается в `icp_segment_raw`.

Маппинг старое -> новое: agency-tech, agency-tech (TeamTailor) -> `rec-agency-tech`;
agency-generic и (1-10), (11-50) -> `rec-agency-small`; agency-generic (51-200),
(201-500), (500+) -> `rec-agency-large`; staff-aug -> `rec-staff-aug`;
independent-fractional, independent-fractional (P1) -> `rec-fractional`; p2-startup,
p2-inhouse-TA, inhouse-recruiter, in-house TA (IT) -> `smb-inhouse`; partner-channel,
investor, amplifier, p2-adjacent -> `partner`; (пусто), unclassified, recruiter-misc,
recruiter-misc (verify), mid-market -> `needs-icp`; out-of-icp, disqualified ->
`out-of-icp`.

### Что это меняет относительно решений 2026-08-06 / 08-07 - явные развязки

1. **`agency-generic` (малые) возвращается в набор как `rec-agency-small`,
   приоритет B.** Основание - решение Алексея по карте 17.08; данные (20% reply на
   20 contacted, у 1-10 и 11-50 лучший отклик в базе) - иллюстрация, не обоснование:
   гардрейл "не переруливать ICP на горстке ответов" помним, выборка мала. Крупные
   (51+) остаются вне работы как `rec-agency-large`.
2. **`inhouse-recruiter` (7 чел) и `in-house TA (IT)` (1 чел) влиты в `smb-inhouse`
   и тем самым ВОЗВРАЩЕНЫ в активный набор** - update 2026-08-07 (b) их не возвращал,
   это отдельное следствие новой карты. Если кто-то из них сидит в крупной компании
   (не малой), при первом касании переразметить в `needs-icp` через `icp_segment_raw`.
3. **Фронт `mid-market` (non-tech, строящие инженерный отдел) слота в карте не имеет
   и на две недели теста ПРИОСТАНОВЛЕН** - он вне обеих гипотез. Единственная строка
   (Topaz Rabi Einy, Semperis) ушла в `needs-icp`. Если фронт возобновляется, для
   него заводится отдельный слаг (например `midmarket-inhouse`) отдельным решением.
4. **`rec-staff-aug` формально спирхедом быть перестаёт** - на две недели теста
   основной удар по трём сегментам A. Спирхед-логика от 2026-07-29 не отменена, а
   отложена: сегмент почти не тронут (2 contacted), вернёмся после теста.

### Правила на две недели теста (до ~2026-08-31)

- Хант и первые DM - только сегменты **A**; **B** - по остаточной квоте;
  C / needs-icp / out-of-icp - не хантить, не писать.
- Правило "сегмент важнее статуса" (2026-08-06) действует в новом словаре:
  вне очереди касаний = `rec-agency-large`, `partner`, `out-of-icp`, а `needs-icp` -
  до скоринга.
- Мерило теста: reply-rate по каждому из A/B сегментов (pipeline считает по
  `segments`-табу). Решение о смене сегментов - после окна, не на 2-3 ответах.

**Hard disqualifiers без изменений: никаких лидов из Украины (UA) и России (RU);
personal-network denylist от 2026-08-06 (b) действует.**

---

## Update 2026-08-21, by Alexey: RU/UA hard-stop is about the EMPLOYER, not the person's city.

Clarification of the 2026-07-18 (UA) and 2026-07-25 (RU) hard disqualifiers: the
stop applies when the COMPANY we would contract with is based in Russia or Ukraine.
A person physically located in RU/UA who works for a company incorporated elsewhere
(first case: Evgeny Konechnyi, Head of Engineering @ Uzum Market - Uzbekistan,
person in St Petersburg) is allowed, scored on normal ICP rules. Note the person's
location in `icp_reason` so the exception is visible.

---

## Update 2026-08-28, by Alexey: ПЕРВЫЙ КЛИЕНТ ЕСТЬ, и он пришёл по реферáлу. Смена оффера и канала.

Решение принято по итогам разбора двухнедельного окна теста сегментов (17-31.08)
и появления первого платящего клиента. Это самая крупная развязка с 29.07.

### Факт, который меняет рамку

**CTRL+ (контракт через Kleos, бывш. Stape) - первый платящий клиент.** Пакет
10 интервью за 750 EUR (75 за штуку), 50% предоплата. Проведено 4 интервью,
из первых трёх один сильный сеньор и два крепких мида, подававшихся сеньорами.
**Клиент нанял.** Карточка: `crm/accounts/ctrl-plus.md`.

**Он пришёл по рекомендации Алины К.**, внешнего рекрутера, для которого CTRL+
давний работодатель. НЕ из холодного аутбаунда. На тот момент воронка
насчитывала 989 инвайтов и 342 первых DM с нулём продаж.

### Замер окна теста 17-24.08 (первые DM, у которых было >=4 дня на ответ)

| сегмент | DM | ответов |
|---|---|---|
| rec-staff-aug | 16 | 0 |
| rec-agency-small | 15 | 0 |
| rec-agency-tech | 13 | 0 |
| rec-fractional | 11 | 0 |
| **итого H1 (рекрутеры)** | **55** | **0** |
| smb-inhouse (H2) | 11 | 1 |
| partner | 13 | 3 |

### Решения

**1. H2 подтверждена деньгами, H1 не подтверждена.**
CTRL+ - ровно форма H2: продуктовая компания с небольшим инженерным отделом,
своего технического интервьюера под нужный стек нет. H1 за всё время: 202
первых DM по четырём рекрутерским сегментам, ноль продаж.

**2. Продукт для холодного касания - Линия 1, техническое интервью как услуга.**
Линия 2 (платформа HireSignal) СНИМАЕТСЯ с холодных касаний и остаётся апсейлом
после первого проданного интервью, когда у клиента появился объём. Основание:
всё, что продалось или движется - Линия 1; всё, что отбито (скоринг, экономия
часов на скрининге, таксономия смежных скиллов, "90 инструментов и 5 ATS") -
Линия 2.

**3. Оффер по рекрутерским сегментам меняется с продуктового на партнёрский.**
Касается `rec-agency-tech`, `rec-fractional`, `rec-agency-small`,
`rec-staff-aug`. Ноль из 55 - это провал продуктового питча, а не провал
аудитории. Тестировать на уже имеющемся: 36 коннектов, готовых к первому DM, и
196 просроченных фолоапов. **Новых инвайтов под этот тест не отправлять.**

**4. Сегмент `partner` переводится из приоритета C ("не для продаж") в
приоритет A** как основной канал. Текущая карта прямо запрещала продавать
единственному сегменту, который отвечает.

**5. ГЛАВНОЕ: канал - не партнёрская программа, а тёплый реферал.**
Три человека подряд отказались от роли партнёра и в том же разговоре предложили
рекомендовать: Алина К. ("я не вот прям рекрутер"), Ольга Ципрусе (уточнила,
что её профиль - HR-стратегия, не сорсинг), Наталья Лалова ("на что-то
подписываться не готова, а вот матчить - да", и сама попросила реферальную
схему). Программу надо продавать и объяснять; реферал - это вопрос "кому из
твоих знакомых это нужно", заданный тому, кто уже видел результат.
**Приоритет смещается на систематический сбор рефералов у тех, кто видел
результат**, впереди холодного хантинга.

**6. Правило "каждый первый DM несёт ссылку на живой борд" ОТМЕНЯЕТСЯ для
партнёрского касания.** Борд - актив Линии 2, в партнёрском питче не к месту
(показывает не ту услугу), плюс отдельный риск отказа от ссылок
(см. `objections.md`, Tika Sharubanashvili). Актив партнёрского касания -
пересылаемый абзац из `partner-program.md`.

**7. Обязательный шаг доставки, доказанный на CTRL+: план интервью
согласуется с техлидом клиента ДО первого кандидата.** Костя Смирнов убрал
алгоритмическую секцию, зарубил лайв-кодинг как отпугивающий, добавил сценарий
про конкурентный переход workflow. Без этой калибровки было бы "интервью по Go
вообще". Это та самая диагностическая встреча из `partner-program.md`, теперь
подтверждённая.

**8. Открытый вопрос "10% против наценки сверху" закрывается в пользу 10%
(модель A, rev share).** При наценке партнёру надо назвать цену заранее и
фиксированно, что ломает механику "цена после диагностики", и он же должен
вести продажу. Урок Ольги Ципрусе: реферер, которому надо объяснять продукт,
не реферит.

**9. Разблокировка каналов - на треть.** Условие "нужны 2-3 анонимизированных
кейса" (решение 29.07 по акселераторам, сетям фракциональных CTO и VC-каналу)
выполнено на один кейс, и кейс с состоявшимся наймом.

### Что НЕ меняется

Жёсткие дисквалификаторы по RU/UA (по работодателю, уточнение 21.08),
personal-network denylist от 06.08, снятые углы (identity-fraud, web3/crypto),
гардрейл "не переруливай ICP на горстке ответов". Сегменты
`rec-agency-large`, `out-of-icp` остаются вне работы, `needs-icp` - до скоринга.

### Сопутствующая правка

Keilian Knudsen (Pangea.ai) переклассифицирован из `rec-agency-small` в
`rec-staff-aug` и поднят с `lost` до `replied`: 28.08 вернулся сам после трёх
месяцев тишины. Карточка `crm/keilian-knudsen.md`. Отдельно показателен факт:
единственный живой контакт в `rec-staff-aug` - тёплый, из мая, при 16 холодных
DM с нулём ответов в окне теста. Сегмент не мёртв, мёртв холодный заход в него.
