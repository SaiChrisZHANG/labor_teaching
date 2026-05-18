# Synthesis, Welfare, and Student Research Designs

## Learning Objectives

By the end of Week 10, students should be able to:

1. define what counts as a behavioral-labor contribution rather than a labor paper with a behavioral label;
2. move from a labor-market puzzle to a behavioral wedge, institutional setting, identifying variation, econometric method, welfare interpretation, and frontier contribution;
3. distinguish treatment effects, behavioral parameters, labor-market margins, welfare-relevant wedges, and equilibrium-adjusted responses;
4. decide when reduced-form evidence is enough and when structural or calibrated welfare analysis is needed;
5. translate earlier course themes into a credible mini research-design memo.

## Opening Orientation

Week 10 asks the capstone question: how do we translate behavioral labor ideas into welfare-relevant, empirically credible, frontier research projects?

This is not a recap week. The course has already introduced worker-side frictions, workplace behavior, identity and norms, policy design, firm response, and behavioral identification. The remaining task is synthesis under research discipline. A strong behavioral-labor project does not stop at an anomaly, an information treatment, or a significant coefficient. It connects a labor-market margin to a behavioral wedge, embeds that wedge in an institution or market, identifies the object being estimated, and states what follows for welfare, policy, or equilibrium interpretation.

:::{admonition} Core points
:class: important

- Behavioral labor projects combine a **labor-market margin**, a **behavioral wedge**, an **institutional environment**, and a **credible design**.
- Good empirical work in this field requires more than finding treatment effects. It requires clarity about what behavioral object is being identified.
- Welfare is not automatic in behavioral labor. Many settings require a benchmark beyond observed choice.
- The frontier often lies in better measurement, tighter design, richer administrative or platform data, and clearer equilibrium interpretation.
- A strong student project can often be built by adapting an existing behavioral-labor design to a new margin, market, institution, data source, or welfare object.

:::

## Bridge

Behavioral Labor began by treating the rational benchmark seriously. That benchmark remains useful because it names the labor object: hours, effort, saving, training, job search, job choice, take-up, sorting, earnings, and productivity. The behavioral move is not to discard the benchmark. It is to ask when nonstandard preferences, biased beliefs, limited attention, social preferences, identity, norms, or learning change the labor prediction in ways that can be measured.

Weeks 2 through 4 supplied the worker-side building blocks. Present bias and commitment problems can reshape labor supply, work-linked saving, training, and effort. Biased beliefs can change search, reservation wages, perceived returns, and career planning. Attention, salience, complexity, and learning can make workers respond to the schedule or program they perceive rather than the one written down.

Weeks 5 and 6 moved those wedges inside firms and social environments. Incentives, monitoring, reciprocity, fairness, identity, and culture can change effort, sorting, evaluation, retention, and workplace contracts. The same worker-side mechanism can look different once managers, peers, teams, and employer policies mediate it.

Weeks 7 through 9 added the discipline that makes the field research-grade. Behavioral claims need measurement and identification. Worker-side wedges may be amplified, dampened, or exploited by firms and markets. Policy design must account for take-up, implementation, intermediaries, targeting, and welfare under distorted choice.

Week 10 turns that architecture into a project-building framework. Students should leave able to write a research-design memo that moves from:

1. a labor-market fact or puzzle,
2. to a behavioral wedge,
3. to an institution or market setting,
4. to an identifying variation,
5. to an econometric method,
6. to a welfare interpretation,
7. to a contribution relative to the frontier.

## Field Core

### What A Behavioral Labor Contribution Looks Like

Not every labor paper with an information intervention, survey module, or psychology word is a behavioral-labor paper. The field is most compelling when the project isolates a wedge between the standard model and observed labor behavior, shows why that wedge changes an economically meaningful margin, and explains how institutions, firms, markets, or policy design shape the response.

A compact map for the course is:

```{math}
:label: eq:research-map-week10
Y = g(B, I, M, P, X; \theta)
```

Here {math}`Y` is the observed labor-market outcome; {math}`B` is the behavioral wedge or mechanism; {math}`I` is the institution or environment; {math}`M` is the firm or market response; {math}`P` is policy or program design; {math}`X` is the observed economic environment; and {math}`\theta` collects preference, belief, technology, information, and institutional parameters.

The map matters because the same behavioral wedge can imply different labor outcomes in different institutions. Present bias in a casual labor market can generate demand for commitment contracts, as in the self-control-at-work logic of [@kaurKremerMullainathan2015]. Present bias in a retirement plan can interact with employer defaults and payroll menus. Inattention in tax filing can change benefit take-up; in a workplace contract, it can change effort response or gaming; in a platform job-search interface, it can change application portfolios.

A credible contribution usually has four features.

First, the labor margin is real. The project is about work, search, effort, training, saving through work, job choice, sorting, promotion, take-up, or policy exposure. It is not only about a laboratory measure attached loosely to workers.

Second, the behavioral wedge is specific. "Information" is not enough. The project should say whether the key object is biased beliefs, missing information, salience, confidence, ambiguity, learning speed, trust, perceived eligibility, present bias, reference dependence, fairness, identity, or social image.

Third, the institution is doing work. Behavioral labor sits at the intersection of labor economics, behavioral economics, policy design, and market response. The empirical setting should explain why this wedge matters here: a nonlinear earnings schedule, a job-search spell, a training application, a payroll default, a subjective evaluation system, a monitoring technology, a team culture, a hiring platform, or a benefit claiming process.

Fourth, the interpretation is bounded. A treatment effect is not automatically a behavioral parameter; a behavioral parameter is not automatically a welfare object; and a worker-level response is not automatically an equilibrium effect. The broad framing in [@dellaVigna2009], [@chetty2015], and [@bernheimTaubinsky2018] is useful because it keeps mechanism, evidence, policy, and welfare on the same page.

### Welfare And Normative Interpretation In Behavioral Labor

Welfare is central because behavioral labor often begins from the possibility that observed choice does not fully reveal welfare. A worker may under-save because inertia dominates attention, under-search because beliefs about offers are biased, fail to claim a benefit because the form is confusing, choose too little training because returns are misperceived, or stay in a workplace arrangement because identity, norms, or social pressure make exit costly in ways the analyst must interpret.

A generic welfare object is:

```{math}
:label: eq:welfare-week10
W = \int \Psi_i\big(a_i, a_i^\star, M, P\big)\, dF(i)
```

Here {math}`a_i` is the observed action, {math}`a_i^\star` is a benchmark action, {math}`M` is firm or market response, {math}`P` is policy or program design, and {math}`\Psi_i` maps these objects into welfare for worker {math}`i`. The hard part is not writing down {math}`W`. The hard part is deciding what {math}`a_i^\star` means.

Different projects use different welfare benchmarks:

- **Observed choice.** This is appropriate when choices plausibly reveal preferences, or when the project makes no welfare claim beyond documenting behavior.
- **Internally valid benchmark.** A project may compare choices before and after information, simplification, commitment, or default changes and treat the corrected environment as more welfare-relevant.
- **Sophisticated or fully informed choice.** The benchmark may be the action workers choose when they understand eligibility, schedules, outside options, or future self-control problems.
- **Long-run learning.** Short-run mistakes may fade as workers gain experience, which means welfare may depend on whether an intervention accelerates learning or overrides it.
- **Structural or calibrated criterion.** Some projects need a model to translate distorted choices, counterfactual policy design, and heterogeneous impacts into welfare.

This is why behavioral welfare cannot be added at the end as decorative language. In [@bernheimFradkinPopov2015], default effects in retirement saving raise the question of whether default-induced choices improve welfare or simply redirect passive choice. In take-up settings such as [@bhargavaManoli2015], higher claiming can be welfare-improving if low take-up reflects psychological or administrative frictions, but the interpretation depends on costs, stigma, targeting, and mistaken eligibility beliefs. [@bernheimTaubinsky2018], [@chetty2015], and [@allcott2025] are useful because they force the analyst to name the normative criterion rather than hiding it behind a significant response.

```{include} assets/tables/10-welfare-and-evidence-map.md
```

### Mapping Topic To Behavioral Wedge To Labor Setting

Good projects often start from a puzzle, but they cannot remain there. A puzzle is a door, not a design. The project must move from "this pattern is surprising" to "this behavioral object changes this labor margin in this institution."

Course examples illustrate the move.

In labor supply, saving, and training, the puzzle may be underinvestment despite high returns, strong response to commitment, or weak response to delayed benefits. The wedge might be present bias, demand for commitment, reference dependence, or misperceived returns. The labor setting might be daily work attendance, training enrollment, payroll saving, or post-displacement human-capital investment. [@kaurKremerMullainathan2015] is useful because the behavioral object is tied to a work arrangement and an effort margin rather than merely inferred from procrastination.

In job search, the puzzle may be overly optimistic or pessimistic job-finding expectations, weak updating, narrow application behavior, or mismatch between perceived and realized offer probabilities. The wedge is often biased beliefs, incomplete information, search confidence, or slow learning. [@muellerSpinnewijnTopa2021] shows why repeated beliefs and employment prospects can turn expectations into a labor object.

In attention, salience, and learning, the puzzle may be weak response to nonlinear schedules, failure to claim benefits, or delayed response to eligibility. The wedge is not "low incentives" but limited attention, schedule misperception, administrative burden, trust, or procedural knowledge. [@bhargavaManoli2015] turns take-up into an object of economic analysis rather than a residual implementation issue.

In workplace behavior, the puzzle may be high effort response to small gifts, asymmetric response to monitoring, gaming, low morale, or subjective evaluation effects. The wedge can be reciprocity, fairness, social preferences, loss aversion, identity, or intrinsic motivation. [@dellaVignaListMalmendierRao2022] is an anchor because it connects social preferences and gift exchange to effort inside the employment relationship.

In identity, norms, and firm culture, the puzzle may be persistent occupational sorting, peer-sensitive behavior, differential response to feedback, or culture-mediated retention. The wedge may be social image, norm compliance, fairness perceptions, gender norms, or identity-based utility. The labor setting matters because norms are transmitted through households, peers, managers, teams, and local labor markets.

In behavioral policy design, the puzzle may be that statutory generosity is high but effective exposure is low. The wedge may be application burden, misunderstanding, inattention, trust, or default passivity. In firm and equilibrium-response projects, the puzzle may be that worker-level frictions survive or change once firms design menus, defaults, recruiting channels, monitoring systems, or platform interfaces.

Many weak projects fail at this mapping stage. They identify a treatment effect but not the behavioral object, identify a behavioral object but not a labor-market margin, or estimate a margin without any welfare interpretation. The cure is to write the mapping explicitly before choosing the estimator.

### Mapping Empirical Setting To Identification Strategy And Econometric Method

The empirical problem is rarely only "estimate the treatment effect." A useful starting estimand is:

```{math}
:label: eq:estimand-week10
\tau = \mathbb{E}[Y_i(1)-Y_i(0) \mid S_i=1]
```

This object may be exactly what a project needs if the question is whether a policy, message, default, contract, or assistance offer changes an observed labor-market outcome for the study sample. But in behavioral labor, the econometric problem is rarely just estimating {math}`\tau`. The analyst must decide whether the design identifies a treatment effect, a behavioral parameter, a welfare-relevant wedge, or an equilibrium-adjusted response.

The practical bridge from setting to method is:

| Empirical setting | Behavioral object | Common methods | What the method can usually support |
| --- | --- | --- | --- |
| Labor-supply schedule or commitment setting | present bias, reference dependence, demand for commitment, schedule perception | field experiment, reduced-form treatment comparison, contract/menu design, structural estimation | effect of commitment or incentive design; sometimes parameter recovery with additional assumptions |
| Repeated beliefs in job search | biased expectations, learning, forecast errors, confidence | panel fixed effects, forecast-error analysis, belief validation, hazard models | relationship between beliefs, updating, and search exits; not automatically welfare |
| Nonlinear schedules and knowledge frictions | salience, tax-benefit knowledge, local learning | bunching, local elasticity, event study, dynamic learning analysis | response to perceived versus statutory incentives if schedule knowledge is measured or shifted |
| Workplace incentives and reciprocity | gift exchange, fairness, monitoring response, social preferences | field experiments, OLS or ANCOVA, heterogeneity analysis, interaction designs, contract-design inference | effort and output response; mechanism if treatment arms isolate channels |
| Implementation and take-up | administrative burden, trust, attention, perceived eligibility | randomized encouragement, reminder or simplification trials, hazard-style claiming analysis, administrative-data treatment evaluation | claiming and completion effects; welfare only with benchmark costs and benefits |
| Welfare and targeting | distorted choice, heterogeneity, policy incidence | sufficient-statistics, calibrated welfare, structural or hybrid approaches | welfare comparison under stated normative benchmark and incidence assumptions |

The same empirical setting can call for different methods depending on the object. Repeated beliefs about job search may require panel methods if the key object is within-person updating, hazard models if the key outcome is exit from unemployment, and information experiments if the key design shifts beliefs directly. Nonlinear tax or benefit schedules may require bunching when workers face kinked incentives, but dynamic learning designs when the question is how workers acquire schedule knowledge. Workplace experiments may estimate clean average treatment effects, but social-preference interpretation often depends on treatment arms that separate gift size, wage framing, monitoring, and worker expectations.

[@haalandRothWohlfart2023] is useful for this week because information experiments are easy to overinterpret. A message may shift beliefs, salience, trust, perceived researcher intent, or attention to a decision deadline. Behavioral labor students should ask what information object moved, what labor margin responded, and what alternative channel remains plausible.

### When Reduced-Form Evidence Is Enough And When Structural Work Is Needed

Reduced-form evidence is enough when the project makes a bounded claim that the design can support. A randomized simplification trial can show that administrative burden suppresses benefit take-up. A workplace experiment can show that a pay framing changes effort. A belief-information intervention can show that perceived returns affect search or training. If the contribution is that a specific friction matters in a specific labor institution, a clean reduced-form design may be more persuasive than a heavy model.

Structural or calibrated work becomes more valuable when the project asks for objects not directly observed in the design:

- present-bias or sophistication parameters;
- reference-point dynamics;
- learning and information acquisition processes;
- welfare under distorted choice;
- counterfactual policy design outside the experimental support;
- firm response, sorting, or equilibrium incidence;
- targeting rules under heterogeneous behavioral wedges.

A compact structural moment objective is:

```{math}
:label: eq:structural-week10
\hat \psi \in \arg\min_{\psi \in \Psi}
\left[m^{data}-m^{model}(\psi)\right]'W\left[m^{data}-m^{model}(\psi)\right].
```

Here {math}`m^{data}` are empirical moments, {math}`m^{model}(\psi)` are model-implied moments, and {math}`\psi` collects parameters such as discounting, belief updating, search costs, attention, or social-preference weights. The gain is interpretation and counterfactual structure. The cost is stronger assumptions, model dependence, and the need to show that the moments identify the relevant behavioral object rather than a flexible residual.

The practical rule is simple: do not use structure because a project feels more sophisticated. Use it when the research question requires an unobserved object or counterfactual that the reduced form cannot identify.

### Equilibrium And External-Validity Considerations

Behavioral labor is strongest when it does not stop at isolated worker choice. Firms, managers, platforms, caseworkers, tax preparers, benefit administrators, peers, households, and markets shape which behavioral frictions matter and whether interventions scale.

Firm response can take several forms. Employers may exploit behavioral biases through complicated menus, opaque incentives, or defaults that benefit the firm. They may accommodate biases by offering commitment, reminders, simplified benefits, or clearer career ladders. They may insure workers against mistakes, sort workers by behavioral traits, or redesign monitoring and evaluation. These responses can change both the observed outcome and the welfare interpretation.

Equilibrium also matters for external validity. A job-search information treatment may work when only some job seekers receive it, but the effect can change if all workers receive the same information and vacancies, wages, or employer screening adjust. A default can raise saving in one firm, but plan providers and employers may redesign menus when defaults become regulated. A take-up simplification can change program composition and budget pressure. A workplace reciprocity intervention can fade as workers learn the treatment is temporary.

This does not mean every project needs a full equilibrium model. It means the proposal must state the equilibrium margin it is leaving offstage. For a student project, that sentence is often enough to keep the claim honest.

### Frontier Project Opportunities In Behavioral Labor

The frontier is not "more behavioral effects." It is better integration of measurement, design, labor-market margins, firm or policy response, and welfare.

```{include} assets/tables/10-frontier-project-opportunities-map.md
```

Several project families are especially promising.

First, dynamic learning of labor-market policies is still underbuilt. Workers learn tax schedules, UI rules, training subsidies, disability earnings limits, and retirement plan features slowly and unevenly. Linked administrative panels and repeated information measures can show whether policy design changes durable knowledge or only temporary salience.

Second, belief formation in job search is a live frontier because labor markets change quickly. Workers may update outside options slowly after sectoral shocks, remote-work changes, technological adoption, immigration shifts, or AI-related task change. Repeated belief elicitation linked to applications, vacancies, offers, and accepted wages can turn expectations into a labor-market object.

Third, algorithmic interfaces are becoming labor institutions. Recommendation systems, application nudges, ranking rules, scheduling apps, productivity dashboards, and digital benefits portals can shape attention, perceived opportunity, and action costs. The behavioral wedge is mediated by an interface and often by a firm or platform.

Fourth, workplace behavior remains open because contracts are not only prices. Monitoring, subjective evaluation, feedback, fairness, identity, and culture can change effort and sorting. The frontier is to connect those mechanisms to durable labor outcomes and firm response rather than only short-run output.

Fifth, behavioral heterogeneity and targeting need sharper welfare frameworks. An intervention that helps inattentive workers may annoy or harm already-informed workers. A default that helps procrastinators may be poorly suited for liquidity-constrained workers. Student projects can make real progress by combining prediction, heterogeneity, and transparent welfare interpretation.

Sixth, firm and market responses deserve more attention. Behavioral wedges may survive because firms exploit them, disappear because markets discipline them, or change form because institutions adapt. This is where Behavioral Labor meets Labor II most directly.

### How To Build A Credible Student Project In This Field

The final project-development object is:

```{math}
:label: eq:project-week10
Contribution = Question + Mechanism + Data + Design + Interpretation
```

The equation is intentionally plain. A project contribution is weak if any term is missing.

The **question** should start from a labor-market fact or puzzle: low training take-up after displacement, biased reservation-wage beliefs, weak response to nonlinear schedules, effort response to subjective evaluation, gendered sorting under norms, low benefit claiming, default-driven saving, or platform-guided search.

The **mechanism** should name the behavioral wedge and the standard alternative. If the project is about beliefs, what is wrong with the beliefs and how are they measured? If it is about attention, why is attention the binding margin rather than low returns? If it is about fairness, what prediction differs from a standard incentive model?

The **data** should observe the labor margin and, where possible, the behavioral object. Strong designs often combine administrative outcomes with survey beliefs, platform logs, HR data, application records, benefit records, or randomized design features.

The **design** should state the source of variation and the estimand. Is the project randomized, quasi-experimental, panel-based, bunching-based, descriptive measurement, structural, or hybrid? What object does it identify, and what does it not identify?

The **interpretation** should say what the result means for welfare, policy, firm behavior, or equilibrium. A project can be valuable without a full welfare result, but it should not imply one without a benchmark.

```{include} assets/tables/10-research-design-template.md
```

### Common Failure Modes

Several failure modes are common enough to diagnose early.

One failure mode is measuring behavior but not the behavioral wedge. A worker clicks less, searches less, claims less, or saves less, but the project cannot distinguish preferences, beliefs, attention, liquidity, hassle, stigma, or constraints.

A second failure mode is identifying a wedge with no labor-market margin. A survey shows misperceptions, but the misperceptions do not map to work, earnings, search, training, take-up, effort, sorting, or firm response.

A third failure mode is treating a reduced-form effect as a structural parameter. An information treatment changes applications, but the project labels the coefficient a belief elasticity without showing how beliefs changed and how other channels were held fixed.

A fourth failure mode is ignoring dynamics. Learning, habit, fatigue, adaptation, and repeated exposure can make short-run effects misleading.

A fifth failure mode is ignoring firms and markets. A worker-side intervention may change employer screening, platform ranking, peer information, or program congestion.

A sixth failure mode is making a welfare claim without a normative framework. Behavioral labor projects need to say whether welfare is evaluated using observed choice, a corrected benchmark, long-run learning, revealed preference under selected conditions, or a model-based criterion.

## Research Lab

The Week 10 lab is a proposal studio. It keeps the course's Reproduce -> Diagnose -> Transfer logic, but adapts it to research design.

**Reproduce.** Students reverse-engineer one or two anchor papers' question and design logic. The goal is not an official replication. It is to identify the paper's behavioral wedge, labor margin, setting, design, method, and welfare claim.

**Diagnose.** Students explain what the anchor identifies and what it does not identify. They name the behavioral object, the labor-market margin, the design, the econometric method, the welfare benchmark, and the equilibrium or external-validity limitation.

**Transfer.** Students build a mini-project memo that applies the same logic to a new setting. The memo must move from puzzle to wedge to setting to variation to method to welfare interpretation to contribution.

The anchor menu is:

1. [@muellerSpinnewijnTopa2021] for beliefs, job search, repeated expectations, and unemployment duration;
2. [@dellaVignaListMalmendierRao2022] for social preferences, gift exchange, and workplace effort;
3. [@bhargavaManoli2015] for take-up, psychological frictions, implementation, and administrative design;
4. [@bernheimFradkinPopov2015] for defaults, retirement saving, and welfare under passive choice.

The bounded local lab generates an anchor menu, a selected-anchor diagnostic table, and a one-page research-design memo scaffold. Students then edit the memo into a project pitch.

## Methods Box

:::{admonition} Methods Box: matching setting to estimand
:class: note

**Start with the object, not the estimator.** A field experiment identifies a treatment effect if the treatment is well defined. It identifies a behavioral parameter only with additional measurement or model structure.

**Beliefs and search settings** often need repeated belief measures, panel fixed effects, forecast-error diagnostics, and hazard models. The key question is whether beliefs are measured, shifted, and linked to search behavior.

**Attention, salience, and nonlinear schedules** often need designs that separate statutory incentives from perceived incentives: bunching, local elasticity estimates, information variation, event studies, or dynamic learning panels.

**Workplace behavior settings** often begin with experiments or contract variation, but mechanism requires treatment arms that separate incentives, monitoring, reciprocity, fairness, and social meaning.

**Take-up and implementation settings** often use encouragement, reminder, simplification, assistance, and administrative-data timing designs. Hazard-style analysis is useful when claiming speed matters.

**Welfare and targeting questions** require explicit benchmarks: observed choice, corrected choice, sophisticated choice, long-run learning, sufficient statistics, calibrated welfare, or structural models.

:::

## Reading Ladder And References

**Field framing.** Start with [@dellaVigna2009] for field evidence in psychology and economics, [@chetty2015] for a pragmatic public-policy perspective, and [@bernheimTaubinsky2018] for behavioral public economics and welfare.

**Worker-side and workplace anchors.** Use [@kaurKremerMullainathan2015] for self-control at work and [@dellaVignaListMalmendierRao2022] for social preferences and gift exchange inside firms.

**Beliefs, search, and information design.** Use [@muellerSpinnewijnTopa2021] for job seekers' beliefs and employment prospects, and [@haalandRothWohlfart2023] for designing and interpreting information-provision experiments.

**Implementation, defaults, and welfare.** Use [@bhargavaManoli2015] for psychological frictions and take-up, [@bernheimFradkinPopov2015] for welfare analysis of default options, and [@allcott2025] for frontier welfare questions around nudges.

## Exercises And Discussion Prompts

1. Pick a labor-market puzzle from an earlier week and write the mapping in equation {eq}`eq:research-map-week10`. Which term is least developed in your current version?
2. For one anchor paper, state whether its main estimate is closest to a treatment effect, behavioral parameter, welfare-relevant wedge, or equilibrium-adjusted response.
3. In equation {eq}`eq:welfare-week10`, define {math}`a_i^\star` for a retirement default, a job-search belief intervention, and a benefit take-up simplification. Why do the benchmarks differ?
4. Use the methods table to match one setting to two possible estimators. What changes about the research question when the estimator changes?
5. Write a one-paragraph project idea using equation {eq}`eq:project-week10`. Then identify the weakest term on the right-hand side.
6. Name one firm or market response that could change the external validity of a worker-side behavioral intervention.

## Reproducibility And Code Lab Note

The Week 10 lab is local and memo-first. It does not require confidential data or official replication packages. The local path is `labs/10-synthesis-welfare-and-student-research-designs/`. Students run the smoke path to generate `output/studio/anchor_menu.csv`, `output/studio/selected_anchor_diagnostic.csv`, and `output/studio/research_design_memo.md`, then revise the memo into an original behavioral-labor project design.

## Slide Companion Note

The Week 10 slide deck should work as a capstone studio deck rather than a duplicate of the chapter. It should show the course architecture, define what counts as a behavioral-labor contribution, isolate welfare and interpretation issues, map settings to methods, identify when reduced-form evidence is enough, surface frontier project families, diagnose common failure modes, and end with a research memo template.

## Bridge Forward

Behavioral Labor ends by opening outward. The next step is not to know every paper in the field. It is to see how a project can become credible: choose a labor margin, name the wedge, understand the institution, find variation, match the method to the estimand, state the welfare benchmark, and say what remains unresolved. That is how a course topic becomes a dissertation-quality question.
