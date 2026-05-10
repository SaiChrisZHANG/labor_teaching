# Week 1 Source Pack — What Is Behavioral Labor?

## Week identity

- Course: Behavioral Labor
- Week: 1
- Canonical chapter path: `books/special-topic1-behavioral/01-what-is-behavioral-labor.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week1/01-what-is-behavioral-labor.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/01-what-is-behavioral-labor/`

## Central question

What makes labor markets a natural domain for behavioral economics, and how should Behavioral Labor be organized so that students can move from benchmark worker/firm models to empirical design, welfare analysis, and frontier research?

## Why this week matters

This lecture should do more than define a field. It should give students a disciplined map for the course. The key message is that labor markets are unusually fertile ground for behavioral economics because labor-market decisions are repeated, high-stakes, dynamic, social, policy-sensitive, and often made under incomplete information and limited attention.

The week should make clear that Behavioral Labor is **not** a bag of isolated biases. It is a way of re-reading labor economics through a structured set of wedges: preferences, beliefs, decision-making/attention, and firm/market/policy responses.

## Position in the sequence

- This course builds directly on Labor I Week 12, but it is broader and more systematic.
- Labor I gave students worker-side foundations and one introductory behavioral bridge.
- Labor II added firms, frictions, institutions, and shocks.
- Behavioral Labor reorganizes both books around behavioral wedges, empirical design, and welfare.

## Core takeaways to build around

By the end of the chapter, students should understand:

1. the benchmark labor model against which behavioral deviations are defined;
2. DellaVigna’s taxonomy and how to translate it into labor-economic language;
3. why labor markets are especially behaviorally rich relative to many other applied fields;
4. how behavioral frictions appear in labor supply, job search, training, contracts, household decisions, and policy take-up;
5. the difference between reduced-form evidence, structural behavioral modeling, welfare claims, and equilibrium responses;
6. how this week foreshadows the rest of the Behavioral Labor course.

## Required chapter architecture

Use the standard structure:

- opening orientation / why this week matters
- Core points box near the top
- Bridge
- Field Core
- Research Lab
- reading ladder
- bridge forward to Week 2

Do not require an Extension / Optional Extension box by default. If genuine frontier or optional material belongs in this week, surface it clearly inside Field Core or Research Lab unless a separate box is specifically warranted.

## Bridge section

The Bridge should do four things:

1. remind students of the benchmark neoclassical labor model from Labor I;
2. show how Behavioral Labor differs from both standard labor and generic behavioral economics;
3. explain why repeated labor-market decisions make misoptimization and learning central;
4. motivate why firms, coworkers, households, and policy designers respond to worker-side behavior.

## Field Core requirements

### 1. Benchmark object

Include a simple benchmark labor-choice or search-choice object. Keep it clean and pedagogical.

A good benchmark is:

```{math}
:label: eq:behavioral-labor-benchmark
a_i^\star \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i) \quad \text{s.t.} \quad c_i = g(a, p, y_i),
```

where {math}`a` is the action (hours, effort, search intensity, training, application choice, take-up, etc.), {math}`\theta_i` are standard preference parameters, and {math}`g(\cdot)` maps actions into payoffs.

The chapter should then explain that Behavioral Labor asks how this benchmark changes when preferences are nonstandard, beliefs are distorted, attention/choice sets are limited, or responses by firms/markets/policy change the environment.

### 2. Behavioral wedge representation

Include a compact formal representation of the behavioral extension. It does not need to be “the model of the course”; it needs to clarify the taxonomy.

A suitable object is something like:

```{math}
:label: eq:behavioral-wedge
a_i^{B} \in \arg\max_{a \in \mathcal{A}_i(\lambda_i)} \tilde{U}_i(a;\theta_i,\beta_i,r_i,\eta_i)
\quad \text{s.t.} \quad \tilde{g}_i(a \mid b_i, \lambda_i),
```

with the text clarifying:
- {math}`\beta_i, r_i, \eta_i` can summarize nonstandard preferences/reference dependence/social preferences,
- {math}`b_i` summarizes nonstandard beliefs/expectations,
- {math}`\lambda_i` captures attention, salience, or complexity constraints,
- firms, coworkers, and policy may respond to {math}`a_i^{B}`.

The point is not to overformalize; the point is to give students a disciplined way to classify behavioral labor papers.

### 3. DellaVigna taxonomy mapped to labor

Use DellaVigna’s structure as the main organizing device:

- nonstandard preferences,
- nonstandard beliefs,
- nonstandard decision-making / attention / complexity,
- market and policy responses.

Make explicit that this course is labor-specific because the objects are:
- labor supply,
- job search,
- training and human capital,
- workplace effort and incentives,
- household labor allocation,
- policy take-up and worker protection.

### 4. Labor domains where the taxonomy matters

The Field Core should have a subsection that makes clear **where** the wedges matter in labor:

- labor supply and intertemporal effort;
- job search and reservation behavior;
- training, upskilling, and application decisions;
- workplace contracts, reciprocity, and effort;
- households, identity, and relative income;
- policy design, salience, and take-up.

This section should connect the taxonomy to specific labor margins students already know from Labor I and Labor II.

### 5. Methods and identification

This week should not just classify wedges. It should also classify how we learn about them.

Require a structured methods block that distinguishes:

- field experiments and framed field experiments,
- information interventions,
- salience / simplification designs,
- administrative nudges,
- observational designs using measured preferences/beliefs,
- structural behavioral estimation.

Be explicit that different designs identify different objects:
- treatment effects,
- beliefs,
- present bias / dynamic inconsistency,
- social preferences,
- identity costs,
- welfare-relevant internalities.

### 6. Welfare and equilibrium

The week should end the Field Core with a disciplined warning: behavioral evidence is not automatically enough for welfare claims.

Require a short formal or semi-formal welfare discussion around:
- decision utility vs experienced/normative utility,
- internalities,
- heterogeneity in sophistication,
- firm and policy responses,
- equilibrium masking or amplifying behavioral wedges.

A simple normative object is enough. For example, define the gap between the observed choice {math}`a_i^{B}` and a benchmark or welfare-relevant choice {math}`a_i^\dagger`, then discuss why measuring that gap is difficult.

## Research Lab design

The Research Lab should feel stronger than a generic literature summary.

### Primary anchor

- [@royerStehrSydnor2015]

Use it as the main week-1 empirical anchor because it is labor-facing, behaviorally motivated, experimentally grounded, and replicable.

### Secondary / challenge anchor

- [@altmannFalkJaegerZimmermann2018]

Use it to represent beliefs, information, and motivational frictions in job search.

### Optional frontier anchor

- [@bertrandKamenicaPan2015]

Use it to represent identity and social norms in labor-market allocation inside households.

### Lab logic

The lab should follow:

- Reproduce
- Diagnose
- Transfer

The lab handout should teach students:
1. how to classify the behavioral mechanism being studied,
2. how to identify the margin affected,
3. what the design can and cannot identify,
4. how to transfer the logic to another labor setting.

A good transfer exercise is to ask students to take the mechanism/design logic from the anchor paper and apply it to another labor margin:
- training take-up,
- application behavior,
- benefit take-up,
- effort/attendance,
- household labor allocation.

## Figures to generate or use

Aim for four figures.

1. **Behavioral Labor taxonomy to labor domains**
   - preferences / beliefs / decision-making / responses on one side
   - supply / search / contracts / households / policy on the other

2. **Benchmark vs behavioral wedge schematic**
   - benchmark worker problem
   - where the wedges enter

3. **Methods and identification map**
   - design type -> identified object -> labor margin

4. **Welfare and equilibrium caution figure**
   - behavioral effect
   - firm/policy response
   - observed outcome
   - welfare interpretation

Keep the figures cleaner than earlier rough conceptual figures:
- no in-figure full-sentence title unless unavoidable,
- consistent fonts,
- no arrow/label collisions,
- restrained palette.

## Tables to use

Use the following tables:

- `assets/tables/01-taxonomy-map.md`
- `assets/tables/01-labor-domains-map.md`
- `assets/tables/01-methods-and-welfare-map.md`

## Reading ladder expectations

The reading ladder should clearly separate:

### Core framing
- [@dellaVigna2009]
- [@dellaVigna2018]

### Welfare / policy framing
- [@chetty2015]

### Labor-facing anchor papers
- [@dellaVignaPaserman2005]
- [@royerStehrSydnor2015]
- [@altmannFalkJaegerZimmermann2018]
- [@bertrandKamenicaPan2015]

### Optional theoretical / identity anchor
- [@akerlofKranton2000]

## Guardrails

- Do **not** let the lecture become an undisciplined list of biases.
- Do **not** drift into generic behavioral economics with only token labor applications.
- Do **not** overclaim welfare implications.
- Do **not** spend too much time on one application area at the expense of the field map.
- Keep this week as a clean introduction that organizes the next nine weeks.

## Forward bridge

End with a short bridge to Week 2:

- Week 1 builds the map.
- Week 2 moves into nonstandard preferences in labor supply, effort, savings, and training.
- Students should leave Week 1 already knowing how to classify later papers.
