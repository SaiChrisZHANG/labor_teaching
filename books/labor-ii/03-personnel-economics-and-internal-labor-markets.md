---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Personnel Economics and Internal Labor Markets

## Learning objectives

By the end of Week 3, students should be able to:

1. define personnel economics as labor economics inside firms and explain why it follows Weeks 1--2 in Labor II;
2. distinguish incentives that affect effort from practices that affect selection, sorting, assignment, promotion, and retention;
3. write down compact agency, multitasking, promotion, and peer-spillover objects and interpret the economic margin each one isolates;
4. explain why promotions are both assignment decisions and incentive devices, including the Peter Principle tradeoff;
5. distinguish manager effects, peer effects, team complementarities, and broader management-practice objects;
6. evaluate personnel-economics evidence by naming the identifying variation, unit of observation, observed outcome margin, and external-validity caveat;
7. connect internal labor markets to current frontier questions on managers, remote work, worker voice, digital traces, AI, training, and within-firm inequality.

The Week 3 economic question is direct: once the firm has chosen how much labor to employ and how quickly to adjust, how should it organize, motivate, evaluate, assign, promote, and retain workers inside the firm?

## Bridge

Weeks 1 and 2 asked how much labor the firm wants and why actual employment moves toward that target gradually. Week 3 asks how the firm runs the workforce it already has. Personnel economics is therefore not a detour into generic management. It is the labor-economics study of practices inside firms: compensation, monitoring, evaluation, career ladders, team design, managers, and workplace rules [@hoffmanStanton2024; @lazear2000].

That positioning matters for the course sequence. Week 3 remains a firm-side, largely partial-equilibrium week. It is still about organizational choices inside the firm rather than about market-wide search equilibrium, bargaining, or monopsony. Those come next. Week 4 will take quits, vacancies, internal hiring, and retention motives and move outward to turnover, unemployment flows, and matching across firms.

A useful Week 3 production object is

```{math}
:label: eq-lii-w3-organization
Y = F\big(K, L, e(\omega), m, T\big),
```

where {math}`e(\omega)` is worker effort under workplace practice {math}`\omega`, {math}`m` is managerial or supervisory input, and {math}`T` is team or organizational structure. Equation {eq}`eq-lii-w3-organization` makes the central Week 3 claim explicit: firms change output not only by changing headcount, but also by changing organization.

```{figure} assets/figures/03-personnel-economics-in-course-map.png
:name: fig-lii-w3-course-map
Personnel economics sits between labor-demand choice and market-wide worker flows. The chapter studies how firms organize labor inside the firm before Labor II turns outward to search, turnover, and wage-setting.
```

```{include} assets/tables/03-personnel-economics-map.md
```

Figure {numref}`fig-lii-w3-course-map` and Table {numref}`tbl:personnel-map-week3` together give the conceptual map students need at the start of the week. Personnel economics studies how internal practices shape productivity and worker outcomes, while the rest of Labor II studies how those internal choices interact with outside options, market frictions, and institutions.

## Field Core

### Incentives, compensation, and the agency benchmark

The canonical starting point is the agency problem. Firms care about output or firm value, but effort is costly to workers and imperfectly observed. A compact Week 3 effort object is

```{math}
:label: eq-lii-w3-effort
e_i = e\big(w_i, b_i(y_i), p_i, \text{monitoring}_i\big),
```

where {math}`w_i` is fixed pay, {math}`b_i(y_i)` is performance-contingent compensation, and {math}`p_i` captures career incentives such as promotion chances. Equation {eq}`eq-lii-w3-effort` is useful because it keeps three personnel margins distinct: pay contracts, future-job incentives, and monitoring.

The classic risk-incentive tradeoff says that stronger pay-for-performance sharpens effort incentives but loads more risk onto workers. That logic explains why piece rates can work well in settings with clean output measures and limited noise, and why they can fail in jobs where output is noisy, team-produced, or easy to game [@lazear2000; @holmstromMilgrom1991]. It also explains why firms often mix base pay, bonus pay, promotion rules, and supervision rather than choosing one instrument in isolation.

Personnel economics quickly moved beyond the narrow question "what is the optimal contract?" because firms also choose who enters the job and who stays. The same incentive system can affect both effort and selection. High-powered incentives may raise effort among incumbents, but they can also attract workers who are more confident in performance-based environments and repel workers who prefer insurance or teamwork. This is the first major Week 3 distinction: incentives can change behavior on the job, but they can also reshape the composition of who sorts into the job in the first place [@hoffmanStanton2024].

`@friebelHeinzKruegerZubanov2017` is a good anchor because the variation comes from a firm-side experiment that changes team incentives directly. The observed units are teams or stores, and the main observed margins are performance and profits. The design is especially useful for effort effects inside one organization, but it is less informative about long-run sorting or whether the same contract would work in a different firm or occupation.

### Multitasking, subjective evaluation, and career incentives

The agency benchmark becomes incomplete when measured performance is only a partial proxy for value. A compact multitasking object is

```{math}
:label: eq-lii-w3-multitask
q_i = \theta_1 a_{i1} + \theta_2 a_{i2} + \varepsilon_i,
```

where measured performance {math}`q_i` loads on some tasks more cleanly than others. Equation {eq}`eq-lii-w3-multitask` is the Week 3 warning against naive output-based pay. If incentives attach strongly to {math}`q_i`, workers may over-supply the measured activity and under-supply the unmeasured one. This is the core logic of multitasking [@holmstromMilgrom1991].

That logic is why subjective evaluation is not merely a soft or informal alternative to incentives. In many jobs, supervisors observe dimensions of value that the formal dashboard does not. Subjective evaluation can therefore repair incomplete measurement, but it introduces its own problems: favoritism, relational contracting, opacity, and uneven treatment across workers. Students should see this as an information-design problem rather than a simple contrast between "hard" and "soft" incentives.

Career incentives belong in the same section because future jobs often substitute for current-job bonus pay. Tournaments and promotion ladders encourage effort today by tying current performance to future advancement [@lazearRosen1981]. But that means the firm is using a future assignment decision to motivate current behavior, which immediately creates tension between current-job incentives and future-job fit.

```{figure} assets/figures/03-incentives-assignment-promotion.png
:name: fig-lii-w3-incentives-promotion
Personnel systems connect current-job incentives to future-job assignment. Narrow performance measures can improve effort on measured tasks while distorting multitasking and promotion choices.
```

Figure {numref}`fig-lii-w3-incentives-promotion` is the bridge from agency to internal labor markets. The main lesson is not that incentives fail. It is that incentives work through multiple channels, some productive and some distortive, and the firm has to coordinate them.

### Promotions, assignment, and internal labor markets

Internal labor markets are the rules, ladders, and screening processes through which firms allocate workers across jobs over time. Promotions are central because they do two things at once. They assign workers to new roles and they motivate workers in current roles.

A compact promotion object is

```{math}
:label: eq-lii-w3-promotion
\Pr(\text{promote}_i=1) = g\big(y_i, z_i, \widehat{m}_i\big),
```

where {math}`y_i` is current measured performance, {math}`z_i` captures collaboration or other soft-skill proxies, and {math}`\widehat{m}_i` is expected productivity in the next role. Equation {eq}`eq-lii-w3-promotion` disciplines the promotion discussion. If the firm promotes only on {math}`y_i`, it may maximize incentives in the current job while making weak assignments into future jobs. If it promotes only on {math}`\widehat{m}_i`, it may weaken tournament incentives for current performance.

This is exactly where the Peter Principle enters. `@bensonLiShue2019` uses personnel records to study a setting where strong current sales performance predicts promotion, while post-promotion managerial performance need not rise in lockstep. The identifying variation comes from promotion decisions in administrative personnel data. The unit is the worker-job transition. The observed outcomes are promotion probabilities and performance in the next role. The external-validity caveat is that internal promotion rules and managerial tasks differ sharply across firms and occupations.

The Week 3 distinction students should retain is precise.

1. Promotions as incentives ask whether the chance of advancement changes effort in the current job.
2. Promotions as assignments ask whether the worker promoted is the worker best matched to the next job.

Those are not the same question. In many organizations they push in different directions. That is why internal labor markets are not just a wage policy or a morale policy. They are an allocation mechanism inside the firm.

### Managers, peers, teams, and organizational spillovers

Managers are themselves a labor input and an organizational technology. They coach, monitor, transmit information, allocate work, and shape retention. Peers matter too, but through different mechanisms: observation, pressure, learning, coordination, and task complementarities. A compact spillover object is

```{math}
:label: eq-lii-w3-peers
y_i = a_i e_i + \rho \bar e_{-i} + u_i,
```

where {math}`\rho` captures spillovers from coworkers. Equation {eq}`eq-lii-w3-peers` is deliberately reduced form. A positive spillover can reflect knowledge transfer, peer pressure, or better coordination, and those interpretations imply different policies.

`@masMoretti2009` is a clean peer-effects anchor because the variation comes from coworker exposure within a workplace setting, the unit is the worker-shift or worker-day, and the observed outcome margin is worker productivity. The main caveat is interpretation: a measured peer effect does not by itself tell us whether the mechanism is pressure, learning, or composition.

Managers are a different object. Manager effects ask how much worker outcomes change when supervisory assignment changes, holding worker composition as fixed as possible. That is not the same as peer effects, and it is not the same as the broader management-practice literature. `@bloomEtAl2019` is especially useful here because it separates the measurement of management practices from the harder question of causal management shocks. Surveys linked to outcomes tell us that management differs substantially across firms, but causal claims require cleaner variation than cross-sectional management scores alone.

Team incentives complicate the picture again. They can internalize complementarities when production is joint, but they also invite free-riding when individual effort is difficult to verify. `@friebelHeinzKruegerZubanov2017` is therefore not just an incentives paper. It is also a teams paper because it asks whether shared incentives improve performance when tasks are interdependent.

```{figure} assets/figures/03-managers-peers-teams.png
:name: fig-lii-w3-managers-peers
Managers, peers, and teams create distinct spillover channels. Personnel economics must separate supervision, coworker exposure, and broader organizational design rather than treating them as one composite firm effect.
```

Figure {numref}`fig-lii-w3-managers-peers` is useful as a taxonomy. Manager effects are about supervisory assignment and coaching. Peer effects are about coworker exposure. Team design is about complementarities, coordination, and free-riding. Management practices sit one level higher and bundle several of those channels at once.

### Data and empirical designs: what modern personnel economists observe

Modern personnel economics is best organized by data and design rather than by a long chronology of topics.

```{figure} assets/figures/03-data-design-frontier-map.png
:name: fig-lii-w3-data-design
Week 3 evidence combines firm experiments, internal policy variation, administrative personnel records, surveys, digital traces, and public-policy shocks. Each design isolates a different internal labor margin and has its own external-validity limits.
```

```{include} assets/tables/03-design-map.md
```

Firm field experiments vary incentives, targets, scheduling rules, or team structures inside one organization. The unit is often the worker, team, store, or shift. The observed margins are effort, output, attendance, or profits. These designs are strongest for clean internal treatment effects and weakest for cross-firm external validity [@friebelHeinzKruegerZubanov2017].

Internal policy changes and phased rollouts vary evaluation rules, workflow tools, promotion criteria, or flexibility policies over time. The unit is usually the worker, team, or business unit. The observed margins are productivity, retention, promotions, or job quality. These are quasi-experiments, not experiments, so the central threat is endogenous adoption: the firm may introduce the policy because conditions were already changing.

Promotions and manager switches in personnel records vary assignment within the firm. The unit is the worker transition or manager-worker match. The observed margins are promotion probabilities, post-promotion performance, subordinate productivity, quits, or career progression. These designs are especially good for separating current performance from next-job fit, but selective promotion and reassignment remain central threats [@bensonLiShue2019].

Management surveys linked to firm outcomes vary measured practices across firms. The unit is typically the firm or plant. The observed margins are productivity, growth, wages, and survival. This evidence is valuable because it broadens the field beyond one-firm case studies, but measurement error and policy endogeneity make practice measurement different from a causal management shock [@bloomEtAl2019].

Digital traces, time-use data, and communication records vary at high frequency within work processes. The unit may be a message, meeting, task, project, or worker-day. The observed margins are time allocation, collaboration, responsiveness, and workflow sequencing. These data are rich enough to study coordination and monitoring directly, but they are often proprietary, setting-specific, and easy to over-interpret if the missing margins of value are large [@hoffmanStanton2024].

Public policies that change workplace practices vary outside the firm but affect what happens inside it. The unit may be the worker, establishment, or firm. The observed margins include wage dispersion, communication, retention, productivity, and promotion patterns. `@harjuJagerSchoefer2025` is useful because it moves the field from internal policy variation to public policy that changes worker voice, while still keeping the personnel-economics object inside the workplace.

Remote-work and technology settings require especially careful separation of selection and treatment. The variation may come from eligibility rules, office re-openings, or staggered tool deployment. The unit is often the worker or team. The observed margins are productivity, promotions, quits, or collaboration. The core identification lesson from `@emanuelHarrington2024` is that a remote-work premium or penalty is hard to interpret unless we separate who selects into remote jobs from what remote work does to a comparable worker once assigned.

The cross-cutting research habit is simple: never present a personnel result without naming the variation, the unit of observation, the outcome margin, and the main external-validity caveat. Table {numref}`tbl:personnel-map-week3` is helpful here because it keeps the theoretical object and the observable margin in the same frame.

### Bridge to Week 4

Week 3 stays inside the firm, but it should already make Week 4 feel inevitable. Promotions affect who quits. Team design changes who searches externally. Manager quality changes retention. Remote-work rules change who stays attached to the firm and who leaves. Week 4 therefore takes the internal labor market objects from this chapter and asks how they map into turnover, vacancies, unemployment flows, and matching across firms.

## Research Lab

The frontier of personnel economics is not just more credible estimates of classic incentive effects. It is a broader effort to understand how modern firms allocate attention, authority, information, and opportunity across workers. The area is especially active because linked personnel data, digital traces, and workplace policy variation now make internal organization observable in ways that were much harder a generation ago [@hoffmanStanton2024].

```{figure} assets/figures/03-research-opportunities-landscape.png
:name: fig-lii-w3-frontier
Recent personnel-economics frontiers combine classic internal-labor-market questions with new data on management, communication, remote work, monitoring, training, and AI-enabled workflow design.
```

```{include} assets/tables/03-frontier-opportunities-map.md
```

### Managers below the C-suite

One major frontier is identifying good managers before the promotion decision is made. Administrative personnel data can track how subordinates perform, quit, learn, or advance under different supervisors, but the hard problem is portability. Does a manager who excels in one workflow, product line, or labor market excel elsewhere too? Promising variation comes from manager reassignments, promotion thresholds, coaching programs, and 360-review systems. The open question is whether manager quality is a stable trait, a match-specific object, or a bundle of task-specific skills [@hoffmanStanton2024].

### Remote and hybrid work as a personnel-economics problem

Remote work is not merely a location choice. It changes monitoring, collaboration, promotion visibility, retention, and sorting. `@emanuelHarrington2024` is a strong anchor because it forces the selection-versus-treatment distinction into the design. Promising data include eligibility rules, staged return-to-office policies, project-assignment records, and communication traces. The unanswered questions concern career effects, manager adaptation, and whether remote-work policies compress or widen within-firm inequality.

### Voice, communication, and internal governance

Worker voice is a natural personnel-economics topic because it changes how information flows upward and how discretion is constrained inside the firm. `@harjuJagerSchoefer2025` provides a bridge from public policy to internal governance. The relevant quasi-experimental openings include representation thresholds, disclosure rules, communication reforms, and workplace complaint systems. The open question is when voice mainly improves information and productivity, and when it mainly redistributes rents or changes bargaining power without improving organization.

### Training, digital traces, algorithmic management, and AI

Training is still undermeasured relative to its importance. Many firms invest heavily in onboarding, coaching, certification, and task redesign, yet administrative evidence often captures output and quits better than learning. A promising empirical path combines training-platform data, manager assignment, and follow-on job transitions to see who learns, who gets new opportunities, and who captures the returns.

Digital traces and algorithmic management broaden the same agenda. Scheduling systems, call logs, meeting data, code reviews, and workflow dashboards make it possible to study attention, monitoring, sequencing, and collaboration directly. The opportunity is to measure organizational processes that earlier personnel work could only infer. The risk is that rich traces tempt researchers to ignore missing margins of value, discretion, and job quality. AI enters here as a new organizational technology: it can complement supervisors, automate monitoring, reshape tasks, and change who becomes promotable. The main research need is design discipline, not simply more granular data [@hoffmanStanton2024].

### External validity and scaling

Personnel economics is unusually vulnerable to external-validity mistakes because many famous results come from one firm, one occupation, or one policy environment. Market conditions, worker composition, managerial capability, and technology stacks can all change treatment effects. This is why multi-firm linked data, replications across settings, and explicit comparison of labor-market environments are such important frontier contributions. A personnel practice that raises output in one dense labor market may fail where hiring pools, outside options, or monitoring technologies differ sharply [@bloomEtAl2019; @hoffmanStanton2024].

The big research payoff of Week 3 is therefore not a single canonical estimate. It is a design agenda: use better internal data, separate treatment from selection, separate incentives from assignment, and ask which practices generalize across firms rather than only whether they work in one carefully studied case.

## Methods Box

Week 3 requires more identification discipline than students often expect from an "inside the firm" topic.

1. Firm-side experiments versus quasi-experiments: experiments randomize incentives or teams inside the firm; quasi-experiments rely on policy timing, thresholds, or phased rollouts and therefore need stronger assumptions about adoption.
2. Incentives affecting effort versus incentives affecting selection and sorting: a short-run bonus treatment is usually closest to an effort object, while compensation systems that change who applies, stays, or exits also move composition.
3. Promotions as assignment versus promotions as incentives: Equation {eq}`eq-lii-w3-promotion` is about next-job match quality, while tournament logic is about effort in the current job.
4. Manager effects versus peer effects: manager effects require variation in supervisory assignment; peer effects require variation in coworker exposure; the mechanisms and policies are different even when both show up as spillovers.
5. Management-practice measurement versus causal management shocks: management surveys document cross-firm heterogeneity, but causal management effects require cleaner intervention or reassignment variation than cross-sectional scores alone.
6. Remote-work or technology settings where selection and treatment must be separated: workers who choose remote jobs are not automatically comparable to workers assigned to office jobs, so eligibility and assignment rules matter as much as observed productivity.
7. Internal policy variation versus public policy that changes workplace practices: an internal evaluation reform and a public worker-voice mandate can both affect promotions or retention, but the latter often bundles institutional channels beyond the firm.
8. External-validity reporting: every empirical result in personnel economics should state the identifying variation, unit of analysis, observed outcome margin, and main reason transportability may fail.

## Reading ladder

### Bridge

- `@hoffmanStanton2024` for a modern map of personnel economics as labor economics inside firms.
- `@lazear2000` for the field-defining case that incentives, pay, and productivity are central labor-economics objects.

### Field Core

- `@holmstromMilgrom1991` for multitasking and the limits of narrow performance measurement.
- `@lazearRosen1981` for tournaments and career incentives.
- `@friebelHeinzKruegerZubanov2017` for a clean firm experiment on team incentives, output, and profits.
- `@bensonLiShue2019` for promotions as assignment rather than merely reward.
- `@masMoretti2009` for peer spillovers and social production environments.
- `@bloomEtAl2019` for management-practice heterogeneity and the measurement-versus-causality distinction.

### Research Lab

- `@emanuelHarrington2024` for remote work with explicit selection-versus-treatment discipline.
- `@harjuJagerSchoefer2025` for worker voice and internal governance as a personnel-economics object.

## Exercises / discussion prompts

1. Use Equations {eq}`eq-lii-w3-effort` and {eq}`eq-lii-w3-multitask` to explain why high-powered incentives can raise measured performance while lowering firm value.
2. Why is a promotion tournament potentially useful even if the firm knows that current job performance is an imperfect predictor of managerial quality?
3. In `@bensonLiShue2019`, what is the identifying variation, what is the unit of observation, and which observed margin most clearly speaks to the Peter Principle?
4. How would you distinguish manager effects from peer effects in a matched personnel panel where both supervisors and coworkers change over time?
5. Why is `@emanuelHarrington2024` a remote-work paper for Week 3 rather than only a labor-supply or amenity paper?
6. Pick one row from Table {numref}`tbl:frontier-opportunities-week3` and propose a credible quasi-experimental design, naming the treatment, unit, outcome margin, and main external-validity concern.

## Reproducibility or code lab note

The Week 3 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure. The bounded reproduction path uses a local synthetic team-level dataset inspired by `@friebelHeinzKruegerZubanov2017` so students can estimate a compact team-incentive effect without confidential data. The diagnose step forces them to separate effort effects from selection or sorting claims. The transfer step uses a synthetic promotion dataset tied to `@bensonLiShue2019` so students can study assignment-versus-incentive tradeoffs, while `@emanuelHarrington2024` serves as the optional extension on selection versus treatment in remote-work settings. The local handout lives at [labs/03-personnel-economics-and-internal-labor-markets/lab.md](labs/03-personnel-economics-and-internal-labor-markets/lab.md).

## Slide companion note

The slide deck at [slides/week3/03-personnel-economics-and-internal-labor-markets.tex](slides/week3/03-personnel-economics-and-internal-labor-markets.tex) should stay tighter than the chapter: course positioning, the Week 2 to Week 3 bridge, the personnel-economics map, agency and compensation, multitasking and subjective evaluation, promotions and assignment, managers and peers, data and external validity, frontier extensions, and the bridge to Week 4 search and turnover.
