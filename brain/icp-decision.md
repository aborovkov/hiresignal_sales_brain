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
