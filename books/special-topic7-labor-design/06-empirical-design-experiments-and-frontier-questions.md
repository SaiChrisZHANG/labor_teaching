# Empirical Design, Experiments, And Frontier Questions

## Learning Objectives

By the end of the week, students should be able to:

1. state the mechanism-first object moved by a design intervention;
2. translate theory into an empirical margin, counterfactual, and welfare object;
3. compare field experiments, audits, institutional pilots, administrative data, platform data, and structural evaluation;
4. diagnose equilibrium response, spillovers, and external-validity limits;
5. outline a publishable applied labor-market design project with a clear theory backbone.

## Opening Orientation

Week 6 turns the course into a research-design capstone. The earlier weeks studied matching rules, recruiting timing, contracts, platform allocation, wage rules, and public-sector assignment as labor-market institutions. The final week asks how to evaluate these designs credibly enough to support a theory-backed applied paper.

The central question is this: how can labor economists turn a design intervention into evidence about hiring, assignment, wages, effort, retention, worker-firm sorting, public staffing, and welfare?

:::{admonition} Core points
:class: important

- Labor-market design evaluation begins with the mechanism: name the rule, contract, ranking system, assignment process, timing norm, or information regime that changes behavior.
- A credible evaluation links that mechanism to an observable labor object such as match quality, vacancy yield, effort, wages, retention, staffing, training, or worker welfare.
- Counterfactuals matter because many design gains are relative to a different rule, not to a no-treatment world.
- Experiments, audits, pilots, administrative data, platform data, and structural models are complements. Each sees a different part of the design problem.
- Welfare claims require equilibrium diagnosis: who gains, who loses, whether surplus rises, and whether the result travels beyond the studied institution.

:::

## Bridge

The course began with centralized matching and labor allocation, then moved through recruiting congestion, incentive contracts, platform rules, and public/professional assignment. Week 6 puts those ingredients into one empirical architecture. A design change is not evaluated because it is elegant on paper. It is evaluated because it changes a labor-market object that matters for workers, firms, public agencies, clients, patients, students, or communities.

The key discipline is to resist the generic question "does the mechanism work?" The labor-economics question is more specific:

- Did the mechanism improve assignment quality, worker welfare, employer staffing, effort, wage setting, retention, or public-service output?
- Did it move the intended margin, or did agents adapt on another margin?
- Is the estimate local to one institutional pilot, or does it reveal a portable labor-market mechanism?

This is why Week 6 is a capstone rather than a generic econometrics lecture. Identification tools enter only after the economic object is named.

## Field Core

### What A Credible Labor-Market Design Evaluation Looks Like

A credible evaluation has five connected layers:

1. **Institutional mechanism.** Which rule, contract, timing protocol, ranking algorithm, assignment system, priority structure, wage rule, or disclosure policy changed?
2. **Labor-market object.** Which observable labor margin should respond if the theory is right?
3. **Empirical leverage.** What variation identifies the effect: randomization, rollout, cutoff, policy change, administrative rule, or structural restriction?
4. **Equilibrium diagnosis.** What spillovers, strategic responses, reallocation, or market-wide adjustments can change interpretation?
5. **Welfare interpretation.** Does the design create surplus, redistribute rents, change bargaining power, or shift risk?

```{include} assets/tables/06-research-design-template.md
```

The first two layers should be written before choosing an estimator. A platform ranking experiment, a teacher-assignment reform, and a residency matching counterfactual may all use different methods, but each must state what the rule moves and why that object is economically meaningful.

### Theory-To-Empirical Translation: Mechanism, Margin, And Counterfactual

Mechanism-first design means beginning with the institutional object rather than the available dataset. Examples from the course include:

- a deferred-acceptance rule that changes match stability and strategic ranking;
- an application cap or signal that changes recruiting congestion;
- a bonus contract that changes effort, sorting, or multitasking;
- a platform visibility rule that changes attention and wage bargaining;
- a public assignment priority that changes staffing and worker career starts.

The empirical translation can be summarized as:

```{math}
:label: eq:week6-design-translation
\text{design rule}
\rightarrow
\text{behavioral margin}
\rightarrow
\text{labor outcome}
\rightarrow
\text{welfare object}.
```

The counterfactual is often the hardest step. In matching markets, the comparison may be the old algorithm, a decentralized offer process, a modified priority rule, or a capacity expansion. In recruiting, it may be a different timing rule or information structure. In contracts, it may be a different monitoring technology or pay formula. In platforms, it may be a ranking, disclosure, price, or fee rule. In public-sector assignment, it may be a different way to balance worker preferences and priority-site staffing.

A useful empirical decomposition is:

```{math}
:label: eq:week6-empirical-object
y_i(\rho) =
\underbrace{d_i(\rho)}_{\text{direct design effect}}
+ \underbrace{b_i(\rho)}_{\text{behavioral response}}
+ \underbrace{e_i(\rho)}_{\text{equilibrium adjustment}},
```

where {math}`\rho` is the design rule and {math}`y_i` is a labor object such as assigned rank, wage, effort, application behavior, retention, or public-service output. The evaluation must say which component it can identify and which component remains a threat.

### Field Experiments, Audits, And Institutional Pilots

Labor-market design is unusually well suited to experimental evidence because institutions often change rules explicitly. Field experiments can vary information, visibility, offer timing, wage posting, incentives, recommendations, priority status, or application costs. Platform experiments are especially valuable when the platform directly controls ranking, disclosure, pricing, invitations, or guarantees [@pallais2014; @horton2017].

Audits are useful when the design problem concerns screening, discrimination, information, or employer response. They can isolate a margin such as callback, interview, wage offer, or invitation. Their limit is that they often observe the first stage of the labor market rather than the full matching, contract, retention, or welfare outcome.

Institutional pilots sit between experiments and policy evaluation. A hospital match redesign, teacher-assignment reform, Army assignment pilot, public-service recruiting change, or platform rollout may create variation without pure individual randomization. These designs are powerful because the intervention is real. They are also fragile because the same reform can change applicant behavior, employer response, congestion, and expectations at once.

The design question should therefore be stated at the market level:

- What exactly was randomized, piloted, or changed?
- Which agents could respond?
- Which non-treated agents are affected through congestion or reallocation?
- What administrative or platform data show the process before final matches?
- What welfare object is observable, and what must be modeled?

### Administrative Data, Platform Data, And Structural Matching Models

Administrative and platform data matter because many design margins are invisible in standard surveys. Rich institutional data can reveal application sets, rankings, priorities, interview slots, offers, waitlists, wage bids, messages, algorithmic recommendations, acceptance, post-match outcomes, productivity, retention, and exit.

The empirical advantage is not just sample size. It is process visibility. Observing the recruiting funnel, preference lists, or platform exposure lets researchers ask whether the mechanism changed who applied, who was considered, who was offered, who accepted, and what happened after the match.

Structural matching and assignment models become especially useful when:

- the welfare object depends on unchosen matches;
- preferences, priorities, or strategic responses are only partly observed;
- policy counterfactuals change the feasible set or market-clearing constraints;
- the researcher needs to compare mechanisms that were not experimentally implemented.

Agarwal's empirical model of the medical match is the anchor example because it links observed matches to a model of preferences and then uses the model for policy counterfactuals [@agarwal2015]. The broader lesson is not that every design paper must be structural. The lesson is that the method should match the object. Reduced-form and experimental designs are strongest for local mechanisms; structural designs become more valuable when the question is counterfactual assignment, market-wide welfare, or mechanism portability.

### Welfare, Equilibrium Response, And Portability

Design interventions can improve a metric without improving welfare. A match may become more stable while wages fall. A platform rule may raise hiring rates while shifting risk to workers. A public assignment rule may fill priority sites while reducing worker welfare or retention. A contract may raise output while worsening multitasking or selection.

A welfare statement should say:

- whose welfare is counted: workers, firms, programs, clients, patients, students, public agencies, or taxpayers;
- whether the design creates surplus or reallocates surplus;
- whether the measured gain survives spillovers, congestion, or strategic response;
- which results are local to the institution and which mechanism is portable.

```{include} assets/tables/06-portability-and-relevance-map.md
```

External validity in this field should be argued through the mechanism, not through superficial institutional similarity. A residency match, an Army assignment system, a teacher placement process, and an online platform can all teach a portable lesson about constrained assignment, information, priority design, or timing. They do not imply the same welfare ranking unless outside options, wage setting, legal constraints, and equilibrium responses are comparable.

### Frontier Questions And Student Research Designs

The frontier of labor-market design is increasingly empirical. The strongest projects are institutionally specific but conceptually portable. They start from a rule that matters for work and then show how the rule changes behavior, allocation, and welfare.

```{include} assets/tables/06-where-the-field-is-and-where-it-is-going.md
```

```{include} assets/tables/06-frontier-project-opportunities-map.md
```

For student projects, a useful one-page design memo has seven parts:

1. the institution and rule;
2. the mechanism and behavioral margin;
3. the labor outcome and welfare object;
4. the available data and missing objects;
5. the source of variation;
6. the equilibrium or spillover threat;
7. the reason the mechanism travels beyond the case.

## Research Lab

The Week 6 Research Lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Agarwal's empirical model of the medical match because it is central to empirical evaluation in labor-market design: the paper turns observed matching outcomes into counterfactual policy analysis [@agarwal2015]. The challenge anchor is Davis, Greenberg, and Jones on deferred acceptance in Army officer labor markets because it pushes the design conversation into experimental evaluation of a structured labor-market assignment mechanism [@davisGreenbergJones2026].

The lab is not an official replication package for either paper. It uses deterministic synthetic teaching data to preserve the logic of matching, assignment, counterfactual welfare, and equilibrium diagnosis without claiming access to confidential residency, Army, platform, or public-sector data.

**Reproduce.** Students recreate a reduced matching counterfactual inspired by the medical match anchor. The script compares a decentralized early-offer rule with a deferred-acceptance-style rule and summarizes preference rank, priority alignment, match quality, shortage-site staffing, and welfare components. The object is not the full structural model. It is the data object that makes counterfactual evaluation meaningful.

**Diagnose.** Students classify what is identified directly and what remains latent: applicant preferences, program priorities, outside options, capacity constraints, strategic ranking, spillovers, and market-wide welfare. They then explain why an improvement in average assigned rank is not automatically a welfare improvement.

**Transfer.** Students adapt the same architecture to one frontier setting: platform ranking, recruiting timing, pay transparency, internal assignment, teacher placement, public-service staffing, or AI-assisted screening. The transfer memo must name the rule, mechanism, labor object, counterfactual, likely spillovers, data requirement, and welfare object.

## Methods Box

:::{admonition} Methods Box: From Mechanism To Design
:class: note

**Use an experiment when the mechanism can be moved directly.** Randomized visibility, offers, information, incentives, recommendations, or priorities are clean when the treated margin is narrow and spillovers are measurable.

**Use an audit when the first-stage response is the labor object.** Callback, interview, wage offer, or screening outcomes can be isolated, but later matching and retention usually remain outside the design.

**Use an institutional pilot when the rule is real and market-wide.** Pilots are valuable for assignment reforms, public staffing, platform redesign, and recruiting protocols, but the analysis must track spillovers and anticipation.

**Use administrative or platform data when the process matters.** Applications, rankings, offers, waitlists, bids, exposure, messages, and post-match outcomes help distinguish the mechanism from final-match correlations.

**Use structural evaluation when the counterfactual is unobserved.** Matching, assignment, and welfare counterfactuals often require modeling preferences, priorities, constraints, and equilibrium response.

:::

## Reading Ladder And References

**Matching redesign and empirical counterfactuals.** Start with Roth and Peranson on the residency match redesign, then read Agarwal on empirical policy analysis in the medical match [@rothPeranson1999; @agarwal2015].

**Recruiting, timing, and market process evidence.** Use Roth and Xing and Niederle and Roth for timing institutions, unraveling, and centralized clearing in professional labor markets [@rothXing1994; @niederleRoth2003; @niederleRoth2009].

**Experiments and platform data.** Use Pallais for field-experimental evidence on entry-level online labor markets, Horton for algorithmic recommendations, and Horton, Rand, and Zeckhauser for online labor-market experimentation [@pallais2014; @horton2017; @horton2010online].

**Public/professional and internal assignment.** Use teacher assignment, Teach For America matching, and Army assignment to see how design evaluation changes when staffing, public objectives, and worker careers are central [@combeTercieuxTerrier2022; @davis2024tfa; @davisGreenbergJones2026].

**Welfare and policy extensions.** Use Agarwal's policy-analysis bridge and the course's platform and public-sector papers to think about portability, equilibrium response, and welfare interpretation [@agarwal2017; @barachHorton2019steering; @horton2025minimumWage; @leaverOzierSerneelsSabarwal2021].

## Exercises And Discussion Prompts

1. Pick one design intervention from Weeks 1-5. Write down the mechanism, behavioral margin, labor object, counterfactual, spillover threat, and welfare object.
2. Compare a field experiment and a structural model for the same assignment problem. What does each identify, and what must each assume?
3. Suppose a platform changes ranking, wage disclosure, and invitation messages at the same time. Which labor outcomes can be measured directly, and which require stronger assumptions?
4. Design an audit for a recruiting or screening rule. What can the audit teach, and what does it miss about match quality or retention?
5. A public-sector assignment reform improves priority-site staffing but lowers worker preference satisfaction. What data would you need before making a welfare claim?
6. Write a one-page research memo for a publishable applied labor-market design project. It must include the rule, theory mechanism, empirical leverage, counterfactual, equilibrium threat, and welfare object.

## Reproducibility And Code Lab Note

The Week 6 code lab lives at `labs/06-empirical-design-experiments-and-frontier-questions/`. It is a bounded synthetic teaching path, not an official replication of Agarwal, Davis-Greenberg-Jones, or any confidential medical, military, platform, or public-sector assignment system. The smoke path creates deterministic teaching data, compares decentralized early offers with deferred-acceptance-style assignment, writes a compact counterfactual summary, diagnoses equilibrium and portability threats, and creates transfer prompts for frontier student projects.

The lab is conservative by design. It uses synthetic data because full replication access is uncertain and because the teaching goal is research architecture: mechanism, margin, counterfactual, equilibrium diagnosis, and welfare.

## Slide Companion Note

The Week 6 slide deck lives at `slides/week6/06-empirical-design-experiments-and-frontier-questions.tex`. The deck mirrors the chapter structure without duplicating the prose: mechanism-first empirical design, experiments/audits/pilots, administrative and platform data, structural matching and equilibrium evaluation, welfare and portability, and the Research Lab design.

## Bridge Forward

This course ends by turning institutional knowledge into research design. Students should leave able to begin with a labor-market design problem, state the mechanism, choose a credible empirical strategy, diagnose equilibrium response, and make a careful welfare claim. The frontier question is no longer whether labor-market institutions matter. It is how to measure what they do, for whom, and under which design environment.
