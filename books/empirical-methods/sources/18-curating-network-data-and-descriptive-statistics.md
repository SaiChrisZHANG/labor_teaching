---
title: Curating Network Data and Descriptive Statistics
subtitle: Empirical Methods — Lecture 18
bibliography:
  - references.bib
---

# Curating Network Data and Descriptive Statistics

## Learning Objectives

By the end of this lecture, students should be able to:

1. Define network objects in ways that are economically meaningful rather than mechanically convenient.
2. Distinguish nodes, edges, weights, direction, bipartite structure, and dynamic networks.
3. Explain the main advantages and limitations of network data in applied economics.
4. Construct a defensible workflow for turning administrative, survey, platform, or relational records into usable network measures.
5. Interpret common descriptive statistics such as degree, centrality, clustering, connected components, and homophily with appropriate caution.
6. Diagnose the most common threats in network-data work: missing links, endogenous boundary choice, privacy constraints, and dynamic mismatch.

## Opening Orientation

Network data are attractive because many economically relevant relationships are not properties of isolated units. Jobs are found through contacts, information travels through neighborhoods and coworkers, firms recruit through referrals, and workers' opportunities often depend on who else is connected to whom. But network data are unusually fragile: the same raw data can imply very different economic objects depending on how researchers define nodes, edges, timing, and boundaries. This lecture therefore treats network curation as part of research design, not as a preprocessing step.

:::{admonition} Core points
:class: important
- Network definition is a substantive economic choice: who is connected to whom, when, and through what channel determines the estimand.
- Descriptive network statistics are useful only when their economic interpretation is clear.
- Missing links, dynamic mismatch, and endogenous network formation are first-order threats, not technical footnotes.
- Good network-data work makes construction choices transparent and ties them directly to the labor or economic mechanism of interest.
:::

## Bridge

Lecture 15 showed that spatial data work is difficult because geography is an empirical object, not a natural constant. Network data raise a parallel issue: relationships are not “given” either. Just as boundary choice shapes spatial estimands, node/edge definitions shape network estimands. Lecture 19 will move from descriptive network data to causal inference under spillovers and interference. This lecture stays one step earlier and asks how to build defensible network measures in the first place.

## Field Core

### 1. What is the empirical object?

Let units be indexed by \(i,j \in \{1,\dots,N\}\). A simple network is represented by an adjacency matrix
```{math}
:label: eq:adjacency
A_{ij} =
\begin{cases}
1 & \text{if there is a link from } i \text{ to } j, \\
0 & \text{otherwise.}
\end{cases}
```

If links have intensity, duration, or value, one may observe a weighted matrix \(W_{ij}\) rather than a binary matrix. If the network is undirected, \(A_{ij}=A_{ji}\); if it is directed, the ordering matters. In many economic settings the natural structure is bipartite:
```{math}
:label: eq:bipartite
B_{if} =
\begin{cases}
1 & \text{if worker } i \text{ is linked to firm } f, \\
0 & \text{otherwise.}
\end{cases}
```
Bipartite data arise naturally in worker–firm networks, student–school networks, applicant–vacancy data, and doctor–hospital assignment settings. One can project a bipartite network onto one side, but projections are lossy and often create spurious density. A worker–worker “coworker” network constructed from shared firms is already an econometric object, not the raw data.

### 2. Why use network data at all?

Network data are attractive when outcomes depend on relationships rather than only on own characteristics. In labor economics, classic uses include referral hiring, neighborhood job-information flows, coworker networks, and employer learning through repeated relational ties. Autor’s overview of job search channels emphasizes that labor markets are wired through multiple intermediated information routes, not just formal applications [@autorWiringLaborMarket2001]. Bayer, Ross, and Topa show that residential proximity and labor-market networks can generate strong local labor-market effects [@bayerRossTopa2008]. Beaman and Magruder use referral incentives to show that networks select workers for jobs rather than merely passing information randomly [@beamanMagruderWhoGetsJob2012].

The payoff from network data is that they let researchers move beyond “individual with covariates” models toward:
- information transmission,
- referral and trust,
- peer exposure,
- diffusion and learning,
- bargaining and influence,
- and unequal access to opportunity through relational channels.

### 3. Descriptive statistics are theory-laden

Common network summaries include:
```{math}
:label: eq:degree
d_i = \sum_j A_{ij}
```
for degree, and
```{math}
:label: eq:strength
s_i = \sum_j W_{ij}
```
for weighted degree (strength). But these are not economically interpretable without a theory of links. A high degree could mean social connectedness, employment intensity, low-quality mass connections, or merely broader observation windows. Centrality statistics may proxy information access in one setting and organizational hierarchy in another. Clustering can measure local redundancy or group closure, but its welfare implications differ sharply by context.

So the right question is never “which statistic should I report?” It is “what economic role do I think the network plays, and which network summary speaks to that role?”

### 4. Substantive choices in network construction

The central design choices are:

**Node definition.** Is the node a worker, household, student, firm, vacancy, manager, neighborhood, school, hospital, or organization?

**Edge definition.** What counts as a relationship? Referral, coworking, friendship, co-residence, kinship, board overlap, repeated transactions, text communication, application/interview flow?

**Direction.** Does the relationship transmit something asymmetrically (recommendation, supervision, information), or is it symmetric?

**Weight.** Is frequency, duration, monetary value, or communication intensity relevant?

**Timing.** Over what horizon is the link defined? A static yearly network may be inappropriate when outcomes depend on weekly or daily interactions.

**Boundary.** Which nodes are observed and which are missing? Neighborhood networks, firm rosters, school cohorts, online platforms, and administrative records each impose different truncation rules.

Each of these choices shapes the estimand. Network work is therefore especially vulnerable to hidden researcher degrees of freedom.

### 5. Main threats and limitations

#### Missing links and partial observation
Administrative data often omit informal ties; survey data miss weak ties; platform data miss off-platform interactions; employer records miss prior relationships formed elsewhere. Missing edges distort centrality, components, and estimated peer environments.

#### Endogenous network formation
Workers choose neighborhoods, schools, firms, and collaborators. The network is therefore often a joint outcome of sorting, not an exogenous environment. This is the most important conceptual reason not to over-interpret descriptive network patterns.

#### Dynamic mismatch
Outcomes may be observed at \(t\) while the relevant network was formed at \(t-2\) or changed sharply between \(t-1\) and \(t\). Static snapshots can easily mismeasure exposure.

#### Boundary and projection problems
Projected networks (for example worker–worker from common firm affiliation) may treat very different intensities as equivalent. Truncating the graph at a city, firm, or school boundary can create artificial components and distort exposure.

#### Privacy and confidentiality
Fine-grained network data are inherently re-identifiable. Network research often requires stronger disclosure control than standard panel-data work, especially when small groups or rare ties matter.

### 6. Practical rules for defensible network-data work

1. Start from the economic mechanism, not the available graph.
2. Document node, edge, direction, weight, timing, and boundary choices explicitly.
3. Show robustness to plausible alternative network definitions.
4. Avoid projecting a bipartite network unless the projection is economically justified.
5. Distinguish missing links from zero links whenever possible.
6. Be explicit about whether the network is a stock, a flow, or a sequence of relations.
7. Treat descriptive statistics as measurements of mechanisms, not outcomes in their own right.
8. Where privacy is severe, prefer reproducible aggregate exposure objects to unreproducible micro graphs.

## Research Lab

### Primary anchor paper

**Bayer, Ross, and Topa (2008)** [@bayerRossTopa2008]

This paper is a good anchor because it shows how a labor-economics question becomes a network-data question: what looks like a neighborhood effect in job outcomes can partly be a labor-market network effect if local residents are connected to employers or to one another in job-relevant ways.

### Reproduce

Rebuild a simple network exposure object from a reduced synthetic worker–neighborhood or worker–firm panel:
- choose nodes,
- define edges,
- compute degree / exposure / local connectedness,
- and reproduce one descriptive table or figure linking network exposure to employment outcomes.

### Diagnose

Ask what the constructed object actually measures:
- referral opportunities?
- sorting into opportunity-rich neighborhoods?
- common exposure to the same employers?
- mechanical co-location?

Then stress-test the construction:
- change the boundary,
- change the edge rule,
- compare binary vs weighted exposure,
- and assess how much the result depends on these choices.

### Transfer

Move the same workflow to a second setting:
- coworker networks inside firms,
- referral links in hiring,
- or student/cohort networks linked to later labor-market outcomes.

The transfer exercise should not be “run the same regression elsewhere,” but “redefine the network object for a different mechanism.”

## Methods Box

### Common network data sources
- administrative rosters (workers within firms, students within schools, patients within providers),
- linked employer–employee data,
- referral-program records,
- survey rosters / name generators,
- platform interaction logs,
- communication metadata,
- neighborhood or co-residence records,
- patent / board / collaboration data.

### Common descriptive objects
- degree / weighted degree,
- in-degree / out-degree,
- components,
- clustering coefficient,
- path length / reachability,
- homophily / assortativity,
- bipartite degree and projection-based exposure,
- local peer-share or referral-share measures.

### Practical cautions
- every summary depends on the graph you constructed,
- every graph depends on a node/edge/timing/boundary choice,
- every boundary choice creates missing data,
- every privacy restriction may distort the observed network.

## Reading Ladder And References

### Core framing
- [@autorWiringLaborMarket2001]
- [@bayerRossTopa2008]
- [@beamanMagruderWhoGetsJob2012]

### Network construction and labor applications
- [@barwickReferralsInequalityLabor2024]
- [@friebelWhatDoEmployee2020]
- [@hellersteinLaborMarketNetworks2015]

### Bridge to causal/network designs
- [@aronowSamiiEstimatingAverageCausal2017]
- [@atheyEcklesImbensExactPvalues2015]

## Exercises And Discussion Prompts

1. Give one labor question where a worker–worker network is the natural object, and one where a worker–firm bipartite network is better.
2. Why can a projection from worker–firm links to worker–worker ties create misleading exposure measures?
3. In a referral-hiring setting, what are the differences between “missing ties,” “unobserved ties,” and “no ties”?
4. Pick one centrality measure and explain what economic mechanism it could represent—and what it definitely does **not** represent without more structure.
5. Under what conditions should a network statistic be treated as an outcome versus an explanatory variable?

## Reproducibility And Code Lab Note

The accompanying code lab should use a **bounded synthetic teaching path** to show how node/edge definitions translate into descriptive objects. If official replication data for the anchor paper are not locally available, the lab should still let students:
- construct a graph,
- compute basic network summaries,
- and diagnose sensitivity to network-definition choices.

## Slide Companion Note

The slide deck should mirror the chapter structure and include:
- one slide on node/edge/bipartite notation,
- one slide on why network definition is substantive,
- one slide on data sources,
- one slide on descriptive statistics and interpretation,
- one slide on common pitfalls,
- and one slide on the Research Lab workflow.

## Bridge Forward

Lecture 19 will ask when network structure can be used for **causal inference** rather than just description. That requires moving from node/edge definitions to exposure mappings, interference, peer effects, and the identification conditions under which network dependence is a feature rather than a fatal problem.
