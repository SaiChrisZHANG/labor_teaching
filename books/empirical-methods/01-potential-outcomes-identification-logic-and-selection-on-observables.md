# Lecture 1. Potential Outcomes, Identification Logic, And Selection-On-Observables

## Learning Objectives

By the end of this lecture, students should be able to:

1. define potential outcomes, treatment assignment, target estimands, and the counterfactual problem;
2. explain what is observed, what is missing, and which assumption links the two;
3. distinguish ATE, ATT, and ATC, and choose among them for applied policy questions;
4. derive the selection-bias decomposition and interpret it as an economic selection problem;
5. state conditional independence and overlap as identifying assumptions, not estimator details;
6. compare regression adjustment, matching, weighting, and doubly robust logic at a transparent design level;
7. diagnose an observables-based design using balance, common support, weighting stability, specification discipline, and sensitivity to unobservables;
8. turn selection-on-observables into a publishable applied project when the institutional setting and covariate information are strong enough.

## Opening Orientation

The first question in empirical economics is not "which estimator should I run?" The first question is "what counterfactual am I trying to learn?" A paper about a job-training program, a school track, a health intervention, a firm technology adoption decision, or a local policy has to say whose outcome under which treatment state is missing from the data. Potential outcomes give us the bookkeeping language for that task.

This lecture starts with that language and then uses it to study selection-on-observables. The design is sometimes treated as a weak default: if no experiment, instrument, discontinuity, or panel shock is available, add controls and hope. That is not the version worth teaching. In its serious form, selection-on-observables is a design for settings where researchers know the assignment process, observe the main determinants of both treatment and untreated outcomes, can show overlap, and can make robustness work part of the claim.

LaLonde's evaluation of training-program estimators is the natural warning label [@lalonde1986]. Dehejia and Wahba's matching reanalysis is the natural design rescue [@dehejiaWahba1999; @dehejiaWahba2002]. Rosenbaum and Rubin supply the propensity-score logic [@rosenbaumRubin1983]. Altonji, Elder, and Taber plus Oster give applied economists a language for asking how strong unobserved selection would need to be to change the conclusion [@altonjiElderTaber2005; @oster2019].

## Core Points

:::{admonition} Core points
:class: important

- A causal design begins with a target parameter and an explicit statement of the missing counterfactual.
- The observed outcome reveals {math}`Y_i(1)` for treated units and {math}`Y_i(0)` for untreated units, but never both for the same unit.
- Naive observational comparisons mix causal effects with selection bias.
- Selection-on-observables identifies effects only when conditional independence and overlap are economically plausible in the setting at hand.
- Regression adjustment, matching, weighting, and doubly robust estimators are different ways to operationalize the same identifying logic.
- A credible observables-based paper defends the covariate set, shows balance and common support, disciplines specification search, and studies sensitivity to omitted variables.
:::

## Bridge

Lecture 1 supplies the grammar for the rest of Block 1. Experiments replace conditional independence with randomized assignment. Difference-in-differences replaces cross-sectional conditional independence with a counterfactual trend assumption. Instrumental variables replace direct comparability with variation from an excluded source. Regression discontinuity replaces global comparability with local comparison around a rule. Those designs differ, but they all answer the same first-order question: what makes the missing potential outcome credible?

Selection-on-observables is therefore both a method and a test of research discipline. If students can name the estimand, state the assignment story, identify the missing potential outcome, and explain why the observed data recover it, they are ready to read the rest of the course more carefully.

## Field Core

### Potential Outcomes And The Counterfactual Problem

Let {math}`Y_i(1)` denote the potential outcome for unit {math}`i` if treated and {math}`Y_i(0)` the potential outcome if untreated. Let {math}`D_i \in \{0,1\}` indicate observed treatment status. The realized outcome is

```{math}
:label: eq:em1-realized-outcome
Y_i = D_iY_i(1) + (1-D_i)Y_i(0).
```

The individual causal effect is

```{math}
:label: eq:em1-unit-effect
\tau_i = Y_i(1) - Y_i(0).
```

Equation {eq}`eq:em1-unit-effect` is conceptually simple and empirically impossible to observe directly. For a treated unit, the researcher observes {math}`Y_i(1)` and misses {math}`Y_i(0)`. For an untreated unit, the researcher observes {math}`Y_i(0)` and misses {math}`Y_i(1)`. The fundamental problem of causal inference is not that economists lack clever estimators. It is that the individual counterfactual is structurally missing.

The design task is to replace the missing potential outcome with a credible comparison. In an experiment, random assignment does that work. In selection-on-observables, the claim is that treated and untreated units with the same observed covariates have comparable potential outcomes. That claim must be argued from the economics of the setting.

### Target Parameters

Applied work should define the estimand before choosing an estimator. Three common targets are:

```{math}
:label: eq:em1-ate
ATE = \mathbb{E}[Y(1)-Y(0)],
```

```{math}
:label: eq:em1-att
ATT = \mathbb{E}[Y(1)-Y(0)\mid D=1],
```

```{math}
:label: eq:em1-atc
ATC = \mathbb{E}[Y(1)-Y(0)\mid D=0].
```

The ATE asks what would happen on average if treatment were assigned to the population represented by the sample. The ATT asks what the treatment did for those who actually received it. The ATC asks what treatment would do for those currently untreated. These are not interchangeable. A job-training program for disadvantaged workers often motivates an ATT: did participants gain? A proposed universal policy may motivate an ATE. A targeting expansion may motivate an ATC or a policy-relevant treatment effect for a margin near eligibility.

Estimators can quietly change the estimand. Matching after trimming weak support may estimate an ATT for treated units who have good comparison matches, not the ATT for all treated units. Weighting can target the ATE, ATT, ATC, or an overlap population depending on the weights. Regression adjustment can look like an ATE but rely on extrapolation if the treated and untreated covariate distributions barely overlap. A polished applied paper keeps the parameter visible as the sample and support change.

### Why Observational Comparisons Are Biased

The naive difference in observed means is

```{math}
:label: eq:em1-naive-diff
\mathbb{E}[Y\mid D=1] - \mathbb{E}[Y\mid D=0].
```

Using the realized-outcome equation, this can be decomposed as

```{math}
:label: eq:em1-selection-bias
\mathbb{E}[Y\mid D=1] - \mathbb{E}[Y\mid D=0]
=
\underbrace{\mathbb{E}[Y(1)-Y(0)\mid D=1]}_{ATT}
+
\underbrace{\mathbb{E}[Y(0)\mid D=1] - \mathbb{E}[Y(0)\mid D=0]}_{\text{selection bias}}.
```

The second term is the difference in untreated potential outcomes between treated and untreated units. It is the problem LaLonde made vivid: nonexperimental comparison groups can differ from program participants in ways that make the comparison misleading even before any treatment effect is considered [@lalonde1986].

The decomposition in {eq}`eq:em1-selection-bias` is also a research prompt. If training participants have lower prior earnings, weaker labor-force attachment, different local labor markets, different motivation, or different access to caseworkers, those differences can move {math}`Y(0)`. A design has to say which of those channels are observed, which are controlled or balanced, and which remain a threat.

### Conditional Independence And Overlap

Let {math}`X_i` denote pre-treatment covariates. Selection-on-observables assumes conditional independence:

```{math}
:label: eq:em1-cia
\{Y_i(1),Y_i(0)\} \perp D_i \mid X_i.
```

For the ATT, researchers sometimes need only a conditional mean independence condition for {math}`Y_i(0)`, because the missing counterfactual for treated units is untreated outcomes:

```{math}
:label: eq:em1-att-cmi
\mathbb{E}[Y_i(0)\mid D_i=1,X_i]
=
\mathbb{E}[Y_i(0)\mid D_i=0,X_i].
```

The support condition is overlap:

```{math}
:label: eq:em1-overlap
0 < \Pr(D_i=1\mid X_i=x) < 1
\quad \text{for relevant } x.
```

Conditional independence is not a claim that covariates are numerous. It is a claim that the observed covariates block the assignment channels that would otherwise make potential outcomes differ by treatment status. Overlap is not a cosmetic diagnostic. It is the requirement that comparable treated and untreated units exist in the data. Without overlap, the design either extrapolates or changes the estimand.

The propensity score {math}`e(X)=\Pr(D=1\mid X)` is useful because Rosenbaum and Rubin show that if treatment is independent of potential outcomes conditional on {math}`X`, then it is also independent conditional on a balancing score such as {math}`e(X)` [@rosenbaumRubin1983]. The propensity score compresses the covariates for balancing; it does not make hidden selection disappear.

### Regression Adjustment, Matching, Weighting, And Doubly Robust Logic

Regression adjustment estimates conditional outcome functions. A simple version is

```{math}
:label: eq:em1-regression-adjustment
\mathbb{E}[Y_i\mid D_i,X_i]
=
\alpha + \tau D_i + g(X_i),
```

with richer designs allowing interactions, flexible functions, or separate outcome models by treatment status. Regression adjustment is transparent and easy to report. Its danger is model dependence: if treated units live in covariate regions with few untreated observations, the estimate can rely on functional-form extrapolation.

Matching constructs treated and untreated comparisons with similar observed covariates. Exact matching, nearest-neighbor matching, Mahalanobis matching, calipers, and propensity-score matching differ in mechanics, but the design question is constant: are matched units similar on the variables that jointly predict treatment and untreated outcomes? Abadie and Imbens show that matching estimators require their own statistical discipline; matching is not merely a preprocessing ritual [@abadieImbens2006].

Inverse-probability weighting uses the propensity score to reweight observations. One ATE representation is

```{math}
:label: eq:em1-ipw-ate
ATE
=
\mathbb{E}\left[
\frac{D_iY_i}{e(X_i)}
-
\frac{(1-D_i)Y_i}{1-e(X_i)}
\right].
```

An ATT weighting comparison keeps treated units at weight one and weights untreated units by the odds of treatment:

```{math}
:label: eq:em1-ipw-att
ATT
=
\mathbb{E}[Y_i\mid D_i=1]
-
\frac{\mathbb{E}\left[\frac{e(X_i)}{1-e(X_i)}(1-D_i)Y_i\right]}
{\mathbb{E}\left[\frac{e(X_i)}{1-e(X_i)}(1-D_i)\right]}.
```

Weighting makes the target population explicit. It also makes weak overlap painful. If {math}`e(X)` is near zero or one, weights can become unstable and a few observations can drive the result.

Doubly robust estimators combine a treatment model with outcome models. One transparent ATE form is

```{math}
:label: eq:em1-aipw
\mathbb{E}\left[
\hat{m}_1(X_i)-\hat{m}_0(X_i)
+
\frac{D_i(Y_i-\hat{m}_1(X_i))}{\hat{e}(X_i)}
-
\frac{(1-D_i)(Y_i-\hat{m}_0(X_i))}{1-\hat{e}(X_i)}
\right],
```

where {math}`\hat{m}_d(X)` predicts outcomes under treatment state {math}`d`. The practical intuition is simple: outcome modeling and treatment modeling each supply a way to reconstruct missing potential outcomes. Combining them can reduce reliance on either model alone, but it does not relax the underlying identifying assumption that selection is captured by observables.

### When Selection-On-Observables Is Strongest

Selection-on-observables is strongest when treatment assignment is substantively understood and the data observe the variables that matter for that assignment. Strong settings often have:

- rich pre-treatment outcomes, not only demographics;
- institutional assignment rules, eligibility scores, counselor recommendations, case histories, or administrative screening variables;
- clear timing, so covariates are measured before treatment;
- untreated comparison units drawn from the same economic environment as treated units;
- enough common support that the design compares like with like;
- limited scope for private information, motivation, provider discretion, or anticipated gains that are both unobserved and strongly related to outcomes.

Training-program evaluation is a useful anchor because the selection story is concrete. Participants differ from nonparticipants in prior earnings, employment histories, education, age, and barriers to work. Some of those variables are observable in administrative records. Others, such as motivation or caseworker discretion, may not be. The design is credible only to the extent that the observed record captures the economically relevant selection margins.

### When It Is Weakest

The design is weakest when the unobserved margin is the main economic margin. Examples include ability, ambition, health shocks, family constraints, firm expectations, political connections, manager discretion, worker beliefs, or anticipated treatment gains. Adding many controls does not solve this if the key selection variable remains latent.

The right interpretation in weak settings may still be useful. An observables-adjusted estimate can show how much of a raw gap is explained by measured differences. It can discipline descriptive comparison. It can define the amount of remaining selection that would be needed to support a causal claim. But the paper should not present the estimator as if it created exogenous variation.

### Theory-To-Applied Design Through Papers

The theory-to-applied bridge is the heart of Lecture 1:

```{include} assets/tables/01-theory-to-applied-bridge.md
```

LaLonde gives the design challenge. Experimental estimates from the National Supported Work demonstration offer a benchmark, and nonexperimental comparison groups show how badly observational estimators can perform when the comparison group does not capture the treated group's untreated counterfactual [@lalonde1986]. The lesson is not "never use observables." The lesson is "the comparison group is the design."

Dehejia and Wahba give the matching anchor. Their reanalysis asks whether careful propensity-score matching, using the right baseline variables and common support restrictions, can recover estimates closer to the experimental benchmark [@dehejiaWahba1999; @dehejiaWahba2002]. The teaching value is that their paper makes design choices visible: which comparison sample, which covariates, which support, which target parameter, and which diagnostics.

Rosenbaum and Rubin give the identification logic. The propensity score is not a magic scalar. It is a balancing score that becomes useful under conditional independence [@rosenbaumRubin1983]. This is why balance diagnostics are design evidence rather than decorative tables.

Altonji, Elder, and Taber plus Oster give the robustness discipline [@altonjiElderTaber2005; @oster2019]. Selection-on-observables papers often live or die after the main table, when readers ask whether unobserved selection could overturn the result. Sensitivity analysis does not prove the assumption. It clarifies how much unobserved selection would be required and whether that amount is plausible relative to observed selection.

### Diagnostics And Robustness As Design Evidence

A selection-on-observables paper should report diagnostics because the identifying assumption is not testable directly. Good diagnostics ask whether the observable implications of the design look credible.

```{include} assets/tables/01-selection-on-observables-diagnostics.md
```

Balance diagnostics ask whether treated and untreated units look similar after adjustment. Standardized differences are more informative than significance tests because balance is a design property, not a hypothesis test powered by sample size.

Overlap diagnostics ask whether the comparison is supported by data. Propensity-score histograms, support ranges, weight distributions, and trimmed estimates show whether the target parameter is being estimated from actual comparisons or from extrapolation.

Matching and weighting choices should be disciplined before outcome hunting. Calipers, exact matching variables, trimming rules, stabilized weights, and covariate sets need an economic rationale. Specification discipline means the preferred estimate should not emerge from searching across models until the desired sign appears.

Sensitivity to unobservables is the last required layer. Oster-style coefficient stability, Altonji-Elder-Taber style selection-on-observables comparisons, Rosenbaum bounds, placebo outcomes, and negative-control outcomes can all help. None of them substitutes for identification. They make the remaining vulnerability visible.

## Research Lab

The Lecture 1 Research Lab follows **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** The main anchor is the LaLonde and Dehejia-Wahba training-program sequence [@lalonde1986; @dehejiaWahba1999; @dehejiaWahba2002]. Students use a bounded synthetic teaching path modeled on the National Supported Work design variables: treatment status, pre-treatment earnings, demographic variables, education, and post-treatment earnings.

**Reproduce.** Students reproduce the design logic, not the official published magnitudes. They estimate a naive difference, a regression-adjusted comparison, a nearest-neighbor propensity-score match, IPW estimates, and a simple doubly robust estimate. The output is a compact table that shows how estimates move as the counterfactual becomes more disciplined.

**Diagnose.** Students inspect balance before and after weighting, propensity-score overlap, common support, and weight stability. They write a short memo explaining which estimates rely most heavily on extrapolation and which estimates are closest to the intended ATT.

**Transfer.** Students then transfer the logic to a different observational setting: take-up of a workplace training or platform upskilling program with rich baseline observables. They must state the target parameter, explain why workers selected into treatment, name the omitted-variable threat, and decide whether the available data are strong enough for a causal claim.

The lab's central question is not "which estimator wins?" It is "what does each estimator require us to believe about the missing potential outcome?"

## Methods Box

:::{admonition} Methods Box: What Makes Observables-Based Designs Persuasive?
:class: note

Strong observables-based designs usually share four ingredients.

1. **Rich pre-treatment information.** Prior outcomes, histories, institutional assignment variables, and timing matter more than long generic covariate lists.
2. **Balance and overlap evidence.** The paper shows that treated and untreated units are comparable in the region used for estimation.
3. **Robustness across estimators and support rules.** Regression adjustment, matching, weighting, and trimmed-support estimates tell a coherent story, or the paper explains why they differ.
4. **Sensitivity to unobservables.** The paper asks how strong omitted selection would need to be to change the interpretation.

The key interpretation sentence is: "This estimate is causal under the maintained assumption that observed pre-treatment variables capture the economically relevant sources of selection into treatment." A reader should be able to point to the institutional setting, the covariate set, the support diagnostics, and the sensitivity analysis and see why that sentence is or is not credible.
:::

## Reading Ladder And References

```{include} assets/tables/01-reading-architecture.md
```

**Foundations.** Start with Rubin for the potential-outcomes tradition and Imbens and Rubin for a full modern treatment of estimands, assignment mechanisms, and identification [@rubin1974; @imbensRubin2015].

**Propensity-score logic.** Rosenbaum and Rubin are essential for understanding why the propensity score is a balancing device tied to conditional independence, not a generic correction [@rosenbaumRubin1983].

**Applied design challenge.** LaLonde is the warning that observational comparison groups can be badly misleading [@lalonde1986].

**Applied design rescue.** Dehejia and Wahba show how matching can be persuasive when the comparison sample, covariates, and common support are taken seriously [@dehejiaWahba1999; @dehejiaWahba2002].

**Estimator discipline.** Abadie and Imbens plus Imbens give students a careful bridge from matching intuition to implementation and inference [@abadieImbens2006; @imbens2015].

**Sensitivity and interpretation.** Altonji, Elder, and Taber plus Oster show how applied economists reason about omitted selection after the main estimates are reported [@altonjiElderTaber2005; @oster2019].

## Exercises And Discussion Prompts

1. Pick a policy setting and write the ATE, ATT, and ATC in words. Which parameter is most relevant for the policy decision?
2. Starting from {eq}`eq:em1-selection-bias`, explain what must be true for the naive difference in means to equal the ATT.
3. For job-training participation, list five pre-treatment covariates that matter for conditional independence. For each one, state the economic selection channel.
4. Give one reason why excellent balance on observed covariates can still leave a design vulnerable to omitted variables.
5. When would weighting be preferable to matching? When would matching be preferable to weighting?
6. Suppose overlap is weak for high-propensity treated units. Should the researcher trim, redefine the estimand, change the comparison group, or stop making a causal claim?
7. Read a selection-on-observables paper in labor, health, education, development, or public economics. Identify the target parameter, the assignment story, the main omitted-variable threat, and the most persuasive diagnostic.
8. Design a transfer project using administrative data. What variables would you need before treatment to make conditional independence plausible?

## Reproducibility And Code Lab Note

The Lecture 1 code lab lives at `labs/01-potential-outcomes-identification-logic-and-selection-on-observables/`. It is a bounded synthetic teaching path inspired by the LaLonde and Dehejia-Wahba design challenge. It does not claim to reproduce the official National Supported Work estimates.

The smoke path creates deterministic synthetic data, estimates naive, regression-adjusted, matching, weighting, and doubly robust comparisons, writes balance and overlap diagnostics, and repeats the design logic in a transfer setting. The lab is deliberately small enough to run locally without external downloads.

## Slide Companion Note

The Lecture 1 slide deck lives at `slides/week1/01-potential-outcomes-identification-logic-and-selection-on-observables.tex`. The deck mirrors the chapter without duplicating it: it defines target parameters, shows the selection-bias decomposition, states conditional independence and overlap, compares the main estimator families, summarizes diagnostics and robustness, and closes with the Research Lab design.

## Bridge Forward

Lecture 2 turns to experiments and field experiments. Randomization changes the assignment mechanism, but it does not remove the need for the discipline introduced here. Experiments still require a target parameter, a treatment definition, a comparison group, outcome measurement, compliance analysis, attrition checks, spillover thinking, and external-validity judgment. The rest of Block 1 can be read as a sequence of alternative ways to make missing potential outcomes credible.
