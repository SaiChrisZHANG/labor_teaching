# Week 3 Source Pack — Beliefs, Expectations, and Job Search

## Week identity

- Course: Behavioral Labor
- Week: 3
- Canonical chapter path: `books/special-topic1-behavioral/03-beliefs-expectations-and-job-search.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week3/03-beliefs-expectations-and-job-search.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/03-beliefs-expectations-and-job-search/`

## Central question

How do beliefs, expectations, attention, and limited information shape job search behavior, and how do labor economists identify these behavioral wedges empirically?

## Why this week matters

Job search is one of the most behaviorally rich domains in labor economics. Workers form beliefs about their employment prospects, choose how intensively to search, decide where to apply, interpret wages and job descriptions as signals, and often update their expectations slowly or imperfectly during unemployment spells. Employers, meanwhile, have limited information about worker skills and fit. This makes job search a natural setting for studying optimism, misperception, weak updating, application costs, and information interventions.

This week should make clear that behavioral job search is not a side topic or a niche add-on. It is a central modern literature linking subjective beliefs, job-search effort, information provision, and labor-market outcomes. The chapter should give students a structured way to think about how behavioral elements enter search through beliefs about job-finding, perceived competitiveness, self-knowledge about skills, and attention to job attributes.

## Position in the sequence

- Week 1 introduced the course-wide behavioral taxonomy.
- Week 2 treated nonstandard preferences in labor supply, effort, savings, and training.
- Week 3 now shifts to **beliefs, expectations, and search behavior**, with job search as the main object.
- This week should also foreshadow later discussions of information design, firm responses, and behavioral policy.

## Core takeaways to build around

By the end of the chapter, students should understand:

1. the benchmark search problem and where behavioral wedges can enter;
2. how subjective beliefs about job-finding probabilities, wages, and competitiveness shape search behavior;
3. why unemployment duration, weak updating, and optimism are empirically important;
4. how workers and firms respond to information provision and skill certification;
5. how posted wages, search costs, and perceived competition can alter applications in nonstandard ways;
6. how labor economists distinguish belief-based explanations from pure heterogeneity or standard search frictions.

## Required chapter architecture

Use the standard structure:

- opening orientation / why this week matters
- **Core points** box
- Bridge
- Field Core
- Research Lab
- reading ladder / references
- bridge forward to Week 4

No default extension box is needed.

## Bridge

The Bridge should do four things:

1. connect Week 2’s preference-based wedges to Week 3’s belief-based wedges;
2. remind students of the standard search framework from labor economics;
3. explain why job search is a natural domain for behavioral labor: repeated choices, uncertainty, feedback, and imperfect self-knowledge;
4. preview that later weeks will move from worker-side search behavior to firm, market, and policy responses.

## Core points box: essentials to surface

- Job search behavior depends not just on preferences, but on **subjective beliefs** about job-finding, wages, competitiveness, and skill fit.
- Behavioral wedges in search can appear as optimism, weak updating, limited information, misperceived competition, or application procrastination.
- Modern labor economics measures these wedges with elicited beliefs, information interventions, field experiments, and two-sided signaling designs.
- Job search is a crucial setting where behavioral labor meets unemployment duration, certification, wage posting, and policy design.
- Welfare and policy interpretation depend on whether observed search behavior reflects distorted beliefs, rational learning, standard frictions, or some combination.

## Field Core: conceptual arc

### A. Benchmark search problem

Start from a simple benchmark job-search problem that students recognize from labor economics. A clean object is:

```{math}
:label: eq:search-choice-week3
\max_{s_t,\bar{w}_t}\; p_t(s_t)\mathbb{E}\left[V^E(w)\mid w\ge \bar{w}_t\right] + \left(1-p_t(s_t)\right)V^U - c(s_t),
```

where {math}`s_t` is search effort, {math}`\bar{w}_t` is the reservation wage, {math}`p_t(s_t)` is the job-finding probability, and {math}`c(s_t)` is the cost of search. The chapter should explain that in the benchmark, workers choose search effort and reservation strategies using correct beliefs about job-finding and wage offers.

### B. Subjective beliefs and behavioral search

Then introduce the behavioral version, where the relevant probabilities or conditional distributions are subjective:

```{math}
:label: eq:subjective-search-week3
\max_{s_t,\bar{w}_t}\; p_t^{b}(s_t)\mathbb{E}^{b}\left[V^E(w)\mid w\ge \bar{w}_t\right] + \left(1-p_t^{b}(s_t)\right)V^U - c(s_t).
```

The key point is that search can be behaviorally distorted even when preferences are standard if workers hold biased or sticky beliefs. Use `[@dellaVigna2009]` and `[@dellaVigna2018]` to frame this within the broader behavioral taxonomy.

### C. Job-finding beliefs, duration dependence, and weak updating

This should be the first major empirical subsection. The chapter should explain why subjective beliefs about job-finding probabilities matter, how they predict search outcomes, and why they may be insufficiently updated over unemployment spells. Students should understand that job seekers can remain optimistic even as realized duration lengthens, and that this has implications for effort, reservation behavior, and welfare.

The main anchor here is `[@muellerSpinnewijnTopa2021]`.

### D. Information provision and search strategy

This subsection should focus on how job seekers respond when they receive advice, information, or motivation relevant to search. The main lesson is that search intensity and employment outcomes can respond to beliefs and strategy formation, not only to incentives. Use `[@altmannFalkJaegerZimmermann2018]` as the main anchor.

### E. Two-sided limited information and skill certification

A core contribution of the recent literature is that job search problems are often two-sided. Workers do not fully know their own relevant labor-market skills; firms do not fully know worker quality. Certification, assessment, and verifiable signals can therefore change worker beliefs, search strategy, and hiring decisions simultaneously.

Use `[@carranzaGarlickOrkinRankin2022]` as the main anchor.

### F. Perceived competition and wage signals

Students should see that posted wages do more than shift expected payoffs. Higher posted wages can also be interpreted as signals of competition or selectivity, changing application behavior in ways that a simple search model might miss. Use `[@belotKircherMuller2022]` as the main anchor.

### G. Search costs, application costs, and talent selection

This subsection should emphasize that behavioral elements also operate through perceived or salience-driven application costs. A small monetary incentive or reduction in search/application cost can have large effects on who applies and how firms recruit. Use `[@abebeCariaOrtizOspina2021]` as the main extension anchor.

### H. A historical bridge: impatience in job search

To connect the modern literature back to an earlier worker-side behavioral tradition, include a compact subsection on impatience and job search. The point is not to spend the week on preference-based search, but to show that behavioral labor has long recognized that search effort and reservation behavior may diverge from the exponential-discounting benchmark. Use `[@dellaVignaPaserman2005]` as the bridge anchor.

## How labor economists use these behavioral elements in applied job-search work

This should be a dedicated synthesis subsection. Organize it around margins:

- **beliefs about job-finding and duration** -> unemployment duration, effort, reservation behavior;
- **information about search strategies or prospects** -> search intensity, employment rates, unemployment exit;
- **skill certification and self-knowledge** -> application targeting, beliefs, hiring, earnings;
- **posted wages and perceived competition** -> attention, applications, self-selection;
- **application costs / frictions** -> who applies, who gets screened, and what firms learn.

The purpose is to show students that behavioral job search is not one narrow literature but a collection of applied designs tied together by a common framework.

## Methods and identification points to include

The chapter should explicitly teach students to ask:

- what belief or information object is being measured?
- what margin of job search is observed?
- what is the counterfactual: different beliefs, different information, different wage posting, different application costs?
- how do we distinguish beliefs from rational heterogeneity or search frictions?
- what remains structural or interpretation-heavy?

Useful contrasts to surface:
- optimistic bias vs rational selection on unobservables;
- weak updating vs true duration dependence in opportunities;
- low application rates vs high information or paperwork costs;
- wage sensitivity vs perceived-competition responses;
- worker-side misperception vs firm-side screening frictions.

## Welfare and policy points

A dedicated subsection should explain why welfare is subtle in behavioral job search. If job seekers are optimistic, inattentive, misinformed about their own skills, or misread job postings, then observed search choices do not necessarily reflect welfare-maximizing behavior. This matters for:

- information provision to job seekers;
- personalized job-search assistance;
- certification and assessment systems;
- wage transparency / posted wages;
- unemployment policy and search support;
- the interpretation of nonemployment duration.

This is also a place to foreshadow later Behavioral Labor weeks on policy design, firm responses, and equilibrium.

## Research Lab

The Research Lab should be concrete and empirical.

### Replication / transfer spine

- Primary anchor: `[@muellerSpinnewijnTopa2021]`
- Secondary / challenge anchor: `[@carranzaGarlickOrkinRankin2022]`
- Optional extension anchor: `[@belotKircherMuller2022]`
- Historical bridge anchor: `[@dellaVignaPaserman2005]`

### What students should diagnose

- What is the behavioral object in the paper: beliefs, expectations, information, competition perceptions, or search costs?
- How is it measured or manipulated?
- What search margin changes: effort, applications, duration, targeting, hiring, or wages?
- Could the result instead be explained by rational learning, search frictions, or standard selection?
- Is the design identifying a belief effect, an information effect, or both?

### Transfer ideas

Keep these bounded and feasible:

- adapt a belief-elicitation design to another job-search context or another population of unemployed workers;
- take a certification/information design and transfer it to another hiring or job-search environment;
- use a simplified dataset or simulation to study how wage signals alter applications under perceived competition;
- compare how job seekers with different subjective beliefs respond to the same labor-market information.

## Candidate figures to encourage in the chapter draft

1. A benchmark-vs-subjective search problem schematic.
2. A duration-dependence / weak-updating figure for job-finding beliefs.
3. A two-sided information / certification map.
4. A wage-signal / perceived-competition application figure.

## Tables to use

Use the following tables:

- `assets/tables/03-beliefs-and-search-map.md`
- `assets/tables/03-job-search-margins-map.md`
- `assets/tables/03-identification-and-design-map.md`

## Reading ladder expectations

### Core framing
- `[@dellaVigna2009]`
- `[@dellaVigna2018]`

### Behavioral job search foundations
- `[@dellaVignaPaserman2005]`
- `[@muellerSpinnewijnTopa2021]`

### Information provision and search strategy
- `[@altmannFalkJaegerZimmermann2018]`

### Two-sided information and skill signaling
- `[@carranzaGarlickOrkinRankin2022]`

### Perceived competition / wage posting
- `[@belotKircherMuller2022]`

### Application costs / selection extension
- `[@abebeCariaOrtizOspina2021]`

## Forward bridge

End by clarifying that Week 3 has treated job search as a behavioral domain driven by beliefs, expectations, information, and perception. The next week will move from worker-side wedges in search behavior to a broader set of labor-market decision environments shaped by attention, salience, complexity, and behavioral policy design.
