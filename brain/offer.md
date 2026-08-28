# OFFER.md

> **TODO / DRAFT.** What we actually sell, the entry motion, and pricing.
> ⚠️ Depends on the open question: **HireSignal = StepUp rebrand, or separate service play?** If rebrand, the offer is the SaaS product + service wrapper. If separate, define the standalone offer. Resolve before quoting anyone.

---

# What We Sell

Framed as outcomes, not tooling (see `positioning.md` → "What We Actually Sell"):

* confidence in engineering evaluation
* stronger, more consistent hiring signal
* structured technical assessment
* interviewer calibration consistency
* reduction of false positives

Concrete deliverable form — **near-term answer (2026-07-29, Alexey): service-led / done-with-you.** The reliable asset today is the founder's evaluation judgment (1,700 interviews — see `proof.md`), NOT an automated product metric. So the near-term motion is: the expert reads capability, the product assists; we sell the expertise, the product hardens behind it. This pragmatically resolves the platform-vs-service question for now (revisit once the product's signal is provably reliable on its own). **Do NOT put identity-fraud / "we catch fakes" detection in the offer** — the product does not reliably deliver it (see `positioning.md` → "AI-Era Identity Fraud - PARKED").

---

# Entry Motion — Free-Sample Wedge (agreed)

Thin-wedge pilot to earn trust before any commercial ask:

* Process a batch of **real resumes against one real JD**, free, fast turnaround.
* Output demonstrates signal quality and calibration on the prospect's own data.
* Upsell path: ATS integration (e.g. Teamtailor) + ongoing screening.

TODO: lock exact wedge parameters (resume count, turnaround SLA, what the deliverable looks like).

---

# Pricing — ОТКРЫТЫЙ ВОПРОС НОМЕР ОДИН (обновлено 2026-08-28)

> ⚠️ **Якорь "~$1,000/month за ~100 кандидатов" СНЯТ 2026-08-28.** Он никогда не
> был подтверждён, ни разу не был продан и описывает модель (подписка за объём),
> которой у нас нет. Не называть, не воскрешать без отдельного решения.

## Что реально происходило с ценой

Четыре несовместимые цены ходили одновременно. Это не сегментация, это
случайность, и первый же партнёр, который спросит "10% от чего", в неё упрётся.

| цена | кому | статус |
|---|---|---|
| **75 EUR за интервью** (пакет 10 за 750, разовое 90) | CTRL+ | **ОПЛАЧЕНО.** Единственная цена, подтверждённая деньгами |
| $200-225 мид / $300-350 сеньор, объём -20-30% | Keilian Knudsen (Pangea), 2026-05-27 | озвучено, не продано |
| $100 transfer price за интервью | Елизавета Иванова, партнёрский трек, 2026-08-19 | принята партнёром, заказа ещё нет |
| ~$1,000/мес за ~100 кандидатов | никому | СНЯТ 2026-08-28 |

Разброс между реальным чеком (75 EUR) и озвученной ценой ($200-350) - **вчетверо**.

## Что решено

* **Единица продажи - одно проведённое интервью.** Не место, не подписка.
* **Продаём пакетами.** Пакетная цена ниже разовой (у CTRL+: 75 против 90),
  добор сверх пакета идёт по пакетной цене.
* **Оплата 50% предоплатой за пакет**, далее отчёт по каждому проведённому
  интервью.
* **Не проведённое по вине кандидата интервью списывается как проведённое.**
  Допустимая отмена - примерно за 4 часа.
* **Цена называется после диагностической встречи**, не в первом касании.
* **Партнёр получает 10% с каждого интервью** (модель A, rev share - решение
  2026-08-28, см. `partner-program.md`).

## Что ещё НЕ решено

* [ ] **Ценовая вилка по грейду и языку.** 75 EUR за интервью на русском против
      $200-350 за англоязычную AI-native оценку - это разные продукты или
      разные цены за одно и то же? Решить до следующего КП.
* [ ] Ориентир диапазона, который можно называть партнёру, чтобы он понимал
      порядок своих 10%.
* [ ] Define wedge → paid conversion trigger.
* [ ] Define integration/upsell pricing.

---

# Objection Coverage

Objection handling lives in `objections.md`. Ensure the offer answers the two known objections: "why not just ChatGPT?" and "these systems are unstable."

---

# Две линии продукта — и они отвечают по-разному `[зафиксировано 2026-08-13, Alexey]`

Это НЕ один продукт с вариантами. Это две разные линии с разной механикой данных.
Путать их в разговоре нельзя: у них противоположный ответ на вопрос про запись.

## Линия 1 — премиум-интервью (сервис)

Наш инженер лично собеседует кандидата, около часа. Живой человек против живого человека.

- Интервью проводим **мы**, в **Zoom**, **с записью**.
- **Копию записи передаём клиенту** вместе с разбором.
- Ответ на «вы записываете?»: **да, и копия ваша** — клиент может проверить любой наш вывод
  по записи. Согласие кандидата на запись берём мы.
- Сила этой линии — верифицируемость: за каждым выводом стоит место в записи.

## Линия 2 — платформа HireSignal

Платформа анализирует кандидатов, собирает список вопросов и отдаёт рекрутёру.
**Собеседование проводит сам рекрутёр**, на своей стороне.

- Звонок наш продукт не трогает. Рекрутёр ведёт его на чём хочет.
- **Запись мы не храним и не получаем.** К нам приходит только текст, который
  рекрутёр решил передать.
- Ответ на «вы записываете?»: **нет, запись остаётся у вас, к нам попадает только
  текст, который вы сами отдали.**
- Сила этой линии — минимальный вход данных. См. `positioning.md` → «Field signal
  2026-08: no recording is a feature» — тот раздел описывает ИМЕННО эту линию.

## Правило для аутрича и для партнёров

Прежде чем отвечать на вопрос про запись, данные или приватность — определи, о какой
линии идёт речь. Ответ, данный не от той линии, будет прямой неправдой, и задаёт его
обычно тот, для кого обработка данных и есть критерий выбора.
