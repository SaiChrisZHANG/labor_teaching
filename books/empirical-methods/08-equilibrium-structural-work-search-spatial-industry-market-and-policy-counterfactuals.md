# Lecture 8. Equilibrium Structural Work: Search, Spatial, Industry/Market, And Policy Counterfactuals

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain equilibrium structure as a research choice for settings where decisions interact through markets, firms, prices, locations, or flows;
2. compare search, spatial, and industry/market equilibrium models using the same applied questions: what is observed, what is latent, what identifies the primitives, and what counterfactual is gained;
3. derive the core equilibrium objects behind matching, free entry, wage or surplus sharing, location choice, market clearing, demand, pricing, fixed points, and welfare;
4. distinguish equilibrium counterfactuals that are disciplined by observed variation from counterfactuals that mostly rest on closure assumptions;
5. evaluate computation, estimation, and validation burdens in equilibrium structural papers;
6. design a Reproduce -> Diagnose -> Transfer lab around a bounded equilibrium counterfactual.

## Opening Orientation

Lecture 8 closes Block 2 by asking what changes once one agent's decision changes the environment faced by others. Lectures 6 and 7 focused on individual structural models: choices, states, moments, likelihoods, simulation, fit, and counterfactual discipline. This lecture adds the equilibrium layer. In many applied questions, vacancies, wages, rents, prices, market shares, entry, commuting flows, and locations are endogenous. A partial-equilibrium model can describe an individual's decision, but it may miss the incidence and welfare effects created by market adjustment.

The central question is: **when is equilibrium structure worth the extra assumptions?** The answer is not "whenever a theorist can write down an equilibrium." Equilibrium structure is worth the cost when the research question depends on endogenous market response: search externalities, vacancy creation, wage-setting, housing incidence, migration, commuting, markups, firm conduct, entry, or policy counterfactuals that reallocate workers and firms across markets. It is not worth the cost when a transparent design identifies the relevant object in the observed environment and the surrounding market response is secondary.

The paper spine is deliberately comparative. Mortensen and Pissarides provide the benchmark search-and-matching closure for unemployment, vacancies, and job creation [@mortensenPissarides1994]. Burdett and Mortensen and Postel-Vinay and Robin show why equilibrium wage dispersion and firm heterogeneity are central in labor markets [@burdettMortensen1998; @postelVinayRobin2002]. Diamond and Hsieh and Moretti show how wages, rents, migration, amenities, and housing supply shape spatial welfare [@diamond2016; @hsiehMoretti2019]. Berry, Levinsohn, and Pakes and Nevo show how demand, pricing, markups, and conduct support market-equilibrium counterfactuals [@berryLevinsohnPakes1995; @nevo2001]. Monte, Redding, and Rossi-Hansberg, Artuc, Chaudhuri, and McLaren, and Caliendo, Dvorkin, and Parro show how equilibrium flows and reallocation matter for commuting, migration, trade, and labor adjustment [@monteReddingRossiHansberg2018; @artucChaudhuriMcLaren2010; @caliendoDvorkinParro2019].

## Core Points

:::{admonition} Core points
:class: important

- Equilibrium structural work is useful when the policy or shock changes the environment faced by many agents, not only the treated agent's choice set.
- Search, spatial, and industry/market models all map latent primitives into endogenous prices, quantities, flows, allocations, and welfare.
- The empirical gain is incidence and welfare analysis under endogenous adjustment; the empirical cost is stronger assumptions, heavier computation, and a higher validation burden.
- A credible equilibrium paper makes the equilibrium margin visible: vacancies, wages, rents, market shares, prices, entry, commuting, migration, or matching.
- Identification requires moments that discipline the primitives that matter for the counterfactual, not only a model that can be solved.
- Counterfactuals should be reported with their distance from observed support, sensitivity to closure assumptions, and fit on targeted and untargeted equilibrium objects.
- Gravity-style structural work belongs here only as a subfamily of spatial or flow equilibrium models, where bilateral frictions map into equilibrium allocations and incidence.
:::

## Bridge

Block 1 trained students to ask what comparison identifies a causal estimand. Lecture 6 added the structural question: what latent preferences, costs, technologies, expectations, dynamic incentives, or welfare objects require a model? Lecture 7 added the estimation question: which likelihood pieces, moments, simulations, weighting choices, and fit diagnostics make the model credible?

Lecture 8 keeps all three habits and adds interaction. Once agents affect each other's environment, the model must specify how the system closes. A job-search policy may change vacancies and market tightness. A local productivity shock may change rents, commuting, and migration. A tax, merger, or technology change may alter firm prices, markups, output, and labor demand. In each case, the object of interest is not only the direct behavioral response. It is the equilibrium allocation that emerges after workers, firms, landlords, consumers, and locations respond together.

This is why equilibrium structural work should be taught as a methods choice rather than as a survey of macro, urban, trade, or industrial-organization models. The transferable lesson is the architecture: name the endogenous equilibrium object, identify the moments that discipline it, solve the counterfactual fixed point, compute welfare or incidence, and make the validation burden explicit.

## Field Core

### A. When Do We Need Equilibrium Structure?

The first question is practical: **what would be wrong with a partial-equilibrium answer?** Equilibrium structure is most useful when at least one of the following is true:

- the policy changes wages, rents, prices, market shares, or vacancies for agents beyond the directly treated group;
- the intervention changes who matches with whom, where workers live or commute, which firms enter, or which products survive;
- welfare depends on incidence through housing costs, markups, congestion, bargaining, or search externalities;
- the counterfactual changes market primitives outside the observed support of a reduced-form design;
- the paper's contribution requires separating primitives from equilibrium outcomes.

A compact way to express the need is:

```{math}
:label: eq:em8-need-equilibrium
\frac{\partial E_i}{\partial a_j} \neq 0
\quad \text{for many } i \neq j,
```

where {math}`a_j` is another agent's action and {math}`E_i` is the environment faced by agent {math}`i`: wages, prices, vacancies, rents, congestion, market shares, or expected matches. When this derivative is economically meaningful, individual optimization alone is incomplete.

The methodological standard is not "equilibrium is realistic." All models are simplifications. The standard is whether the equilibrium closure buys a necessary object. In search, the object may be market tightness and wage incidence. In spatial work, it may be rent capitalization and mobility. In market equilibrium, it may be markups and pass-through. In flow models, it may be bilateral frictions and reallocation. A paper should say why the added closure is essential and where it could fail.

```{include} assets/tables/08-static-vs-dynamic-map.md
```

### B. Search And Matching Equilibrium

Search and matching models are useful when workers and firms meet through a frictional process and the number of vacancies is endogenous. The benchmark is Mortensen and Pissarides: unemployment, vacancies, job creation, job destruction, and wages are jointly determined [@mortensenPissarides1994]. Labor applications extend this logic to wage dispersion, firm heterogeneity, rent sharing, and worker-firm sorting [@burdettMortensen1998; @postelVinayRobin2002].

Let {math}`u` denote unemployed workers, {math}`v` vacancies, and {math}`m(u,v)` a matching function. Market tightness is:

```{math}
:label: eq:em8-tightness
\theta = \frac{v}{u}.
```

The job-finding and vacancy-filling rates are:

```{math}
:label: eq:em8-meeting-rates
f(\theta)=\frac{m(u,v)}{u},
\qquad
q(\theta)=\frac{m(u,v)}{v}.
```

A standard free-entry condition closes the firm side:

```{math}
:label: eq:em8-free-entry
\kappa = q(\theta) J,
```

where {math}`\kappa` is the vacancy posting cost and {math}`J` is the value of a filled job. If vacancy posting becomes more profitable, entry raises {math}`v`, changes {math}`\theta`, and alters both job-finding and vacancy-filling rates.

Wages are often pinned down by surplus sharing. If {math}`S=J+W-U` is total match surplus, {math}`W` is the worker value of employment, {math}`U` is the worker value of unemployment, and {math}`\beta` is the worker's bargaining weight, a Nash-style condition implies:

```{math}
:label: eq:em8-surplus-sharing
W-U = \beta S,
\qquad
J=(1-\beta)S.
```

This is not just theory notation. It says what the model can identify and what it assumes. Transitions into jobs discipline job-finding rates. Vacancy duration or vacancy stocks discipline vacancy-filling rates. Wages discipline surplus division only if the researcher has a credible wage-setting structure. Separations discipline job destruction. Policy variation may help identify how benefits, taxes, minimum wages, or hiring subsidies change tightness and surplus.

The empirical gain is clear: the researcher can ask how a policy changes unemployment, vacancies, wages, and welfare after firms respond. The risk is equally clear: the matching technology, bargaining rule, vacancy cost, separation process, and worker heterogeneity can carry a great deal of identifying weight. A credible paper reports which moments discipline each object and shows fit for transitions, wages, vacancies, and separations, not only one headline counterfactual.

### C. Spatial Equilibrium

Spatial equilibrium models are useful when workers choose where to live, work, commute, or migrate, and when wages, rents, amenities, and local prices adjust. Diamond studies how workers with different skill levels sort across places and how wages, rents, and amenities affect welfare [@diamond2016]. Hsieh and Moretti use a spatial equilibrium counterfactual to show how housing constraints in high-productivity cities can generate misallocation [@hsiehMoretti2019]. Monte, Redding, and Rossi-Hansberg show how commuting and migration create local employment elasticities through flow equilibrium [@monteReddingRossiHansberg2018].

A minimal indirect-utility object for worker {math}`i` in location {math}`j` is:

```{math}
:label: eq:em8-location-utility
V_{ij}
=
w_j
- r_j
- \tau_{ij}
+ A_j
+ \varepsilon_{ij},
```

where {math}`w_j` is the wage or employment opportunity, {math}`r_j` is housing cost, {math}`\tau_{ij}` is commuting or migration cost, {math}`A_j` is amenity value, and {math}`\varepsilon_{ij}` is an idiosyncratic preference shock. With logit-style shocks, location or commuting shares take the familiar form:

```{math}
:label: eq:em8-location-choice
s_{ij}
=
\frac{\exp(V_{ij}/\sigma)}
{\sum_{\ell}\exp(V_{i\ell}/\sigma)}.
```

Equilibrium then requires population, employment, housing, and wages to be mutually consistent. A stylized market-clearing condition is:

```{math}
:label: eq:em8-spatial-clearing
N_j(w,r,A,\tau)
=
H_j(r_j;\eta_j),
\qquad
L_j(w,r,A,\tau)=D_j(w_j,Z_j),
```

where {math}`H_j` is housing supply and {math}`D_j` is local labor demand. Housing incidence can be summarized by:

```{math}
:label: eq:em8-housing-incidence
dV_j
=
dw_j - dr_j + dA_j - d\tau_j,
\qquad
dr_j
=
\frac{1}{\eta_j} dN_j
\text{local supply shifters}.
```

The key applied lesson is that wage effects are not welfare effects. A productivity shock can raise wages in a city but also raise rents. A place-based policy can benefit landowners more than workers if housing supply is inelastic. A transit improvement can change welfare through commuting costs and location choice even if local wages barely move.

The identification burden follows the object. Wages alone cannot identify amenity values. Rents alone cannot identify productivity. Migration or commuting flows help discipline mobility frictions, but the interpretation depends on how the model treats preferences, moving costs, housing supply, and local labor demand. A credible spatial equilibrium paper reports fit for wages, rents, population or employment, and flows, and it explains which counterfactual margins are close to observed variation.

#### Gravity-Style Flow Models

Gravity-style models fit inside this lecture only as a subfamily of spatial or flow equilibrium work. They are useful when the empirical object is a bilateral flow: trade, commuting, migration, applications, referrals, or worker allocation. They recover friction-like objects that help map origin-destination characteristics into equilibrium flows. They should not dominate the lecture because the central methods issue is broader: when endogenous flows and prices change incidence.

A simple gravity-style object is:

```{math}
:label: eq:em8-gravity
M_{ij}
=
A_i B_j \tau_{ij}^{-\sigma},
```

where {math}`M_{ij}` is a bilateral flow, {math}`\tau_{ij}` is a bilateral friction, and {math}`A_i` and {math}`B_j` are origin and destination terms that often absorb market size, productivity, or multilateral resistance. In labor applications, the first diagnostic question is substantive: are these flows workers, commuters, job applications, migrants, or traded goods that shift labor demand? The second is structural: does the model only describe flows, or does it close the equilibrium with wages, rents, prices, or employment?

### D. Industry And Market Equilibrium

Industry and market equilibrium models are useful when firms set prices, quantities, quality, wages, or product menus strategically, and when labor outcomes depend on those choices. Berry, Levinsohn, and Pakes and Nevo are the canonical differentiated-product examples because demand, marginal cost, markups, ownership, and counterfactual pricing must be solved jointly [@berryLevinsohnPakes1995; @nevo2001]. Labor students do not need to become IO specialists to learn the transferable method: estimate demand and supply primitives, recover markups or conduct, and simulate policy under equilibrium pricing.

Let product or firm {math}`j` have demand:

```{math}
:label: eq:em8-demand
q_j
=
D_j(p,x,\xi;\theta_d),
```

where {math}`p` is the vector of prices, {math}`x` observed characteristics, {math}`\xi` unobserved quality or demand, and {math}`\theta_d` demand parameters. A simple pricing first-order condition for a single-product firm is:

```{math}
:label: eq:em8-pricing-foc
p_j - mc_j
=
-\left(\frac{\partial D_j(p,x,\xi;\theta_d)}{\partial p_j}\right)^{-1}
\;D_j(p,x,\xi;\theta_d),
```

or, in elasticity form:

```{math}
:label: eq:em8-markup
\frac{p_j-mc_j}{p_j}
=
-\frac{1}{\varepsilon_{jj}}.
```

The equilibrium mapping can be written as:

```{math}
:label: eq:em8-market-map
(p^\ast,q^\ast,L^\ast)
=
\Psi(\theta_d,\theta_c,\Omega,Z),
```

where {math}`\theta_c` are cost or production primitives, {math}`\Omega` is ownership or conduct, {math}`Z` are market shifters and instruments, and {math}`L^\ast` is labor demand or employment implied by output and technology.

The labor-economics relevance is broad. Market power can affect wages through product-market rents, monopsony-like wage setting, pass-through, platform pricing, technology adoption, or merger-induced reallocation. The equilibrium model is useful when the policy changes the pricing or conduct environment rather than only one worker's treatment status.

The validation burden is high. Demand estimates require credible price variation or instruments. Cost recovery depends on the conduct assumption. Labor incidence depends on how labor enters cost, production, or bargaining. A counterfactual merger, tax, subsidy, or technology shock is persuasive only if substitution patterns, price-cost implications, and pass-through are believable.

### E. Policy Counterfactuals And Welfare In Equilibrium

The core appeal of equilibrium structural work is the ability to simulate counterfactuals when incidence is endogenous. Let {math}`\tau` denote a policy: unemployment insurance, a vacancy subsidy, a housing deregulation, a transit improvement, a minimum wage, a tax, a merger, a tariff, or a training subsidy that affects markets. Let {math}`x` collect equilibrium objects: wages, vacancies, prices, rents, employment, market shares, entry, commuting flows, or migration.

An equilibrium counterfactual is a fixed point:

```{math}
:label: eq:em8-fixed-point
x^\ast(\tau)
=
\Phi(x^\ast(\tau),\tau;\theta).
```

The model may have one equilibrium, multiple equilibria, or no stable equilibrium under some policies. A careful paper therefore distinguishes a fixed point from an equilibrium selection rule and reports whether the counterfactual is robust to starting values, numerical tolerances, or alternative closures.

The welfare object depends on the equilibrium allocation:

```{math}
:label: eq:em8-welfare
W(\tau)
=
\sum_i \omega_i U_i(x^\ast(\tau),\tau;\theta)
+
\sum_f \Pi_f(x^\ast(\tau),\tau;\theta)
+
R(x^\ast(\tau),\tau),
```

where {math}`\omega_i` are distributional weights, {math}`U_i` worker or household welfare, {math}`\Pi_f` firm profits, and {math}`R` government revenue, landowner surplus, or other fiscal/resource terms. The counterfactual effect is:

```{math}
:label: eq:em8-welfare-change
\Delta W
=
W(\tau_1)-W(\tau_0).
```

The interpretive question is not only whether {math}`\Delta W` is positive. It is whose welfare is counted, how prices and rents redistribute surplus, how transition costs are handled, whether welfare is static or dynamic, and whether unmodeled margins would move under the policy.

This is where Hsieh and Moretti are especially useful as a teaching anchor. The paper's central object is an equilibrium counterfactual: how much aggregate output is lost when housing constraints prevent workers from moving to high-productivity cities [@hsiehMoretti2019]. A reduced-form local wage effect would not recover that object because the policy changes population, rents, productivity allocation, and aggregate output jointly.

### F. Estimation, Computation, And Identification Burdens

Equilibrium adds a layer to the estimation problem. The researcher must estimate primitives and solve equilibrium objects at each parameter vector or counterfactual policy. In practice, four computational approaches appear often.

**Nested fixed point.** The outer loop searches over parameters, while the inner loop solves the equilibrium or dynamic model. This is conceptually clean and close to the logic of Rust-style structural estimation, but it can be slow when the equilibrium problem is large [@rust1987optimal].

**MPEC intuition.** Mathematical programming with equilibrium constraints puts parameters and equilibrium variables in one constrained optimization problem. The attraction is that equilibrium conditions are imposed directly. The risk is that the optimization problem can be numerically delicate, and students must still understand the economics of the constraints.

**Calibration-estimation hybrids.** Some parameters are estimated from moments, some are calibrated from external evidence, and some are normalized for closure. This can be honest and useful when data are limited, but the paper must report which counterfactual conclusions depend on calibrated values.

**Equilibrium simulation.** Many equilibrium counterfactuals require simulating market response after changing policy. Simulation makes heterogeneous agents, markets, or locations tractable, but it adds approximation error, seed dependence, and sensitivity to the equilibrium algorithm.

The identification question should be written as a map:

```{math}
:label: eq:em8-identification-map
\widehat m^{data}
=
\left[
\text{choices},
\text{transitions},
\text{prices},
\text{flows},
\text{shares},
\text{wages},
\text{rents},
\text{entry}
\right]
\quad \Longleftrightarrow \quad
m^{model}(\theta,x^\ast(\theta)).
```

Weak equilibrium papers hide which parameters are identified by which moments. Strong papers make this visible. They explain which moments discipline preferences, frictions, costs, conduct, housing supply, matching, or mobility, and which objects are closure assumptions. They also report fit on equilibrium variables not mechanically targeted by the estimator.

```{include} assets/tables/08-theory-to-applied-bridge.md
```

### G. What Can Go Wrong Empirically?

Equilibrium structure can fail in predictable ways.

First, the model may identify the headline result through closure rather than variation. If a housing-supply elasticity, bargaining weight, matching elasticity, or conduct parameter is calibrated and the welfare result moves with that number, the paper needs sensitivity analysis.

Second, the equilibrium margin may be wrong. A model of migration may miss commuting. A model of wage bargaining may miss amenities or nonwage compensation. A model of product-market pricing may miss labor-market frictions. A model of trade flows may miss local housing incidence.

Third, the counterfactual may move too far from support. Small policy changes near observed variation are easier to trust than reforms that change the whole equilibrium environment.

Fourth, the model may fit targeted moments while failing untargeted ones. Search papers should show more than unemployment. Spatial papers should show more than wages. Market-equilibrium papers should show more than market shares. Flow models should show more than aggregate flows.

Finally, computation may create false precision. Local minima, multiple equilibria, weak convergence, simulation noise, and sensitivity to starting values can all masquerade as economic results. The empirical standard is to report the numerical problem in enough detail that readers can see where the counterfactual comes from.

```{include} assets/tables/08-structural-estimation-diagnostics.md
```

## Research Lab

The Week 8 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. The primary anchor is Hsieh and Moretti because the paper contains a real spatial-equilibrium counterfactual: relaxing housing constraints in high-productivity places changes population allocation, rents, output, and welfare [@hsiehMoretti2019]. The challenge/extension anchor is Berry, Levinsohn, and Pakes with Nevo because market-equilibrium counterfactuals rely on a different equilibrium domain: product demand, pricing, markups, and pass-through [@berryLevinsohnPakes1995; @nevo2001].

### Reproduce

Students work with a small synthetic city panel inspired by the Hsieh-Moretti logic. The script computes baseline wages, rents, housing constraints, population allocation, output, and welfare. It then runs a housing-supply counterfactual that relaxes constraints in high-productivity cities and solves a simple spatial-equilibrium update.

The goal is to reproduce the **logic** of a spatial equilibrium counterfactual:

- wages alone are not welfare;
- rents absorb part of local productivity gains;
- housing constraints limit reallocation;
- aggregate output changes when workers cannot move to productive places.

### Diagnose

Students diagnose the equilibrium assumptions rather than treating the output table as truth. They inspect which moments are observed in the synthetic data, which objects are inferred by closure, and how sensitive the counterfactual is to housing-supply elasticity, mobility elasticity, and productivity dispersion.

The required memo asks:

- which equilibrium object is most important for the result;
- whether the housing-supply parameter is identified or calibrated in the teaching path;
- how the welfare result changes under alternative mobility elasticities;
- which untargeted facts would be needed in a publishable paper;
- where a reduced-form design would stop.

### Transfer

Students transfer the equilibrium logic to a market-equilibrium setting. The transfer script uses synthetic differentiated-product market data to estimate a compact demand curve, recover markups under a pricing rule, and simulate a marginal-cost shock. This is a BLP/Nevo-style teaching path, not a BLP replication. The point is to compare equilibrium domains: in spatial work, incidence runs through wages, rents, and mobility; in market equilibrium, incidence runs through demand elasticities, markups, prices, and quantities.

Minimum student deliverables are:

1. one Reproduce paragraph describing the spatial counterfactual and its welfare object;
2. one Diagnose paragraph naming the identifying moments and the closure assumptions;
3. one Transfer paragraph comparing spatial incidence with market-equilibrium pass-through;
4. one final sentence saying when equilibrium structure was worth the extra assumptions.

## Methods Box

:::{admonition} Equilibrium structural checklist
:class: note

1. **Name the equilibrium margin.** Is it tightness, wages, rents, prices, market shares, entry, commuting, migration, or bilateral flows?
2. **Name the primitive.** Is the latent object a preference, friction, cost, conduct parameter, matching technology, housing elasticity, mobility cost, or productivity shifter?
3. **Name the moment.** Which observed variation disciplines the primitive: transitions, vacancies, wages, rents, flows, prices, shares, entry, or policy variation?
4. **Name the counterfactual gain.** What can the equilibrium model answer that a reduced-form or partial-equilibrium design cannot?
5. **Name the closure assumptions.** Which pieces are estimated, calibrated, normalized, or borrowed from external evidence?
6. **Validate fit.** Show targeted and untargeted equilibrium objects, sensitivity to key closures, and distance from support.
7. **Report computation.** State the fixed point, solver, tolerances, starting values, convergence behavior, and simulation uncertainty.
:::

## Reading Ladder And References

```{include} assets/tables/08-reading-architecture.md
```

**First pass: why equilibrium enters.** Read Mortensen and Pissarides for the benchmark search closure and Hsieh and Moretti for a spatial-equilibrium counterfactual where partial equilibrium misses the target object [@mortensenPissarides1994; @hsiehMoretti2019].

**Second pass: compare equilibrium domains.** Read Diamond for location choice and spatial welfare, Berry, Levinsohn, and Pakes for market-equilibrium pricing, and Nevo for measuring market power in a differentiated-product setting [@diamond2016; @berryLevinsohnPakes1995; @nevo2001].

**Third pass: flows and labor adjustment.** Read Monte, Redding, and Rossi-Hansberg for commuting and migration, Artuc, Chaudhuri, and McLaren for trade shocks and labor adjustment, and Caliendo, Dvorkin, and Parro for general-equilibrium trade and labor dynamics [@monteReddingRossiHansberg2018; @artucChaudhuriMcLaren2010; @caliendoDvorkinParro2019].

**Reference shelf.** Keep Rust and Lecture 7 nearby as a reminder that equilibrium estimation still requires the same chain: identification, estimation, fit, counterfactual discipline, and inference [@rust1987optimal].

## Exercises And Discussion Prompts

1. Give one applied question where a partial-equilibrium treatment effect is probably enough and one where equilibrium structure is essential. Name the equilibrium margin in the second example.
2. In a search model, what moments would discipline the matching function, vacancy cost, separation process, and wage-setting rule? Which of these would be hardest to defend empirically?
3. In a spatial model, explain why a local wage increase is not automatically a welfare gain. What data would help separate productivity, amenities, housing supply, and mobility frictions?
4. In an industry-equilibrium model, explain how demand elasticities and conduct assumptions shape pass-through to workers or consumers.
5. Write the fixed point for a policy counterfactual in one domain: search, spatial, market equilibrium, or flow/gravity. What would multiple equilibria or nonconvergence mean substantively?
6. Choose one equilibrium paper from the reading ladder. Write a referee-style paragraph identifying the strongest validation evidence and the most important assumption.
7. When does a gravity-style model belong in a labor-economics methods lecture? Give one example where it clarifies the object and one where it would distract from the main question.

## Reproducibility And Code Lab Note

The canonical Lecture 8 lab folder is:

```text
labs/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals/
```

The lab is a bounded teaching path. It creates deterministic synthetic data, computes a Hsieh-Moretti-style spatial-equilibrium counterfactual, diagnoses sensitivity to housing and mobility assumptions, and transfers the logic to a compact BLP/Nevo-style market-equilibrium pass-through exercise. It does not claim to reproduce the published magnitudes in any paper and does not invent an official replication package.

The smoke path runs:

```bash
ENV_NAME=research bash smoke.sh
```

Expected outputs include reproduced spatial counterfactual tables, sensitivity diagnostics, a spatial incidence figure, market-equilibrium transfer tables, and a pass-through figure.

## Slide Companion Note

The Week 8 slide deck should not duplicate the chapter. It should define the capstone question, show when equilibrium structure is necessary, compare search, spatial, and industry/market equilibrium in parallel, isolate policy counterfactuals and welfare, summarize computation and identification burdens, include a concise gravity-style note, and end with the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is `slides/week8/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.tex`.

## Bridge Forward

Block 2 ends here. The next block turns to machine learning for applied economics. The connection is closer than it may first appear. Machine learning can help predict, measure, and flexibly model heterogeneity, but it does not by itself define an estimand, identify a causal effect, or solve an equilibrium counterfactual. The Block 2 discipline remains useful: name the object, state the assumptions, connect the method to observed variation, validate the output, and be explicit about what the counterfactual requires.
