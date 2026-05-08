---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Synthesis and Student Research Designs

## Learning objectives

By the end of Week 13, students should be able to:

1. place a labor-market question inside one integrated map of workers, firms, frictions, institutions, and shocks;
2. explain how Labor I worker-side objects and Labor II market-side objects fit together in modern labor economics;
3. choose deliberately among worker-, firm-, establishment-, occupation/task-, region-, and market-level units of analysis;
4. distinguish descriptive, reduced-form, and structural approaches without treating them as a prestige ranking;
5. separate policies from shocks, direct effects from spillovers, and partial-equilibrium responses from equilibrium conclusions;
6. explain how wage-setting, labor market power, institutions, and major shocks interact rather than treating each block as a silo;
7. turn a labor-market mechanism into a bounded research design that names the treatment object, observed margin, and offstage equilibrium channels;
8. identify frontier directions that connect Labor II to Behavioral Labor, Labor Markets and Political/Cultural Institutions, and dissertation-scale questions.

The economic question for Week 13 is explicit: when a labor-market outcome changes, how do we decide whether the key object is worker choice, firm behavior, market friction, institution, or shock, and what kind of empirical design is needed to learn something credible about it?

## Bridge

### Labor I to Labor II and back again

Labor I centered the worker. It emphasized labor supply, human capital, households, inequality, discrimination, mobility, and policy targeted at individuals or families. Labor II kept those worker-side objects alive, but embedded them inside firms, search frictions, wage-setting institutions, labor market power, and large market-level shocks. The two-semester sequence is therefore best understood as one field with two vantage points rather than two disconnected courses.

The practical reason this bridge matters is that a wage, employment, or mobility outcome rarely comes from one mechanism alone. Worker heterogeneity remains important, but it is filtered through labor demand, organizational design, bargaining environments, institutional coverage, enforcement capacity, and the propagation of macro, technology, and trade shocks [@hicks1932; @hamermesh1993; @mortensenPissarides1994].

```{figure} assets/figures/13-labor-ii-architecture-map.png
:name: fig-lii-w13-architecture
Week 13 reorganizes Labor II as one architecture rather than a list of topics. Workers, firms, frictions, institutions, and shocks interact through different units of observation, horizons, and equilibrium channels.
```

```{include} assets/tables/13-labor-ii-architecture-map.md
```

Table {numref}`tbl:labor2-architecture-week13` gives the semester's compact architecture. It is useful precisely because it does not pretend that all questions have the same unit, treatment, or counterfactual.

### One architecture object for the semester

The capstone object for the course is

```{math}
:label: eq:labor2_architecture
Y_{u,t+h} = \mathcal{G}\left(X^{\text{worker}}_{u,t},\; X^{\text{firm}}_{u,t},\; \mathcal{F}_{m,t},\; \mathcal{I}_{m,t},\; \mathcal{S}_{m,t:h}\right).
```

Equation {eq}`eq:labor2_architecture` is not itself a structural model. It is a disciplined organizing device. The index {math}`u` may refer to a worker, firm, establishment, occupation/task cell, region, or market depending on the question. The point is to force the class to ask what changes in the mapping from fundamentals to observed outcomes when the unit changes.

The economic content of the components is straightforward.

1. {math}`X^{\text{worker}}` captures worker heterogeneity, skills, demographics, search intensity, and outside options.
2. {math}`X^{\text{firm}}` captures technology, productivity, organization, management, and labor-demand conditions.
3. {math}`\mathcal{F}` captures frictions such as search, mobility costs, bargaining environments, and information asymmetries.
4. {math}`\mathcal{I}` captures institutions and regulation such as wage floors, bargaining systems, enforcement, insurance, and legal constraints.
5. {math}`\mathcal{S}` captures shocks, including macro fluctuations, technology adoption, and trade exposure.

The payoff from writing the architecture this way is that it makes clear why Labor II is not just "firm behavior" or just "policy." It is about how these objects interact.

:::{admonition} Core Material
:class: tip
- Labor II fits workers, firms, frictions, institutions, and shocks into one architecture
- unit of analysis is part of theory rather than only a data-management choice
- descriptive, reduced-form, and structural approaches answer different questions
- policies and shocks are analytically different objects even when they hit similar outcomes
- a strong project names mechanism, observed margin, equilibrium scope, and contribution
:::

:::{admonition} Optional Extension Block
:class: note
- dissertation-scale and cross-course frontier directions are surfaced later in the chapter under `Frontier directions and bridge beyond Labor II`
:::

## Field Core

### Choosing the unit of analysis is part of the theory

Students often treat the unit of analysis as a data-management choice. In labor economics it is part of the conceptual design.

```{figure} assets/figures/13-question-mechanism-unit-design.png
:name: fig-lii-w13-design-map
The research pipeline in Labor II should run from question to mechanism, then to unit, data, design, equilibrium scope, and contribution. Good projects become clearer as each choice disciplines the next one.
```

The basic unit framework is:

1. **Worker:** use when the mechanism is about earnings, employment, search, mobility, learning, or welfare distribution across people.
2. **Firm or establishment:** use when the mechanism is about labor demand, organization, wage-setting, adoption, or compliance inside production units.
3. **Occupation or task:** use when the object is exposure, job content, task substitution, or the measurement of work.
4. **Region or local labor market:** use when shocks or policies operate through place-based exposure, commuting zones, or regional spillovers.
5. **Market or policy regime:** use when the main object is institutional coverage, equilibrium incidence, or comparison across bargaining or regulatory systems.

Each unit does something well and leaves something offstage. Worker panels are strongest on individual trajectories but may miss general-equilibrium price and entry responses. Firm or establishment data are strong on direct adjustment but weaker on uncovered labor-market spillovers. Occupation or task cells are useful for measurement and exposure design but are often far from welfare objects. Regional designs identify place incidence well but do not, by themselves, identify the welfare of incumbent workers. Market-level comparisons clarify institutions but often aggregate away rich heterogeneity.

The class should therefore ask four questions every time the unit is chosen:

1. What is the unit of treatment?
2. What is the unit of observation?
3. What margin is actually observed?
4. Which equilibrium channels are offstage because of that choice?

### A generic empirical object and what it does not guarantee

Much of the empirical literature can be summarized by

```{math}
:label: eq:labor2_empirical
\Delta y_{u,t+h} = \beta D_{u,t} + X_{u,t}'\Gamma + \varepsilon_{u,t+h}.
```

Equation {eq}`eq:labor2_empirical` looks familiar, but its content changes dramatically with {math}`u`, {math}`D`, and {math}`y`.

1. If {math}`u` is a worker, then {math}`D` may be treatment exposure, a layoff event, a union contract, or a human-capital shock.
2. If {math}`u` is a firm or establishment, then {math}`D` may be a payroll-tax change, technology adoption, a merger, or enforcement intensity.
3. If {math}`u` is a local labor market, then {math}`D` may be import exposure, robot exposure, or regional policy intensity.
4. If {math}`u` is a market or policy regime, then {math}`D` may be bargaining coverage, a statutory wage floor, or an insurance rule.

The capstone lesson is that the equation is never the main intellectual contribution. The main contribution comes from the match between question, mechanism, unit, variation, and claim.

### Descriptive, reduced-form, and structural approaches are choice problems

The semester should leave students with a clear framework for choosing among three broad approaches.

1. **Descriptive or decomposition work:** best when the first-order contribution is measurement, classification, trend decomposition, exposure construction, or a new empirical object.
2. **Reduced-form causal work:** best when a policy or shock is well defined, the treatment object is clear, and the observed margin is closely aligned with the question.
3. **Structural or equilibrium work:** best when the question requires counterfactual welfare analysis, equilibrium spillovers, dynamic adjustment, or policy simulations outside the support of the observed variation.

This is not a status hierarchy. Descriptive work is enough when the field lacks a clean measure. Reduced-form work is enough when the policy or shock is sharp and the claim is local. Structural work becomes necessary when the question itself is about equilibrium propagation, welfare, or counterfactual policy combinations [@saezSchoeferSeim2019; @kimVogel2021TradeShocksLaborMarketAdjustment].

### Comparative synthesis I: wage-setting and labor market power

Weeks 1 through 8 can be reread as one large wage-setting block. Labor demand sets the value of labor to firms; search and matching generate frictions; bargaining and posting determine how surplus is split; monopsony determines the elasticity of labor supply to the firm; unions and collective bargaining create institutional voice; and wage floors or labor standards alter the outside-option and coverage environment [@hicks1932; @mortensenPissarides1994; @hallMilgrom2008; @yehMacalusoHershbein2022; @jagerNaiduSchoefer2024].

The unifying question is not "which model is correct?" It is "which wage-setting margin is doing the work here?" The answer differs across designs.

1. In a labor-demand setting, wages matter because they shift cost and scale decisions.
2. In a search-and-bargaining setting, wages depend on nonemployment values, outside offers, and surplus division.
3. In a modern monopsony setting, wages depend on labor supply to the firm, mobility frictions, and rents.
4. In an institutional setting, wages also depend on coverage, bargaining coordination, legal standards, and enforcement.

[@saezSchoeferSeim2019] is useful here because it makes incidence, labor demand, and rent sharing interact rather than treating them as separate literatures. [@yehMacalusoHershbein2022] clarifies that concentration, markdowns, and mobility are related but not identical objects. [@jagerNaiduSchoefer2024] shows that bargaining institutions reshape the wage structure in ways that cannot be reduced to one competitive benchmark.

The big synthesis point is that labor market power is not an optional add-on to wage-setting. It is one of the mechanisms that determines how wages, employment, pass-through, and policy incidence are translated into observed outcomes.

### Comparative synthesis II: institutions and regulation

The institution block is easiest to understand when students stop asking whether a policy "works" in the abstract and instead ask four narrower questions.

1. What margin is directly targeted?
2. Who is directly covered?
3. Where do spillovers go?
4. Which outcome object is being observed, and which welfare object remains offstage?

Minimum wages, bargaining systems, labor law, enforcement, insurance, and transparency policies all differ along these dimensions [@cengizDubeLindnerZipperer2019; @jagerNaiduSchoefer2024; @macleod2011GreatExpectations]. A minimum wage directly targets the lower tail of the wage distribution, but its incidence also runs through employment, hours, prices, turnover, composition, compliance, and spillovers. Collective bargaining changes wages and worker voice, but it also changes coverage, compression, coordination, and the translation of productivity into pay. Labor law and enforcement are not separable because rights without compliance capacity are weak treatments.

The capstone lesson is that institutions change the mapping from micro behavior to equilibrium outcomes. That is why policy evaluation in Labor II is rarely only about a treated worker or a treated firm. It is about coverage, uncovered margins, and equilibrium response.

### Comparative synthesis III: macro, technology, and trade shocks

The shock block of Labor II is best taught comparatively. Macro fluctuations, technology, and trade are not the same shock, but they all raise the same discipline questions: what is exposed, which margin adjusts first, what horizon is being measured, and what kind of equilibrium object is needed to interpret the result [@shimer2005CyclicalBehavior; @acemogluRestrepo2020RobotsJobs; @autorDornHanson2013ChinaSyndrome; @kimVogel2021TradeShocksLaborMarketAdjustment].

Macro shocks highlight vacancies, unemployment, job-finding, separations, wage cyclicality, and matching efficiency. Technology shocks highlight tasks, firm adoption, worker learning, and local reallocation. Trade shocks highlight import competition, export exposure, offshoring, local incidence, and slow worker or place adjustment. The bridge across all three is that short-run observed outcomes and long-run welfare interpretations are rarely the same object.

This is why the course should always distinguish:

1. worker adjustment from place adjustment;
2. short-run incidence from long-run reallocation;
3. direct exposure from indirect spillovers;
4. observed outcomes from counterfactual welfare objects.

### Policies versus shocks are analytically different objects

```{figure} assets/figures/13-policy-vs-shock-comparison.png
:name: fig-lii-w13-policy-shock
Policies and shocks both move labor markets, but they differ in timing, treatment assignment, equilibrium propagation, and the counterfactual questions they invite. Keeping those differences visible improves both empirical design and interpretation.
```

Policies and shocks should not be thrown into one generic "treatment effects" bucket.

1. A **policy** usually has a legal or administrative margin, a covered population, and a natural implementation date.
2. A **shock** usually changes prices, exposure, technology, or demand conditions without clean coverage boundaries.
3. Policy evaluation often centers on compliance, incidence, and spillovers from a rule.
4. Shock evaluation often centers on exposure mapping, transmission channels, and dynamic adjustment.

The difference matters for design. A minimum-wage study can often define the treated jurisdiction and the statutory timing. A robot or trade-exposure study often needs a model of how sectoral change maps into local treatment intensity. The equilibrium challenge also differs. Policies typically invite questions about avoidance, uncovered sectors, prices, and legal enforcement. Shocks typically invite questions about reallocation, migration, entry, sectoral shifts, and dynamic propagation.

### Partial equilibrium, equilibrium reasoning, and welfare caution

One of the most important habits Labor II should leave behind is resistance to over-claiming. A coefficient on wages, employment, or transitions is not yet a welfare statement.

```{math}
:label: eq:labor2_welfare_caution
\Delta W \neq \omega \cdot \beta
```

Equation {eq}`eq:labor2_welfare_caution` is a warning label. Without additional assumptions on spillovers, incidence, adjustment, and distributional weights, a reduced-form estimate {math}`\beta` does not map mechanically into welfare. The main cases where students must slow down are familiar.

1. Place-level losses do not automatically equal incumbent-worker welfare losses.
2. Short-run employment declines do not settle long-run adjustment questions.
3. Treated-firm effects do not equal market-wide incidence.
4. Measured wages or employment do not exhaust nonwage amenities, insurance, or worker voice.

The practical takeaway is not that reduced-form evidence is weak. It is that reduced-form evidence is strongest when the question is local and the claim is disciplined. The moment the paper's conclusion depends on uncovered margins, equilibrium spillovers, or welfare aggregation, more structure is needed.

### When is a design "enough"?

The capstone should help students avoid both overreach and needless escalation.

1. A descriptive design is enough when the field lacks a clean object, exposure measure, decomposition, or measurement frame.
2. A reduced-form design is enough when the mechanism and observed margin line up well enough to answer a bounded causal question.
3. A structural design is needed when the contribution requires equilibrium propagation, welfare, dynamic transition paths, or policy counterfactuals beyond the observed variation.

The phrase "enough" is doing real work here. The point is not to upgrade every good question into a structural dissertation. The point is to match the design to the claim.

### From question to mechanism to contribution

The capstone research template for Labor II is:

1. question;
2. mechanism;
3. unit;
4. data;
5. design;
6. counterfactual scope;
7. contribution.

```{include} assets/tables/13-research-design-template.md
```

Table {numref}`tbl:research-design-template-week13` is the practical template for research design memos. It is meant to convert broad curiosity into a bounded first project.

The common successful paths look different from one another.

1. A worker-side extension may ask whether an established place-level shock also changes mobility, job ladders, or within-worker wage growth.
2. A firm-side extension may ask whether a known policy or shock works differently through organizational design, compliance capacity, or pass-through.
3. A task or occupation extension may improve measurement rather than estimate a new causal effect.
4. A market-level extension may ask whether an institution changes spillovers, coordination, or equilibrium adjustment rather than only direct treatment effects.

What these successful paths share is not the same method. It is that the contribution is clear before the specification is.

### Common failure modes

```{figure} assets/figures/13-common-failure-modes.png
:name: fig-lii-w13-failure-modes
The most common Week 13 mistakes are conceptual before they are econometric: vague mechanisms, mismatched units, hidden equilibrium claims, and over-interpretation of one observed margin.
```

The recurring mistakes in labor-market research design are predictable.

1. confusing gaps with mechanisms;
2. letting the unit of treatment and unit of observation drift apart without explanation;
3. narrating a short-run coefficient as if it were a long-run equilibrium result;
4. treating a place effect as if it were automatically a worker-welfare statement;
5. using "equilibrium" language without naming the equilibrium object;
6. claiming policy relevance without saying who is covered and where spillovers go.

The reason to make these mistakes explicit is supportive rather than punitive. Most weak early-stage projects fail here, not because the student lacks technique, but because the empirical object and the conceptual claim were never fully matched.

### Frontier directions and bridge beyond Labor II

```{include} assets/tables/13-frontier-and-bridge-map.md
```

Table {numref}`tbl:frontier-bridge-week13` maps the next step outward from the core course. The point of the frontier section is not to declare a trend list. It is to show how a bounded Labor II design can connect to later field courses and dissertation questions.

```{figure} assets/figures/13-frontier-and-dissertation-bridge.png
:name: fig-lii-w13-frontier-bridge
Week 13 should end with a bridge, not a summary. Labor II provides the market-side backbone for later work on behavioral frictions, political and cultural institutions, worker power, technology, globalization, and dissertation-scale labor questions.
```

Three outward bridges are especially important.

1. **Back to Labor I:** the next research step may revisit worker heterogeneity, human capital, family constraints, inequality, discrimination, or mobility with better market-side discipline.
2. **Toward Behavioral Labor:** search behavior, application technology, worker beliefs, firm evaluation, and bounded rationality become more interesting once search frictions, wage-setting, and institutions are already onstage.
3. **Toward Labor Markets and Political/Cultural Institutions:** bargaining systems, enforcement, informality, norms, identity, and state capacity can be studied as labor-market objects rather than as detached political-economy background.

At the dissertation level, the strongest Week 13 projects are usually modest in scale but sharp in mechanism. A student does not need the field's grand unified model. The student needs a labor-market question with a credible unit, observable margin, and honest statement about what remains offstage.

## Research Lab

The Week 13 lab is a capstone studio rather than a standard single-paper replication. Its logic is **Diagnose -> Compare -> Design**.

Students should choose one anchor paper, or one tightly related pair, from the required capstone menu:

1. [@saezSchoeferSeim2019]
2. [@yehMacalusoHershbein2022]
3. [@cengizDubeLindnerZipperer2019]
4. [@jagerNaiduSchoefer2024]
5. [@acemogluRestrepo2020RobotsJobs]
6. [@autorDornHanson2013ChinaSyndrome]

For the chosen anchor, the lab requires students to identify:

1. the central labor-market mechanism;
2. the unit of treatment and observation;
3. the observed margin;
4. the key equilibrium concern;
5. one plausible extension or transfer design.

The local handout lives at [labs/13-synthesis-and-student-research-designs/lab.md](labs/13-synthesis-and-student-research-designs/lab.md). The bounded local path generates a memo-ready artifact rather than a full estimation exercise, but it still produces a concrete research-design document that can be discussed, revised, and smoke-tested.

## Methods Box

Keep these distinctions explicit throughout the capstone.

1. Worker-level, firm-level, establishment-level, occupation/task-level, place-level, and market-level objects answer different questions.
2. Policies and shocks are different treatment families and should not be interpreted with identical logic.
3. Partial-equilibrium effects and equilibrium effects are distinct objects even when they use similar notation.
4. Short-run adjustment and long-run adjustment can move in opposite directions.
5. Descriptive decomposition, reduced-form identification, and structural counterfactual analysis support different claims.
6. Outcome variables such as wages, employment, unemployment, or transitions are not automatically welfare objects.
7. Direct treatment effects and spillovers must be separated whenever coverage or reallocation matters.
8. A design is only as credible as its definition of treatment, observed margin, and offstage equilibrium channels.

## Reading ladder

### Ladder A. Architecture and classic foundations

- [@hicks1932]
- [@hamermesh1993]
- [@mortensenPissarides1994]

### Ladder B. Wage-setting, power, and institutions

- [@saezSchoeferSeim2019]
- [@yehMacalusoHershbein2022]
- [@cengizDubeLindnerZipperer2019]
- [@jagerNaiduSchoefer2024]
- [@macleod2011GreatExpectations]

### Ladder C. Shocks and adjustment

- [@shimer2005CyclicalBehavior]
- [@acemogluRestrepo2020RobotsJobs]
- [@autorDornHanson2013ChinaSyndrome]
- [@kimVogel2021TradeShocksLaborMarketAdjustment]

### Ladder D. Capstone studio and frontier directions

- one paper from the wage-setting or labor-power block
- one paper from the institution or regulation block
- one paper from the macro-adjustment block
- one paper from the technology or trade block

## Exercises / discussion prompts

1. Pick one result from Labor I and one result from Labor II that seem to conflict. Is the tension about mechanism, unit, horizon, or equilibrium scope?
2. Take one famous policy paper and one famous shock paper from the course. Compare their treatment object, observed margin, and main offstage equilibrium channel.
3. Choose a student research idea and state the smallest design that would be enough to support its central claim. Then state what stronger claim would require structural or equilibrium machinery.
4. Compare a worker-level extension and a place-level extension of the same anchor paper. Which one is more informative for mechanism, and which one is more informative for welfare?

## Reproducibility or code lab note

Week 13's bounded lab path is memo-first by design. The local script builds an anchor-paper menu and a structured research-design memo scaffold rather than a full replication package. That is deliberate: the pedagogical goal is to make students diagnose, compare, and design with discipline before they scale up to data-heavy work.

## Slide companion note

The slide companion for this week lives at [slides/week13/13-synthesis-and-student-research-designs.tex](slides/week13/13-synthesis-and-student-research-designs.tex). The deck is intentionally tighter than the chapter prose: it defines the capstone question, shows the architecture map, compares design choices, isolates common failure modes, and ends with bridges to later labor-field and dissertation work.
