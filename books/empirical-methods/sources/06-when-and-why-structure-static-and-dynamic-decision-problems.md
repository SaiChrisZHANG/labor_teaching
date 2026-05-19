---
title: Lecture 6. When and Why Structure? Static and Dynamic Decision Problems
bibliography:
  - references.bib
---

# Lecture 6. When and Why Structure? Static and Dynamic Decision Problems

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when a structural model is necessary rather than merely optional;
2. distinguish static from dynamic decision problems and identify the relevant state variables;
3. map observed outcomes to latent primitives such as preferences, technologies, expectations, and constraints;
4. explain what structural estimation contributes beyond a credible comparison;
5. evaluate structural papers in terms of identification, fit, counterfactual discipline, and interpretation.

## Opening Orientation

This lecture opens the structural-estimation block by treating structure as a **research choice** rather than a methodological ideology. The central question is not whether structural work is “better” than design-based work, but when an applied question requires a model because the object of interest is latent, dynamic, welfare-relevant, or outside the observed policy support. Structural work is most valuable when the empirical question is about incentives under new rules, expectations, dynamic adjustment, or equilibrium behavior that cannot be read directly off a reduced-form contrast [@keane2010structural; @aguirregabiria2010dynamic].

```{admonition} Core points
:class: important
- Structural models are useful when the policy question depends on latent primitives, dynamic behavior, expectations, or welfare objects that are not directly observed.
- The key distinction is not “causal versus noncausal,” but **credible comparison versus disciplined model-based extrapolation**.
- A structural paper must specify what is observed, what is latent, and what variation in the data disciplines the latent objects.
- Static and dynamic problems require different state variables, different identifying variation, and different interpretation of estimated parameters.
- The main credibility threats in structural work are not only functional form, but also misspecified expectations, under-disciplined heterogeneity, weak fit to non-target moments, and overconfident counterfactual interpretation.
```

## Bridge

The causal-inference block asked: *what can we learn from comparisons that are already in the data?* This block asks a different question: *what if the object of interest is not directly observed, or the policy of interest has never been observed before?* The bridge from reduced-form to structure is therefore the move from **design-based identification of observed treatment effects** to **model-based identification of primitives and behavioral rules** [@keane2010structural].

## Field Core

### 1. Why structure?

A reduced-form design is often enough when the object of interest is a treatment effect under a policy or shock already observed in the data. But structure becomes attractive when researchers need to answer questions such as:

- What is the value of a training subsidy that changes the timing of schooling, work, and fertility over the lifecycle?
- What would happen under a policy regime never observed in the data?
- How much of observed behavior reflects latent preferences versus constraints?
- What is the welfare effect of a reform when welfare itself is not observed?
- How will behavior change once agents anticipate the reform?

These questions require a model because they involve latent primitives, forward-looking decisions, or counterfactuals outside the support of observed policies [@todd2006assessing; @low2010wage].

### 2. Static discrete choice: what is observed and what is latent?

A useful starting point is a static discrete-choice problem. An agent chooses among alternatives \(j \in \mathcal{J}\), with latent utility

```{math}
:label: eq:latent-utility
U_{ij} = X_{ij}'\beta + \xi_{ij} + \varepsilon_{ij},
```

where \(X_{ij}\) is observed to the researcher, \(\xi_{ij}\) may be observed by agents but not by the econometrician, and \(\varepsilon_{ij}\) is an idiosyncratic shock. The researcher observes the chosen alternative,

```{math}
:label: eq:choice-rule
d_{ij} = \mathbf{1}\{U_{ij} \ge U_{ik} \ \forall k \in \mathcal{J}\},
```

but does not directly observe utility, expectations, or latent costs.

If \(\varepsilon_{ij}\) is Type-I extreme value, the model implies the familiar logit probability,

```{math}
:label: eq:logit-choice-probability
P(d_{ij}=1 \mid X_i) = \frac{\exp(X_{ij}'\beta + \xi_{ij})}{\sum_{k \in \mathcal{J}} \exp(X_{ik}'\beta + \xi_{ik})}.
```

This is useful as a teaching device because it shows the basic structural move: start from a utility model, derive a behavioral object, and estimate parameters that are interpretable as latent preference or cost parameters.

### 3. Dynamic decision problems

Static models are often inadequate in labor settings because many labor choices are dynamic:
- schooling and career choice,
- job search and reservation wages,
- labor supply over the lifecycle,
- fertility and work,
- retirement and savings,
- training and occupation switching.

In a dynamic setting, the value of an action today depends on how it changes tomorrow’s state. Let \(s_t\) denote the state at time \(t\), \(a_t\) the chosen action, and \(u(a_t,s_t)\) per-period utility. A canonical dynamic decision problem is written as

```{math}
:label: eq:bellman
V(s_t) = \max_{a_t \in \mathcal{A}(s_t)} \left\{ u(a_t,s_t) + \beta \mathbb{E}\left[V(s_{t+1}) \mid s_t, a_t\right] \right\}.
```

The current action affects future states \(s_{t+1}\), and therefore future options. This is why dynamic models need:
- state variables,
- transition rules,
- expectations,
- discounting,
- sometimes latent heterogeneity in preferences or productivity.

The dynamic choice rule then depends not only on current utility but on continuation values:

```{math}
:label: eq:choice-specific-value
v(a_t,s_t) = u(a_t,s_t) + \beta \mathbb{E}\left[V(s_{t+1}) \mid s_t, a_t\right].
```

Structural estimation becomes useful precisely because continuation values are not directly observed.

### 4. What structure adds

A structural model contributes in at least four ways.

#### 4.1 Latent primitives
It allows researchers to infer objects not directly observed in the data:
- risk aversion,
- switching costs,
- search costs,
- discount factors,
- expectations,
- learning parameters,
- latent skill prices.

#### 4.2 Dynamic incentives
It makes clear that the effect of a policy today depends on future incentives. A subsidy can shift behavior not only through current prices, but also through expected future returns.

#### 4.3 Counterfactual policy analysis
It can evaluate policies not observed in the historical data, provided the model is well disciplined.

#### 4.4 Welfare
It can map behavior into welfare objects when welfare is not directly observed in reduced-form comparisons.

### 5. Identification, estimation, and fit

A structural model is not credible merely because it is explicit. The core question is always: **what in the data identifies the latent objects?**

Three common estimation logics are:

#### Likelihood-based estimation
Specify the full probability of observed choices or outcomes given parameters \(\theta\), then estimate

```{math}
:label: eq:likelihood
\hat{\theta} = \arg\max_{\theta} \sum_{i=1}^{N} \log f(y_i \mid x_i; \theta).
```

#### Method of moments / simulated method of moments
Choose parameters so that model-implied moments match empirical moments:

```{math}
:label: eq:mm
\hat{\theta} = \arg\min_{\theta} \left[ m^{data} - m^{model}(\theta) \right]' W \left[ m^{data} - m^{model}(\theta) \right].
```

#### Dynamic programming with simulation / CCP methods
Use value-function iteration, simulation, or conditional-choice-probability shortcuts to solve and estimate dynamic models [@hotz1993conditional; @aguirregabiria2010dynamic].

The lecture should emphasize that “fit” is not generic goodness of fit. Good structural work must show:
- which moments were targeted,
- which non-target moments the model can also match,
- which counterfactuals are close to the identifying variation,
- and where the model is weak.

### 6. Credibility threats and limits

Structural work has recurring failure modes.

#### Functional-form dependence
A strong result may be an artifact of specific parametric assumptions.

#### Expectations misspecification
If the model misstates what agents know or expect, dynamic parameters may be misleading.

#### Identification by assumption
The model may appear well estimated, but the key primitives may be pinned down more by normalization or exclusion assumptions than by informative variation.

#### Weak off-target fit
A model can match the moments it was asked to fit while missing crucial untargeted behavior.

#### Extrapolation beyond support
A structural counterfactual may be technically computable but substantively weak if the new policy is too far from the observed environment.

These limits do not make structure unhelpful. They simply mean that structural work must be read with the same discipline we bring to reduced-form designs.

### 7. Research architecture: from theory to applied work

A good way to understand structural work is to ask five questions of any paper.

1. **What is the economic question?**
2. **What is latent and why does reduced-form work not recover it?**
3. **What variation in the data disciplines the model?**
4. **What moments or likelihood objects are being fit?**
5. **Which counterfactual or welfare object becomes available once the model is estimated?**

This framework helps students see why some papers are worth the cost of structure while others are not.

### 8. Signature papers and what they teach

#### Rust (1987)
Rust’s bus-engine replacement model remains the canonical example of dynamic discrete choice. The observed object is replacement behavior; the latent object is the value of replacing versus waiting; the model’s contribution is to infer replacement costs and continuation values under a dynamic maintenance problem [@rust1987optimal].

#### Hotz and Miller (1993)
Hotz and Miller show how dynamic problems can sometimes be estimated by using conditional choice probabilities rather than full nested dynamic programming at every step. This is a methodological advance about implementation, not just a labor application [@hotz1993conditional].

#### Keane and Wolpin (1997)
Keane and Wolpin treat early-career decisions as a dynamic problem involving work, schooling, and occupational choice. The model is useful because career choices today change experience, skills, and future wages tomorrow [@keane1997career].

#### Todd and Wolpin (2006)
Todd and Wolpin show how a dynamic model can be used to evaluate a policy counterfactual—in this case a schooling subsidy—while validating the model against experimental variation [@todd2006assessing].

#### Low, Meghir, and Pistaferri (2010)
This is a strong example of lifecycle structure used to recover latent insurance and labor-supply mechanisms under wage and employment risk [@low2010wage].

#### Adda, Dustmann, and Stevens (2017)
This paper illustrates how dynamic models help quantify long-run career costs and intertemporal tradeoffs when childbearing and labor-market choices interact over time [@adda2017career].

## Research Lab

### Primary anchor: Rust (1987) in reduced pedagogical form

**Reproduce.** Recreate a bounded pedagogical version of a dynamic discrete-choice problem in which an agent chooses whether to continue or replace a capital good. The goal is not to replicate the full original paper, but to reproduce the logic of dynamic choice and the role of continuation values.

**Diagnose.** Explain what the dynamic model identifies that a static hazard or reduced-form comparison cannot. Identify the key latent objects and discuss which parts are disciplined by observed transitions and which parts depend more heavily on assumptions.

**Transfer.** Adapt the same logic to a simple labor problem: job acceptance versus continued search, training versus immediate work, or retirement now versus retirement later. The transfer exercise should focus on states, actions, and continuation values rather than solving a large model.

### Challenge / extension anchor: Keane and Wolpin (1997)

Use a simple career-choice setting to show how dynamic structure becomes more demanding when state variables multiply, expectations matter, and policy counterfactuals change future opportunity sets. Students should compare the bus-replacement logic to a human-capital or career-choice problem and explain why the estimation challenge is harder.

## Methods Box

A practical way to judge whether a structural model is appropriate is to ask:

1. Is the parameter of interest latent rather than directly observed?
2. Is behavior dynamic or state dependent?
3. Is the policy counterfactual outside observed support?
4. Is welfare central to the question?
5. Are equilibrium or strategic responses important?

If the answer to several of these is yes, structure is often worth considering. If not, a reduced-form approach may be more transparent and sufficient.

## Reading Ladder And References

### Core
- [@keane2010structural]
- [@rust1987optimal]
- [@hotz1993conditional]
- [@keane1997career]

### Next
- [@aguirregabiria2010dynamic]
- [@todd2006assessing]
- [@low2010wage]
- [@adda2017career]

## Exercises And Discussion Prompts

1. Give an example of an empirical question where reduced-form evidence is enough and another where structure is necessary.
2. In a dynamic labor model, what counts as a state variable and why?
3. Why is “good fit” not a sufficient argument for believing a structural counterfactual?
4. Compare Rust (1987) and Keane–Wolpin (1997). What is latent in each case, and what is the model buying the researcher?
5. What are the main tradeoffs between likelihood-based estimation and moment-based estimation?

## Reproducibility And Code Lab Note

The Week 6 lab should provide a bounded pedagogical dynamic discrete-choice workflow. If full official replication files are not locally available, the teaching path may use synthetic data and a simplified dynamic-choice model. The goal is to teach state variables, continuation values, and counterfactual discipline rather than to reproduce every original result exactly.

## Slide Companion Note

The slide deck for this lecture should emphasize:
- when structure is worth the cost,
- the distinction between static and dynamic problems,
- observed versus latent objects,
- Bellman logic,
- estimation strategies,
- and the interpretation limits of structural counterfactuals.

## Bridge Forward

The next lecture moves from “when structure?” to “how structure is implemented in practice,” focusing on identification, estimation routines, simulation, and fit. That lecture will make the computational and empirical side of structural work much more concrete.
