# Contracts, Incentives, Screening, And Moral Hazard

## Opening Orientation / Why This Week Matters

Week 3 moves from market-level allocation to the design of the employment relationship itself. Once a worker and firm are matched, the central problem is no longer only who meets whom. The contract determines which information is revealed, how risk is shared, how effort is elicited, how subjective judgments are used, and how the relationship is sustained when both sides have private information.

The central question is this: how should labor contracts be designed when effort, type, commitment, and multitasking are imperfectly observed?

By the end of the week, students should be able to:

1. write a concise principal-agent model for effort, noise, risk sharing, and incentive provision in employment;
2. distinguish contracts that screen hidden types from contracts that elicit hidden effort;
3. explain why multitasking, subjective evaluation, and relational incentives are central workplace design problems;
4. translate a contract-theory object into an empirical labor design with observed margins, institutional variation, and welfare objects;
5. design a bounded empirical exercise that separates incentive effects from sorting effects.

:::{admonition} Core points
:class: important

- Labor contracts solve multiple problems at once: they screen hidden type, elicit hidden effort, allocate risk, and shape retention and promotion.
- A principal-agent framework is useful because wedges emerge whenever effort, commitment, evaluator behavior, or type are imperfectly observed.
- The best empirical labor papers in this area translate hidden objects into observable margins such as output, attendance, quits, performance ratings, promotions, wage trajectories, and task mix.
- Multitasking, subjectivity, and relational enforcement are not footnotes; they are central reasons why simple performance-pay formulas often fail.
- Welfare is broader than productivity. A contract can raise output while increasing risk, distorting unmeasured work, worsening inequality, or shifting surplus away from workers.

:::

## Bridge

Week 2 studied the recruiting process: applications, interviews, offer timing, and unraveling. Week 3 asks what happens after a match is formed. A match can be efficient in the assignment sense and still destroy surplus if the contract gives poor incentives, screens the wrong workers, misallocates risk, or rewards the wrong signal.

Labor II gives the background personnel-economics language: firms choose pay, supervision, promotion, monitoring, and job design. Contract theory adds the discipline of naming the hidden object. Is the firm trying to learn worker type? Elicit effort? Help the worker commit to a work plan? Reduce gaming? Keep supervisors from rewarding influence rather than production? The labor-economics contribution is to connect those hidden objects to real data and institutional variation inside workplaces.

## Field Core

### A Principal-Agent Baseline For Labor Contracts

Start with a worker who chooses effort {math}`e` at cost {math}`c(e)`, with {math}`c'(e)>0` and {math}`c''(e)>0`. Output depends on effort, worker type, task design, and noise:

```{math}
:label: eq:week3-pa-output
y = f(e,\theta,x) + \varepsilon,
```

where {math}`\theta` is worker type, {math}`x` is job design or task assignment, and {math}`\varepsilon` is noise. The firm would like to condition pay on effort, but effort is costly to observe. The contract therefore conditions compensation on a signal: output, sales, quality, attendance, a supervisor rating, a promotion score, or a composite performance measure.

The standard tradeoff is incentives versus insurance. Let pay be {math}`w(y)=a+by`, where {math}`b` is the incentive intensity. A higher {math}`b` makes effort more valuable to the worker, but it also exposes the worker to output risk:

```{math}
:label: eq:week3-incentives-risk
\max_{a,b} \; \mathbb{E}[y-w(y)]
\quad \text{subject to participation and incentive compatibility.}
```

The participation constraint says the worker must prefer the job to the outside option. The incentive-compatibility constraint says the worker's chosen effort must maximize expected utility given the contract. In labor settings, the relevant outside option may be unemployment, another firm, gig work, a public job, a family constraint, or an internal transfer. That is why the contract cannot be interpreted separately from the labor market around it.

This baseline already shows the main wedge. Stronger measured incentives can raise effort on the rewarded margin, but they also shift risk, attract different workers, and encourage effort substitution when the measure is incomplete.

```{include} assets/tables/03-principal-agent-map.md
```

### Screening, Hidden Type, And Contract Menus

Hidden type is not the same object as hidden effort. A firm may want to learn whether a worker is productive, reliable, patient, collaborative, low-risk, promotable, or able to handle autonomy. Contracts screen types when different workers select into different offers or survive different thresholds.

Labor-market screening devices include probation, promotion ladders, nonlinear bonuses, referral rules, tenure clocks, apprenticeship contracts, benefit menus, schedule flexibility, and high-powered incentive pay. These devices can reveal type before the firm makes a longer commitment. They can also change who enters the firm in the first place.

This is why a pay reform cannot be read mechanically as an effort treatment. Lazear's performance-pay study is the benchmark teaching example because the observed productivity gain combines an incentive channel and a sorting channel [@lazear2000]. Dohmen and Falk show more generally that workers with different traits sort differently into performance-pay environments [@dohmenFalk2011]. The empirical object is therefore not only "did output rise?" but "which workers came, which workers left, and how did the same workers change behavior?"

Screening questions should preserve the distinction between:

- contracts that attract or reveal hidden type;
- contracts that elicit hidden action from a given worker;
- contracts that help sustain effort through monitoring, promotion, or relational enforcement.

### Incentives, Effort, And Measured Productivity

The clearest applied evidence comes from workplaces where output is observed at high frequency: piece-rate production, call centers, retail stores, sales teams, service completion logs, field production, and platform tasks. These settings make effort more measurable, but they do not remove the identification problem. Output still combines effort, ability, technology, task allocation, peer effects, and demand conditions.

Classic and frontier papers use different institutional margins:

- Lazear studies a move from hourly pay to piece rates in windshield installation, separating productivity effects from selection [@lazear2000].
- Bandiera, Barankay, and Rasul use a firm-level experiment to study how incentives for managers change worker outcomes and inequality [@bandieraBarankayRasul2007].
- Friebel, Heinz, Krueger, and Zubanov study team incentives in a retail chain, making peer production and team organization visible [@friebelHeinzKruegerZubanov2017].
- DellaVigna and Pope use experimental variation to compare monetary incentives, non-monetary motives, and expert forecasts about effort [@dellaVignaPope2018].

The central applied lesson is that "effort" is not one empirical object. A contract may raise measured productivity because workers work harder, work longer, change task allocation, learn faster, game the metric, help peers less, or because high-productivity workers sort into the contract. The paper's design must say which channel is being identified.

### Multitasking, Subjective Evaluation, And Relational Incentives

Many jobs have multiple outputs. A teacher teaches testable skills and non-testable skills. A police officer enforces rules and builds trust. A caseworker processes files and helps clients. A manager produces short-run numbers and develops workers. If the contract rewards only what is easy to measure, effort shifts toward measured tasks and away from valuable unmeasured tasks.

The multitask model captures this directly:

```{math}
:label: eq:week3-multitask
y_j = f_j(e_j) + \varepsilon_j,
\qquad j=1,\dots,J.
```

If pay depends strongly on {math}`y_1` but not on {math}`y_2`, workers will over-supply effort on task 1 and under-supply effort on task 2 relative to the firm's objective. Holmstrom and Milgrom make this point central to job design and incentive contracts [@holmstromMilgrom1991]. Baker emphasizes that performance measures create incentives only to the extent that they align with the principal's true objective [@baker1992performance]. Prendergast's survey remains the broad personnel-economics map for these tradeoffs [@prendergast1999].

Subjective evaluation is one response to multitasking. Supervisors may observe dimensions that formal metrics miss: cooperation, judgment, reliability, mentoring, and quality. But subjectivity creates its own agency problem. Workers may reallocate effort toward pleasing evaluators, cultivating influence, or managing impressions. de Janvry and coauthors show how subjective performance evaluation can alter bureaucratic work behavior through influence activities [@deJanvryHeSadouletWangZhang2023].

Relational incentives are another response. Firms often use discretionary bonuses, promotion promises, repeated interaction, or reputational concerns when formal contracts are incomplete. These arrangements can sustain cooperation when courts or formulas cannot verify effort, but they rely on commitment by the firm and credibility for the worker. MacLeod's employment-contracts chapter is useful for connecting law, informal promises, and labor-market performance [@macleod2011GreatExpectations].

### Commitment, Self-Control, And Worker-Side Demand For Contracts

Principal-agent language often starts from the firm's problem, but labor contracts may also solve worker-side commitment problems. Workers may want a schedule, target, penalty, or payment rule that helps them follow through on desired work effort. Kaur, Kremer, and Mullainathan show that self-control at work can make workers demand commitment-style arrangements [@kaurKremerMullainathan2015].

This changes welfare interpretation. A contract that looks high-pressure may reduce worker welfare if it shifts risk or extracts effort. But a contract with commitment features may also help some workers reach their own preferred effort path. The empirical task is to distinguish commitment demand from coercion, liquidity constraints, risk preferences, and sorting.

### How A Contract-Theory Question Becomes An Empirical Labor Paper

A strong empirical paper in this area translates a hidden contracting object into a measurable labor-market design.

**1. What hidden object matters?** The paper should name the object precisely: effort, type, commitment, evaluator favoritism, influence activities, multitasking, peer effects, social preferences, or relational enforcement.

**2. What observable margin is used?** The observable margin should match the hidden object: output per hour, quality-adjusted output, attendance, lateness, quits, contract take-up, task mix, ratings, promotions, wage growth, peer output, or evaluator-specific behavior.

**3. What institutional variation or design identifies the mechanism?** Identification can come from a contract change, randomized incentive experiment, bonus redesign, probation threshold, evaluator assignment, rater rotation, promotion rule, contract menu, platform policy, or matched employer-employee panel.

**4. What competing mechanisms must be separated?** The paper must distinguish incentives from sorting, effort from ability, quantity from quality, output from gaming, evaluator learning from favoritism, and commitment demand from risk or liquidity constraints.

**5. What labor-market welfare object is relevant?** The answer may be productivity, worker surplus, risk exposure, retention, inequality inside firms, organizational output, client welfare, public-service quality, or the division of surplus between worker and firm.

```{include} assets/tables/03-theory-to-empirical-bridge.md
```

### Threats To Interpretation

Several threats recur across the literature.

**Incentives versus selection.** If a new contract changes who enters or exits the firm, the average productivity change cannot be read as an effort effect.

**Measured output versus true performance.** Quantity may rise while quality, safety, cooperation, or client welfare falls.

**Risk shifting.** Higher-powered incentives can increase earnings volatility even when average pay rises.

**Evaluator response.** Subjective ratings may reflect true performance, favoritism, bias, or worker effort directed at the evaluator.

**Equilibrium spillovers.** Team incentives, peer effects, and promotion tournaments can change coworkers' behavior, not only the treated worker's behavior.

**External validity.** A clean incentive experiment in a short-run task may not describe repeated employment relationships with promotion, retention, learning, and informal norms.

These threats are the reason contract theory is useful for applied labor. It forces the paper to say what is hidden, what is observed, and what counterfactual contract would reveal the mechanism.

## Research Lab

The Week 3 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Lazear's performance-pay paper because it turns a contract-theory question into a clear applied labor design: a real pay reform changes measured productivity, but the empirical interpretation must separate effort incentives from worker sorting [@lazear2000].

The challenge anchor is de Janvry and coauthors on subjective performance evaluation because it studies a different hidden object: workers may direct effort toward evaluators when evaluation is subjective [@deJanvryHeSadouletWangZhang2023]. Kaur, Kremer, and Mullainathan provide a second challenge path for students who want to focus on commitment and self-control at work [@kaurKremerMullainathan2015].

The lab is not an official replication package for any paper. It uses deterministic synthetic teaching data to separate incentive effects from sorting effects and then transfers the same logic to subjective evaluation or commitment. This conservative path is deliberate: the repository does not claim access to proprietary firm personnel records or official replication data.

**Reproduce.** Students recreate a reduced performance-pay fact: average output is higher after a move to piece-rate pay. The synthetic data include worker fixed productivity, contract regime, output, pay, tenure, and entry or exit status.

**Diagnose.** Students decompose the output change into within-worker incentive response and workforce-composition change. They then classify which objects are observed directly and which remain latent: effort, type, commitment, task mix, quality, and gaming.

**Transfer.** Students adapt the same empirical architecture to a second hidden-object problem: subjective evaluation and influence activities, or worker demand for commitment contracts. The transfer memo must state the institution, hidden object, observed margin, variation, identification strategy, welfare object, and main threat.

```{include} assets/tables/03-reading-and-lab-map.md
```

## Methods Box

:::{admonition} Methods Box: Measuring Effort, Commitment, Type, And Incentive Response
:class: note

**Output-based administrative data.** Use production logs, sales, call-center records, completed tasks, quality scores, or service metrics when output is measured repeatedly. These data are close to effort but still mix effort, ability, task assignment, demand, and teamwork.

**Contract-change field studies.** Use a firm or platform redesign in pay, bonuses, probation, promotion, or scheduling. These designs are naturally tied to theory but often mix incentives, sorting, and retention.

**Randomized incentive experiments.** Vary pay formula, bonus size, framing, goal, or contract menu experimentally. Experiments strengthen internal validity but may have short horizons and limited external validity.

**Subjective-evaluation audits and evaluator-assignment designs.** Exploit random or quasi-random evaluator assignment, rater rotation, evaluator uncertainty, rating text, or changes in supervisor information. These designs are central for studying favoritism, influence activities, and hidden multitask effort.

**Worker surveys linked to administrative outcomes.** Measure beliefs, risk preferences, stress, self-control, perceived fairness, or commitment demand and connect them to output, attendance, tenure, and contract choice.

**Digital traces, time-use, and attendance records.** Use timestamps, badge swipes, platform activity, time-use logs, scheduling records, or absence data to measure effort timing and discipline. The key warning is that activity is not always productive effort.

**Structural estimation.** Estimate latent effort, type, commitment, or risk-preference parameters when hidden objects are not directly observed. Structural work can discipline counterfactual contracts, but the welfare claims depend on the model and exclusion restrictions.

:::

```{include} assets/tables/03-frontier-methods-box.md
```

## Reading Ladder And References

**Core theoretical framing.** Start with Holmstrom and Milgrom on multitask principal-agent problems, Baker on performance measures, Prendergast on incentives in firms, and Lazear and Rosen on tournaments as labor contracts [@holmstromMilgrom1991; @baker1992performance; @prendergast1999; @lazearRosen1981].

**Core applied labor papers.** Use Lazear for performance pay and sorting, Bandiera, Barankay, and Rasul for incentive design inside firms, Dohmen and Falk for sorting into performance pay, and Friebel, Heinz, Krueger, and Zubanov for team incentives in retail [@lazear2000; @bandieraBarankayRasul2007; @dohmenFalk2011; @friebelHeinzKruegerZubanov2017].

**Commitment, subjective evaluation, and social motives.** Use Kaur, Kremer, and Mullainathan for self-control at work, de Janvry and coauthors for subjective evaluation and influence activities, DellaVigna and Pope for effort motivation, and DellaVigna, List, Malmendier, and Rao for gift exchange and social preferences at work [@kaurKremerMullainathan2015; @deJanvryHeSadouletWangZhang2023; @dellaVignaPope2018; @dellaVignaListMalmendierRao2022].

**Personnel-economics bridge.** Use MacLeod on employment contracts and Hoffman and Stanton for a current review of new personnel-economics evidence [@macleod2011GreatExpectations; @hoffmanStanton2024].

## Exercises And Discussion Prompts

1. Write the principal-agent problem for a worker whose output is noisy. What changes when the worker is risk averse?
2. Give one labor contract that mainly screens hidden type and one that mainly elicits hidden effort. What data would distinguish the two mechanisms?
3. Why can stronger performance pay reduce organizational performance in a multitask job?
4. In Lazear's setting, what would you need to separate the within-worker incentive effect from worker sorting?
5. Suppose a firm introduces subjective performance ratings. What design could distinguish true supervisor information from favoritism or influence activities?
6. How would you measure commitment demand for a work arrangement without confusing it with risk preferences or liquidity constraints?
7. Choose a workplace. Name the hidden object, observed margin, institutional variation, identification strategy, welfare object, and main threat.
8. When should a firm prefer a relational or discretionary bonus over formulaic performance pay?

## Reproducibility And Code Lab Note

The Week 3 code lab lives at `labs/03-contracts-incentives-screening-and-moral-hazard/`. It is a bounded synthetic teaching path, not an official replication of Lazear, de Janvry and coauthors, or Kaur, Kremer, and Mullainathan. The smoke path creates deterministic worker-contract data; reproduces a compact performance-pay summary; diagnoses incentives versus sorting, risk sharing, and hidden objects; and writes transfer prompts for subjective evaluation and commitment settings.

The lab is conservative by design. It does not claim access to proprietary personnel files, firm payroll data, supervisor-rating records, official replication packages, or confidential workplace experiments. Its goal is to help students practice how a contract-theory question becomes an empirical labor design.

## Slide Companion Note

The Week 3 slide deck lives at `slides/week3/03-contracts-incentives-screening-and-moral-hazard.tex`. The deck mirrors the chapter structure without duplicating the prose: it opens with the principal-agent baseline, separates screening from effort incentives, makes multitasking and subjective evaluation visible, translates theory objects into empirical labor designs, and closes with frontier measurement strategies and the Research Lab workflow.

## Bridge Forward

Week 4 moves from contracts inside employment relationships to assignment, wages, platforms, and pricing rules. The bridge is that workplace contracts shape effort and information after a match, while platforms and assignment systems shape which workers see which jobs, how tasks are allocated, how wages are set, and how rules distribute risk across the market.
