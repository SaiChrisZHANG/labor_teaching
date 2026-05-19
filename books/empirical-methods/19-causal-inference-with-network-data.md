# Lecture 19. Causal Inference With Network Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish ordinary treatment-effect designs from settings with peer effects, spillovers, or interference;
2. explain the reflection problem and why network structure can change identification;
3. write potential outcomes under interference and defend an exposure mapping;
4. explain randomized saturation, network experiments, and partial-interference assumptions;
5. diagnose when dyadic or network-targeted econometric methods are needed beyond Lectures 1 to 5;
6. choose inference procedures that respect dependence induced by links, clusters, or dyads;
7. evaluate what a network-causal paper identifies, what assumptions it needs, where it can fail, and how the network definition shapes interpretation.

## Opening Orientation

Lecture 19 asks: **how can researchers estimate effects when units influence one another through observed or latent links?** Lecture 18 built the graph. This lecture asks what can be learned causally once that graph exists.

Network causal inference matters because many labor-market interventions do not stop with the treated worker. Coworkers learn from one another. Managers transmit practices to teams. Referrals move information through worker contacts. Classmates, neighborhoods, firms, and platforms create exposure environments. When these links matter, the usual individual treatment contrast can miss the main mechanism.

The difficulty is that networks also break familiar shortcuts. Peers select into the same groups. Outcomes move together because of common shocks. Treated units affect untreated units. Observations indexed by worker pairs or worker-firm pairs are not independent. A graph can be the mechanism, the assignment environment, the source of dependence, or a post-treatment object.

The paper spine is deliberately research-facing. Manski gives the reflection problem [@manski1993]. Bramoulle, Djebbari, and Fortin and Goldsmith-Pinkham and Imbens show how network structure can help identify peer effects [@bramoulleDjebbariFortin2009; @goldsmithPinkhamImbens2013]. Aronow and Samii and Athey, Eckles, and Imbens formalize interference and network-experiment inference [@aronowSamiiEstimatingAverageCausal2017; @atheyEcklesImbensExactPvalues2015]. Cornelissen, Dustmann, and Schonberg provide the primary labor peer-effects anchor [@cornelissenPeerEffectsWorkplace2017]. Pallais and Sands and Barwick, Deng, Li, and Rao show how referral networks make the labor-market mechanism more explicit [@pallaisEvidenceFieldExperiments2016; @barwickJobReferralNetwork2019]. Graham and Canen give students a path into dyadic data and network dependence [@grahamNetworkData2019; @canenInferenceLinearDyadic2022].

## Core Points

:::{admonition} Core points
:class: important

- Network definition is part of identification: nodes, edges, weights, timing, and boundaries define who can affect whom.
- The reflection problem warns that peer correlations do not by themselves identify endogenous social effects.
- Potential outcomes must allow one unit's outcome to depend on others' treatments; exposure mappings make that object estimable.
- Randomized saturation and network experiments identify direct and spillover effects only relative to the assignment rule and interference assumptions.
- Partial interference is useful when spillovers are plausibly contained inside clusters, but it is a substantive assumption.
- Dyadic and network data create dependence that ordinary heteroskedastic-robust or one-way clustered standard errors may miss.
- Network-targeted methods are needed when links define exposure, treatment propagation, the estimating unit, or the dependence structure.
:::

## Bridge

Lectures 1 to 5 taught the core design vocabulary: potential outcomes, experiments, DID, IV, RD, and local designs. Those tools remain essential. Network methods do not replace them. They clarify when their usual assumptions are too small for the setting.

The key change is SUTVA. In the core lectures, a unit's potential outcome could often be written as {math}`Y_i(1)` or {math}`Y_i(0)`. In a network setting, that notation hides the main problem: worker {math}`i` may be affected by the treatment, behavior, or information of connected workers {math}`j`.

Lecture 16 made a spatial version of the same point. If deworming in one school affects nearby schools, or if a place-based policy affects neighboring regions, the untreated comparison is not necessarily untreated [@miguelKremer2004]. Lecture 19 moves from geographic proximity to explicitly measured or theorized relationships: coworkers, classmates, referrers, applicants, managers, firms, teams, neighborhoods, and platforms.

```{include} assets/tables/19-spatial-identification-problems-map.md
```

The bridge from Lecture 18 is equally direct. Network curation asked whether the graph is defensible. Causal inference asks whether the graph, assignment rule, timing, and inference procedure can support a counterfactual claim.

## Field Core

### A. What Changes Once Links Matter

In a standard binary-treatment design, the researcher might define:

```{math}
:label: eq:em19-sutva
\tau = \mathbb{E}[Y_i(1)-Y_i(0)].
```

This estimand assumes that the treatment assigned to unit {math}`j` does not change unit {math}`i`'s potential outcome. Network settings relax that assumption. Let {math}`G` denote the network and {math}`Z=(Z_1,\ldots,Z_N)` the treatment vector. A general potential outcome is:

```{math}
:label: eq:em19-network-po
Y_i = Y_i(Z_i, Z_{-i}; G).
```

This notation is honest but unusable without restrictions. It says that unit {math}`i` can have a different potential outcome for every possible assignment vector in the network. With 1,000 workers, the number of assignment states is enormous.

Applied work therefore needs structure. The usual structure is an **exposure mapping**:

```{math}
:label: eq:em19-exposure-mapping
D_i = g_i(Z_{-i},G), \qquad
Y_i = Y_i(Z_i,D_i).
```

The exposure {math}`D_i` might be the share of treated coworkers, whether a manager is treated, the number of treated neighbors within two steps, the treatment saturation in a classroom, or whether an applicant is linked to a treated referrer. Aronow and Samii show how average causal effects can be defined under general interference once the exposure mapping is specified [@aronowSamiiEstimatingAverageCausal2017].

The gain is interpretability. The cost is responsibility. If the exposure mapping is wrong, the estimand is wrong.

### B. The Reflection Problem And Peer Effects

Peer-effects papers often begin with a linear-in-means formulation:

```{math}
:label: eq:em19-linear-in-means
Y_i
=
\alpha
+ \beta \sum_j w_{ij}Y_j
+ \gamma \sum_j w_{ij}X_j
+ \delta X_i
+ \varepsilon_i,
```

where {math}`w_{ij}` are network or peer-group weights. The coefficient {math}`\beta` is the endogenous peer effect: peer outcomes affect own outcomes. The coefficient {math}`\gamma` is a contextual effect: peer characteristics affect own outcomes. Correlated effects arise when peers share unobserved shocks or select into the same group.

Manski's reflection problem is that, without additional structure, these forces are hard to separate [@manski1993]. If a worker's effort and coworkers' effort are jointly determined inside the same team, a regression of own effort on average coworker effort can reflect influence, sorting, shared management, or a common demand shock.

Network structure can help when it creates excluded-peer variation. Bramoulle, Djebbari, and Fortin show that intransitive networks can identify peer effects because friends of friends can affect peers without being direct peers of the focal unit [@bramoulleDjebbariFortin2009]. Goldsmith-Pinkham and Imbens emphasize the assumptions behind peer-effect estimation with social networks, including the role of the reference group and the network itself [@goldsmithPinkhamImbens2013].

For students, the practical lesson is sharp:

- a leave-one-out peer average can remove mechanical inclusion of the focal worker, but it does not solve endogenous sorting;
- network topology can help only if the exclusion restrictions are economically credible;
- timing matters because peer exposure should precede the outcome;
- peer behavior on the right-hand side is dangerous when it is jointly determined with own behavior.

Cornelissen, Dustmann, and Schonberg are the labor anchor because they ask a concrete workplace question: how do coworker peer groups affect individual productivity, and what variation makes that claim credible [@cornelissenPeerEffectsWorkplace2017]? The design is useful for students because it makes the peer-group definition, sorting threat, and interpretation problem visible.

### C. Interference, Spillovers, And Exposure Mappings

Peer effects are only one network-causal problem. Many interventions generate spillovers even when there is no peer outcome on the right-hand side:

- a job-search workshop changes information available to untreated friends;
- manager training changes workloads for everyone in the team;
- a referral bonus changes which applicants enter the pool;
- a platform visibility rule changes congestion and matching for connected users;
- classroom or workplace interventions change norms, learning, or effort through peers.

With exposure mappings, researchers can define direct and indirect effects. For two exposure states {math}`d` and {math}`d'`, a direct effect at exposure {math}`d` is:

```{math}
:label: eq:em19-direct-effect
\tau^{direct}(d)
=
\mathbb{E}\left[Y_i(1,d)-Y_i(0,d)\right].
```

A spillover effect for treatment status {math}`z` is:

```{math}
:label: eq:em19-spillover-effect
\tau^{spill}(z;d,d')
=
\mathbb{E}\left[Y_i(z,d)-Y_i(z,d')\right].
```

These estimands are useful because they separate being treated from being exposed to treated neighbors. They also force the researcher to defend the exposure scale. Is the relevant object any treated neighbor, the count of treated neighbors, the share treated, distance-weighted exposure, a treated high-centrality peer, or a saturation cell?

The main failure modes are common:

1. the network misses the true channel;
2. exposure is measured after treatment or after outcomes begin to respond;
3. spillovers travel beyond the assumed neighborhood;
4. the exposure mapping compresses heterogeneous paths into one noisy scalar;
5. the reported direct effect is actually a mixture of direct, indirect, and equilibrium responses.

### D. Randomized Saturation, Network Experiments, And Partial Interference

Randomization remains powerful in network settings, but the design must randomize the right object. A simple individual experiment identifies a direct treatment effect cleanly only if untreated units are not affected by treated units. When spillovers are expected, the design should vary exposure.

A randomized saturation design assigns different treatment probabilities to clusters, teams, villages, classrooms, or worksites. One team might have treatment probability {math}`p=0.25`; another might have {math}`p=0.75`. Untreated units in high-saturation teams can then be compared with untreated units in low-saturation teams to learn about spillovers. Treated units across saturation cells can reveal how direct effects depend on peer exposure.

The saturation intuition is:

```{math}
:label: eq:em19-saturation
Z_i \sim Bernoulli(p_c), \qquad
p_c \in \{p_L,p_H\},
```

where {math}`c` indexes a cluster. The design creates variation in both own treatment {math}`Z_i` and exposure {math}`D_i`, often summarized as the treated share among peers or inside a cluster.

Miguel and Kremer are not a labor paper, but they are a canonical teaching anchor because they made externalities part of the estimand rather than a nuisance [@miguelKremer2004]. Labor-facing applications include team training, workplace information interventions, referral incentives, job-search assistance, and platform experiments where spillovers are expected.

Network experiments use the observed graph more directly. Treatment may be assigned to seeds, high-centrality nodes, clusters, or graph partitions. The assignment rule matters for both identification and inference. Athey, Eckles, and Imbens show why exact or randomization-based inference can be valuable when the assignment and interference structure are network-specific [@atheyEcklesImbensExactPvalues2015].

Partial interference is the common compromise:

```{math}
:label: eq:em19-partial-interference
Y_{ic}=Y_{ic}(Z_{ic},Z_{-i,c}), \qquad
Y_{ic} \text{ does not depend on } Z_{k\ell} \text{ for } \ell \ne c.
```

It says spillovers occur within clusters but not across clusters. This can be plausible for classrooms, teams, villages, or closed workplaces. It is weaker in open labor markets, online platforms, and cities where workers, vacancies, information, or prices cross boundaries.

### E. Dyadic And Network-Targeted Econometric Methods

Some network data are naturally indexed by pairs rather than individuals. Examples include worker-firm applications, employee-applicant referrals, worker-worker coworker ties, schoolmate dyads, bilateral flows, board interlocks, and collaboration records. A dyadic outcome might be:

```{math}
:label: eq:em19-dyadic-model
Y_{ij}
=
X_{ij}'\beta
+ a_i
+ b_j
+ u_{ij}.
```

The problem is dependence. The dyads {math}`(i,j)` and {math}`(i,k)` share unit {math}`i`. The dyads {math}`(i,j)` and {math}`(k,j)` share unit {math}`j`. Even if each pair is an observation, the pairs are not independent. Graham's review and Canen's work give students entry points for dyadic models and inference under network dependence [@grahamNetworkData2019; @canenInferenceLinearDyadic2022].

This is where network-targeted methods go beyond Lectures 1 to 5. Ordinary robust standard errors handle heteroskedasticity, not pairwise dependence. One-way clustering handles one shared dimension, not necessarily two-sided dyadic dependence. A DID, IV, RD, or experiment can still be the design, but the estimating unit and variance estimator must match the relational data-generating process.

```{include} assets/tables/19-network-targeted-methods-toolkit.md
```

The practical rule is not to use the most exotic method available. Use network-targeted econometrics when one of four things is true:

1. links define treatment exposure;
2. links define the estimating unit;
3. links define interference or spillover paths;
4. links define the dependence structure for inference.

### F. Interpreting Network-Causal Estimates

Network estimates are easy to overstate. A direct effect under one exposure mapping is not necessarily the total policy effect. A spillover effect within one cluster design is not necessarily a market-wide equilibrium effect. A peer-effect coefficient in a fixed graph does not say what would happen if the policy changed the graph itself.

Network definition is therefore not a data appendix detail. It is substantive. A coworker edge can mean direct collaboration, same manager, same occupation, same establishment, same shift, or same firm. A referral edge can mean information, screening, favoritism, trust, or homophily. A neighborhood edge can mean local job information or shared sorting into opportunity. Each definition changes the estimand.

Good papers make this visible. They state:

- the economic channel carried by the link;
- the timing that makes exposure prior to outcome;
- the variation that separates influence from sorting or common shocks;
- the exposure mapping and alternatives;
- the inference procedure under dependence;
- the interpretation limits of direct, spillover, and equilibrium effects.

```{include} assets/tables/19-good-design-checklist.md
```

## Research Lab

The Week 19 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a deterministic synthetic teaching path, not an official replication package.

The primary anchor is Cornelissen, Dustmann, and Schonberg [@cornelissenPeerEffectsWorkplace2017]. The lab uses their paper as a workplace peer-effects design template: define the peer group, build leave-one-out peer measures, estimate a peer-exposure object, and diagnose reflection and sorting risks. The challenge anchor is Pallais and Sands [@pallaisEvidenceFieldExperiments2016], with Barwick, Deng, Li, and Rao as a referral-network inequality extension [@barwickJobReferralNetwork2019].

### Reproduce

Students reproduce a teaching-scale workplace peer-effects design. They:

- build synthetic teams, coworker links, treatment assignment, and outcomes;
- construct leave-one-out peer treatment and peer productivity measures;
- estimate direct treatment and spillover associations under a team exposure mapping;
- summarize randomized saturation cells and untreated exposure contrasts.

The point is not to recover a real published coefficient. The point is to make the peer-effect object and exposure mapping visible.

### Diagnose

Students diagnose the design:

- compare team-level, graph-neighbor, and weighted exposure mappings;
- inspect whether peer outcomes are contemporaneous and therefore reflection-prone;
- run a small randomization-inference exercise under the synthetic assignment rule;
- evaluate whether partial interference across teams is plausible;
- explain which estimates are design-based, which are descriptive, and which would require stronger assumptions.

### Transfer

Students transfer the logic to referral dyads. They:

- construct employee-applicant referral pairs;
- estimate a simple pair-level model for callback or hiring;
- compare naive heteroskedastic-robust inference with pair-aware two-way cluster logic;
- write a memo explaining how the estimand changes from workplace peer exposure to referral-network access.

The transfer task makes the dyadic issue concrete. The observation is no longer just a worker. It is a worker-applicant pair, and dependence follows shared referrers and shared applicants.

## Methods Box

### Network-Targeted Methods For Applied Work

**Exposure mappings.** Start by mapping assignments and the graph into a small set of exposure states: own treatment, treated peer share, treated manager, number of treated neighbors, treated high-centrality contact, or distance-weighted treated exposure. This identifies effects of exposure states, not every possible assignment vector. The mapping is credible when it follows the mechanism and timing. It fails when the true channel travels through unmeasured links, longer paths, or heterogeneous contacts collapsed into one exposure.

**Randomization inference and permutation logic.** In network experiments, inference should often follow the actual assignment rule. If seeds, clusters, saturation cells, or graph partitions were randomized, permutations should respect that design. The null is usually sharp only after specifying the interference or exposure structure. This is especially useful in small or highly dependent networks, but it fails when the researcher permutes labels in ways the experiment could never have assigned.

**Dyadic-robust variance estimation and dependence.** Pair-level data need inference that allows dyads sharing a unit to be correlated. A practical starting point is two-way cluster or dyadic-robust logic over the two unit dimensions. The goal is to avoid pretending that referral pairs, worker-firm applications, or collaboration dyads are IID rows. This helps inference, but it does not solve endogenous link formation or omitted pair-level confounding.

**Leave-one-out peer measures and reflection caveats.** A leave-one-out peer mean,

```{math}
:label: eq:em19-loo
\bar X_{-i,g}
=
\frac{1}{n_g-1}\sum_{j \in g, j\ne i} X_j,
```

removes the focal unit from the group average. That is useful for avoiding mechanical self-inclusion. It does not by itself identify peer effects. Sorting, correlated shocks, simultaneity, and post-treatment group formation remain design problems.

**Graph- or saturation-based experimental designs.** If spillovers are expected, randomize exposure. Saturation designs vary treatment intensity across clusters. Graph experiments assign treatment to seeds, neighborhoods, or graph partitions. These designs can identify direct and spillover effects when the assignment rule, exposure mapping, and interference assumptions line up. They fail when spillovers cross assumed boundaries or when the graph used for design misses the real channel.

**When network methods are needed beyond Lectures 1 to 5.** Use the core causal toolkit when the question is a standard treatment contrast and spillovers are negligible or can be blocked by design. Use network-targeted methods when the treatment is transmitted through relationships, the untreated are exposed through treated peers, peer outcomes enter the behavioral model, observations are dyads, or dependence follows the graph.

## Reading Ladder And References

```{include} assets/tables/19-reading-architecture.md
```

**Core conceptual anchor.** Start with Manski for the reflection problem [@manski1993]. Then read Bramoulle, Djebbari, and Fortin and Goldsmith-Pinkham and Imbens for how network topology and peer-group assumptions can help or fail [@bramoulleDjebbariFortin2009; @goldsmithPinkhamImbens2013].

**Interference and experiments.** Aronow and Samii formalize exposure-mapping estimands under interference [@aronowSamiiEstimatingAverageCausal2017]. Athey, Eckles, and Imbens connect inference to network interference [@atheyEcklesImbensExactPvalues2015]. Miguel and Kremer remain the clean teaching example for externalities and saturation logic [@miguelKremer2004].

**Labor applications.** Cornelissen, Dustmann, and Schonberg anchor workplace peer effects [@cornelissenPeerEffectsWorkplace2017]. Pallais and Sands show how referral experiments make social ties part of a labor-market design [@pallaisEvidenceFieldExperiments2016]. Barwick, Deng, Li, and Rao connect referral networks to inequality and matching [@barwickJobReferralNetwork2019].

**Methods and inference.** Graham gives the broad network-data econometrics map [@grahamNetworkData2019]. Canen gives students a route into inference for linear dyadic data models with network dependence [@canenInferenceLinearDyadic2022].

## Exercises And Discussion Prompts

1. Write a linear-in-means peer-effects model for workplace productivity. Which term is an endogenous peer effect, which term is a contextual effect, and where can correlated effects enter?
2. Why does a leave-one-out peer average reduce mechanical reflection but not solve endogenous group formation?
3. Define two exposure mappings for a manager-training experiment: one based on treated coworker share and one based on graph-neighbor treatment. What does each estimand mean?
4. When is partial interference plausible in a workplace or classroom? When is it implausible in a labor-market or platform setting?
5. Design a randomized saturation experiment for a job-search program. What would untreated units in high-saturation clusters identify relative to untreated units in low-saturation clusters?
6. A referral paper uses applicant-referrer pairs as observations. Why can ordinary robust standard errors be misleading?
7. Choose one labor-network paper and state the network definition, exposure mapping, identifying variation, inference problem, and interpretation limit.

## Reproducibility And Code Lab Note

The Lecture 19 code lab lives at `labs/19-causal-inference-with-network-data/`. It uses deterministic synthetic data because no official replication data are locally available in the repository. The lab is intentionally bounded: students reproduce a peer-exposure object, diagnose exposure and reflection risks, and transfer the design to referral dyads with pair-aware inference.

The lab should not be read as evidence about the magnitude of real workplace peer effects or referral effects. Its purpose is to make the causal architecture explicit: peer group, graph definition, treatment assignment, exposure mapping, reflection risk, partial interference, dyadic dependence, and inference.

## Slide Companion Note

The Lecture 19 slide deck is under `slides/week19/19-causal-inference-with-network-data.tex`. It should define the question, contrast ordinary treatment effects with network exposure, isolate the reflection problem, show potential outcomes under interference, explain saturation and exposure mappings, summarize network-targeted methods, make dyadic inference visible, and end with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Lecture 18 made network data defensible. Lecture 19 made causal claims conditional on exposure mappings, randomization, topology, partial interference, and dependence-aware inference. Lecture 20 asks what changes when the network itself is endogenous and policy may change link formation, search, referrals, diffusion, or equilibrium behavior on the graph.
