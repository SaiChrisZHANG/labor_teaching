---
title: "Lecture 11. Causal ML, Policy Learning, and External Validity"
bibliography:
  - references.bib
---

# Lecture 11. Causal ML, Policy Learning, and External Validity

## Learning Objectives

By the end of this lecture, students should be able to:
- distinguish **heterogeneity estimation** from **policy learning** and from **prediction**
- define policy value, regret, targeting rules, and distribution shift in applied-economics language
- explain when individualized or subgroup treatment rules are empirically and substantively meaningful
- evaluate the limits of portability and external validity when treatment effects vary across settings
- recognize when common ML algorithms are useful measurement tools, targeting tools, or poor choices for the empirical problem at hand

## Opening Orientation

Lecture 10 treated machine learning as a way to estimate causal effects under high-dimensional nuisance structure. Lecture 11 asks a different question: once treatment effects vary, how should researchers decide **for whom** a policy is useful, **how** that policy should be targeted, and **whether** that targeting rule would survive contact with a new population, a new institution, or a new implementation environment?

This lecture is therefore about the transition from *heterogeneity as description* to *heterogeneity as decision input*. That transition is attractive, but dangerous: the same methods that organize heterogeneity can also overfit subgroups, exaggerate transportability, or quietly embed fairness and implementation assumptions that are not statistical at all.

```{admonition} Core points
:class: note
- Lecture 10 asks how to estimate effects credibly with high-dimensional nuisance components; Lecture 11 asks how to **use** heterogeneity once estimated.
- A treatment rule is an economic object, not just an ML object: it depends on feasibility, welfare weights, constraints, and implementation.
- Policy learning requires different diagnostics than effect estimation: value, regret, overlap, subgroup stability, and portability matter.
- External validity is not automatic; heterogeneous treatment effects in one site do not imply the same targeting rule is optimal elsewhere.
- Common ML algorithms are tools, not answers. Their role depends on whether the object is prediction, measurement, heterogeneity, or policy choice.
```

## Bridge

Lecture 10 introduced orthogonalization, sample splitting, and flexible heterogeneous-effect estimation. Here, those same tools become building blocks for targeting and policy design. The question is no longer simply whether treatment effects differ, but whether the evidence is strong enough to support differential treatment assignment, how to evaluate that rule, and when the rule is likely to break outside the original sample.

## Field Core

### 1. From Heterogeneity to Decision Rules

Let
```{math}
:label: eq:cate
\tau(x) = \mathbb{E}[Y(1) - Y(0)\mid X=x]
```
denote the conditional average treatment effect.

A policy rule maps covariates into treatment:
```{math}
:label: eq:policyrule
\pi(x) \in \{0,1\}.
```

The value of a treatment rule is:
```{math}
:label: eq:policyvalue
V(\pi) = \mathbb{E}[Y(\pi(X))].
```

An optimal rule under a given welfare criterion is:
```{math}
:label: eq:optimalrule
\pi^*(x) = \mathbf{1}\{\tau(x) \geq 0\}
```
only in the simplest case where treatment is costless, feasible for everyone, and welfare weights are uniform. In practice, capacity, budget, risk, fairness, and administrative constraints often imply:
```{math}
:label: eq:constrainedrule
\pi^* \in \arg\max_{\pi \in \Pi} \; V(\pi)
```
for a constrained policy class \(\Pi\).

A useful summary object is **regret**:
```{math}
:label: eq:regret
R(\pi) = V(\pi^*) - V(\pi).
```

The lecture’s first conceptual point is that **CATE estimation is not the same thing as policy learning**. CATEs organize treatment-effect heterogeneity; policy learning uses those effects, plus constraints and welfare criteria, to choose an assignment rule.

### 2. Heterogeneity Estimation Versus Policy Learning

Lecture 10 focused on the partially linear logic:
```{math}
:label: eq:plm
Y = \alpha D + g(X) + U,
```
or its heterogeneous extension:
```{math}
:label: eq:hte
Y = m(X) + \tau(X)D + U.
```

Lecture 11 keeps that foundation but shifts attention to:
- how to aggregate heterogeneous effects into decisions,
- how to evaluate those decisions out of sample,
- how to avoid using noise in subgroup estimates as if it were true policy-relevant signal.

This is why papers such as [@KitagawaTetenov2018] and [@atheyWager2021] are central: they treat targeting rules as empirical objects whose value can be estimated, compared, and disciplined.

### 3. Policy Value, Welfare, and Empirical Welfare Maximization

A practical policy-learning problem asks: among a class of candidate policies \(\Pi\), which one performs best?

One common object is the empirical welfare criterion:
```{math}
:label: eq:ewm
\hat{\pi} \in \arg\max_{\pi \in \Pi} \hat{V}(\pi),
```
where \(\hat{V}(\pi)\) is an estimated policy value.

The main implementation questions are:
- What is the policy class \(\Pi\)? Linear score rules, trees, or richer rules?
- How is policy value estimated?
- Is the policy feasible under budget or capacity constraints?
- How unstable is the selected rule across samples?

This is where **policy trees**, **empirical welfare maximization**, and **policy learning with observational data** enter.

### 4. External Validity, Distribution Shift, and Portability

Suppose a targeting rule is learned in source population \(S\), but the policy will be deployed in target population \(T\). Then the policy value in the target is:
```{math}
:label: eq:targetvalue
V_T(\pi) = \mathbb{E}_T[Y(\pi(X))].
```

Even if \(\pi\) performs well in \(S\), portability requires more than internal validity:
- support/overlap in covariates or relevant states,
- similarity of treatment-effect heterogeneity,
- stability of institutional implementation,
- stability of behavioral response,
- comparable constraints and policy costs.

A stylized reweighting perspective is:
```{math}
:label: eq:reweighting
\mathbb{E}_T[h(X)] = \mathbb{E}_S\left[\omega(X)h(X)\right],
```
where \(\omega(X)\) reweights the source toward the target. But this only helps if the relevant state variables are observed and support overlaps sufficiently.

The economic point is that **transportability is an equilibrium and institutional question, not just a statistical one**. A targeting rule that works in one setting may fail elsewhere because take-up, implementation, or constraint sets differ.

### 5. Fairness, Feasibility, and Deployment

Policy-learning papers often talk as if heterogeneity-based treatment rules are mechanically desirable. But economists should immediately ask:
- Is targeting legally feasible?
- Is the information required to target observable in practice?
- Does the rule induce stigma, sorting, or gaming?
- Does the rule create disparate impact across protected groups?
- Are there political or administrative reasons a lower-information rule may dominate a higher-performing one?

This is where the distinction between **statistical optimality** and **economic implementability** matters most.

### 6. A Practical ML Section Summary

The field increasingly relies on a common toolkit. What matters is not memorizing all algorithms, but knowing when they fit the research object.

#### Lasso, ridge, and elastic net
Best for:
- high-dimensional controls
- variable shrinkage
- stable linear prediction
- preprocessing for causal design

Caveats:
- coefficient interpretation is unstable after aggressive selection
- prediction gains do not imply causal validity
- variable inclusion is sensitive to tuning and collinearity

#### Random forests and gradient boosting
Best for:
- nonlinear prediction
- heterogeneous response surfaces
- flexible feature interactions
- measurement and classification tasks

Caveats:
- opaque functional form
- overfitting if tuning is careless
- poor transportability under feature drift
- feature importance is not causal importance

#### Causal forests / generalized random forests
Best for:
- discovering structured heterogeneity
- prioritizing follow-up analysis
- building ingredients for targeting

Caveats:
- estimated heterogeneity can be noisy
- subgroup instability is common
- policy conclusions require overlap, validation, and a welfare criterion
- standard errors and inference need care

#### Policy trees
Best for:
- interpretable decision rules
- explicit treatment assignment under simple constraints

Caveats:
- instability under small samples
- value estimates can be optimistic without honest validation
- simple trees may omit relevant nuance; complex trees lose interpretability

#### Support vector machines
Best for:
- margin-based classification with moderate-dimensional features
- some text and document-classification tasks

Caveats:
- not naturally interpretable for policy
- not a default causal tool
- tuning/kernel choices matter heavily

#### Neural networks / deep learning
Best for:
- very large, complex, unstructured data
- text, images, audio, or rich sequence data
- settings where feature learning itself matters

Caveats:
- heavy data requirements
- weaker interpretability
- transportability and fairness concerns are often sharper
- often excessive for standard tabular economics problems

#### Clustering methods
Best for:
- exploratory typologies
- unsupervised grouping
- market segmentation or worker/firm taxonomies

Caveats:
- clusters are not causal groups
- solutions depend on the chosen metric and number of clusters
- clustering can be useful descriptively but dangerous if treated as structural truth

### 7. Research Designs in Practice

The strongest applied papers in this area do not simply estimate heterogeneous effects. They usually do three things:
1. define a concrete intervention and a feasible assignment rule,
2. evaluate value/regret under transparent assumptions,
3. assess whether the learned rule is likely to transport.

Representative applications:
- empirical welfare maximization in treatment targeting [@KitagawaTetenov2018]
- policy learning with observational data [@atheyWager2021]
- algorithmic assignment and targeting in applied settings [@BansakFerwerdaHainmuellerEtAl2018]
- transportability and external validity debates [@Allcott2015; @Vivalt2020]

## Research Lab

### Primary anchor
**Reproduce:** [@KitagawaTetenov2018]

Students should reproduce the basic policy-learning logic: estimate treatment heterogeneity, define a feasible policy class, and compare policy value to simpler treatment rules.

### Diagnose
Key diagnostic questions:
- Is the learned policy exploiting genuine heterogeneity or sample noise?
- How sensitive is policy value to overlap and trimming?
- How much does policy performance vary across folds/subsamples?
- Is the policy learning step optimizing for welfare, accuracy, or something else?

### Transfer
**Transfer:** adapt the design to a new target population or site-level context inspired by external-validity papers such as [@Allcott2015] or [@Vivalt2020].

Good transfer exercises:
- reweight the source sample toward a target population,
- compare subgroup-targeting and simple universal rules,
- show how a policy with strong in-sample value may weaken under population shift.

## Methods Box

### Core workflow for causal ML with policy learning
1. define the policy-relevant target parameter
2. estimate nuisance components carefully
3. estimate heterogeneity honestly
4. constrain the policy class
5. evaluate value/regret out of sample
6. assess transportability and fairness
7. report uncertainty in value, not just in treatment effects

### Implementation caveats
- CATE estimates are rarely decision rules by themselves.
- Policy-learning results can be very unstable under weak overlap.
- External validity requires more than covariate balance; institutional comparability matters.
- A modest, transparent targeting rule often beats a highly flexible but poorly interpretable one.

## Reading Ladder And References

### Core
- [@wagerEstimationInferenceHeterogeneous2018]
- [@atheyGeneralizedRandomForests2019]
- [@KitagawaTetenov2018]
- [@atheyWager2021]

### External validity and transportability
- [@Allcott2015]
- [@Vivalt2020]
- [@DehejiaPopElechesSamii2021]

### Applications and policy design
- [@BansakFerwerdaHainmuellerEtAl2018]
- [@atheyImbens2016]

## Exercises And Discussion Prompts

1. Why is a noisy but unbiased CATE estimate not automatically useful for policy targeting?
2. Under what conditions does a policy tree become preferable to a fully flexible targeting rule?
3. What are the economic—not just statistical—obstacles to external validity?
4. Give an example where the “best” rule by value may be unacceptable because of fairness or implementation constraints.
5. When should economists prefer a simpler transparent rule to a more accurate but opaque rule?

## Reproducibility And Code Lab Note

The lecture’s lab should be implemented as a bounded teaching path:
- reduced reproduction of a policy-learning application,
- diagnosis of instability/overlap/value,
- transfer to a target-population or site-portability exercise.

## Slide Companion Note

The slide deck for this lecture should make the distinction from Lecture 10 explicit on the first substantive slide:
- Lecture 10: estimate effects with high-dimensional nuisance structure
- Lecture 11: use heterogeneity for decisions, policy rules, and portability

## Bridge Forward

This lecture closes the core ML block by showing that flexible methods are most useful when tied to economic objects: welfare, constraints, implementation, and portability. The remaining flexible blocks can then reinterpret these issues in spatial or network settings, where the same questions become even more acute because interference and equilibrium spillovers are harder to ignore.
