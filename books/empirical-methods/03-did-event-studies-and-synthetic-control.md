# Lecture 3. DID, Event Studies, And Synthetic Control

## Learning Objectives

By the end of this lecture, students should be able to:

1. state the identifying logic of canonical two-period DID, dynamic event studies, modern staggered-adoption DID, and synthetic control;
2. explain parallel trends, no anticipation, support, donor-pool quality, and pre-treatment fit as design requirements rather than regression decorations;
3. derive and interpret the 2x2 DID estimand, TWFE event-study specification, group-time ATT, imputation-style ATT, synthetic-control weighting problem, and cluster-robust variance estimator;
4. diagnose when TWFE is informative and when staggered adoption with heterogeneous treatment effects creates forbidden comparisons, contaminated event-time coefficients, or misleading weights;
5. choose among Goodman-Bacon diagnostics, Callaway-Sant'Anna group-time ATT estimation, Sun-Abraham interaction-weighted event studies, Borusyak-Jaravel-Spiess imputation DID, and synthetic control for a concrete applied setting;
6. make practical inference decisions about serial correlation, clustering level, few-cluster problems, wild cluster bootstrap, and placebo or permutation evidence;
7. translate a panel-comparison idea into a publishable applied project with a clear counterfactual, estimand, robustness plan, and interpretation.

## Opening Orientation

Lecture 3 moves from the clean assignment logic of experiments to designs that build counterfactuals from outcome paths. The central question is no longer "who was randomized?" It is "which untreated evolution stands in for the treated units' missing untreated outcomes?"

This question appears constantly in applied economics. Minimum-wage changes, plant openings, court rulings, platform rules, immigration shocks, unemployment-insurance reforms, collective-bargaining laws, technology adoption, and city-level policies often affect some groups or places before others. Researchers observe outcomes before and after the change. The temptation is to run a fixed-effects regression and call the result a design. This lecture pushes in the opposite direction: the regression is only persuasive when the comparison path is credible.

Card and Krueger are the classical anchor because their New Jersey and Pennsylvania comparison makes the 2x2 DID logic visible [@cardKrueger1994]. Bertrand, Duflo, and Mullainathan are the inference warning because serial correlation can make DID estimates look much more precise than they are [@bertrandDufloMullainathan2004]. Goodman-Bacon explains what TWFE estimates in staggered-adoption settings [@goodmanBacon2021]. Callaway and Sant'Anna, Sun and Abraham, and Borusyak, Jaravel, and Spiess give modern ways to recover interpretable effects when timing and effects are heterogeneous [@callawaySantAnna2021; @sunAbraham2021; @borusyakJaravelSpiess2024]. Abadie, Diamond, and Hainmueller show how to build a synthetic untreated path when one treated unit needs a custom comparison [@abadieDiamondHainmueller2010]. Roth supplies a caution about treating pre-trend tests as proof of identification [@roth2022].

## Core Points

:::{admonition} Core points
:class: important

- DID, event studies, and synthetic control are counterfactual panel designs. They are not just fixed-effects estimators.
- The central identifying object is the missing untreated path for treated units.
- Classical 2x2 DID identifies an ATT when treated and comparison groups would have followed parallel untreated trends.
- Naive staggered TWFE can be biased under heterogeneous effects because it can compare treated units to already-treated units and contaminate event-time coefficients.
- Modern DID estimators repair the comparison set, the aggregation weights, or the untreated-outcome imputation; they do not eliminate the need for a persuasive design.
- Inference is part of the design: serial correlation, clustering level, few clusters, and placebo evidence determine whether the estimate is defensible.
- Synthetic control belongs in the same panel comparative toolkit because it builds a counterfactual path when average untreated trends are too crude.
:::

## Bridge

Lecture 2 used random assignment to construct a counterfactual by design. DID replaces random assignment with untreated outcome paths. Event studies add timing and dynamics. Synthetic control replaces an average comparison group with a weighted donor path. Each method answers the same potential-outcomes question from Lecture 1: what observed object can stand in for the missing potential outcome?

The remaining lectures in Block 1 will change the source of identifying variation again, through instruments and discontinuities. The discipline remains the same: define the estimand, state the identifying comparison, explain what can break it, and show what the estimate can and cannot support.

## Field Core

### Canonical Two-Period DID

Let {math}`D_i \in \{0,1\}` indicate whether unit {math}`i` belongs to the group exposed to treatment after period 0. Let {math}`Post_t` indicate the post-treatment period. Potential outcomes are {math}`Y_{it}(1)` under treatment and {math}`Y_{it}(0)` without treatment. In the simple two-group, two-period design, the canonical DID estimand is:

```{math}
:label: eq:em3-did-2x2
\tau^{DID}
=
\Big(\mathbb{E}[Y_{i1}\mid D_i=1]-\mathbb{E}[Y_{i0}\mid D_i=1]\Big)
-
\Big(\mathbb{E}[Y_{i1}\mid D_i=0]-\mathbb{E}[Y_{i0}\mid D_i=0]\Big).
```

This is a difference in outcome changes. It subtracts the comparison group's change from the treated group's change because the treated group's untreated post-period outcome is missing.

The identifying restriction is parallel trends in untreated potential outcomes:

```{math}
:label: eq:em3-parallel-trends
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0)\mid D_i=1]
=
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0)\mid D_i=0].
```

Under {eq}`eq:em3-parallel-trends` and no anticipation, {eq}`eq:em3-did-2x2` identifies the average treatment effect on the treated in the post period:

```{math}
:label: eq:em3-att-post
ATT_1
=
\mathbb{E}[Y_{i1}(1)-Y_{i1}(0)\mid D_i=1].
```

The fixed-effects regression version is:

```{math}
:label: eq:em3-simple-did-regression
Y_{it}=\alpha_i+\lambda_t+\tau(D_i \times Post_t)+\varepsilon_{it}.
```

In the 2x2 case, {math}`\hat{\tau}` equals the DID contrast. The regression does not create identification. It implements the comparison in {eq}`eq:em3-did-2x2`.

### What Classical DID Identifies

Classical DID is best used when a policy or shock affects one group at a clear date, untreated comparison units are economically close enough to proxy for the treated group's counterfactual trend, and treatment is not anticipated in a way that changes pre-period behavior. Card and Krueger's minimum-wage comparison is useful pedagogically because the treated group, comparison group, timing, and outcome are visible [@cardKrueger1994].

The design identifies an ATT for the treated group and post-treatment period covered by the comparison. It does not identify the effect for places with different institutions, the effect of a much larger policy, equilibrium effects outside the treated and comparison markets, or dynamic effects beyond the observed outcome window. In a minimum-wage setting, for example, a short-run restaurant employment DID is not automatically a statement about long-run automation, entry and exit, prices, or monopsony power. Those may be mechanisms or extensions, but the DID estimand is narrower.

Implementation caveats are concrete. The researcher must define the treatment date, prevent post-treatment covariates from entering as controls, use pre-treatment outcomes to assess trend plausibility, inspect composition changes, and match inference to the assignment level. If stores are observed within states and the policy varies by state, unit-level standard errors are not enough.

The correct interpretation sentence is: "Relative to the comparison group's change, the treated group changed by {math}`\hat{\tau}` more after treatment; under parallel untreated trends and no anticipation, this is the post-treatment ATT for the treated group in this setting."

### Event Studies And Dynamic Treatment Paths

Event studies extend DID by estimating effects before and after treatment relative to an event date. Let {math}`G_i` denote unit {math}`i`'s first treatment period, and define event time {math}`k=t-G_i`. A common TWFE event-study specification is:

```{math}
:label: eq:em3-twfe-event-study
Y_{it}
=
\alpha_i+\lambda_t+
\sum_{k\neq -1}\beta_k\mathbf{1}\{t-G_i=k\}
+\varepsilon_{it},
```

where event time {math}`k=-1` is the omitted baseline.

Event studies are best used when the timing of treatment is meaningful and the researcher needs to show dynamic response: whether effects emerge immediately, build slowly, fade out, or appear before formal implementation. They are also useful for visualizing whether pre-treatment outcome paths are grossly inconsistent with the design story.

What an event study identifies depends on the timing structure. With one treated cohort and a never-treated or clean not-yet-treated comparison group, post-event coefficients can be interpreted as dynamic ATT estimates under parallel trends and no anticipation. With staggered adoption, the same TWFE formula can mix comparisons across cohorts in ways that no longer correspond to cohort-specific event-time effects.

Event studies do not prove parallel trends. Insignificant pre-period coefficients may reflect low power, noisy outcomes, or selective specification choices. Roth shows why conditioning interpretation on a passed pre-trend test can be misleading [@roth2022]. A good event-study figure is design evidence, not the design itself.

Practical implementation should report the event-time window, binning of distant leads and lags, omitted category, included cohorts, treatment reversals, anticipation window, and comparison group used for each coefficient. If the policy was announced before implementation, event time should reflect the first point at which behavior could respond, or the estimand should explicitly allow anticipation.

### Staggered Adoption And Group-Time Effects

Many applied settings have staggered adoption: some states, firms, schools, or markets adopt earlier than others. Let {math}`G_i=g` denote first treatment in period {math}`g`; let {math}`G_i=\infty` denote never treated. A transparent modern target is the group-time ATT:

```{math}
:label: eq:em3-group-time-att
ATT(g,t)
=
\mathbb{E}\left[Y_{it}(g)-Y_{it}(\infty)\mid G_i=g\right],
\qquad t\ge g.
```

This object asks: for the cohort first treated in period {math}`g`, what is the treatment effect at calendar time {math}`t` relative to remaining untreated? Aggregated effects should then use explicit weights:

```{math}
:label: eq:em3-att-aggregation
ATT^{agg}
=
\sum_{g}\sum_{t\ge g}\omega_{gt}ATT(g,t),
\qquad
\sum_{g}\sum_{t\ge g}\omega_{gt}=1.
```

The aggregation weights are a research choice. An event-time average answers a dynamic-response question. A cohort-size-weighted average answers a population exposure question. A calendar-time average answers a policy-environment question. Modern DID makes that choice visible.

### Why Staggered TWFE Can Fail

The standard TWFE regression for staggered adoption is:

```{math}
:label: eq:em3-staggered-twfe
Y_{it}=\alpha_i+\lambda_t+\tau D_{it}+\varepsilon_{it},
```

where {math}`D_{it}=1` once unit {math}`i` has adopted. The problem is not that fixed effects are bad. The problem is that, with staggered timing, the regression can use already-treated units as controls for later-treated units and later-treated units as controls for earlier-treated units. When treatment effects vary across cohorts or event time, already-treated outcomes include treatment effects. They are not untreated counterfactuals.

Goodman-Bacon decomposes the TWFE coefficient into weighted 2x2 DID comparisons [@goodmanBacon2021]. Some comparisons are clean: treated cohorts versus never-treated units, or earlier-treated versus later-treated units before the latter adopt. Others are problematic: later-treated cohorts compared to earlier-treated cohorts after the earlier cohorts are already exposed. Those comparisons are often called forbidden comparisons because the control group is contaminated by treatment.

The bias logic has three connected pieces.

First, **forbidden comparisons** use treated potential outcomes where the design needs untreated potential outcomes. If an early adopter already has a large effect, its post-adoption path is a bad proxy for what a later adopter would have done without treatment.

Second, **event-study contamination** arises when TWFE relative-time coefficients absorb treatment effects from other cohorts. Sun and Abraham show that a coefficient plotted as the effect at event time {math}`k` can contain weighted averages of effects from other event times and cohorts [@sunAbraham2021]. A flat pre-trend in a naive TWFE event study can therefore be less reassuring than it looks.

Third, **weighting problems** mean the TWFE coefficient may not be a convex average of the policy-relevant effects the researcher has in mind. Some effects can receive unintuitive or negative implicit weights. A single number can look precise while answering a poorly defined mixture of comparisons.

This does not mean every old TWFE estimate is wrong. If treatment effects are constant, if adoption timing is effectively two-group, or if forbidden comparisons carry little weight, the problem can be small. But in applied work with plausible heterogeneity, TWFE should be treated as a diagnostic starting point rather than the default final answer.

### Modern DID Methods

Modern DID methods differ in how they define valid comparisons and recover interpretable effects. The choice should follow the research question, not software fashion.

**Goodman-Bacon decomposition.** Use this when you need to diagnose a static TWFE estimate. It tells you which 2x2 comparisons contribute to {math}`\hat{\tau}` and how much weight they receive [@goodmanBacon2021]. It does not, by itself, produce the preferred causal estimate. Its main contribution is to reveal whether the headline regression is driven by clean comparisons or contaminated ones.

**Callaway-Sant'Anna group-time ATT.** Use this when the natural object is {math}`ATT(g,t)` or an explicit aggregation of those effects [@callawaySantAnna2021]. The estimator compares a treated cohort to never-treated or not-yet-treated units, then aggregates transparently. It is especially useful when cohorts differ in levels, timing, or treatment-effect paths and the paper needs to report effects by cohort, calendar time, or event time.

The implementation rule is to define the comparison group before estimating. Never-treated controls are clean if they are comparable and exist in sufficient number. Not-yet-treated controls can improve support, but they require the assumption that future adopters are valid untreated comparisons before adoption. The aggregation should match the paper's claim.

**Sun-Abraham interaction-weighted event studies.** Use this when the main object is the dynamic event-time path under staggered adoption [@sunAbraham2021]. The method interacts cohort and relative time so that event-time effects are estimated from valid cohort-specific comparisons and then aggregated. It is the natural replacement for a naive TWFE event-study plot when students want the graph to mean what readers think it means.

The caveat is interpretation: the plotted event-time coefficient is still an average over cohorts that contribute observations at that relative time. Long-run lags may be identified by early adopters only. Report cohort support by event time when the window is long.

**Borusyak-Jaravel-Spiess imputation DID.** Use this when the design can be framed as estimating untreated outcomes from untreated observations and imputing missing counterfactuals for treated observations [@borusyakJaravelSpiess2024]. A simplified imputation logic is:

```{math}
:label: eq:em3-bjs-imputation-att
\widehat{ATT}_{\mathcal{S}}
=
\frac{1}{|\mathcal{S}|}
\sum_{(i,t)\in \mathcal{S}}
\left(Y_{it}-\widehat{Y}_{it}(0)\right),
```

where {math}`\mathcal{S}` is a chosen set of treated observations and {math}`\widehat{Y}_{it}(0)` is predicted using untreated observations under a model for untreated potential outcomes, often with unit and time fixed effects.

This approach is attractive when there are many cohorts, many potential aggregations, and a clear untreated-outcome model. The caveat is that imputation makes the untreated-outcome model explicit. If untreated trends differ in ways the model misses, the imputed counterfactual can be wrong even though the estimator avoids forbidden comparisons.

**de Chaisemartin-D'Haultfoeuille and related corrected TWFE approaches.** Use these when treatment is staggered or switching and you need estimators designed to avoid negative or contaminated weights [@dechaisemartinDhaulfouille2020]. These methods are valuable for understanding the weighting problem and for settings where treatment paths are more complex than simple absorbing adoption.

The practical decision rules are:

- If the design is truly two groups and two periods, start with classical DID and make parallel trends persuasive.
- If treatment is staggered and effects may be heterogeneous, do not present naive TWFE as the main estimate without a decomposition or modern alternative.
- If the estimand is a dynamic path, use Sun-Abraham or imputation-based event-time estimates and report support by event time.
- If the estimand is cohort or calendar-time policy incidence, use Callaway-Sant'Anna group-time ATT estimates and aggregate explicitly.
- If the design has one treated state, city, firm, or market, synthetic control may be more credible than an average-control DID.
- If treatment reverses, switches repeatedly, or has varying intensity, define the treatment path and estimand before choosing the estimator.

### Synthetic Control As A Panel Counterfactual

Synthetic control belongs in the same family as DID because it solves the same missing-path problem differently. Instead of assuming the treated unit would follow the average trend of a comparison group, it constructs a weighted combination of untreated donor units that matches the treated unit before treatment.

Let unit 1 be treated after period {math}`T_0`, and let donor units {math}`j=2,\dots,J+1` remain untreated. Let {math}`X_1` contain pre-treatment outcomes and predictors for the treated unit, and {math}`X_0` contain the same objects for donors. Synthetic control chooses weights:

```{math}
:label: eq:em3-scm-weights
\widehat{w}
=
\arg\min_{w}
(X_1-X_0w)'V(X_1-X_0w)
\quad
\text{s.t.}
\quad
w_j\ge 0,\;
\sum_{j=2}^{J+1}w_j=1.
```

The post-treatment treatment effect estimate is:

```{math}
:label: eq:em3-scm-effect
\widehat{\tau}_{1t}
=
Y_{1t}-\sum_{j=2}^{J+1}\widehat{w}_jY_{jt},
\qquad t>T_0.
```

Synthetic control is best used when there is one or a small number of treated aggregate units, the treated unit is unusual enough that a simple untreated average is not persuasive, and a donor pool can reproduce the pre-treatment path. Abadie, Diamond, and Hainmueller's California tobacco example is the standard design anchor [@abadieDiamondHainmueller2010].

It identifies a unit-specific counterfactual gap under the assumption that the weighted donor path approximates the treated unit's untreated potential outcome after treatment. It does not identify a population-average treatment effect unless the treated unit is itself the population of interest or the researcher adds a separate argument for external validity.

The implementation caveats are concrete: define the donor pool before looking at post-treatment outcomes, avoid donors affected by spillovers, report pre-treatment fit, show the weights, inspect whether one donor dominates, run placebo or permutation exercises, and separate poor pre-fit from a null effect. If the synthetic control cannot match the treated unit before treatment, the post-treatment gap is hard to interpret.

### Variance, Clustering, And Inference

DID and event-study designs almost always involve persistent outcomes, persistent treatment, and grouped assignment. Bertrand, Duflo, and Mullainathan show why this matters: if researchers ignore serial correlation, standard errors can severely overreject [@bertrandDufloMullainathan2004]. A policy that turns on once and stays on creates a highly persistent treatment variable. Employment, earnings, prices, firm outcomes, and local labor-market conditions are also persistent. Treating each unit-period observation as independent manufactures precision.

For a linear model {math}`Y=X\beta+u`, a transparent cluster-robust variance estimator is:

```{math}
:label: eq:em3-cluster-robust-variance
\widehat{V}_{CR}
=
(X'X)^{-1}
\left(\sum_{g=1}^{G}X_g'\widehat{u}_g\widehat{u}_g'X_g\right)
(X'X)^{-1},
```

where {math}`g` indexes clusters, {math}`X_g` stacks observations in cluster {math}`g`, and {math}`\widehat{u}_g` stacks residuals in that cluster. The key idea is simple: allow arbitrary residual correlation within each cluster and rely on independence, or weaker dependence, across clusters.

The clustering level should be chosen from the design. Cluster at the level where treatment is assigned or where shocks plausibly co-move. If the policy varies by state, state-level clustering is the natural starting point even if the data contain many individuals or firms. If treatment varies by school district, firm, commuting zone, or market, inference should respect that level. When shocks are correlated across both units and time, two-way clustering or spatially robust methods may be appropriate, but the paper must explain the dependence structure rather than choose the smallest standard error.

Few clusters create a separate problem. Conventional cluster-robust asymptotics can perform poorly with a small number of clusters, few treated clusters, or highly unbalanced cluster sizes. In those cases, report the number of total and treated clusters, use wild cluster bootstrap as a practical remedy when appropriate, and consider randomization-inference or placebo-style evidence when the assignment process is design-based. Synthetic-control settings often need placebo or permutation logic because there may be only one treated aggregate unit.

Standard errors can look precise when the design is not. A small standard error around a contaminated TWFE estimand does not rescue the estimand. A tight synthetic-control post-treatment gap does not help if pre-treatment fit is poor. Inference quantifies sampling uncertainty around a design object; it does not validate the comparison.

### Parallel Trends, Pre-Trends, And Robustness

Parallel trends is an assumption about untreated potential outcomes. It is not a claim that treated and control units have the same levels. It is not proven by adding unit and time fixed effects. It is not automatically established by an insignificant lead coefficient.

Useful evidence includes:

- institutional timing showing that adoption was not a response to outcome trends;
- pre-treatment outcome paths over several periods when available;
- comparison-group sensitivity;
- composition checks for treated and comparison units;
- anticipation checks around announcement and implementation;
- placebo outcomes or placebo policies;
- robustness to alternative windows, binning choices, and aggregation weights;
- transparent inference at the assignment level.

The strongest DID papers combine institutional knowledge and empirical diagnostics. A weak paper treats a pre-trend figure as a permission slip. A strong paper explains why the comparison units are the right counterfactual, what remaining violations would mean, and how robust the conclusion is to plausible alternatives.

### Theory-To-Applied Design Through Papers

The theory-to-applied bridge for this lecture is:

```{include} assets/tables/03-theory-to-applied-bridge.md
```

Card and Krueger are the classical design anchor because students can see every component of the DID: a treated state, comparison state, pre and post periods, and an employment outcome [@cardKrueger1994]. The paper also teaches a broader lesson: a controversial estimate must be defended through design, measurement, and sensitivity, not only through a coefficient.

Bertrand, Duflo, and Mullainathan shift attention from point estimates to inference [@bertrandDufloMullainathan2004]. Their lesson should be part of every DID project: panel designs can have many observations and still have little independent variation.

Goodman-Bacon makes the hidden comparison structure visible [@goodmanBacon2021]. The decomposition is most valuable before the final estimator is chosen because it tells the researcher whether TWFE is summarizing clean 2x2 comparisons or mixing in already-treated controls.

Callaway and Sant'Anna, Sun and Abraham, and Borusyak, Jaravel, and Spiess are not interchangeable software commands [@callawaySantAnna2021; @sunAbraham2021; @borusyakJaravelSpiess2024]. They correspond to different ways of defining the estimand and comparison set. A student should be able to say why one is the right baseline for the question.

Abadie, Diamond, and Hainmueller complete the panel toolkit by showing how donor construction can be the design [@abadieDiamondHainmueller2010]. When the treated unit is a state, city, or firm with a distinctive pre-period path, synthetic control may be more honest than asking an untreated average to do too much.

### Design Checklist

Before estimating, a DID, event-study, or synthetic-control paper should answer eight questions:

1. What changed, when, and for whom?
2. What is the target estimand: 2x2 ATT, {math}`ATT(g,t)`, event-time path, aggregate ATT, or unit-specific synthetic gap?
3. Which units are valid controls at each time?
4. Is treatment absorbing, staggered, reversible, or continuous?
5. Is no anticipation plausible, or should the event window start at announcement?
6. What is the relevant clustering or placebo-inference level?
7. How will the paper diagnose pre-treatment comparability, support, and composition?
8. What does the estimate not identify?

This is why Lecture 3 is not "the panel regression lecture." It is the lecture about how panel comparisons become causal designs.

## Research Lab

The Lecture 3 Research Lab follows **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** Card and Krueger's minimum-wage DID is the reproduction anchor [@cardKrueger1994]. Students use a bounded synthetic teaching path modeled on a two-state fast-food comparison. The lab does not reproduce official published magnitudes. It reproduces the design logic: before-after differences, comparison-state trends, the DID contrast, and state-level inference.

**Diagnosis anchor.** Goodman-Bacon, Callaway and Sant'Anna, Sun and Abraham, and Borusyak, Jaravel, and Spiess provide the modern DID diagnosis anchor [@goodmanBacon2021; @callawaySantAnna2021; @sunAbraham2021; @borusyakJaravelSpiess2024]. Students work with a staggered synthetic panel where treatment effects vary across cohorts and event time. They compare naive TWFE to group-time ATT and imputation-style estimates, then explain which comparisons are valid.

**Transfer anchor.** Synthetic control is the transfer extension [@abadieDiamondHainmueller2010]. Students move to a single treated city and donor pool, choose donor weights from pre-treatment paths, inspect pre-fit, estimate post-treatment gaps, and use donor placebo comparisons to discipline interpretation.

**Reproduce.** Students compute the 2x2 DID estimate for the Card-Krueger-style teaching data, run the equivalent fixed-effects regression, and write the interpretation sentence in ATT language.

**Diagnose.** Students estimate a naive staggered TWFE coefficient, construct group-time ATT estimates using not-yet-treated controls, estimate an imputation-style ATT from untreated observations, and compare inference with and without clustering. The required memo identifies forbidden comparisons, event-time support, and the clustering level.

**Transfer.** Students implement a small synthetic-control exercise for one treated city. They report donor weights, pre-treatment root mean squared prediction error, post-treatment gaps, and placebo gaps for donor units.

The central lab question is not "which estimator gives the largest effect?" It is "which comparison would a skeptical applied reader accept as the missing untreated path?"

## Methods Box

:::{admonition} Methods Box: Practical Design Rules For DID, Event Studies, And Synthetic Control
:class: note

```{include} assets/tables/03-modern-did-diagnostics.md
```

```{include} assets/tables/03-modern-did-estimator-choice-guide.md
```

```{include} assets/tables/03-variance-clustering-and-inference-guide.md
```

The design problem comes first. Estimator choice follows from treatment timing, treatment-effect heterogeneity, comparison-group quality, donor-pool support, and the inference environment.
:::

## Reading Ladder And References

```{include} assets/tables/03-reading-architecture.md
```

**Foundations.** Start with Card and Krueger for the classical DID design [@cardKrueger1994]. Add Bertrand, Duflo, and Mullainathan immediately because inference is not optional in DID [@bertrandDufloMullainathan2004].

**Modern staggered DID.** Read Goodman-Bacon first to understand what TWFE is doing [@goodmanBacon2021]. Then read Callaway and Sant'Anna for group-time ATT estimation, Sun and Abraham for dynamic event-study correction, and Borusyak, Jaravel, and Spiess for imputation-based DID [@callawaySantAnna2021; @sunAbraham2021; @borusyakJaravelSpiess2024].

**Synthetic control.** Read Abadie, Diamond, and Hainmueller as the main donor-construction anchor [@abadieDiamondHainmueller2010]. Abadie and Gardeazabal are also useful for seeing synthetic control in a comparative case-study setting [@abadieGardeazabal2003].

**Interpretation and caution.** Roth is the pre-trend caution [@roth2022]. Roth, Sant'Anna, Bilinski, and Poe provide a broader synthesis of modern DID practice [@rothSantAnnaBilinskiPoe2023]. de Chaisemartin and D'Haultfoeuille and Athey and Imbens are useful for additional design-based perspectives on staggered adoption [@dechaisemartinDhaulfouille2020; @atheyImbens2022].

## Exercises And Discussion Prompts

1. Starting from {eq}`eq:em3-did-2x2`, explain in words what the second difference is replacing.
2. State parallel trends using {eq}`eq:em3-parallel-trends`. What does the restriction allow treated and comparison groups to differ in? What does it rule out?
3. In a Card-Krueger-style design, what does the DID identify? Name two objects it does not identify.
4. Write the TWFE event-study specification in {eq}`eq:em3-twfe-event-study` in words. Which event time is omitted, and why does that matter?
5. Why can already-treated units be bad controls in staggered adoption? Give a concrete labor-market example.
6. What does the Goodman-Bacon decomposition teach a researcher before choosing the final estimator?
7. Compare Callaway-Sant'Anna, Sun-Abraham, and Borusyak-Jaravel-Spiess. For each, name the setting where it is most useful.
8. Explain the imputation logic in {eq}`eq:em3-bjs-imputation-att`. What must be credible about {math}`\widehat{Y}_{it}(0)`?
9. In a synthetic-control design, why is pre-treatment fit part of the identification argument rather than only a model-fit statistic?
10. Using {eq}`eq:em3-cluster-robust-variance`, explain why many individuals observed inside a few treated states do not create many independent policy shocks.
11. Suppose a DID estimate has a tiny standard error but the comparison group has a visibly different pre-treatment trend. How should the paper's interpretation change?
12. Design a publishable panel-comparison project in labor, public, urban, development, education, or firms. State the treated units, comparison units, timing, estimand, main threat, clustering level, and preferred estimator.

## Reproducibility And Code Lab Note

The Lecture 3 code lab lives at `labs/03-did-event-studies-and-synthetic-control/`. It is a bounded synthetic teaching path with three parts:

- a Card-Krueger-style 2x2 DID reproduction exercise;
- a staggered-adoption diagnosis exercise comparing naive TWFE, group-time ATT, and imputation-style estimates;
- a synthetic-control transfer exercise with donor weights, pre-fit, post-treatment gaps, and placebo comparisons.

The lab is intentionally synthetic because the course does not bundle full original replication data. The goal is to make the design decisions executable: students can see how changing the comparison set, estimator, and clustering level changes the interpretation.

## Slide Companion Note

The Lecture 3 slide deck lives at `slides/week3/03-did-event-studies-and-synthetic-control.tex`. The deck mirrors the chapter without duplicating it: it defines the 2x2 DID estimand and parallel trends, introduces event-study dynamics, explains staggered TWFE failures, compares modern DID estimators, makes clustering and serial correlation visible, connects synthetic control to the panel toolkit, and closes with the Research Lab design.

## Bridge Forward

Lecture 3 teaches students to recover counterfactual trends from panel comparisons. Lecture 4 switches from trend-based identification to external variation through instruments. The core discipline stays the same: define the estimand, justify the comparison, and be explicit about what the design can and cannot identify.
