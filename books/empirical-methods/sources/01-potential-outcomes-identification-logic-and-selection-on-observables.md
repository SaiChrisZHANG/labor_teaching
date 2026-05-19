---
title: Lecture 1. Potential Outcomes, Identification Logic, and Selection-On-Observables
bibliography:
  - references.bib
---

# Lecture 1. Potential Outcomes, Identification Logic, and Selection-On-Observables

## Learning Objectives

By the end of this lecture, students should be able to:

1. define potential outcomes, treatment assignment, target estimands, and the counterfactual problem;
2. explain the selection-bias decomposition and why observational comparisons fail without design assumptions;
3. state when selection-on-observables can identify a causal effect and when it cannot;
4. distinguish regression adjustment, matching, weighting, and doubly robust estimators at the level of design logic;
5. interpret results from observables-based designs cautiously, including overlap, balance, and sensitivity diagnostics;
6. map a theory of selection into a publishable applied research project.

## Opening Orientation

This lecture sets the language for the rest of the methods course. Even when a paper later calls itself experimental, quasi-experimental, structural, or machine-learning-based, it still needs three things: a target parameter, a credible counterfactual, and an argument for why the observed data are informative about the missing potential outcomes. The potential-outcomes framework is therefore not a niche formalism; it is the bookkeeping system for applied research.

Selection-on-observables is introduced here as a serious design rather than as the weakest possible fallback. In many applied settings, treatment is not randomized, but researchers do observe institutional detail, rich baseline covariates, timing, and pre-treatment outcomes. The core question is whether those observables are enough to make treated and untreated units comparable for the estimand of interest.

:::{admonition} Core points
:class: note

- Every causal design begins with a target parameter and an explicit counterfactual.
- Observational comparisons fail because treatment status is selected, not because regression is intrinsically bad.
- Selection-on-observables identifies causal effects only when conditional independence and overlap are economically plausible.
- Matching, regression adjustment, weighting, and doubly robust estimators are all ways of operationalizing the same design logic.
- A good observables-based paper is persuasive when it shows rich institutional knowledge, overlap, balance, and sensitivity to omitted variables.
:::

## Bridge

Lecture 1 gives students the design logic that underlies the rest of Block 1. Experiments in Lecture 2 make the counterfactual cleaner by design. DID, IV, and RD later in the block will replace conditional independence with other identification assumptions. So this lecture is not only about observables-based methods; it is about how to think clearly about any causal design.

## Field Core

### The Fundamental Problem of Causal Inference

Let {math}`Y_i(1)` denote the potential outcome for unit {math}`i` if treated and {math}`Y_i(0)` the potential outcome if untreated. Let {math}`D_i \in \{0,1\}` indicate treatment. The realized outcome is

```{math}
:label: eq:po-realized-outcome
Y_i = D_i Y_i(1) + (1-D_i)Y_i(0).
```

The causal effect for a unit is

```{math}
:label: eq:unit-effect
\tau_i = Y_i(1) - Y_i(0),
```

but researchers never observe both potential outcomes for the same unit. This is the fundamental problem. All empirical methods are attempts to recover some average of {math}`\tau_i` by using variation across units, places, time, or assignment rules.

### Target Parameters

The first design choice is the estimand. Three common parameters are:

```{math}
:label: eq:ate
ATE = \mathbb{E}[Y(1)-Y(0)],
```

```{math}
:label: eq:att
ATT = \mathbb{E}[Y(1)-Y(0)\mid D=1],
```

```{math}
:label: eq:atc
ATC = \mathbb{E}[Y(1)-Y(0)\mid D=0].
```

A good paper does not jump directly to estimation. It first asks which parameter is policy-relevant or theoretically meaningful. A training program may naturally motivate the ATT; a universal policy proposal may motivate the ATE; a targeting question may require the ATC or a richer heterogeneous-effect object.

### Why Observational Comparisons Are Biased

The naive difference in mean outcomes can be decomposed as

```{math}
:label: eq:selection-bias
\mathbb{E}[Y\mid D=1] - \mathbb{E}[Y\mid D=0]
=
ATT
+
\Big(\mathbb{E}[Y(0)\mid D=1] - \mathbb{E}[Y(0)\mid D=0]\Big).
```

The second term is the selection-bias term. It is the difference in untreated potential outcomes between treated and untreated units. The entire design problem is to make that term vanish, or at least argue that it is small enough and disciplined enough to be informative.

### Conditional Independence and Overlap

Selection-on-observables replaces unconditional comparability with conditional comparability. Let {math}`X_i` be observed covariates. The key identifying assumption is

```{math}
:label: eq:cia
\{Y_i(1), Y_i(0)\} \perp D_i \mid X_i,
```

often called conditional independence, selection-on-observables, or unconfoundedness.

The corresponding support condition is overlap:

```{math}
:label: eq:overlap
0 < \Pr(D_i=1 \mid X_i=x) < 1
\quad \text{for all relevant } x.
```

These are not statistical housekeeping assumptions. They are economic statements. Conditional independence says that once the relevant selection variables are held fixed, assignment is as good as random. Overlap says the treated and untreated groups actually coexist over the relevant support of {math}`X` so comparison is possible.

### The Main Estimation Families

#### Regression Adjustment

A regression-adjustment design models

```{math}
:label: eq:ra
\mathbb{E}[Y \mid D, X] = \alpha + \tau D + g(X),
```

or richer interactive/flexible versions of {math}`g(X)`. The strength of regression adjustment is transparency and easy extension. The weakness is functional-form dependence if the conditional expectation is misspecified.

#### Matching

Matching tries to construct treated and untreated groups with similar covariate distributions. Exact matching, nearest-neighbor matching, Mahalanobis matching, and propensity-score matching all operationalize the same idea: replace an incomparable untreated group with one that looks more like the treated group on observed dimensions.

The main economic question is not “which matching algorithm is fashionable?” but “have I matched on the variables that jointly drive both treatment and untreated outcomes?”

#### Weighting

Inverse-probability weighting uses the propensity score {math}`e(X)=\Pr(D=1\mid X)` to reweight observations and recover a target estimand. For the ATE, one canonical form is

```{math}
:label: eq:ipw
ATE
=
\mathbb{E}\left[\frac{D Y}{e(X)} - \frac{(1-D)Y}{1-e(X)}\right].
```

The value of weighting is that it makes the balancing logic explicit. The danger is instability when overlap is weak and estimated propensity scores get close to 0 or 1.

#### Doubly Robust Logic

Doubly robust estimators combine an outcome model and a treatment model. Intuitively, they protect the estimator when one nuisance model is misspecified but the other is reasonably well specified. Students do not need the full semiparametric theory in Lecture 1, but they should understand why observables-based designs increasingly use flexible nuisance estimation together with balance and overlap diagnostics.

### When Selection-on-Observables Is Most Credible

This design is most persuasive when:

- assignment depends on rich observed institutional criteria;
- baseline outcomes and histories are recorded;
- treatment timing is well measured;
- researchers understand why units enter treatment and can measure the relevant margins of that choice;
- untreated units plausibly represent the counterfactual support of treated units.

Classic examples include training-program evaluation, school/program take-up with rich baseline records, medical treatment choices with detailed claims and diagnoses, and labor-market programs with administrative eligibility rules plus observable participant histories.

### When It Is Weakest

Selection-on-observables is weakest when the key selection margins are latent and economically important:
- motivation,
- ability,
- private beliefs,
- family shocks,
- anticipated gains,
- political or social connections,
- provider discretion that is not recorded.

In those cases, the method can still be useful descriptively, but the burden of interpretation and sensitivity analysis becomes much heavier.

### Theory-to-Applied Research Design

A good applied paper in this space usually has this architecture:

1. **Target parameter.** What average effect is substantively meaningful?
2. **Selection story.** Why do units choose or receive treatment?
3. **Observed proxies for the selection story.** Which variables make conditional independence more plausible?
4. **Support.** Are treated and untreated units comparable in the relevant region?
5. **Estimator choice.** Why matching, weighting, regression adjustment, or a doubly robust combination?
6. **Robustness.** How fragile is the result to omitted variables, support loss, or model choice?

This is why selection-on-observables is not “just running a regression.” The design lives or dies on the researcher’s economic story of treatment assignment.

## Research Lab

The Lecture 1 Research Lab follows **Reproduce → Diagnose → Transfer**.

**Primary anchor.** LaLonde’s training-program comparison, together with Dehejia and Wahba’s matching reanalysis, is the natural anchor for this lecture [@lalonde1986; @dehejiaWahba1999; @dehejiaWahba2002]. It is the canonical case for asking whether observables can reconstruct a credible counterfactual.

**Challenge anchor.** Rosenbaum and Rubin provide the balancing-score logic behind the propensity score [@rosenbaumRubin1983], while modern sensitivity work by Altonji, Elder, and Taber and by Oster provides the practical robustness language students will keep using in applied work [@altonjiElderTaber2005; @oster2019].

**Reproduce.** Students reproduce a bounded version of the job-training comparison, estimating naive differences, regression-adjusted estimates, matching estimates, and simple weighting estimates on a reduced or synthetic teaching dataset.

**Diagnose.** Students then diagnose why the answers differ. They inspect balance, common support, covariate overlap, propensity-score tails, and sensitivity to specification. The diagnosis question is not “which estimator is right?” but “what does each estimator assume about the counterfactual?”

**Transfer.** Students then transfer the design logic to a different observational setting: for example, program take-up, training participation, school-track choice, or platform adoption, where rich observables make selection-on-observables plausible but not automatic. The transfer exercise should force them to name the target parameter, the selection story, the required observables, and the main omitted-variable threat.

## Methods Box

:::{admonition} Methods Box: What Makes Observables-Based Designs Persuasive?
:class: note

A strong observables-based design usually has four ingredients:

1. **Rich pre-treatment information.** Prior outcomes and institutional assignment variables matter more than a long generic covariate list.
2. **Balance and overlap evidence.** Show whether treated and untreated units are actually comparable.
3. **Robustness across estimators.** Compare regression adjustment, matching, weighting, and trimmed-support designs.
4. **Sensitivity to unobservables.** Ask how strong omitted selection would need to be to overturn the conclusion.

Useful diagnostics and tools include:

```{include} assets/tables/01-selection-on-observables-diagnostics.md
```

The key lesson is interpretation. A result from selection-on-observables should be read as “causal under the maintained assumption that observed variables capture the economically relevant sources of selection.” The credibility of the claim rises when institutional knowledge makes that assumption compelling.

:::

## Reading Ladder And References

**Foundations.** Start with Rosenbaum and Rubin on the propensity score and with Imbens and Rubin for the potential-outcomes framework [@rosenbaumRubin1983; @imbensRubin2015].

**Canonical applied anchor.** Read LaLonde first for the challenge, then Dehejia and Wahba for the matching reanalysis [@lalonde1986; @dehejiaWahba1999; @dehejiaWahba2002].

**Practical design/diagnostic layer.** Add Abadie and Imbens on matching estimators and Imbens on identification/design logic [@abadieImbens2006; @imbens2015].

**Sensitivity and interpretation.** Use Altonji, Elder, and Taber plus Oster to show how economists reason about omitted variables after the main estimates are reported [@altonjiElderTaber2005; @oster2019].

## Exercises And Discussion Prompts

1. Write down the difference between the ATE and the ATT in a policy setting of your choice. Which one is more relevant, and why?
2. Starting from [](#eq:selection-bias), explain in words what must be true for the naive difference in means to equal the ATT.
3. Suppose treatment is job-training participation. List five covariates that matter for conditional independence and explain the economic selection channel behind each.
4. Why can good balance on observed covariates still leave a design vulnerable to omitted variables?
5. In an observables-based paper, when would you prefer weighting to matching? When might trimming be necessary?
6. Give one applied setting in labor, development, urban, health, or public economics where selection-on-observables is likely strong and one where it is likely weak.

## Reproducibility And Code Lab Note

The eventual lab folder for this lecture should live at:

`books/empirical-methods/labs/01-potential-outcomes-identification-logic-and-selection-on-observables/`

The bounded teaching path should use a reduced or synthetic dataset modeled on the LaLonde/Dehejia–Wahba design so the lab is runnable locally without external downloads. If full original data are not bundled, the lab should be explicit that it reproduces the design logic rather than published magnitudes.

## Slide Companion Note

The slide deck for this lecture should live at:

`books/empirical-methods/slides/week1/01-potential-outcomes-identification-logic-and-selection-on-observables.tex`

The slides should foreground the design logic:
- target parameter,
- counterfactual,
- identifying assumption,
- support,
- estimator,
- diagnostics,
- interpretation.

## Bridge Forward

Lecture 2 will remove the selection-on-observables assumption and replace it with randomized assignment. That move simplifies the counterfactual, but it does not eliminate the need to think carefully about implementation, compliance, spillovers, attrition, and external validity. The rest of Block 1 can be read as a sequence of alternative ways to solve the same problem introduced here: how to make the missing potential outcomes economically and empirically credible.
