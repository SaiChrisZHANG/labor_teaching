# Lecture 10. High-Dimensional Controls, Heterogeneity, And Double/Debiased ML

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain why high-dimensional controls create inference problems beyond ordinary regression;
2. distinguish post-double selection, orthogonal-score DML, and causal-forest heterogeneity workflows;
3. write the partially linear model and the outcome and treatment nuisance functions;
4. derive the residual-on-residual logic behind double/debiased ML;
5. explain how sample splitting and cross-fitting protect inference from overfit nuisance estimates;
6. define conditional average treatment effects and interpret causal-forest or generalized-random-forest outputs;
7. diagnose overlap, feature leakage, learner choice, tuning, fold instability, and uncertainty for heterogeneous effects;
8. decide when these tools sharpen an economics research design and when they are being used as a substitute for one.

## Opening Orientation

Lecture 10 moves from prediction as measurement to flexible methods inside causal research designs. The central question is: **how can applied economists use many controls, flexible nuisance functions, and treatment-effect heterogeneity without confusing prediction accuracy with causal identification?** This is not a generic machine-learning lecture. The target is credible estimation of treatment effects or treatment-effect functions when the data contain rich worker histories, firm characteristics, geography, text-derived variables, lagged outcomes, or many possible interactions.

The key discipline is to separate three objects. The causal parameter is the object of interest. The nuisance functions help adjust for confounding or improve precision. The prediction algorithm is only a tool for estimating those nuisance functions. Double/debiased machine learning is useful precisely because it treats nuisance prediction as auxiliary rather than as the research answer [@chernozhukovDoubleDebiasedMachine2018].

The paper spine is methodological and applied. Belloni, Chernozhukov, and Hansen show how high-dimensional control selection can support inference on treatment effects when selection is disciplined rather than ad hoc [@belloniInferenceTreatmentEffects2014]. Chernozhukov and coauthors provide the double/debiased machine learning framework for treatment and structural parameters [@chernozhukovDoubleDebiasedMachine2018]. Wager and Athey, and Athey, Tibshirani, and Wager, develop causal forests and generalized random forests for heterogeneous effects and local moment problems [@wagerEstimationInferenceHeterogeneous2018; @atheyGeneralizedRandomForests2019]. Davis and Heller show how causal forests can be used to study heterogeneity in an economics application, while Dube and coauthors show double machine learning in an online labor-market setting [@davisUsingCausalForests2017; @dubeMonopsonyOnlineLabor2020].

## Core Points

:::{admonition} Core points
:class: important

- High-dimensional methods help use rich observables, but they do not identify causal effects by themselves.
- Post-double selection is a disciplined control-selection method: select controls from both the outcome equation and the treatment equation, then estimate the target on their union.
- Double/debiased ML is an orthogonal-score method: estimate nuisance functions flexibly, residualize outcome and treatment, and estimate the target parameter with a score that is locally insensitive to nuisance error.
- Sample splitting and cross-fitting matter because the observations used to learn nuisance functions should not be the same observations used to evaluate the target score.
- CATEs and causal forests are useful only when treatment-effect heterogeneity is substantively meaningful, support is adequate, and uncertainty is reported honestly.
- Prediction accuracy is not causal validity. Overlap, timing, leakage, identifying assumptions, and reporting discipline do the causal work.
:::

## Bridge

Lecture 9 asked when prediction is a final object and when it is an input into measurement. Lecture 10 asks when prediction is a **nuisance input** for causal estimation. The bridge is subtle but important. A model can predict outcomes very well while producing a biased treatment estimate if it uses post-treatment features, violates sample-splitting discipline, or adjusts in regions with weak overlap. Conversely, a nuisance model with only moderate predictive accuracy can still be useful if the resulting orthogonal score estimates the target parameter stably.

The applied-economics framing is therefore: first define the research design and target parameter, then decide whether high-dimensional controls, double/debiased ML, or causal forests help execute that design.

```{include} assets/tables/10-theory-to-applied-bridge.md
```

## Field Core

### A. Why High-Dimensional Controls Create A Causal Problem

Many empirical projects now contain more plausible controls than a researcher can justify by hand: pre-treatment earnings histories, firm fixed effects, vacancy text, location histories, lagged outcomes, interactions, and sector-by-place-by-time measures. The problem is not only computational. It is inferential.

If the researcher searches over controls and then reports ordinary regression standard errors as if the model had been fixed in advance, inference can be badly misleading. If the researcher includes everything, high dimensionality can create weak signal, collinearity, overfitting, and unstable estimates. If the researcher hand-picks controls after seeing results, the design becomes difficult to defend.

The target remains a causal estimand. For a binary treatment, a baseline average treatment effect is:

```{math}
:label: eq:em10-ate
\theta_0
=
\mathbb E\left[Y_i(1)-Y_i(0)\right].
```

High-dimensional controls help only under a design assumption such as conditional independence:

```{math}
:label: eq:em10-unconfoundedness
\left(Y_i(1),Y_i(0)\right) \perp D_i \mid X_i,
\qquad
0 < \Pr(D_i=1\mid X_i) < 1.
```

The first condition says the relevant confounders are observed in {math}`X_i`. The second says overlap is strong enough to compare treated and untreated units at similar covariate values. No machine-learning method removes the need to defend those conditions.

### B. Post-Double Selection And The Role Of Lasso

The canonical partially linear model is:

```{math}
:label: eq:em10-plm
Y_i
=
\theta_0 D_i
+
g_0(X_i)
+
U_i,
\qquad
\mathbb E[U_i\mid D_i,X_i]=0.
```

The treatment equation is:

```{math}
:label: eq:em10-treatment-equation
D_i
=
m_0(X_i)
+
V_i,
\qquad
\mathbb E[V_i\mid X_i]=0.
```

Post-double selection uses lasso or a related sparse selector twice:

```{math}
:label: eq:em10-pds-selected-sets
\widehat S_Y
=
\operatorname{supp}\left(\widehat\gamma_Y\right),
\qquad
\widehat S_D
=
\operatorname{supp}\left(\widehat\gamma_D\right),
\qquad
\widehat S
=
\widehat S_Y \cup \widehat S_D.
```

Then the researcher estimates {math}`\theta_0` by ordinary least squares of {math}`Y_i` on {math}`D_i` and the controls in {math}`\widehat S`. The point of the union is economic: a covariate may be important because it predicts treatment assignment, because it predicts the outcome, or because it does both. Selecting only from the outcome equation can omit confounders that are weak outcome predictors but strong treatment predictors [@belloniInferenceTreatmentEffects2014].

Post-double selection is best used when the target is low-dimensional, the control set is large but approximate sparsity is plausible, and the researcher wants a transparent selected-control regression. It identifies the treatment effect under the same selection-on-observables logic as the partially linear model. It does not identify effects when confounding is unobserved, when important nonlinearities are missed, or when overlap is weak. The selected controls should be reported as an estimation device, not as a structural list of mechanisms.

### C. Orthogonalization And Double/Debiased ML

Double/debiased ML starts from a related model but focuses on a different problem: how to estimate the target parameter when the nuisance functions are learned flexibly and may be imperfect.

Define the outcome and treatment nuisance functions:

```{math}
:label: eq:em10-nuisance-functions
g_0(X_i)=\mathbb E[Y_i\mid X_i],
\qquad
m_0(X_i)=\mathbb E[D_i\mid X_i].
```

Residualize outcome and treatment:

```{math}
:label: eq:em10-residuals
\widetilde Y_i
=
Y_i-g_0(X_i),
\qquad
\widetilde D_i
=
D_i-m_0(X_i).
```

If the nuisance functions were known, the residual-on-residual estimand would be:

```{math}
:label: eq:em10-residual-on-residual-population
\theta_0
=
\frac{\mathbb E[\widetilde D_i\widetilde Y_i]}
{\mathbb E[\widetilde D_i^2]}.
```

In practice, {math}`g_0` and {math}`m_0` are estimated. The orthogonal score for the partially linear model is:

```{math}
:label: eq:em10-orthogonal-score
\psi(W_i;\theta,\eta)
=
\left(D_i-m(X_i)\right)
\left[
Y_i-g(X_i)-\theta\left(D_i-m(X_i)\right)
\right],
\qquad
\eta=(g,m).
```

The estimator solves:

```{math}
:label: eq:em10-score-condition
\frac{1}{n}\sum_{i=1}^{n}
\psi(W_i;\widehat\theta,\widehat\eta)
=0.
```

Equivalently, after cross-fitted residualization:

```{math}
:label: eq:em10-dml-estimator
\widehat\theta_{DML}
=
\left(\frac{1}{n}\sum_{i=1}^{n}\widehat{\widetilde D}_i^2\right)^{-1}
\left(\frac{1}{n}\sum_{i=1}^{n}\widehat{\widetilde D}_i\widehat{\widetilde Y}_i\right).
```

Orthogonality means that small first-stage nuisance errors have only second-order effects on the score for {math}`\theta_0` at the truth. Informally, mistakes in {math}`\widehat g` and {math}`\widehat m` enter as products rather than as first-order bias terms. This is why the nuisance functions can be learned with lasso, random forests, boosted trees, neural nets, or ensembles without requiring those learners to be the causal object [@chernozhukovDoubleDebiasedMachine2018].

The interpretation is narrow and powerful. DML estimates a low-dimensional treatment or structural parameter under an orthogonal moment condition, credible identification assumptions, and adequate nuisance rates. It does not prove that treatment is as good as random conditional on {math}`X_i`. It does not repair bad timing, post-treatment controls, or poor support.

### D. Sample Splitting And Cross-Fitting

Sample splitting prevents the same observation from both training the nuisance model and evaluating the target score. Partition the sample into folds {math}`I_1,\ldots,I_K`. For each fold {math}`k`, estimate nuisance functions on the complement {math}`I_k^c`, then predict residuals only for observations in {math}`I_k`:

```{math}
:label: eq:em10-cross-fitting
\widehat{\widetilde Y}_i
=
Y_i-\widehat g^{(-k)}(X_i),
\qquad
\widehat{\widetilde D}_i
=
D_i-\widehat m^{(-k)}(X_i),
\qquad
i\in I_k.
```

Cross-fitting rotates this procedure across all folds and stacks the held-out residuals. The final score condition uses every observation, but each observation is evaluated with nuisance functions trained elsewhere.

A credible implementation reports:

- the number of folds and the fold construction;
- whether folds were clustered when treatment or shocks are clustered;
- whether tuning was nested inside each training fold;
- which nuisance learners were used for {math}`g` and {math}`m`;
- sensitivity to learner class, seeds, folds, and sample restrictions.

Cross-fitting is not cosmetic. If tuning or feature selection uses the full sample before splitting, the procedure can leak information from the score sample into the nuisance learner and weaken the inferential argument.

### E. What DML Identifies, And What It Does Not

For high-dimensional controls and double/debiased ML, the researcher should be able to fill in the following design statement before running code:

```text
Target parameter:
Identifying variation:
Observed confounders:
Timing of controls:
Overlap population:
Nuisance learners:
Cross-fitting plan:
Robustness checks:
```

DML is best used when the target parameter is low-dimensional, the identification story is already credible, and nuisance functions are too rich for a hand-specified linear model. It identifies the target implied by the moment condition, such as an ATE in a partially linear model or another structural parameter with an orthogonal score. It does not identify causal effects from purely predictive variation, unobserved confounding, support extrapolation, or mechanically selected post-treatment controls.

The most common abuse is to report a DML estimate as if the algorithm itself supplied the research design. A better report says: the design relies on conditional comparison given pre-treatment observables; DML is used to estimate the nuisance adjustment flexibly; overlap and sensitivity checks indicate the estimate is or is not stable.

### F. CATEs And Substantively Meaningful Heterogeneity

A conditional average treatment effect is:

```{math}
:label: eq:em10-cate
\tau(x)
=
\mathbb E\left[Y_i(1)-Y_i(0)\mid X_i=x\right].
```

Sometimes the conditioning variable is a lower-dimensional policy feature {math}`Z_i=h(X_i)`, such as baseline earnings, prior employment, market thickness, or youth risk score:

```{math}
:label: eq:em10-cate-z
\tau(z)
=
\mathbb E\left[Y_i(1)-Y_i(0)\mid Z_i=z\right].
```

CATEs are useful when heterogeneity answers an economic question: who benefits from a job-training program, which workers are harmed by a policy, where monopsony power is stronger, or whether an intervention works through a mechanism predicted by theory. They are less useful when the researcher merely asks a flexible algorithm to find any subgroup with large effects.

The support burden is higher than for an ATE. Estimating {math}`\tau(x)` requires treated and untreated observations with comparable covariates near {math}`x`. A highly variable CATE surface may reflect sparse support, weak treatment variation, or adaptive overfitting rather than meaningful heterogeneity.

### G. Causal Forests And Generalized Random Forests

Causal forests adapt random-forest logic to treatment-effect estimation. Instead of splitting only to predict {math}`Y_i`, the forest searches for covariate partitions that reveal differences in treatment effects. Honest forests separate the data used to choose splits from the data used to estimate effects within leaves, which reduces adaptive overfitting [@wagerEstimationInferenceHeterogeneous2018].

A useful way to view the heterogeneity object is a local residual-on-residual problem. With forest weights {math}`\alpha_i(x)` centered around target covariate value {math}`x`, a causal-forest style estimator solves:

```{math}
:label: eq:em10-causal-forest-object
\widehat\tau(x)
=
\arg\min_{\tau}
\sum_{i=1}^{n}
\alpha_i(x)
\left[
\left(Y_i-\widehat\mu(X_i)\right)
-
\tau\left(D_i-\widehat e(X_i)\right)
\right]^2,
```

where {math}`\widehat\mu(X_i)` is an outcome nuisance estimate and {math}`\widehat e(X_i)` is a propensity-score or treatment nuisance estimate. Generalized random forests extend the same idea to local moment conditions rather than only treatment effects [@atheyGeneralizedRandomForests2019].

Causal forests are best used for disciplined heterogeneity discovery, targeting diagnostics, and comparison with simpler interaction models. They identify treatment-effect heterogeneity under the same causal assumptions as the underlying design, plus stronger support and regularity demands for local estimation. They do not make variable importance causal, they do not prove mechanisms, and they do not create overlap.

In applied papers, forest output should be interpreted as evidence about patterns of heterogeneity, not as a ranked list of causes. A variable can be important for splitting because it marks support, precision, or correlated economic environments. Mechanism claims still need theory, timing, and additional evidence.

### H. Implementation Caveats That Matter In Practice

```{include} assets/tables/10-high-dimensional-controls-heterogeneity-and-ddml-diagnostics.md
```

Several implementation issues deserve explicit reporting.

**Overlap support.** Flexible adjustment is dangerous in thin support. Report the propensity-score distribution, trimming rules, effective sample, and whether estimates are driven by regions where one treatment state is rare.

**Feature leakage.** All controls and features must be pre-treatment. In labor-market data, leakage can enter through post-hire outcomes, post-policy firm behavior, edited platform metadata, or text created after treatment assignment.

**Nuisance-learner choice.** Lasso is attractive when approximate sparsity is plausible. Forests and boosted trees are attractive for nonlinearities and interactions. Ensembles can improve nuisance fit but make transparency harder. The learner choice should match the nuisance problem, not the desire for an impressive method label.

**Hyperparameter tuning.** Tuning should occur inside the training fold. Tuning on the full sample can quietly undo sample-splitting discipline.

**Fold instability.** Estimates that move sharply across fold assignments, seeds, or learner classes should be reported as fragile. Instability can be a sign of weak support, weak signal, or overly flexible learners.

**Uncertainty for heterogeneous effects.** Average-effect standard errors are not enough for CATE claims. Researchers should report uncertainty for subgroup effects, honest forest intervals when available, and whether discovered heterogeneity survives hold-out or pre-specified validation.

**Honest forests versus adaptive overfitting.** Forests that use the same observations to choose splits, estimate leaf effects, and select highlighted subgroups can overfit heterogeneity. Honesty and held-out validation are not technical niceties; they are part of the design.

### I. Reporting Discipline

A strong applied paper using these tools usually reports four layers:

1. a simple design-based or low-dimensional benchmark;
2. the high-dimensional or DML estimate and the exact target parameter;
3. overlap, leakage, tuning, and fold-stability diagnostics;
4. a heterogeneity analysis that is labeled exploratory or confirmatory.

The result should be readable without knowing the software package. `DoubleML`, `EconML`, and `grf` are useful implementation stacks, but the paper should explain the estimand, score, nuisance functions, cross-fitting plan, and interpretation in economics language.

## Research Lab

The Week 10 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. The primary anchor is Dube and coauthors because their online labor-market application uses double machine learning to estimate a causal labor-market parameter while adjusting flexibly for rich observables [@dubeMonopsonyOnlineLabor2020]. The challenge anchor is Davis and Heller because their causal-forest application pushes students to decide when discovered heterogeneity is substantively meaningful and when it is only noisy subgroup variation [@davisUsingCausalForests2017].

### Reproduce

Students work with a deterministic synthetic online labor-market dataset. They estimate a wage-setting treatment effect using:

- a baseline low-dimensional regression;
- a naive high-dimensional regression;
- cross-fitted residual-on-residual DML with ridge nuisance learners;
- a post-double-selection variant using lasso-style control selection.

The goal is to reproduce the **design logic** of DML:

- define outcome, treatment, and pre-treatment controls;
- estimate outcome and treatment nuisance functions on training folds;
- residualize on held-out folds;
- estimate the treatment parameter on residuals;
- compare the estimate with simpler benchmarks.

### Diagnose

Students inspect whether the DML result is credible:

- overlap of treated and untreated observations after nuisance prediction;
- sensitivity across folds and learners;
- leakage audit for post-treatment platform features;
- stability of selected controls in post-double selection;
- whether the treatment parameter remains interpretable after flexible adjustment.

The required memo should say whether DML sharpens a credible design or merely hides design uncertainty behind a modern estimator.

### Transfer

Students transfer the logic to treatment-effect heterogeneity inspired by causal-forest applications. The transfer dataset represents a youth employment program with baseline risk, neighborhood conditions, prior work, and treatment assignment. Students estimate:

- subgroup CATEs by baseline risk;
- a simple interaction benchmark;
- a lightweight honest-tree heterogeneity exercise;
- hold-out diagnostics for whether the discovered heterogeneity is stable.

The point is not to produce a frontier forest implementation. The point is to learn what a publishable heterogeneity claim would need: overlap, pre-specified economic dimensions, uncertainty, and validation against simpler alternatives.

Minimum student deliverables are:

1. one Reproduce paragraph defining the target parameter, nuisance functions, and cross-fitting plan;
2. one Diagnose paragraph interpreting overlap, leakage, learner sensitivity, and fold stability;
3. one Transfer paragraph explaining whether heterogeneity is substantively meaningful;
4. one final sentence stating what the method identifies and what it does not identify.

## Methods Box

:::{admonition} High-dimensional causal estimation checklist
:class: note

1. **Name the estimand.** Is the target an ATE, ATT, structural parameter, CATE, policy score, or subgroup contrast?
2. **State the identifying assumption.** What comparison identifies the effect after conditioning on observables or using the design?
3. **Define the nuisance functions.** Which function predicts the outcome? Which function predicts treatment? Are they auxiliary to the parameter of interest?
4. **Protect timing.** Exclude post-treatment features, labels, platform edits, future outcomes, and constructed variables that encode treatment assignment.
5. **Check overlap before modeling.** Thin support is not solved by flexible learners.
6. **Use honest sample splitting.** Tune nuisance learners within training folds and evaluate scores on held-out folds.
7. **Compare to simple baselines.** A DML estimate should be interpretable relative to a low-dimensional design.
8. **Stress-test learners and folds.** Report whether estimates move across lasso, ridge, forests, seeds, folds, and trimming rules.
9. **Treat CATEs carefully.** Heterogeneity needs support, uncertainty, and an economic reason to matter.
10. **Separate discovery from confirmation.** A forest can generate hypotheses; a design and validation strategy make them credible.
:::

## Reading Ladder And References

```{include} assets/tables/10-reading-architecture.md
```

**First pass: high-dimensional controls.** Read Belloni, Chernozhukov, and Hansen on post-double selection and the logic of inference after selecting controls [@belloniInferenceTreatmentEffects2014].

**Second pass: orthogonal scores and DML.** Read Chernozhukov and coauthors for the partially linear model, Neyman orthogonality, sample splitting, cross-fitting, and the broader treatment/structural-parameter framework [@chernozhukovDoubleDebiasedMachine2018].

**Third pass: heterogeneity.** Read Wager and Athey for causal forests and Athey, Tibshirani, and Wager for generalized random forests [@wagerEstimationInferenceHeterogeneous2018; @atheyGeneralizedRandomForests2019]. Nie and Wager are useful for the R-learner view of heterogeneous treatment effects [@nieQuasiOracleEstimationHeterogeneous2021].

**Applied pass: economics research design.** Read Dube and coauthors for DML in an online labor-market application, then Davis and Heller for a causal-forest heterogeneity application [@dubeMonopsonyOnlineLabor2020; @davisUsingCausalForests2017].

## Exercises And Discussion Prompts

1. Write the partially linear model for an applied labor question with high-dimensional controls. Which variables are outcome nuisances, which are treatment nuisances, and which parameter is the target?
2. Explain why selecting controls only from the outcome equation can miss confounders. Give an example from worker, firm, or place data.
3. Derive the residual-on-residual DML estimator from the orthogonal score in {numref}`eq:em10-orthogonal-score`.
4. Draw a sample-splitting diagram for five-fold cross-fitting. Where should hyperparameter tuning occur?
5. A DML estimate changes sharply when random forests replace lasso in the nuisance step. What diagnostics would you inspect before interpreting the result?
6. Give one setting where a CATE is substantively meaningful and one setting where a discovered CATE is likely to be noise.
7. A causal forest reports that baseline earnings are the most important variable. Why is this not automatically a causal mechanism?
8. Suppose overlap is weak for workers in small rural labor markets. What should the paper report, and how might the estimand change after trimming?

## Reproducibility And Code Lab Note

The canonical Lecture 10 lab folder is:

```text
labs/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml/
```

The lab is a bounded teaching path. It creates deterministic synthetic data for an online labor-market DML exercise and a youth-employment heterogeneity transfer exercise. It does not claim to reproduce the published estimates in Dube and coauthors or Davis and Heller, and it does not invent official replication inputs.

The smoke path runs:

```bash
ENV_NAME=research bash smoke.sh
```

Expected outputs include baseline versus DML treatment-effect estimates, fold-level nuisance diagnostics, overlap summaries, leakage and selected-control audits, subgroup CATE tables, honest-tree heterogeneity summaries, and transfer design prompts.

## Slide Companion Note

The Week 10 slide deck should not duplicate the chapter. It should define why high-dimensional controls create a new inference problem, show post-double selection, isolate orthogonalization and DML math, explain cross-fitting, introduce CATEs and causal forests, summarize implementation pitfalls, and end with the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is `slides/week10/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.tex`.

## Bridge Forward

Lecture 11 turns from high-dimensional causal estimation to policy learning, targeting, and external validity. The continuity is direct: Lecture 10 teaches how to estimate average and conditional effects credibly; Lecture 11 asks how, and whether, those heterogeneous estimates should guide decisions under constraints, welfare objectives, and distribution shift.
