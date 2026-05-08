# Week 10 source pack — Aggregate Fluctuations and Labor Market Adjustment

## Purpose of this file

This is the intellectual control file for Labor II Week 10. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do aggregate fluctuations reshape unemployment, vacancies, job finding, separations, job-to-job transitions, wages, and match quality, and what are the main theoretical and empirical tools labor economists use to study those margins?

## Week identity

- Course: Labor II
- Week: 10
- Length: 3 hours core, with an optional 60–90 minute extension block
- Position in sequence: follows Week 9 on labor regulation, enforcement, and insurance and precedes Week 11 on technology, automation, AI, and labor demand
- Goal: give students a labor-focused framework for aggregate adjustment that begins with canonical search-and-matching logic, then moves to stock-flow accounting, search efficiency, separations, job-to-job transitions, wage cyclicality, and match-quality/sorting evidence

## Why this week matters

Weeks 1–9 studied labor demand, wage-setting, search, monopsony, and labor institutions mostly in partial equilibrium or institution-specific settings. Week 10 zooms out and asks how those mechanisms behave when shocks are aggregate.

This should still feel like labor economics, not a general macro lecture. The organizing idea is that aggregate fluctuations matter through several distinct but related margins:

1. **Stocks and flows**
   - unemployment and vacancies are stocks;
   - job finding, separations, job-to-job transitions, and participation transitions are flows.

2. **Matching versus composition**
   - movements in the Beveridge curve can reflect genuine matching efficiency changes,
   - but they can also reflect heterogeneity, market segmentation, or compositional shifts in workers and vacancies.

3. **Unemployment versus reallocation**
   - some cyclical variation shows up in unemployment and nonemployment,
   - some shows up in job-to-job transitions, worker churning, and reallocation across firms.

4. **Wages versus quantity adjustment**
   - cyclical slack can show up in unemployment, vacancies, and hiring;
   - but it can also show up in weak wage growth, lower job-ladder mobility, deteriorating match quality, or more intense selection.

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. write down the core labor-market flow system connecting employment, unemployment, nonparticipation, and vacancies;
2. explain how the canonical matching model links vacancies, unemployment, job finding, and wage-setting;
3. distinguish stock movements in unemployment from flow movements in job finding, separations, and job-to-job transitions;
4. explain why the Beveridge curve can move because of either matching efficiency or composition/heterogeneity;
5. describe why endogenous separation, on-the-job search, and job ladders matter for cyclical adjustment;
6. explain what is meant by cyclical wage rigidity, wage cyclicality for incumbents versus movers, and wage cyclicality net of sorting;
7. evaluate empirical evidence on search efficiency, match quality, churning, and the job ladder over the business cycle;
8. connect aggregate labor-market adjustment to the institution/policy block behind it and to the secular shock lectures ahead.

## Tone and authorial voice

- This chapter should sound like an advanced PhD labor-economics field-course lecture, not a New Keynesian macro lecture.
- It should stay focused on labor-market objects: unemployment, vacancies, hazards, separations, job-to-job transitions, wages, matches, and worker-firm reallocation.
- It should avoid drifting into a general lecture on the Phillips curve, inflation targeting, or monetary policy.
- It should repeatedly distinguish:
  - **stocks** from **flows**,
  - **matching efficiency** from **heterogeneity/composition**,
  - **unemployment** from **reallocation**,
  - **wage cyclicality** from **sorting-induced wage composition**,
  - and **theory objects** from **empirical proxies**.

## Canonical references for Week 10

### Conceptual and framework references
- Shimer, equilibrium unemployment and vacancy volatility [@shimer2005CyclicalBehavior]
- Hall, equilibrium wage stickiness [@hall2005EquilibriumWageStickiness]
- Mortensen and Pissarides, endogenous job creation and destruction [@mortensenPissarides1994JobCreation]
- Rogerson, Shimer, and Wright, survey of search-theoretic labor models [@rogersonShimerWright2005Survey]
- Elsby, Michaels, and Ratner, Beveridge-curve survey [@elsbyMichaelsRatner2015Beveridge]

### Core evidence on stocks, flows, and cyclical unemployment
- Elsby, Michaels, and Solon, ins and outs of cyclical unemployment [@elsbyMichaelsSolon2009InsOuts]
- Krusell, Mukoyama, Rogerson, and Şahin, gross worker flows over the cycle [@krusellMukoyamaRogersonSahin2017GrossFlows]
- Fujita and Ramey, endogenous separation and Beveridge dynamics [@fujitaRamey2012EndogenousSeparation]

### Matching efficiency and Beveridge-curve shifts
- Barnichon and Figura, aggregate matching function and heterogeneity [@barnichonFigura2015AggregateMatching]
- Barlevy, Faberman, Hobijn, and Şahin, shifting reasons for Beveridge-curve shifts [@barlevyFabermanHobijnSahin2024BeveridgeShifts]

### Separations, job ladders, and composition of unemployment
- Mueller, separations, sorting, and cyclical unemployment [@mueller2017SeparationsSorting]
- Haltiwanger, Hyatt, Kahn, and McEntarfer, cyclical job ladders [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders]

### Wages, job-to-job transitions, and sorting
- Karahan, Michaels, Pugsley, Şahin, and Schuh, job-to-job transitions and wage fluctuations [@karahanMichaelsPugsleySahinSchuh2017JobToJob]
- Figueiredo, wage cyclicality and labor-market sorting [@figueiredo2022WageCyclicality]
- Morales-Jiménez, unemployment and wages under information frictions [optional theory extension] [@moralesJimenez2022InformationFrictions]

## Non-negotiable formal core

The current draft should not stop at verbal framework. The final chapter needs a concrete mathematical spine. At a minimum, the Field Core should explicitly introduce the following objects.

### A. Flow accounting and unemployment dynamics

Start with the two-state continuous-time benchmark and then briefly note the three-state extension.

```{math}
:label: eq:u-law-motion
\dot u_t = s_t(1-u_t) - f_t u_t
```

with steady state

```{math}
:label: eq:u-steady-state
u_t^{\ast} = \frac{s_t}{s_t + f_t}.
```

This is the cleanest way to show that the unemployment stock can move because of either inflows {math}`s_t` or outflows {math}`f_t`.

Then briefly connect to a three-state flow matrix:

```{math}
:label: eq:three-state-flow
\begin{pmatrix}
E_{t+1}\\
U_{t+1}\\
N_{t+1}
\end{pmatrix}
=
P_t
\begin{pmatrix}
E_t\\
U_t\\
N_t
\end{pmatrix},
```

where {math}`P_t` collects the {math}`E,U,N` transition hazards. The point is not to make the week about nonparticipation, but to show students where “hidden slack” lives and why a pure two-state view can miss participation adjustment.

### B. Matching technology and market tightness

The canonical matching function should appear explicitly:

```{math}
:label: eq:matching
m_t = \mu_t u_t^{\alpha} v_t^{1-\alpha},
```

with market tightness {math}`\theta_t = v_t/u_t`, job-finding rate

```{math}
:label: eq:job-finding
f_t = \frac{m_t}{u_t} = \mu_t \theta_t^{1-\alpha},
```

and vacancy-filling rate

```{math}
:label: eq:vacancy-filling
q_t = \frac{m_t}{v_t} = \mu_t \theta_t^{-\alpha}.
```

Students should see that cyclical movements in unemployment can come from movements in tightness, the efficiency term {math}`\mu_t`, or both.

### C. Vacancy posting, surplus, and the volatility puzzle

The lecture should include a minimal value/surplus block so that Shimer and Hall do not become pure verbal labels.

A stripped-down free-entry condition is enough:

```{math}
:label: eq:free-entry
\kappa = q_t \, \mathbb{E}_t[J_{t+1}],
```

or equivalently {math}`\kappa / q_t = \mathbb{E}_t[J_{t+1}]`, where {math}`J_t` is the firm value of a filled job and {math}`\kappa` is vacancy posting cost.

Then define match surplus

```{math}
:label: eq:surplus
S_t = J_t + W_t - U_t,
```

and explain that the Shimer volatility problem is fundamentally about why plausible aggregate shocks do not move the surplus enough in the benchmark model [@shimer2005CyclicalBehavior], while Hall’s wage-stickiness argument effectively keeps wages from absorbing too much of the shock and thereby amplifies vacancy creation [@hall2005EquilibriumWageStickiness].

You do **not** need to turn the week into a full wage-bargaining lecture, but you do need enough math for students to see why the surplus is the object that matters.

### D. Beveridge curve and matching-efficiency residuals

Do not present “matching efficiency” only as a verbal concept. Write down the residual:

```{math}
:label: eq:matching-efficiency
\mu_t = \frac{m_t}{u_t^{\alpha} v_t^{1-\alpha}}.
```

Then immediately warn that this is not automatically a structural primitive. The same residual can move because of search intensity, heterogeneity, vacancy composition, worker composition, or segmentation [@barnichonFigura2015AggregateMatching]; [@barlevyFabermanHobijnSahin2024BeveridgeShifts].

Under exogenous separation, the steady-state Beveridge object can be written as

```{math}
:label: eq:beveridge
u_t^{\ast} = \frac{s_t}{s_t + \mu_t \theta_t^{1-\alpha}},
```

which makes clear that Beveridge-curve shifts can be read as changes in separation, matching, or tightness, but not identified as one of those without extra structure.

### E. Endogenous separation

The week should not treat separation as an exogenous constant. At least one threshold or surplus-based destruction object should appear:

```{math}
:label: eq:endogenous-separation
s_t = \Pr\!\left(S_t(z) < 0\right),
```

or, if you want the integral form,

```{math}
:label: eq:separation-integral
s_t = \int \mathbf{1}\{S_t(z) < 0\}\, dG_t(z).
```

The point is to show students that recessionary unemployment can rise because matches that were marginally viable in good times are no longer viable in bad times [@mortensenPissarides1994JobCreation]; [@fujitaRamey2012EndogenousSeparation].

### F. On-the-job search, job ladders, and churning

The lecture should also include one simple job-to-job object. A reduced-form on-the-job search representation is enough:

```{math}
:label: eq:ee-flow
EE_t = \lambda_t^{e}\Pr\!\left(w' > w\right),
```

where {math}`\lambda_t^{e}` is the employed offer-arrival rate. Students should see that cyclical wage growth can collapse partly because the {math}`EE_t` margin collapses, not only because the unemployed find jobs less often [@karahanMichaelsPugsleySahinSchuh2017JobToJob].

For churning/excess worker reallocation, include one accounting identity such as

```{math}
:label: eq:churning
\text{Churning}_t = \text{Worker Reallocation}_t - \text{Job Reallocation}_t.
```

This is useful because it separates net employment adjustment from replacement hiring and within-firm turnover.

### G. Wage cyclicality and composition

There should be at least one explicit measurement equation showing why wage cyclicality is hard to interpret:

```{math}
:label: eq:wage-cyclicality
\Delta \log \bar w_t = \beta^{I} \, cyc_t + \omega_t^{EE}\beta^{EE} \, cyc_t + comp_t + sort_t,
```

where {math}`\beta^{I}` captures incumbent wage cyclicality, {math}`\beta^{EE}` captures mover/job-ladder cyclicality, and {math}`comp_t` and {math}`sort_t` capture selection and sorting. The point is not the exact parametric form; the point is to make students see why “wages are weakly cyclical” is often a composition statement, not a clean structural claim [@figueiredo2022WageCyclicality].

## Reading-ladder design

### Ladder A. Canonical framework and the volatility puzzle
- [@rogersonShimerWright2005Survey]
- [@shimer2005CyclicalBehavior]
- [@hall2005EquilibriumWageStickiness]

### Ladder B. Flow accounting and Beveridge-curve interpretation
- [@elsbyMichaelsSolon2009InsOuts]
- [@elsbyMichaelsRatner2015Beveridge]
- [@barnichonFigura2015AggregateMatching]

### Ladder C. Endogenous separation, reallocation, and job ladders
- [@mortensenPissarides1994JobCreation]
- [@fujitaRamey2012EndogenousSeparation]
- [@mueller2017SeparationsSorting]
- [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders]

### Ladder D. Wages, job-to-job transitions, and match quality
- [@karahanMichaelsPugsleySahinSchuh2017JobToJob]
- [@figueiredo2022WageCyclicality]
- [@barlevyFabermanHobijnSahin2024BeveridgeShifts]

## Lab design spine

The lab should follow the standard Reproduce -> Diagnose -> Transfer structure.

### Primary anchor
- [@barnichonFigura2015AggregateMatching]

### Secondary / challenge anchor
- [@elsbyMichaelsSolon2009InsOuts]

### Optional extension anchor
- [@karahanMichaelsPugsleySahinSchuh2017JobToJob]

### Transfer ideas

Bounded transfer ideas could include:
- estimating a simple Beveridge curve and matching-efficiency residual using public unemployment and vacancy data;
- reproducing an unemployment stock-flow decomposition over a selected recession window;
- comparing pre- and post-crisis Beveridge dynamics in a public aggregate series;
- building a synthetic or reduced-data job-to-job cyclicality exercise tied to wage growth or reallocation.

The lab handout should force students to name:
1. the cyclical labor-market object being studied,
2. whether the object is a stock, flow, or derived efficiency concept,
3. which margin is directly observed,
4. which margin is inferred,
5. and which transfer exercise changes the sample, recession episode, geography, or data aggregation.

## Chapter architecture

The final chapter should be one of the heavier weeks in Labor II. It should move cleanly from theory to evidence.

### 1. Bridge and reorientation

Begin with one clean question:

**When aggregate labor demand weakens or strengthens, which labor-market margins do the adjusting?**

### 2. Flow accounting and the stock-flow view of unemployment

This should be a formal opening section, not only a prose section.

Minimum content:
- equation [](#eq:u-law-motion),
- steady state [](#eq:u-steady-state),
- a short three-state extension using [](#eq:three-state-flow),
- intuitive contrast between stock movements and hazard movements.

### 3. Matching, tightness, and the Beveridge curve

Minimum content:
- equations [](#eq:matching)–[](#eq:vacancy-filling),
- market tightness as the key state variable,
- Beveridge curve logic,
- matching-efficiency residual [](#eq:matching-efficiency),
- warning that efficiency residuals mix structure and composition.

### 4. Surplus, vacancy creation, and the volatility puzzle

Minimum content:
- free-entry condition [](#eq:free-entry),
- match surplus [](#eq:surplus),
- Shimer volatility puzzle,
- Hall amplification via wage rigidity.

### 5. Unemployment stocks versus flows

Minimum content:
- ins-and-outs decomposition,
- cyclical inflows versus outflows,
- why severe recessions often involve both,
- explicit discussion of what is observed and what is inferred in CPS-style decompositions.

### 6. Separations, churning, job-to-job transitions, and on-the-job search

This should go well beyond a standard matching lecture.

Minimum content:
- endogenous separation objects [](#eq:endogenous-separation) or [](#eq:separation-integral),
- on-the-job search object [](#eq:ee-flow),
- churning/excess reallocation object [](#eq:churning),
- job ladders and reallocation,
- why aggregate labor adjustment is not just unemployment.

### 7. Wages, sorting, and match quality over the cycle

Minimum content:
- incumbents vs movers,
- job-ladder mobility,
- wage cyclicality decomposition [](#eq:wage-cyclicality),
- match quality and sorting,
- why measured rigidity is often contaminated by composition.

### 8. Measurement, identification, and open questions

Minimum content:
- what different data sources see and miss: CPS, JOLTS, LEHD, firm panels, public vacancy series;
- why time-series fit is not the same as identifying a mechanism;
- why state/regional variation, matched employer-employee data, and decomposition methods complement aggregate time series;
- open questions on search efficiency, hysteresis, job ladders, temporary layoffs, and cyclical match quality.

### 9. Bridge to Week 11

The bridge should say:
- Week 10 studied how aggregate labor markets react to cyclical shocks.
- Week 11 will ask how labor markets adjust to technology, automation, AI, and broader labor-demand restructuring.
- The transition is from **cyclical adjustment** to **structural or secular adjustment**, while keeping the same labor-market margins in view.

## Must-include formal objects

The final chapter should include at least:
- one flow law of motion for unemployment,
- one steady-state unemployment expression,
- one matching function,
- one job-finding and one vacancy-filling equation,
- one free-entry or surplus condition,
- one Beveridge-curve interpretation,
- one matching-efficiency residual,
- one endogenous-separation object,
- one on-the-job-search or job-to-job object,
- one wage-cyclicality decomposition.

## Figures and tables

The chapter should use the supplied tables:
- `assets/tables/10-cyclical-margins-map.md`
- `assets/tables/10-theory-to-evidence-map.md`
- `assets/tables/10-measurement-and-identification-map.md`

If figures do not yet exist, create clean schematic figures with these stable filenames:
- `assets/figures/10-aggregate-flows-and-margins.png`
- `assets/figures/10-beveridge-curve-and-matching-efficiency.png`
- `assets/figures/10-separations-jobfinding-unemployment.png`
- `assets/figures/10-job-to-job-wage-cyclicality.png`
- `assets/figures/10-match-quality-and-reallocation.png`

## Optional extension block

### Extension A. Beveridge-curve shifts and post-2020 labor markets
- use [@barlevyFabermanHobijnSahin2024BeveridgeShifts]
- discuss why the source of Beveridge shifts changed across eras
- connect measurement to policy interpretation

### Extension B. Job ladders, match quality, and wage composition
- use [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders] and [@figueiredo2022WageCyclicality]
- focus on how reallocation margins change measured wages and job quality over the cycle

## What to avoid

- Do not turn the week into a generic lecture on inflation, Phillips curves, or monetary policy.
- Do not reduce the entire business cycle to one single margin such as job finding.
- Do not present matching efficiency as a primitive without discussing heterogeneity and composition.
- Do not discuss wages without distinguishing incumbents, movers, and composition effects.
- Do not ignore job-to-job transitions, churning, or on-the-job search.
- Do not let the chapter become a list of macro facts without a research framework.
