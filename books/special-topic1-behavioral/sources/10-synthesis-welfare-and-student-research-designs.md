# Week 10 Source Pack — Synthesis, Welfare, and Student Research Designs

## Week identity

- Course: Behavioral Labor
- Week: 10
- Canonical chapter path: `books/special-topic1-behavioral/10-synthesis-welfare-and-student-research-designs.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week10/10-synthesis-welfare-and-student-research-designs.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/10-synthesis-welfare-and-student-research-designs/`

## Central question

How do we translate the concepts, methods, and empirical findings of Behavioral Labor into welfare-relevant, frontier-quality research projects of our own?

## Why this week matters

The course has already covered the main behavioral objects that labor economists study: nonstandard preferences, beliefs and expectations, attention and complexity, workplace incentives, identity and norms, behavioral policy design, and firm/market response. By Week 10, the key pedagogical problem is no longer exposure. It is **synthesis**.

Students can easily leave an advanced special-topics course with a long list of papers and a vague sense of what the field is about. That is not enough. This final week should instead leave students with a working research framework: how to move from a labor-market puzzle to a behavioral mechanism, then to a setting, a design, an estimand, a welfare interpretation, and finally a contribution that genuinely adds something to the literature.

This week should therefore do three things at once:

1. synthesize the field into a coherent map;
2. clarify the welfare and interpretation issues that make behavioral labor distinct;
3. turn the course into a project-generation workshop.

The guiding idea is that a strong behavioral-labor paper is rarely “just” a labor paper with a behavioral label. It typically combines:
- a concrete labor-market margin,
- a specific behavioral wedge,
- a design that isolates that wedge,
- and a clear interpretation of welfare or policy relevance.

## Position in the sequence

- Weeks 1–4 built the taxonomy: preferences, beliefs, attention, learning.
- Weeks 5–6 moved into workplace and social environments: incentives, reciprocity, identity, norms, and culture.
- Weeks 7–9 expanded to empirical tools, equilibrium responses, and policy design.
- Week 10 now closes the loop by asking how one turns the whole architecture into a research agenda.

## Core teaching goal

By the end of the week, students should be able to:

- articulate what counts as a behavioral-labor contribution;
- distinguish a behavioral mechanism from a reduced-form treatment effect;
- identify when a project requires a welfare benchmark beyond revealed preference;
- map labor settings to appropriate empirical and econometric tools;
- diagnose the most common failure modes in project design;
- and formulate their own behavioral-labor research idea in a clear, disciplined format.

## Required chapter architecture

Use the standard special-topics structure:

- opening orientation / why this week matters
- **Core points** box
- Bridge
- Field Core
- Research Lab
- reading ladder / references
- forward bridge to dissertation-quality work and adjacent special topics

Do not add an Extension box by default.

## Bridge

The Bridge should do four things:

1. remind students that the course is not ending with a mere recap; it is ending with a framework for doing research;
2. explain how earlier weeks supply inputs to project design:
   - preferences,
   - beliefs,
   - attention/learning,
   - workplace incentives,
   - norms/culture,
   - policy design,
   - firm and market responses;
3. make clear that welfare and interpretation are central rather than optional in behavioral labor;
4. foreshadow that the final output of the week is not just understanding but a draftable research design.

## Core points box: essentials to surface

- Behavioral labor projects combine a **labor-market margin**, a **behavioral wedge**, an **institutional environment**, and a **credible design**.
- Good empirical work in this field requires more than finding treatment effects; it requires clarity about what behavioral object is being identified.
- Welfare is not automatic in behavioral labor: many settings require a benchmark beyond observed choice.
- The frontier often lies in better measurement, tighter design, richer administrative or platform data, and clearer equilibrium interpretation.
- A strong student project can often be built by adapting an existing behavioral-labor design to a new margin, market, institution, or data source.

## Field Core: conceptual arc

### A. What counts as a behavioral-labor contribution?

Start by telling students that not every labor paper with an information intervention or survey module is a behavioral-labor paper. The field is most compelling when it isolates a wedge between the standard model and observed behavior and shows why that wedge matters for labor-market outcomes.

A compact organizing equation should appear early:

```{math}
:label: eq:research-map-week10-source
Y = g(B, I, M, P, X; \theta)
```

The text should explain:
- `{math}`B`` = behavioral wedge (present bias, biased beliefs, inattention, fairness, identity, etc.)
- `{math}`I`` = institutional environment (tax schedule, benefits, contract form, workplace practice, platform design)
- `{math}`M`` = firm or market response
- `{math}`P`` = policy or program design
- `{math}`Y`` = observed labor outcome

This is the week’s master map. It shows why behavioral labor is never just “psychology added to labor.” The same wedge can look very different depending on the institution and the equilibrium environment.

Use `[@dellaVigna2009]`, `[@chetty2015]`, and `[@bernheimTaubinsky2018]` to frame the field.

### B. Welfare and interpretation in behavioral labor

This should be one of the main intellectual blocks of the lecture.

Students need to see that behavioral labor raises a special interpretation problem: observed choice may not fully reveal welfare. A worker can choose a dominated savings path, misperceive outside options in search, or fail to claim a benefit because of administrative burden, limited attention, or mistaken beliefs. Once that happens, reduced-form responses do not translate mechanically into welfare.

A compact welfare object should appear:

```{math}
:label: eq:welfare-week10-source
W = \int \Psi_i\big(a_i, a_i^\star, M, P\big)\, dF(i)
```

The text should explain that the hard part is not writing down `{math}`W``. The hard part is deciding what `{math}`a_i^\star`` is supposed to mean:
- a fully informed benchmark?
- a long-run learned action?
- a commitment-consistent action?
- a welfare-relevant objective recovered from choice under certain conditions?

This is where `[@bernheimTaubinsky2018]`, `[@chetty2015]`, and `[@allcott2025]` become especially useful. Students should see that welfare analysis is not an afterthought; it shapes what counts as a good behavioral-labor paper.

### C. From topic to wedge to design

This section should be very practical. The goal is to move from intellectual interest to research architecture.

A good project typically starts with one of the following:
- a puzzling labor-market pattern;
- a policy response that seems too small, too delayed, or too heterogeneous;
- a workplace design that generates distortions or underperformance;
- a search or matching pattern that standard frictions alone do not explain.

Then the project should move through a decomposition like:

```{math}
:label: eq:project-week10-source
Contribution = Question + Mechanism + Data + Design + Interpretation
```

The text should emphasize that good proposals are often weak at one of these stages:
- interesting question, weak mechanism;
- plausible mechanism, poor data;
- nice data, but no identifying variation;
- design identifies something, but interpretation is vague;
- treatment effect exists, but welfare meaning is unclear.

Use concrete course examples to show the mapping:
- labor supply / commitment -> `[@kaurKremerMullainathan2015]`
- beliefs and search -> `[@muellerSpinnewijnTopa2021]`
- workplace preferences -> `[@dellaVignaListMalmendierRao2022]`
- take-up / implementation -> `[@bhargavaManoli2015]`
- defaults and retirement saving -> `[@bernheimFradkinPopov2015]`

### D. Mapping empirical settings to econometric methods

This section should directly answer the issue you raised earlier in the course: students often understand the empirical setting but not the practical econometric methods.

A compact estimand equation should appear:

```{math}
:label: eq:estimand-week10-source
\tau = \mathbb{E}[Y_i(1)-Y_i(0) \mid S_i=1]
```

Then explain why the field often needs more than `{math}`\tau``:
- sometimes the goal is a treatment effect,
- sometimes a behavioral parameter,
- sometimes a welfare-relevant wedge,
- sometimes an equilibrium-adjusted object.

This section should directly connect settings to methods, for example:
- repeated beliefs panel -> FE, forecast-error decomposition, validation exercises;
- unemployment duration / search -> hazard models and dynamic exit analysis;
- nonlinear schedules / knowledge frictions -> bunching and local elasticity methods;
- workplace experiments -> OLS / ANCOVA, heterogeneity, treatment interaction design;
- take-up and implementation -> randomized encouragement, hazard-style claiming analysis, administrative-data treatment evaluation;
- preference or dynamic-learning recovery -> structural MLE / SMM / calibrated models.

Use `[@haalandRothWohlfart2023]` as a methods-oriented bridge to information design and interpretation.

### E. When reduced-form is enough and when structure is needed

Students should be pushed to think carefully here.

Some behavioral labor papers are powerful because a reduced-form design is enough to establish that a specific friction matters in a policy or workplace setting. But other questions demand more:
- present bias parameters,
- reference-point dynamics,
- learning and information acquisition,
- equilibrium persistence of wedges,
- welfare under distorted choice.

The chapter should therefore explain the logic of moving from reduced-form to structure without turning this into a structural-econometrics lecture.

A compact structural objective can appear:

```{math}
:label: eq:structural-week10-source
\hat \psi \in \arg\min_{\psi \in \Psi}
\left[m^{data}-m^{model}(\psi)\right]'W\left[m^{data}-m^{model}(\psi)\right]
```

The emphasis should be practical: what kind of question forces you toward this move, and what do you gain or lose when you make it?

### F. Frontier project opportunities

This section should be more ambitious than a list of “future work” bullets. It should make the frontier feel real and accessible.

Good frontier themes to surface:
- dynamic learning of policy schedules and claiming rules;
- belief formation and misperception in job search under rapidly changing labor markets;
- algorithmic interfaces, recommendation systems, and behavioral job search;
- subjective evaluation, monitoring, and behavioral contracting inside firms;
- firm-side exploitation/accommodation/insurance of worker biases;
- behavioral heterogeneity and targeting in labor-market policy;
- welfare analysis when behavior changes over time through learning or institutional adaptation;
- linked survey–administrative–platform data for measuring behavioral objects at scale.

The point is not just to say these are interesting. It is to show why they are still open:
- measurement challenges,
- interpretation challenges,
- equilibrium complications,
- external-validity problems,
- and insufficient welfare evidence.

### G. Common failure modes in project design

This section should be short but sharp. Students benefit from hearing what *not* to do.

Common failure modes:
- the project measures a behavior but not the behavioral wedge;
- the project identifies a wedge but the labor-market margin is too weak or unimportant;
- the design estimates a reduced form but treats it as if it were a parameter;
- the project ignores learning dynamics;
- the project ignores firm or market response;
- the project makes a welfare claim without a normative framework;
- the project is interesting but not distinctly behavioral or not distinctly labor.

### H. Research memo template / project studio

The chapter should end by becoming a project workshop.

Students should be told to structure a project memo around:
1. puzzle or fact,
2. behavioral mechanism,
3. labor-market setting,
4. outcome and unit of observation,
5. identifying variation,
6. econometric method,
7. welfare or policy interpretation,
8. contribution relative to the frontier.

This should feel like the natural culmination of the course.

## Methods bridge: what students should leave knowing

This week must be especially concrete on methods. The key pedagogical aim is to close the gap between setting and estimator.

The chapter or table should summarize things like:

- **Labor-supply commitment / menu settings** -> field experiments, reduced-form treatment contrasts, structural parameter recovery.
- **Repeated subjective expectations in job search** -> panel FE, hazard models, forecast-error decomposition.
- **Nonlinear schedules and knowledge frictions** -> bunching, local elasticity, dynamic learning/event-study approaches.
- **Workplace incentives / reciprocity / evaluation** -> field experiments, treatment heterogeneity, contract-design inference.
- **Take-up / claiming / administrative burden** -> randomized encouragement, hazard-style take-up analysis, administrative-data treatment designs.
- **Welfare / targeting / long-run policy design** -> sufficient-statistics, calibrated welfare, structural approaches.

The point is not technical completeness. It is to make the field feel empirically actionable.

## Research Lab requirements

This week should function as a proposal studio more than a standard single-paper lab.

Keep the Reproduce -> Diagnose -> Transfer logic, but reinterpret it:

- **Reproduce**: reverse-engineer the logic of one or two anchor papers and identify the wedge, margin, design, and welfare claim.
- **Diagnose**: explain what the paper identifies, what it does *not* identify, and what assumptions support interpretation.
- **Transfer**: build a short original project memo using the same logic in a new labor-market setting.

The anchor menu should be:
- `[@muellerSpinnewijnTopa2021]`
- `[@dellaVignaListMalmendierRao2022]`
- `[@bhargavaManoli2015]`
- `[@bernheimFradkinPopov2015]`

The bounded student path should end in a one-page research-design memo, not just a replication note.

## Slide and visual expectations

The slides should feel like a capstone studio deck, not a normal lecture recap.

At minimum, they should include:
1. why a final synthesis week matters,
2. a full course architecture map,
3. what counts as a behavioral-labor contribution,
4. welfare and interpretation,
5. topic -> wedge -> setting -> design -> method,
6. when reduced-form is enough and when structure is needed,
7. frontier project families,
8. common failure modes,
9. a research memo template,
10. a final bridge to dissertation-quality work and adjacent special topics.

## Suggested chapter tone

- research-heavy
- practical
- explicit about methods
- explicit about welfare and interpretation
- optimistic about project opportunities
- not a recap for its own sake

## Reading ladder shape

The reading ladder should distinguish:
- **foundation**: field framing and welfare logic;
- **anchor papers**: one paper from each main course domain;
- **project inspiration**: frontier pieces with unresolved questions.

The chapter should not try to summarize every paper from the course. It should curate the right set for turning understanding into research.