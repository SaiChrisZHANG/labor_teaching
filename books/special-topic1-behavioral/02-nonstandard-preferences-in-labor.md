# Nonstandard Preferences in Labor Supply, Effort, Savings, and Training

## Learning Objectives

By the end of Week 2, students should be able to:

1. locate nonstandard preferences inside DellaVigna's behavioral-economics taxonomy;
2. distinguish present bias, commitment demand, risk aversion, reference dependence, loss aversion, and social preferences as labor-facing preference objects;
3. map each object to worker-side margins: labor supply timing, effort intensity, retirement or payroll-linked saving, and training completion;
4. describe the identifying variation behind applied labor designs that use these preferences;
5. explain why preference-based departures complicate welfare evaluation and policy design.

## Opening Orientation

Week 1 introduced Behavioral Labor as a field organized around labor objects rather than a catalog of biases. Week 2 makes that discipline concrete by focusing on one branch of the taxonomy: nonstandard preferences. The economic question is whether workers' choices over work, effort, saving, and self-investment reveal stable standard preferences, or whether short-run selves, reference points, social motives, and demand for discipline reshape the relevant labor margin.

:::{admonition} Core points
:class: important

- Nonstandard preferences matter in labor because workers repeatedly make intertemporal choices about effort, labor supply, saving, and training.
- The same preference object can move several margins at once: hours, output, retirement saving, and self-investment.
- Labor economists operationalize these preferences through contract choice, effort response, savings take-up, training completion, and reference-point shifts.
- Empirical claims must name both the identifying variation and the observed worker-side margin.
- Welfare is harder than in standard models because observed choices need not reveal stable, time-consistent welfare rankings.

:::

## Bridge

DellaVigna's taxonomy separates behavioral departures into nonstandard preferences, nonstandard beliefs, and nonstandard decision-making [@dellaVigna2009; @dellaVigna2018]. Week 2 isolates the first branch. The goal is not to decide that every low-saving, low-effort, or low-training choice is a preference anomaly. The goal is to ask when a preference-based account adds disciplined predictions beyond standard impatience, heterogeneity, information, technology, or constraints.

This week therefore stays on worker-side margins. Present bias can change labor supply timing, deadline response, and training completion. Commitment demand can reveal that workers value restrictions on future behavior. Risk aversion matters when saving, variable pay, or uncertain training returns change the cost of exposure. Reference dependence can make targets, expectations, or wage disappointments behaviorally relevant. Social preferences and reciprocity can change workplace effort even when private material incentives are held fixed.

## Field Core

### DellaVigna Taxonomy, Narrowed To Preferences

The standard labor model usually treats preferences as stable primitives. Behavioral Labor keeps the same disciplined choice language but allows the utility object to differ from the benchmark in empirically meaningful ways. In Week 2, the worker still chooses a labor action {math}`a`, but the action may be evaluated through short-run temptation, reference points, fairness concerns, or social payoffs:

```{math}
:label: eq:week2-pref-choice
a_i^B \in \arg\max_{a \in \mathcal{A}_i}
\tilde{U}_i(a;\beta_i,\rho_i,r_i,\eta_i),
```

where {math}`\beta_i` captures present bias, {math}`\rho_i` can summarize risk exposure or curvature, {math}`r_i` is a reference point, and {math}`\eta_i` captures social or reciprocal concerns. Later weeks move to beliefs, attention, and perceived choice sets. Here the object is narrower: how the worker values current costs, future benefits, gains, losses, risk, and social payoffs.

```{include} assets/tables/02-preference-taxonomy-map.md
```

### Present Bias And Self-Control

Present bias is a preference object over time. A worker may plan to exert effort, save, or complete training, but when the current cost arrives the present self gives that cost extra weight. A compact quasi-hyperbolic representation is:

```{math}
:label: eq:qhb-week2
U_t = u(c_t,\ell_t) + \beta \sum_{\tau=t+1}^{T} \delta^{\tau-t} u(c_\tau,\ell_\tau),
\qquad \beta \in (0,1].
```

When {math}`\beta<1`, the worker discounts all future utility relative to current utility. In labor applications, {math}`\ell_t` should be read broadly: hours, effort, task completion, training time, or the disutility of saving today. The object is not simply impatience. Ex ante, the worker may prefer a future plan with more effort, saving, or training; ex post, the current self may deviate.

Labor economists operationalize present bias by observing dynamic choices where current costs and future returns are separated. In [@kaurKremerMullainathan2010] and [@kaurKremerMullainathan2015], the central worker-side margin is effort in a real workplace. The designs use work arrangements, contract choice, and timing around paydays to ask whether workers value mechanisms that raise future effort and whether effort varies with short-run self-control pressure. The empirical question is not just whether incentives change output, but whether the pattern looks like self-control rather than standard effort costs, liquidity constraints, or learning.

Training and self-investment use the same logic. A worker may value a credential or skill ex ante but postpone enrollment, attendance, or completion when current effort costs arrive. A credible empirical design needs variation in deadlines, commitment options, reminders, or training structure and must observe the margin that moves: starts, attendance, modules completed, certification, or subsequent labor outcomes.

### Commitment Demand

Commitment demand is an implication of self-control problems, not a separate bias. A worker demands commitment when she voluntarily accepts a restriction, deadline, default, penalty, or monitoring arrangement that makes future deviation harder. In a standard model with no other frictions, paying for less flexibility is puzzling. In a present-biased model, it can be a way for the long-run self to discipline the short-run self.

In labor supply and effort settings, commitment can appear as demand for dominated or restrictive work arrangements, structured scheduling, or deadlines. In savings settings, it can appear as automatic payroll deduction, default enrollment, escalation, or costly withdrawal restrictions. In training, it can appear as cohort schedules, completion pledges, deposits, or progress rules. The observed margin is usually contract take-up, savings participation, contribution behavior, attendance, or task completion.

The interpretation requires care. Commitment take-up is informative about self-control only if the design separates true demand for discipline from selection, employer assignment, screening, monitoring technology, or correlated tastes for structure. A clean design asks which restriction the worker chose, what counterfactual flexibility was available, and how future effort, saving, or completion changed after the restriction was selected or assigned.

### Work-Linked Savings And Risk

Savings belongs in Behavioral Labor when it is tied to work, payroll systems, retirement institutions, or worker planning. A worker's saving choice affects retirement timing, insurance against employment shocks, and the ability to finance training or mobility. The behavioral object can be present bias, procrastination, inertia, default response, or risk aversion.

[@madrianShea2001] is a central work-linked design because the identifying variation is a change in 401(k) default enrollment at the employer, and the observed margin is retirement-plan participation and contribution behavior. The behavioral interpretation emphasizes inertia and procrastination, but the labor economist still has to rule out information, transaction costs, match design, and worker composition. [@dufloGaleLiebmanOrszagSaez2006] is useful as an auxiliary savings design because randomized saving incentives reveal how participation and contributions respond when financial returns are made salient and immediate.

Risk aversion is not the main spine of the week, but it matters on worker-side margins. Workers who dislike risk may underinvest in training with uncertain returns, prefer stable compensation over variable pay, or save more precautionarily when labor income is volatile. In empirical work, the preference object is usually operationalized through choices over variable pay, contribution allocations, insurance-like benefits, or training under uncertain payoffs. The design burden is to distinguish risk preferences from liquidity constraints, borrowing limits, information about returns, and employer selection into jobs.

### Reference Dependence And Loss Aversion

Reference-dependent preferences evaluate outcomes relative to a reference point, not only by levels. A simple representation is:

```{math}
:label: eq:refdep-week2
u(x \mid r) = m(x) + \mu\!\left(m(x)-m(r)\right),
```

where {math}`r` is the reference point and losses relative to {math}`r` may loom larger than gains. In labor economics, {math}`x` can be daily earnings, hours, output, wage changes, performance evaluations, or progress toward training goals.

The worker-side margins are labor supply timing, effort intensity, and performance around targets or disappointments. In taxi labor supply, [@crawfordMeng2011] use variation in realized opportunities and a model of income and hours targets to interpret daily stopping behavior. In public-sector performance, [@mas2006] uses arbitration decisions that create pay outcomes relative to expectations; the observed margin is police performance after wage disappointment or favorable wage resolution. The identifying question is whether responses are asymmetric around a reference point after accounting for standard incentive effects, income effects, fatigue, learning, and worker composition.

For training, reference points may be target completion dates, grade thresholds, credential milestones, or expectations about progress. A shortfall can change effort if the worker experiences it as a loss, but the design must show where the reference point comes from and which completion margin responds.

### Social Preferences, Reciprocity, And Workplace Effort

Social preferences enter when workers care about fairness, employer generosity, peer outcomes, reciprocity, or the surplus created for others. A compact workplace-effort object is:

```{math}
:label: eq:social-pref-week2
U_i = w_i - c(e_i) + \eta_i S(e_i, \pi_f, g_f),
```

where {math}`e_i` is effort, {math}`\pi_f` is employer payoff, {math}`g_f` is employer generosity or treatment, and {math}`\eta_i` measures the weight on social or reciprocal concerns. The standard wage-effort benchmark is still present, but effort can respond to the relational environment even when private monetary incentives are fixed.

The theoretical anchor is [@fehrSchmidt1999]. The labor application is workplace effort and performance. [@dellaVignaListMalmendierRao2022] uses field-experimental variation in piece rates, whether work benefits the employer, employer returns, and surprise gifts. The observed margins are effort, productivity, and extra work. The design asks whether workers exert effort because of private incentives, altruism toward the employer, warm glow, reciprocity, or social norms. This week keeps the application focused on worker effort; broader firm strategy returns in Week 5.

### Mapping Preferences To Labor Margins

The same empirical habit applies across preference objects. Start with the margin, then name the preference, then state the design.

```{include} assets/tables/02-labor-applications-map.md
```

Present bias maps naturally to labor supply timing, effort intensity, and training completion. Commitment demand maps to chosen restrictions, payroll saving defaults, and structured training environments. Risk aversion maps to variable pay, precautionary saving, and uncertain training returns. Reference dependence maps to target labor supply, wage disappointment, performance evaluation, and training goals. Social preferences map to workplace effort, cooperation, and reciprocity.

This sequence prevents overclaiming. A paper does not identify present bias merely because workers under-save or postpone training. It needs variation that separates self-control from low returns, low liquidity, information, transaction costs, or institutional barriers. A paper does not identify social preferences merely because workers exert effort. It needs variation in social payoffs, gifts, fairness, or employer generosity, ideally while holding private incentives and monitoring fixed.

### Welfare And Policy Interpretation

Preference-based departures complicate labor-policy evaluation because observed choices may not reveal stable, time-consistent welfare rankings. If workers are present-biased, the ex ante self may value a commitment device that the ex post self resists. If workers are reference-dependent, welfare depends partly on how reference points are formed, updated, or manipulated. If workers have social preferences, higher effort may reflect meaningful relational motivation, costly pressure, or norms that transfer surplus to firms.

The policy implications are therefore delicate. Payroll saving defaults, commitment contracts, training-completion supports, target setting, and workplace gifts can raise measured outcomes while leaving welfare ambiguous. A credible welfare paragraph must say whose preferences count, whether workers are sophisticated about their own future behavior, what the counterfactual choice environment is, and whether firms or policymakers can exploit the same behavioral regularity. Later weeks return to these issues through policy design, firm response, and equilibrium incidence.

```{include} assets/tables/02-identification-and-welfare-map.md
```

## Research Lab

The Week 2 lab uses a bounded synthetic path to make an abstract preference object operational. The primary anchor is [@kaurKremerMullainathan2010] and [@kaurKremerMullainathan2015]. Students reproduce a Kaur-Kremer-Mullainathan-style factbook with synthetic data on contract choice, output, and payday timing. The point is to see how present bias becomes a labor design: the preference object is self-control, the observed margin is workplace effort, and the identifying variation comes from contract structure and timing.

The lab workflow is **Reproduce -> Diagnose -> Transfer**:

1. **Reproduce:** build synthetic workplace data and estimate output patterns by contract type and payday distance.
2. **Diagnose:** separate incentive effects, commitment demand, payday timing, liquidity, and effort costs.
3. **Transfer:** apply the same logic to a synthetic work-linked savings design inspired by [@madrianShea2001], with [@dufloGaleLiebmanOrszagSaez2006] as a savings-incentive comparison.

The challenge anchor is [@mas2006]. Students sketch how a reference-point design would use wage disappointment or favorable wage resolution as identifying variation and police performance as the observed margin. The optional frontier anchor is [@dellaVignaListMalmendierRao2022], where students classify whether workplace effort responds to private incentives, employer surplus, gifts, or social preferences.

The bounded student path does not use proprietary workplace, payroll, or administrative data. It is a teaching analog designed to practice mechanism, margin, and identification.

## Methods Box

For each preference-based paper, use four questions:

1. **Worker-side margin:** Is the outcome hours, effort, saving, contribution rate, training completion, or performance?
2. **Identifying variation:** Is the design using contract choice, randomized incentives, default changes, payroll timing, targets, arbitration shocks, or gifts?
3. **Mechanism contrast:** What standard explanation remains: liquidity, information, transaction costs, fatigue, monitoring, or selection?
4. **Welfare object:** Does the observed choice reveal welfare, or do ex ante and ex post selves, reference points, or social pressure create a gap?

Reduced-form designs are strongest for causal effects on observed margins. Structural or model-based designs are needed when the question is a preference parameter, counterfactual policy, or welfare. The empirical discipline is to avoid sliding from "the treatment changed behavior" to "we measured a behavioral preference" without the additional identifying argument.

## Reading Ladder And References

**Core framing.** Start with [@dellaVigna2009] for the evidence taxonomy and [@dellaVigna2018] for structural behavioral economics.

**Present bias, commitment, and effort.** Read [@frederickLoewensteinODonoghue2002] for time preference, then [@kaurKremerMullainathan2010] and [@kaurKremerMullainathan2015] for workplace self-control and commitment.

**Savings and work-linked planning.** Use [@madrianShea2001] for retirement saving defaults and [@dufloGaleLiebmanOrszagSaez2006] for saving incentives.

**Reference dependence and loss aversion.** Read [@koszegiRabin2006] for the preference object, [@mas2006] for pay reference points and performance, and [@crawfordMeng2011] for reference-dependent labor supply.

**Social preferences and reciprocity.** Use [@fehrSchmidt1999] for fairness preferences and [@dellaVignaListMalmendierRao2022] for workplace gift exchange and effort.

## Exercises And Discussion Prompts

1. Choose one worker-side margin: labor supply timing, effort intensity, saving, or training completion. Write the standard model and then add one nonstandard preference object. What prediction changes?
2. In a commitment-contract design, what evidence would distinguish true demand for discipline from selection into high-effort workers?
3. Suppose a payroll saving default raises participation. List one present-bias interpretation, one transaction-cost interpretation, and one information interpretation. What additional variation would help distinguish them?
4. For [@mas2006], state the identifying variation, the reference point, the observed performance margin, and one standard alternative explanation.
5. For a workplace gift-exchange experiment, explain what must be held fixed before interpreting effort changes as social preferences rather than monitoring, career concerns, or private incentives.

## Reproducibility And Code Lab Note

The Week 2 lab lives at `labs/02-nonstandard-preferences-in-labor/`. It creates deterministic synthetic data for a workplace self-control design and a work-linked savings transfer design. The smoke path builds the data, runs the reproduction script, and runs the transfer script. The lab is not an official replication package; it is a bounded pedagogical path for converting preference objects into applied labor designs.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-nonstandard-preferences-in-labor.tex`. The deck is a conceptual and empirical map rather than a duplicate of this chapter: it bridges from Week 1, highlights the nonstandard-preferences branch of the taxonomy, walks through present bias, savings, reference dependence, social preferences, identification, welfare, and ends with the bridge to Week 3 on beliefs, expectations, and search.

## Bridge Forward

Week 2 has treated worker behavior as a preference problem on labor supply, effort, savings, and training margins. Week 3 asks when the same observed behavior is instead driven by beliefs, expectations, and perception, especially in job search and labor-market decision environments.
