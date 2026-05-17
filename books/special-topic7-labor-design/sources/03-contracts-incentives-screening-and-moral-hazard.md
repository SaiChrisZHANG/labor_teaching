---
title: Contracts, Incentives, Screening, and Moral Hazard
bibliography:
  - references.bib
---

# Week 3. Contracts, Incentives, Screening, and Moral Hazard

## Opening orientation

Week 3 moves from market-level allocation to the design of the employment relationship itself. Once a worker and firm are matched, the central problem is no longer only who meets whom, but how the employment contract reveals information, allocates risk, elicits effort, disciplines behavior, and shapes retention. This week therefore turns contract theory into labor economics: wages, performance pay, probation, promotions, subjective evaluation, and monitoring are all labor-market institutions that mediate hidden action and hidden information.

```{admonition} Core points
:class: important
- Labor contracts solve multiple problems at once: they screen hidden type, elicit hidden effort, allocate risk, and shape retention and promotion.
- A principal-agent framework is useful because wedges emerge whenever effort, commitment, or type are imperfectly observed.
- The best empirical labor papers in this area translate hidden objects into observable margins such as output, attendance, quits, performance ratings, promotions, or wage trajectories.
- Multitasking, subjectivity, and relational enforcement are not side issues; they are central reasons why simple performance-pay formulas often fail.
```

## Bridge

Week 2 showed that recruiting design shapes who gets matched and when. Week 3 asks what happens after a match is made. The core bridge is that matching alone does not determine efficiency: a poorly designed employment contract can destroy surplus even when the match itself is good.

## Field Core

### 1. A principal-agent framework for labor contracts

Start from the canonical labor contracting problem. A worker chooses effort {math}`e` at cost {math}`c(e)`. Output {math}`y` depends on effort, worker type, job design, and noise:
```{math}
:label: eq:pa-output
y = f(e,\theta,x) + \varepsilon,
```
where {math}`\theta` is hidden type and {math}`x` is task or job design. The firm cannot usually observe effort directly, so pay cannot be conditioned on effort itself; it must be conditioned on noisy output, subjective ratings, or other imperfect signals. This creates the classic tradeoff between incentives and insurance: stronger performance pay improves incentives but loads more risk onto workers.

When the worker performs multiple tasks, the contract also creates distortions:
```{math}
:label: eq:multitask
y_j = f_j(e_j) + \varepsilon_j, \qquad j=1,\dots,J.
```
If only some tasks are measured, workers will reallocate effort toward measurable tasks and away from unmeasured ones [@holmstromMilgrom1991; @baker1992performance].

### 2. Screening, hidden type, and contract menus

Labor contracts are rarely one-size-fits-all. Firms use probation, promotion ladders, nonlinear bonuses, referral rules, and benefit menus to sort workers of different types. In applied labor settings, “type” may mean productivity, reliability, patience, self-control, social preferences, or susceptibility to multitask distortions.

A useful applied question is therefore not only whether a contract raises average effort, but which workers it attracts or retains. Lazear’s performance-pay study is the benchmark illustration: a pay reform changed both productivity and sorting, so the observed output gain reflects incentives and selection together [@lazear2000]. Dohmen and Falk make this point more generally by showing that performance pay and worker traits sort together [@dohmenFalk2011].

### 3. Incentives, effort, and measured productivity

The strongest applied papers in this area open the “effort” black box with direct or semi-direct output data. Piece-rate factories, call centers, retail teams, field production, and public-service settings are useful because they give relatively clean output measures.

Classic examples:
- Lazear (2000): piece rates in windshield installation [@lazear2000]
- Bandiera, Barankay, and Rasul: incentive changes and manager-worker organization [@bandieraBarankayRasul2007]
- Friebel et al. (2017): team incentives in retail [@friebelHeinzKruegerZubanov2017]
- DellaVigna and Pope (2018): broad evidence on what motivates effort [@dellaVignaPope2018]

The main empirical lesson is that “effort” is not one object. Contracts may raise output through:
- more intense work,
- longer time on task,
- better selection,
- different task allocation,
- or strategic gaming.

### 4. Commitment, self-control, and labor contracts

Some labor contracts also solve worker-side commitment problems. Kaur, Kremer, and Mullainathan show that workers may demand contracts that help them commit to desired work patterns, implying that labor contracts can respond not only to principal-agent problems but also to worker self-control problems [@kaurKremerMullainathan2015]. This is important for applied work because observed contract demand may reflect both productivity incentives and self-imposed discipline.

This also changes welfare interpretation. A contract that looks harsh from a standard revealed-preference perspective may be chosen because it provides commitment. That makes commitment a hidden object that labor economists need to measure, not assume away.

### 5. Subjective evaluation, multitasking, and influence activities

Many workplaces cannot measure true output well enough to use purely formulaic pay. They therefore rely on supervisors, ratings, and promotion committees. This helps with multitasking but creates another wedge: workers may shift effort toward pleasing evaluators rather than producing organizational output. The recent randomized field experiment by de Janvry et al. provides a clean example of this problem in public-sector work [@deJanvryHeSadouletWangZhang2023].

This literature is useful because it shows why the right applied object is not simply “is the contract high-powered?” but “which signal is being rewarded?” Subjective evaluation may correct one measurement problem while creating another.

### 6. From theory to applied labor research

A good applied paper in this area usually makes five choices explicit.

#### (i) What hidden object matters?
Examples:
- effort,
- type,
- self-control / commitment,
- evaluator-specific influence,
- social preferences,
- multitask distortions.

#### (ii) What observable margin captures it?
Examples:
- output per hour,
- attendance,
- quits,
- promotions,
- performance ratings,
- task mix,
- wage growth,
- contract take-up.

#### (iii) What institutional variation identifies it?
Examples:
- contract changes,
- bonus redesign,
- probation rules,
- evaluator assignment,
- promotion thresholds,
- randomized incentive framing,
- menu variation.

#### (iv) What competing mechanisms must be separated?
Examples:
- incentives vs selection,
- effort vs task reallocation,
- output vs gaming,
- screening vs retention,
- commitment vs coercion.

#### (v) What welfare object matters?
Examples:
- productivity,
- worker risk,
- retention,
- inequality inside firms,
- organizational output,
- worker surplus.

### 7. Research architecture

This week naturally supports at least four applied project types:

1. **Contract-change papers**  
   Study a real redesign in pay, probation, or bonus rules.

2. **Signal-quality papers**  
   Compare objective and subjective performance signals.

3. **Commitment-demand papers**  
   Study whether workers sort into or demand discipline-enhancing contracts.

4. **Multitask / influence papers**  
   Show how contracts reshape unobserved effort allocation rather than total effort alone.

## Methods Box

### Measuring or eliciting effort, commitment, and hidden objects

The frontier methods in this area differ by what the hidden object is.

#### A. Effort
Common empirical proxies:
- output-based administrative data,
- sales or production logs,
- attendance and lateness records,
- machine/digital trace data,
- task completion rates.

Strength:
- often high frequency and objective.

Limitation:
- output may combine effort, ability, and task allocation.

#### B. Commitment / self-control
Common approaches:
- contract menu choice,
- randomized contract framing,
- dynamic attendance targets,
- deviations from stated work plans,
- worker surveys linked to administrative outcomes.

Strength:
- can identify demand for contract form itself.

Limitation:
- commitment demand may be confounded with risk preferences or liquidity constraints.

#### C. Hidden type
Common approaches:
- probation and promotion thresholds,
- ex post performance revealed after ex ante contract choice,
- matched employer-employee panels,
- referral or screening design changes.

Strength:
- useful for separating incentive from selection effects.

Limitation:
- type is often persistent but imperfectly measured.

#### D. Subjective evaluation / influence
Common approaches:
- random or quasi-random evaluator assignment,
- rater rotation,
- variation in evaluator identity or uncertainty,
- text/rating comparisons,
- linked surveys on perceived favoritism.

Strength:
- directly studies agency problems inside organizations.

Limitation:
- difficult to observe organizationally valuable effort separately from evaluator-pleasing effort.

## Research Lab

### Primary anchor paper
**Lazear (2000), “Performance Pay and Productivity.”** This is the primary anchor because it is the cleanest example of a contract-theory question becoming an applied labor paper: a contract redesign changes measured output, but the paper must separate incentive effects from selection [@lazear2000].

### Reproduce
Recreate one reduced fact about the contract change:
- the productivity shift,
- the sorting component,
- or the wage-productivity relation under the new pay scheme.

### Diagnose
Ask:
- what hidden object is being targeted—effort or type?
- how much of the measured gain is incentives versus sorting?
- what output measure is being rewarded?
- what important unmeasured distortions might remain?

### Transfer
Apply the same logic to a bounded alternative setting:
- a probation or bonus redesign,
- a commitment-style contract menu,
- or a subjective-evaluation environment in which measured output is incomplete.

### Challenge / extension anchor
Use **de Janvry et al. (2023)** or **Kaur, Kremer, and Mullainathan (2015)** as the extension:
- de Janvry et al.: subjective evaluation and influence activities [@deJanvryHeSadouletWangZhang2023]
- Kaur, Kremer, and Mullainathan: self-control and demand for work arrangements [@kaurKremerMullainathan2015]

## Reading Ladder And References

### Core theoretical framing
- Holmström and Milgrom (1991)
- Baker (1992)
- Prendergast (1999)

### Core applied labor papers
- Lazear (2000)
- Bandiera, Barankay, and Rasul (2007)
- Dohmen and Falk (2011)
- Friebel et al. (2017)

### Frontier / extension papers
- Kaur, Kremer, and Mullainathan (2015)
- DellaVigna and Pope (2018)
- de Janvry et al. (2023)
- DellaVigna et al. (2022)

## Exercises And Discussion Prompts

1. Why is output an imperfect measure of effort in most labor settings?
2. Give one setting where a contract menu would mainly screen type, and one where it would mainly solve commitment problems.
3. Why can stronger incentives reduce organizational performance in a multitask setting?
4. What empirical design would best distinguish:
   - incentive effects,
   - sorting effects,
   - influence activities,
   - and commitment demand?
5. When should a firm prefer subjective evaluation to objective performance pay?

## Reproducibility And Code Lab Note

The Week 3 lab should center on a reduced teaching-path reproduction of a contract-change result, followed by a transfer exercise that applies the same logic to a different hidden-object problem (commitment or subjective evaluation). If official replication files are not locally available, the teaching path should use reduced or synthetic data that separate incentive effects from sorting.

## Slide Companion Note

The slide deck should emphasize:
- the principal-agent core,
- why multitasking and subjective evaluation matter,
- how hidden objects become observable margins,
- and how a theory paper turns into an applied labor design.

## Bridge Forward

Week 4 moves from contract design inside ongoing employment relationships to assignment, wages, platforms, and pricing rules. The bridge is that once firms choose contracts and incentive systems, the next design question is how workers are allocated across jobs and how wages or pricing rules are set across the market.
