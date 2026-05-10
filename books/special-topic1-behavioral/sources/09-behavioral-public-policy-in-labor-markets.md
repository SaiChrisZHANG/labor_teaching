# Week 9 source pack — Behavioral public policy in labor markets

## Week identity
- Course: Special Topic 1 — Behavioral Labor
- Week: 9
- Working title: **Behavioral public policy in labor markets**
- Position in course: policy-design week after the equilibrium-response week
- Role in sequence: synthesizes Weeks 2–8 by asking what behavioral frictions and firm or market responses imply for the design, implementation, and welfare analysis of labor-market policy

## Topic boundary
This week should remain labor-focused. The main policy domains should be:
- tax credits and labor-supply incentives,
- benefit claiming and take-up,
- unemployment insurance and job-search support,
- training and post-displacement investment,
- retirement and work-linked saving,
- disability / claiming / work-incentive environments where useful.

It should **not** become:
- a generic public economics lecture,
- a general “nudges” lecture detached from labor,
- or a bucket of unrelated policies.

The organizing focus is not the list of policies themselves, but the **roles behavioral frictions play in labor-policy design**.

## Central question
How do behavioral frictions alter the design, implementation, targeting, equilibrium effects, and welfare analysis of labor-market policies?

## Why this week matters
By Week 9, students have seen that behavioral labor is not just about documenting deviations from the standard model. Week 8 made firm and market response explicit. The practical question is what those deviations and responses imply for policy. In labor settings, behavioral frictions change not only whether workers respond to incentives, but also whether they learn about policies, understand schedules, complete applications, comply with requirements, trust the system, or even know they are eligible.

This means behavioral labor policy must go beyond the standard price-versus-quantity logic. It has to ask:
1. when a friction is a bias to be corrected,
2. when a friction can be used as a policy lever,
3. when implementation itself is the key margin,
4. how learning and endogenous information acquisition shape dynamic policy effects,
5. how firms, intermediaries, and local information environments reshape incidence,
6. how welfare should be evaluated when observed choices may not reveal welfare-relevant preferences.

## Core teaching goal
By the end of the week, students should be able to:
- classify the main roles behavioral frictions play in labor-policy design;
- explain why the same friction may matter for incentives, implementation, learning, and welfare at once;
- connect labor-policy environments to specific empirical designs and econometric tools;
- distinguish policies that **correct**, **harness**, or **interact with** behavioral frictions;
- see where the frontier lies: dynamic learning, digital implementation, intermediary responses, and welfare under normative ambiguity.

## Required chapter architecture
Keep the established special-topics structure:
1. short opening orientation / why this week matters
2. **Core points** box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references

Do not add an Extension box by default.

## Bridge
The Bridge should do three things:
1. connect Weeks 2–4 to this week by explaining that nonstandard preferences, beliefs, attention, salience, complexity, and learning all have direct policy-design implications;
2. connect Weeks 5–6 to this week by showing that workplace behavior, identity, norms, and fairness also matter for how workers experience and respond to policy;
3. connect Week 7 to this week by emphasizing that the right labor-policy design depends on what empirical object we think is distorted and what method we use to study it.

## Organizing framework
This chapter should be organized around a taxonomy of the roles of behavioral frictions in labor policy.

### Role 1. Frictions as wedges or mistakes to be corrected
Behavioral frictions may cause workers to misunderstand schedules, underclaim benefits, delay enrollment, under-save, or fail to invest in training. In this view, the policy task is corrective: improve understanding, reduce complexity, or lower frictions that prevent welfare-improving action.

### Role 2. Frictions as levers that policy can harness
Behavioral tools such as defaults, reminders, active choice, simplification, framing, and commitment can be used to move outcomes in welfare-improving directions. This is not just “less friction”; it is policy design that uses predictable decision patterns.

### Role 3. Frictions as implementation and take-up constraints
A policy may be generous on paper but weak in practice because workers do not know about it, do not trust it, fail to apply, or face administrative burden. In labor policy, implementation is often an economic margin, not merely a bureaucratic detail.

### Role 4. Frictions as dynamic learning problems
Policy effects can be delayed, persistent, or heterogeneous because workers learn schedules and claiming rules over time, gather information from peers, or selectively acquire information only when stakes become large enough.

### Role 5. Frictions as equilibrium and intermediary modifiers
Behavioral policy is not only about workers. Employers, tax preparers, counselors, caseworkers, and local information environments may amplify or dampen policy effects. This can change incidence, pass-through, and who actually benefits.

### Role 6. Frictions as welfare and targeting complications
When choices are behaviorally distorted, welfare analysis becomes harder. Who is “mistaken”? Which preferences are welfare-relevant? Should policy target groups with the largest mistakes, the lowest information, or the greatest gains from correction?

## Field Core

### 1. Standard labor policy versus behavioral labor policy
Start from the contrast between a standard model and a behavioral-policy environment.

A compact policy-design object is:
```{math}
:label: eq:policy-env-week9
p = (\tau, n, s, d),
```
where:
- {math}`\tau`` denotes prices, tax/subsidy rates, or other financial incentives,
- {math}`n`` denotes information architecture or salience design,
- {math}`s`` denotes simplification / administrative burden / claiming support,
- {math}`d`` denotes defaults, commitment devices, or active-choice architecture.

In a standard model, policy mostly works through {math}`\tau``. In a behavioral model, the other components become first-order.

### 2. Worker choice under behavioral policy
Then introduce a generic choice problem:
```{math}
:label: eq:behavioral-choice-week9
a_i(p) \in \arg\max_{a \in \mathcal{A}} \tilde U_i(a; p, b_i) - K_i(a; p),
```
where:
- {math}`b_i`` summarizes the worker’s beliefs, attention, sophistication, or other behavioral state,
- {math}`K_i(a;p)`` captures procedural or cognitive costs induced or reduced by policy.

The chapter should explain that a labor policy may change:
- the objective incentive,
- the perceived incentive,
- the cost of understanding or claiming,
- and the pace of learning.

### 3. Take-up and implementation as labor-policy margins
Make take-up explicit:
```{math}
:label: eq:takeup-week9
D_i(p) = \mathbf{1}\!\left\{\tilde V_i(p; b_i) - C_i(p) \ge 0\right\}.
```
This section should stress that low participation in a labor policy may come from:
- low awareness,
- misunderstanding of eligibility,
- complexity of claiming,
- distrust or stigma,
- or the interaction of these with work constraints.

Students should leave knowing that labor policy often fails or succeeds at the implementation margin.

### 4. Dynamic learning and endogenous information acquisition
This is one of the frontier parts of the lecture. Policy effects need not be static:
```{math}
:label: eq:learning-week9
b_{i,t+1} = B\!\left(b_{it},\, m_{it},\, x_{i,t+1},\, p_t\right),
```
where:
- {math}`m_{it}` is information acquisition,
- {math}`x_{i,t+1}` is experience or outside information,
- {math}`p_t` is the policy environment itself.

The text should explain that:
- policy can create learning,
- local information environments matter,
- measured elasticities may understate long-run effects if people learn slowly,
- behavioral design and dynamic labor responses cannot be separated cleanly.

### 5. Policy-effect decomposition
Require a compact decomposition discussion such as:
```{math}
:label: eq:policy-decomp-week9
\frac{d a_i}{d p}
=
\frac{\partial a_i}{\partial \tau}\frac{d\tau}{dp}
+
\frac{\partial a_i}{\partial n}\frac{dn}{dp}
+
\frac{\partial a_i}{\partial s}\frac{ds}{dp}
+
\frac{\partial a_i}{\partial d}\frac{dd}{dp}.
```
This is not meant to be literal in every application; it is a teaching device to emphasize that policy works through multiple channels.

### 6. Welfare and normative ambiguity
Make welfare explicit:
```{math}
:label: eq:welfare-week9
W(p) = \int \Psi_i\!\left(a_i(p), a_i^\star(p), p\right)\, dF(i),
```
where {math}`a_i^\star(p)`` is a benchmark or welfare-relevant action.

This section should explain:
- why revealed preference is not enough when choices are distorted,
- why defaults and nudges raise normative ambiguity,
- why targeted simplification may improve welfare differently from stronger monetary incentives,
- and why heterogeneity in mistakes matters for both equity and efficiency.

## Applied policy blocks

### 1. Biases as targets of correction
Use tax credits, Social Security / retirement rules, disability claiming, and benefit take-up as main examples. The key point is that policy may underperform not because incentives are too weak, but because workers do not understand or perceive them.

### 2. Biases as policy levers
Use defaults, reminders, active choice, simplification, and commitment devices as examples. This should not read as “nudges are always good”; instead it should show when such tools substitute for or complement price incentives.

### 3. Implementation and administrative burden
This section should emphasize that the economics of implementation is central:
- claiming is behavior,
- applications are labor-market actions,
- forms, notices, timing, and interfaces shape response,
- and policy design often lives in the administrative details.

### 4. Dynamic learning and persistence
Use local knowledge, repeated exposure, and delayed learning to explain why policy responses may grow over time, differ across neighborhoods, or depend on peer environments.

### 5. Firms, intermediaries, and market response
This section should make clear that behavioral labor policy does not end with the worker:
- employers may change menus, counseling, defaults, or plan contributions,
- tax preparers or counselors may mediate information,
- local knowledge spillovers may alter incidence,
- and labor-market equilibrium can amplify or mute the policy effect.

### 6. Welfare, targeting, and research gaps
This section should organize frontier questions:
- when should policy correct versus harness a bias?
- how should policies target people with high mistakes versus high gains?
- how do digital systems change attention, complexity, and implementation?
- how should equilibrium response be built into behavioral labor policy analysis?
- when are labor policies complements to information provision, simplification, or defaults?

## Methods and identification
Students should leave this week with a practical map from policy problem to empirical design.

Explicitly distinguish:
1. randomized information / reminder / mailing experiments;
2. simplification and application redesign experiments;
3. local-knowledge or peer-information designs;
4. dynamic event-study / panel designs for learning;
5. designs around defaults, active choice, and commitment;
6. welfare analysis using sufficient statistics, calibrated models, or structural frameworks;
7. equilibrium or intermediary-response settings where reduced-form worker response is not enough.

The methods discussion should be concrete:
- information experiments -> randomized field experiments, ANCOVA, heterogeneity by baseline knowledge
- dynamic learning -> panel/event-study / distributed-lag style analysis
- take-up / claiming -> extensive-margin models, hazard/timing, treatment of application completion
- defaults and commitment -> treatment comparisons, passive-choice margins, calibrated welfare
- welfare / targeting -> sufficient-statistics or structural approaches under normative ambiguity

## Research Lab

### Primary anchor
- `[@bhargavaManoli2015]`

This is the cleanest primary anchor because it makes implementation, take-up, salience, and psychological frictions central while remaining directly relevant to labor-oriented transfer ideas.

### Secondary / challenge anchor
- `[@chettyFriedmanSaez2013]`

Use this to teach students that labor-policy response depends on knowledge and local information environments, not only on the schedule itself.

### Optional extension anchor
- `[@bernheimFradkinPopov2015]` or `[@kostolMyhre2021]`

Use the defaults paper if you want the welfare-design/defaults branch. Use the learning paper if you want the dynamic-learning branch.

### Lab logic
The lab should train students to answer:
1. what friction is the policy targeting?
2. is the intervention correcting a mistake or harnessing a behavioral regularity?
3. is the main outcome a response to incentives or a take-up / implementation response?
4. what welfare benchmark is being used?
5. where might equilibrium or intermediary responses matter?
6. how could the design be transferred to a related labor policy environment?

## Reading strategy
The reading ladder should be structured, not chronological.

### Framing
- DellaVigna-style behavioral taxonomy as background
- pragmatic behavioral public policy
- behavioral public economics / welfare background

### Core labor-policy readings
- EITC knowledge and local labor-supply response
- psychological frictions and take-up
- learning tax-benefit schedules
- defaults and retirement-saving design
- Social Security information and claiming
- UI-recipient information / training response

### Frontier / methods / welfare
- information provision design
- welfare of nudges versus taxes
- equilibrium, targeting, and dynamic-learning gaps

## Distinctive contribution of this week
The distinctive contribution of the week is not “behavioral policies exist.” It is that the chapter gives students a **systematic framework** for thinking about behavioral labor policy:

- **correcting** mistakes,
- **harnessing** biases,
- dealing with **implementation** frictions,
- understanding **dynamic learning**,
- studying **equilibrium and intermediary** responses,
- and handling **welfare / targeting** under normative ambiguity.

That should make Week 9 a genuine frontier lecture rather than a list of case studies.
