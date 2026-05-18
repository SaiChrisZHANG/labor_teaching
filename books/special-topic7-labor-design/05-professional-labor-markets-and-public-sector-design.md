# Professional Labor Markets And Public-Sector Design

## Learning Objectives

By the end of the week, students should be able to:

1. explain why professional and public-sector assignment systems are labor-market institutions rather than generic allocation algorithms;
2. compare centralized assignment, priority rules, service obligations, and wage rigidity across residency, teacher, public-service, and military labor markets;
3. describe how internal job ladders, promotions, training, and on-the-job search change the design problem after initial assignment;
4. analyze movement "in and out" of the public sector as a mechanism-design margin involving participation, selection, retention, and exit;
5. design a bounded empirical exercise that links a rule change to staffing, match quality, retention, career mobility, worker welfare, and public-service outcomes.

## Opening Orientation

Week 5 studies professional and public-sector labor markets as design laboratories. These markets are useful for labor economics because the allocation problem is unusually explicit: workers must be assigned to hospitals, schools, agencies, branches, offices, units, or training slots; wages are often rigid or compressed; service quality matters for people beyond the worker and employer; and public legitimacy requires fairness, transparency, and defensible priorities.

The central question is this: what can structured professional and public-sector labor markets teach us about mechanism design when staffing needs, career ladders, worker welfare, and public objectives all matter?

:::{admonition} Core points
:class: important

- Professional and public-sector labor markets reveal design problems that are often hidden in decentralized private labor markets: fairness, transparency, local staffing needs, service quality, and career formation.
- The same matching or priority rule can behave differently when outside options, wage rigidity, service obligations, training pipelines, staffing targets, and public objectives differ.
- Internal job ladders, promotions, training, and within-system mobility are part of market design because initial assignments affect later careers and because organizations can design the rules of internal movement.
- Entry into and exit from public employment are design margins. Pay scales, pensions, mission value, transfer rights, probation, and promotion systems all shape who enters, who stays, and who leaves.
- Military and teacher labor markets are not just examples. They are empirical laboratories where assignment rules, priorities, career incentives, and public objectives can be observed and evaluated.

:::

## Bridge

Weeks 1 and 2 studied centralized matching, congestion, timing, and unraveling. Week 3 moved inside employment relationships through contracts, screening, incentives, and moral hazard. Week 4 studied platforms and intermediaries that choose visibility, assignment, wage, and governance rules. Week 5 combines those tools in institutions where design choices are formal, consequential, and politically visible.

The bridge is direct. A residency match, teacher-placement system, public hiring process, civil-service ladder, or military branching mechanism is not just a matching problem. It is also a labor-supply problem, a career-formation problem, a training problem, a retention problem, and a public-service problem. Stability, strategy-proofness, and priority design remain useful. They do not settle the labor question by themselves.

## Field Core

### Professional Labor Markets As Design Laboratories

Professional and public-sector labor markets are structured environments where rules do work that wages and informal bargaining often do in private decentralized markets. Residency programs, teacher-placement systems, civil-service jobs, public-service fellowships, and military assignments commonly include:

- formal applications or preference lists;
- assignment or clearing rules;
- priority categories, eligibility constraints, or service obligations;
- compressed wages or administratively set pay scales;
- training pipelines and probation periods;
- promotion ladders, rotations, transfers, or internal bidding systems;
- retention, performance, and public-service objectives.

These features make the institutional detail central. A deferred-acceptance mechanism can look similar on paper across settings, but it is not the same labor institution if one setting has flexible wages and easy exit, another has wage compression and geographic staffing mandates, and another has long service obligations and branch-specific training.

```{include} assets/tables/05-core-design-concepts-map.md
```

### Staffing, Fairness, Transparency, And Public Objectives

A compact way to organize the week is to let the institution choose a rule vector

```{math}
:label: eq:week5-rule-vector
\rho = (A, P, C, L),
```

where {math}`A` is the assignment or clearing rule, {math}`P` is the priority system, {math}`C` is the contract or commitment environment, and {math}`L` is the internal ladder or mobility rule. The labor economist then asks how {math}`\rho` changes assignment, training, retention, promotions, entry, exit, and welfare.

Worker welfare in these markets is broader than initial placement:

```{math}
:label: eq:week5-worker-welfare
W_i(\rho) =
u_i(j_i)
+ \tau_i(j_i,\rho)
+ g_i(L,\rho)
- c_i(j_i,\rho)
- \lambda_i r_i(\rho)
+ b_i^{out}(\rho),
```

where {math}`u_i(j_i)` is utility from the assigned job or site, {math}`\tau_i` is training and human-capital value, {math}`g_i` is promotion or internal-mobility value, {math}`c_i` is search, relocation, effort, or service-obligation cost, {math}`r_i` is earnings or career risk, and {math}`b_i^{out}` captures outside options and future exit opportunities.

The public or organizational objective is also richer than match surplus:

```{math}
:label: eq:week5-public-objective
\max_{\rho} \; S(\rho)
= \text{match quality}
+ \text{staffing in priority sites}
+ \text{public-service output}
+ \text{retention}
- \text{unfairness or opacity costs}.
```

This formulation is only a guide. Its purpose is to discipline interpretation. If a reform raises average preference satisfaction but worsens staffing in hard-to-serve locations, the welfare claim is incomplete. If a priority rule improves staffing but increases exit or blocks career mobility, the design may fail dynamically.

### Army And Military Assignment As Structured Labor Markets

Military labor markets make the design problem especially clear because assignments, contracts, service commitments, branch priorities, training pipelines, and organizational staffing needs are all first order. A branch assignment is not only a job match. It determines training, peer networks, promotion paths, geographic mobility, future specialization, and retention.

The West Point and Army branching literature shows why matching with contracts matters in a real labor market. Branch-of-choice contracts combine assignment with additional service commitments, so the mechanism must handle preferences, priorities, and contractual terms at the same time [@sonmezSwitzer2013]. Redesigning the Army branching process makes priority design visible because organizational objectives and cadet preferences have to be encoded into the rule [@greenbergPathakSonmez2021]. Experimental evidence on deferred acceptance across Army officer labor markets then connects a mechanism change to match outcomes and implementation realities in a structured internal labor market [@davisGreenbergJones2026].

The labor lesson is not that one algorithm is universally best. It is that assignment design depends on the surrounding institution:

- service obligations change outside options and continuation values;
- branch-specific training changes the cost of mismatch;
- staffing targets change the meaning of efficiency;
- promotion systems make early assignments dynamically consequential;
- managers and workers may adapt through communication, ranking behavior, or internal search.

### Teacher And Public-Service Allocation As Empirical Design Laboratory

Teacher and public-service labor markets are a second anchor because they link worker assignment to public-service delivery. The central object is not only where workers want to go. It is whether students, clients, patients, or communities receive adequate staffing and whether workers have credible career paths.

Teacher assignment research shows how formal assignment design can incorporate school priorities, teacher preferences, and policy constraints [@combeTercieuxTerrier2022]. Evidence from Teach For America uses a professional/public-service placement setting to study how labor-market design can improve match outcomes while keeping school needs and teacher preferences visible [@davis2024tfa]. Public teacher recruitment evidence from Rwanda separates selection, effort, and retention under alternative contract designs, showing that public-service staffing depends on who enters as well as how workers perform after entry [@leaverOzierSerneelsSabarwal2021].

This is why Week 5 should not become "school choice for workers." Teacher assignment is a labor-economics problem because the assignment rule affects worker search, location choices, retention, effort, training, and public-service output. Wage rigidity and staffing mandates mean that nonprice rules may do much of the allocative work. Evidence on teacher pay and public-sector productivity reinforces the same point: pay scales, incentives, and assignment systems jointly shape labor allocation and service quality [@biasi2021; @bauDas2017].

### Internal Ladders, Training, And On-The-Job Search

Professional and public-sector labor markets do not end at initial assignment. Workers learn, rotate, promote, transfer, and sometimes search while already inside the system. Internal mobility can be rule-based, manager-mediated, seniority-based, priority-based, or partly market-like. Each design changes career incentives.

An internal ladder affects labor allocation through several margins:

- initial placements create training opportunities and credentials;
- probation and early evaluations affect later promotion eligibility;
- transfer rules determine whether mismatch can be repaired;
- internal job bidding changes on-the-job search;
- managerial discretion can incorporate local information but may reduce transparency;
- promotion rules affect effort, retention, and worker sorting.

Recent evidence on internal talent markets studies whether stable matching logic can be brought inside organizations, where workers and jobs already know something about each other and where managers retain authority [@cowgillDavisMontagnesPerkowski2025]. The Army assignment setting adds the same dynamic concern: a branch match affects training, future assignments, leadership development, and retention [@davisGreenbergJones2026]. Personnel-economics work more broadly reminds students that practices, promotions, and productivity are part of a connected labor system rather than separable administrative details [@hoffmanStanton2024].

On-the-job search is therefore not a side issue. In a structured public or professional market, an assignment rule can either create a path for workers to move toward better matches or lock early mismatch into the career ladder.

### Public/Private Outside Options And Movement In And Out

Public-sector design cannot be evaluated only among workers who remain inside the system. Workers decide whether to apply, accept, stay, transfer, or exit. Public jobs compete with private jobs through pay, job security, pensions, mission value, location, promotion prospects, and work rules. These outside options change the effective mechanism because a rule only matters for workers who participate and continue.

This is the "in and out" margin from a mechanism-design perspective:

- entry rules affect who joins the applicant pool;
- assignment rules affect who accepts the job;
- wage rigidity affects which types are willing to enter;
- service obligations affect continuation and exit;
- internal mobility affects whether workers stay after mismatch;
- pensions and job security affect retention over the life cycle;
- private-sector options affect sorting and wage pressure.

Evidence on public-sector labor flows and education decisions shows why this margin matters. Public employment is part of aggregate labor reallocation, not a closed administrative sector [@fontaineLobelRoux2020]. Public-sector wages and employment rules can affect education and occupational choices before workers ever appear in the public-sector applicant pool [@chassamboulliPavlopoulou2023].

## Research Lab

The Week 5 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Davis, Greenberg, and Jones because it places a mechanism change in a professional/public-sector labor market with measurable assignment outcomes and organizational constraints [@davisGreenbergJones2026]. The challenge anchor is Davis on matching Teach For America teachers to schools because it transfers the same design logic to a teacher/public-service setting where location, school needs, and public objectives are central [@davis2024tfa].

The lab is not an official replication package for either paper. It uses deterministic synthetic teaching data to preserve the logic of structured assignment, public priorities, internal career value, and retention without claiming access to confidential Army, school, or personnel records.

**Reproduce.** Students recreate a reduced market-level comparison between a deferred-acceptance-style assignment rule and a manager-directed assignment rule in a synthetic Army officer market. The output focuses on preference rank, priority alignment, hard-to-staff fill, predicted retention, and training/career value.

**Diagnose.** Students classify what the design identifies and what remains latent: worker preferences, unit priorities, manager information, service obligations, training fit, internal-mobility value, public objectives, and outside options. The key question is whether improved assignment is a worker-welfare improvement, an organizational staffing improvement, or both.

**Transfer.** Students adapt the same architecture to teacher placement, public-service recruitment, civil-service entry, internal talent markets, or public/private exit margins. The transfer memo must state the rule, labor margin, counterfactual design, data requirement, welfare object, public objective, and main threat.

```{include} assets/tables/05-reading-and-lab-map.md
```

## Methods Box

:::{admonition} Methods Box: Evaluating Structured Labor-Market Design
:class: note

**Name the rule.** Is the study changing assignment, priorities, contracts, service obligations, internal mobility, promotion rules, or wage/incentive rules?

**Name the labor margin.** Does the rule affect preference rank, match quality, staffing, entry, acceptance, training, effort, retention, promotion, transfer, or exit?

**State the counterfactual.** What would the same workers and jobs have faced under the old rule or under a different priority system?

**Separate public objectives from worker welfare.** A reform can improve staffing while lowering worker utility, or raise worker preference satisfaction while worsening service access.

**Track dynamics.** Initial assignment, training, internal mobility, and exit are linked. A one-shot match-quality measure is often too narrow.

:::

```{include} assets/tables/05-methods-and-data-map.md
```

```{include} assets/tables/05-theory-to-empirical-bridge.md
```

## Reading Ladder And References

**Core matching and professional-market foundations.** Start with Roth and Peranson on redesigning the medical residency match, Roth and Xing on timing institutions, Niederle and Roth on gastroenterology with and without a centralized match, and Agarwal on empirical analysis of the medical match [@rothPeranson1999; @rothXing1994; @niederleRoth2003; @agarwal2015].

**Military and structured assignment.** Use Sonmez and Switzer for matching with branch-of-choice contracts, Greenberg, Pathak, and Sonmez for Army priority design, and Davis, Greenberg, and Jones for experimental evidence on deferred acceptance in Army officer labor markets [@sonmezSwitzer2013; @greenbergPathakSonmez2021; @davisGreenbergJones2026].

**Teacher and public-service allocation.** Use Combe, Tercieux, and Terrier for teacher assignment design, Davis for Teach For America teacher-school matching, Leaver et al. for public teacher recruitment contracts, Biasi for teacher labor markets under different pay schemes, and Bau and Das for public-sector pay/productivity misallocation [@combeTercieuxTerrier2022; @davis2024tfa; @leaverOzierSerneelsSabarwal2021; @biasi2021; @bauDas2017].

**Internal ladders and public-sector structure.** Use Cowgill et al. for internal talent markets, Hoffman and Stanton for modern personnel-economics practice, Fontaine, Lobel, and Roux for public-sector labor flows, and Chassamboulli and Pavlopoulou for public-sector employment, wages, and education decisions [@cowgillDavisMontagnesPerkowski2025; @hoffmanStanton2024; @fontaineLobelRoux2020; @chassamboulliPavlopoulou2023].

## Exercises And Discussion Prompts

1. Why might the same deferred-acceptance mechanism perform differently in residency, teacher placement, and military assignment?
2. Give one example in which a priority rule improves staffing but may reduce worker welfare. What data would you need to know the welfare effect?
3. How do service obligations change the mechanism-design problem in military labor markets?
4. In a teacher-placement system, what is the difference between improving worker preference satisfaction and improving public-service output?
5. How do internal job ladders and training pipelines change the interpretation of initial match quality?
6. When should managerial discretion be treated as useful private information, and when should it be treated as a threat to fairness or transparency?
7. How would you design an empirical test of whether a public-sector assignment reform changes entry, retention, or exit?
8. Choose one structured labor market. State the rule, labor margin, counterfactual, data requirement, worker-welfare object, public objective, and main threat.

## Reproducibility And Code Lab Note

The Week 5 code lab lives at `labs/05-professional-labor-markets-and-public-sector-design/`. It is a bounded synthetic teaching path, not an official replication of Davis, Greenberg, and Jones; Davis; Sonmez and Switzer; or any Army, school, public-service, or civil-service administrative system. The smoke path creates deterministic structured labor-market data; compares a deferred-acceptance-style assignment rule with a manager-directed assignment rule; diagnoses staffing, preference, training, retention, internal mobility, and outside-option margins; and writes transfer prompts for teacher placement, public-service recruitment, internal talent markets, and public-sector entry/exit.

The lab is conservative by design. It does not claim access to confidential personnel files, official assignment records, school placement systems, military branch preferences, or replication packages. Its goal is to help students practice how a professional/public-sector rule change becomes an empirical labor design.

## Slide Companion Note

The Week 5 slide deck lives at `slides/week5/05-professional-labor-markets-and-public-sector-design.tex`. The deck mirrors the chapter structure without duplicating the prose: it opens with professional and public-sector design principles, separates worker welfare from public staffing objectives, highlights Army assignment and teacher/public-service placement, brings in internal ladders and public/private movement, and closes with methods and the Research Lab workflow.

## Bridge Forward

Week 6 turns the whole course into empirical research design. The bridge is that Week 5 makes the full stack visible: matching rules, timing, contracts, platforms, internal ladders, public objectives, and worker outside options all appear in the same structured labor markets. The final week asks students to convert that stack into credible research designs with explicit mechanisms, counterfactuals, data requirements, and welfare claims.
