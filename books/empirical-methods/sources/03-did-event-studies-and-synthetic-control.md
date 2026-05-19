---
title: Lecture 3. DID, Event Studies, and Synthetic Control
bibliography:
  - references.bib
---

# Lecture 3. DID, Event Studies, and Synthetic Control

## Learning Objectives

By the end of this lecture, students should be able to:

1. state the identifying logic of canonical two-period DID, dynamic event studies, and synthetic control;
2. explain the role of parallel trends, no anticipation, and support/overlap in panel settings;
3. diagnose when two-way fixed-effects DID is informative and when staggered adoption with heterogeneous effects makes it misleading;
4. explain the logic behind modern DID corrections and know when to prefer group-time ATT estimators, interaction-weighted event studies, or imputation-based estimators;
5. make practical decisions about clustering, serial correlation, and inference in panel designs;
6. translate a DID, event-study, or synthetic-control idea into a publishable applied project with a clear counterfactual and robustness strategy.

## Opening Orientation

Lecture 3 moves from the clean assignment logic of experiments to panel-based designs that recover a counterfactual from untreated trends. These methods are central to applied economics because many policy, institutional, and market changes occur over time and affect some units but not others. The core question is therefore no longer “who was randomized?” but “which untreated evolution stands in for the missing potential outcomes of the treated units?”

This lecture is also where modern practice matters. DID and event studies are now so widely used that weak implementations can look credible simply because the regression format is familiar. The important distinction is not whether a paper has fixed effects and leads/lags; it is whether the comparison is valid, the estimand is clear, and the inference procedure respects serial dependence and treatment-timing structure.

:::{admonition} Core points
:class: note

- DID, event studies, and synthetic control are all counterfactual panel designs built around trends, not just regression formulas.
- The core identifying question is which untreated evolution stands in for the treated potential outcomes.
- Staggered TWFE can be biased under treatment-effect heterogeneity because it uses bad comparisons and contaminated event-time coefficients.
- Modern DID estimators differ mainly in how they define valid comparisons and aggregate group-time effects.
- Clustering and serial-correlation discipline are part of identification practice, not a technical afterthought.
- Synthetic control is strongest when the treated unit is unusual, the donor pool is credible, and pre-treatment fit is part of the design argument.
:::

## Bridge

Lecture 2 used randomization to construct a counterfactual by design. Lecture 3 now asks what to do when the assignment mechanism is not randomized but the analyst observes untreated units over time. The remaining lectures in Block 1 will change the source of identifying variation again—through instruments and thresholds—but the discipline is the same: define the estimand, state the design assumption, and show why the observed comparison is credible.

## Field Core

### Canonical Two-Period DID

Let {math}`D_i \in \{0,1\}` indicate whether unit {math}`i` is exposed to treatment after period 0, and let {math}`Y_{it}(0)` and {math}`Y_{it}(1)` denote potential outcomes without and with treatment. The classical DID estimand is

```{math}
:label: eq:did-2x2
ATT^{DID} = \Big( \mathbb{E}[Y_{i1} \mid D_i=1] - \mathbb{E}[Y_{i0} \mid D_i=1] \Big)
- \Big( \mathbb{E}[Y_{i1} \mid D_i=0] - \mathbb{E}[Y_{i0} \mid D_i=0] \Big).
```

It identifies the post-treatment average treatment effect on the treated when untreated potential outcomes satisfy parallel trends:

```{math}
:label: eq:parallel-trends
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0) \mid D_i=1]
=
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0) \mid D_i=0].
```

The point of the second difference is not to “control for fixed differences” as a slogan; it is to replace the missing untreated change for the treated group with the observed change for a comparison group.

### What DID Identifies and When It Is Best

Classical DID is strongest when:
- treatment timing is well defined;
- untreated comparison units plausibly track the treated units absent treatment;
- anticipation is limited;
- outcomes are measured consistently over time;
- the main inferential challenge is a policy or shock that changes some units but not others.

It is weakest when untreated comparison units are structurally different in trend, when treatment is rolled out endogenously in response to pre-trends, or when treatment timing is staggered in a way that invites contaminated comparisons.

### Event Studies and Dynamic Effects

A dynamic event-study specification typically writes

```{math}
:label: eq:event-study
Y_{it} = \alpha_i + \lambda_t + \sum_{k \neq -1} \beta_k \mathbf{1}\{t-G_i = k\} + \varepsilon_{it},
```

where {math}`G_i` is first treatment timing and the omitted event time {math}`k=-1` is the baseline. These regressions are appealing because they appear to show both pre-trends and post-treatment dynamics in a single picture.

But the coefficients are only interpretable when the underlying comparisons are valid. Event studies are not a license to replace design reasoning with a figure. The important questions are:
- Which units serve as controls at each relative time?
- Are already-treated units being used as comparisons?
- Is no-anticipation plausible?
- Are treatment effects likely heterogeneous over event time or across cohorts?

### Why Staggered TWFE Can Fail

The modern DID literature shows that in staggered-adoption settings, TWFE can compare newly treated units to already-treated units. With heterogeneous treatment effects, those comparisons are not causal counterfactuals for untreated outcomes. Goodman-Bacon shows that the TWFE coefficient can be decomposed into weighted 2x2 comparisons, some of which are “forbidden” or at least not policy-relevant because the control group is already treated [@goodmanBacon2021].

Sun and Abraham show that dynamic event-study coefficients can be contaminated because relative-time indicators absorb heterogeneous effects from other cohorts [@sunAbraham2021]. The issue is not a small technical correction; it is that the plotted coefficient can fail to correspond to the causal event-time effect students think they are seeing.

### Modern DID Estimators: What They Correct

A useful way to organize the modern literature is by the object it tries to recover.

#### Group-Time ATT Estimation

Callaway and Sant'Anna define cohort- and calendar-time-specific effects

```{math}
:label: eq:att-gt
ATT(g,t) = \mathbb{E}[Y_t(g)-Y_t(\infty) \mid G=g], \qquad t \ge g,
```

and then aggregate them with transparent weights [@callawaySantAnna2021]. The correction logic is simple: compare cohort {math}`g` only to units not yet treated (or never treated) at time {math}`t`, then average after estimation.

**Best use case:** staggered adoption with heterogeneous effects, especially when you want cohort-specific or group-time effects and a transparent aggregation rule.

#### Interaction-Weighted Event Studies

Sun and Abraham recover dynamic event-time effects by interacting event time with cohort and then aggregating valid comparisons [@sunAbraham2021].

**Best use case:** when the main object is the dynamic response profile and treatment timing is staggered.

#### Imputation-Based DID

Borusyak, Jaravel, and Spiess estimate untreated outcomes using untreated observations and then compare realized treated outcomes to imputed untreated paths [@borusyakJaravelSpiess2024]. A simplified representation is

```{math}
:label: eq:bjs-imputation
\widehat{ATT}_{it} = Y_{it} - \widehat{Y}_{it}(0),
```

where {math}`\widehat{Y}_{it}(0)` is predicted from untreated units / untreated periods under an explicit untreated-outcome model.

**Best use case:** staggered treatment with many cohorts, when the researcher wants flexible aggregation and a clean untreated-outcome reconstruction.

#### Practical Rules of Thumb

- **Single adoption date, two groups, short panel:** classical DID is often fine if the design argument is strong.
- **Staggered timing with heterogeneous effects:** do not default to TWFE; use group-time ATT or imputation-based estimators.
- **Dynamic effects are the main object:** prefer interaction-weighted event studies or imputation-based event-time aggregation over naive TWFE event-study plots.
- **Very few treated units / a single treated jurisdiction:** synthetic control may be more persuasive than panel DID.
- **Treatment reversals or complex switching:** be explicit that the standard staggered-adoption toolkit may not apply cleanly.

### Synthetic Control

Synthetic control is best understood as a transparent panel counterfactual method for cases with one or a few treated units. It chooses donor weights to match pre-treatment predictors/outcomes:

```{math}
:label: eq:scm-weights
\widehat{w} = \arg\min_{w} (X_1 - X_0 w)'V(X_1 - X_0 w)
\quad \text{s.t.} \quad w_j \ge 0, \; \sum_j w_j = 1.
```

The post-treatment effect is then

```{math}
:label: eq:scm-effect
\widehat{\tau}_t = Y_{1t} - \sum_j \widehat{w}_j Y_{jt}.
```

Synthetic control is particularly attractive when the treated unit is unusual, conventional parallel-trends arguments are weak, and pre-treatment fit itself is a central design argument. Its weakness is that it depends heavily on donor-pool quality, pre-treatment fit, and credible placebo/permutation logic.

### Variance, Clustering, and Inference

DID-style designs live in panel data, so serial dependence is central. Bertrand, Duflo, and Mullainathan show that naive standard errors can drastically overreject when outcomes are serially correlated and treatment varies at a higher level than the individual observation [@bertrandDufloMullainathan2004].

A transparent cluster-robust variance estimator can be written as

```{math}
:label: eq:crve
\widehat{V}_{CR} = (X'X)^{-1}
\left(\sum_{g=1}^{G} X_g' \widehat{u}_g \widehat{u}_g' X_g \right)
(X'X)^{-1},
```

where {math}`g` indexes clusters.

The main implementation questions are practical, not ceremonial:
- At what level is treatment assigned or plausibly correlated?
- At what level do shocks or residuals co-move?
- Are there enough clusters for asymptotic CRVE to be reliable?
- Would a wild cluster bootstrap be safer?

A good practical rule is to cluster at the level of treatment variation or at a higher plausibly correlated level unless the design suggests otherwise. Few treated clusters, few total clusters, or highly persistent outcomes should trigger caution and often a wild-bootstrap or randomization-inference supplement.

### Parallel Trends, Pre-Trends, and Robustness

Passing a pre-trend test is not the same as establishing parallel trends. Roth’s work is useful here because it shows that low-powered pre-trend tests can make weak designs look reassuring, while conditioning on passing them can distort inference [@roth2022].

A good DID paper therefore needs more than a pre-trend figure. It should provide:
- an institutional argument for why comparison trends are plausible;
- sensitivity to alternative comparison groups and windows;
- checks for composition changes and anticipation;
- inference discipline;
- clarity about what object is actually estimated.

### Theory-to-Applied Research Logic

A strong applied paper in this family usually has this architecture:

1. **Shock or policy.** What changed, when, and for whom?
2. **Counterfactual.** Which untreated units plausibly track the treated units absent treatment?
3. **Estimand.** Is the target a 2x2 ATT, a group-time ATT, a dynamic treatment path, or a single-unit counterfactual gap?
4. **Timing structure.** Is treatment staggered? Are there anticipation effects? Are some units always treated or already treated?
5. **Inference.** What is the relevant clustering level, and how many clusters exist?
6. **Interpretation.** Is the result a local average policy effect, a dynamic response profile, or a synthetic comparison for one treated unit?

This is why Lecture 3 is not “the panel regression lecture.” It is the lecture about how panel comparisons become causal designs.

## Research Lab

The Lecture 3 Research Lab follows **Reproduce → Diagnose → Transfer**.

**Primary anchor.** Card and Krueger’s minimum-wage DID is the primary reproduction anchor [@cardKrueger1994]. It is the cleanest way to teach classical DID and the difference-in-differences estimand.

**Diagnosis anchor.** Goodman-Bacon [@goodmanBacon2021], Callaway and Sant'Anna [@callawaySantAnna2021], Sun and Abraham [@sunAbraham2021], and Borusyak, Jaravel, and Spiess [@borusyakJaravelSpiess2024] provide the diagnosis logic for why staggered TWFE can fail and how modern DID estimators repair the comparison.

**Transfer anchor.** Abadie, Diamond, and Hainmueller [@abadieDiamondHainmueller2010] provide the natural transfer extension: when the treated unit is unusual or isolated, move from staggered DID logic to a synthetic-control counterfactual.

**Reproduce.** Students reproduce a bounded two-period DID on a reduced or synthetic teaching dataset modeled on a classical policy comparison.

**Diagnose.** Students then run a staggered synthetic example and compare naive TWFE estimates to a group-time ATT or imputation-based estimator, explicitly identifying where bad comparisons appear and how clustering changes inference.

**Transfer.** Students then transfer the logic to a single treated unit or small-treated-unit setting using synthetic control. The transfer exercise should force them to name the treated unit, donor pool, pre-treatment fit criterion, and placebo design.

## Methods Box

:::{admonition} Methods Box: Practical Design Rules for DID, Event Studies, and Synthetic Control
:class: note

The most useful practical reminders for this family of methods are:

```{include} assets/tables/03-modern-did-diagnostics.md
```

For inference and clustering, also keep this close at hand:

```{include} assets/tables/03-variance-clustering-and-inference.md
```

The main lesson is that the design problem comes first. Estimator choice follows from the timing structure, treatment heterogeneity, comparison group quality, and inference environment.

:::

## Reading Ladder And References

**Foundations.** Start with Card and Krueger [@cardKrueger1994], Bertrand, Duflo, and Mullainathan [@bertrandDufloMullainathan2004], and Abadie, Diamond, and Hainmueller [@abadieDiamondHainmueller2010].

**Modern DID core.** Then read Goodman-Bacon [@goodmanBacon2021], Callaway and Sant'Anna [@callawaySantAnna2021], Sun and Abraham [@sunAbraham2021], and Borusyak, Jaravel, and Spiess [@borusyakJaravelSpiess2024].

**Interpretation and caution.** Add Roth [@roth2022] and, if helpful, de Chaisemartin and D'Haultfoeuille [@dechaisemartinDhaulfouille2020].

**Use these papers to answer four design questions:**
- What comparison is valid?
- What estimand is being recovered?
- What goes wrong in staggered TWFE?
- What inference discipline is needed?

## Exercises And Discussion Prompts

1. Starting from [](#eq:did-2x2), explain in words what parallel trends means and what it does not mean.
2. Why can a staggered TWFE estimator be biased when treatment effects differ across cohorts or event time?
3. Suppose the main object of interest is a dynamic treatment path. When would you prefer Sun–Abraham to a naive TWFE event study?
4. What is the intuition behind group-time ATT estimation? Why is the “not-yet-treated” comparison important?
5. Give one setting where synthetic control would likely be more persuasive than DID, and explain why.
6. Why can clustering at the wrong level make a design look more precise than it really is?
7. What is the difference between “passing a pre-trend test” and having a persuasive parallel-trends design argument?

## Reproducibility And Code Lab Note

The eventual lab folder for this lecture should live at:

`books/empirical-methods/labs/03-did-event-studies-and-synthetic-control/`

The bounded teaching path should include:
- a simple 2x2 DID reproduction,
- a staggered synthetic panel to diagnose TWFE vs modern DID,
- and a small synthetic-control transfer exercise.

If full original data are not bundled, the lab should be explicit that it reproduces the design logic rather than published magnitudes.

## Slide Companion Note

The slide deck for this lecture should live at:

`books/empirical-methods/slides/week3/03-did-event-studies-and-synthetic-control.tex`

The slides should foreground design logic:
- 2x2 DID and parallel trends,
- event-study interpretation,
- why staggered TWFE can fail,
- how modern DID estimators differ,
- clustering and serial correlation,
- when synthetic control is the right move.

## Bridge Forward

Lecture 3 teaches students to recover counterfactual trends from panel comparisons. Lecture 4 will switch again from trend-based identification to exogenous variation in treatment through instruments. The theme stays the same: define the estimand, justify the comparison, and be explicit about what the design can and cannot identify.
