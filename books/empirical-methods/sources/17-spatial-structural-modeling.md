# Lecture 17. Spatial Structural Modeling

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when a reduced-form spatial design is not enough and a spatial equilibrium model becomes necessary;
2. map an applied spatial question into equilibrium objects such as wages, rents, commuting costs, migration costs, local productivity, amenities, and housing supply;
3. distinguish static from dynamic quantitative spatial models;
4. understand how gravity-style blocks fit inside broader spatial structural work;
5. evaluate identification, calibration, fit, and policy-counterfactual claims in spatial models;
6. summarize where the spatial-methods literature is now and where the most promising opportunities lie.

## Opening Orientation

This is the final lecture in the spatial-methods block. Lecture 15 focused on constructing spatial empirical objects; Lecture 16 focused on identification with space. Lecture 17 asks what to do when the object of interest is itself an equilibrium outcome: a city, region, commuting system, or migration market in which workers, firms, rents, amenities, and policies all interact. The point is not to promote structure for its own sake. The point is to show when a serious applied question cannot be answered with partial-equilibrium evidence alone.

```{admonition} Core points
:class: important
- Spatial structural models become useful when policy or shocks reallocate workers, firms, rents, commuting flows, or amenities across places, so reduced-form treatment effects no longer answer the full research question.
- The key objects are not only employment or wages, but also rents, migration, commuting, location choice, market access, welfare, and incidence.
- Gravity-style structures for trade, commuting, and migration are often tractable building blocks inside broader spatial equilibrium models, not a separate universe.
- Good spatial structural work is persuasive only when readers can see what is identified, what is calibrated, what is imposed, how fit is assessed, and which counterfactual margins the model is being trusted to extrapolate.
```

## Bridge

The previous two lectures emphasized a discipline: first define space carefully, then identify causal effects credibly. Structural spatial work does not replace those lessons. It builds on them. Once the estimand becomes an equilibrium object—such as city-level incidence, commuting adjustment, or the welfare consequences of housing reform—the key question is how individual decisions aggregate through prices and quantities across locations [@monteReddingRossiHansberg2018; @hsiehMoretti2019].

## Field Core

### 1. When is reduced-form evidence not enough?

A reduced-form design can tell us whether one place or boundary changed relative to another. But many place-based policies and shocks affect several margins at once:
- wages,
- rents,
- migration,
- commuting,
- firm entry,
- local amenities,
- and housing quantities.

A reduced-form estimate of, say, the effect of a housing reform on local wages is not enough if the substantive question is who captured the gains, whether workers relocated, or whether the policy changed welfare through rents as much as through wages [@hsiehMoretti2019]. Similarly, a local labor-demand shock can be absorbed through commuting or migration rather than only by workers already living in the treated place [@monteReddingRossiHansberg2018].

A useful rule is:

```{math}
:label: eq:spatial-not-enough
\text{Need structure when } Y_{it}(d) \text{ is not the policy object, but rather } \mathcal{E}(d),
```

where {math}`\mathcal{E}(d)` is an equilibrium object such as a vector of wages, rents, commuting flows, location choices, and welfare under policy or shock {math}`d`.

### 2. Core equilibrium objects

A standard spatial-equilibrium lecture should make clear what the model is trying to recover.

#### Worker-side utility

```{math}
:label: eq:spatial-worker-utility
U_{ij} = w_j - r_j - \tau_{ij} + a_j + \varepsilon_{ij},
```

where {math}`w_j` is the wage in location/job market {math}`j`, {math}`r_j` is the cost of housing or local prices, {math}`\tau_{ij}` is the migration or commuting cost from worker location {math}`i`, {math}`a_j` is amenity value, and {math}`\varepsilon_{ij}` captures idiosyncratic taste.

This equation makes the lecture’s central point: a nominal wage is not the welfare object.

#### Choice probabilities and flows

If the idiosyncratic term is extreme value, a standard logit choice probability is

```{math}
:label: eq:spatial-choice-prob
P_{ij} = \frac{\exp(V_{ij})}{\sum_{k}\exp(V_{ik})},
\quad \text{where} \quad
V_{ij}=w_j-r_j-\tau_{ij}+a_j.
```

That same logic underlies many migration, commuting, and gravity-style models.

#### Labor demand / productivity side

A location or workplace labor-demand block often takes the form

```{math}
:label: eq:spatial-labor-demand
L_j^d = L_j^d(w_j, A_j, X_j),
```

where {math}`A_j` captures local productivity or market access, and {math}`X_j` may include sectoral composition, trade access, or local demand shifters.

#### Housing or land-supply side

```{math}
:label: eq:housing-supply
H_j^s = H_j^s(r_j, Z_j),
```

where {math}`Z_j` captures supply constraints, regulation, or geography.

#### Equilibrium

In equilibrium, workers, firms, and housing markets must clear jointly. A convenient abstract representation is

```{math}
:label: eq:spatial-equilibrium
\mathcal{E}(\theta) = \left\{ P_{ij}(\theta), w_j(\theta), r_j(\theta), L_j(\theta), H_j(\theta) \right\}_{i,j}
```

for parameter vector {math}`\theta`, where {math}`\theta` includes productivity, amenities, moving costs, commuting frictions, and supply elasticities.

### 3. Static vs dynamic quantitative spatial models

A big practical distinction is whether the research question is essentially static or intrinsically dynamic.

#### Static models
Best when the question is:
- incidence at a point in time,
- comparative statics across places,
- long-run equilibria,
- welfare decomposition under a counterfactual.

Examples include many housing, commuting, and place-incidence models [@hsiehMoretti2019; @ahlfeldtReddingSturmWolf2015].

#### Dynamic models
Needed when the question depends on:
- transition paths,
- adjustment lags,
- capital or housing dynamics,
- aging, tenure choice, or forward-looking migration,
- policy timing.

Recent dynamic urban/spatial work shows why transition dynamics can matter a great deal, especially when migration and housing choices are forward-looking [@GreaneyParkhomenkoVanNieuwerburgh2025].

### 4. Gravity-style blocks as a spatial structural family

Gravity-style models belong in this lecture, but as a subfamily.

Their appeal is that many bilateral flows—trade, commuting, migration—can be written in forms like

```{math}
:label: eq:gravity
X_{ij} = \frac{A_i B_j}{\Phi_{ij}^{\kappa}},
```

or in log-linearized variants, where {math}`\Phi_{ij}` is a bilateral cost (distance, time, frictions), and {math}`\kappa` is the trade/flow-cost elasticity.

In practice, gravity blocks are useful because they:
- discipline bilateral flows,
- connect data on commuting or migration to structural frictions,
- create a tractable bridge between reduced-form spatial patterns and equilibrium objects.

But they are usually not enough alone. They must sit inside a broader model of wages, rents, amenities, housing, and labor demand if the research question concerns full spatial incidence or welfare [@monteReddingRossiHansberg2018].

### 5. Identification, calibration, estimation, and fit

Spatial models often combine several empirical strategies.

#### Identification
The first discipline is mapping each parameter to empirical variation:
- commuting or migration flows for frictions,
- wages/rents for productivity and amenities,
- housing quantities/prices for supply elasticities,
- bilateral costs for network structure.

#### Calibration vs estimation
Some spatial papers calibrate elasticities and recover the remaining objects; others estimate more of the model directly. The research question should drive the choice. Calibrating too much weakens discipline; estimating everything may be impossible with available variation.

#### Fit
A persuasive paper shows:
- what moments or objects are targeted,
- which moments are not targeted,
- and whether the untargeted margins are at least qualitatively consistent.

#### Counterfactual credibility
Spatial counterfactuals are attractive because they directly speak to policy, but they are fragile. The model may be very informative about nearby interventions and much less informative about large reforms that change market access, supply, or sorting in ways not seen in the data.

```{admonition} Methods Box
:class: note
**How to read a spatial structural paper**
1. What is the equilibrium object of interest: incidence, migration, commuting, rent pass-through, welfare, or aggregate output?
2. Which parameters are recovered from data and which are calibrated?
3. What moments identify moving costs, local productivity, amenities, or housing supply?
4. What would the paper’s main claim look like in reduced-form language?
5. How far outside observed support does the key counterfactual go?
6. What margins are allowed to adjust, and which are fixed by assumption?
```

### 6. Research architecture for spatial structural work

A clean applied spatial structural project usually follows this sequence:

1. **Reduced-form fact or estimand**  
   Example: a local labor-demand shock changes commuting more than migration.

2. **Economic mechanism**  
   Hypothesis: commuting frictions are lower than migration frictions for the relevant workers.

3. **Structural object**  
   Need to recover commuting costs, migration costs, and perhaps housing supply elasticity.

4. **Model**  
   Minimal equilibrium structure linking those objects to bilateral flows, wages, and housing prices.

5. **Counterfactual**  
   Policy, shock, or infrastructure change altering one of those frictions.

6. **Welfare/incidence interpretation**  
   Which workers, firms, landlords, or commuters gain?

This is the part students often miss: the model is not the contribution by itself. The contribution is the connection between the reduced-form fact, the structural object, and the policy counterfactual.

### 7. Spatial methods block summary: where the literature is now and what comes next

This is the final lecture of the spatial block, so students should leave with a clear map.

#### What the block has done
- **Lecture 15**: how spatial data become empirical objects.
- **Lecture 16**: how to identify causal effects with spatial variation.
- **Lecture 17**: when equilibrium reasoning is necessary.

#### Where the literature is now
Current frontier spatial work is increasingly:
- integrating commuting, migration, and housing jointly,
- modeling dynamic transitions rather than only long-run equilibria,
- connecting spatial models to labor-market power, local inequality, and remote work,
- using richer bilateral data and high-frequency mobility data,
- confronting equilibrium multiplicity and computational tractability more directly [@Redding2024; @AllenArkolakisLi2024; @GreaneyParkhomenkoVanNieuwerburgh2025].

#### Future opportunities
Promising directions include:
- remote work and hybrid commuting in spatial equilibrium,
- climate adaptation, insurance, and relocation,
- labor-market power and monopsony in space,
- neighborhood-level spatial equilibrium with heterogeneous workers,
- supply constraints and local employment composition,
- combining structural spatial models with rich administrative worker-firm data,
- integrating platform / transportation data with labor allocation.

The lesson is not “every spatial project should be structural.” The lesson is that students should know when reduced-form evidence answers the question and when equilibrium modeling becomes essential.

## Research Lab

### Primary anchor paper
A natural primary anchor is Monte, Redding, and Rossi-Hansberg (2018) [@monteReddingRossiHansberg2018]. It is excellent for teaching:
- bilateral commuting and migration data,
- equilibrium labor-demand incidence,
- structural interpretation of local employment elasticities,
- and policy/shock counterfactual logic.

### Reproduce
Reproduce one core object:
- a bilateral commuting/migration flow relationship,
- or a local employment/incidence decomposition implied by commuting openness.

### Diagnose
Students should then diagnose:
- which object is actually identified by the reduced-form variation,
- what commuting and migration margins are assumed or imposed,
- how the bilateral data do the work,
- and which counterfactual claims depend heavily on equilibrium structure.

### Transfer
A good bounded transfer exercise is to take the logic to a nearby setting:
- a housing-constrained labor-market incidence question inspired by [@hsiehMoretti2019],
- or a dynamic urban setting inspired by [@GreaneyParkhomenkoVanNieuwerburgh2025].

The point is not to fully replicate a large model, but to understand how a reduced-form spatial fact becomes a structural equilibrium claim.

## Reading Ladder And References

### Core theory and method
- [@monteReddingRossiHansberg2018]
- [@hsiehMoretti2019]
- [@Redding2024]

### Canonical applied structural examples
- [@ahlfeldtReddingSturmWolf2015]
- [@AllenArkolakis2014]

### Frontier / dynamic / equilibrium properties
- [@AllenArkolakisLi2024]
- [@GreaneyParkhomenkoVanNieuwerburgh2025]

## Exercises And Discussion Prompts

1. A place-based policy changes employment in treated regions. When is a reduced-form estimate enough, and when do you need a spatial equilibrium model?
2. In a housing-constrained economy, why can a high nominal wage be a poor welfare measure?
3. What does a gravity block identify well, and what does it miss?
4. What is the weakest assumption you could make and still answer your preferred spatial policy question?
5. Name one frontier spatial question where dynamic structure is essential and one where it is likely unnecessary.

## Reproducibility And Code Lab Note

The lab should not try to rebuild a full quantitative spatial equilibrium model from scratch unless a transparent reduced teaching path is available. A bounded teaching path is preferable:
- reproduce one bilateral-flow or local-incidence object,
- diagnose the equilibrium logic,
- and transfer it to a nearby setting with reduced or synthetic data.

## Slide Companion Note

The slide deck should emphasize:
1. the equilibrium map,
2. when reduced-form fails,
3. gravity as a building block,
4. static vs dynamic structure,
5. the spatial-block summary,
6. the Reproduce → Diagnose → Transfer lab logic.

## Bridge Forward

This completes the spatial methods block. Students should now be able to tell the difference between:
- building a spatial dataset,
- identifying a causal spatial effect,
- and modeling the equilibrium environment in which that effect propagates.

That distinction is the core methodological payoff of the block.
