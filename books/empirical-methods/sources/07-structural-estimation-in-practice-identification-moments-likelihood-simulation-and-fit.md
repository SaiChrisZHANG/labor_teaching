---
title: Lecture 7. Structural Estimation in Practice: Identification, Moments, Likelihood, Simulation, and Fit
bibliography:
  - references.bib
---

# Lecture 7. Structural Estimation in Practice: Identification, Moments, Likelihood, Simulation, and Fit

## Learning Objectives

By the end of this lecture, students should be able to:

1. map a structural model's primitives to the observed variation that identifies them;
2. distinguish likelihood, method-of-moments, GMM, simulated method of moments, and indirect inference in practice;
3. explain how weighting choices, targeted moments, and goodness-of-fit shape substantive conclusions;
4. evaluate structural estimates using validation, sensitivity, and counterfactual discipline;
5. discuss how to estimate uncertainty in structural work using asymptotic formulas, the delta method, bootstrap methods, and related approaches.

## Opening Orientation

Lecture 6 asked when a research question requires structure at all. Lecture 7 asks the next question: **how do researchers take a structural model to data credibly?** The point of structural estimation is not simply to produce a vector of parameters. It is to build a disciplined mapping from data variation to latent primitives, and from primitives to counterfactuals and welfare objects. The key challenge is that this mapping is only persuasive when readers can see which variation identifies the model, why a particular estimation strategy was chosen, how well the model fits the empirical objects it claims to match, and how uncertainty is being reported [@newey1994large; @keane2010structural; @aguirregabiria2010dynamic].

```{admonition} Core points
:class: important
- Structural credibility comes from the chain **identification -> estimation -> fit -> counterfactual discipline -> inference**, not from solving a complicated model.
- Likelihood, moments, simulation, and indirect inference are different ways of disciplining the same underlying primitives with data.
- Weighting choices and targeted moments are substantive choices: they determine which data features the model is required to explain.
- Good structural practice requires transparent fit diagnostics, validation outside the estimation target, and honest reporting of sensitivity.
- Variance estimation is not optional. Delta-method formulas, information-matrix approximations, bootstrap methods, and simulation-aware inference all matter for interpretation.
```

## Bridge

Lecture 6 introduced static and dynamic decision problems and clarified when structure is worth the cost. This lecture moves from model *choice* to model *implementation*. The bridge is simple: once the researcher has specified what is observed, what is latent, and what counterfactual is of interest, the next task is to decide **which empirical objects will discipline the model** and **how uncertainty will be quantified**.

## Field Core

### 1. Identification in structural models

A structural model is identified only if some feature of the data moves the latent primitive of interest while holding the rest of the model coherent. A useful checklist is:

1. What is the primitive of interest?
2. What observable behavior depends on it?
3. What variation in data shifts that behavior?
4. Could another primitive generate the same movement?
5. Which assumptions break the observational equivalence?

This is the structural analogue of asking what comparison identifies a reduced-form estimate. The difference is that structural models often map one observable object into several latent components at once. For example, a job-search model may use unemployment duration, accepted wages, and offer arrival rates jointly to separate search costs, reservation behavior, and offer distributions. A lifecycle model may use labor supply, wage growth, and savings jointly to discipline risk, insurance, and labor-supply elasticity [@keane2010structural; @low2010wage].

### 2. Likelihood-based estimation

If the model implies a full density for the observed data, a natural approach is maximum likelihood:

```{math}
:label: eq:likelihood-lecture7
\hat{\theta} = \arg\max_{\theta} \sum_{i=1}^{N} \log f(y_i \mid x_i; \theta).
```

Likelihood is attractive when the model is strongly parametric, the data-generating process is specified in detail, and the researcher is willing to commit to the distributional structure. The gain is efficiency if the model is correctly specified; the cost is that misspecification can be consequential. In dynamic discrete-choice settings, likelihood often rides on recursive structure and latent shocks; in practice, computational burden can be substantial.

### 3. Moments, GMM, and simulation-based estimation

Many applied structural papers prefer to match moments rather than commit to a full likelihood. Let {math}`m^{data}` be empirical moments and {math}`m^{model}(\theta)` the model-implied analogues. Then

```{math}
:label: eq:gmm-criterion
\hat{\theta} = \arg\min_{\theta} \left[m^{data} - m^{model}(\theta)\right]' W \left[m^{data} - m^{model}(\theta)\right].
```

When the model is analytically intractable, moments may be simulated:

```{math}
:label: eq:smm-criterion
\hat{\theta} = \arg\min_{\theta} \left[m^{data} - \hat m^{sim}(\theta; R)\right]' W \left[m^{data} - \hat m^{sim}(\theta; R)\right],
```

where {math}`R` indexes simulation draws. This is the logic of simulated method of moments (SMM): choose parameters so the simulated model reproduces the empirical objects the researcher cares about [@pakes1989simulation].

The practical question is not “likelihood or moments?” in the abstract. It is:
- which observables are most informative for the primitive of interest,
- which moments are robust and interpretable,
- and how much structure the researcher is willing to impose on the full joint distribution?

### 4. Indirect inference intuition

Indirect inference is useful when a structural model is easy to simulate but hard to estimate directly. The researcher chooses an auxiliary model or set of summary statistics {math}`a(\cdot)`, estimates it on the real data, and then chooses structural parameters so the same auxiliary objects are reproduced in simulated data:

```{math}
:label: eq:indirect-inference
\hat{\theta} = \arg\min_{\theta} \left[a(y^{data}) - a(y^{sim}(\theta))\right]' W \left[a(y^{data}) - a(y^{sim}(\theta))\right].
```

This is conceptually useful because it separates the **behavioral model** from the **empirical summary objects** that the audience already knows how to read. But the choice of auxiliary statistics is substantive: if the auxiliary model ignores the core behavioral patterns, indirect inference can look computationally impressive while being substantively weak [@gourieroux1993indirect].

### 5. Weighting matrices, targeted moments, and overidentification

In GMM/SMM-style work, the weighting matrix {math}`W` determines which discrepancies the criterion penalizes most heavily. The “optimal” weighting matrix is asymptotically related to the inverse variance of the empirical moments, but a practically useful lecture point is that **targeting moments is a scientific choice, not just a numerical one**. If a model is estimated to match wages but not employment transitions, then readers should not trust it equally on both objects.

Overidentification can be a feature rather than a bug: extra moments let the researcher test whether the model can explain behavior it was not explicitly engineered to match. But the usual caveat applies — overidentification tests have low power in some settings and can be sensitive to simulation noise or weakly informative moments [@newey1994large].

### 6. Fit, validation, and counterfactual discipline

A good structural paper should answer at least four fit questions:

1. Which moments or distributions were targeted?
2. Which untargeted objects does the model also fit?
3. Does the model get the qualitative comparative statics right?
4. Is the policy counterfactual close enough to observed variation to be credible?

This is where model validation matters. For example, Todd and Wolpin use experimental variation to validate a dynamic schooling model before deploying it for broader policy counterfactuals [@todd2006assessing]. The general lesson is that fit is not a generic goodness-of-fit number; it is a **mapping between the question asked and the data patterns the model must explain**.

### 7. Variance estimation, bootstrapping, and inference in structural work

Structural estimation does not end with a point estimate. Applied readers need to know how much uncertainty attaches to parameters, moments, and counterfactuals.

#### 7.1 Hessian / information-matrix style inference

For likelihood-based estimators, the asymptotic variance is often approximated with the inverse Hessian or information matrix:

```{math}
:label: eq:info-matrix
\widehat{\mathrm{Var}}(\hat{\theta}) \approx \left[-\frac{1}{N}\sum_{i=1}^{N} \frac{\partial^2 \ell_i(\theta)}{\partial \theta \partial \theta'}\right]^{-1}.
```

This is convenient, but can be fragile if the model is misspecified or the numerical optimizer is unstable.

#### 7.2 Sandwich / OPG logic

For M-estimators and misspecification-robust inference, the sandwich form is often more appropriate:

```{math}
:label: eq:sandwich
\widehat{\mathrm{Var}}(\hat{\theta}) = A^{-1} B A^{-1},
```

where {math}`A` is the Jacobian/Hessian-type matrix and {math}`B` is the variance of the score or moment conditions. In GMM, the same logic appears through the Jacobian of the moments and the covariance of the empirical moments [@newey1994large].

#### 7.3 Delta method for counterfactuals

If the object of interest is a smooth function {math}`g(\hat\theta)` — for example a welfare measure or policy counterfactual — the delta method gives

```{math}
:label: eq:delta-method
\widehat{\mathrm{Var}}\big(g(\hat\theta)\big) \approx G(\hat\theta)\, \widehat{\mathrm{Var}}(\hat\theta)\, G(\hat\theta)',
```

where {math}`G(\hat\theta) = \partial g(\theta)/\partial \theta'\vert_{\hat\theta}`. This is often the practical default for reporting standard errors on elasticities, welfare measures, or treatment effects implied by the model.

#### 7.4 Bootstrap and resampling

Bootstrapping is especially useful when:
- the estimator is complicated or multi-step,
- analytical variance formulas are hard to derive,
- finite-sample behavior is a concern,
- or the object of interest is a nonlinear counterfactual.

A generic bootstrap distribution is constructed by repeatedly re-estimating the model on resampled data and using the empirical distribution of {math}`\hat\theta^{*(b)}` or {math}`g(\hat\theta^{*(b)})`. In practice, the lecture should emphasize two caveats:
- structural estimation can make naive bootstrap extremely expensive,
- and the resampling scheme must respect dependence (clusters, panels, or matched units when relevant).

#### 7.5 Cluster bootstrap and dependence

If the model is matched to clustered or panel moments, resampling must reflect the level at which variation is independent. A cluster bootstrap or block bootstrap can be more appropriate than iid resampling. This is especially important when moments are built from worker–firm panels, geographic panels, or policy-level variation.

#### 7.6 Two-step and simulation-related uncertainty

Two practical complications are often under-taught:
- **generated regressor / two-step variance**, where first-stage estimation uncertainty matters (Murphy–Topel logic), and
- **simulation error**, where a small number of simulation draws injects noise into the criterion function.

In practice, a transparent applied paper should state:
- whether uncertainty includes first-stage/generated-object estimation,
- whether simulation draws are held fixed or increased for inference,
- and whether the reported standard errors refer to primitives, moments, or counterfactuals.

### 8. When is likelihood better? When are moments better?

A practical decision rule is:

- Prefer **likelihood** when the model is tightly specified, the distributional assumptions are credible, and computational tractability is manageable.
- Prefer **moments / GMM / SMM** when the researcher wants to target economically meaningful summary statistics, avoid overcommitting to a full distribution, or work with complex simulation models.
- Prefer **indirect inference** when the model is easy to simulate but hard to estimate directly and there is a clear auxiliary empirical representation.

The tradeoff is not just efficiency versus convenience. It is also about interpretability: readers often understand a moments table more directly than a full latent likelihood.

### 9. Theory-to-applied bridge: how structural estimation becomes a paper

A useful way to read a structural paper is to ask:

1. What is the question?
2. Which primitives are latent?
3. Which moments or likelihood components identify them?
4. Why was this estimation strategy chosen?
5. Which counterfactuals are being taken seriously?
6. How is uncertainty reported?

#### Rust (1987)
Rust is the benchmark for likelihood-based dynamic discrete choice. The observed object is replacement timing; the latent object is continuation value and replacement cost. The paper is as much about implementation of dynamic likelihood estimation as it is about bus engines [@rust1987optimal].

#### Nevo (2000/2001) and BLP-style estimation
BLP-style work is the canonical illustration of moments, simulation, and counterfactual discipline. Even though the application is not labor, it is invaluable for teaching why researchers target moments, worry about multiple local minima, and validate substitution patterns before taking policy counterfactuals seriously [@berryLevinsohnPakes1995; @nevo2000maturity].

#### Todd and Wolpin (2006)
This is a model-validation lesson: structural counterfactuals are more persuasive when the model is disciplined by experimental or quasi-experimental variation [@todd2006assessing].

#### Low, Meghir, and Pistaferri (2010)
This paper shows how structural work can be indispensable when the question concerns latent insurance, wage risk, and lifecycle labor-supply behavior. The estimation logic is inseparable from the substantive question [@low2010wage].

#### Adda, Dustmann, and Stevens (2017)
A strong labor example of dynamic lifecycle structure in practice, showing how the model translates into career/fertility counterfactuals and how those counterfactuals depend on estimation discipline [@adda2017career].

## Research Lab

### Primary anchor: Rust (1987) in a reduced pedagogical estimation path

**Reproduce.** Implement a simplified dynamic-choice estimation exercise that mimics the mapping from observed decisions to continuation values and replacement/switching costs.

**Diagnose.** Ask what identifies the dynamic primitives, how sensitive the estimates are to the transition process, and whether the likelihood fit is informative about policy counterfactuals.

**Transfer.** Recast the same workflow for a labor setting: a stylized job-search, schooling, or training decision where continuation values matter.

### Challenge anchor: Todd and Wolpin (2006) or Adda, Dustmann, and Stevens (2017)

Use the second paper to show how the same logic scales up once the model includes richer states, family dynamics, or explicit policy counterfactuals. The point is not to fully replicate the frontier paper, but to understand why the model needs moments, simulation, and validation beyond point estimation.

## Methods Box

### Practical implementation rules for structural estimation

1. **Start from the question, not the algorithm.** If the counterfactual is within observed support, a reduced-form design may be enough.
2. **State the latent objects clearly.** Readers should know what the model adds beyond the observable comparison.
3. **Justify the estimation strategy.** Explain why likelihood, moments, simulation, or indirect inference is the right tool.
4. **Show the identifying variation.** Make clear which data features move which primitives.
5. **Report fit transparently.** Show both targeted and untargeted moments where possible.
6. **Report inference transparently.** State whether uncertainty comes from Hessian, sandwich, delta method, bootstrap, cluster bootstrap, or a multi-step correction.
7. **Treat counterfactuals as claims.** Their credibility depends on how well the model was disciplined by the data.

## Reading Ladder And References

### Core readings

- Rust (1987)
- Hotz and Miller (1993)
- Berry, Levinsohn, and Pakes (1995)
- Todd and Wolpin (2006)
- Low, Meghir, and Pistaferri (2010)

### Implementation and overview readings

- Newey and McFadden (1994)
- Pakes and Pollard (1989)
- Gourieroux, Monfort, and Renault (1993)
- Keane (2010)
- Aguirregabiria and Mira (2010)

### Labor-oriented extensions

- Keane and Wolpin (1997)
- Adda, Dustmann, and Stevens (2017)

## Exercises And Discussion Prompts

1. When is likelihood-based estimation genuinely more informative than a moments-based approach?
2. Give an example of a model that fits targeted moments well but would still not justify the intended counterfactual.
3. Why are weighting choices in GMM or SMM substantive rather than purely numerical?
4. When would you prefer a bootstrap to a delta-method approximation for a counterfactual object?
5. What does it mean to say that a structural result is “identified by assumption”?

## Reproducibility And Code Lab Note

The Lecture 7 lab should use a reduced pedagogical structural-estimation workflow rather than attempt full frontier replication. The priority is that students can see:
- how the criterion function is constructed,
- how parameters are mapped to moments or likelihood,
- how fit is checked,
- and how uncertainty is reported.

If a full official replication package is not locally available, the teaching path should rely on reduced synthetic data and bounded computational examples.

## Slide Companion Note

The slide deck should keep the lecture organized around the implementation chain:
identification -> estimation -> fit -> counterfactual discipline -> inference.
Slides should include explicit equations, concrete paper anchors, and a variance/inference slide that covers Hessian, sandwich, delta method, bootstrap, and simulation-noise issues.

## Bridge Forward

Lecture 7 focused on how to estimate and evaluate a structural model in practice. Lecture 8 will scale this logic up to **equilibrium structural work**, where the key added object is no longer only dynamic choice, but market interaction and policy counterfactuals with general-equilibrium feedback. In that setting, the same questions about identification, fit, and inference remain essential—but they now have to discipline equilibrium objects as well.
