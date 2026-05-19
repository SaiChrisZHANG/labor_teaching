# Lecture 18. Curating Network Data And Descriptive Statistics

## Learning Objectives

By the end of this lecture, students should be able to:

1. define network objects in ways that are economically meaningful rather than mechanically convenient;
2. distinguish nodes, edges, weighted links, directed links, bipartite networks, and multilayer or relational settings;
3. explain why network definition is a substantive economic choice that shapes the estimand;
4. describe why network data are useful for studying referrals, information transmission, coworker exposure, neighborhood job information, learning, bargaining, and inequality;
5. compute and interpret common descriptive network statistics without treating them as causal evidence;
6. diagnose missing links, endogenous network formation, boundary choices, homophily versus influence, privacy risk, and dynamic mismatch;
7. design a reproducible workflow for building defensible network data in applied economics.

## Opening Orientation

Lecture 18 opens the optional network-methods block. The central question is: **how should researchers define, measure, and summarize the relationships that shape economic outcomes?** Jobs are found through contacts, referrals, neighborhoods, coworkers, schools, managers, and platforms. Information travels through relationships. Learning and diffusion happen through repeated interaction. Bargaining power and inequality can depend on who has access to valuable contacts, which firms recruit through which channels, and whether workers are embedded in opportunity-rich networks.

The practical work can look like building an adjacency matrix, projecting a worker-firm panel into coworker links, cleaning referral records, using survey name generators, or computing degree and centrality. But the economic work is deeper. The researcher is deciding what counts as a relationship, when it exists, how strong it is, whether it is directional, and where the observed network ends.

This lecture is deliberately parallel to Lecture 15. Spatial data were not "just GIS" because place, boundary, distance, and exposure choices shaped the empirical object. Network data are not "just graph construction" for the same reason. A node definition, edge rule, time window, and graph boundary can change what the estimated variable means.

The paper spine is labor-facing. Autor describes how job search became wired through multiple information channels rather than only conventional applications [@autorWiringLaborMarket2001]. Bayer, Ross, and Topa use residential proximity to study informal hiring networks and labor-market outcomes [@bayerRossTopa2008]. Beaman and Magruder show that referral incentives affect which workers are selected for jobs [@beamanMagruderWhoGetsJob2012]. Friebel, Heinz, Krueger, and Zubanov study employee referral programs as a management practice [@friebelWhatDoEmployee2020]. Barwick, Li, Rao, and Zahur connect referrals to inequality in labor markets [@barwickReferralsInequalityLabor2024]. Hellerstein, McInerney, and Neumark use labor-market networks to understand recovery from mass layoffs [@hellersteinLaborMarketNetworks2015].

The lecture's claim is conservative. Network curation is not network causal inference. It does not solve the reflection problem, peer effects, interference, endogenous link formation, or sorting. But weak network curation can defeat any downstream design. If links are missing, boundaries are arbitrary, timing is wrong, or descriptive statistics are interpreted without a mechanism, the analysis will answer a different question from the one the paper claims to ask.

## Core Points

:::{admonition} Core points
:class: important

- Network definition is a substantive economic choice: node, edge, direction, weight, timing, layer, and boundary choices help define the estimand.
- A link is not only a data relation. It is a claim about information, trust, exposure, monitoring, search, bargaining, learning, or another economic channel.
- Bipartite and multilayer data should usually be preserved until the projection is economically justified.
- Descriptive statistics such as degree, strength, centrality, clustering, components, and homophily are theory-laden measurements, not automatic mechanisms.
- Missing links, endogenous network formation, boundary truncation, homophily versus influence, privacy, and dynamic mismatch are first-order threats.
- Defensible network-data work reports alternative plausible graph definitions and separates measurement sensitivity from causal interpretation.
- Lecture 18 builds and diagnoses network objects. Lecture 19 asks when network structure can support causal claims.
:::

## Bridge

Lecture 15 opened the spatial block by asking what it means to turn places, borders, distances, and exposures into empirical objects. Lecture 18 asks the same upstream question for relationships. A network can make a labor-market mechanism visible, but only after the researcher states what a link means.

```{include} assets/tables/18-network-data-concepts-map.md
```

The bridge from earlier modules is direct. A DID design using coworkers as exposure units, a randomized referral experiment, a peer-effect study, a structural search model with contacts, or a platform-labor paper using message logs all inherit graph construction choices. If those choices are hidden, the estimand is hidden too.

Lecture 19 will move to causal inference with network data: peer effects, interference, exposure mappings, randomized saturation, and network experiments. Lecture 18 stays one step earlier. It asks whether another researcher can understand the graph, reproduce it, and evaluate whether the descriptive statistics match the economic mechanism.

## Field Core

### A. Network Notation And Empirical Objects

Let units be indexed by {math}`i,j \in \{1,\ldots,N\}`. A simple directed network can be represented by an adjacency matrix:

```{math}
:label: eq:em18-adjacency
A_{ij}
=
\begin{cases}
1 & \text{if there is a link from } i \text{ to } j, \\
0 & \text{otherwise.}
\end{cases}
```

If the network is undirected, {math}`A_{ij}=A_{ji}`. If the link is directional, {math}`A_{ij}` and {math}`A_{ji}` can mean different things. A worker can refer another worker without receiving a referral back. A manager can supervise a worker without being supervised by the worker. A senior coworker can transmit information to a junior coworker in a way that is not symmetric.

Many labor networks are weighted. Let {math}`W_{ij}` measure intensity, duration, frequency, value, or exposure strength. In a referral graph, {math}`W_{ij}` might be the number of referrals from worker {math}`i` to worker {math}`j`. In a coworker graph, it might be months of overlap. In a platform graph, it might be transaction value or message frequency. A binary link and a weighted link are different empirical claims.

Bipartite networks are often the natural raw object:

```{math}
:label: eq:em18-bipartite
B_{if}
=
\begin{cases}
1 & \text{if worker } i \text{ is linked to firm } f, \\
0 & \text{otherwise.}
\end{cases}
```

Worker-firm, student-school, applicant-vacancy, doctor-hospital, and worker-client relationships are bipartite. A one-mode projection can be useful, but it is a new constructed object:

```{math}
:label: eq:em18-projection
P^{worker}_{ij}
=
\sum_f B_{if}B_{jf}.
```

Equation {eq}`eq:em18-projection` says workers {math}`i` and {math}`j` are connected through shared firms. The caveat is immediate. Two workers who overlap in a small team for three years are not the same as two workers who appear in the same large firm for one month. Projection can inflate density, create artificial components, and mix coworker exposure with firm-level sorting.

Multilayer or relational settings add another dimension. Let {math}`A^{\ell}_{ij}` denote layer {math}`\ell`: coworker links, residential proximity, kinship, communication, school cohort, referral, or platform transaction. A single collapsed network,

```{math}
:label: eq:em18-layer-collapse
\tilde A_{ij} = \mathbf{1}\left\{\sum_{\ell} A^{\ell}_{ij} > 0\right\},
```

may be convenient, but it bundles different mechanisms. The substantive question should decide whether to keep layers separate, weight them, or collapse them.

### B. What A Network Variable Means Economically

A network variable is not automatically a measure of "social capital." It is a relationship-specific measurement claim. Before computing {math}`d_i`, centrality, clustering, or homophily, the researcher should be able to finish the sentence: **this edge represents the channel through which** ...

Examples in labor economics make the point:

- **Referrals.** A directed edge from employee {math}`i` to applicant {math}`j` may represent information about job openings, screening information about worker quality, trust, favoritism, or bargaining leverage. Beaman and Magruder show that the type of referral incentive changes selection into referred jobs [@beamanMagruderWhoGetsJob2012]. Barwick, Li, Rao, and Zahur connect referrals to inequality, so the relevant link is not merely "knows someone" but access to job-relevant recommendation channels [@barwickReferralsInequalityLabor2024].
- **Information transmission.** A neighborhood or coworker link may proxy job-information flow. Bayer, Ross, and Topa interpret residential proximity as a channel for informal hiring networks [@bayerRossTopa2008]. The link is meaningful only if the neighborhood boundary and timing plausibly capture information exchange.
- **Coworker exposure.** A worker-firm spell can generate coworker exposure, mentoring, monitoring, peer learning, or workplace norms. The edge rule should distinguish overlap in the same establishment, same occupation, same team, same manager, or same firm when those channels differ.
- **Neighborhood and job-information networks.** Residence-based links can matter because local contacts share employer information, commute knowledge, childcare constraints, or norms about work. They can also reflect sorting into neighborhoods. The descriptive variable must not silently treat sorting as influence.
- **Learning and diffusion.** Links can carry technologies, training, management practices, or job-search strategies. The time window matters because exposure must precede the outcome.
- **Bargaining and inequality.** Network position can shape outside options, access to vacancies, information about wages, and collective leverage. A central worker in a referral network may have different bargaining possibilities from an isolated worker, but only if centrality maps to job-relevant information or influence.

The same raw link can therefore mean different things across papers. A coworker tie in one project can be peer exposure; in another, a referral channel; in another, a firm fixed-effect proxy; in another, evidence of occupational sorting. The graph is part of the design.

### C. Why Network Data Are Useful For Labor Economics

Network data let applied researchers study mechanisms that are hard to see in isolated individual records.

**Search and referrals.** Formal job applications are only one route into employment. Autor emphasizes that labor-market matching depends on information channels, intermediaries, and technology [@autorWiringLaborMarket2001]. Referral data let researchers study who hears about vacancies, who is recommended, and how firms screen.

**Neighborhood job information.** Bayer, Ross, and Topa make neighborhood proximity relevant because workers living near one another may share information about jobs and employers [@bayerRossTopa2008]. The network object helps move beyond a generic neighborhood effect toward a labor-market channel.

**Coworkers and organizations.** Linked employer-employee data can reveal exposure through workplaces, teams, and managers. The link may carry information, norms, training, job ladders, or screening signals. The same data can also reveal limits: a firm roster observes organizational co-presence, not every informal relation.

**Learning and diffusion.** Networks can show how practices, beliefs, or technologies spread through firms, schools, villages, platforms, and occupations. Descriptive diffusion patterns are useful, but causal claims require stronger assumptions taken up later.

**Bargaining and inequality.** Network access is unequally distributed. Referral channels can advantage already connected workers or transmit inequality across groups. Barwick, Li, Rao, and Zahur make the distributional stakes explicit [@barwickReferralsInequalityLabor2024]. Hellerstein, McInerney, and Neumark show how labor-market networks can matter during recovery from displacement [@hellersteinLaborMarketNetworks2015].

**Model discipline.** Network measures can discipline structural or equilibrium models of search, referrals, peer effects, and formation. But they do so only when the measured graph corresponds to the theoretical relation in the model.

### D. Practical Data Sources And Construction

```{include} assets/tables/18-data-sources-and-network-definitions.md
```

The construction workflow should begin from the economic mechanism and then move to data.

**Linked employer-employee records.** These data are powerful for worker-firm bipartite graphs, coworker projections, manager exposure, firm-to-firm mobility, and displacement networks. The main limitation is that they usually observe employment relations, not friendship, advice, or informal job-information ties outside the administrative frame.

**Referral-program records.** Referral logs often have clean direction and timing: employee {math}`i` referred applicant {math}`j` for vacancy {math}`v` at date {math}`t`. They are excellent for studying formal referral mechanisms. They miss informal referrals, unrecorded recommendations, and off-system contacts.

**Surveys and name generators.** Survey rosters can capture friendship, kinship, advice, support, and job-search contacts. They provide mechanism-rich links but suffer from recall error, survey boundaries, respondent fatigue, and missing weak ties.

**Platform and communication logs.** Online labor platforms, internal messaging, and collaboration systems provide high-frequency interaction data. These links are behaviorally rich but mediated by platform rules, privacy constraints, and changing interface design.

**School, cohort, and neighborhood rosters.** These create peer and exposure networks for students, residents, and cohorts. The challenge is that co-presence is not necessarily interaction, and assignment to groups is often endogenous.

**Professional, patent, board, and collaboration data.** These networks are useful for knowledge diffusion, entrepreneurship, innovation, and elite labor markets. They often capture visible formal relationships while missing informal advice and unobserved collaboration.

The practical rule is to preserve the closest raw relational object. If the data start as worker-firm spells, keep the bipartite spell table. If the data start as referrals, keep the directed edge list with dates and vacancies. If the data start as survey names, keep roster structure and nonresponse. Derived projections and statistics should be reproducible products, not replacements for the raw relation.

### E. Descriptive Statistics Are Theory-Laden

Common network summaries are useful because they compress relational structure. They are dangerous because the same statistic can have different economic meanings across graph definitions.

Degree is:

```{math}
:label: eq:em18-degree
d_i = \sum_j A_{ij}.
```

In a job-referral network, out-degree may measure how many people worker {math}`i` refers. In-degree may measure how many referral opportunities worker {math}`i` receives. In a coworker projection, degree may mostly measure firm size unless the graph is normalized or constructed within teams.

Weighted degree or strength is:

```{math}
:label: eq:em18-strength
s_i = \sum_j W_{ij}.
```

Strength can be better than degree when exposure intensity matters. It can also hide concentration. A worker with one very strong tie and a worker with many weak ties can have the same strength but very different information environments.

Eigenvector-style centrality summarizes whether a node is connected to well-connected nodes:

```{math}
:label: eq:em18-centrality
c_i = \lambda^{-1}\sum_j A_{ij}c_j.
```

Centrality can proxy access to information or influence in some settings. In others it proxies organization size, survey visibility, or platform activity. It should not be interpreted without a theory of how paths transmit economic content.

Local clustering asks whether a node's neighbors are connected to one another. High clustering can mean trust and repeated local interaction. It can also mean redundant information and closed opportunity sets. Components describe disconnected subgraphs. They matter when job information, disease, technology, or norms cannot travel across gaps. But artificial components can be created by truncating the observation frame.

Homophily and assortativity summarize whether linked nodes are similar. A simple group-homophily measure is:

```{math}
:label: eq:em18-homophily
H
=
\frac{\sum_i \sum_j A_{ij}\mathbf{1}\{g_i=g_j\}}
{\sum_i \sum_j A_{ij}}.
```

This statistic can describe segregation in job-information networks, referral access, or coworker exposure. It does not distinguish preference-based sorting, constraints, historical segregation, firm assignment, or influence. Homophily is a descriptive fact until the formation process is modeled or identified.

Bipartite projections deserve special caution. In worker-firm data, a worker with many projected coworkers may simply have worked at large firms. Normalization, time overlap, team definitions, establishment identifiers, and firm-size adjustment often matter more than the graph software.

### F. Common Mistakes And Diagnostic Checks

Network curation has failure modes that can change the economics.

**Missing links.** A missing link is not the same as a zero link. Administrative data may miss informal contacts, survey data may miss weak ties, and platform data may miss off-platform relations. Missing links distort degree, centrality, clustering, components, and exposure.

**Endogenous network formation.** Workers choose firms, neighborhoods, schools, friends, and collaborators. Firms choose whom to hire and which referral programs to use. The network is often a joint outcome with labor-market outcomes. Descriptive network differences should therefore be interpreted as structure to explain, not as exogenous variation.

**Boundary choices.** A graph can be truncated by city, school, firm, platform, industry, sample, or survey roster. Boundary truncation can create artificial isolates, alter centrality, and hide bridging links. Researchers should report the observed frame and sensitivity to plausible boundaries.

**Homophily versus influence.** Similar connected workers may influence one another, but they may also select into the same firm, school, occupation, neighborhood, or platform. Manski's reflection problem is the canonical warning for peer effects [@manski1993]. Lecture 18 treats this as a diagnostic issue; Lecture 19 treats it as an identification issue.

**Projection error.** Projecting bipartite data into one-mode links can create dense graphs that reflect shared institutions more than direct relationships. The raw bipartite relation should remain visible.

**Privacy and confidentiality.** Network data are unusually re-identifiable because relational patterns can reveal people even after names are removed. Disclosure control can remove rare links, suppress small components, aggregate nodes, or mask timing. These choices change the graph and must be documented.

**Time aggregation and dynamic mismatch.** A yearly coworker network may be too coarse if the mechanism operates during a short training period. A referral network measured after an outcome may be post-treatment. A static graph can miss entry, exit, churn, and changing exposure.

Diagnostic checks should be concrete:

1. report node and edge counts by period and source;
2. compare binary and weighted versions of the main exposure;
3. show sensitivity to alternative time windows and graph boundaries;
4. inspect isolates, components, high-degree nodes, and small cells;
5. compare raw bipartite statistics with projected graph statistics;
6. document link missingness separately from true zero links;
7. state what privacy masking changes about degree, strength, and components;
8. keep descriptive diagnostics separate from causal robustness.

### G. Rules Of Thumb For Defensible Network Work

```{include} assets/tables/18-practical-rules-and-pitfalls.md
```

For applied economics, the checklist can be sharpened:

1. state the labor-market mechanism before defining the graph;
2. define node, edge, direction, weight, time window, layer, and boundary separately;
3. preserve raw edge lists, bipartite spell tables, and survey rosters before projection;
4. build the primary network statistic and at least one plausible alternative;
5. report missing-link risk and the difference between unobserved and absent ties;
6. normalize projections when institution size mechanically creates links;
7. test whether descriptive patterns are driven by boundary truncation or a few hubs;
8. document privacy masking as a measurement choice;
9. avoid causal language until the design addresses sorting, interference, and reflection;
10. make the graph construction rerunnable from raw relational records.

### H. Where Curation Ends And Causal Inference Begins

Network curation produces empirical objects: edge lists, adjacency matrices, bipartite incidence matrices, layered graphs, exposure measures, degree, strength, centrality, clustering, components, and homophily. These objects are necessary for network research, but they do not identify causal effects by themselves.

After curation, a researcher may have a referral exposure, a coworker peer measure, a neighborhood job-information proxy, a platform interaction graph, or a centrality measure. Causal inference still requires assumptions about link formation, treatment assignment, peer effects, interference, timing, and inference under dependence. Bramoulle, Djebbari, and Fortin, Goldsmith-Pinkham and Imbens, Aronow and Samii, and Athey, Eckles, and Imbens all become more central once the researcher claims causal effects through network structure [@bramoulleDjebbariFortin2009; @goldsmithPinkhamImbens2013; @aronowSamiiEstimatingAverageCausal2017; @atheyEcklesImbensExactPvalues2015].

The right standard for Lecture 18 is therefore: can another researcher understand what relation was built, why it matches the economic mechanism, how sensitive it is to plausible graph definitions, and what errors remain before the causal design begins?

## Research Lab

The Week 18 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package.

The primary anchor is Bayer, Ross, and Topa [@bayerRossTopa2008]. It is a good teaching anchor because it asks how a labor-economics question becomes a network-data question: do nearby residents share job-relevant information that links neighborhoods to employers? The contrast and extension papers are Beaman and Magruder on referral selection, Barwick, Li, Rao, and Zahur on referrals and inequality, and Friebel, Heinz, Krueger, and Zubanov on formal employee referral programs [@beamanMagruderWhoGetsJob2012; @barwickReferralsInequalityLabor2024; @friebelWhatDoEmployee2020].

### Reproduce

Students reproduce a compact neighborhood-employer network exposure object from deterministic synthetic worker data. They:

- define workers, residential blocks, neighborhoods, firms, and worker-firm links;
- construct a neighborhood-employer bipartite object;
- project it into worker-level exposure to local contacts at the same employer;
- compute degree, weighted local employer exposure, components, and homophily diagnostics;
- estimate a simple descriptive relationship between network exposure and employment or wage outcomes.

The goal is not to replicate Bayer, Ross, and Topa's confidential data. It is to make visible how a residential labor-market network object is defined before any causal interpretation.

### Diagnose

Students diagnose what the constructed object actually measures:

- referral opportunities or common exposure to the same nearby employer?
- residential sorting into opportunity-rich blocks?
- mechanical co-location in large firms?
- neighborhood job-information flow or shared local shocks?
- true absence of ties or unobserved informal links?

They stress-test the construction by changing the boundary, changing the edge rule, comparing binary and weighted links, auditing missing-link risk, and comparing bipartite and projected summaries.

### Transfer

Students transfer the same curation logic to a directed referral-program setting inspired by Beaman and Magruder, Barwick, Li, Rao, and Zahur, and Friebel, Heinz, Krueger, and Zubanov. They:

- construct a directed employee-applicant referral edge list;
- compute in-degree, out-degree, referral success, and group composition;
- compare referral access across groups;
- write a short memo explaining what the directed link captures and what it misses.

The transfer task previews Lecture 19 without making a causal claim. The output is a documented graph and a design memo, not an estimated peer effect.

## Methods Box

### Data Sources And Descriptive Statistics

Common data sources include linked employer-employee records, referral-program logs, survey rosters, name generators, platform interaction logs, communication metadata, school cohorts, neighborhood or co-residence records, patents, boards, and collaboration data. Each source has a natural graph and a natural blind spot. Administrative rosters observe formal affiliation; surveys observe reported informal relations; platforms observe mediated behavior; communication logs observe interaction metadata but often not economic content.

Common descriptive statistics include:

| Object | What it measures | Useful for | Caveat |
|---|---|---|---|
| Degree | Number of links {math}`d_i=\sum_j A_{ij}` | Opportunity access, referral reach, peer exposure | Sensitive to observation window and institution size |
| Weighted degree / strength | Link intensity {math}`s_i=\sum_j W_{ij}` | Duration, frequency, value, exposure intensity | Can hide concentration in a few ties |
| In-degree / out-degree | Received versus sent links | Directed referrals, advice, supervision | Direction must match mechanism |
| Centrality | Position relative to connected nodes | Information access, influence, brokerage | Often confounds size, visibility, and activity |
| Clustering | Whether neighbors are connected | Local closure, redundancy, trust | Welfare meaning is context-specific |
| Components | Connected subgraphs | Reachability and isolation | Boundaries can create artificial components |
| Assortativity / homophily | Similarity among linked nodes | Segregation, referral inequality, sorting | Does not separate selection from influence |
| Bipartite projections | One-mode links induced by shared affiliations | Coworker or peer exposure | Projection can inflate density and erase mechanism |

The reporting standard is not to list every statistic. It is to report the smallest set that speaks to the paper's mechanism and to explain what each statistic cannot show.

## Reading Ladder And References

```{include} assets/tables/18-reading-architecture.md
```

**Core framing.** Start with Autor for a broad view of labor-market information channels and with Jackson for the general economics of networks [@autorWiringLaborMarket2001; @jackson2008]. Then read Bayer, Ross, and Topa as the main labor-network curation anchor [@bayerRossTopa2008].

**Referral and labor applications.** Beaman and Magruder, Friebel, Heinz, Krueger, and Zubanov, Barwick, Li, Rao, and Zahur, and Hellerstein, McInerney, and Neumark show how referral and labor-market network objects enter empirical labor research [@beamanMagruderWhoGetsJob2012; @friebelWhatDoEmployee2020; @barwickReferralsInequalityLabor2024; @hellersteinLaborMarketNetworks2015].

**Network econometrics bridge.** Manski, Bramoulle, Djebbari, and Fortin, Goldsmith-Pinkham and Imbens, Chandrasekhar, Aronow and Samii, and Athey, Eckles, and Imbens prepare students for Lecture 19's causal network methods [@manski1993; @bramoulleDjebbariFortin2009; @goldsmithPinkhamImbens2013; @chandrasekhar2016; @aronowSamiiEstimatingAverageCausal2017; @atheyEcklesImbensExactPvalues2015].

## Exercises And Discussion Prompts

1. Give one labor question where a worker-worker network is the natural object and one where a worker-firm bipartite network is better. What changes in the estimand?
2. Why can a worker-firm projection into worker-worker links create misleading exposure measures? Give one normalization or restriction that would improve the object.
3. In a referral-hiring setting, distinguish missing ties, unobserved ties, and true zero ties. Which one is most dangerous for interpreting degree?
4. Pick one centrality measure and explain what economic mechanism it could represent. Then explain what it definitely does not represent without more structure.
5. How would you diagnose whether a neighborhood network statistic is measuring information transmission rather than residential sorting?
6. Design a privacy-safe release for a network lab when the raw graph cannot be shared. What aggregate objects would you preserve?
7. Under what conditions should a network statistic be treated as an outcome rather than an explanatory variable?

## Reproducibility And Code Lab Note

The Lecture 18 code lab lives at `labs/18-curating-network-data-and-descriptive-statistics/`. It uses deterministic synthetic data because no official replication data are locally available in the repository. The synthetic path is deliberately small and student-facing. It lets students construct a graph, compute basic network summaries, diagnose sensitivity to network-definition choices, and transfer the workflow to a directed referral setting.

The lab should not be read as evidence about the magnitude of real referral or neighborhood effects. Its purpose is to make graph construction auditable: node definitions, edge rules, timing, weights, boundaries, missing-link risk, and privacy constraints are explicit.

## Slide Companion Note

The Lecture 18 slide deck is under `slides/week18/18-curating-network-data-and-descriptive-statistics.tex`. It should not duplicate the chapter. The deck should define the question, map node/edge/bipartite concepts, show why network definition is substantive, summarize data sources and construction rules, interpret descriptive statistics, isolate pitfalls and privacy risks, and end with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Lecture 19 asks when network structure can be used for **causal inference** rather than description. That requires exposure mappings, interference assumptions, peer-effect designs, randomized saturation or network experiments, and inference under dependence. The bridge is simple: Lecture 18 makes the graph defensible; Lecture 19 asks what can be learned causally once that graph exists.
