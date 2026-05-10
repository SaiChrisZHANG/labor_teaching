# Week 5 source pack — Incentives, contracts, reciprocity, monitoring, and workplace behavior

## Week identity

- Course: Behavioral Labor
- Week: 5
- Canonical chapter path: `books/special-topic1-behavioral/05-incentives-contracts-reciprocity-and-workplace-behavior.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week5/05-incentives-contracts-reciprocity-and-workplace-behavior.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/05-incentives-contracts-reciprocity-and-workplace-behavior/`

## Central question

How do nonstandard preferences and behavioral responses reshape incentives, contracts, monitoring, supervision, and workplace behavior inside firms, and how do labor economists distinguish treatment effects, selection, evaluation, and unintended consequences empirically?

## Why this week matters

This week is where Behavioral Labor visibly meets modern personnel economics. Standard labor models often treat the workplace as a clean incentive problem: firms choose contracts, workers choose effort, and outcomes reflect productivity plus incentives. The behavioral labor literature shows that this is incomplete. Workers respond to gifts, framing, fairness, social preferences, identity, and subjective interpretations of contracts. Firms do not simply choose “more incentives” or “less incentives”; they choose incentive environments, monitoring regimes, evaluation systems, disclosure rules, bonus timing, and relational gestures that can reshape effort, gaming, reciprocity, and retention.

Monitoring and supervision are especially important to make explicit. Incentives rarely operate in a vacuum. Piece rates, bonuses, and target pay are almost always interpreted through a regime of observation and evaluation. Objective monitoring can complement incentives by making effort or output visible; subjective supervision can instead redirect behavior toward influence activities, relationship management, or gaming. One of the frontier questions in behavioral labor is therefore not just whether workers respond to pay, but how pay, monitoring, supervision, and contract perception jointly shape workplace behavior.

This is also one of the most active frontiers of the literature. Classic gift-exchange evidence remains central, but the modern frontier asks sharper questions: what exactly is being estimated when gifts raise extra work but not productivity; when do loss-framed incentives backfire through gaming; when does monitoring complement incentives versus crowd out reciprocity; how should firms separate productive effort from supervisor-pleasing effort under subjective evaluation; and how do digital or algorithmic monitoring systems change the behavioral content of the employment relationship? That is why this week should feel like more than “behavioral biases at work.” It should teach students how behavioral objects enter contract design and workplace governance.

## Position in the sequence

- Week 1 introduced the course-wide behavioral taxonomy.
- Week 2 studied nonstandard preferences mainly through labor supply, effort, savings, and training.
- Week 3 focused on beliefs and job search.
- Week 4 treated attention, salience, complexity, and learning.
- Week 5 now shifts firmly inside the firm: incentives, contracts, reciprocity, monitoring, supervision, and workplace behavior.
- The week should also foreshadow Week 6 by showing how identity, norms, fairness, and workplace organization connect to broader labor-market allocation.

## Topic boundary

Keep the week labor-focused and workplace-focused. This is not a generic behavioral game theory week and not a generic personnel economics survey. The main objects should be:

- real effort and productivity,
- compensation packages and framing,
- reciprocity / gift exchange,
- monitoring and supervision,
- objective versus subjective evaluation,
- performance pay and sorting,
- fairness / contract perception,
- gaming and unintended contract responses,
- digital or algorithmic monitoring as a frontier extension.

The week can briefly mention mission/meaning or identity where they help explain workplace behavior, but it should not drift away from incentives, contracts, and employer–worker interactions.

## Core teaching goal

By the end of the week, students should be able to:

1. write down a benchmark incentive/effort problem and identify where behavioral wedges enter;
2. distinguish reciprocity, reference dependence, loss framing, monitoring, subjective evaluation, and contract perception as separate workplace channels;
3. explain why performance monitoring and supervision are not neutral add-ons but part of the behavioral environment of the firm;
4. understand the modern empirical literature on gift exchange, framed incentives, monitoring, subjective evaluation, performance pay, and workplace behavior;
5. articulate frontier research questions about contract design, gaming, heterogeneity, monitoring, and behavioral responses inside firms.

## Required chapter architecture

Use the special-topics standard:

- short opening orientation / why this week matters
- **Core points** box
- Bridge
- Field Core
- Research Lab
- reading ladder / references
- bridge forward to Week 6

Do not add an Extension / Optional Extension box by default.

## Bridge

The Bridge should do five things:

1. connect Week 2’s nonstandard preferences to the workplace by showing that the same primitives matter differently inside firms than in worker-side labor supply;
2. connect Week 4’s information/complexity issues to contract design and supervision, emphasizing that firms choose how legible incentives are and how workers are evaluated;
3. explain why this week sits at the boundary between behavioral labor and personnel economics;
4. make clear that monitoring and supervision are part of incentive design, not an afterthought;
5. preview that Week 6 will broaden from workplace contracts to identity, norms, and broader allocation/fairness issues in labor markets.

## Core points box: essentials to surface

- Incentive contracts are behavioral objects: workers respond not just to levels of pay, but to framing, reference points, reciprocity, fairness, and monitoring.
- Behavioral workplace responses show up in extra work, productivity, gaming, sorting, and compensation heterogeneity.
- Gift exchange and reciprocity can raise effort, but the margin affected need not be the same as productivity.
- Monitoring and supervision are not mechanically beneficial: they can complement incentives, crowd out reciprocity, or redirect effort toward gaming or influence.
- Subjective evaluation creates a distinct behavioral channel because workers may respond to supervisors rather than only to tasks or output.
- Modern empirical work must distinguish treatment, selection, contract choice, evaluation, and organizational responses.

## Field Core: conceptual arc

### A. Benchmark effort and contract problem

Start from a standard workplace benchmark in which a worker chooses effort {math}`e` under a compensation schedule {math}`w(y(e))`:

```{math}
:label: eq:benchmark-effort-week5
\max_{e \ge 0} \; u\!\left(w(y(e))\right) - c(e).
```

Explain that the benchmark assumes effort responds only through standard consumption utility and disutility of effort. In the simplest agency view, firms alter {math}`w(\cdot)` and workers move along the effort margin.

### B. Incentives plus monitoring

The next step should make monitoring explicit. Contracts operate under some evaluation technology. Let {math}`m` denote the monitoring regime or information technology faced by the worker:

```{math}
:label: eq:behavioral-contract-week5
\max_{e \ge 0} \; u\!\left(w(y(e),m)\right) - c(e) + B\!\left(g_i, r_i, f_i, s_i, m_i; e\right),
```

where {math}`B(\cdot)` collects behavioral channels such as generosity, reference points, framing, social preferences, and monitoring/evaluation salience.

The chapter should explain that monitoring is not just a technical input. It changes how workers interpret incentives, what outcomes become salient, and what dimensions of behavior are rewarded or punished.

### C. Reciprocity and gift exchange

This should be the first major empirical subsection. Use classic field evidence to show that workers can reciprocate employer generosity and that gifts can affect output differently from contract changes alone. The chapter should not stop at “gift exchange exists.” It should push students to ask:
- what margin moves (extra work, productivity, compliance, attendance),
- whether the worker responds to kindness, effort by the employer, or simply surprise,
- whether effects are short-lived or persistent,
- how gift exchange interacts with standard incentives and monitoring.

Use `[@kubeMarechalPuppe2012]` and `[@dellaVignaListMalmendierRao2022]` as core anchors. The latter is especially useful because it separates responsiveness of extra work from responsiveness of productivity.

### D. Reference dependence and loss-framed incentives

The next subsection should move from reciprocity to reference-dependent contracts. Workers may react differently to a bonus framed as something to gain versus something already possessed and at risk of losing. This should be presented as a behavioral contract-design problem, not merely a citation to prospect theory.

A clean formal object is:

```{math}
:label: eq:loss-framing-week5
U(e) = u\!\left(w(y(e))\right) - c(e) + \lambda \min\{0,\, b(e)-r\}.
```

The chapter should explain:
- why loss framing was initially appealing,
- why later work emphasizes hidden margins like gaming, multitasking, and distortion,
- why firms must care about total performance, not just target attainment,
- why monitoring intensity matters for whether loss framing bites on productive margins or gaming margins.

Use `[@hossainList2012]` as the classic factory-framing anchor and `[@pierceReesJonesBlank2025]` as the frontier corrective showing how loss-framed incentives can backfire.

### E. Monitoring, supervision, and subjective evaluation

This should be an explicit major subsection, not a footnote. Distinguish:
- objective monitoring of output or behavior,
- supervision with discretion,
- subjective performance ratings,
- algorithmic or digital monitoring.

A useful conceptual object is:

```{math}
:label: eq:subjective-evaluation-week5
\max_{e,a \ge 0} \; u\!\left(w\big(z(e), \hat q^S(e,a)\big)\right) - c(e) - \psi(a),
```

where {math}`a` denotes influence activity or supervisor-facing effort and {math}`\hat q^S` is a subjective evaluation.

This subsection should show students that monitoring and evaluation can shift effort toward production, compliance, or influence activities depending on what the supervisor sees and rewards. Key questions:
- does monitoring complement or crowd out intrinsic/reciprocal motivation?
- does supervision improve productivity or simply visibility of effort?
- when does subjective evaluation induce supervisor-pleasing rather than mission-oriented effort?
- how do digital or algorithmic monitoring tools change worker behavior?

Use `[@kelley2024monitoring]`, `[@deJanvrySadouletSuriWang2023]`, and `[@macleod2003subjective]` as explicit anchors.

### F. Performance pay, heterogeneity, and sorting

This subsection should show that behavioral workplace responses are heterogeneous and that observed pay-performance effects can combine treatment and sorting. The key labor-economics question is not only “does performance pay work?” but also:
- for whom,
- along which margin,
- under what evaluation or monitoring regime,
- and with what selection into contract types.

A useful reduced-form sorting object is:

```{math}
:label: eq:contract-sorting-week5
k_i^\star \in \arg\max_{k \in \mathcal{K}} \; \mathbb{E}\!\left[U_i\!\left(w_k(y_i(e),m), e\right)\right],
```

where workers choose among contract forms {math}`k`.

The chapter should explain why performance-pay evidence often mixes:
- direct treatment on existing workers,
- endogenous selection into jobs/contracts,
- heterogeneous responses across worker types,
- monitoring differences across workplaces.

Use `[@dellaVignaPope2018]` as the benchmark motivation map and `[@bandieraFischerPratYtsma2021]` as the modern heterogeneity/response-difference anchor.

### G. From motivating effort to distorting effort

This is a crucial integrative section. Behavioral contract design can raise effort, but it can also distort behavior:
- gaming of targets,
- multitasking distortions,
- low-quality output,
- undesirable task substitution,
- excess effort devoted to appearing productive,
- short-run effort with long-run cost.

Students should see that the frontier is increasingly about the quality and composition of effort, not just total output.

### H. Welfare and design implications

The welfare block should ask:
- when should firms use simple high-powered incentives,
- when do gifts or reciprocity dominate explicit pay changes,
- when does loss framing create hidden costs,
- when does stronger monitoring improve behavior and when does it crowd out valuable dimensions of work,
- how should firms weigh average treatment effects against heterogeneous responses and sorting,
- when is “better motivation” actually better workplace design?

This should end with the point that behavioral labor turns contract design into a richer empirical question about interpretation, heterogeneity, monitoring, evaluation, and unintended consequences.

## Methods and identification

This week should have a strong methods section. Students should be able to map the literature into clear empirical strategies:

1. **gift / generosity field experiments**
   - unexpected gifts,
   - monetary vs nonmonetary gifts,
   - changes in contract presentation,
   - measurement of extra work vs productivity.

2. **framing experiments in real workplaces**
   - gain vs loss framing,
   - prepaid vs postpaid bonuses,
   - target-based compensation with observable gaming margins.

3. **monitoring and supervision designs**
   - randomized monitoring intensity,
   - supervisor training or managerial-intervention designs,
   - objective versus subjective evaluation,
   - designs that reveal influence activities or nonproductive effort.

4. **real-effort experiments with contract variation**
   - benchmark motivation mappings,
   - comparison of monetary and behavioral motivators,
   - interpretation of behavioral treatment arms.

5. **sorting / contract-choice designs**
   - workers selecting into piece rates or performance pay,
   - separating treatment effects from composition effects.

6. **heterogeneity synthesis**
   - pooled or hierarchical evidence on differential responses,
   - implications for inequality and contract design.

The methods section should explicitly distinguish:
- treatment effects on current workers,
- selection into contracts/jobs,
- output versus productivity versus gaming,
- individual incentives versus social or relational channels,
- monitoring versus motivation,
- reduced-form treatment effects versus structural contract-design interpretation.

## Required tables to use

Use and cite the editable tables in the final chapter:

- `assets/tables/05-incentives-monitoring-and-supervision-map.md`
- `assets/tables/05-workplace-behavior-frontier-map.md`
- `assets/tables/05-identification-and-design-map.md`

## Research Lab

The Research Lab should train students to think like applied labor economists working on workplace behavior rather than just to summarize papers.

### Lab architecture

Use the standard structure:
- Reproduce
- Diagnose
- Transfer

### Primary lab anchor

Use `[@dellaVignaListMalmendierRao2022]`.

Why:
- it is behaviorally central,
- it is workplace-based,
- it distinguishes extra work from productivity,
- it is an excellent example of how labor economists operationalize reciprocity and social preferences.

### Secondary / challenge anchor

Use `[@kelley2024monitoring]`.

Why:
- it brings monitoring explicitly into the week,
- it lets students compare pay-based incentives with monitoring-based interventions,
- it helps them think about complementarities between compensation and supervision.

### Optional frontier extension

Use `[@deJanvrySadouletSuriWang2023]`.

Why:
- it pushes students toward the subjective-evaluation frontier,
- it makes clear that supervision can redirect effort toward influence activities,
- it sharpens the distinction between measured performance and organizational goals.

### What students should diagnose

The lab should train students to diagnose:
- what behavioral object is being shifted,
- whether the design changes pay, monitoring, evaluation, or relational treatment,
- whether the outcome is productivity, extra work, influence activity, or gaming,
- whether the design identifies treatment, sorting, or both,
- how the same design could transfer to remote work, digital monitoring, or other supervision settings.

### Suggested transfer exercise

Ask students to take the logic of one of the lab papers and sketch how it would apply in one of these environments:
- remote-work monitoring,
- gig/platform work,
- algorithmic management,
- training or probation periods,
- public-sector supervision.

## Must-cite reading spine

The final chapter should visibly rely on:

- `[@dellaVigna2009]`
- `[@dellaVigna2018]`
- `[@kubeMarechalPuppe2012]`
- `[@dellaVignaListMalmendierRao2022]`
- `[@dellaVignaPope2018]`
- `[@bandieraFischerPratYtsma2021]`
- `[@hossainList2012]`
- `[@pierceReesJonesBlank2025]`
- `[@kelley2024monitoring]`
- `[@deJanvrySadouletSuriWang2023]`
- `[@macleod2003subjective]`

## Optional frontier references

If room allows, the week can also briefly point students toward:
- supervisor bonus and subjective-evaluation interactions in team-incentive settings,
- digital or algorithmic monitoring,
- relational versus explicit contracts,
- worker responses to surveillance or visibility technologies.

These should remain frontier pointers rather than the main body of the week.

## Forward bridge to Week 6

End by explaining that Week 5 studied how firms design and govern behavior **inside the employment relationship** through pay, monitoring, and evaluation. Week 6 will widen the lens to identity, norms, fairness, and broader labor-market allocation, where the relevant behavioral forces are no longer only contractual but also social and institutional.
