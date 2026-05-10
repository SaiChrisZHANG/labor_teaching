# Week 4 source pack — Attention, salience, complexity, and learning in labor

## Week identity
- Course: Special Topic 1 — Behavioral Labor
- Week: 4
- Working title: **Attention, salience, complexity, and learning in labor**
- Position in course: first week focused on nonstandard decision-making after nonstandard preferences (Week 2) and beliefs / expectations / job search (Week 3)
- Role in sequence: isolates the **attention / salience / complexity** branch of DellaVigna’s taxonomy and makes clear that these wedges are dynamic because workers learn and acquire information endogenously

## Topic boundary
This week should stay labor-focused and should not become a generic public-finance salience lecture or a generic psychology lecture. The main applications should be:
- labor supply under tax-benefit schedules and nonlinear incentives,
- benefit take-up and claiming,
- workplace effort under opaque incentive schemes,
- work-linked saving / retirement / claiming decisions,
- training / upskilling / policy navigation when information is complex.

Week 3 already handled behavioral job search directly. This week may briefly refer back to search, but the main organizing focus should be attention, salience, complexity, learning, and endogenous information acquisition across the broader labor domain.

## Central question
How do attention, salience, complexity, learning, and endogenous information acquisition shape labor supply, effort, saving, claiming, and policy take-up, and how do labor economists distinguish these mechanisms empirically?

## Why this week matters
This is one of the frontier weeks of the course because the most interesting work no longer treats attention or salience as a static one-shot mistake. In labor markets, people repeatedly encounter schedules, contracts, benefit rules, and information environments. They learn from experience, from neighbors, from employers, and from policy communication. They also choose how much information to acquire. That means the observed wedge between actual incentives and perceived incentives can itself evolve endogenously over time.

This week should therefore show students that “inattention” is too crude a label unless we know:
1. what information workers actually perceive,
2. whether the mapping from actions to payoffs is opaque,
3. whether workers can and do learn,
4. whether firms or policymakers make information more legible,
5. how those dynamics affect welfare and policy design.

## Core teaching goal
By the end of the week, students should be able to:
- distinguish salience, complexity, lack of information, and endogenous information acquisition;
- explain why learning matters for the interpretation of behavioral wedges in labor;
- map these mechanisms into labor supply, benefit take-up, claiming, effort, saving, and training;
- understand the main empirical designs used to identify these mechanisms;
- see why this literature is increasingly about dynamic learning and design, not just static mistakes.

## Required chapter architecture
Keep the established series structure:
1. opening orientation / why this week matters
2. **Core points** box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references

Do not add an Extension box by default.

## Bridge
The Bridge should do three things:
1. connect Week 3 to Week 4 by explaining that subjective beliefs and expectations only matter if people notice, process, and update relevant information;
2. connect DellaVigna’s taxonomy to this week by positioning attention / salience / complexity as the main nonstandard decision-making channel;
3. explain why labor is a natural domain because workers repeatedly face complex schedules, incentive formulas, claiming rules, and disclosure regimes.

## Field Core

### 1. Benchmark transparent labor choice
Start from a benchmark in which the worker knows the relevant mapping from actions to payoffs.

A clean generic object is:
```{math}
:label: eq:transparent-choice-week4
a_i^\star \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i) \quad \text{s.t.} \quad c_i = y_i + w_i a - T_i(a),
```
where {math}`T_i(a)` is the true tax-benefit or contract schedule.

Use the text to explain that the benchmark assumes not only standard preferences and beliefs, but also a transparent decision environment.

### 2. Salience and perceived incentives
Then introduce a salience wedge in which the worker reacts to a perceived rather than actual schedule:
```{math}
:label: eq:salience-choice-week4
a_i^{S} \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i) \quad \text{s.t.} \quad c_i = y_i + w_i a - \tilde{T}_i(a),
```
with {math}`\tilde{T}_i(a) \neq T_i(a)`.

The chapter should explain that this wedge can reflect:
- low salience of marginal incentives,
- misperception of nonlinear schedules,
- reliance on heuristics such as average rather than marginal incentives,
- incomplete understanding of the policy environment.

### 3. Complexity and opacity
Make clear that complexity is not the same thing as low salience. Complexity means the decision environment is hard to decode even if information is nominally available. Workers may understand some coarse features but not the relevant local slope or incentive mapping.

A useful discussion question is:
- when does complexity simply attenuate response,
- when does it change which incentive the worker thinks matters,
- when do firms or policymakers intentionally or unintentionally create opacity?

Use workplace incentive contracts, claiming rules, and payroll-linked saving as the main illustrations.

### 4. Learning and endogenous information acquisition
This is the key frontier part that should be explicit, not buried. Include a dynamic object such as:
```{math}
:label: eq:learning-choice-week4
a_{it}, m_{it} \in \arg\max \tilde{U}_{it}(a;\theta_i,b_{it}) - C(m_{it})
\quad \text{with} \quad
b_{i,t+1}=B(b_{it},m_{it},x_{it+1}),
```
where:
- {math}`m_{it}` is costly information acquisition / attention effort,
- {math}`b_{it}` is the worker’s current representation of the relevant schedule or environment,
- {math}`x_{it+1}` is new experience, signals, or policy communication.

The text should explain that:
- a worker may look inattentive today because the environment is new,
- that same worker may learn tomorrow,
- observed attenuation can therefore reflect both static frictions and dynamic updating,
- policy design changes both current choices and the speed of learning.

### 5. Distinguish the objects carefully
The chapter should explicitly distinguish:
- low salience,
- complexity / opacity,
- missing information,
- endogenous information acquisition,
- slow or selective learning.

Students should come away understanding that these are related but empirically distinct objects.

### 6. Labor-supply applications
The first main application block should be labor supply under nonlinear tax-benefit schedules and work incentives.

Core papers here should be:
- knowledge diffusion and local EITC responses,
- direct information interventions about schedules,
- misperception of claiming and benefit rules.

Require the chapter to explain:
- why responses to kinks/notches are attenuated,
- how much attenuation may reflect information rather than preferences,
- how local knowledge or information diffusion changes observed elasticities.

### 7. Take-up, claiming, and policy navigation
The second application block should be worker-policy interaction:
- benefit take-up,
- claiming behavior,
- reminders/simplification,
- filing or enrollment frictions.

This should make clear that “complexity” often appears in the data as incomplete take-up or delayed claiming, but the interpretation depends on whether the intervention changes:
- awareness,
- salience,
- procedural hassle,
- perceived eligibility,
- confidence or trust.

### 8. Workplace incentives and effort
The third application block should be workplace incentives.
Use this to show that complexity is not just a public-policy issue. Worker effort changes when pay schemes are difficult to decode, when some margins of compensation are opaque, or when incentive formulas are cognitively demanding.

This section should be connected to:
- effort provision,
- contract design,
- bounded rationality,
- opacity in performance pay.

### 9. Work-linked savings / retirement / training
A shorter section should cover work-linked saving, retirement, and training:
- defaults and information design in retirement saving,
- learning Social Security incentives,
- training or upskilling decisions when returns or procedures are difficult to parse.

This section should not dominate the week, but it should show that the same decision-making frictions matter outside immediate hours or effort choices.

### 10. Welfare and design
The welfare block should emphasize:
- welfare depends on whether people can learn,
- simplification may matter more for some groups than others,
- dynamic learning can reduce long-run distortions even if short-run wedges are large,
- firms and policymakers may redesign choice architecture strategically.

A good final point is that the relevant policy question is often not “are people biased?” but:
- what information do they have,
- how costly is it to process,
- how quickly do they learn,
- and how should institutions design around those facts?

## Methods and identification
This week should have a strong methods section. Students should leave knowing how the literature separates different mechanisms.

Explicitly distinguish:
1. randomized information letters / tutorials / disclosure;
2. simplification interventions and procedural redesign;
3. quasi-experimental schedule changes combined with variation in prior knowledge or learning opportunities;
4. workplace incentive experiments with varying opacity;
5. designs that directly monitor information acquisition;
6. structural models with learning or endogenous information choice.

The methods section should also explain common diagnostic questions:
- what is observed: hours, earnings, effort, take-up, claiming, saving, training?
- what is manipulated: information, salience, complexity, disclosure, incentives?
- what mechanism is identified: awareness, understanding, attention, learning, or effort to acquire information?
- what is left unidentified without stronger structure?

## Research Lab

### Primary anchor
- `[@kostolMyhre2021]`

This should be the main anchor because it directly links labor-supply responses to learning the schedule, making the dynamic point of the week concrete.

### Secondary / challenge anchor
- `[@bhargavaManoli2015]`

Use this to teach students that take-up frictions are not automatically one thing. They need to diagnose whether the intervention changed knowledge, hassle, salience, or some other procedural/psychological margin.

### Optional extension anchor
- `[@abelerHuffmanRaymond2025]`

Use this to push students from public-policy complexity into workplace incentive opacity and effort. If you want one additional frontier illustration in the text or reading ladder, use `[@bartosBauerChytilovaMatejka2016]` for endogenous costly attention.

### Lab logic
The lab should follow:
- Reproduce
- Diagnose
- Transfer

The lab handout should teach students to ask:
1. what information environment is the agent facing?
2. what part of that environment is opaque or low-salience?
3. does the design identify static inattention or dynamic learning?
4. what labor margin is observed?
5. what would a plausible transfer design look like in another labor setting?

A good bounded transfer exercise is to move the same logic to:
- another claiming or take-up margin,
- a payroll-linked saving environment,
- a training enrollment decision,
- or a simpler simulated incentive contract.

## Figures to aim for
The chapter should ideally have at least four figures:
1. salience vs complexity vs information vs learning taxonomy;
2. labor-supply responses under transparent vs perceived schedules;
3. methods / identification map;
4. welfare and design implications with learning.

Keep figure paths stable if they are generated.

## Tables to use
Use:
- `assets/tables/04-attention-salience-complexity-map.md`
- `assets/tables/04-dynamic-learning-and-information-acquisition-map.md`
- `assets/tables/04-identification-and-welfare-map.md`

## Reading ladder expectations

### Core framing
- `[@dellaVigna2009]`
- `[@dellaVigna2018]`

### Salience / information / labor supply
- `[@chettyFriedmanSaez2013]`
- `[@kostolMyhre2021]`

### Take-up / claiming / policy navigation
- `[@bhargavaManoli2015]`
- `[@liebmanLuttmer2015]`

### Complexity and effort
- `[@abelerHuffmanRaymond2025]`

### Information acquisition / frontier methods
- `[@bartosBauerChytilovaMatejka2016]`
- `[@haalandRothWohlfart2023]`

### Optional broader salience anchor
- `[@chettyLooneyKroft2009]`

## Guardrails
- Do not let the chapter collapse into generic tax salience.
- Do not treat all attenuation as attention.
- Do not ignore learning dynamics.
- Do not make the week job-search-only.
- Keep the labor margins explicit throughout.
