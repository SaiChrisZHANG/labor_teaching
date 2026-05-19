# Lecture 20. Structural Modeling With Network Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when reduced-form network evidence is not enough for the counterfactual;
2. distinguish models of behavior on a network from models of endogenous network formation;
3. write the core objects in structural peer-effects, search, referral, diffusion, and formation models;
4. diagnose what variation identifies structural network primitives and what assumptions do the work;
5. evaluate policies that change links, information flows, matching opportunities, or equilibrium behavior;
6. describe the frontier of the network-methods block and propose researchable next questions.

## Opening Orientation

Lecture 18 built network data as an empirical object. Lecture 19 asked how links change causal identification, exposure, interference, and inference. Lecture 20 asks a harder question: **when do researchers need an economic model of network formation or network-mediated behavior to answer the policy question?**

The answer is deliberately conservative. A structural network model is not needed just because a graph appears in the data. It becomes useful when the counterfactual changes the network itself, changes information flows through the network, changes who can search or match with whom, or changes equilibrium behavior among linked agents. In those settings, a reduced-form estimate of an exposure effect on the observed graph may be too local. The policy of interest may move the system outside the support of the design.

The paper spine keeps the lecture methods-oriented and labor-facing. Graham gives the broad econometric map for network data [@grahamNetworkData2019], while Graham's degree-heterogeneity model and Mele's dense-formation model make formation a structural object [@graham2017econometric; @mele2017structural]. Jackson, Rogers, and Zenou show why social-network structure has economic consequences [@jacksonRogersZenou2017]. Calvo-Armengol and Jackson connect networks to employment, wages, and inequality [@calvoarmengol2004effects; @calvoarmengol2007wage]. Dustmann, Glitz, Schonberg, and Bruderl, Galenianos, and Pallais and Sands give labor-market referral and search anchors [@dustmann2016referral; @galenianos2021referral; @pallais2016referrals].

The key burden is validation. Once links are endogenous, the researcher must explain not only how outcomes respond to links, but why the links exist, how they would change under policy, and which empirical moments discipline those claims.

## Core Points

:::{admonition} Core points
:class: important

- Structural network models add value when policies change relationships, information flows, search opportunities, matching sets, or equilibrium behavior.
- Behavior-on-network models condition on a graph; formation models explain the graph itself. Many labor counterfactuals need both.
- Endogenous links create a heavier burden than ordinary peer-effects designs because sorting, strategic interaction, and outcomes can be jointly determined.
- Referral, search, diffusion, and matching models are useful only when the link has a clear economic meaning.
- Estimation must connect model primitives to moments that matter for the counterfactual: degree, clustering, homophily, referral yields, transitions, wages, match quality, or adoption paths.
- Validation should include fit to network topology, behavior conditional on links, out-of-sample or held-out moments when possible, and sensitivity to formation assumptions.
- The Network Methods block closes with a division of labor: Lecture 18 defines the network, Lecture 19 identifies effects through the network, and Lecture 20 asks what happens when policy changes the network.
:::

## Bridge

The bridge from Lectures 18 and 19 is a change in the counterfactual. In Lecture 18, the main question was whether a graph was measured in a defensible way. In Lecture 19, the graph helped define exposure, interference, and dependence. In Lecture 20, the graph may itself be an outcome of choices, institutions, search frictions, or policy.

The same labor setting can move through all three layers:

1. **Network definition and data.** A firm records which employee referred which applicant, when the referral happened, and for which vacancy.
2. **Causal identification with networks.** A referral bonus or randomized information intervention changes exposure to treated referrers or vacancies.
3. **Structural modeling and counterfactuals.** A policy changes who can refer whom, how firms rank referral signals, which workers receive vacancy information, and how applicants redirect search effort.

Reduced-form designs are still essential. They discipline the model and often provide the most credible local evidence. But if the question is, "What happens if the platform changes the ranking algorithm, if a firm subsidizes cross-group referrals, or if a training program rewires coworker learning paths?", the researcher needs a way to model behavior and links under the new rule.

## Field Core

### A. When Reduced-Form Network Methods Are Not Enough

A reduced-form exposure design might estimate:

```{math}
:label: eq:em20-reduced-form-exposure
Y_i = \alpha + \tau D_i(G,Z) + X_i'\beta + u_i,
```

where {math}`D_i(G,Z)` is exposure through the observed graph {math}`G`. This can be powerful when {math}`G` is fixed for the research question and the variation in {math}`D_i` is credible. Lecture 19 lives mostly in this space.

The limitation appears when policy changes the graph or the equilibrium behavior supported by the graph. The object may be:

```{math}
:label: eq:em20-policy-value
V(p)
=
\mathbb{E}\left[
W_i\left(G(p), a_i(G(p),X,\varepsilon), X_i\right)
\right],
```

where policy {math}`p` changes links {math}`G(p)`, actions {math}`a_i(\cdot)`, and welfare {math}`W_i(\cdot)`. A reduced-form estimate of {math}`\tau` in equation {eq}`eq:em20-reduced-form-exposure` does not identify equation {eq}`eq:em20-policy-value` unless the observed exposure variation maps cleanly to the new policy environment.

Examples are common in labor economics:

- a referral subsidy changes who refers whom, not only the return to an existing referral;
- a platform changes which workers and firms can see each other;
- a school or workplace assignment rule changes peer groups;
- a diffusion policy changes the path of information through coworkers or managers;
- a matching reform changes congestion and outside options for linked agents.

In each case, the reduced-form result is an input. The structural claim is about behavior under a different network, not only outcomes conditional on the observed network.

```{include} assets/tables/20-structural-network-models-map.md
```

### B. Behavior On Networks

Behavior-on-network models condition on the graph and model choices or outcomes given links. A stylized peer-effects model is:

```{math}
:label: eq:em20-behavior-network
a_i
=
\alpha
+ \beta x_i
+ \gamma \sum_j g_{ij}a_j
+ \delta \sum_j g_{ij}x_j
+ \varepsilon_i,
```

where {math}`g_{ij}` is a normalized link or exposure weight. The parameter {math}`\gamma` captures endogenous peer effects and {math}`\delta` captures contextual effects. This is close to the language of Lecture 19, but a structural model adds equilibrium interpretation. The researcher must explain how the system of actions is solved, whether multiple equilibria matter, and how beliefs or information enter.

For example, in a workplace learning model, {math}`a_i` might be effort, adoption of a new practice, or productivity. Links may transmit information from managers and coworkers. A policy that trains high-centrality workers has a different predicted effect from a policy that trains random workers only if the model says how trained workers affect others and how others respond.

The identifying variation can come from experiments, timing, quasi-random assignment, panel changes in teams, or excluded-peer variation. But the structural interpretation depends on more than the coefficient. It depends on the equilibrium concept, the timing of actions, the information structure, and the stability of the graph under the counterfactual.

### C. Endogenous Network Formation

Formation models explain why links exist. A simple latent-utility representation is:

```{math}
:label: eq:em20-link-utility
G_{ij}
=
\mathbf{1}\left\{
U_{ij}(X_i,X_j,G_{-ij},\eta_{ij}) \ge 0
\right\}.
```

This notation hides several hard choices. If {math}`U_{ij}` depends only on dyad characteristics, links can be modeled as conditionally independent. If {math}`U_{ij}` depends on {math}`G_{-ij}`, formation is strategic: transitivity, clustering, congestion, indirect connections, or status can affect the payoff to a link. Mele's model is useful precisely because it takes dense strategic formation seriously [@mele2017structural]. Graham's formation work shows how degree heterogeneity can be a central econometric object rather than nuisance variation [@graham2017econometric].

Labor applications make the economic stakes visible:

- workers choose neighborhoods, schools, platforms, teams, and firms;
- firms choose referral programs, screening rules, teams, and communication structures;
- applicants choose where to search based on contacts and expected competition;
- managers choose whom to mentor or connect;
- institutions constrain which contacts are feasible.

Treating this network as exogenous can be harmless for some descriptive or local causal questions. It is dangerous for counterfactuals that change link incentives or link opportunities.

### D. Search, Referrals, And Labor-Market Applications

Referral and search networks are the natural labor-market home for structural network modeling. A worker's contact set affects which vacancies arrive, how credible a recommendation is, how firms screen applicants, and how workers update beliefs about match quality. The link can represent information, trust, monitoring, favoritism, reputation, or access to a bottlenecked vacancy.

A compact search-and-referral environment can be summarized as:

```{math}
:label: eq:em20-referral-arrival
\lambda_i(G)
=
\lambda_0
+ \lambda_1 \sum_j G_{ij} q_j,
```

where {math}`\lambda_i(G)` is the arrival rate of useful job information and {math}`q_j` is the quality, vacancy access, or information reliability of contact {math}`j`. This is not a full model, but it makes the counterfactual visible. A policy may raise {math}`\lambda_0`, subsidize new links {math}`G_{ij}`, change the quality of information {math}`q_j`, or change employer beliefs about referred applicants.

Calvo-Armengol and Jackson show how employment and inequality can move through networks even without a conventional treatment assignment [@calvoarmengol2004effects; @calvoarmengol2007wage]. Dustmann, Glitz, Schonberg, and Bruderl connect referral-based job search to observed labor-market outcomes [@dustmann2016referral]. Galenianos studies how referral networks can generate inequality [@galenianos2021referral]. Pallais and Sands show that field experiments can discipline referral mechanisms even when the full structural environment is not estimated [@pallais2016referrals].

The research lesson is not that every referral paper must estimate a full equilibrium model. It is that the model should match the policy. A referral bonus, cross-group referral subsidy, platform-ranking change, or vacancy-information intervention changes more than a coefficient on an existing edge.

### E. Diffusion And Equilibrium Behavior On Networks

Diffusion models study how information, technologies, norms, practices, or beliefs spread through links. A simple adoption equation might be:

```{math}
:label: eq:em20-diffusion
\Pr(a_{it}=1)
=
\sigma\left(
\alpha
+ X_i'\beta
+ \rho \sum_j g_{ij} a_{j,t-1}
+ \kappa s_{it}
\right),
```

where {math}`s_{it}` is a seed, training, or information shock and {math}`\rho` governs diffusion through lagged peer adoption. This family is useful for studying training spillovers, management-practice diffusion, technology adoption, job-search norms, or information about wages and vacancies.

Equilibrium matters when adoption changes incentives for others. A platform may become congested after information improves. A firm may change hiring standards after referrals expand. Workers may redirect search when more peers enter the same channel. These responses are hard to capture with a fixed-network exposure effect.

This is the point of structural network work: it can make the general-equilibrium or strategic channel explicit. The price is that assumptions become more visible and more demanding.

### F. Estimation, Computation, And Validation

Structural network models are computationally difficult because the graph is high-dimensional and equilibrium can be strategic or path dependent. Researchers therefore use approximations:

- conditional likelihood or moment restrictions for dyads;
- simulation-based estimation;
- local-statistic approximations to strategic formation;
- sparse-network restrictions;
- separable behavior and formation blocks;
- held-out moments for validation.

```{include} assets/tables/20-identification-and-computation-map.md
```

The central question is not whether the method sounds sophisticated. It is whether the data discipline the primitives that matter for the counterfactual. A useful moment vector might be:

```{math}
:label: eq:em20-moments
m(\theta)
=
\mathbb{E}_{\theta}\left[
\text{degree},
\text{clustering},
\text{homophily},
\text{wage covariance across links},
\text{job transitions},
\text{referral yields}
\right].
```

Moment choice is economic. If the counterfactual changes cross-group referrals, the model must fit segregation, degree heterogeneity, referral success, and match outcomes across groups. If the counterfactual changes diffusion, clustering, path length, seed reach, and adoption timing matter more. If the counterfactual changes platform visibility, congestion and substitution across search channels may be central.

Validation should be unusually explicit:

1. fit network topology, not only outcome regressions;
2. fit behavior conditional on links, not only link formation;
3. report which moments identify which primitives;
4. test sensitivity to alternative graph definitions from Lecture 18;
5. compare fixed-network and endogenous-formation counterfactuals;
6. use experiments or reduced-form designs from Lecture 19 as discipline when available;
7. state which counterfactuals are extrapolations beyond observed support.

### G. What Structural Network Models Add

Structural network models add value when they answer questions that the previous two lectures cannot answer alone.

**Counterfactual links.** What happens if workers receive subsidized access to contacts outside their usual referral neighborhood?

**Counterfactual information flows.** What happens if vacancy information reaches peripheral workers more reliably?

**Counterfactual matching sets.** What happens if a platform changes ranking, recommendations, or eligibility so that workers and firms see different feasible partners?

**Equilibrium behavior.** What happens if workers respond to others' search, adoption, referrals, or congestion?

**Welfare and distribution.** Do network policies increase total surplus, redistribute opportunities, or both?

The payoff is broader policy analysis. The risk is overclaiming. A structural network counterfactual is credible only when the formation and behavior assumptions are visible, empirically disciplined, and tied to the policy.

### H. Network Block Summary

```{include} assets/tables/20-network-block-summary.md
```

The network-methods literature is now strongest in three connected areas. First, researchers can measure richer worker, firm, neighborhood, school, platform, and referral networks from administrative and digital records. Second, causal work has clarified exposure mappings, interference, randomized saturation, graph experiments, and dyadic dependence. Third, structural work is increasingly able to model formation, search, referrals, diffusion, and equilibrium behavior, though usually with stronger assumptions.

The key open questions sit at the boundaries:

- how to combine credible reduced-form variation with structural counterfactuals that change links;
- how to validate endogenous formation models when unobserved relationships are important;
- how to model network policies that affect both efficiency and inequality;
- how to protect privacy while preserving economically meaningful network structure;
- how to handle dynamic networks where links, beliefs, and outcomes evolve together.

Future research opportunities are especially strong in labor settings with rich relational data: referral hiring, internal labor markets, coworker learning, platform matching, school-to-work transitions, manager networks, and local opportunity networks. The best projects will not be generic graph exercises. They will state the labor-market mechanism, build the network that corresponds to that mechanism, use credible variation where possible, and reserve structural assumptions for the counterfactuals that truly need them.

## Research Lab

The Week 20 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. No official replication data for the anchor papers are locally available in the repository.

The primary anchor is Mele's structural model of network formation [@mele2017structural], with Graham's degree-heterogeneity formation work as the econometric companion [@graham2017econometric]. The challenge anchor is Galenianos on referral networks and inequality [@galenianos2021referral], with Dustmann, Glitz, Schonberg, and Bruderl as a labor-search extension [@dustmann2016referral].

### Reproduce

Students reproduce a teaching-scale structural network workflow. They:

- generate a deterministic worker network with groups, occupations, skill, distance, and referral access;
- estimate a simple link-formation model using dyad characteristics;
- compute moments on degree, homophily, clustering, wage covariance across links, and referral yields;
- estimate a behavior-on-network equation for a network-mediated labor-market outcome;
- compare a fixed-network policy counterfactual with an endogenous-link counterfactual.

The goal is not to reproduce Mele's full estimator. The goal is to make the structural logic visible: formation moments discipline link primitives, behavior moments discipline outcome response, and counterfactuals depend on whether the graph is fixed or endogenous.

### Diagnose

Students diagnose the validation burden:

- which moments discipline homophily, degree heterogeneity, and referral productivity?
- does the model fit network topology and behavior conditional on links?
- how sensitive is the counterfactual to treating links as fixed?
- what unobserved meeting opportunities or strategic complementarities are omitted?
- which reduced-form facts from Lecture 19 would make the structural counterfactual more credible?

The output is a short validation memo, not a claim that the synthetic model is a frontier estimator.

### Transfer

Students transfer the workflow to a referral-search design inspired by Galenianos and Dustmann, Glitz, Schonberg, and Bruderl [@galenianos2021referral; @dustmann2016referral]. They:

- construct a referral opportunity set from synthetic workers and vacancies;
- simulate a policy that subsidizes cross-group referral links;
- compare match access, callback rates, and inequality under fixed and endogenous links;
- write a memo explaining what assumptions are needed for a real labor-market application.

The transfer task is deliberately concrete. Students should leave knowing how to move from a labor-market counterfactual to the network primitives and validation evidence needed to support it.

## Methods Box

### Practical Workflow For Structural Network Research

1. State the economic question and the policy counterfactual.
2. Define the network object: nodes, links, direction, weights, timing, and boundaries.
3. Decide whether the model is behavior on a fixed network, endogenous formation, or both.
4. Write the formation equation, behavior equation, welfare or outcome object, and equilibrium concept.
5. Identify which data variation or moments discipline each primitive.
6. Estimate the model using the simplest method that matches the counterfactual.
7. Validate topology, behavior conditional on links, and policy-relevant moments.
8. Compare fixed-network and endogenous-network counterfactuals.
9. Report assumptions that are not identified by the data.

### Common Failure Modes

- treating observed links as exogenous when policy changes the links;
- fitting degree distributions while missing the labor-market outcome that matters;
- using a peer-effects coefficient as if it identified a network redesign;
- matching homophily without explaining sorting, opportunity, or preferences;
- estimating a referral model without employer screening or applicant search response;
- presenting welfare conclusions without counterfactual validation;
- hiding privacy masking, missing links, or boundary truncation in the appendix.

## Reading Ladder And References

```{include} assets/tables/20-reading-architecture.md
```

**Core structural-network methods.** Start with Graham for the broad network-data map [@grahamNetworkData2019]. Then read Graham on degree heterogeneity and Mele on dense strategic formation [@graham2017econometric; @mele2017structural]. Chandrasekhar provides a handbook entry on econometrics of network formation [@chandrasekhar2016].

**Behavior, formation, and economic consequences.** Jackson, Rogers, and Zenou explain why network structure has economic consequences [@jacksonRogersZenou2017]. Bramoulle, Djebbari, and Fortin and Goldsmith-Pinkham and Imbens remain useful for connecting peer-effect identification to network structure [@bramoulleDjebbariFortin2009; @goldsmithPinkhamImbens2013].

**Labor-market search and referrals.** Calvo-Armengol and Jackson provide foundational models of networks, employment, wages, and inequality [@calvoarmengol2004effects; @calvoarmengol2007wage]. Dustmann, Glitz, Schonberg, and Bruderl, Galenianos, Pallais and Sands, and Barwick, Li, Rao, and Zahur connect referral and search networks to labor-market allocation and inequality [@dustmann2016referral; @galenianos2021referral; @pallais2016referrals; @barwickReferralsInequalityLabor2024].

**Frontier extensions.** Herskovic and Ramos study information acquired through peers [@herskovic2020acquiring]. Banerjee, Chandrasekhar, Duflo, and Jackson show that network structure can respond to policy exposure [@banerjee2024network]. Hafner, Massenot, and Smeets study reference production in labor-market relationships [@hafner2023working].

## Exercises And Discussion Prompts

1. Give one network-policy question where a reduced-form exposure estimate is enough and one where a structural network model is needed.
2. In a referral-hiring setting, distinguish a policy that changes outcomes conditional on existing links from a policy that changes link formation.
3. Write a simple formation equation for coworker advice links. Which primitives are about opportunity, preferences, and strategic payoffs?
4. What moments would you match if the counterfactual changes cross-group referrals? Which moments would matter less?
5. Why can two models with similar degree distributions imply different policy effects?
6. Design a validation table for a diffusion model of workplace training adoption.
7. Explain how Lectures 18, 19, and 20 would divide the work in a project on platform job recommendations.

## Reproducibility And Code Lab Note

The Lecture 20 code lab lives at `labs/20-structural-modeling-with-network-data/`. It uses deterministic synthetic data because no official replication data are locally available in the repository. The lab builds a small formation-and-behavior environment, estimates simple teaching models, compares fixed-network and endogenous-link counterfactuals, and transfers the logic to referral search.

The lab should not be read as evidence about real referral effects or the magnitude of network formation primitives. Its purpose is to make the structural workflow auditable: network definition, formation assumptions, behavior-on-network assumptions, moments, validation, counterfactual design, and limits are explicit.

## Slide Companion Note

The Lecture 20 slide deck is under `slides/week20/20-structural-modeling-with-network-data.tex`. It should define the question, explain when reduced-form network methods are not enough, contrast behavior on networks with endogenous formation, connect search and referrals to labor-market applications, isolate estimation and validation burdens, summarize the Network Methods block, and end with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Lecture 20 closes the Network Methods block. Students should now be able to separate three tasks: define the network object, identify causal effects through the network, and model counterfactuals that change the network itself.

The larger lesson of the course is methodological humility. A method is not credible because it is simple or structural, reduced-form or model-based. It is credible when the question, data, identifying variation, assumptions, validation, and counterfactual are aligned.
