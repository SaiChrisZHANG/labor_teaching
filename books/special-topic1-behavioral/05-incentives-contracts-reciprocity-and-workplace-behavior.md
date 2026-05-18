# Incentives, Contracts, Reciprocity, and Workplace Behavior

## Learning Objectives

By the end of Week 5, students should be able to:

1. write a benchmark effort problem and identify where behavioral contract objects enter;
2. distinguish incentives, monitoring, supervision, reciprocity, reference dependence, and contract framing as separate workplace channels;
3. explain why monitoring and subjective evaluation can change effort composition, not only effort levels;
4. separate extra work, productivity, gaming, influence activity, sorting, and heterogeneous contract response;
5. map gift-exchange, loss-framing, monitoring, subjective-evaluation, real-effort, and contract-choice designs to the objects they identify;
6. evaluate when stronger incentives improve organizational outcomes and when they redirect behavior toward hidden margins.

## Opening Orientation

Week 5 moves Behavioral Labor inside the firm. The employment relationship is not only a wage and an output target. It is a workplace environment with pay rules, monitoring, supervisors, messages, discretion, gifts, reference points, and evaluation systems. The central economic question is how workers interpret those objects and how firms should design contracts once effort, productivity, reciprocity, and gaming can diverge.

:::{admonition} Core points
:class: important

- Incentive contracts are behavioral objects: workers respond not only to pay levels, but also to framing, reference points, reciprocity, fairness, and monitoring.
- Behavioral workplace responses show up in extra work, productivity, gaming, sorting, compensation heterogeneity, and supervisor-facing behavior.
- Gift exchange and reciprocity can raise effort, but the moved margin need not be measured productivity.
- Monitoring and supervision can complement incentives, crowd out reciprocal motivation, or redirect effort toward gaming and influence activity.
- Subjective evaluation is a distinct channel because workers may optimize toward what supervisors observe and reward, not only toward task output.
- Modern empirical work must distinguish treatment, selection, contract choice, evaluation, monitoring, and organizational responses.

:::

## Bridge

Weeks 2 through 4 built the behavioral primitives. Week 2 showed how nonstandard preferences enter labor supply and effort. Week 3 emphasized beliefs about returns and opportunities. Week 4 showed that workers respond to perceived and learned schedules, not only to rules written on paper. Week 5 asks what happens when firms themselves choose the schedules, messages, monitoring technologies, and evaluation systems.

This week sits at the boundary between behavioral labor and personnel economics. The benchmark personnel problem asks how pay and monitoring induce effort. Behavioral labor keeps that benchmark, but adds that contracts are interpreted by workers. A wage increase can be a price, a gift, a signal of trust, or a new reference point. A bonus can motivate production, target chasing, or gaming. Monitoring can make output visible, but it can also change what workers believe the firm values.

Monitoring and supervision therefore belong in the center of the week. Incentives rarely operate in isolation. Piece rates, bonuses, subjective ratings, digital dashboards, and supervisor discretion define what is visible and what is rewarded. Week 6 will widen the lens from workplace contracts to identity, norms, fairness, and allocation. Week 5 stays inside the employment relationship: pay, effort, reciprocity, monitoring, and evaluation.

## Field Core

### Benchmark Effort And Contract Problem

Start with a worker choosing effort {math}`e` under a compensation schedule {math}`w(y(e))`:

```{math}
:label: eq:benchmark-effort-week5
\max_{e \ge 0} \; u\!\left(w(y(e))\right) - c(e)
```

The benchmark is useful because it fixes the labor margin. Effort raises measured output {math}`y(e)`, compensation maps output into pay, and effort is costly. In the simplest agency interpretation, the firm changes {math}`w(\cdot)` and the worker moves along the effort margin.

That benchmark also hides several assumptions. It treats the contract as understood, the output measure as aligned with productivity, the worker's response as pay-driven, and the evaluation technology as neutral. Behavioral labor opens each assumption. Workers may interpret a wage, gift, bonus, target, monitoring regime, or rating process through reciprocity, reference points, fairness, attention, and beliefs about the firm.

### Incentives Plus Monitoring

Let {math}`m` denote the monitoring regime or information technology faced by the worker. A richer workplace problem is:

```{math}
:label: eq:behavioral-contract-week5
\max_{e \ge 0} \; u\!\left(w(y(e),m)\right) - c(e) + B\!\left(g_i, r_i, f_i, s_i, m_i; e\right)
```

The term {math}`B(\cdot)` collects behavioral channels: perceived generosity {math}`g_i`, reference points {math}`r_i`, framing {math}`f_i`, social or reciprocal motives {math}`s_i`, and monitoring salience {math}`m_i`. The object is deliberately broad, but the empirical discipline must be narrow. A paper should say which behavioral object changes, which workplace margin moves, and whether the result is treatment, sorting, monitoring, or evaluation.

```{include} assets/tables/05-incentives-monitoring-and-supervision-map.md
```

Monitoring is not just a technical input. It changes what workers see, what managers observe, and what counts as performance. It may complement incentives by making productive effort measurable. It may crowd out reciprocity by making a relational contract feel transactional. It may also redirect effort toward visible actions that are weakly related to output.

### Reciprocity And Gift Exchange

Gift exchange is the cleanest entry point because it puts the employment relationship directly on the page. In the classic view, workers may reciprocate employer generosity with higher effort even when formal incentives do not require it. [@kubeMarechalPuppe2012] provides a canonical workplace field experiment on reciprocity and gift exchange. The central behavioral object is perceived generosity; the labor margins are effort, output, and the type of gift or wage gesture.

The modern lesson is more demanding than "gifts work." A gift may increase extra work, but not productivity. It may operate through kindness, surprise, attention, social norms, or temporary morale. [@dellaVignaListMalmendierRao2022] is especially useful because it separates social-preference and gift-exchange responses from standard incentive response and asks whether the outcome is extra work or productivity. That distinction is essential for personnel economics: a firm does not only care whether workers do more; it cares whether the added activity creates value.

The applied question is therefore always four-part. What object changed: wage, gift, employer effort, message, or relational treatment? What margin moved: time, output, quality, attendance, compliance, or productivity? How persistent is the response? And how does the effect interact with monitoring and standard pay incentives?

### Reference Dependence And Loss-Framed Incentives

Reference-dependent contracts make the framing of incentives central. A bonus framed as a gain may differ from a bonus framed as something provisionally owned and at risk of being lost. One compact object is:

```{math}
:label: eq:loss-framing-week5
U(e) = u\!\left(w(y(e))\right) - c(e) + \lambda \min\{0,\, b(e)-r\}
```

Here {math}`r` is the reference point and {math}`b(e)` is the bonus-relevant outcome. When {math}`b(e)<r`, the loss term lowers utility. The design intuition is simple: loss framing can make a target feel more urgent than an equal gain-framed bonus.

[@hossainList2012] is the classic factory-framing anchor because it shows how simple framing manipulations can affect productivity in a real workplace. But the frontier corrective is just as important. [@pierceReesJonesBlank2025] shows why firms must measure broad performance, not only target attainment. Loss framing may raise the behavior attached to the target while inducing gaming, multitasking distortions, lower quality, or other hidden costs.

This is the first major place where the week distinguishes stronger incentives from better organizational outcomes. A stronger psychological frame can increase measured response and still reduce total value if the measured target is incomplete or if monitoring makes gaming easy.

### Monitoring, Supervision, And Subjective Evaluation

Monitoring and supervision should be separated. Objective monitoring records output, time, location, transactions, or task completion. Supervision often adds discretion, judgment, feedback, relational authority, and career consequences. Subjective evaluation is a further object: workers are rewarded partly on an evaluator's assessment.

```{math}
:label: eq:subjective-evaluation-week5
\max_{e,a \ge 0} \; u\!\left(w\big(z(e), \hat q^S(e,a)\big)\right) - c(e) - \psi(a)
```

Here {math}`z(e)` is objective productive output, {math}`\hat q^S(e,a)` is a supervisor's subjective assessment, and {math}`a` denotes influence activity or relationship-building effort directed at the evaluator. The worker may allocate effort between production and supervisor-facing activity. This creates a different labor object from simple pay-for-output.

[@macleod2003subjective] provides the contract-theory anchor for subjective evaluation. [@deJanvrySadouletSuriWang2023] brings the issue into empirical workplace behavior by studying subjective performance evaluation and influence activities. [@kelley2024monitoring] makes monitoring a first-order empirical object and helps students ask when observation changes productivity, compliance, relational treatment, or managerial control.

The frontier is visible here. Does monitoring complement pay by making productive effort measurable, or does it crowd out intrinsic and reciprocal motivation? Does supervision improve output, or does it make workers look busy to the evaluator? Do digital dashboards and algorithmic management reveal productivity, or do they create new gaming margins? Behavioral labor speaks to modern personnel economics because these are contract-design questions, not side remarks.

### Performance Pay, Heterogeneity, And Sorting

Performance pay rarely has one representative effect. Workers differ in responsiveness to monetary incentives, reciprocal motives, loss framing, risk, confidence, and tolerance for monitoring. Firms also sort workers into contracts and workplaces. A contract-choice object makes this explicit:

```{math}
:label: eq:contract-sorting-week5
k_i^\star \in \arg\max_{k \in \mathcal{K}} \; \mathbb{E}\!\left[U_i\!\left(w_k(y_i(e),m), e\right)\right]
```

Workers choose among contract forms {math}`k`, and the observed performance-pay effect can mix treatment and selection. A high average response may reflect strong treatment effects on incumbents, positive selection into performance pay, or both. A weak average response may hide large gains for one group and crowd-out, risk exposure, or sorting for another.

[@dellaVignaPope2018] is the motivation benchmark because it maps how different monetary and nonmonetary motivators affect effort. [@bandieraFischerPratYtsma2021] is the heterogeneity anchor because it builds evidence across experiments on differential response to performance pay. Together they discipline the empirical question: for whom does the contract work, on what margin, and under what monitoring or evaluation regime?

### From Motivating Effort To Distorting Effort

The central caution is that extra work is not the same as productivity. A worker may spend more time, complete more observable tasks, hit more targets, or produce more visible signals while creating little additional value. Contracts can move effort along at least five margins:

- productive effort that raises valuable output;
- extra work that raises activity but not productivity;
- task substitution away from unmeasured quality or maintenance;
- gaming that improves measured performance without improving production;
- influence activity that improves supervisor evaluations rather than output.

The same distinction applies to monitoring versus motivation. Monitoring may reveal effort, but it may not motivate; it may motivate, but toward the wrong metric; or it may change the meaning of the employment relationship. Objective evaluation differs from subjective evaluation because the latter can turn supervisors into targets of worker effort. Stronger incentives differ from better organizational outcomes because measured effort and firm value can diverge. Average effects differ from heterogeneous responses because a contract can help one group, harm another, and change who selects into the job.

```{include} assets/tables/05-workplace-behavior-frontier-map.md
```

### Welfare And Design Implications

Behavioral contract design is not a prescription for more manipulation. It is a framework for asking which workplace environment creates valuable effort at acceptable cost. Gifts may be efficient when reciprocity raises productivity without heavy monitoring. Explicit incentives may dominate when output is cleanly measured and gaming is limited. Loss framing may be powerful when targets are aligned, but costly when workers can distort the metric. Subjective evaluation may capture hard-to-measure quality, but it may also induce influence activity and favoritism.

The welfare question must include workers, firms, and organizational quality. Monitoring can raise productivity and still reduce worker surplus or crowd out trust. Performance pay can raise output and also increase earnings inequality or selection. Algorithmic monitoring can improve feedback and also create surveillance costs, stress, or hidden gaming. Behavioral labor does not replace personnel economics; it makes the contract environment empirically richer.

## Research Lab

The Week 5 lab is organized around **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is [@dellaVignaListMalmendierRao2022]. Students use deterministic synthetic data to reproduce a compact workplace gift-exchange factbook. The teaching path separates extra work from productivity, compares wage and gift treatments, and asks whether a reciprocity interpretation is stronger than a pure price response.

**Diagnose.** Students classify each design by four objects: the behavioral object shifted, the workplace margin observed, the contract or governance element changed, and the identifying claim. A valid diagnosis must say whether the design changes pay, monitoring, evaluation, relational treatment, or framing. It must also say whether the outcome is productivity, extra work, influence activity, or gaming.

**Transfer.** The secondary anchor is [@kelley2024monitoring]. Students adapt the diagnostic logic to monitoring intensity and ask whether observation complements incentives, substitutes for pay, or changes relational motivation. The optional frontier extension is [@deJanvrySadouletSuriWang2023], which pushes students to separate productive output from supervisor-facing effort under subjective evaluation.

The bounded path runs locally without confidential data. It is not an official replication package. It trains the empirical habit: name the behavioral object, name the labor margin, name what varies, and name whether the design identifies treatment, sorting, monitoring, or evaluation.

## Methods Box

:::{admonition} Methods Box: identifying workplace incentive mechanisms
:class: note

**Gift and generosity field experiments** vary unexpected gifts, employer effort, monetary versus nonmonetary gestures, or contract presentation. They identify reciprocity or social-preference responses only after the analyst separates kindness, surprise, salience, and standard pay effects.

**Framing experiments in real workplaces** vary gain versus loss framing, prepaid bonuses, clawbacks, or target presentation. They identify reference-dependent response most cleanly when the outcome includes broad productivity, quality, and gaming measures.

**Randomized monitoring or supervision intensity** changes visibility, feedback, managerial attention, or observation. These designs must distinguish monitoring from motivation and from relational treatment by supervisors.

**Subjective-evaluation designs** use supervisor ratings, evaluation discretion, or performance-assessment changes. They are strongest when they can observe objective output, subjective ratings, and influence activity separately.

**Real-effort experiments with contract variation** vary monetary incentives, goals, feedback, gifts, and nonmonetary motivators. They map effort response, but external validity depends on how closely the task resembles workplace production.

**Contract-choice and sorting designs** observe workers selecting into contracts, piece rates, or performance-pay jobs. They distinguish treatment from selection only when contract assignment, choice sets, or worker types are measured clearly.

**Organizational data on gaming and multitasking** reveal whether contracts move the intended margin or a proxy. They are most informative when the firm observes more than the target used for pay.

:::

```{include} assets/tables/05-identification-and-design-map.md
```

Across all designs, do not present an empirical result without naming the behavioral object, the labor margin, the outcome metric, and whether the design identifies treatment, sorting, monitoring, or evaluation effects.

## Reading Ladder And References

**Core framing.** Start with [@dellaVigna2009] and [@dellaVigna2018] for the broad behavioral-economics taxonomy and structural discipline. Read them here through contracts, effort, monitoring, and workplace design.

**Reciprocity and gift exchange.** Use [@kubeMarechalPuppe2012] for gift exchange in the workplace and [@dellaVignaListMalmendierRao2022] for a richer design that separates social preferences, extra work, and productivity.

**Motivation and heterogeneity.** Read [@dellaVignaPope2018] as the motivation benchmark and [@bandieraFischerPratYtsma2021] for heterogeneous performance-pay response.

**Loss framing and unintended consequences.** Pair [@hossainList2012] with [@pierceReesJonesBlank2025]. The first shows the appeal of loss-framed workplace incentives; the second shows why broad performance and gaming margins matter.

**Monitoring, supervision, and subjective evaluation.** Use [@kelley2024monitoring] for monitoring, [@macleod2003subjective] for subjective evaluation in contracts, and [@deJanvrySadouletSuriWang2023] for influence activities and bureaucratic workplace behavior.

## Exercises And Discussion Prompts

1. In equation {eq}`eq:benchmark-effort-week5`, what assumptions are needed for output {math}`y(e)` to be a good productivity measure?
2. In equation {eq}`eq:behavioral-contract-week5`, choose one object inside {math}`B(\cdot)`. What workplace treatment would shift it without changing standard pay incentives?
3. A gift raises time spent on the task but not output quality. Is that reciprocity, extra work, productivity, or gaming? What additional measure would you want?
4. Compare a gain-framed and loss-framed bonus. What outcome would distinguish productive target response from target gaming?
5. In equation {eq}`eq:subjective-evaluation-week5`, give an example of {math}`a` in a real workplace. How could a design separate {math}`a` from productive effort {math}`e`?
6. In equation {eq}`eq:contract-sorting-week5`, explain why observed performance-pay workers may not reveal the treatment effect for all workers.
7. Design a monitoring experiment for remote work. State the behavioral object, the labor margin, the outcome metric, and the main welfare concern.

## Reproducibility And Code Lab Note

The Week 5 lab lives at `labs/05-incentives-contracts-reciprocity-and-workplace-behavior/`. It creates deterministic synthetic data for a gift-exchange workplace design, a monitoring transfer design, and a subjective-evaluation frontier extension. The smoke path builds the data, runs the reproduction script, and runs the transfer script. It is a bounded teaching lab, not an official replication package for the cited papers.

## Slide Companion Note

The Week 5 slide deck lives at `slides/week5/05-incentives-contracts-reciprocity-and-workplace-behavior.tex`. The deck gives the conceptual map, presents the benchmark and behavioral contract objects, makes monitoring and subjective evaluation explicit, and ends with productivity versus extra work, gaming, algorithmic monitoring, and the bridge to Week 6.

## Bridge Forward

Week 5 studied how firms design and govern behavior inside the employment relationship through pay, monitoring, supervision, evaluation, and relational treatment. Week 6 widens the lens to identity, norms, fairness, and broader labor-market allocation, where behavioral forces are not only contractual but also social and institutional.
