# Matching, Market Design, And Labor Allocation

## Learning Objectives

By the end of Week 1, students should be able to:

1. explain why centralized matching appears in professional entry labor markets when decentralized search creates congestion, early contracting, or unstable allocations;
2. define stability, thickness, congestion, timing, priority rules, strategy-proofness, fairness, and welfare as labor-market design objects;
3. distinguish the design problem from the algorithm used to implement a design;
4. translate a matching-theory question into an empirical labor-market project with data, counterfactuals, and welfare or fairness objects;
5. design a bounded research exercise that uses a professional labor market to compare centralized matching, timing rules, priorities, or counterfactual policies.

The central question is this: when do designed matching rules improve labor allocation relative to decentralized search and bargaining?

## Opening Orientation / Why This Week Matters

Labor economists often study markets that do not clear well through decentralized search, bilateral bargaining, and posted wages alone. In many professional entry markets, timing frictions, congestion, strategic early offers, and multidimensional preferences create systematic misallocation. Week 1 sets up the course by asking when explicit matching rules improve labor allocation relative to decentralized market interaction and how labor economists can turn these design questions into credible empirical research projects.

This is a theory-heavy opening week, but the theory has a labor-economics job to do. Stability is not only an abstract property of a matching. It is a claim about whether workers and employers have incentives to defect from the assignment. Thickness is not only market size. It is whether candidates and jobs are present at the same decision moment. Strategy-proofness is not only an incentive theorem. It shapes whether observed rank-order lists can be interpreted as preference data. Priority rules and fairness constraints are not only administrative choices. They change access to training slots, geographic staffing, and early-career opportunity.

:::{admonition} Core points
:class: important

- Matching design matters when labor markets are thick, congested, strategic, or institutionally constrained.
- Stability, thickness, timing, and strategy-proofness are labor-market objects because they shape who works where, when careers start, and how welfare is distributed.
- Professional entry markets such as medical residency, clinical psychology, specialist fellowships, and legal clerkships provide labor-economics anchors for market design.
- A strong empirical paper in this area links institutional detail to a measurable allocation problem, a counterfactual design change, and a welfare or fairness object.
- The lecture standard is translation: matching theory should become an applied research design rather than stopping at mechanism exposition.

:::

## Bridge

Labor II studied decentralized search, bargaining, monopsony, and regulation. This course starts where those lectures leave off: some labor markets solve congestion and strategic timing problems through explicit rules rather than relying only on decentralized offers and search. The question is not whether design replaces labor economics, but how labor institutions are engineered when decentralized allocation performs poorly.

The opening examples should remain labor markets. School choice and kidney exchange are important market-design settings, but this course asks how matching rules shape professional entry, staffing, career starts, wages, geographic placement, and worker welfare. Medical residency, clinical psychology, law clerkships, specialist fellowships, and public-service placement markets are therefore the natural anchors.

## Field Core

### Why Centralized Matching Appears In Labor Markets

In many labor markets, firms and workers cannot simply rank all options, make simultaneous offers, and wait for the market to clear. Offers take time, candidates must decide under uncertainty, and rejected offers create bottlenecks. These frictions make timing itself part of the allocation problem. The classic professional-entry examples are medical residency, clinical psychology, and judicial clerkships, where decentralized contracting historically produced unraveling, exploding offers, or inefficient timing [@rothPeranson1999; @rothXing1997; @niederleRoth2009].

A centralized clearinghouse can improve allocation when it:

- thickens the market by pooling participants at one time;
- reduces congestion from slow offer-response cycles;
- makes accepted offers more comparable across applicants and programs;
- shifts competition from timing to preferences, priorities, and capacities;
- creates a public rule that participants can evaluate, contest, and improve.

Centralization is not automatically efficient. A poorly designed centralized system can elicit strategic rankings, encode unfair priorities, leave important match dimensions outside the mechanism, or suppress wage competition. The key question is comparative: what failure in the decentralized labor market is the centralized rule meant to solve, and what new margins does the rule create?

```{include} assets/tables/01-professional-labor-markets-map.md
```

### Matching Rules As Labor Allocation Objects

A simple many-to-one matching model has applicants {math}`i \in I`, programs {math}`p \in P`, program capacities {math}`q_p`, applicant preferences over programs, and program priorities over applicants. A matching {math}`\mu` assigns each applicant either to one program or to no program and assigns each program no more than {math}`q_p` applicants.

A blocking pair is the basic instability object:

```{math}
:label: eq:matching-market-design-blocking-pair
\text{applicant } i \text{ and program } p \text{ block } \mu
\quad \text{if} \quad
p \succ_i \mu(i)
\quad \text{and} \quad
i \succ_p j
\text{ for some } j \in \mu(p),
```

with the analogous condition when program {math}`p` has an unfilled position. In words: an applicant and program that are not matched to each other would both rather be matched to each other than remain with the assigned outcome. In labor settings, this matters because blocking pairs are pressure points for renegotiation, early contracting, off-mechanism deals, and distrust in the clearinghouse.

The deferred-acceptance algorithm is one way to produce stable matchings under standard conditions. The economic object is broader than the algorithm. A labor economist should ask which side proposes, whether couples or contracts break substitutability, what priorities encode, whether wages are held fixed, and whether the data generated by the mechanism can support empirical analysis.

### Core Design Objects: Stability, Thickness, Congestion, Timing, And Priorities

The theoretical vocabulary of this field is useful because it disciplines what counts as a design problem.

**Stability.** A matching is unstable if a worker and employer who are not matched to each other would both prefer to be. In labor settings, instability matters because it predicts unraveling, renegotiation, dissatisfaction with centralized outcomes, and pressure to contract outside the rule [@rothPeranson1999].

**Thickness.** A market is thick when enough agents are present at the same time for good matches to be found. Thickness is not just scale; it is simultaneous participation at the relevant decision moment [@rothXing1997].

**Congestion and timing.** When decisions must be made before enough information arrives, firms may issue exploding offers and workers may accept prematurely. Timing rules are therefore part of labor allocation, not just administrative detail [@niederleRoth2009].

**Strategy-proofness.** A matching rule is strategy-proof for one side if truthful preference revelation is a dominant strategy. Strategy-proofness matters empirically because truthful reports can be interpreted as preference data more directly than strategically shaded reports.

**Priorities and fairness.** Priority rules matter because labor markets often involve constraints beyond pure bilateral choice: training slots, couples, quotas, geographic obligations, underserved-area needs, diversity goals, or public-service priorities [@rothPeranson1999; @kojimaPathakRoth2013]. A priority rule can be fair in one sense and allocatively costly in another, so the welfare object must be explicit.

```{include} assets/tables/01-core-design-concepts-map.md
```

### Fairness, Welfare, And Labor-Market Interpretation

A labor-market design can improve efficiency while redistributing rents or changing who gets priority. That is why welfare in these markets is not exhausted by aggregate match quality. Relevant labor objects include:

- training-slot access;
- rural or underserved-area staffing;
- career starts and early wage paths;
- the burden of strategic behavior;
- bargaining power at entry;
- whether certain groups systematically lose access under decentralized timing.

This is one reason professional entry markets are good teaching cases: the same mechanism that improves matching efficiency may also alter distributional outcomes, geographic staffing, wage-setting power, or the allocation of prestigious first jobs [@agarwal2015].

### From Theory To Empirical Design

This is where the course connects to applied labor economics rather than stopping at theory.

A credible empirical market-design project usually has five ingredients.

1. **Institutional detail.** The paper must describe the market rule precisely enough that a reader knows who submits preferences, who holds priority, when offers arrive, whether wages are fixed, and what options exist outside the mechanism.
2. **Market failure or design object.** The paper should name the failure: unraveling, exploding offers, congestion, unstable assignments, poor geographic staffing, wage suppression, strategic misreporting, or unequal access.
3. **Data on the mechanism.** The researcher needs data on preferences, priorities, matches, timing, outcomes, vacancies, rank-order lists, wages, locations, or post-match labor outcomes.
4. **Counterfactual design or policy comparison.** The analysis should compare designs: centralized versus decentralized matching, altered timing, changed priorities, quotas, subsidies, staffing incentives, or alternative clearing algorithms.
5. **Welfare, fairness, or allocation object.** The design needs an object such as match quality, geographic access, strategic burden, labor supply to underserved areas, early-career earnings, program staffing, or employer market power.

The key applied move is to treat the mechanism as labor-market design, not as a black-box institutional reform. The goal is to identify how the rule changes allocation and which workers, firms, programs, regions, or patients gain or lose from that change [@agarwal2017].

```{include} assets/tables/01-theory-to-empirical-bridge.md
```

### Methods And Data Map

Market-design evidence uses more than one empirical style. Some papers use institutional case evidence and engineering constraints; some exploit rule changes; some estimate preferences under stability assumptions; some simulate counterfactual policies. The right design depends on the object being measured.

```{include} assets/tables/01-methods-and-data-map.md
```

The practical lesson is that the data requirement comes from the theoretical object. A stability question needs enough information to diagnose blocking pressure. A congestion question needs timing and offer data. A priority-rule question needs eligibility, rank, capacity, and outcome data. A welfare question needs outcomes beyond the final assignment.

### Professional Labor Markets As Empirical Anchors

This week should keep labor markets, not generic matching examples, as the primary anchor.

Good labor-market anchors include:

- the National Resident Matching Program;
- clinical psychologists;
- gastroenterology and other specialist fellowship markets;
- law clerk labor markets;
- public-service placement markets;
- rural or underserved-area staffing systems.

These markets are useful because they exhibit the core design tensions in a way labor economists care about: timing and congestion, worker welfare and career starts, employer staffing, geographic placement, and the relationship between allocation rules and wages or labor supply [@rothPeranson1999; @rothXing1997; @niederleRoth2009; @ashlagiEtAl2023].

## Research Lab

The Week 1 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Roth and Peranson on the redesign of the medical residency match because it is central to labor-market matching design and feasible to translate into a bounded teaching exercise about stable matching, congestion, couples, and engineering constraints [@rothPeranson1999]. The challenge anchor is Agarwal on empirical and policy analysis in the medical match because it shows how matching design can become counterfactual labor-market policy analysis [@agarwal2015; @agarwal2017].

The lab is not an official replication package for either paper. It uses deterministic synthetic data to help students practice the empirical translation: institutional rule, market failure, observed mechanism data, counterfactual design, and welfare or fairness object.

**Reproduce.** Students implement a simplified centralized many-to-one match for a professional entry market. The object is not an exact NRMP replication. It is a transparent reproduction of the design logic: applicants and programs have preferences or priorities, programs have capacities, and a centralized rule produces assignments.

**Diagnose.** Students compare the centralized match to a stylized decentralized exploding-offer path. They diagnose match rates, blocking-pair pressure, applicant rank outcomes, program priority outcomes, unfilled slots, and service-priority placement. The purpose is to ask which labor-market problem the design solves and which distributional objects remain unsettled.

**Transfer.** Students redesign the exercise for a neighboring labor market such as clinical psychology, law clerkships, specialist fellowships, or rural public-service placement. The transfer memo must state the institution, failure mode, needed data, counterfactual design, and welfare or fairness object.

## Methods Box

:::{admonition} Methods Box: Turning Matching Theory Into Labor Evidence
:class: note

**Start from the institution.** Name the timing rule, capacity constraint, wage rule, outside option, and information structure before naming the estimator.

**Separate the design object from the algorithm.** Stability, strategy-proofness, congestion, priority, and fairness are economic objects. Deferred acceptance is one possible implementation.

**Let data needs follow theory.** Preferences require rank data or credible revealed-preference assumptions. Congestion requires timing data. Priority rules require eligibility and capacity data. Welfare requires outcomes after the assignment.

**State the counterfactual.** The comparison might be decentralized offers, a different clearing date, altered priorities, regional quotas, couples policies, subsidies, or a different capacity rule.

**Keep equilibrium response visible.** Workers and programs can change ranking, application, interview, and outside-option behavior when the rule changes.

**Do not equate stability with welfare.** A stable match can still raise fairness, wage-setting, geographic staffing, or distributional questions.

:::

## Reading Ladder And References

**Core framing.** Start with Roth and Peranson on redesigning the medical residency match, Roth and Xing on congestion and bottlenecks in decentralized professional labor markets, and Niederle and Roth on exploding offers and market culture [@rothPeranson1999; @rothXing1997; @niederleRoth2009].

**Applied empirical and policy bridge.** Read Agarwal on estimating preferences and policy analysis in the medical match, then use Ashlagi and coauthors for current debates over early versus single matches in residency transitions [@agarwal2015; @agarwal2017; @ashlagiEtAl2023].

**Broader theoretical context.** Use Gale and Shapley for the original stable matching result, Roth and Sotomayor for two-sided matching foundations, Roth's market-design overview, and Kojima, Pathak, and Roth for matching with couples and incentive complications [@galeShapley1962; @rothSotomayor1990; @roth2008; @kojimaPathakRoth2013].

## Exercises And Discussion Prompts

1. Why are thick labor markets especially vulnerable to timing failures?
2. In what sense is stability a labor-market outcome rather than only a theoretical concept?
3. How would you distinguish a design problem from a pure information problem?
4. What labor-market outcomes should be used to evaluate a centralized match beyond whether it produces stable assignments?
5. Choose a professional-entry labor market. What data would you need to measure preferences, priorities, matches, timing, and outcomes?
6. Design a credible empirical project that studies one labor-market design change using observable match or staffing data.
7. Suppose a rural-staffing priority improves underserved-area placement but lowers average applicant rank. What welfare and fairness objects should be reported?

## Reproducibility And Code Lab Note

The Week 1 code lab lives at `labs/01-matching-market-design-and-labor-allocation/`. It is a bounded synthetic teaching path, not an official replication of Roth and Peranson or Agarwal. The smoke path creates deterministic reduced data; runs a centralized many-to-one match; compares it to a stylized decentralized exploding-offer process; diagnoses stability, congestion, priority, fairness, and welfare objects; and transfers the design to neighboring professional labor markets.

The lab is conservative by design. It does not claim access to official NRMP rank-order lists, program files, confidential applicant records, or a full official replication package. Its goal is to make students practice the research-design architecture they can later apply to real institutional data.

## Slide Companion Note

The Week 1 slide deck lives at `slides/week1/01-matching-market-design-and-labor-allocation.tex`. The deck mirrors the chapter structure without duplicating the prose: it opens with why centralized matching appears in labor markets, isolates stability, thickness, congestion, timing, strategy-proofness, priorities, fairness, and welfare, anchors the discussion in professional-entry labor markets, and closes with the theory-to-empirical bridge and Research Lab workflow.

## Bridge Forward

Week 2 turns from the existence of matching rules to the markets where timing and congestion become acute: recruiting, unraveling, and the design of decentralized versus centralized entry. The key transition is from "why matching rules exist" to "how recruiting rules and timing institutions alter equilibrium behavior."
