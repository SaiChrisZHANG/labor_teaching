---
title: Causal Inference with Network Data
bibliography:
  - references.bib
---

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish ordinary treatment-effect problems from settings with peer effects, spillovers, or interference;
2. explain the reflection problem and why network structure matters for identification;
3. match research questions to suitable tools such as exposure mappings, randomized saturation designs, dyadic-robust inference, and network experiments;
4. evaluate what a network design identifies, where it can fail, and how dependence changes inference;
5. translate a network-causal question into a reproducible applied project.

## Opening Orientation

Networks matter when units influence one another through observed or latent links rather than only through their own treatment or covariates. In labor markets, these links arise through referrals, coworkers, managers, schools, neighborhoods, firms, and platforms. The empirical challenge is that the same links that generate interesting spillovers also create correlated outcomes, endogenous sorting, and failures of the standard stable-unit-treatment-value assumption.

This lecture treats network causality as a design problem. The goal is not to make students memorize a menu of estimators, but to help them diagnose when networks are the mechanism, when they are a threat to identification, and when network-targeted methods are required to recover a meaningful causal quantity.

:::{admonition} Core points
:class: important
- Network settings force researchers to define **who affects whom** and **through what exposure mapping**.
- The reflection problem means that correlations among peers are not enough to identify social effects [@manski1993].
- Network designs often require explicit assumptions about interference, partial interference, or dyadic dependence.
- Randomized saturation, network experiments, and exposure-based estimands can identify causal spillovers when ordinary individual treatment effects fail.
- Inference changes in network settings: dependence can survive even after controlling for observables, so ordinary standard errors are often misleading.
:::

## Bridge

Lectures 1–5 treated causality largely under versions of SUTVA, where one unit's treatment does not affect another unit's outcome. Lecture 16 showed a spatial version of the same problem: nearby units share shocks or affect one another through place-based exposure. Network methods make that logic explicit at the relationship level. The central design question is no longer only “who is treated?”, but also “which untreated units are indirectly exposed, and how?”

## Field Core

### 1. Why network causality is different

In ordinary potential-outcomes notation, unit *i* has potential outcomes \(Y_i(1)\) and \(Y_i(0)\). Under interference, that is too simple because the outcome may depend on the treatments of connected others. A more general representation is

```{math}
:label: eq:network-po
Y_i = Y_i\bigl(Z_i, Z_{-i}; G\bigr),
```

where \(G\) is the observed network and \(Z_{-i}\) is the treatment vector for units other than \(i\). This object is too rich to estimate without structure, so most applied work uses **exposure mappings**:

```{math}
:label: eq:exposure-mapping
Y_i = Y_i\bigl(Z_i, g_i(Z_{-i},G)\bigr),
```

where \(g_i(\cdot)\) compresses others’ treatments into a manageable exposure measure, such as the share of treated neighbors, treated coworkers, or treated classmates [@aronowSamiiEstimatingAverageCausal2017].

The empirical payoff is obvious: if job referrals, peer behavior, or manager treatment propagate through a network, the indirect effect may be the main mechanism. The cost is equally obvious: one must defend the exposure mapping itself.

### 2. The reflection problem and peer effects

A natural starting point is the linear-in-means model:

```{math}
:label: eq:linear-in-means
Y_i = \alpha + \beta \bar{Y}_{N(i)} + \gamma \bar{X}_{N(i)} + \delta X_i + \varepsilon_i,
```

where \(\bar{Y}_{N(i)}\) is average peer behavior and \(\bar{X}_{N(i)}\) is average peer characteristics. Manski showed that without strong structure or special variation, endogenous peer effects \(\beta\) are not separately identified from correlated effects and contextual effects [@manski1993].

Network structure can help. In intransitive or incomplete networks, excluded-peer variation can break the linear dependence that drives the reflection problem. Bramoullé, Djebbari, and Fortin show how network topology can provide identification when some peers affect others indirectly but are not directly in one another’s reference group [@bramoulleDjebbariFortin2009].

For applied work, the key lesson is: **a peer-effects design is only as credible as its reference-group definition and exclusion logic**. The design must explain why one peer’s treatment affects another’s outcome only through the hypothesized channel.

### 3. Interference, spillovers, and exposure mappings

Many interventions generate spillovers without any obvious “peer behavior” outcome. Think of:
- job search information moving through referral networks;
- wage policies affecting coworkers through scheduling or workload;
- manager training affecting entire teams;
- platform policies changing congestion for all users.

A practical way to study these effects is to define estimands indexed by direct treatment and exposure, such as:

```{math}
:label: eq:direct-indirect
\tau^{\text{direct}}(g)=\mathbb{E}[Y_i(1,g)-Y_i(0,g)],
\qquad
\tau^{\text{spill}}(z;g,g')=\mathbb{E}[Y_i(z,g)-Y_i(z,g')].
```

Aronow and Samii provide a general framework for such estimands under arbitrary exposure mappings [@aronowSamiiEstimatingAverageCausal2017]. In practice, this framework forces researchers to articulate:
1. what counts as a relevant connection,
2. which exposure summary is substantively meaningful,
3. whether treatment can propagate beyond one step in the network.

### 4. Randomized saturation, network experiments, and partial interference

Randomized saturation designs vary not only who is treated, but also the share treated within a cluster, village, classroom, or team. They are particularly useful when the direct effect may be contaminated by spillovers. Designs of this type let researchers ask whether untreated units in high-treatment environments behave differently from untreated units in low-treatment environments.

Applied examples like Miguel and Kremer’s deworming study illustrate why saturation matters: the intervention changed outcomes through epidemiological spillovers, so individual treatment status alone did not capture the full effect [@miguelKremer2004]. In labor-related settings, saturation-style logic also appears in referral experiments, coworker spillovers, and local hiring interventions.

Partial interference is the compromise assumption that spillovers occur within clusters but not across them. It is often defensible in organizational, classroom, village, or workplace settings, but much less plausible in open labor markets or platforms. The design lesson is simple: **partial interference is a convenience assumption, not a law of nature**.

### 5. Dyadic data and dyadic dependence

Some network problems are better represented as **dyadic data**: observations are indexed by pairs \((i,j)\), not by individuals. Examples include:
- worker–firm application pairs,
- referral links,
- board or coworker ties,
- bilateral flows,
- pairwise communication or collaboration.

A simple dyadic model takes the form

```{math}
:label: eq:dyadic-model
Y_{ij} = X_{ij}'\beta + a_i + a_j + u_{ij},
```

where dependence arises because dyads sharing a unit are not independent. Standard IID or cluster logic is often wrong here. Graham’s review and recent work by Canen discuss dyadic data methods and inference under such dependence [@grahamNetworkData2019; @canenInferenceLinearDyadic2022].

The applied implication is important: if your estimating unit is a pair, then both the **sampling process** and the **variance formula** need to respect shared-unit dependence.

### 6. Network-targeted econometric methods: when to use what

The point of this lecture is not only to revisit methods from Lectures 1–5 with network language. Network settings create their own design choices.

#### Exposure mappings
Use when the key question is about **direct and indirect treatment exposure** and the researcher can justify how others’ treatment status matters. Best for:
- cluster or village interventions,
- coworker/manager treatment exposure,
- network contagion or information flows.

#### Randomized saturation / network experiments
Use when treatment can be randomized at different intensities or over parts of the network. Best for:
- peer environments,
- referral or information-sharing experiments,
- interventions where spillovers are part of the design.

#### Dyadic-robust inference
Use when data are indexed by pairs and dependence comes from shared agents. Best for:
- worker–firm or person–person links,
- referral dyads,
- collaboration/communication ties.

#### Leave-one-out peer measures
Use cautiously when peer exposure is built from group averages excluding the focal individual. These can reduce mechanical reflection, but they do not solve endogenous sorting or correlated unobservables by themselves.

#### Structural or control-function approaches
Use when network formation itself is endogenous and central to the question. For example, if referral networks or peer groups are chosen, one may need a model of link formation or a control-function strategy rather than a reduced-form exposure design.

## Methods Box

### Network-targeted methods and practical caveats

**1. Exposure mapping**
- Best when theory suggests a small set of exposure states (e.g., share treated neighbors, treated manager, treated coworkers).
- Identification depends on whether that mapping captures the true spillover channel.
- Main failure mode: misspecified exposure mapping that hides important paths.

**2. Randomized saturation / graph experiments**
- Best when treatment intensity can be randomized across clusters or parts of the graph.
- Can separately identify direct and spillover effects under strong design control.
- Main failure mode: spillovers crossing the assumed boundaries or clusters.

**3. Dyadic-robust inference**
- Best when observations are pairs and dependence arises because dyads share units.
- Necessary in worker–firm, referral, or pairwise-interaction data.
- Main failure mode: assuming ordinary robust or cluster standard errors are enough when dependence is pair-structured.

**4. Leave-one-out peer averages**
- Best as descriptive or reduced-form exposure measures when peer groups are naturally given.
- Can help avoid mechanical simultaneity but does not solve endogenous group formation.
- Main failure mode: treating leave-one-out construction as a full identification strategy.

**5. Randomization / permutation inference**
- Especially useful in network experiments where asymptotics are weak or dependence is strong.
- Helps align inference with the actual randomization protocol.
- Main failure mode: using generic asymptotics in very dependent, small-network settings.

**6. Control-function / structural network approaches**
- Best when who links to whom is itself endogenous and central.
- Useful when policy affects formation, not only outcomes on a fixed graph.
- Main failure mode: underestimating how much identifying power comes from modeling assumptions.

## Research Lab

### Primary anchor paper

**Peer Effects in the Workplace** by Cornelissen, Dustmann, and Schönberg is a strong primary anchor because it is a labor-relevant peer-effects paper that makes the identification problem concrete: who counts as a peer, what the peer group is, and what variation identifies the spillover [@cornelissenPeerEffectsWorkplace2017].

### Reproduce

Reproduce one headline peer-effects result using a reduced teaching dataset or a stylized peer-exposure design. The goal is to recover the basic peer-effect object and show how the estimating equation changes when the peer group is redefined.

### Diagnose

Diagnose the identification threats:
- endogenous sorting into peer groups,
- common shocks to workers sharing a team,
- reflection and simultaneity,
- whether the design identifies a true social interaction or only correlated effects.

Then ask what assumptions the original paper needs to make those threats manageable.

### Transfer

Transfer the logic to a network-based hiring or referral setting, where the relevant object is not coworker productivity but access to information, job leads, or referrals. A good transfer exercise is to define a new exposure mapping and explain how the estimand changes when the spillover channel is informational rather than effort-based.

### Challenge / extension anchor

**Evidence from Field Experiments on Referrals** by Pallais and Sands is a useful challenge anchor because it makes the network channel more explicit and more labor-market oriented: treatment changes both information and screening through social ties [@pallaisEvidenceFieldExperiments2016].

## Reading Ladder And References

### Core theory and econometric framing
- Manski on the reflection problem and endogenous social effects [@manski1993]
- Bramoullé, Djebbari, and Fortin on network identification of peer effects [@bramoulleDjebbariFortin2009]
- Aronow and Samii on average causal effects under general interference [@aronowSamiiEstimatingAverageCausal2017]
- Graham on network data and dyadic methods [@grahamNetworkData2019]

### Applied labor/network examples
- Cornelissen, Dustmann, and Schönberg on peer effects in the workplace [@cornelissenPeerEffectsWorkplace2017]
- Pallais and Sands on referrals and peer influence in labor-market experiments [@pallaisEvidenceFieldExperiments2016]
- Barwick, Deng, Li, and Rao on referral networks and labor-market inequality [@barwickJobReferralNetwork2019]
- Miguel and Kremer on spillovers and cluster-interference logic [@miguelKremer2004]

### Inference and frontier methods
- Canen on inference in linear dyadic data models [@canenInferenceLinearDyadic2022]
- Recent work on global or network interference design/inference if students want frontier econometrics follow-up

## Exercises And Discussion Prompts

1. Why does the reflection problem persist even if the researcher has rich covariates?
2. When is a leave-one-out peer average merely descriptive, and when can it be part of a credible design?
3. What makes an exposure mapping persuasive in a labor application?
4. Why might partial interference be reasonable in a classroom but not in an online labor market?
5. Suppose a paper estimates referral effects using worker pairs. What is wrong with ordinary robust standard errors?

## Reproducibility And Code Lab Note

A bounded teaching lab for this lecture should:
- reproduce a peer-effects or referral design,
- compare at least two peer-group / network definitions,
- show how inference changes once dyadic or clustered dependence is acknowledged,
- and transfer the design to a second labor-network setting.

If official replication materials are not locally available, use a reduced or synthetic teaching path and label it transparently as pedagogical rather than exact replication.

## Slide Companion Note

The lecture slides should keep the network-causal logic visual:
- a graph showing direct treatment vs exposure,
- a slide on the reflection problem,
- a slide on dyadic dependence,
- a slide comparing network-targeted methods,
- a slide on the Research Lab workflow.

## Bridge Forward

Lecture 18 taught students how to define nodes, edges, and descriptive network objects. Lecture 19 teaches how those relationships alter identification and inference. The next step is to ask what happens when network formation itself becomes part of the equilibrium object rather than a fixed data structure.
