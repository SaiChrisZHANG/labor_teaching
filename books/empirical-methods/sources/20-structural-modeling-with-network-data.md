---
title: "Structural Modeling with Network Data"
bibliography:
  - references.bib
---

# Structural Modeling with Network Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. Explain when a reduced-form network design is not enough and a structural network model becomes useful.
2. Distinguish between models of **behavior on networks** and models of **network formation**.
3. Write down the core objects in structural peer-effects, referral, diffusion, and formation models.
4. Diagnose what variation identifies structural network primitives and what assumptions do the work.
5. Evaluate the credibility of counterfactuals that change links, information flows, or matching opportunities.
6. Place current structural network research within the broader Network Methods block and identify frontier opportunities.

## Opening Orientation

Lecture 18 treated network data as an empirical object. Lecture 19 treated network dependence as an identification problem. Lecture 20 asks what happens when the research question itself is about how relationships form, persist, and mediate economic behavior. In these settings, reduced-form designs often recover local causal objects but cannot answer counterfactual questions about changing the **network itself**, the **flow of information**, or the **matching process**.

The lecture is therefore about when a network model is worth the additional assumptions. The answer is not “always.” Structural network work is useful when the policy changes links, information, search, diffusion, or assignment opportunities in ways that push the researcher outside the support of observed reduced-form variation.

```{admonition} Core points
:class: important
- Structural network models are useful when policies or shocks change **relationships**, not just individual treatment status.
- The key distinction is between **behavior on a network** and **formation of the network itself**.
- Identification is difficult because links are often endogenous, strategic, and jointly determined with outcomes.
- Counterfactuals about referrals, peer groups, search connections, ranking systems, or information diffusion usually require stronger assumptions than reduced-form network designs.
- Good structural network work must make the assumptions, equilibrium logic, and validation strategy unusually transparent.
```

## Bridge

The logic of the Network Methods block is cumulative.

- Lecture 18: what a network is, how it is measured, and why node/edge definitions are economic choices.
- Lecture 19: how dependence, spillovers, and exposure mappings alter causal identification.
- Lecture 20: how to model network-mediated behavior or formation when the goal is to simulate counterfactual changes in links, information, and matching.

This lecture therefore does not replace the earlier reduced-form material. It asks when researchers need more structure because the policy or institution of interest changes the network itself.

## Field Core

### Why structure in network settings?

The canonical reasons are familiar from the earlier structural block, but the network setting makes them sharper.

A network model is useful when the applied question asks about:

- a policy that changes referral links or information flows;
- a platform or institution that changes who can connect to whom;
- an intervention that affects equilibrium peer groups or learning paths;
- a labor-market design that changes matching opportunities through network access;
- a change in incentives that alters link formation, not only outcomes conditional on links.

In these environments, the researcher often wants an object like:

```{math}
:label: eq:network_policy_value
V(p) = \mathbb{E}\big[ W_i(G(p), a_i(G(p), X, \varepsilon), X ) \big],
```

where policy {math}`p` changes the network {math}`G(p)`, which in turn changes actions {math}`a_i(\cdot)` and welfare {math}`W_i`. A reduced-form estimate of the effect of exposure on outcome usually does not identify this object unless the network is fixed and policy-invariant.

### Behavior on networks

A basic structural peer-effects model starts from an action equation:

```{math}
:label: eq:network_peer_effects
a_i = \alpha + \beta x_i + \gamma \sum_j g_{ij} a_j + \delta \sum_j g_{ij} x_j + \varepsilon_i,
```

where {math}`g_{ij}` describes the relevant link or normalized exposure weight. The parameter {math}`\gamma` captures endogenous peer effects and {math}`\delta` contextual effects.

The problem is not writing down such a model. The problem is that {math}`g_{ij}` is usually not random, and the outcomes of peers are themselves jointly determined. This is why structural work in networks often has to make explicit assumptions about equilibrium behavior, timing, and information.

### Network formation

A simple latent-utility representation for link formation is:

```{math}
:label: eq:link_utility
g_{ij} = \mathbf{1}\{ U_{ij}(X_i, X_j, G_{-ij}, \eta_{ij}) \ge 0 \},
```

where utility from linking depends on observables, unobservables, and existing network structure. In strategic formation models, links are not independent dyadic draws because transitivity, clustering, congestion, or indirect links matter for payoffs.

This is where the literature on degree heterogeneity, homophily, and strategic formation enters. The same data can support very different counterfactuals depending on whether one interprets observed links as:

- exogenous contact opportunities,
- equilibrium best responses,
- outcomes of repeated search,
- or institutional rules that govern who meets whom.

### Labor applications: referrals, search, matching, diffusion

For labor economists, structural network modeling is most compelling when it connects to concrete labor institutions.

#### Referral and job-search networks

Referral networks are a natural case because links transmit information, shape access to vacancies, and can alter both match quality and inequality. In a search-and-referral model, the value of a worker’s network depends on who learns about vacancies and how referral signals affect employer beliefs.

This is one reason labor applications are attractive pedagogically: the structural assumptions are economically interpretable. A link is not just a graph edge; it is a channel for vacancy information, screening, trust, or reputation.

#### Matching and assignment on networks

Some labor markets are effectively constrained matching systems because workers only observe or can reach a subset of jobs through institutional or social links. Structural network models can then be used to ask:

- what happens if certain links are subsidized or removed?
- how much inequality is driven by network segregation?
- does improving information flow raise total surplus or mostly redistribute opportunities?

#### Diffusion and workplace learning

A third family studies how information, norms, or technologies diffuse through coworkers, managers, or firms. These models matter when the policy changes communication or exposure networks rather than simply individual incentives.

### Identification and what actually identifies the model

The central question is always: what variation disciplines the primitives?

Potential sources include:

- panel evolution of links and outcomes;
- quasi-random shocks to meeting opportunities;
- institutional rules that constrain assignment or referrals;
- experiments that alter information flow or contact structure;
- dyadic or bipartite administrative data with repeated decisions;
- equilibrium restrictions plus rich moments from network topology.

A useful decomposition is:

```{math}
:label: eq:network_moments
m(\theta) = \mathbb{E}_\theta \big[
\text{degree},\,
\text{clustering},\,
\text{homophily},\,
\text{wage covariance across links},\,
\text{transition rates},\,
\text{referral yields}
\big].
```

The choice of moments is not just computational. It is substantive. If the counterfactual concerns diffusion, moments on clustering and path length may matter. If the counterfactual concerns inequality in job access, moments on segregation, degree heterogeneity, or referral productivity are more relevant.

### Computation, equilibrium, and counterfactuals

Structural network models are often hard because the network itself is high-dimensional and equilibrium objects are path dependent or strategic. Researchers therefore simplify:

- sparse or dyadic approximations,
- equilibrium restrictions on local statistics,
- simulation-based estimation,
- or partial-equilibrium network environments with reduced-form formation rules.

That is acceptable if the simplification is aligned with the applied question. It is not acceptable if the model claims to answer a full network counterfactual while only weakly disciplining formation or feedback.

### What structural network models add

The value added is usually one of four things:

1. **Counterfactual changes in links**  
   Example: what if workers gain access to additional referral channels or a platform changes exposure?

2. **Counterfactual changes in information flow**  
   Example: what if a policy increases the reliability or scope of job information?

3. **Equilibrium changes in who interacts with whom**  
   Example: what if a labor-market reform changes sorting or segregation of contacts?

4. **Welfare analysis**  
   Example: do referrals improve efficiency, redistribute opportunities, or both?

These are precisely the objects that reduced-form network designs often cannot recover on their own.

### Network Block Summary: where the literature is now

The network methods literature is now strongest in four areas:

- measurement of worker, firm, neighborhood, and peer networks from administrative and platform data;
- causal designs for peer effects, spillovers, and referrals under partial interference or explicit exposure mappings;
- labor applications of referrals, workplace peers, and information diffusion;
- econometric models of link formation and degree heterogeneity.

What remains frontier is the integration of these pieces. Many papers are either:
- good at reduced-form identification but weak on counterfactual link changes, or
- good at structural counterfactuals but dependent on stronger assumptions and thinner validation.

The opportunity is to connect rich modern data to sharper economic models without letting the model outrun the evidence.

## Research Lab

### Primary anchor paper

Use Bryan Graham’s **Network Data** as the primary anchor for the lecture’s methodological lab. It is the best general gateway for seeing how dyadic regression, summary statistics, and network formation fit together in one empirical framework. [@grahamNetworkData2019]

### Challenge / extension paper

Use Galenianos’ **Referral Networks and Inequality** or Mele’s **A Structural Model of Dense Network Formation** as the challenge paper. The first is a labor-market application where referrals alter allocation and inequality. The second is a canonical econometric-formation paper showing what is gained and lost when formation itself becomes the object. [@galenianos2021referral; @mele2017structural]

### Reproduce

Reproduce one bounded object from the primary anchor:
- a network statistic,
- a dyadic regression setup,
- or a simple simulation of link heterogeneity / homophily.

### Diagnose

Diagnose:
- what the network is assumed to be measuring;
- whether links are exogenous, institutional, or strategic;
- what moments identify the model;
- whether the counterfactual changes outcomes on a fixed network or the network itself.

### Transfer

Transfer the logic to a labor-market setting:
- referral hiring,
- coworker learning,
- platform visibility,
- school-to-job contact structures,
- or workplace team formation.

The goal is not to fully re-estimate a frontier network model in class. The goal is to learn how to reason from an applied labor question to a defensible network counterfactual.

## Methods Box

### Practical workflow for structural network work

1. Define the economic network object.
   - worker-worker
   - worker-firm bipartite
   - firm-firm
   - neighborhood/social contact
   - platform exposure graph

2. Decide whether the research question is about:
   - behavior on a fixed network,
   - formation of the network,
   - or both.

3. Write down:
   - the action equation,
   - the formation equation,
   - the welfare object,
   - and the actual policy counterfactual.

4. Choose moments or likelihood objects that match the counterfactual.
5. Be explicit about what is not identified without stronger assumptions.
6. Validate with out-of-sample moments, network topology, or policy-relevant reduced-form facts.

### Common failure modes

- treating observed links as exogenous when they are strategic;
- estimating peer effects without credible exposure assumptions;
- claiming a counterfactual about network redesign without modeling formation;
- matching moments that do not discipline the policy-relevant object;
- overstating welfare conclusions from descriptive network fit.

## Reading Ladder And References

### Core theory / methods
- [@grahamNetworkData2019]
- [@graham2014methods]
- [@graham2017econometric]
- [@mele2017structural]

### Labor-network applications
- [@galenianos2021referral]
- [@dustmann2016referral]
- [@pallais2016referrals]
- [@calvoarmengol2004effects]
- [@calvoarmengol2007wage]

### Frontier / extensions
- [@herskovic2020acquiring]
- [@banerjee2024network]
- [@hafner2023working]

## Exercises And Discussion Prompts

1. Give an example of a policy question where a reduced-form peer-effects estimate is enough, and a second example where you need a structural network model.
2. In a referral-hiring application, what moments would you want to match if the policy changes information flow rather than wages?
3. Why is a model of network formation often required for welfare analysis?
4. Compare the assumptions needed for:
   - a fixed-network exposure design,
   - an endogenous-formation model,
   - and a labor-market referral equilibrium model.
5. Explain why two models with similar fit on degree distributions can imply very different counterfactuals.

## Reproducibility And Code Lab Note

The coding goal for this lecture is not a full frontier network estimator. It is a bounded workflow:
- build or simulate a small network,
- compute economically meaningful network statistics,
- estimate one simple dyadic or exposure-based relation,
- and show how the counterfactual changes when links are treated as fixed versus endogenous.

## Slide Companion Note

The slide deck should give students:
1. one conceptual map of the Network Methods block;
2. one slide on behavior on networks vs network formation;
3. one slide on labor applications;
4. one slide on identification and moments;
5. one slide on where the literature is now and where the opportunities are.

## Bridge Forward

This lecture closes the Network Methods block.

Students should now be able to distinguish:
- what a network is as an empirical object,
- how dependence changes causal identification,
- and when a structural network model is required for credible policy counterfactuals.

The larger lesson of the empirical methods course is that methods differ not only in credibility, but in what question they are capable of answering.
