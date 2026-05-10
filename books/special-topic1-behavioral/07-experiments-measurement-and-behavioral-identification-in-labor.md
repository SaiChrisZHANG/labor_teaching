# Experiments, Measurement, and Behavioral Identification in Labor

## Learning Objectives

By the end of Week 7, students should be able to:

1. distinguish behavioral objects, labor margins, identifying variation, estimands, econometric methods, and interpretation limits;
2. explain why behavioral labor does not have one special estimator, but combines standard labor-econometrics tools with behavioral measurement and modeling;
3. match repeated beliefs data, field experiments, job-search durations, nonlinear schedules, quasi-experiments, and structural problems to practical econometric methods;
4. diagnose when a design identifies a reduced-form treatment effect, a measurement relationship, a latent behavioral parameter, or a welfare-relevant mechanism;
5. design a bounded empirical exercise that moves from a behavioral object to a labor setting, data design, method, and interpretation.

Week 7 is the empirical toolkit lecture for Behavioral Labor. Weeks 1 through 6 named the substantive objects: present bias, beliefs, attention, complexity, reciprocity, identity, norms, fairness, and firm culture. This week asks how applied labor economists measure those objects and identify their role in work, search, take-up, effort, and allocation.

The economic question is practical: when a worker responds to an information letter, an elicited belief, a search spell, a nonlinear schedule, a wage gift, or a policy shock, what exactly has been identified? The answer depends on the behavioral object, the labor margin, the source of variation, the data structure, the estimator, and the welfare benchmark.

:::{admonition} Core points
:class: important

- Behavioral labor research links **behavioral objects** to **labor settings**, **identification strategies**, and **econometric methods**.
- Modern applied work often combines standard labor designs with behavioral measurement: field experiments, subjective expectations data, information interventions, nonlinear-incentive settings, and structural estimation.
- Different labor outcomes call for different empirical tools. Search durations often use hazard models, nonlinear schedules often use bunching methods, panel beliefs data often use fixed effects and validation exercises, and latent behavioral parameters may require structural estimation.
- Good empirical work asks not only "what is the setting?" but also "what is the estimand, what is the method, and what assumptions make the interpretation credible?"
- The frontier is not only new topics. It is better measurement, clearer design, and tighter links between reduced-form evidence, behavioral parameters, and welfare.

:::

## Bridge

The course now turns from **what behavioral labor objects are** to **how they are measured and identified**. A belief about job-finding chances, a present-bias parameter, a salience friction, a reciprocity motive, or a norm sensitivity term is rarely observed directly. Researchers infer these objects from experimental treatments, surveys, administrative outcomes, search spells, effort data, contract choices, policy discontinuities, and model-based parameter recovery.

There is no single "behavioral method." The same labor setting can be studied with different tools depending on the question. A job-search study might use an information RCT to estimate a treatment effect, a beliefs panel to study updating, a hazard model to study exit from unemployment, or a structural search model to recover beliefs and costs. A nonlinear tax-benefit setting might use bunching to estimate local response, an information treatment to test knowledge, or a quasi-experiment to study policy exposure.

That is why Week 7 is organized around a practical arc:

1. define the behavioral object;
2. name the labor margin;
3. state the identifying variation;
4. choose the estimand;
5. use the econometric method that fits the data structure;
6. state the interpretation and welfare limits.

Week 8 will use this toolkit for firm, market, and equilibrium responses to behavioral frictions. Week 9 will then turn that equilibrium view into behavioral public policy. The empirical discipline starts here.

## Field Core

### What Counts As Behavioral Identification In Labor?

Behavioral identification in labor is the attempt to isolate a nonstandard preference, belief, attention friction, social preference, norm sensitivity, or learning process from standard labor-market alternatives. The alternatives matter. A low job-search response may reflect mistaken beliefs, but it may also reflect low returns to search, liquidity constraints, weak networks, discrimination, application costs, or employer-side frictions. A weak response to an earnings incentive may reflect inattention, but it may also reflect adjustment costs, fixed hours, firm scheduling, or tax-benefit interactions.

The first empirical move is therefore measurement. Let {math}`\theta_i` denote a latent behavioral object for worker {math}`i`: a belief, preference parameter, attention cost, reciprocity weight, norm sensitivity, or learning rule. Researchers often observe a noisy proxy {math}`z_{ij}` from survey item, task, elicitation, administrative behavior, or model moment {math}`j`:

```{math}
:label: eq:measurement-week7
z_{ij} = \theta_i + \eta_{ij}
```

The measurement problem is that {math}`\eta_{ij}` may be classical noise, survey error, experimenter-demand effects, misunderstanding, timing mismatch, or endogenous reporting. A belief elicited after a job-search spell may already reflect the spell. A preference measured in a task may not transport to the workplace. A norm proxy may capture local culture, worker sorting, or manager assignment. The methods question is how to connect {math}`z_{ij}` to labor behavior without pretending the proxy is the object itself.

```{include} assets/tables/07-behavioral-object-data-and-design-map.md
```

The practical diagnosis is always the same: name the behavioral object, the labor margin, the data object, the source of variation, and the strongest standard alternative.

### Randomized Field Experiments And Labor Settings

Field experiments are central because they vary incentives, information, reminders, gifts, framing, deadlines, or program communication while observing real labor margins. The key labor advantage is ecological: job seekers search, workers produce output, taxpayers claim benefits, applicants respond to postings, and firms implement contracts in real environments.

A canonical treatment equation is:

```{math}
:label: eq:rct-week7
Y_i = \alpha + \beta T_i + X_i'\gamma + \varepsilon_i
```

Here {math}`Y_i` is a labor outcome such as search effort, employment, benefit take-up, productivity, applications, or retention. {math}`T_i` is randomized treatment, and {math}`X_i` may include baseline outcomes, strata, or pre-treatment covariates. In many labor-field experiments, plain OLS or ANCOVA is the right practical estimator because assignment does the identification and baseline controls improve precision. Randomization inference becomes useful when samples are small, assignment is clustered, or exact design-based inference is central. Heterogeneity analysis becomes important when treatment plausibly works through baseline beliefs, search constraints, prior knowledge, worker type, or firm environment.

The behavioral interpretation still requires care. In [@altmannFalkJaegerZimmermann2018], job-search information can shift knowledge, expectations, motivation, attention, and planning. In [@bhargavaManoli2015], an IRS mailing can shift information, salience, hassle costs, perceived eligibility, or trust. In workplace effort settings such as [@dellaVignaPope2018] and [@dellaVignaListMalmendierRao2022], treatment effects may reflect monetary incentives, reciprocity, gift exchange, task meaning, or selection into effort. [@listRasul2011] is the broader labor field-experiment anchor: the experiment identifies the treatment effect, while the behavioral claim depends on treatment content, mechanism measurement, and design diagnostics.

### Subjective Expectations, Beliefs, And Repeated Measurement

Beliefs and expectations are often behavioral objects, not mere controls. Job seekers hold beliefs about offer arrival, wages, competition, duration dependence, search returns, and the probability that an application converts to a job. The empirical task is not just to ask for a forecast once. It is to study the level, bias, persistence, updating, and predictive content of beliefs.

Repeated subjective expectations data naturally call for panel tools. A typical applied workflow estimates within-person changes, relates forecast errors to later search behavior, validates beliefs against realized outcomes, and checks whether belief updating is consistent with observed labor-market signals. Panel fixed effects help separate stable optimism, pessimism, ability, or local labor-market conditions from updating over time. Validation regressions help ask whether stated beliefs predict realized exits, applications, reservation wages, or earnings.

[@muellerSpinnewijnTopa2021] is the central anchor. The labor object is job-finding beliefs. The margin is unemployment exit and search behavior. The design uses elicited expectations linked to outcomes. The methods include beliefs panels, validation, forecast-error decomposition, and duration analysis. A student should be able to say: this is a belief-elicitation panel, so fixed effects, validation, and measurement-error concerns matter.

### Information Interventions And Learning Designs

Information interventions are not just RCTs with a different label. They are designs that try to move beliefs, salience, procedural knowledge, confidence, perceived eligibility, or learning speed. [@haalandRothWohlfart2023] is useful because it forces researchers to define the information object carefully.

In labor settings, the same "information" treatment may have several mechanisms. A job-search counseling letter can raise expected returns to search, clarify where to search, increase confidence, reduce planning costs, or make unemployment duration more salient. A benefit-take-up notice can reveal eligibility, reduce perceived paperwork burden, raise trust, or trigger deadline attention. A nonlinear-schedule explanation can change knowledge of the budget set, not the budget set itself.

The econometric implementation may still be equation {eq}`eq:rct-week7`: OLS, ANCOVA, clustered standard errors, randomization inference, and heterogeneity by baseline beliefs. The interpretation is different. Researchers must state what information object changed and whether the evidence supports belief updating, attention, procedural simplification, motivation, or a bundle.

### Job-Search Durations And Hazard Methods

Search outcomes often arrive as durations rather than one-shot outcomes. A worker is unemployed in period {math}`t`, searches, receives information, updates beliefs, and may exit unemployment in the next period. The natural object is a hazard:

```{math}
:label: eq:hazard-week7
h_{it} = \Pr(U_{i,t+1}=0 \mid U_{it}=1,\, X_{it}, B_{it})
```

Here {math}`U_{it}=1` denotes unemployment, {math}`X_{it}` contains worker and labor-market conditions, and {math}`B_{it}` denotes beliefs, information exposure, benefit rules, or behavioral state variables. If the outcome is exit from unemployment, the method often follows the outcome: discrete-time logit or probit hazards, Cox-style hazard models, competing-risks models when exits have multiple destinations, and duration-dependence tests.

The behavioral interpretation asks whether duration dependence reflects discouragement, learning, benefit exhaustion, employer screening, declining search effort, or changing reservation wages. In a job-search information experiment, a treatment may shift the hazard through beliefs or through search intensity. In a beliefs panel, a measured belief may predict the hazard but still be correlated with unobserved opportunity. The applied habit is to match the duration outcome to hazard methods and then discipline the behavioral channel with measurement, timing, and validation.

### Nonlinear Schedules, Salience, And Bunching

Labor-market policy often uses nonlinear schedules: tax credits, benefit phaseouts, unemployment insurance rules, disability thresholds, earnings tests, overtime rules, and piece-rate or bonus schedules. When workers know and attend to the schedule, sharp changes in incentives can generate local bunching or local elasticities. When workers do not know the schedule, attenuation may reveal salience or learning frictions rather than low structural responsiveness.

A compact local elasticity object is:

```{math}
:label: eq:bunching-week7
\hat e = \frac{\Delta b / b}{\Delta (1-\tau)/(1-\tau)}
```

Here {math}`\Delta b / b` is the excess mass or local behavioral response around the kink, notch, or threshold, while {math}`\Delta (1-\tau)/(1-\tau)` is the change in the net-of-tax or net-of-subsidy incentive. Bunching estimators, kink and notch methods, and local reduced-form elasticities use institutional variation to study local labor-supply response.

Behavioral labor adds the interpretation problem. In [@chettyFriedmanSaez2013], differences in knowledge about the EITC help explain heterogeneous responses to nonlinear incentives. A bunching estimate alone may not identify deep preferences if workers do not understand the schedule, if learning varies across neighborhoods, or if firms mediate hours and earnings. The practical question is what the bunching response identifies: preferences, adjustment costs, salience, information, or a composite.

### Quasi-Experiments In Behavioral Settings

Behavioral labor is not only field experiments and structural models. Many credible designs use policy, institutional, or information variation that shifts behavior without researcher randomization. Thresholds can invite RD. Eligibility changes can invite DiD. Staggered rollout can invite event studies. Encouragement, exposure, or administrative assignment can invite IV. Policy reforms can shift incentives, salience, or knowledge in ways that make standard labor quasi-experimental tools useful.

The method should be chosen from the source of variation:

- a score, age, earnings, or eligibility threshold points toward RD or kink/notch logic;
- staggered policy timing points toward DiD or event-study designs;
- randomized or quasi-random encouragement points toward IV when take-up is endogenous;
- administrative simplification or information exposure points toward reduced-form, IV, or event-study designs depending on assignment;
- nonlinear schedule changes point toward bunching, local elasticities, and policy-counterfactual calibration.

The behavioral claim is not automatic. A DiD estimate of a simplification reform may identify a policy effect, while the behavioral interpretation requires evidence on hassle, attention, knowledge, or trust. An RD estimate at an eligibility threshold may identify a local treatment effect, while welfare may require knowing whether non-take-up reflects informed choice or friction.

### Structural Behavioral Estimation

Some questions cannot be answered by reduced forms alone. If the research goal is to recover present bias, reference dependence, search costs, social-preference parameters, belief-updating rules, or dynamic information costs, the empirical object is a behavioral parameter vector rather than only a treatment effect.

A generic moment-matching objective is:

```{math}
:label: eq:structural-week7
\hat \psi \in \arg\min_{\psi \in \Psi}
\left[m^{data}-m^{model}(\psi)\right]'W\left[m^{data}-m^{model}(\psi)\right]
```

Here {math}`\psi` denotes behavioral parameters, {math}`m^{data}` denotes empirical moments, {math}`m^{model}(\psi)` denotes model-implied moments, and {math}`W` weights the moments. Maximum likelihood, simulated method of moments, dynamic discrete-choice estimation, and calibrated moment exercises all fit this broad logic.

Structural tools are useful when the question requires counterfactuals or parameter recovery: how much of effort response is reciprocity rather than incentives, how large is present bias at work, how workers update beliefs during search, or how policy design changes welfare under mistakes. [@dellaVigna2018] is the conceptual anchor. [@kaurKremerMullainathan2015] and [@dellaVignaListMalmendierRao2022] show why labor-facing structural discipline can be useful when reduced-form facts are not enough to recover behavioral parameters. The cost is model dependence, so the paper must say which moments identify which parameters and how fit and sensitivity are assessed.

### Given This Empirical Setting, What Methods Do Researchers Actually Use?

The practical answer is that researchers use familiar labor-econometric tools, but attach them to behavioral measurement, design, and interpretation. The method is usually determined by five things: the behavioral object, the labor margin, the data structure, the source of variation, and the desired estimand.

```{include} assets/tables/07-empirical-setting-to-econometric-methods-map.md
```

Use the table as a methods cheat sheet:

- randomized labor intervention -> OLS or ANCOVA, with randomization checks, clustered standard errors when needed, randomization inference for small or clustered designs, and heterogeneity by baseline behavioral state;
- repeated beliefs panel -> fixed effects, validation regressions, forecast-error decomposition, and measurement-error-aware interpretation;
- job-search duration -> discrete-time logit or probit hazards, Cox-style hazards, competing risks, and duration-dependence checks;
- nonlinear schedule -> bunching estimators, kink or notch logic, local elasticities, and salience or knowledge interactions;
- quasi-experimental policy or information shock -> IV, RD, DiD, or event studies, depending on the variation;
- behavioral parameter recovery -> MLE, SMM, dynamic discrete-choice tools, calibrated moments, and sensitivity checks.

The key lesson is modest but powerful: in applied work, there is often no separate "behavioral estimator." There is a labor setting, a behavioral object, and a standard empirical tool used with extra attention to measurement, mechanism, and welfare.

### Failure Modes, Diagnostics, And Interpretation

The most common mistake is to mistake a setting for an estimand. "This is a field experiment" is not enough. The chapter, paper, or student design must say whether the estimand is an ITT, ATE, treatment-on-treated effect, belief-updating parameter, hazard effect, local elasticity, latent preference parameter, or welfare object.

```{include} assets/tables/07-identification-diagnostics-and-common-failures.md
```

The other mistakes follow from the same source. Treatment is confused with measurement. Beliefs are confused with realized opportunities. Bunching is interpreted as preferences even when knowledge frictions matter. Reduced-form results are used for welfare without a welfare benchmark. Structural language is used without saying which data moments identify which parameters. External validity and equilibrium response are ignored.

A strong behavioral-labor interpretation separates:

- **behavior:** what moved in the data;
- **mechanism:** what behavioral object plausibly moved;
- **method:** what estimator generated the claim;
- **estimand:** what parameter or treatment effect was identified;
- **welfare:** what additional assumptions are needed to say whether the change improved outcomes.

## Research Lab

The Week 7 lab is organized around **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is [@altmannFalkJaegerZimmermann2018]. Students use deterministic synthetic data to reproduce a compact job-search information experiment. The bounded path estimates treatment effects on search plans, applications, beliefs, and exits, then summarizes a discrete-time hazard analog. The goal is not an official replication. It is to practice matching an information intervention to OLS/ANCOVA and hazard-style methods.

**Diagnose.** Students classify the design by six objects: the behavioral object, the observed labor margin, the identifying variation, the natural econometric method, the identifying assumptions, and whether the result is reduced form, measurement-based, or structural. A valid diagnosis must state whether the intervention shifts beliefs, attention, procedural knowledge, motivation, or a bundle.

**Transfer.** The secondary anchor is [@dellaVignaListMalmendierRao2022]. Students transfer the same design-to-method logic to workplace gift exchange and social-preference recovery: what is the behavioral object, what is the labor margin, what moments would be used, and when would structural MLE or SMM be useful? An optional extension uses [@chettyFriedmanSaez2013] or [@kaurKremerMullainathan2015] to transfer the framework to nonlinear schedules or self-control at work.

The bounded student path runs locally without confidential data. It trains the empirical habit of moving from object to setting to method to interpretation rather than stopping at a plausible behavioral story.

## Methods Box

:::{admonition} Methods box: behavioral identification in applied labor
:class: note

**Field experiments** identify treatment effects when assignment is valid. The practical estimators are often OLS or ANCOVA, with randomization checks, clustered standard errors when appropriate, randomization inference for small designs, and heterogeneity analysis when baseline behavioral states matter.

**Beliefs and expectations panels** measure subjective objects repeatedly. The practical tools are panel fixed effects, validation against outcomes, forecast-error decompositions, and measurement-error diagnostics.

**Search and unemployment durations** are naturally studied with hazard methods. Discrete-time logit or probit hazards and Cox-style models fit spell data, censoring, duration dependence, and changing beliefs or benefits.

**Nonlinear schedules** use bunching, kink, notch, and local-elasticity tools. Behavioral interpretation requires evidence on knowledge, salience, adjustment costs, and learning.

**Quasi-experiments** use IV, RD, DiD, and event-study designs when policy, timing, thresholds, or exposure shift incentives or information. The behavioral mechanism still needs measurement or a credible mechanism test.

**Structural estimation** is useful when the object is a behavioral parameter or counterfactual. MLE, SMM, dynamic discrete-choice models, and calibrated moment exercises require explicit moments, model fit, and sensitivity checks.

:::

## Reading Ladder

**Framing and methods backbone.** Start with [@dellaVigna2009] for field evidence in psychology and economics, [@dellaVigna2018] for structural behavioral economics, [@listRasul2011] for labor field experiments, and [@haalandRothWohlfart2023] for information-provision design.

**Beliefs and expectations measurement.** Use [@muellerSpinnewijnTopa2021] to study subjective job-finding beliefs, duration dependence, bias, and validation against labor-market outcomes.

**Information interventions and labor settings.** Pair [@altmannFalkJaegerZimmermann2018] with [@bhargavaManoli2015]. Read them as designs that require both treatment-effect estimation and careful interpretation of what information, salience, or procedural object moved.

**Structural and parameter-recovery examples.** Use [@kaurKremerMullainathan2015] and [@dellaVignaListMalmendierRao2022] to see why behavioral labor sometimes needs model-based parameter recovery rather than only reduced-form effects.

**Salience, knowledge, and nonlinear schedules.** Use [@chettyFriedmanSaez2013] as the anchor for knowledge frictions, nonlinear incentives, and labor-supply response.

**Real-effort benchmark.** Use [@dellaVignaPope2018] to connect incentive variation, effort tasks, forecasting, and mechanism interpretation.

## Exercises And Discussion Prompts

1. In equation {eq}`eq:measurement-week7`, give one example where {math}`z_{ij}` is an elicited belief and one example where it is an administrative behavior. What might enter {math}`\eta_{ij}` in each case?
2. In equation {eq}`eq:rct-week7`, when is OLS or ANCOVA enough? When would you add randomization inference, clustered standard errors, or treatment-effect heterogeneity?
3. In equation {eq}`eq:hazard-week7`, explain why unemployment exit data naturally lead to discrete-time hazard methods. What would be the behavioral interpretation of {math}`B_{it}`?
4. In equation {eq}`eq:bunching-week7`, why does bunching not automatically identify a preference elasticity when knowledge or salience frictions matter?
5. In equation {eq}`eq:structural-week7`, choose two moments that could identify a reciprocity parameter in a workplace gift-exchange setting. What assumption links each moment to the parameter?
6. Pick one empirical setting from the methods cheat sheet. State the behavioral object, labor margin, identifying variation, estimand, method, and welfare limit.
7. Design a nearby transfer study for job-search reminders, benefit take-up, remote-work effort, or nonlinear scheduling. Name the method you would actually estimate.

## Reproducibility And Code Lab Note

The Week 7 lab lives at `labs/07-experiments-measurement-and-behavioral-identification-in-labor/`. It creates deterministic synthetic data for a job-search information experiment, a beliefs-panel validation exercise, a hazard-style unemployment exit summary, and a transfer exercise on workplace gift exchange and local schedule response. The smoke path builds the data, runs the reproduction script, and runs the transfer script. It is a bounded teaching lab, not an official replication package for the cited papers.

## Slide Companion Note

The Week 7 slide deck lives at `slides/week7/07-experiments-measurement-and-behavioral-identification-in-labor.tex`. The deck defines the central question, bridges from Weeks 1 through 6, introduces measurement, experiments, beliefs data, information interventions, hazards, bunching, quasi-experiments, and structural estimation, and ends with common failure modes and the bridge to Week 8.

## Bridge Forward

Week 7 gives the empirical discipline needed for the final part of the course. Week 8 turns to firm, market, and equilibrium responses to behavioral frictions. The same tools will reappear, but the emphasis will shift from identifying worker-level wedges to separating worker response, firm strategy, and market outcomes before Week 9 turns to policy design.
