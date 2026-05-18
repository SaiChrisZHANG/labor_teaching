# Assignment, Wages, Platforms, And Pricing Rules

## Learning Objectives

By the end of the week, students should be able to:

1. distinguish visibility, assignment, pricing, and monitoring rules as separate labor-market design objects;
2. write a compact framework in which an intermediary chooses rules that affect allocation, bargaining power, risk, and worker welfare;
3. explain why platform rules can reduce information frictions while also shifting surplus or risk onto workers;
4. translate algorithmic design questions into empirical labor papers with measurable margins and explicit counterfactual rules;
5. design a bounded empirical exercise using randomized disclosure, ranking, guarantee, wage-rule, or platform-policy variation.

## Opening Orientation

Week 4 studies labor markets where assignment, pricing, and evaluation are not passive outcomes of decentralized search. They are designed by an intermediary, platform, employer, or public organization. Online labor markets, hiring platforms, app-based work, and structured wage systems make this visible: a rule determines who sees which jobs, which workers receive attention, how wages are displayed or negotiated, how quality is inferred, how work is monitored, and who bears demand risk.

The central question is this: how do assignment algorithms, platform rules, and wage-setting systems shape labor allocation and worker welfare?

:::{admonition} Core points
:class: important

- Assignment, ranking, wage posting, commissions, monitoring, and reputation systems are labor-market institutions, not neutral technical details.
- Platform rules can improve information, trust, and matching, but the same rules can reallocate bargaining power, surplus, risk, and future opportunity.
- A useful framework separates four choices: visibility or ranking, matching or assignment, wage or price rules, and monitoring or evaluation rules.
- Applied papers in this area should name the exact rule, the labor margin it moves, the counterfactual design, and the worker welfare object.
- Frontier evidence often comes from platform A/B tests, randomized information disclosure, randomized recommendations or guarantees, wage-rule experiments, policy redesigns, and surveys or conjoint designs about platform governance.

:::

## Bridge

Week 3 studied contracts inside employment relationships. Week 4 moves outward to labor markets where contracts, wages, and evaluation are mediated by platforms or other intermediaries. The same hidden objects remain: type, effort, quality, commitment, risk, and outside options. The design lever changes. Instead of only choosing a pay formula inside a firm, the intermediary chooses which workers and jobs become visible, how tasks are routed, what wage or price information is displayed, which commissions or floors apply, and how reputation or monitoring disciplines behavior.

This bridge matters for labor economics because platform rules jointly shape search, matching, wage setting, supervision, and worker welfare. A platform is not only a technology provider. It is a labor-market institution that changes who gets access to work, how pay is formed, and how risk is distributed.

## Field Core

### Platforms And Intermediaries As Labor-Market Designers

An intermediary can affect the labor market at several stages:

- whether workers and employers find each other at all;
- which opportunities are displayed, hidden, ranked, recommended, or delayed;
- whether workers bid, bargain, accept a posted wage, face a wage floor, or pay a commission;
- how quality is summarized through ratings, histories, tests, guarantees, or salary information;
- how disputes, cancellations, penalties, deactivation, and monitoring are handled.

The intermediary's objective therefore matters. A platform may care about fill rates, revenue, growth, buyer trust, worker retention, liquidity, legal risk, or market share. Those objectives need not coincide with worker surplus or long-run matching efficiency. A ranking rule can improve buyer trust while making new workers less visible. A wage floor can raise accepted pay for some jobs while reducing postings or changing worker entry. A monitoring rule can reduce shirking while increasing stress, deactivation risk, and income volatility.

```{include} assets/tables/04-core-design-concepts-map.md
```

### A Compact Rule Framework

Let a platform or intermediary choose a rule vector

```{math}
:label: eq:week4-rule-vector
\rho = (V, A, P, M),
```

where {math}`V` is a visibility or ranking rule, {math}`A` is a matching or assignment rule, {math}`P` is a wage, price, commission, or pay-transparency rule, and {math}`M` is a monitoring, evaluation, reputation, or governance rule. Workers differ in type {math}`\theta_i`, availability {math}`a_i`, outside option {math}`b_i`, risk tolerance {math}`r_i`, and preferences over flexibility and job quality. Jobs or clients differ in task value, urgency, quality requirements, and willingness to pay.

Worker welfare can be summarized as

```{math}
:label: eq:week4-worker-welfare
W_i(\rho) =
\mathbb{E}[w_i(\rho)]
- c_i(e_i, a_i)
- \lambda_i \operatorname{Var}(w_i(\rho))
+ \phi_i \text{Flex}_i(\rho)
+ q_i(\rho)
- s_i(\rho),
```

where expected earnings, effort or time costs, earnings risk, flexibility, match quality, and search or monitoring burden all depend on the rules. The platform's objective may be written schematically as

```{math}
:label: eq:week4-platform-objective
\max_{\rho} \; \Pi(\rho)
= \text{fees}(\rho)
+ \text{future market thickness}(\rho)
+ \text{trust}(\rho)
- \text{operational and legal costs}(\rho),
```

subject to participation by workers and employers, incentive compatibility, information constraints, and platform governance constraints. This is not meant to dominate the lecture. Its purpose is organizational: whenever a paper studies an algorithmic or platform rule, students should ask which component of {math}`\rho` changed and which part of {math}`W_i(\rho)` moved.

The same rule can have multiple effects. A worker guarantee may reveal quality, increase visibility, shift buyer beliefs, change wage bids, and make future jobs easier to obtain. A dynamic price multiplier may attract workers to high-demand times, but it may also move demand risk onto workers and make pay less predictable. A recommendation algorithm may reduce search costs while concentrating opportunity among already-visible workers.

### Assignment, Ranking, And Visibility

The first design object is visibility. Workers usually do not observe a neutral market menu. They see jobs through search results, alerts, recommendation systems, invitation rules, and filters. Employers likewise see workers through rankings, ratings, endorsements, credentials, and application pools shaped by platform design.

Applied papers make this concrete. Pallais studies an online labor market experiment in which treated inexperienced workers received public evaluations, improving future employment and wage outcomes by changing information and effective visibility [@pallais2014]. Horton studies algorithmic labor-market recommendations as a field experiment, showing how platform recommendations can redirect attention and hiring [@horton2017]. Barach and Horton study steering in online markets, where a platform guarantee changes buyer trust and allocation because the platform signal is informative and credible [@barachHorton2019steering].

The labor-economics lesson is that assignment is often partly algorithmic and partly informational. A strong empirical paper separates:

- the mechanical exposure effect of being shown or ranked higher;
- the belief effect induced by platform signals, ratings, guarantees, or histories;
- the response of workers and employers to the new information environment;
- the equilibrium effect on congestion, wages, and future opportunity.

### Wage-Setting, Price Rules, Commissions, And Transparency

The second design object is compensation. Platform labor markets and online hiring systems differ in whether they use posted wages, bids, bargaining, commissions, price floors, dynamic pricing, pay transparency, or structured pay scales. These are not cosmetic details. They affect who applies, how workers target search, how employers screen, whether workers bear demand risk, and how surplus is divided.

Online job posts often contain little wage information, making wage opacity itself a search friction [@batraTaska2023wageInfo]. Pay-transparency rules in postings can change wages, applicant behavior, and the information environment [@arnoldQuachTaska2025payTransparency]. Employers can use compensation history in online labor markets in ways that shape offers and sorting [@barachHorton2021compensationHistory]. Wage-floor and minimum-wage experiments on platforms are especially valuable because they vary a pay rule directly rather than treating wages as an equilibrium residual [@horton2025minimumWage].

Gig and ride-hailing settings add dynamic pricing and commission rules. Drivers may value schedule flexibility, but platform-mediated pricing also changes earnings predictability, the timing of work, and who bears demand fluctuations. Evidence on Uber drivers emphasizes the value of flexible work and the importance of interpreting platform labor supply through both wages and nonwage job attributes [@chenChevalierRossiOehlsen2019; @hallKrueger2018analysis]. Algorithmic wage-setting in ride-hailing raises a neighboring question: when does personalized or dynamic pricing allocate workers efficiently, and when does it discipline labor supply or extract surplus [@chenLuoYuan2023drivingDrivers]?

### Worker Welfare, Flexibility, And Risk

Worker welfare in platform labor markets is broader than average hourly earnings. The relevant object may include:

- total earnings and hourly pay;
- earnings volatility and downside risk;
- unpaid search, waiting, and travel time;
- flexibility over when and where to work;
- autonomy over accepting tasks;
- deactivation or rating risk;
- access to future jobs and reputation accumulation;
- bargaining power against employers, clients, or the platform.

This distinction is not decorative. A platform rule can increase average match quality while worsening earnings volatility. It can increase task completion while making workers absorb cancellation risk. It can make flexible work more valuable for some workers and less secure for others. It can reduce employer uncertainty while stratifying workers by early ratings or platform-curated reputation.

Stanton and Thomas study who benefits from online gig economy platforms, making the surplus-distribution question explicit [@stantonThomas2021whoBenefits]. Davis and Samaniego de la Parra examine application flows, which helps students connect platform design to the observable recruiting funnel rather than only to final hires [@davisSamaniego2024applicationFlows]. Together these papers push students to ask whether the platform is reducing frictions, reallocating attention, changing bargaining power, or all three.

### Platform Governance, Market Power, And Rule Incidence

Assignment and pricing rules are also governance rules. A platform that controls search rankings, ratings, pay formulas, fees, dispute resolution, and deactivation procedures can alter the division of rents even when measured match quality improves. That is why this week treats platform governance as a labor-market design issue rather than as background institutional detail.

The incidence question should be stated directly:

- Which workers gain visibility, and which workers become harder to find?
- Does a pay rule raise worker earnings, reduce employer demand, increase platform fees, or change hours?
- Does reputation reduce adverse selection or lock workers into early noisy ratings?
- Does flexibility represent worker surplus, platform-side risk shifting, or both?
- Does monitoring improve quality, or does it discipline workers through opaque penalties and deactivation risk?

Answering these questions requires evidence on margins before final outcomes: applications, invitations, rankings, wage bids, acceptance rates, posted wages, commissions, hours online, waiting time, ratings, disputes, deactivations, and repeat work.

### How Algorithm Design Becomes An Empirical Labor Paper

A platform-design question becomes an applied labor paper when the algorithmic rule is translated into a labor margin and a counterfactual.

**1. Name the rule.** Is the paper studying visibility, ranking, recommendation, assignment, reputation disclosure, wage transparency, commission changes, price floors, guarantees, monitoring, or deactivation?

**2. Name the labor margin.** Does the rule affect applications, invitations, interviews, hires, wage bids, accepted wages, hours, task acceptance, retention, ratings, future jobs, volatility, or worker exit?

**3. State the counterfactual design.** What would workers and employers have seen or faced under the old rule? What information, ranking, price, or monitoring regime changed?

**4. Separate mechanism from incidence.** A rule may improve match quality and still shift surplus. The design should distinguish information, attention, bargaining power, risk allocation, and selection.

**5. Define welfare.** The paper must say whether welfare means match surplus, worker surplus, employer surplus, platform revenue, earnings stability, flexibility, fairness, or access to future opportunity.

```{include} assets/tables/04-theory-to-empirical-bridge.md
```

### Threats To Interpretation

Several threats recur across the literature.

**Information versus attention.** A disclosure treatment may change employer beliefs, but it may also mechanically place workers in front of more employers.

**Short-run treatment effects versus equilibrium design.** A ranking or wage experiment may identify a local treatment effect but not the long-run effect once all workers and employers adapt.

**Average earnings versus welfare.** Earnings can rise while risk, waiting time, monitoring burden, or loss of autonomy also rises.

**Platform objective versus worker welfare.** Rules chosen to maximize fill rates, commissions, or buyer trust may not maximize worker surplus.

**Selection into platform work.** Observed platform workers are selected on outside options, preferences for flexibility, liquidity needs, risk tolerance, and access to other jobs.

**Opaque rule changes.** Platforms may redesign several rules at once, bundling ranking, information, pricing, and governance changes.

These threats are why the rule vector is useful. It prevents the paper from treating "the algorithm" as one object and forces the researcher to say which rule changed and which labor margin identifies the mechanism.

## Research Lab

The Week 4 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Pallais because it turns a platform information and visibility intervention into a clear applied labor design: a small public signal for inexperienced workers changes future hiring outcomes in an online labor market [@pallais2014]. The challenge anchor is Barach and Horton on platform steering and guarantees because it shows how a platform rule can redirect buyer attention through trust and credibility [@barachHorton2019steering]. Students who want a wage-rule extension can transfer the same logic to pay transparency, compensation history, or platform minimum-wage experiments [@barachHorton2021compensationHistory; @arnoldQuachTaska2025payTransparency; @horton2025minimumWage].

The lab is not an official replication package for any paper. It uses deterministic synthetic teaching data to preserve the logic of information, assignment, and wage-rule designs without claiming access to proprietary platform records, confidential A/B tests, or official replication files.

**Reproduce.** Students recreate a reduced visibility and information result: inexperienced workers receiving a public signal or ranking lift have higher employer invitations, hire rates, accepted wages, and future jobs in the synthetic online labor-market data.

**Diagnose.** Students decompose the reduced effect into assignment exposure, information or belief updating, wage changes, future reputation accumulation, and worker risk. They classify what is observed directly and what remains latent: employer beliefs, worker type, platform objective, bargaining power, and welfare.

**Transfer.** Students adapt the same architecture to one neighboring platform rule: platform guarantees or steering, recommendation rankings, compensation-history disclosure, wage transparency, minimum pay rules, dynamic pricing in ride-hailing, or deactivation and dispute governance. The transfer memo must state the rule, labor margin, counterfactual design, identification strategy, welfare object, and main threat.

```{include} assets/tables/04-reading-and-lab-map.md
```

## Methods Box

:::{admonition} Methods Box: Frontier Experimental Designs For Platform Labor Markets
:class: note

**Platform A/B tests.** Randomize ranking, search order, application prompts, visibility, recommendations, or matching rules. These designs identify the direct effect of the coded rule, but short-run experiments may miss equilibrium adaptation.

**Randomized information or reputation disclosure.** Reveal ratings, histories, credentials, wage information, or employer messages to subsets of users. These designs are powerful when information is the intended mechanism, but they often bundle learning, visibility, and sorting [@pallais2014].

**Randomized recommendation, guarantee, or ranking interventions.** Randomize platform steering, guarantees, badges, endorsements, or invitations. These designs help separate trust and attention from underlying worker quality [@barachHorton2019steering; @horton2017].

**Wage-floor or pay-rule experiments.** Randomize posted minimum wages, price floors, bidding rules, commissions, bonus formulas, or transparency requirements. These designs connect directly to wage-setting, but large-scale interventions can create spillovers across workers and employers [@horton2025minimumWage].

**Natural experiments from platform policy changes.** Use staggered rollouts, jurisdictional changes, eligibility thresholds, or rule redesigns in wage posting, platform fees, matching algorithms, deactivation procedures, or transparency rules [@arnoldQuachTaska2025payTransparency].

**Survey, conjoint, and lab-in-the-field designs.** Elicit worker and employer preferences over flexibility, fairness, transparency, algorithmic management, or algorithm aversion. These designs are useful for welfare interpretation, especially when administrative data do not reveal preferences directly.

:::

```{include} assets/tables/04-frontier-methods-box.md
```

## Reading Ladder And References

**Core platform and information papers.** Start with Pallais on information and entry-level online hiring, Stanton and Thomas on online hiring intermediaries, Horton on algorithmic recommendations, and Barach and Horton on steering and guarantees [@pallais2014; @stantonThomas2016; @horton2017; @barachHorton2019steering].

**Assignment, messages, and application flows.** Use Horton, Johari, and Kircher for employer messages, search targeting, and wage bids; Davis and Samaniego de la Parra for application flows; and Barach and Horton for compensation history in online labor markets [@hortonJohariKircher2024sorting; @davisSamaniego2024applicationFlows; @barachHorton2021compensationHistory].

**Wage information, transparency, and pay rules.** Use Batra and Taska for wage information in online job posts, Arnold, Quach, and Taska for pay transparency, Cullen for the broader pay-transparency map, and Horton for platform minimum-wage experimentation [@batraTaska2023wageInfo; @arnoldQuachTaska2025payTransparency; @cullen2024; @horton2025minimumWage].

**Gig work, flexibility, and worker welfare.** Use Chen, Chevalier, Rossi, and Oehlsen on the value of flexible work, Hall and Krueger on Uber drivers, Stanton and Thomas on who benefits from gig platforms, and Chen, Luo, and Yuan for algorithmic wage-setting in ride-hailing [@chenChevalierRossiOehlsen2019; @hallKrueger2018analysis; @stantonThomas2021whoBenefits; @chenLuoYuan2023drivingDrivers].

## Exercises And Discussion Prompts

1. Why is a ranking rule a labor-market institution rather than a technical detail?
2. Give one example of a platform rule that improves information while reducing worker bargaining power.
3. In a randomized information-disclosure experiment, how would you separate employer learning from mechanical visibility?
4. How is a randomized wage-rule experiment different from a randomized recommendation experiment?
5. In ride-hailing, when is flexibility a worker amenity and when is it a channel for risk shifting?
6. Choose a platform rule. Name the rule, the labor margin, the counterfactual, the identification strategy, the welfare object, and the main threat.
7. What data would you need to distinguish platform revenue maximization from worker welfare improvement?
8. How should a paper report effects when average earnings rise but earnings volatility and deactivation risk also rise?

## Reproducibility And Code Lab Note

The Week 4 code lab lives at `labs/04-assignment-wages-platforms-and-pricing-rules/`. It is a bounded synthetic teaching path, not an official replication of Pallais, Barach and Horton, Horton, Johari, and Kircher, or any platform's internal experiment. The smoke path creates deterministic online labor-market data; reproduces a compact information and visibility summary; diagnoses assignment exposure, employer beliefs, wage changes, reputation accumulation, and risk; and writes transfer prompts for steering, pay transparency, wage floors, dynamic pricing, and governance.

The lab is conservative by design. It does not claim access to proprietary platform logs, confidential A/B tests, official replication packages, worker location traces, or platform pricing code. Its goal is to help students practice how a platform-rule change becomes an empirical labor design.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-assignment-wages-platforms-and-pricing-rules.tex`. The deck mirrors the chapter structure without duplicating the prose: it opens with platforms as labor-market designers, introduces the rule-vector framework, separates visibility and assignment from pricing and governance, connects platform rules to worker welfare, and closes with frontier experimental methods and the Research Lab workflow.

## Bridge Forward

Week 5 moves from platforms and algorithmic rule design to professional and public-sector labor markets. The bridge is that both settings require explicit design choices under fairness, transparency, and staffing constraints. Week 4 asks how platforms choose visibility, assignment, pricing, and governance rules; Week 5 asks how public and professional institutions choose assignment rules when legitimacy, priority, equity, and service quality are first-order labor-market objectives.
