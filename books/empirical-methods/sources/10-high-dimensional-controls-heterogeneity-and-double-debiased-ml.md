---
title: High-Dimensional Controls, Heterogeneity, and Double/Debiased ML
bibliography:
  - references.bib
---

# High-Dimensional Controls, Heterogeneity, and Double/Debiased ML

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when high-dimensional controls create a genuine estimation problem rather than just a larger regression;
2. distinguish post-double selection from orthogonal-score / double machine learning approaches;
3. derive the partially linear model and the residual-on-residual logic behind DML;
4. explain why sample splitting and cross-fitting matter for valid inference;
5. interpret conditional average treatment effects and understand what causal forests are estimating;
6. diagnose practical implementation issues such as overlap, learner choice, hyperparameter tuning, instability, and uncertainty;
7. decide when these tools sharpen an applied economics design and when they are being used as a substitute for design.

## Opening Orientation

This lecture closes the first machine-learning methods block by moving from prediction toward causal estimation with many controls and rich heterogeneity. The main object is not predictive accuracy by itself. It is valid estimation of a target parameter when the researcher wants to use many covariates, flexible nuisance functions, or rich treatment-effect heterogeneity without letting overfitting contaminate the causal parameter. The central question is therefore design-oriented: when do high-dimensional controls, orthogonalization, and causal forests help applied economists answer a better-defined causal question, and when do they merely produce a more complicated regression [@belloniInferenceTreatmentEffects2014; @chernozhukovDoubleDebiasedMachine2018].

## Core points

```{admonition} Core points
:class: important

- High-dimensional methods are useful when the controls or nuisance objects are too rich for hand-picked low-dimensional regression, but they do not replace identification.
- Post-double selection and double/debiased ML solve different problems: one is about disciplined control selection; the other is about orthogonalizing a target parameter away from nuisance estimation error.
- Sample splitting and cross-fitting are central because they separate nuisance learning from target-parameter estimation.
- Heterogeneity methods such as causal forests are most useful when treatment-effect variation is substantively meaningful, the support is adequate, and the researcher is explicit about whether the goal is discovery, targeting, or welfare analysis.
- Flexible methods can reduce omitted-variable bias and improve measurement, but they can also fail through weak overlap, unstable tuning, leakage, and overinterpretation of noisy heterogeneity.
```

## Bridge

Lecture 9 treated machine learning as a toolkit for prediction and measurement. Lecture 10 keeps the same concern for implementation but turns it toward causal work: how do we use flexible nuisance estimation without turning the nuisance prediction problem into the answer? The lecture therefore sits between the design-based block and the measurement lecture. It asks how modern tools can exploit high-dimensional information while still honoring the logic of identification [@chernozhukovDoubleDebiasedMachine2018; @wagerEstimationInferenceHeterogeneous2018].

## Field Core

### 1. Why high-dimensional controls are a causal problem

Many applied datasets contain a large set of potentially relevant covariates: worker histories, firm characteristics, geographic exposures, text-derived variables, lagged outcomes, and flexible interactions. A researcher could try to put all of them into a regression, but that strategy fails when dimensionality is high relative to sample size or when naive model selection creates invalid post-selection inference.

The two main questions are:

1. how to use many controls to reduce confounding; and
2. how to estimate the target causal parameter without making inference hostage to overfit nuisance functions.

This is why high-dimensional causal estimation differs from generic prediction. The target is not the best-fitting outcome model; it is the treatment parameter or treatment-effect function.

### 2. Post-double selection and the logic of disciplined controls

A canonical partially linear setup is:

```{math}
:label: eq:plm
Y_i = \theta_0 D_i + g_0(X_i) + U_i, \qquad \mathbb{E}[U_i \mid D_i, X_i] = 0.
```

Here \(Y_i\) is the outcome, \(D_i\) the treatment, and \(X_i\) a high-dimensional control vector. The problem is that neither the outcome nuisance \(g_0(X_i)\) nor the treatment nuisance may be low-dimensional.

Post-double selection begins from the observation that good control selection should look at both the outcome equation and the treatment equation. The idea is to use lasso-style selection in both places and then estimate the target parameter on the union of selected controls [@belloniInferenceTreatmentEffects2014].

Conceptually, it helps because a covariate can matter for treatment assignment even if it is a weak predictor of the outcome, and vice versa. This is an applied-economics point, not just a variable-selection point.

### 3. Orthogonalization and double/debiased ML

Double machine learning starts from the same partially linear environment but solves a different problem: how to estimate the treatment parameter in a way that is locally insensitive to errors in the nuisance functions.

Let

```{math}
:label: eq:nuisance
m_0(X_i) = \mathbb{E}[D_i \mid X_i], \qquad g_0(X_i) = \mathbb{E}[Y_i \mid X_i].
```

Then define residualized treatment and outcome:

```{math}
:label: eq:residualized
\tilde D_i = D_i - m_0(X_i), \qquad \tilde Y_i = Y_i - g_0(X_i).
```

The orthogonal score for the partially linear model can be written as:

```{math}
:label: eq:orthogonal-score
\psi(W_i; \theta, \eta) = \left(D_i - m(X_i)\right)\left(Y_i - g(X_i) - \theta\left(D_i - m(X_i)\right)\right),
```

where \(\eta = (g,m)\) collects the nuisance functions. Orthogonality means that small estimation errors in \(g\) and \(m\) have only second-order effects on the target score at the truth. That is the core mathematical reason DML works [@chernozhukovDoubleDebiasedMachine2018].

The DML estimator can then be viewed as a residual-on-residual regression:

```{math}
:label: eq:dml
\hat\theta_{DML} = \left(\frac{1}{n}\sum_i \hat{\tilde D}_i^2\right)^{-1} \left(\frac{1}{n}\sum_i \hat{\tilde D}_i \hat{\tilde Y}_i\right).
```

### 4. Sample splitting and cross-fitting

Why not just estimate the nuisance functions and plug them in on the same data? Because overfitting the nuisance step can contaminate the target step.

Sample splitting solves this by estimating nuisance functions on one fold and evaluating the orthogonal score on another. Cross-fitting improves efficiency by rotating that logic across folds and averaging the resulting score contributions.

In practice, the researcher should explain:
- how the folds were defined,
- whether tuning was nested inside each training fold,
- which learner was used for the nuisance functions,
- and whether results are stable across reasonable learner choices.

### 5. Heterogeneity and conditional average treatment effects

Once the target is no longer a single scalar parameter, the researcher may want to estimate a conditional average treatment effect:

```{math}
:label: eq:cate
\tau(x) = \mathbb{E}[Y_i(1) - Y_i(0) \mid X_i = x].
```

CATEs are not automatically interesting. They are useful when heterogeneity corresponds to real economics questions: targeting, welfare incidence, distributional consequences, or mechanism testing.

The key practical warning is that estimating \(\tau(x)\) is much more demanding than estimating an average treatment effect. Support, overlap, and the noise level of heterogeneity matter enormously. A spiky or unstable forest is often telling you more about data sparsity than about meaningful treatment-effect variation.

### 6. Causal forests and generalized random forests

Causal forests adapt random-forest logic to treatment-effect estimation. The broad idea is to recursively partition the covariate space in ways that are informative about heterogeneity in treatment effects, then average over trees while using sample-splitting/honesty rules to limit adaptive overfitting [@wagerEstimationInferenceHeterogeneous2018; @atheyGeneralizedRandomForests2019].

The appeal for economists is not that forests reveal “the truth.” It is that they offer a disciplined way to:
- discover potentially important heterogeneity,
- construct policy scores for targeting,
- and evaluate whether heterogeneity is stable enough to matter.

But the caveats are first-order:
- forests do not rescue bad overlap,
- variable importance is not causal importance,
- tuning strongly affects results,
- and subgroup discovery can become noisy p-hacking if not linked to a clear question.

### 7. Practical implementation rules

For applied work, the most important implementation questions are:

- **What is the target parameter?** ATE, ATT, CATE, policy score, or welfare-weighted effect?
- **How strong is overlap?** Flexible methods do badly in thin support regions.
- **What are the nuisance learners?** Lasso, random forests, boosted trees, neural nets, or ensembles each imply different bias/variance tradeoffs.
- **How was tuning done?** Hyperparameters chosen on the full sample can quietly undo the logic of sample splitting.
- **Are results stable?** Check sensitivity across learners, seeds, folds, and subsamples.
- **What uncertainty is reported?** Standard errors for average effects are not the same as uncertainty about heterogeneous effects or policy rules.

A useful discipline is to report one baseline low-dimensional model, one high-dimensional / orthogonalized estimate, and one heterogeneity exercise, then explain exactly what each adds.

### 8. What these methods do not solve

These tools do not solve the identification problem. If treatment assignment is fundamentally confounded by unobservables, orthogonalization does not change that. If the support is bad, forests cannot manufacture overlap. If the downstream outcome is normatively irrelevant, a beautifully tuned CATE surface still has little value.

The right interpretation is that DML and causal forests improve the use of rich observables once the research design already has a credible identification logic or a clearly stated descriptive/predictive target.

## Research Lab

### Primary anchor paper

A useful primary anchor is [@dubeMonopsonyOnlineLabor2020], which uses double machine learning in a large online labor-market setting. The paper is helpful because it shows DML in a real economic application where flexible nuisance estimation sharpens a causal object without becoming the object itself.

### Reproduce

Reproduce a bounded version of the residualization logic:
- choose a treatment, outcome, and high-dimensional control set;
- estimate nuisance functions using a simple learner;
- cross-fit residuals;
- estimate the residual-on-residual treatment parameter.

### Diagnose

Diagnose the design:
- what is the underlying identifying assumption once rich observables are included?
- how strong is overlap?
- how sensitive are results to the nuisance learner?
- does the treatment parameter remain interpretable after flexible adjustment?

### Transfer

Transfer the design to a heterogeneity setting using [@davisUsingCausalForests2017] or another causal-forest application:
- define the treatment effect heterogeneity object;
- assess whether heterogeneity is substantively meaningful;
- compare a simple interaction design to a forest-based heterogeneity estimate.

The goal is to learn when these tools improve an applied design and when they merely create a more complicated black box.

## Methods Box

### Practical rules for applied economists

1. Start with the causal question, not the learner.
2. Write down the target parameter before training nuisance functions.
3. Check overlap before celebrating flexible adjustment.
4. Use sample splitting and cross-fitting honestly.
5. Report learner choice and tuning choices transparently.
6. Compare results to simpler baseline models.
7. Treat CATEs as economically meaningful only when the heterogeneity question matters substantively.
8. Do not interpret variable importance as a causal mechanism.
9. Be explicit about which parts of the procedure are exploratory versus confirmatory.

### Common software workflows

Useful practical stacks include:
- `DoubleML` for orthogonal-score / DML workflows,
- `econml` for heterogeneous-treatment and policy-learning workflows,
- `grf` for causal forests and generalized random forests,
- baseline lasso / elastic-net workflows via `glmnet` or `sklearn`-style implementations.

The lecture should mention these tools only as implementations of econometric ideas, not as substitutes for understanding the assumptions.

## Reading Ladder And References

### Core methodological readings

- [@belloniInferenceTreatmentEffects2014]
- [@chernozhukovDoubleDebiasedMachine2018]
- [@wagerEstimationInferenceHeterogeneous2018]
- [@atheyGeneralizedRandomForests2019]

### Applied economics readings

- [@davisUsingCausalForests2017]
- [@dubeMonopsonyOnlineLabor2020]

## Exercises And Discussion Prompts

1. Why is orthogonality the key mathematical idea behind DML rather than just “using ML first”? 
2. When would post-double selection be preferable to a more general DML implementation? 
3. Give one applied setting where a CATE is substantively meaningful and one where it is likely to be noise. 
4. Why does cross-fitting help, and what can still go wrong even with cross-fitting? 
5. Suppose a causal forest finds strong heterogeneity in a thin-support region. How should an applied economist respond? 

## Reproducibility And Code Lab Note

The bounded teaching lab should demonstrate:
- residualization of outcome and treatment with a high-dimensional control set,
- cross-fitting,
- comparison of a baseline model to a DML estimate,
- and, optionally, a simple causal-forest heterogeneity exercise.

## Slide Companion Note

The lecture deck should include one slide each on:
- why high-dimensional controls create a causal problem,
- post-double selection,
- orthogonalization and DML math,
- cross-fitting,
- causal forests and CATEs,
- implementation pitfalls,
- and the Research Lab workflow.

## Bridge Forward

Lecture 11 turns from high-dimensional causal estimation toward text, computation, and LLM-based methods. The key continuity is that both lectures ask how flexible tools can sharpen applied research without replacing design logic.
