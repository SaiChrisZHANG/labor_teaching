# Lecture 17. Spatial Structural Modeling

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when a reduced-form spatial design is not enough and a spatial equilibrium model becomes necessary;
2. map an applied spatial question into equilibrium objects such as indirect utility, moving costs, commuting costs, wages, rents, local productivity, amenities, and housing supply;
3. distinguish static quantitative spatial models from dynamic spatial models with transition paths and forward-looking adjustment;
4. interpret gravity-style trade, commuting, and migration blocks as one tractable family inside broader spatial structural work;
5. evaluate identification, calibration, estimation, model fit, and counterfactual claims in spatial equilibrium papers;
6. summarize what Lectures 15 to 17 together contribute to an applied research design and identify open frontiers in spatial methods.

## Opening Orientation

Lecture 15 asked how researchers construct spatial empirical objects. Lecture 16 asked how spatial spillovers, sorting, exposure, and correlated shocks change causal inference. Lecture 17 asks a third question: **when do applied questions require a model of how workers, firms, rents, amenities, commuting flows, migration, and local prices interact across space?**

The lecture is methods-focused. It is not a general survey of urban economics, trade, migration, housing, or regional development. The object is the research workflow: when the policy question is an equilibrium object, what structure is needed, which data discipline the primitives, how should fit be assessed, and how far can the counterfactual be trusted?

The motivating distinction is partial equilibrium versus spatial equilibrium. A credible border design, shift-share design, or place-based event study can estimate a local effect. But many spatial policies do not only change treated units. They alter wages, rents, housing quantities, commuting patterns, firm location, market access, amenities, and welfare at the same time. Monte, Redding, and Rossi-Hansberg show why commuting and migration jointly shape local employment elasticities [@monteReddingRossiHansberg2018]. Hsieh and Moretti show why housing constraints can turn local productivity into rents, misallocation, and aggregate output losses rather than only local wage changes [@hsiehMoretti2019].

The central claim is conservative: not every spatial paper should be structural. But students should know when reduced-form place effects are the input rather than the answer.

## Core Points

:::{admonition} Core points
:class: important

- Spatial structural models become necessary when the research object is an equilibrium vector: wages, rents, location choices, commuting flows, migration, firm location, housing quantities, amenities, and welfare under a policy or shock.
- Reduced-form place effects are often essential evidence, but they may not identify incidence or welfare when workers, firms, landlords, and commuters adjust simultaneously.
- Core primitives include indirect utility, moving costs, commuting costs, local productivity, amenities, housing supply, congestion, labor demand, and bilateral frictions.
- Static models are useful for long-run incidence and comparative statics. Dynamic models are needed when transition paths, adjustment lags, expectations, tenure, capital, or policy timing matter.
- Gravity-style trade, commuting, and migration equations are tractable building blocks inside spatial structural models, not the whole lecture.
- Persuasive spatial structural work states what is identified, what is calibrated, what is estimated, what moments fit, and which counterfactual margins are extrapolated.
- The spatial block as a whole gives students three separate skills: curate spatial objects, identify causal effects with space, and model equilibrium propagation across places.
:::

## Bridge

Lectures 15 and 16 remain binding constraints. A structural model cannot rescue weak geography, undocumented exposure construction, contaminated comparisons, or unsupported spillover assumptions. It builds on the same discipline: define the economic object, state the counterfactual, document the data-generating process, and explain which assumptions do the work.

```{include} assets/tables/17-theory-to-applied-bridge.md
```

The bridge from earlier structural lectures is also direct. Lecture 6 introduced structure as a way to recover latent primitives and evaluate counterfactuals. Lecture 7 emphasized identification, moments, likelihood, simulation, and fit. Lecture 8 introduced equilibrium structural work across search, spatial, market, and policy environments. Lecture 17 narrows the lens to spatial equilibrium, where location choices and bilateral flows connect many local markets at once.

## Field Core

### A. Why Equilibrium Spatial Modeling Is Sometimes Necessary

Reduced-form spatial evidence is often the right first step. It can estimate whether a treated place changed relative to a comparison place, whether an exposure predicts outcomes, or whether a border generated a local discontinuity. It is enough when the estimand is local, the counterfactual remains inside observed support, and the policy question does not require prices or quantities elsewhere to adjust.

Spatial equilibrium modeling becomes necessary when the applied question asks about an object like:

- who captures a local productivity gain once rents and commuting respond;
- whether a transit improvement helps residents, in-commuters, firms, or landlords;
- how housing restrictions in productive places affect aggregate output and welfare;
- whether a local labor-demand shock is absorbed by migration, commuting, wages, rents, or unemployment;
- how a place-based subsidy changes firm location, local labor demand, and neighboring places;
- how a climate, infrastructure, or remote-work shock reallocates workers across locations over time.

One way to state the boundary is:

```{math}
:label: eq:em17-policy-object
\text{Reduced form is enough when } \tau(d)
\text{ is the policy object. Structure is needed when } \mathcal{E}(d)
\text{ is the policy object,}
```

where {math}`\tau(d)` is a local treatment effect and {math}`\mathcal{E}(d)` is an equilibrium mapping from policy or shock {math}`d` to wages, rents, flows, quantities, and welfare. The model is not automatically better. It is justified only if the research question requires {math}`\mathcal{E}(d)`.

The most common failure is to interpret a nominal wage effect as welfare. A worker's welfare can rise less than wages if rents increase, commuting costs worsen, or amenities fall. A resident may gain differently from an in-commuter. A firm may face a different effective labor supply depending on commuting openness. These are spatial equilibrium questions because the units interact through markets and movement.

### B. Core Spatial Equilibrium Objects

Spatial structural models differ in detail, but the same object classes appear repeatedly.

**Indirect utility.** A compact worker-side object is:

```{math}
:label: eq:em17-indirect-utility
V_{ioj}
=
w_j - r_i - c_{ij}^{commute} - m_{oi}
+ a_i + \varepsilon_{ioj},
```

where worker origin {math}`o`, residence {math}`i`, and workplace {math}`j` may differ. The wage {math}`w_j`, rent or local price {math}`r_i`, commuting cost {math}`c_{ij}^{commute}`, moving cost {math}`m_{oi}`, amenity {math}`a_i`, and idiosyncratic taste {math}`\varepsilon_{ioj}` together define the value of a spatial option. The equation makes two lessons visible. First, wages are not welfare. Second, residence, workplace, and origin are different spatial objects.

**Location choice and migration.** With extreme-value taste shocks, the probability that a worker from origin {math}`o` chooses residence {math}`i` and workplace {math}`j` can be written:

```{math}
:label: eq:em17-location-choice
P_{ioj}
=
\frac{\exp(\bar V_{ioj}/\sigma)}
{\sum_{i'}\sum_{j'}\exp(\bar V_{oi'j'}/\sigma)},
```

where {math}`\bar V_{ioj}` is utility net of the idiosyncratic component and {math}`\sigma` controls how strongly workers respond to utility differences. Migration data help discipline moving costs. Residence-workplace flows help discipline commuting costs. If the model observes only populations, it usually needs stronger assumptions to separate preferences, frictions, and prices.

**Commuting.** Commuting links residential labor supply to workplace labor demand. A bilateral commuting share can be summarized as:

```{math}
:label: eq:em17-commuting-share
\pi_{ij}^{commute}
=
\frac{B_j \phi_{ij}^{-\kappa}}
{\sum_{\ell}B_{\ell}\phi_{i\ell}^{-\kappa}},
```

where {math}`B_j` is workplace attractiveness, {math}`\phi_{ij}` is a bilateral commute cost, and {math}`\kappa` is the flow-cost elasticity. In applied work, {math}`\phi_{ij}` might come from distance, travel time, transit access, traffic, tolls, schedule constraints, or historical transport networks. The commuting matrix is not just a data object. It determines how local shocks propagate across residence and workplace geographies.

**Wages, rents, and amenities.** Spatial equilibrium models usually require a real-wage or utility object:

```{math}
:label: eq:em17-real-utility
\omega_i = w_i - r_i + a_i,
```

or a richer version with commuting and moving costs. Rents capitalize access and amenities; wages reflect productivity, labor demand, and sorting; amenities enter utility but are often latent. A model that does not separate these objects can misread a high-rent place as high-welfare or a high-wage place as high-opportunity.

**Housing supply and congestion.** A simple housing supply block is:

```{math}
:label: eq:em17-housing-supply
H_i^s = \bar H_i \left(\frac{r_i}{\bar r_i}\right)^{\eta_i},
```

where {math}`\eta_i` is a local supply elasticity. Low {math}`\eta_i` means demand shocks are more likely to show up in rents than in population. Congestion can enter through housing, commuting, local public goods, schools, or disamenities. These forces often decide incidence.

**Labor demand and firm location.** A workplace or firm-location block links wages to productivity and local demand:

```{math}
:label: eq:em17-labor-demand
L_j^d = D_j(w_j, A_j, M_j, X_j),
```

where {math}`A_j` is local productivity, {math}`M_j` is market access or demand access, and {math}`X_j` collects local shifters such as sector mix, infrastructure, regulations, or agglomeration forces. Firm entry or location choice can be modeled explicitly when the policy affects where firms operate, not only how many workers are employed in existing places.

**Equilibrium.** The equilibrium object combines choices, prices, and quantities:

```{math}
:label: eq:em17-equilibrium-map
\mathcal{E}(\theta;d)
=
\left\{
P_{ioj},\,
\pi_{ij}^{commute},\,
w_j,\,
r_i,\,
L_j,\,
H_i,\,
U_o
\right\}_{o,i,j},
```

where {math}`\theta` contains preferences, frictions, productivity, amenities, and supply parameters. A counterfactual changes {math}`d` and recomputes the fixed point. The economic content lies in which margins are allowed to adjust and which are held fixed.

### C. Static Versus Dynamic Quantitative Spatial Models

Static spatial models are useful when the question is about long-run incidence or comparative statics. They ask what the allocation would look like after workers, firms, rents, and flows adjust. This is the right first language for many place-based policies, housing-supply counterfactuals, transport improvements, and commuting-cost changes [@ahlfeldtReddingSturmWolf2015; @hsiehMoretti2019; @monteReddingRossiHansberg2018].

Dynamic spatial models are needed when the path matters. If moving is costly, housing capital is durable, workers are forward-looking, firms invest, households have tenure choices, or policy timing changes expectations, the long-run equilibrium may be insufficient. Dynamic urban work pushes spatial models toward transition paths, forward-looking migration, housing tenure, and macro-housing frictions [@GreaneyParkhomenkoVanNieuwerburgh2025].

```{include} assets/tables/17-static-vs-dynamic-map.md
```

The static-dynamic choice is not about sophistication. It is about the estimand. If the question is long-run incidence, a dynamic model may be unnecessary. If the question is who bears adjustment costs over the first five years of a housing, transport, climate, or remote-work shock, a static model may hide the object of interest.

### D. Gravity-Style Blocks As One Structural Family

Gravity-style equations are central in spatial economics because many bilateral flows decline with bilateral costs and rise with origin and destination attractiveness. They appear in trade, commuting, migration, applications, referrals, and trips. A generic gravity block is:

```{math}
:label: eq:em17-gravity-block
F_{ij}
=
\frac{O_i D_j \phi_{ij}^{-\kappa}}
{\sum_{\ell}D_{\ell}\phi_{i\ell}^{-\kappa}},
```

where {math}`O_i` is origin mass, {math}`D_j` is destination attractiveness or demand, {math}`\phi_{ij}` is bilateral cost, and {math}`\kappa` is the elasticity of flows with respect to cost. Log-linear versions are useful for diagnosis:

```{math}
:label: eq:em17-log-gravity
\log F_{ij}
=
\alpha_i + \delta_j - \kappa \log \phi_{ij} + e_{ij}.
```

Gravity is powerful because it links observed flows to unobserved frictions. It is also dangerous when treated as the whole model. A commuting gravity equation can recover how flows respond to travel costs, but incidence still depends on wages, rents, local labor demand, housing supply, and welfare. A migration gravity equation can discipline moving costs, but the welfare effect of a shock depends on what movers leave, where they arrive, and how prices adjust. A trade gravity equation can recover trade frictions, but local labor outcomes depend on production, factor mobility, and market clearing.

The right teaching statement is: gravity is a disciplined way to model bilateral flows inside a spatial equilibrium system. It is a subfamily of spatial structural work, not a substitute for the full equilibrium object when the policy question is incidence or welfare.

### E. Identification, Calibration, Estimation, Fit, And Counterfactual Interpretation

Spatial structural papers often combine reduced-form evidence, calibrated elasticities, direct estimation, and model inversion. Students should learn to ask which object comes from which source.

```{include} assets/tables/17-structural-estimation-diagnostics.md
```

**Identification.** The model should map empirical variation to primitives. Bilateral commuting or migration flows can identify flow-cost elasticities and frictions. Wages and employment can help recover local productivity or labor demand. Rents, prices, housing quantities, or land-use constraints can discipline housing supply. Amenities are often residual objects, so papers need restrictions or validation to keep amenities from absorbing every mismatch.

**Calibration versus estimation.** Some parameters may be calibrated from external papers, such as elasticities or housing supply responses. Others may be estimated from the paper's data. Calibration is not a sin, but it changes the evidentiary status of the result. A credible paper reports which headline counterfactuals move when calibrated parameters change.

**Fit.** Fit should be shown for targeted and untargeted objects. If the model targets commuting flows, wages, and rents, it should also report how it does on population changes, employment shares, non-targeted flows, or external validation moments when available. A model can fit targeted moments mechanically and still be unpersuasive for the counterfactual margin.

**Counterfactual distance.** A small transport-cost shock near observed support is different from a national remote-work transformation, a major climate migration scenario, or a large housing deregulation. Counterfactual credibility depends on how far the model extrapolates and whether the relevant margins were observed in the data.

**Welfare and incidence.** Spatial structural models are valuable because they can report welfare and incidence, but only if the utility object is explicit. Students should ask whose welfare is reported: incumbent residents, movers, commuters, landlords, firms, taxpayers, or a representative worker. Distributional weights and ownership of land or housing can change the answer.

### F. Spatial Methods Block Summary

This lecture closes the spatial methods block, so students need a separate map of what the block has accomplished.

**What Lectures 15 to 17 give students.** Lecture 15 teaches students to build defensible spatial objects: geographies, crosswalks, distances, travel costs, exposures, and access measures. Lecture 16 teaches them to make causal claims with space: spatial dependence, interference, border logic, shift-share exposure, sorting, and spatially robust inference. Lecture 17 teaches them when the estimand is no longer a local effect but an equilibrium object that requires prices, quantities, flows, and welfare.

**Where the literature is now.** Current spatial methods work is increasingly quantitative, flow-based, and data-rich. The literature uses commuting, migration, trade, housing, and firm-location data to connect local shocks to equilibrium incidence. It is also more explicit about equilibrium properties, multiplicity, computation, and validation [@reddingRossiHansberg2017; @Redding2024; @AllenArkolakisLi2024].

**Main active frontiers.** Important frontiers include dynamic adjustment, forward-looking migration, housing tenure, durable housing, remote work, climate adaptation, local labor-market power, sorting with heterogeneous workers, endogenous amenities, transport networks, and high-frequency mobility or platform data. Dynamic urban models are especially useful when transition paths and policy timing are central rather than incidental [@GreaneyParkhomenkoVanNieuwerburgh2025].

**Future opportunities.** Labor economists can contribute by combining administrative worker-firm data with spatial equilibrium discipline, studying remote and hybrid work as a commuting-cost shock, modeling how monopsony and firm market power vary across space, linking climate risk to migration and housing, and building transparent teaching-scale versions of frontier models. The most promising projects will not be structural for style. They will use the lightest model that recovers the equilibrium object the research question actually requires.

## Research Lab

The Week 17 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package.

The primary anchor paper is Monte, Redding, and Rossi-Hansberg [@monteReddingRossiHansberg2018]. It is central because it links commuting, migration, goods-market linkages, local employment elasticities, gravity-style flows, and spatial equilibrium counterfactuals. The challenge and extension paper is Greaney, Parkhomenko, and Van Nieuwerburgh [@GreaneyParkhomenkoVanNieuwerburgh2025], which pushes the block toward dynamic urban modeling, transition paths, forward-looking households, and housing frictions.

### Reproduce

Students reproduce a compact commuting-flow and local-incidence object inspired by Monte, Redding, and Rossi-Hansberg. Using deterministic synthetic locations and bilateral residence-workplace flows, they:

- estimate a simple gravity-style commuting relationship;
- construct commuting openness by residence location;
- solve a small teaching equilibrium with wages, rents, commuting costs, and location choices;
- compare a local productivity shock under fixed-flow and reallocated-flow interpretations;
- summarize which places gain through workplace employment, resident welfare, rents, or commuting access.

The purpose is not to replicate the published quantitative model. It is to make one central object visible: a local shock does not stay local when workers commute and locations interact.

### Diagnose

Students then diagnose which parts of the model are disciplined by data and which are imposed:

- Which bilateral flows identify commuting frictions?
- Which moments are targeted and which are left for validation?
- How sensitive is the counterfactual to the commuting elasticity?
- How sensitive is rent incidence to housing supply elasticity?
- What would be needed to separate amenities from productivity?
- Where would a reduced-form design stop?

The Diagnose memo must distinguish reduced-form evidence, identified structural primitives, calibrated elasticities, and closure assumptions.

### Transfer

Students transfer the logic to a dynamic frontier setting inspired by Greaney, Parkhomenko, and Van Nieuwerburgh. The synthetic teaching task does not solve a full dynamic urban model. Instead, students compare a static long-run response with a transition path under migration frictions and gradual housing adjustment. They:

- simulate adjustment after a housing or commuting-cost shock;
- compare impact, medium-run, and long-run welfare;
- identify which conclusions would be missed by a static model;
- write a memo explaining when dynamic structure is necessary rather than decorative.

The transfer task keeps the frontier concrete. The goal is to see why transition dynamics can change incidence and welfare interpretation.

## Methods Box

:::{admonition} Methods Box: How To Read A Spatial Structural Paper
:class: note

1. State the equilibrium object before the model details: incidence, welfare, commuting, migration, rents, productivity, market access, or firm location.
2. List the observed data objects: wages, rents, populations, housing quantities, bilateral flows, travel costs, firm locations, amenities, or outcomes.
3. Map each primitive to evidence: moving costs, commuting costs, productivity, amenities, housing supply, labor demand, and flow elasticities.
4. Separate estimated parameters from calibrated parameters and inverted residual objects.
5. Inspect targeted fit and untargeted fit separately.
6. Ask what the reduced-form version of the main fact would be.
7. Ask which margins adjust in the counterfactual and which are fixed by assumption.
8. Evaluate counterfactual distance from observed support.
9. Read welfare tables by group: residents, commuters, movers, landlords, firms, and taxpayers can gain differently.
10. Treat gravity blocks as flow discipline, not as a complete welfare model unless the rest of the equilibrium system is specified.
:::

## Reading Ladder And References

```{include} assets/tables/17-reading-architecture.md
```

For a first pass, students should read Monte, Redding, and Rossi-Hansberg for the commuting and migration benchmark, Hsieh and Moretti for spatial misallocation through housing constraints, and Redding and Rossi-Hansberg for the broader quantitative spatial economics architecture [@monteReddingRossiHansberg2018; @hsiehMoretti2019; @reddingRossiHansberg2017].

For canonical quantitative examples, Ahlfeldt, Redding, Sturm, and Wolf show how urban structure, density, and the Berlin Wall can be used to quantify agglomeration and welfare, while Allen and Arkolakis provide a trade-and-topography example of spatial equilibrium with bilateral frictions [@ahlfeldtReddingSturmWolf2015; @AllenArkolakis2014].

For frontier directions, students should read Redding's recent overview, Allen, Arkolakis, and Li on equilibrium properties, and Greaney, Parkhomenko, and Van Nieuwerburgh on dynamic urban economics [@Redding2024; @AllenArkolakisLi2024; @GreaneyParkhomenkoVanNieuwerburgh2025].

## Exercises And Discussion Prompts

1. A place-based policy raises employment in treated regions. When is the reduced-form estimate the answer, and when is it only an input into a spatial equilibrium model?
2. Write an indirect-utility expression for a worker who chooses both residence and workplace. Which terms are observed, which are latent, and which are likely to be calibrated?
3. Explain why a high nominal wage can be a poor welfare measure in a housing-constrained city.
4. A transit investment lowers commuting costs between two locations. Which outcomes would identify the commuting-cost elasticity? Which outcomes would speak to welfare?
5. What does a gravity-style commuting equation identify well, and what does it miss if it is not embedded in an equilibrium model?
6. Choose a spatial counterfactual and list the margins that should adjust. Which one margin would be most dangerous to hold fixed?
7. Give one research question where a static spatial model is enough and one where dynamic structure is essential.
8. Design one untargeted fit check for a spatial structural paper using bilateral flows.
9. How would your interpretation differ for incumbent residents, in-commuters, potential movers, firms, and landlords?

## Reproducibility And Code Lab Note

The Lecture 17 lab is located in `labs/17-spatial-structural-modeling/`. It uses deterministic synthetic teaching data so the public workflow does not depend on confidential commuting microdata, proprietary routing data, or an uncertain replication package. The smoke path creates the data, estimates a gravity-style commuting relationship, solves a compact equilibrium counterfactual, diagnoses model fit and sensitivity, and transfers the logic to a dynamic adjustment exercise.

Students should state clearly that the lab is a teaching reproduction of structural logic, not an official replication of Monte, Redding, and Rossi-Hansberg or Greaney, Parkhomenko, and Van Nieuwerburgh. The output is a methods memo about equilibrium objects, assumptions, and counterfactual interpretation.

## Slide Companion Note

The Lecture 17 slides should not duplicate the chapter. They should make the architecture visible:

- why reduced-form spatial evidence can be insufficient;
- the core equilibrium map linking utility, flows, wages, rents, housing, firms, and welfare;
- static versus dynamic spatial structure;
- gravity-style blocks as flow discipline inside broader equilibrium models;
- identification, calibration, fit, and counterfactual interpretation;
- a separate summary of the spatial methods block;
- the Reproduce -> Diagnose -> Transfer lab design.

At least one slide should state plainly: **gravity is a building block, not the whole spatial structural model.**

The canonical slide source is `slides/week17/17-spatial-structural-modeling.tex`.

## Bridge Forward

This completes the spatial methods block. Students should now be able to distinguish three tasks that are often blurred: curating spatial data, identifying causal effects with space, and modeling the equilibrium environment through which spatial shocks propagate.

The bridge to the network block is natural. Spatial models organize interaction through geography, distance, commuting, migration, and market access. Network models organize interaction through links, peers, referrals, firms, schools, platforms, and social structure. In both blocks, the methodological discipline is the same: define the object, state the counterfactual, and make the dependence structure explicit.
