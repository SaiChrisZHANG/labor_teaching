# Lecture 6. When And Why Structure? Static And Dynamic Decision Problems

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain structure as a research choice that complements design-based evidence rather than replacing it;
2. identify when an applied question requires latent primitives, expectations, dynamic incentives, welfare, equilibrium response, or policy counterfactuals outside observed support;
3. distinguish static from dynamic decision problems and name the relevant states, actions, beliefs, shocks, and constraints;
4. map observed data into latent preferences, technologies, frictions, and transition rules;
5. derive the basic mathematical objects behind static discrete choice, dynamic value functions, choice probabilities, moments, likelihoods, and counterfactual mappings;
6. evaluate structural papers by asking what variation identifies the model, what the model fits, what the counterfactual assumes, and where the main credibility threats live;
7. translate a structural question into an applied economics paper with a clear economic object, empirical design, model discipline, and interpretation boundary.

## Opening Orientation

Lecture 6 opens Block 2: structural estimation. The point of the block is not to stage a contest between "structural" and "reduced-form" economics. Good applied work often uses both. Reduced-form and design-based methods are powerful when the relevant comparison is present in the data and the estimand is an observed treatment effect. Structural methods become useful when the object of interest is not directly observed, when current choices depend on future incentives, when the policy has not yet been observed, when welfare is central, or when equilibrium response cannot be recovered from a single contrast.

The central question for this lecture is therefore: **when does the research question require an economic model?** A structural model is worth the cost when it converts economic theory into disciplined empirical restrictions that help recover latent primitives, simulate policies, or interpret welfare. It is not worth the cost when it mainly renames an estimand that a simpler design already identifies more transparently.

The paper spine is deliberately practical. Rust's engine-replacement model shows how dynamic discrete choice can infer replacement costs and continuation values from observed replacement behavior [@rust1987optimal]. Hotz and Miller show how conditional choice probabilities can help estimate dynamic models without repeatedly solving the full dynamic program [@hotz1993conditional]. Keane and Wolpin model young men's schooling, work, and occupation choices as a dynamic career problem [@keane1997career]. Todd and Wolpin use experimental evidence to validate a dynamic model for policy counterfactuals [@todd2006assessing]. Low, Meghir, and Pistaferri use lifecycle structure to study wage risk, employment risk, and insurance [@low2010wage]. Adda, Dustmann, and Stevens show how career costs of children accumulate dynamically [@adda2017career]. Keane and Aguirregabiria and Mira provide useful orientation for what structural work is trying to do and how dynamic discrete-choice models are estimated [@keane2010structural; @aguirregabiria2010dynamic].

## Core Points

:::{admonition} Core points
:class: important

- Structure is a research choice, not an ideological alternative to credible empirical design.
- Structure is most useful when the target object is latent, dynamic, welfare-relevant, equilibrium-mediated, or outside observed policy support.
- A structural paper must say what is observed, what is latent, and what variation in the data disciplines the latent objects.
- Static models map choices to contemporaneous utilities, constraints, and shocks; dynamic models add states, transition rules, expectations, discounting, and continuation values.
- Counterfactuals are credible only to the extent that the estimated primitives, transition rules, and equilibrium environment remain disciplined under the new policy.
- The main threats are functional-form dependence, misspecified expectations, weakly disciplined heterogeneity, poor off-target fit, and identification by assumption rather than by data variation.
- Good structural work reports fit, sensitivity, validation, and interpretation limits with the same seriousness that design-based work reports balance, first stages, pre-trends, or bandwidth checks.
:::

## Bridge

Block 1 asked what can be learned from comparisons already present in the data. Potential outcomes, experiments, DID, IV, RD, RKD, and bunching all required the researcher to define the estimand, identify the variation, state assumptions, and interpret the estimate within its support. The most important habit from Block 1 carries into Block 2: credibility comes from matching the method to the economic question and the data-generating process.

Structural estimation changes the object. Instead of asking only for the effect of an observed treatment, it often asks for primitives that generate behavior: preferences, costs, skills, beliefs, technologies, search frictions, information sets, bargaining rules, or transition laws. Once those objects are disciplined, the researcher can simulate policies that have not been observed, recover welfare objects that do not appear as outcomes, or trace behavior over time. The price is that the model carries more of the identifying burden.

Lecture 7 will ask how to estimate, solve, and validate structural models in practice. Lecture 6 first asks when that machinery is worth using.

## Field Core

### A. Why Structure? What Reduced-Form Methods Leave Latent

Reduced-form designs are often the right answer. If a policy was implemented, treatment variation is credible, the estimand is a treatment effect in the observed environment, and the main policy question concerns that same margin, a transparent design may dominate a large model. A field experiment, DID, IV, RD, or local design can answer many applied questions directly.

Structure becomes attractive when the paper's target is not the observed effect itself. Common triggers are:

- **Latent primitives.** The researcher needs preferences, switching costs, search costs, skill production, risk aversion, information, or productivity rather than only observed choices and outcomes.
- **Expectations.** The decision depends on what agents believe about future wages, job offers, policy rules, health, fertility, retirement, or macro conditions.
- **Dynamic incentives.** Today's choice changes tomorrow's state, so a one-period treatment effect misses option value and path dependence.
- **Policy counterfactuals outside observed support.** The reform changes prices, rules, menus, or opportunity sets in ways not observed historically.
- **Welfare objects not directly observed.** The policy question asks about utility, equivalent variation, insurance value, compensating variation, or distributional welfare.
- **Equilibrium response.** Workers, firms, prices, queues, vacancies, schools, or locations adjust jointly, so partial contrasts cannot recover the incidence of the policy.

The applied standard is not "could a model be written down?" A model can always be written down. The standard is whether the model buys a necessary object that the data cannot reveal without structure. A structural model should earn its keep by making the latent object, identifying variation, and counterfactual logic more explicit.

### B. Static Decision Problems

A static decision problem is useful when the key tradeoff is contemporaneous. A worker chooses among jobs, a household chooses hours given a tax schedule, a student chooses a school from a menu, or a firm chooses whether to adopt a technology today. The model is static if the current action does not need to be valued through its effect on future states.

A generic static discrete-choice model starts with latent utility for person {math}`i` and alternative {math}`j`:

```{math}
:label: eq:em6-static-utility
U_{ij}
=
u_j(X_i,Z_{ij};\theta)
+ \alpha_i q_{ij}
+ \xi_j
+ \varepsilon_{ij}.
```

Here {math}`X_i` are observed individual characteristics, {math}`Z_{ij}` are observed alternative-specific attributes, {math}`q_{ij}` may be a price, wage, distance, schedule, or quality measure, {math}`\theta` are preference parameters, {math}`\alpha_i` allows heterogeneous tradeoffs, {math}`\xi_j` is an unobserved alternative quality term, and {math}`\varepsilon_{ij}` is an idiosyncratic utility shock.

The researcher observes the chosen alternative:

```{math}
:label: eq:em6-choice-rule
d_{ij}
=
\mathbf{1}
\left\{
U_{ij}\ge U_{ik}
\text{ for all } k\in\mathcal{J}_i
\right\}.
```

The structural move is to connect the latent utility model in {eq}`eq:em6-static-utility` to observed choices through a probability model. If {math}`\varepsilon_{ij}` is Type-I extreme value and the systematic component is {math}`V_{ij}=u_j(X_i,Z_{ij};\theta)+\alpha_i q_{ij}+\xi_j`, then:

```{math}
:label: eq:em6-logit-probability
\Pr(d_{ij}=1\mid X_i,Z_i;\theta)
=
\frac{\exp(V_{ij})}
{\sum_{k\in\mathcal{J}_i}\exp(V_{ik})}.
```

Equation {eq}`eq:em6-logit-probability` is not the whole of structural work. It is a simple example of the mapping that all structural papers need: assumptions about preferences, shocks, and information imply a probability of observed behavior. Estimation then asks which {math}`\theta` makes the observed choices most likely or best matches the empirical moments.

Static structure can be useful in labor applications when the question concerns job amenities, nonpecuniary utility, compensating differentials, static labor supply, program take-up, occupational choice, location choice, or school choice. It is less useful when a one-period formulation hides the central margin. For example, a training decision is usually not static because training changes future wages, job offers, and occupational options.

### C. Dynamic Decision Problems

Dynamic models are needed when actions today change tomorrow's state. State variables summarize the payoff-relevant past: schooling, experience, tenure, assets, health, fertility, search duration, occupation, firm match quality, unemployment duration, location, or machine mileage. Actions change those states through transition rules.

Let {math}`s_t` be the state, {math}`a_t\in\mathcal{A}(s_t)` the action set, {math}`u(a_t,s_t;\theta)` current utility, {math}`\delta` the discount factor, and {math}`F(s_{t+1}\mid s_t,a_t;\theta)` the transition law. The canonical Bellman equation is:

```{math}
:label: eq:em6-bellman
V(s_t)
=
\max_{a_t\in\mathcal{A}(s_t)}
\left\{
u(a_t,s_t;\theta)
+
\delta
\mathbb{E}_{\theta}
\left[
V(s_{t+1})
\mid s_t,a_t
\right]
\right\}.
```

The choice-specific value of action {math}`a` is:

```{math}
:label: eq:em6-choice-specific-value
v(a,s;\theta)
=
u(a,s;\theta)
+
\delta
\sum_{s'}V(s';\theta)F(s'\mid s,a;\theta).
```

The value comparison can be written concretely for a continue-versus-stop problem. In a job-search setting, an unemployed worker may accept a wage offer or continue searching. In a replacement setting, a manager may replace a bus engine or continue operating it. Let {math}`C` denote continuation and {math}`S` denote stopping or replacement:

```{math}
:label: eq:em6-continue-stop
v_C(s;\theta)
=
u_C(s;\theta)
+
\delta\sum_{s'}V(s';\theta)F_C(s'\mid s;\theta),
\qquad
v_S(s;\theta)
=
u_S(s;\theta)
+
\delta\sum_{s'}V(s';\theta)F_S(s'\mid s;\theta).
```

The agent chooses {math}`S` when {math}`v_S(s;\theta)+\varepsilon_S` exceeds {math}`v_C(s;\theta)+\varepsilon_C`. With logit shocks, the dynamic conditional choice probability is:

```{math}
:label: eq:em6-dynamic-ccp
\Pr(a_t=a\mid s_t=s;\theta)
=
\frac{\exp(v(a,s;\theta))}
{\sum_{b\in\mathcal{A}(s)}\exp(v(b,s;\theta))}.
```

This equation looks like static logit, but the systematic values contain continuation values. That is the key difference. In a dynamic model, a worker may stay in school not because school pays today, but because it changes tomorrow's wage distribution. A worker may reject a job not because unemployment is pleasant, but because the option value of search is high. A firm may delay adjustment not because current costs are small, but because waiting has option value.

```{include} assets/tables/06-static-vs-dynamic-map.md
```

### D. States, Actions, Expectations, And Latent Heterogeneity

Dynamic structure forces the researcher to be explicit about four objects.

**States.** A state variable is not any observed covariate. It is a sufficient statistic for future payoffs and transitions, given the model. Experience is a state if it affects wages or job offers. Assets are a state if they affect consumption smoothing. Children are a state if they affect time costs and future labor supply. A state omitted from the model can turn into misspecified dynamics.

**Actions.** The action set must match the economic margin. "Work" may be too coarse if the paper is about occupation choice, hours, remote work, search effort, or firm mobility. A model with the wrong menu can fit choices for the wrong reason.

**Expectations.** Expectations determine the continuation value. The researcher must specify whether agents know transition probabilities, learn over time, hold rational expectations, use subjective beliefs, or face information frictions. This is not cosmetic. A schooling model with overly optimistic wage expectations and a schooling model with borrowing constraints can produce similar enrollment patterns but very different policy conclusions.

**Latent heterogeneity.** Structural models often need unobserved types:

```{math}
:label: eq:em6-latent-type
\theta_i=\theta_0+\Lambda h_i,
\qquad
h_i\in\{1,\ldots,H\},
\qquad
\Pr(h_i=h\mid X_i)=\pi_h(X_i).
```

Latent types can represent ability, preferences, costs, beliefs, risk tolerance, family constraints, or match quality. They are useful when observed histories reveal persistent differences not captured by observables. They become dangerous when they are so flexible that they absorb any misfit without being disciplined by meaningful variation. A paper should explain which outcomes, transitions, or choices identify latent heterogeneity and which normalizations are doing work.

### E. What Is Observed Versus What Is Latent

A structural paper should make the data map visible. In a typical labor model, the researcher observes some combination of choices, wages, employment, schooling, tenure, assets, family events, locations, policy rules, or firm outcomes. The researcher does not directly observe utility, search costs, preferences over risk, expected wage offers, job-offer arrival rates, information sets, or welfare.

A useful way to write the model-to-data mapping is:

```{math}
:label: eq:em6-model-to-data
\underbrace{\{a_{it},y_{it},s_{it},p_{it}\}_{i,t}}_{\text{observed data}}
\quad
\Longleftarrow
\quad
\underbrace{
\left[
u(a,s;\theta),
F(s'\mid s,a;\theta),
G(y\mid s,a;\theta),
\mathcal{I}_{it},
\varepsilon_{it}
\right]
}_{\text{latent primitives and behavioral rules}}.
```

Here {math}`p_{it}` denotes policies, prices, or rules; {math}`G` maps states and actions into observed outcomes; {math}`\mathcal{I}_{it}` is the information set. Identification requires more than this diagram. The researcher has to say which parts of the observed data discipline each latent object. Wages may discipline returns to experience. Transitions may discipline job-offer or separation rates. Choice frequencies across states may discipline preferences and costs. Policy changes may discipline price or incentive responses. Experimental variation may discipline counterfactual validation.

The weakest structural papers blur this mapping. They estimate many latent objects and then report a counterfactual as if all objects were equally data-driven. The strongest papers tell the reader which parameters are tightly tied to observed variation, which are normalized, which are borrowed from the literature, and which are explored through sensitivity analysis.

### F. Counterfactuals And Welfare

Structural counterfactuals start from estimated primitives and then change an environment. Suppose a baseline policy is {math}`p_0` and a counterfactual policy is {math}`p_1`. Given estimated primitives {math}`\widehat{\theta}`, the model implies policy-specific decision rules, transition laws, outcomes, and welfare:

```{math}
:label: eq:em6-counterfactual-mapping
\widehat{\theta}
\quad \Longrightarrow \quad
\left\{
\sigma_{\widehat{\theta}}(a\mid s;p),
F_{\widehat{\theta}}(s'\mid s,a;p),
Y_{\widehat{\theta}}(p),
W_{\widehat{\theta}}(p)
\right\}.
```

The counterfactual effect of a policy can then be summarized as:

```{math}
:label: eq:em6-policy-effect
\Delta Y(p_1,p_0)
=
\mathbb{E}_{\widehat{\theta}}
\left[
Y_i(p_1)-Y_i(p_0)
\right],
\qquad
\Delta W(p_1,p_0)
=
\mathbb{E}_{\widehat{\theta}}
\left[
W_i(p_1)-W_i(p_0)
\right].
```

This is powerful because {math}`Y_i(p_1)` and {math}`W_i(p_1)` may not be observed in the data. It is fragile because the conclusion depends on whether {math}`\widehat{\theta}` and the transition rules remain valid under {math}`p_1`. A counterfactual close to observed variation is usually more credible than one that changes the entire opportunity set. A welfare calculation is more persuasive when the utility normalization, outside option, heterogeneity, and distributional weights are transparent.

In applied work, the counterfactual section should therefore answer:

1. Which primitives are held fixed?
2. Which policy rules, prices, or constraints change?
3. Does the model allow agents to adjust expectations?
4. Does the model allow equilibrium objects to adjust?
5. Which outcomes and welfare objects are reported?
6. How far is the counterfactual from the support that identified the model?

### G. Identification, Estimation, And Fit

The identification question is: what features of the data pin down {math}`\theta`? In a static choice model, cross-sectional variation in prices, wages, menus, and attributes may discipline preference parameters. In a dynamic model, transitions across states, repeated choices, policy variation, and outcome histories may discipline transition rules, costs, and continuation values. In equilibrium models, prices and market-clearing conditions may discipline technologies or frictions.

One likelihood-based estimator chooses parameters that make observed behavior most probable:

```{math}
:label: eq:em6-likelihood
\widehat{\theta}_{ML}
=
\arg\max_{\theta}
\sum_{i=1}^{N}\sum_{t=1}^{T_i}
\log
\Pr_{\theta}
\left(
a_{it}\mid s_{it},p_{it}
\right)
+
\log f_{\theta}
\left(
y_{it},s_{i,t+1}\mid a_{it},s_{it},p_{it}
\right).
```

A moment-based estimator chooses parameters that match empirical objects:

```{math}
:label: eq:em6-moment-objective
\widehat{\theta}_{MM}
=
\arg\min_{\theta}
\left[
\widehat{m}^{data}-m^{model}(\theta)
\right]'
W
\left[
\widehat{m}^{data}-m^{model}(\theta)
\right].
```

The model-implied moments might include choice shares by state, transition rates, wage profiles, employment durations, schooling histories, hazard rates, or policy responses. If the model is simulated, the same logic becomes:

```{math}
:label: eq:em6-simulation-objective
m^{model}(\theta)
=
\frac{1}{S}
\sum_{s=1}^{S}
m\left(
\widetilde{a}^{(s)}(\theta),
\widetilde{y}^{(s)}(\theta),
\widetilde{s}^{(s)}(\theta)
\right).
```

Fit is not a generic beauty contest. A model can match the targeted moments mechanically and still fail on behavior essential for the counterfactual. Good reporting separates:

- targeted moments used in estimation;
- non-target moments used for validation;
- parameters estimated from direct variation versus parameters disciplined by functional form or normalization;
- sensitivity to alternative specifications, heterogeneity, expectations, and state definitions;
- counterfactuals near observed support versus counterfactuals that extrapolate heavily.

### H. Theory-To-Applied: How A Structural Question Becomes A Paper

A structural applied paper begins with a policy or behavioral question that cannot be answered by an observed comparison alone. The workflow is:

1. **Economic question.** Define the policy, decision, market, or welfare object.
2. **Observed data.** Name the choices, states, outcomes, policies, and transitions observed.
3. **Latent object.** State what the researcher needs but does not observe.
4. **Model.** Specify preferences, constraints, shocks, expectations, transition laws, and information.
5. **Identification.** Explain what data variation disciplines each major primitive.
6. **Estimation.** Use likelihood, moments, simulation, CCP methods, or another transparent mapping.
7. **Fit and validation.** Show targeted and non-targeted fit, plus any experimental or quasi-experimental validation.
8. **Counterfactual and interpretation.** Report what the model adds and what remains assumption-dependent.

```{include} assets/tables/06-theory-to-applied-bridge.md
```

The same checklist makes the anchor papers easier to read.

**Rust (1987).** The economic question is when a capital good should be replaced. The observed data are mileage states and replacement decisions. The latent objects are replacement costs, maintenance costs, shocks, and continuation values. A static hazard can describe replacement frequency, but it does not recover the value of waiting or the replacement policy under new costs. The model contributes a dynamic decision rule and counterfactual policy analysis. The threats are functional form, the information set, transition assumptions, and whether the estimated maintenance and replacement costs are disciplined by enough state variation [@rust1987optimal].

**Hotz and Miller (1993).** The economic question is methodological: how can dynamic models be estimated when solving the dynamic program repeatedly is costly? The latent object remains the value function. The contribution is to use conditional choice probabilities to recover differences in choice-specific value functions under assumptions about shocks and choice probabilities. The threat is that CCPs are only as informative as the state definition, support, and maintained assumptions [@hotz1993conditional].

**Keane and Wolpin (1997).** The economic question is how young men choose schooling, work, and occupations over time. The observed data include choices and wages over early careers. The latent objects include skill accumulation, preferences, shocks, and expectations. Reduced-form comparisons can document wage profiles or schooling correlations, but they cannot easily simulate career paths under new policies because today's choices shape future experience and options. The model contributes a dynamic human-capital and occupational-choice framework. The threats are state-space choices, unobserved heterogeneity, expectations, and fit to career transitions [@keane1997career].

**Todd and Wolpin (2006).** The economic question is how a schooling subsidy affects child schooling and fertility. The observed data include experimental variation and household behavior. The latent objects include preferences, constraints, fertility-schooling interactions, and dynamic responses. The model contributes policy counterfactuals beyond the experimental rule and uses the experiment for validation. The main threat is whether validation under one policy is enough to support counterfactuals under another [@todd2006assessing].

**Low, Meghir, and Pistaferri (2010).** The economic question is how workers face wage risk, employment risk, and insurance over the lifecycle. The latent objects include risk processes, labor supply responses, insurance mechanisms, and intertemporal preferences. Reduced-form earnings and employment dynamics do not directly reveal insurance value or welfare. The model contributes lifecycle welfare and policy analysis. The threats are risk-process specification, borrowing and insurance assumptions, and whether the model matches non-targeted lifecycle behavior [@low2010wage].

**Adda, Dustmann, and Stevens (2017).** The economic question is how children affect women's careers over time. The observed data include employment, wages, fertility, and career histories. The latent objects include dynamic career costs, preferences, fertility timing, and expectations. Static comparisons can confound timing, selection, and persistence. The model contributes a dynamic accounting of long-run career costs and counterfactual timing. The threats are heterogeneity, expectations, and whether fertility and labor-market states are modeled with enough discipline [@adda2017career].

### I. Credibility Threats And Limits

Structural credibility threats are not mysterious. They are concrete and should be named.

**Functional form.** Parametric utility, production, shock, or transition assumptions can drive estimates. A paper should show sensitivity to functional forms that change the substantive conclusion.

**Misspecified expectations.** Dynamic behavior depends on beliefs. If agents are assumed to know policy rules, wage distributions, or transition probabilities that they do not know, continuation values and welfare may be wrong.

**Weakly disciplined latent heterogeneity.** Latent types can improve fit while hiding misspecification. The model should show which choices, outcomes, or histories reveal the types.

**Poor fit off the estimation target.** Matching targeted moments is not enough. The model should be tested against non-targeted behavior that matters for the counterfactual.

**Identification by assumption.** Some parameters may be estimated mainly because the model normalizes them, restricts shocks, excludes variables, or imposes separability. These restrictions should be visible.

**Extrapolation beyond support.** A model can always compute a counterfactual. The question is whether the counterfactual lies close enough to the observed policy, price, state, and behavioral support to be credible.

**Equilibrium misspecification.** If wages, prices, vacancies, queues, firms, locations, or peer behavior adjust, a partial-equilibrium model may misstate incidence and welfare.

The right conclusion is not that structural results should be distrusted. The right conclusion is that structural results should be read like any other empirical design: identify the object, inspect the variation, evaluate the assumptions, and report the limits.

## Research Lab

The Lecture 6 Research Lab follows **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** The primary anchor is Rust's dynamic engine-replacement model [@rust1987optimal]. The lab uses a reduced synthetic teaching path rather than an official replication. Students work with mileage states, replacement choices, transition rules, continuation values, and a replacement-cost counterfactual. The goal is to reproduce the dynamic-choice logic, not the published magnitude.

**Challenge / transfer anchor.** The transfer anchor is Keane and Wolpin's dynamic schooling, work, and career-choice logic [@keane1997career]. Students move from a two-action replacement problem to a small career-choice setting where actions change future human-capital states. The transfer is deliberately bounded so that students can focus on states, actions, expectations, and counterfactual discipline.

**Reproduce.** Students generate deterministic synthetic bus-panel data, estimate empirical replacement probabilities by mileage state, solve a simple dynamic logit replacement model, and estimate replacement and maintenance parameters by a likelihood-style objective.

**Diagnose.** Students compare dynamic and static fit, identify which moments discipline replacement costs and maintenance costs, inspect state support, and run a counterfactual that changes replacement cost. The diagnosis memo explains what a static hazard cannot identify and where the dynamic model remains assumption-dependent.

**Transfer.** Students apply the same logic to a simplified career-choice panel. The transfer exercise names schooling/work states, computes transition and choice moments, and simulates a tuition-subsidy counterfactual. Students compare what the model can say about dynamic incentives with what it cannot credibly say without richer data and validation.

The central lab question is not "did the model solve?" It is "what latent object did the model recover, what variation disciplined it, and how far should the counterfactual be trusted?"

## Methods Box

:::{admonition} Methods Box: Practical Structural Estimation Diagnostics
:class: note

```{include} assets/tables/06-structural-estimation-diagnostics.md
```

Use this table before estimation and after reading the results. A structural paper is more credible when the answers are specific: which primitive is latent, which variation disciplines it, which moments are targeted, which moments validate it, and which counterfactuals stay near observed support.
:::

## Reading Ladder And References

```{include} assets/tables/06-reading-architecture.md
```

**Orientation.** Start with Keane and Aguirregabiria and Mira to understand what structural work is trying to buy and how dynamic discrete-choice models are typically estimated [@keane2010structural; @aguirregabiria2010dynamic].

**Canonical dynamic discrete choice.** Read Rust with Hotz and Miller [@rust1987optimal; @hotz1993conditional]. Rust gives the economic model, Bellman logic, and replacement counterfactual. Hotz and Miller give the CCP shortcut that helps separate dynamic-choice estimation from brute-force dynamic programming.

**Labor and lifecycle applications.** Read Keane and Wolpin, Low, Meghir, and Pistaferri, and Adda, Dustmann, and Stevens as applied examples where dynamic labor-market behavior is the central object [@keane1997career; @low2010wage; @adda2017career].

**Policy counterfactuals and validation.** Read Todd and Wolpin for a model that uses experimental variation to validate dynamic counterfactual analysis [@todd2006assessing].

**Static choice foundation.** McFadden is the classic discrete-choice foundation for connecting latent utility to observed choices [@mcfadden1974]. It is useful background, even though the Lecture 6 research lab focuses on dynamic choice.

## Exercises And Discussion Prompts

1. Give one applied economics question where a reduced-form estimate is enough. Give one where structure is necessary. Explain the difference in terms of the target object.
2. Write a static utility model for job choice with wages, commute distance, and remote-work availability. Which objects are observed, and which are latent?
3. Starting from {eq}`eq:em6-logit-probability`, explain how a distributional assumption on shocks turns latent utility into choice probabilities.
4. Define a state variable for a dynamic schooling model. Why is it a state rather than just a control variable?
5. Use {eq}`eq:em6-bellman` to explain why a training subsidy may affect work today and wages tomorrow.
6. In a continue-versus-stop problem, what data patterns would discipline the stopping cost? What patterns would discipline transition probabilities?
7. Compare Rust and Keane-Wolpin. What is latent in each paper, and what does the model buy beyond descriptive dynamics?
8. Explain why good fit to targeted moments does not prove that a counterfactual is credible.
9. Name one counterfactual that stays close to observed support and one that requires heavy extrapolation.
10. Design a structural labor paper in two paragraphs. State the economic question, observed data, latent object, model, identifying variation, estimation target, validation exercise, and main threat.

## Reproducibility And Code Lab Note

The Lecture 6 code lab lives at `labs/06-when-and-why-structure-static-and-dynamic-decision-problems/`. It is a bounded synthetic teaching path inspired by dynamic discrete-choice and career-choice papers. It does not claim to reproduce official published data or estimates.

The smoke path creates deterministic synthetic data, estimates a small dynamic replacement model, writes choice-probability and likelihood diagnostics, runs a replacement-cost counterfactual, and then transfers the logic to a simplified schooling/work career-choice setting. The lab is intentionally small enough to run locally without external downloads.

## Slide Companion Note

The Lecture 6 slide deck lives at `slides/week6/06-when-and-why-structure-static-and-dynamic-decision-problems.tex`. The deck mirrors the chapter without duplicating it: it defines why structure is needed, separates static from dynamic problems, names observed and latent objects, shows Bellman-style math, summarizes estimation strategies, translates anchor papers into applied design logic, lists credibility threats, and closes with the Research Lab design.

## Bridge Forward

Lecture 6 explains when structure is worth the cost. Lecture 7 turns to implementation: identification arguments, likelihood, moments, simulation, indirect inference intuition, fit, validation, and transparent reporting. The discipline stays the same across the block: a structural model is credible only when readers can see what the data identify and how the model supports the counterfactual.
