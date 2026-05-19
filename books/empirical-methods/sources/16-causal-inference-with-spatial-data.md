---
title: Lecture 16. Causal Inference with Spatial Data
bibliography:
  - references.bib
---

# Lecture 16. Causal Inference with Spatial Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish when geography is the source of identification, a threat to inference, or the mechanism itself;
2. explain how spatial spillovers and interference violate simple SUTVA logic and how exposure mappings partially repair that problem;
3. implement and interpret core spatial causal designs, including border designs, spatial RD, shift-share/place-based designs, and exposure-based designs;
4. explain when Conley-style or other spatially robust inference is necessary and what it does and does not solve;
5. diagnose the main threats in spatial work: sorting, correlated shocks, endogenous boundaries, MAUP, and hidden spillovers;
6. translate a spatial identification problem into a credible applied economics project with explicit geography, counterfactual, and inference choices.

## Opening Orientation

Lecture 15 showed that spatial data are not neutral bookkeeping objects: geographies, buffers, travel-time, and boundary definitions determine what the empirical object actually is. Lecture 16 asks the next question: once those objects exist, **how can researchers make causal claims with them?**

Spatial data create a special identification problem because nearby units often share shocks, affect one another, sort into the same places, and cross boundaries. Geography can therefore play three roles at once: it can provide identifying variation, it can threaten inference, and it can be the mechanism of interest. The core skill in this lecture is learning to say which role space is playing in a given design and what assumptions are needed to make that role credible.

:::{admonition} Core points
:class: note
- Spatial data complicate causal inference because proximity creates correlated shocks, interference, endogenous sorting, and ambiguous geography choice.
- Conley-style or related spatially robust inference addresses spatially correlated residuals, but it does not solve bias from spillovers or endogenous location choice.
- Exposure mappings, border designs, spatial RD, and shift-share designs all use geography differently; students should be explicit about the identifying object in each case.
- The same place-based design can fail for very different reasons: hidden spillovers, endogenous boundaries, MAUP, transport costs, or omitted local shocks.
- A strong spatial causal design names the mechanism, the geography, the interference structure, the comparison group, and the inference correction all at once.
:::

## Bridge

Lecture 15 focused on how to build spatial objects. Lecture 16 focuses on how to identify causal effects with those objects. The connection is direct: every spatial design inherits the geography, distance, and exposure choices made upstream. Lecture 17 will then ask what changes when the researcher wants not just a treatment effect, but a spatial counterfactual equilibrium.

## Field Core

### 1. Geography in causal inference: source, threat, or mechanism?

The first discipline in spatial work is to decide which role geography plays.

- **Source of identification**: borders, distance discontinuities, or spatially varying exposure create quasi-experimental variation.
- **Threat to inference**: nearby units share shocks, making standard errors and even untreated comparisons misleading.
- **Mechanism**: travel cost, neighborhood exposure, local public goods, or commuting access are themselves the channel through which a treatment works.

Many papers fail because they slide across these roles. A border is not automatically identification. A spatial correlation correction is not automatically a spillover model. A tract-level exposure is not automatically a neighborhood effect. Good spatial causal work is explicit about which role geography is playing.

### 2. Spatial dependence, SUTVA, and exposure mappings

The textbook potential-outcomes framework often assumes that one unit's outcome depends only on its own treatment status. Spatial work routinely violates this. A more realistic object is:

```{math}
:label: eq:spatial-exposure-po
Y_i = Y_i(D_i, E_i),
```

where {math}`D_i` is own treatment and {math}`E_i` is a summary of neighbors' treatment or place-based exposure. A common exposure mapping is:

```{math}
:label: eq:spatial-exposure-map
E_i = \sum_{j \neq i} w_{ij} D_j,
```

where {math}`w_{ij}` encodes geographic proximity, commuting links, or some other notion of exposure.

This is the first big lesson for students: **interference is not a footnote in spatial work**. If treatment spills across space, then a design that implicitly assumes no spillovers can be biased even when the assignment rule itself looks clean. Miguel and Kremer’s worm-paper remains a canonical lesson because it made this point explicit and measured treatment externalities rather than treating them as noise [@miguelKremer2004].

In practice, researchers need to decide whether they believe:
1. no spillovers;
2. spillovers are negligible beyond a radius;
3. spillovers can be summarized by an exposure mapping;
4. spillovers are themselves the object of interest.

### 3. Spatially correlated shocks and inference

Nearby places often experience common weather, policy, labor-demand, or demographic shocks. Even if treatment is well defined, ordinary robust or simple clustered standard errors can understate uncertainty when residuals decay with distance rather than cluster neatly by one administrative unit.

A generic Conley-style covariance estimator takes the form:

```{math}
:label: eq:conley-vcov
\widehat{\mathrm{Var}}(\hat\beta)
=
(X'X)^{-1}
\left(
\sum_i \sum_j K\!\left(\frac{d_{ij}}{c}\right)
x_i x_j' \hat u_i \hat u_j
\right)
(X'X)^{-1},
```

where {math}`d_{ij}` is distance between observations, {math}`c` is a cutoff radius, and {math}`K(\cdot)` downweights correlations at larger distances.

Students should be clear about what this does: it changes **inference**, not **identification**. Conley-style corrections do not solve spillovers, sorting, or endogenous boundary choice. They only adjust variance estimates when residual dependence is spatially structured. This is why many empirical papers report Conley-style standard errors as a robustness step, not as the heart of the design.

### 4. Border designs and spatial RD

A spatial border design compares units on opposite sides of a policy, administrative, or institutional border. The intuition is local comparability: nearby places may be similar except for the rule or institution that changes at the boundary.

A generic spatial RD specification can be written as:

```{math}
:label: eq:spatial-rd
Y_i = \alpha + \tau \mathbf{1}\{b_i \ge 0\} + f(b_i) + X_i'\gamma + \varepsilon_i,
```

where {math}`b_i` is signed distance to the border.

There are at least three distinct families students should separate:

1. **Administrative border comparisons** (for example contiguous counties or municipalities).
2. **Boundary-discontinuity designs** with signed distance to a frontier or school-zone line.
3. **Multi-dimensional spatial RD** where units are compared near an irregular boundary and distance alone does not summarize all relevant geography.

Anchor papers here differ for a reason:
- Dube, Lester, and Reich use contiguous county pairs to compare labor-market policy across nearby counties [@dubeLesterReich2010].
- Black uses school-district boundaries to value school quality [@black1999].
- Dell uses a historical treatment boundary in Peru to study long-run labor-market and development effects [@dell2010].

These papers are useful because each teaches a different caveat:
- contiguous units may still differ in trends;
- boundaries may be endogenous to sorting or policy;
- historical boundaries may coincide with many long-lived local differences.

A good spatial RD does not merely show a map. It argues why local continuity is plausible, why the border is not itself chosen by current outcomes, and why nearby units do not contaminate one another too much across the boundary.

### 5. Shift-share and place-based exposure designs

Shift-share designs use pre-period local shares and aggregate shocks to construct local exposure:

```{math}
:label: eq:shift-share
Z_\ell = \sum_s w_{\ell s} g_s,
```

where {math}`w_{\ell s}` are location-specific shares and {math}`g_s` are common shocks at the sector, origin-country, or product level.

Students now encounter shift-share instruments in many settings:
- trade shocks,
- migration shocks,
- industrial/technology exposure,
- and place-based policy incidence.

What makes this a spatial method is that the local exposure inherits a geography and a market definition. The key identification questions are:
- are the shares plausibly predetermined?
- are the shocks exogenous?
- what is the effective source of identifying variation?
- are residual spatial correlations or spillovers still present?

This is why modern work emphasizes decomposition and diagnostics for shift-share designs rather than treating them as plug-and-play instruments [@borusyakHullJaravel2025; @goldsmithPinkhamSorkinSwift2020]. When used carefully, they are powerful; when used casually, they can bury endogeneity inside shares and correlated local structure.

A related but distinct family is **place-based policy design**, such as empowerment zones or local subsidy programs. These often combine geography, policy timing, and spillovers, so the same questions recur: what is the right geography, who is exposed, and where does the comparison group come from?

### 6. Spatial mismatch, neighborhood exposure, and sorting

Some spatial designs try to estimate the effect of where people live or the jobs they can access. Here the main threat is sorting: workers choose neighborhoods, commutes, or schools partly based on latent attributes that also affect labor outcomes.

This is why neighborhood and local-opportunity work often relies on:
- mover designs,
- randomized housing or mobility lotteries,
- or plausibly exogenous shocks to location or transport access.

The broader lesson is methodological: **when place is the treatment, selection into place is usually the central threat**. Spatial mismatch or neighborhood effects cannot be identified with geography alone. Students need to ask:
- who chose the place?
- when was the place chosen?
- what alternatives were feasible?
- how much of the measured “neighborhood effect” is really sorting or correlated local institutions?

### 7. MAUP and endogenous geography choice

The modifiable areal unit problem (MAUP) is not just a descriptive nuisance. It can change the causal estimand. A treatment effect estimated at the tract level may not resemble the same effect at the county or commuting-zone level because the mechanism, spillovers, and residual correlation all change with the unit of analysis.

This leads to a practical rule: if a result changes sharply when the geography changes, the researcher should ask whether the mechanism is truly scale-dependent or whether the design was never tightly tied to mechanism in the first place.

### 8. Good design logic: what students should say in a paper

A strong spatial causal design should explicitly answer:

1. **What is the mechanism?** commuting cost, local labor demand, neighborhood exposure, spillover, or institutional boundary?
2. **What is the relevant geography?** tract, county, commuting zone, boundary segment, radius, or network catchment?
3. **Where does identification come from?** border, shock, exposure, timing, or mover variation?
4. **How is interference handled?** ignored, bounded by distance, modeled through exposure mappings, or made part of the estimand?
5. **How is inference handled?** Conley-style correction, clustering, permutation, randomization inference, or something else?
6. **What are the main threats?** sorting, endogenous boundaries, omitted local shocks, MAUP, temporal mismatch, spillovers.
7. **What is the counterfactual?** and is it local, general-equilibrium, or exposure-based?

That checklist matters more than any single estimator.

## Research Lab

### Primary anchor paper
Use a border-based or local spatial design as the main replication anchor. A strong default is [@dubeLesterReich2010] because it forces students to think about contiguous comparisons, border choices, local shocks, and spatially correlated inference all at once.

### Reproduce
Recreate a simplified spatial comparison:
- define a border-pair or local-neighbor sample,
- estimate a baseline treatment effect,
- report standard inference and a spatially aware inference correction.

### Diagnose
Students then diagnose:
- whether geography is the identifying source or only a control,
- whether nearby untreated units may also be exposed,
- how sensitive inference is to spatial correction or geography choice,
- and whether the comparison set is economically coherent.

### Transfer
Transfer the design logic to one of:
- a spatial RD around a historical or policy boundary (e.g. [@dell2010]),
- a shift-share/place-exposure design (e.g. [@borusyakHullJaravel2025]),
- or a neighborhood/mobility design where sorting is central (e.g. [@chettyHendrenKatz2016]).

## Methods Box

:::{admonition} Methods Box: Practical Spatial Causal Inference Rules
:class: note

```{include} assets/tables/16-designs-and-corrections-toolkit.md
```

```{include} assets/tables/16-good-design-checklist.md
```

The most common failure in spatial causal work is to fix the estimator before fixing the geography and the interference structure. The best projects reverse that order.

:::

## Reading Ladder And References

### Core methodological anchors
- [@conley1999]
- [@borusyakHullJaravel2025]
- [@goldsmithPinkhamSorkinSwift2020]

### Border and spatial RD anchors
- [@black1999]
- [@dell2010]
- [@dubeLesterReich2010]

### Exposure and sorting anchors
- [@miguelKremer2004]
- [@chettyHendrenKatz2016]
- [@bussoGregoryKline2013]

## Exercises And Discussion Prompts

1. Give one example where geography is the source of identification, one where it is mainly a threat to inference, and one where it is the mechanism itself.
2. Why can Conley-style standard errors be useful in a spatial design while still leaving the estimate biased?
3. When does a border design become a spatial RD rather than just a neighbor comparison?
4. What assumptions make a shift-share design spatially meaningful rather than just a weighted index?
5. Suppose a treatment effect disappears when the geography changes from tract to county. What are two interpretations of that fact?

## Reproducibility And Code Lab Note

The Lecture 16 lab should include a reduced spatial border or exposure exercise with synthetic or bounded data. The smoke path should be runnable offline and should illustrate geography construction, baseline estimation, and one spatial-diagnostic step.

## Slide Companion Note

Slides should make three distinctions especially clear:
1. geography as source, threat, or mechanism;
2. border designs vs exposure designs vs shift-share designs;
3. inference corrections vs identification fixes.

Include one slide that explicitly says: **spatially robust standard errors are not a substitute for a spillover model or a sorting design**.

## Bridge Forward

Lecture 16 shows how space complicates causal inference. Lecture 17 takes the next step and asks when partial-equilibrium causal estimates are no longer enough because locations, commuting flows, prices, or firms interact in equilibrium.
