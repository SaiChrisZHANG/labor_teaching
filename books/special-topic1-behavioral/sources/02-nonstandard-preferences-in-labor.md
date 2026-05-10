# Week 2 source pack — Nonstandard preferences in labor

## Week identity
- Course: Special Topic 1 — Behavioral Labor
- Week: 2
- Working title: **Nonstandard preferences in labor**
- Position in course: first substantive mechanisms week after the Week 1 framing chapter
- Role in sequence: isolates the **nonstandard preferences** branch of DellaVigna’s framework before later weeks move to beliefs, decision-making, firm responses, and policy design

## Topic boundary
This week should stay primarily in the worker-side topic family of **labor supply, effort, savings, and training**. That means the main applications should be:
- intertemporal labor supply and effort timing,
- workplace effort and performance,
- work-linked savings behavior,
- training or self-investment under self-control problems.

Occupational sorting, broad market allocation, and generic consumer-finance applications should not become the main storyline here.

## Central question
How do nonstandard preferences alter labor supply, effort, savings, and training, and how do labor economists identify those preference objects in applied work?

## Why this week matters
Week 1 establishes Behavioral Labor as a labor field rather than a list of biases. Week 2 should make that claim concrete. The point is not to catalogue every behavioral preference object. The point is to show students that a small set of preference departures—present bias, commitment demand, loss aversion/reference dependence, social preferences, and selected risk-related distortions—recur across central worker-side labor questions.

This week should therefore do four things clearly:
1. define the main nonstandard preference objects in a disciplined way;
2. map each object to labor supply, effort, savings, or training margins;
3. show how the literature identifies them empirically;
4. explain why welfare and policy interpretation become more delicate once worker preferences are nonstandard.

## Structure to aim for in the chapter
1. opening orientation / why this week matters
2. **Core points** box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references

No default extension box is needed.

## Bridge
The chapter should open by reminding students of DellaVigna’s tripartite taxonomy from Week 1:
- nonstandard preferences
- nonstandard beliefs
- nonstandard decision-making

Then make the week-specific move explicit: Week 2 focuses only on the first branch. Students should come away understanding that many worker-side labor puzzles can first be read as preference problems before they are read as belief or information problems.

## Core points box: essentials to surface
- Nonstandard preferences matter in labor because workers make intertemporal choices about labor supply, effort, savings, and training.
- The same preference object can affect several worker-side margins at once: hours, performance, retirement saving, and self-investment.
- Labor economists operationalize these preferences through contract choice, effort response, savings take-up, training completion, and reference-point shifts.
- Welfare conclusions are harder than in standard labor models because observed choices need not reflect stable, time-consistent welfare rankings.

## Field Core: conceptual arc

### A. DellaVigna taxonomy with this week isolated
Start from the DellaVigna classification and explain that this week is about deviations from standard preferences, not about biased beliefs or limited attention. The discussion should rely on `[@dellaVigna2009]` and `[@dellaVigna2018]`.

### B. Present bias and self-control problems
Introduce a compact quasi-hyperbolic or present-bias object. The point is not a long behavioral-theory digression, but a clean statement that workers may value future effort, saving, or training plans ex ante and then underinvest ex post.

Suggested formal object:
```{math}
:label: eq:qhb-week2
U_t = u(c_t,\ell_t) + \beta \sum_{\tau=t+1}^{T} \delta^{\tau-t} u(c_\tau,\ell_\tau), \qquad \beta \in (0,1]
```

Then explain worker-side applications:
- effort under piece rates and deadlines;
- procrastination in completing work or training tasks;
- under-saving in workplace-linked savings environments;
- demand for commitment devices that discipline future effort or saving.

Use `[@kaurKremerMullainathan2010]` and `[@kaurKremerMullainathan2015]` as the main labor applications.

### C. Commitment demand
Make clear that commitment demand is not a separate “bias” so much as a revealed implication of self-control problems. Worker-side examples should include:
- demand for restrictive or high-powered work arrangements;
- savings plans or defaults that constrain future selves;
- structured training environments that reduce procrastination or noncompletion.

Use workplace and work-linked savings examples, not generic consumer-finance examples.

### D. Savings and self-control in labor-linked settings
This should be its own subsection rather than a side remark. Emphasize that saving behavior matters for labor economists when it is tied to employment, retirement systems, payroll deduction, or human-capital accumulation. The goal is to show that behavioral labor naturally includes workplace savings and intertemporal worker planning.

Use `[@madrianShea2001]` and `[@dufloGaleLiebmanOrszagSaez2006]` as practical anchors for how labor economists study work-linked savings behavior.

### E. Loss aversion and reference dependence
Introduce a simple reference-dependent utility representation. Emphasize that labor economists care because workers respond to wages, performance targets, and disappointments relative to reference points rather than only levels.

Suggested formal object:
```{math}
:label: eq:refdep-week2
u(x\mid r) = m(x) + \mu(m(x)-m(r)),
```
where losses relative to {math}`r` loom larger than gains.

Keep the applications worker-side:
- target earnings and target labor supply;
- performance responses to pay disappointment or shortfalls;
- reference points in work effort and training goals.

Use `[@koszegiRabin2006]`, `[@mas2006]`, and `[@crawfordMeng2011]`.

### F. Social preferences, reciprocity, and workplace effort
Explain that workplaces are relational environments, so social preferences matter for effort, morale, reciprocity, and cooperation. Keep this subsection focused on effort and performance rather than broader firm-organization topics.

Use `[@fehrSchmidt1999]` as a broad theoretical anchor and `[@dellaVignaListMalmendierRao2022]` as the central applied labor anchor.

### G. Risk-related preference differences: keep brief and worker-side
Risk aversion should be covered briefly, not as the main spine of the week. The relevant worker-side uses are:
- savings and precautionary behavior,
- willingness to accept variable compensation,
- training under uncertainty about returns.

Do not let this turn into a broad occupational-sorting lecture.

## How labor economists use these preference objects in applied work
This should be a dedicated synthesis subsection, not only scattered across the theory. Organize it as:
- **labor supply / effort timing** for present bias and self-control;
- **work-linked savings choice** for commitment and procrastination;
- **training/self-investment completion** for self-control and future-self problems;
- **performance targets and wage disappointment** for reference dependence;
- **gift exchange and workplace effort** for social preferences.

The point is to show students that preferences become labor economics when they are mapped to concrete worker-side margins: hours, effort, saving, completion, and productivity.

## Methods and identification points to include
The chapter should teach students to ask:
- what is the worker-side margin observed?
- what counterfactual is the design comparing?
- how is a preference object distinguished from beliefs, information, technology, or constraints?
- when is the evidence reduced-form and when is it structural / model-dependent?

Useful contrasts to surface:
- present bias vs liquidity constraints;
- low saving vs transaction costs or information frictions;
- reference dependence vs standard incentive effects;
- social preferences vs monitoring or repeated-game incentives.

## Welfare and policy paragraph to include
A dedicated subsection should explain why welfare interpretation is harder here. If workers are time-inconsistent, reference-dependent, or socially motivated, observed worker choices in labor supply, saving, or training may not reveal stable welfare rankings. This matters for:
- commitment devices;
- payroll saving defaults;
- training-completion policies;
- performance incentives and target setting;
- worker-focused behavioral policy design.

This subsection should foreshadow the later policy and equilibrium weeks.

## Research Lab
The research lab should be concrete, not generic.

### Replication / transfer spine
- Primary anchor: `[@kaurKremerMullainathan2010]` and/or `[@kaurKremerMullainathan2015]`
- Savings-side auxiliary anchor: `[@madrianShea2001]` or `[@dufloGaleLiebmanOrszagSaez2006]`
- Challenge anchor: `[@mas2006]`
- Optional extension anchor: `[@dellaVignaListMalmendierRao2022]`

### What students should diagnose
- What exactly is the preference object in the paper?
- What worker-side margin is actually observed?
- Could the result instead be rationalized by information, constraints, or standard incentives?
- What would change if welfare were evaluated from the ex ante vs ex post self?

### Transfer ideas
Keep these bounded and feasible:
- take a present-bias/commitment design and apply the same logic to training completion, application deadlines, or work scheduling;
- take a workplace-savings design and apply the same logic to another payroll-linked or default-based worker choice;
- take a reference-point design and apply the same logic to performance after wage, target, or evaluation changes;
- take a reciprocity design and apply the same logic to a small alternative effort setting.

## Candidate figures to encourage in the chapter draft
1. A DellaVigna taxonomy figure with the Week 2 “nonstandard preferences” branch highlighted.
2. A present-bias / commitment timeline for effort, savings, or training.
3. A reference-dependent utility schematic around a target/reference point.
4. A workplace reciprocity / gift-exchange conceptual map.

## Tables to use
- `assets/tables/02-preference-taxonomy-map.md`
- `assets/tables/02-labor-applications-map.md`
- `assets/tables/02-identification-and-welfare-map.md`

## Reading ladder

### Core framing
- `[@dellaVigna2009]`
- `[@dellaVigna2018]`

### Present bias / commitment / effort
- `[@frederickLoewensteinODonoghue2002]`
- `[@kaurKremerMullainathan2010]`
- `[@kaurKremerMullainathan2015]`

### Savings and commitment
- `[@madrianShea2001]`
- `[@dufloGaleLiebmanOrszagSaez2006]`

### Reference dependence / loss aversion
- `[@koszegiRabin2006]`
- `[@mas2006]`
- `[@crawfordMeng2011]`

### Social preferences / reciprocity
- `[@fehrSchmidt1999]`
- `[@dellaVignaListMalmendierRao2022]`

## Forward bridge
End by clarifying that Week 2 has treated behavior as a **preference problem** on worker-side margins: labor supply, effort, savings, and training. Week 3 will ask when labor behavior is instead driven by **beliefs, expectations, and perception**, especially in job search and labor-market decision environments.
