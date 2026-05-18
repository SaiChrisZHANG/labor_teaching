# Attention, Salience, Complexity, and Learning in Labor

## Learning Objectives

By the end of Week 4, students should be able to:

1. locate attention, salience, complexity, and learning inside DellaVigna's nonstandard decision-making branch;
2. write a transparent labor-choice benchmark and then replace the true schedule with a perceived schedule;
3. distinguish low salience, opaque mapping, missing information, endogenous information acquisition, and dynamic learning;
4. map these objects to labor supply, benefit take-up, claiming, workplace effort, retirement saving, and training navigation;
5. compare information letters, simplification designs, quasi-experimental schedule changes, monitored attention designs, workplace incentive experiments, and structural learning models;
6. explain why welfare depends on whether attention frictions are stable, state-dependent, or reduced through learning and design.

## Opening Orientation

Week 3 studied beliefs and expectations in job search. Week 4 widens the lens to labor choices where the relevant rule, incentive, or payoff schedule exists, but workers may not notice it, understand it, or find it worth decoding. The economic question is not whether workers are "biased" in a loose sense. It is whether labor supply, effort, benefit claiming, saving, or training decisions are made against the true environment or against a perceived, simplified, or gradually learned version of it.

:::{admonition} Core points
:class: important

- Attention and salience are labor objects because earnings schedules, benefits, payroll rules, and incentive contracts must be perceived before they can affect behavior.
- Complexity is not the same as low salience: a schedule can be visible but still hard to translate into marginal payoffs.
- Learning is central. Workers repeatedly encounter rules, receive signals, talk to peers, and decide whether to acquire costly information.
- The same worker may look more or less behaviorally distorted depending on experience, exposure, stakes, and information design.
- Empirical designs must name both the labor margin and the behavioral object: hours, earnings, take-up, claiming, effort, saving, training, awareness, understanding, attention, or learning.
- Welfare depends on whether frictions are persistent mistakes, rational responses to costly information, or short-run wedges that policy and firm design can reduce.

:::

## Bridge

DellaVigna's taxonomy separates nonstandard preferences, nonstandard beliefs, and nonstandard decision-making [@dellaVigna2009; @dellaVigna2018]. Week 2 isolated preferences. Week 3 studied beliefs and expectations, especially in job search. Week 4 turns to decision-making when information is available in principle but not necessarily attended to, processed, or updated.

The bridge from Week 3 is tight. Subjective beliefs matter only if workers notice and process relevant information. A job seeker may hold mistaken beliefs about wage offers; a worker facing an earnings disregard, benefit cliff, bonus threshold, or retirement rule may face a related but distinct problem: the schedule itself may be hard to perceive or decode. Attention and learning are therefore not decorations around a standard model. They determine the effective choice environment.

Labor is a natural domain for this week because workers repeatedly face nonlinear incentives, firm pay formulas, program rules, enrollment deadlines, and training procedures. A tax-benefit schedule, an EITC phase-in, a disability benefit earnings rule, a Social Security claiming formula, a retirement-plan default, or a piece-rate contract may be written down. The question is whether the worker knows the local mapping from action to payoff and how that knowledge changes with experience.

## Field Core

### Benchmark Transparent Labor Choice

Start with a worker choosing an action under a known schedule. The action {math}`a` can be hours, earnings, effort, claiming, contribution behavior, or training enrollment:

```{math}
:label: eq:transparent-choice-week4
a_i^\star \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i)
\quad \text{s.t.} \quad c_i = y_i + w_i a - T_i(a).
```

Here {math}`T_i(a)` is the true tax-benefit, payroll, or contract schedule. The benchmark assumes more than standard preferences and beliefs. It assumes the worker knows how the schedule maps actions into consumption, eligibility, take-up, or pay. That transparency assumption is often strong in labor settings. Nonlinear tax rules, earnings disregards, performance-pay formulas, and benefit application procedures can make the local incentive hard to see even when the formal rule is public.

The benchmark is still useful because it fixes the margin. If {math}`a` is annual earnings, the observed outcome is bunching, earnings adjustment, or labor supply. If {math}`a` is a claim, the observed outcome is application or take-up. If {math}`a` is effort, the observed outcome is output or task completion. Behavioral interpretation begins only after the analyst says which true schedule should matter and which observed margin moves.

### Salience And Perceived Incentives

The first departure replaces the actual schedule with the perceived schedule:

```{math}
:label: eq:salience-week4
a_i \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i) \quad \text{s.t.} \quad \tilde{T}_i(a) \neq T(a).
```

The worker reacts to {math}`\tilde{T}_i(a)`, not necessarily to {math}`T(a)`. In a tax-benefit setting, {math}`\tilde{T}_i(a)` may omit an EITC phase-in, use an average rather than marginal tax rate, ignore a benefit cliff, or overweight a highly visible withholding rule. In a workplace setting, {math}`\tilde{T}_i(a)` may be the compensation formula the worker thinks applies, not the formula in the contract.

This wedge can reflect several objects. Low salience means the relevant incentive exists but is not psychologically prominent at the moment of choice. Misperception means the worker holds an incorrect representation of the schedule. Heuristic use means the worker compresses a complicated map into a simpler rule, such as "extra earnings are taxed away" or "the bonus is probably not worth chasing." Incomplete understanding means the worker lacks enough information to construct the local payoff.

The reduced-form signature is often attenuated response. Workers bunch less at kinks than a frictionless model predicts, fail to claim a benefit for which they appear eligible, or provide less effort under a complex bonus. But attenuation alone does not identify attention. It could reflect adjustment costs, liquidity, work constraints, stigma, standard heterogeneity, or rational nonresponse to a low-value margin. A credible interpretation names the observed labor margin and the perceived object.

### Complexity, Opacity, And Information Acquisition

Complexity is not just low salience. A rule can be salient and still hard to decode. The worker may know that a schedule matters while being unable to compute the relevant local slope, threshold, or interaction with other programs. This is common in earnings-tested benefits, tax credits, retirement claiming, employer bonus formulas, and training subsidies with eligibility rules.

The frontier object is dynamic. Workers can learn through repeated exposure, peers, employers, caseworkers, tax preparers, reminders, portals, or personal mistakes. They can also choose whether to pay attention:

```{math}
:label: eq:learning-week4
a_{it}, m_{it} \in \arg\max \tilde{U}_{it}(a;\theta_i,b_{it}) - C(m_{it})
\quad \text{with} \quad
b_{i,t+1}=B(b_{it},m_{it},x_{it+1}).
```

Here {math}`m_{it}` is endogenous information acquisition or attention effort, {math}`b_{it}` is the worker's current representation of the schedule or decision environment, and {math}`x_{it+1}` is new experience, a signal, a peer conversation, a letter, a payroll message, or another information event. This object makes clear why static labels can mislead. A worker may appear inattentive because the environment is new. The same worker may respond strongly after several payroll cycles, after a tax-preparer conversation, or after receiving a targeted explanation.

Policy and firm design enter directly. They can change current choices by making an incentive salient. They can also change the speed of learning by reducing {math}`C(m_{it})`, changing the signal {math}`x_{it+1}`, or redesigning the schedule so {math}`b_{it}` is easier to update. Complexity is sometimes an exogenous administrative fact, but it can also be a design choice.

```{include} assets/tables/04-dynamic-learning-and-information-acquisition-map.md
```

### Distinguishing The Objects

Students should separate five related but distinct objects.

**Low salience** means a relevant feature of the environment is present but not prominent. A reminder or redesigned paycheck may move behavior by putting the same information in front of the worker at the decision moment.

**Complexity or opacity** means the mapping from action to payoff is difficult to decode. Disclosure may not be enough if workers cannot translate a formula into marginal incentives.

**True lack of information** means the worker does not know a fact, rule, eligibility condition, deadline, or option. Information provision can change awareness or beliefs, but the treatment may also change salience and trust.

**Endogenous information acquisition** means the worker chooses how much to learn. Attention is then part of the choice problem, and responses depend on stakes, monitoring, costs, cognitive load, and the expected value of information.

**Dynamic learning** means the perceived environment evolves with experience. A short-run response to a new schedule can differ from a long-run response after repeated exposure and local diffusion.

```{include} assets/tables/04-attention-salience-complexity-map.md
```

### Labor Supply And Benefit Schedules

Labor supply under taxes and benefits is the central application because the statutory schedule can differ sharply from the schedule workers perceive. The EITC is the canonical example: the phase-in, plateau, and phase-out create nonlinear earnings incentives, but many workers may not know the exact local marginal return. The observed labor margins are annual earnings, hours, employment, and bunching around kinks or thresholds.

[@chettyFriedmanSaez2013] use differences in local knowledge about the EITC to study earnings responses. The labor margin is earnings adjustment near EITC incentives; the behavioral object is local knowledge and diffusion about the schedule. Their design is useful for Week 4 because it treats information as embedded in places and networks, not only as an individual cognitive trait. Neighborhoods with more EITC knowledge can generate stronger responses to the same statutory incentives.

[@kostolMyhre2021] make the dynamic point especially concrete. The observed margin is labor supply in response to the tax and benefit schedule. The behavioral object is learning the schedule over time. This matters because attenuated bunching or muted labor-supply response may not mean preferences are inelastic. It may mean workers are still learning the local payoff map. Short-run elasticities can therefore mix true preferences, optimization frictions, knowledge, and exposure.

This literature also clarifies what not to infer. A weak response to a kink does not automatically identify inattention. It may reflect adjustment costs, hours constraints, employer scheduling, income risk, or a rational choice not to optimize over a small local gain. A strong response after information arrives does not automatically identify a pure belief update. The same intervention may make the incentive salient, simplify the schedule, increase trust in the rule, or signal that action is expected.

### Benefit Take-Up, Claiming, And Policy Navigation

Benefit take-up and claiming decisions turn complexity into a labor-market object because many programs are tied to earnings, work status, payroll records, disability status, unemployment spells, family structure, or training eligibility. The observed margins are application starts, completed filings, take-up, claiming dates, recertification, and continued participation.

[@bhargavaManoli2015] is a core anchor because the treatment changes how eligible people encounter an IRS benefit-claiming opportunity. The observed labor-policy margin is take-up of social benefits. The behavioral object is not one thing by default. A simplified notice can change awareness, salience, perceived eligibility, confidence, hassle, stigma, or the cost of action. A reduced-form effect on take-up is valuable, but it does not separately identify all those mechanisms without additional measurement or design variation.

This point generalizes to reminders, letters, web portals, caseworker scripts, and simplified forms. A reminder may operate because a deadline becomes salient. A letter may operate because a worker learns eligibility. A simplified interface may operate because it reduces procedural costs. A trusted messenger may operate because it changes perceived legitimacy. Labor economists need to state which margin is observed and which mechanism is inferred.

Policy navigation also matters for training and reemployment programs. A worker may appear to have low demand for training when the real barrier is interpreting eligibility, deadlines, subsidy rules, or application steps. The behavioral object is then decision-making in a complex institution, not necessarily low returns or weak motivation.

### Workplace Incentives And Effort

Complexity is not only a public-program issue. Firms design compensation systems, bonus thresholds, commissions, penalties, performance metrics, and feedback dashboards. Workers may exert effort against a perceived contract that differs from the actual contract, especially when formulas are nonlinear or cognitively demanding.

The observed margin is effort, output, task allocation, or bonus attainment. The behavioral object is incentive opacity or bounded rationality in decoding the contract. [@abelerHuffmanRaymond2025] is the frontier-facing anchor here because it asks how incentive complexity changes effort provision. The key lesson is not simply that workers dislike complex contracts. It is that incentive effects depend on whether workers understand which action changes pay.

This application also changes the welfare and design conversation. A firm may simplify incentives to help workers respond to productivity-enhancing margins. It may also use opacity strategically if complexity shifts surplus, dampens claims, or hides low expected compensation. Week 5 returns to incentives and contracts inside firms; Week 4 supplies the decision-making channel that makes contract design legibility a labor object.

### Work-Linked Savings, Retirement, And Training

Work-linked saving and retirement decisions combine defaults, disclosure, long horizons, and payroll implementation. [@madrianShea2001] is usually taught as a defaults and inertia paper, but it also belongs in this week because payroll-linked saving requires workers to notice an option, understand the default, and evaluate delayed consequences. [@dufloGaleLiebmanOrszagSaez2006] adds an information and salience dimension by studying saving incentives in a setting where returns can be made more immediate and visible.

Social Security and retirement claiming bring the dynamic dimension to the surface. [@liebmanLuttmer2015] study whether people respond differently when they better understand Social Security. The observed margins include older-worker labor supply and retirement-related behavior; the behavioral object is understanding of a complex dynamic incentive system. The key Week 4 question is whether information changes beliefs, attention to the relevant rule, or the ability to map future claiming and work into lifetime resources.

Training and upskilling decisions fit the same template. Workers may underinvest because returns are low or credit constraints bind. But they may also underinvest because subsidy rules, course requirements, completion deadlines, and returns are hard to learn. A good design states whether it changes information about returns, salience of deadlines, complexity of enrollment, or the cost of acquiring guidance.

### Welfare And Design

Welfare depends on the persistence and source of the wedge. If inattention is stable and workers repeatedly ignore high-value choices, observed decisions may be poor guides to welfare. If inattention is state-dependent, the same worker may make good choices in familiar environments and poor choices after a rule change, job transition, or benefit shock. If learning is fast, short-run mistakes may have smaller long-run welfare costs. If learning is slow or selective, early exposure and information design become first-order policy tools.

Simplification and information provision can have heterogeneous effects. Workers with low prior knowledge, high stakes, limited time, low trust, or weak access to advisors may benefit more from simplification. Workers who already understand the schedule may be unaffected. Some interventions can even backfire if they make a low-value margin salient, create confusion, or increase perceived surveillance.

Firm and policy design choices matter because they shape both incentives and the cost of understanding incentives. A government can make eligibility and earnings rules easier to compute. A firm can make performance pay transparent. A training provider can make completion requirements legible. Conversely, institutions can preserve opacity. The welfare question is therefore not just "are workers biased?" It is: what do workers know, how costly is it to process, how quickly do they learn, who designs the environment, and whose welfare is counted?

## Research Lab

The Week 4 lab uses a bounded synthetic path organized around **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is [@kostolMyhre2021]. Students reproduce a compact factbook on labor-supply responses as workers learn a tax-benefit schedule. The synthetic data track true marginal incentives, perceived incentives, repeated exposure, information treatment, earnings, and hours. The point is to diagnose whether attenuated response reflects static inattention, slow learning, or another labor-supply friction.

**Diagnose.** Students classify four objects: the information or salience object changed, the labor margin observed, whether the design identifies learning or only a reduced-form information response, and which standard alternatives remain. They should explicitly distinguish mistakes about the schedule from optimization frictions, lack of attention, lack of information, and endogenous information acquisition.

**Transfer.** The challenge anchor is [@bhargavaManoli2015]. Students adapt the logic to a policy-navigation design where reminders, information, and simplification affect take-up. The optional extension anchor is [@abelerHuffmanRaymond2025], which pushes the same diagnostic framework into workplace incentive opacity and effort.

Bounded transfer ideas include applying information or salience logic to another worker-policy margin, adapting a complexity design to training enrollment, or building a simple simulation of learning under opaque incentives. The lab is not an official replication package. It is a pedagogical path for turning dynamic attention and information objects into labor research designs.

## Methods Box

:::{admonition} Methods Box: identifying attention, complexity, information, and learning
:class: note

**Information letters and tutorials** communicate facts, rules, eligibility, or returns. They identify the causal effect of exposure on a labor margin, but the treatment may combine missing information, salience, trust, motivation, and reminders.

**Simplification, salience, and disclosure interventions** change how easy a rule is to notice or decode. They are strongest for studying complexity or opacity, but they often change hassle costs and salience at the same time.

**Quasi-experimental schedule or rule changes with learning variation** use changes in actual incentives combined with prior knowledge, exposure, geography, cohorts, or repeated interaction. They can show how learning attenuates or amplifies labor-supply responses, but correlated sophistication and diffusion can remain threats.

**Monitored information-acquisition designs** observe reading, clicks, attention time, or costly requests for information. They speak directly to endogenous attention, but experiment behavior may differ from natural information search.

**Workplace incentive experiments** vary contract complexity, opacity, or compensation formulas while observing effort. They identify effort responses to more or less legible incentives, but interpretation must separate bounded rationality from morale, peer effects, and social preferences.

**Structural models with learning or endogenous information acquisition** jointly model beliefs, attention choice, schedule understanding, and labor behavior. They are useful for welfare and counterfactual policy, but conclusions depend on functional form, learning assumptions, and the normative treatment of mistakes.

:::

```{include} assets/tables/04-identification-and-welfare-map.md
```

The diagnostic discipline is the same across designs. First name the observed labor margin: hours, earnings, effort, take-up, claiming, saving, or training. Then name the manipulated object: information, salience, complexity, disclosure, incentive level, or learning opportunity. Then state what is identified. A treatment effect does not automatically separate mistakes about a schedule, optimization frictions, low attention, missing information, dynamic learning, and endogenous information acquisition.

## Reading Ladder And References

**Core framing.** Start with [@dellaVigna2009] for the broad taxonomy and [@dellaVigna2018] for structural behavioral economics. Read them with Week 4 narrowed to nonstandard decision-making.

**Salience, information, and labor supply.** Use [@chettyFriedmanSaez2013] for local knowledge and EITC earnings responses, then [@kostolMyhre2021] for labor-supply responses to learning the tax and benefit schedule.

**Take-up, claiming, and policy navigation.** Read [@bhargavaManoli2015] for psychological and procedural frictions in social-benefit take-up, and [@liebmanLuttmer2015] for Social Security information and older-worker responses.

**Complexity and effort.** Use [@abelerHuffmanRaymond2025] to connect bounded rationality, incentive complexity, and workplace effort provision.

**Information acquisition and frontier methods.** Read [@bartosBauerChytilovaMatejka2016] for monitored information acquisition and [@haalandRothWohlfart2023] for design principles in information-provision experiments.

**Broader salience anchor.** Use [@chettyLooneyKroft2009] as a public-finance salience benchmark, but keep the Week 4 interpretation tied to labor margins.

## Exercises And Discussion Prompts

1. In equation {eq}`eq:transparent-choice-week4`, choose a labor action {math}`a`. What must the worker know for the transparent benchmark to be plausible?
2. In equation {eq}`eq:salience-week4`, give one EITC example, one workplace-incentive example, and one benefit-claiming example where {math}`\tilde{T}_i(a) \neq T(a)`.
3. A reform changes labor supply only after two years of exposure. State one learning interpretation, one standard adjustment-cost interpretation, and one selection interpretation.
4. A simplified claiming letter increases take-up. Which mechanisms are consistent with the result: awareness, salience, hassle-cost reduction, trust, or perceived eligibility?
5. Design a workplace incentive experiment that separates incentive level from incentive opacity. What effort margin would you observe?
6. Explain why welfare conclusions differ when inattention is stable, when it is reduced by learning, and when attention is chosen endogenously.

## Reproducibility And Code Lab Note

The Week 4 lab lives at `labs/04-attention-salience-complexity-and-learning/`. It creates deterministic synthetic data for a Kostol-Myhre-style labor-supply learning design, a Bhargava-Manoli-style policy-navigation transfer design, and a small workplace incentive-opacity extension. The smoke path builds the data, runs the reproduction script, and runs the transfer script. It is a bounded teaching lab, not an official replication package.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-attention-salience-complexity-and-learning.tex`. The deck is a conceptual and empirical map rather than a duplicate of the chapter. It bridges from Week 3, highlights the nonstandard decision-making branch of the taxonomy, presents the benchmark and perceived-schedule objects, maps salience versus complexity versus information versus learning, and ends with identification, welfare, and the bridge to Week 5.

## Bridge Forward

Week 4 has shown how perceived schedules, complexity, and learning shape labor supply, claiming, effort, saving, and training. Week 5 moves inside the firm more fully: incentives, contracts, reciprocity, and workplace behavior when employers design the environment in which workers respond.
