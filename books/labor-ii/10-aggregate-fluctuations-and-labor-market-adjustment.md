---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Aggregate Fluctuations and Labor Market Adjustment

## Learning objectives

By the end of Week 10, students should be able to:

1. distinguish unemployment as a stock from job finding, separations, job-to-job moves, and participation transitions as flow hazards;
2. derive and interpret the canonical law of motion for unemployment and its steady-state implication;
3. explain how matching, market tightness, free entry, and match surplus connect vacancies to hires and unemployment;
4. distinguish Beveridge-curve shifts driven by tightness, separations, matching residuals, and heterogeneity or composition;
5. explain why cyclical unemployment depends on both inflows and outflows and why separations cannot be treated as a nuisance margin;
6. analyze aggregate labor adjustment through unemployment, job-to-job mobility, churning, wage cyclicality, and match quality rather than through one single macro statistic;
7. evaluate empirical evidence by naming the identifying variation, unit of observation, observed margin, and key hidden margin left offstage;
8. connect Week 10 back to Week 9 institutions and forward to Week 11 technology and structural adjustment.

The economic question for Week 10 is straightforward but demanding: when aggregate conditions weaken or strengthen, which labor-market margins do the adjusting, and how do labor economists separate matching, separation, mobility, wages, and composition in the evidence?

## Bridge

Week 9 studied labor regulation, enforcement, and insurance as mechanisms that shape layoffs, recalls, vacancy posting, search, and formal-versus-informal adjustment. Week 10 scales those same objects up to aggregate fluctuations. The point is not to leave labor economics for a general macro detour. It is to ask what happens to labor-market stocks, hazards, wages, and match quality when shocks are economy-wide rather than policy-specific or local.

This week should feel like a return to Week 4 search and matching, but at a higher level of resolution. Week 4 introduced unemployment, vacancies, separations, and job ladders as frictional labor-market objects. Week 10 asks how those margins move together over the cycle and why the same recession can show up as lower job finding, higher separation, weaker job-to-job mobility, slower wage growth, more intense worker sorting, or an outward shift in the Beveridge curve. The lecture therefore stays centered on labor objects: workers, firms, matches, hazards, mobility, and wages [@rogersonShimerWright2005Survey; @elsbyMichaelsRatner2015Beveridge].

Three distinctions must stay explicit from the start.

1. Unemployment is a stock; job finding, separation, job-to-job mobility, and participation transitions are hazards.
2. A matching-efficiency residual is not automatically a structural primitive; it can absorb heterogeneity, search intensity, segmentation, and vacancy composition.
3. Wage cyclicality for incumbents, movers, and the average observed wage are different objects because composition and sorting move over the cycle.

```{include} assets/tables/10-cyclical-margins-map.md
```

Table {numref}`tbl:cyclical-margins-map` is the opening map for the week. It keeps the lecture anchored to distinct labor-market margins rather than a bag of recession facts.

```{figure} assets/figures/10-aggregate-flows-and-margins.png
:name: fig-lii-w10-flows-margins
Week 10 organizes aggregate labor adjustment around stocks, hazards, and hidden margins. Unemployment is only one visible outcome; job-to-job transitions, participation shifts, and wage composition matter at the same time.
```

Figure {numref}`fig-lii-w10-flows-margins` previews the lecture logic. Aggregate labor adjustment is a map of margins, not a single time series.

:::{admonition} Core Material
:class: tip
- aggregate adjustment runs through stocks, hazards, job ladders, wages, and composition at the same time
- unemployment stocks are not interpretable without inflows and outflows
- Beveridge-curve shifts can reflect composition, search intensity, mismatch, or matching efficiency
- job-to-job mobility and wage cyclicality are central cyclical margins, not side details
- macro-labor evidence must name both the observed margin and the hidden margin left offstage
:::

:::{admonition} Optional Extension Block
:class: note
- the Research Lab extension block below surfaces Beveridge-curve shifts after 2020 and cyclical job-ladder questions
:::

## Field Core

### Stocks, flows, and the law of motion for unemployment

The cleanest opening is the two-state flow benchmark. Let {math}`u_t` denote unemployment, {math}`s_t` the employment-to-unemployment hazard, and {math}`f_t` the unemployment-to-employment hazard. Then unemployment evolves according to

```{math}
:label: eq:u-law-motion
\dot u_t = s_t(1-u_t) - f_t u_t
```

with steady state

```{math}
:label: eq:u-steady-state
u_t^{\ast} = \frac{s_t}{s_t + f_t}.
```

Equations {eq}`eq:u-law-motion` and {eq}`eq:u-steady-state` make the first non-negotiable Week 10 point visible. A high unemployment stock can come from high inflows, low outflows, or both. Saying that unemployment rose is therefore not yet an explanation. We need to know which hazard moved and whether the observed stock hides other adjustments in labor-force participation or direct job-to-job mobility [@elsbyMichaelsSolon2009InsOuts].

The two-state benchmark is useful because it is transparent, but it is not complete. Hidden slack often lives in a three-state system with employment, unemployment, and nonparticipation:

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

where {math}`P_t` collects the transition hazards across {math}`E`, {math}`U`, and {math}`N`. The point is not to make the week about participation alone. It is to show where “hidden slack” enters and why a pure unemployment-rate narrative can miss important cyclical movement in labor supply and attachment [@krusellMukoyamaRogersonSahin2017GrossFlows].

### Matching, tightness, and the Beveridge curve

The canonical matching function is

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

These equations separate the worker-side and vacancy-side objects. {math}`f_t` governs the outflow from unemployment; {math}`q_t` governs recruiting congestion and the expected payoff from vacancy posting. Tightness is therefore good news for workers and bad news for recruiters at the same time. The logic is familiar from Week 4, but Week 10 uses it to study cyclical volatility rather than only steady-state search [@shimer2005CyclicalBehavior; @rogersonShimerWright2005Survey].

The reduced-form matching-efficiency residual is

```{math}
:label: eq:matching-efficiency
\mu_t = \frac{m_t}{u_t^{\alpha} v_t^{1-\alpha}}.
```

This residual is tempting to call “search efficiency,” but that interpretation requires care. A movement in {math}`\mu_t` can reflect changes in search intensity, the mix of workers and vacancies, market segmentation, recruiting effort, or true matching technology. Barnichon and Figura's central contribution is precisely to show that aggregate matching residuals absorb heterogeneity and composition, not only structural efficiency [@barnichonFigura2015AggregateMatching]. Barlevy, Faberman, Hobijn, and Şahin make the same point in a modern Beveridge-curve context: the reason for an outward shift is historically contingent rather than mechanically tied to one primitive [@barlevyFabermanHobijnSahin2024BeveridgeShifts].

Under exogenous separation, the steady-state Beveridge object can be written as

```{math}
:label: eq:beveridge
u_t^{\ast} = \frac{s_t}{s_t + \mu_t \theta_t^{1-\alpha}}.
```

Equation {eq}`eq:beveridge` is useful because it turns Beveridge-curve interpretation into a decomposition problem. An outward shift can come from weaker tightness, higher separations, lower residual matching efficiency, or a reweighting of searchers and vacancies across segments [@elsbyMichaelsRatner2015Beveridge].

```{figure} assets/figures/10-beveridge-curve-and-matching-efficiency.png
:name: fig-lii-w10-beveridge
The Beveridge curve is a relationship among unemployment, vacancies, and implied tightness, but shifts in the curve need not identify one single mechanism. Matching residuals mix efficiency, heterogeneity, search intensity, and vacancy composition.
```

Figure {numref}`fig-lii-w10-beveridge` is the lecture's warning label. A time-series fit to unemployment and vacancies is not the same thing as identification of a labor-market mechanism.

### Surplus, vacancy creation, and the volatility puzzle

Search frictions matter for cyclical adjustment because vacancy creation depends on expected surplus. A stripped-down free-entry condition is

```{math}
:label: eq:free-entry
\kappa = q_t \, \mathbb{E}_t[J_{t+1}],
```

where {math}`\kappa` is the vacancy-posting cost and {math}`J_t` is the value of a filled job to the firm. Match surplus is

```{math}
:label: eq:surplus
S_t = J_t + W_t - U_t,
```

where {math}`W_t` is worker value inside the match and {math}`U_t` is worker value outside the match. Equations {eq}`eq:free-entry` and {eq}`eq:surplus` are the smallest value block that makes the Shimer-Hall debate legible. In the benchmark model, plausible productivity shocks do not move surplus enough to generate the observed volatility of unemployment and vacancies. Shimer's point is that the canonical model under-amplifies aggregate labor volatility because wages and surplus absorb too much of the shock [@shimer2005CyclicalBehavior]. Hall's wage-stickiness logic changes that conclusion by keeping wages from moving one-for-one with productivity, which allows surplus and therefore vacancy creation to respond more sharply [@hall2005EquilibriumWageStickiness].

The labor-economics interpretation matters. This is not primarily a story about inflation. It is a story about how much of an aggregate shock shows up in hiring incentives versus wage adjustment, and therefore about which labor-market margin bears the adjustment.

```{include} assets/tables/10-theory-to-evidence-map.md
```

Table {numref}`tbl:theory-evidence-map` connects these theory objects to the evidence we actually observe. The useful habit is to ask which empirical margin corresponds to the theory object and which important equilibrium object remains latent.

### Unemployment stocks versus flows: ins, outs, and what is observed

The stock-flow decomposition literature is valuable because it stops us from treating unemployment as if it moved through one channel. Equation {eq}`eq:u-law-motion` implies that

```{math}
:label: eq:du-decomp
\Delta u_t \approx (1-u_t)\Delta s_t - u_t \Delta f_t,
```

so cyclical unemployment can be decomposed into an inflow contribution and an outflow contribution around the observed stock. Elsby, Michaels, and Solon show that the relative importance of inflows and outflows changes across recession episodes and horizons. Mild downturns may look mostly like a collapse in job finding; severe downturns often involve both weaker outflows and elevated inflows [@elsbyMichaelsSolon2009InsOuts].

What is observed in a CPS-style stock-flow decomposition is the transition count or hazard between measured labor-force states. What is inferred is the contribution of those hazards to stock dynamics under a transition-accounting framework. The hidden margin is everything the basic state system does not see directly: recall expectations, misclassification, direct E-to-E mobility, vacancy-side recruiting intensity, and the quality of reemployment matches. That is why national time-series decompositions are indispensable but incomplete.

### Separations, endogenous separation, and recessionary unemployment

Week 10 should not treat separation as an exogenous constant. In an endogenous-separation environment, jobs end when match surplus falls below zero for sufficiently weak match quality {math}`z`:

```{math}
:label: eq:endogenous-separation
s_t = \Pr\!\left(S_t(z) < 0\right).
```

Equivalently,

```{math}
:label: eq:separation-integral
s_t = \int \mathbf{1}\{S_t(z) < 0\}\, dG_t(z).
```

These expressions convert separation from a nuisance parameter into a labor-market margin that responds to cyclical conditions, heterogeneity, and dispersion in match productivity. Mortensen and Pissarides provide the canonical job-creation and job-destruction framework [@mortensenPissarides1994JobCreation]. Fujita and Ramey show why recession dynamics are often misread if we impose exogenous separations too quickly [@fujitaRamey2012EndogenousSeparation]. Mueller then sharpens the point by linking separation and cyclical unemployment to sorting across workers and jobs rather than only a representative match [@mueller2017SeparationsSorting].

```{figure} assets/figures/10-separations-jobfinding-unemployment.png
:name: fig-lii-w10-separations
Unemployment dynamics combine inflows, outflows, and endogenous separation. Recessions can raise unemployment because more matches break, because fewer new matches form, or because both forces interact with heterogeneity and recall behavior.
```

Figure {numref}`fig-lii-w10-separations` places inflows and outflows on the same visual footing. This is especially important because discussions that overemphasize job finding often understate layoffs, recalls, and the composition of job loss.

Churning is also useful here because not all cyclical worker reallocation appears as net job loss. A compact accounting object is

```{math}
:label: eq:churning
\text{Churning}_t = \text{Worker Reallocation}_t - \text{Job Reallocation}_t.
```

Equation {eq}`eq:churning` distinguishes net employment adjustment from replacement hiring and within-firm turnover. In downturns, lower churning may signal weaker replacement hiring and less reallocation even before unemployment peaks. That is one reason aggregate adjustment is not exhausted by the unemployment stock.

### Job-to-job transitions, on-the-job search, and cyclical job ladders

Aggregate labor adjustment also runs through employed search and direct job-to-job mobility. A reduced-form on-the-job-search object is

```{math}
:label: eq:ee-flow
EE_t = \lambda_t^{e}\Pr\!\left(w' > w\right),
```

where {math}`\lambda_t^{e}` is the employed offer-arrival rate and the acceptance term captures the chance of receiving a preferable alternative. This makes the core point transparent: the cycle affects wages and mobility not only because unemployed workers find jobs more or less often, but also because employed workers climb job ladders more or less often.

Karahan, Michaels, Pugsley, Şahin, and Schuh show that job-to-job transitions are a first-order source of cyclical wage fluctuations [@karahanMichaelsPugsleySahinSchuh2017JobToJob]. Haltiwanger, Hyatt, Kahn, and McEntarfer show that cyclicality in job ladders is organized by firm wage and firm size, which means recessionary adjustment changes who upgrades and which firms receive movers [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders]. The key labor distinction is between aggregate unemployment dynamics and cross-sectional reallocation. Some downturns chiefly destroy hiring and mobility toward better firms; others raise unemployment sharply. Both are labor-market adjustments, but they are not the same object.

```{figure} assets/figures/10-job-to-job-wage-cyclicality.png
:name: fig-lii-w10-j2j
On-the-job search and direct job-to-job mobility connect the business cycle to wage growth and job ladders. A weak labor market compresses outside offers, slows upgrading, and changes who remains in incumbent jobs.
```

Figure {numref}`fig-lii-w10-j2j` is the bridge from flows to wages. A collapse in {math}`EE_t` can flatten wage growth even before an equivalent movement appears in measured unemployment.

### Wages, sorting, and match quality over the cycle

Observed wage cyclicality is hard to interpret because the mean wage mixes incumbent workers, movers, selection into continued employment, and sorting into different firms. A simple decomposition is

```{math}
:label: eq:wage-cyclicality
\Delta \log \bar w_t = \beta^{I} \, cyc_t + \omega_t^{EE}\beta^{EE} \, cyc_t + comp_t + sort_t,
```

where {math}`\beta^{I}` captures incumbent wage cyclicality, {math}`\beta^{EE}` captures the wage-growth contribution of job changers and job ladders, and {math}`comp_t` and {math}`sort_t` capture composition and sorting terms. Equation {eq}`eq:wage-cyclicality` should change how students hear the phrase “wages are weakly cyclical.” That claim may describe true wage rigidity for incumbents, but it may also reflect the collapse of mover wages, the loss of low-wage jobs, or improved average match quality among those who remain employed.

Figueiredo is the key anchor because it shows that measured wage cyclicality is deeply intertwined with labor-market sorting [@figueiredo2022WageCyclicality]. Job-ladder evidence reinforces the same lesson: when upward mobility freezes, the observed average wage path need not reveal the true cyclicality of offers or outside options [@karahanMichaelsPugsleySahinSchuh2017JobToJob; @haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders].

```{figure} assets/figures/10-match-quality-and-reallocation.png
:name: fig-lii-w10-match-quality
Measured wage cyclicality mixes incumbent wage adjustment, mover wage gains, and changing composition of surviving matches. Cyclical reallocation can make average wages look rigid even when offer distributions and match quality move sharply.
```

Figure {numref}`fig-lii-w10-match-quality` keeps the match-quality and sorting channel explicit. It is the easiest way to show why wage evidence and unemployment evidence need not point to the same margin.

### Measurement, identification, and open questions

The right empirical habit in Week 10 is to map each design to its observed and hidden margins.

```{include} assets/tables/10-measurement-and-identification-map.md
```

Table {numref}`tbl:measurement-identification-map` should be read as a design checklist.

National time-series matching and Beveridge-curve evidence uses aggregate monthly or quarterly data. The identifying variation is cyclical movement over time. The unit of observation is the aggregate market-time cell. The observed margins are unemployment, vacancies, hires, and sometimes stock-flow hazards. The hidden margin is the composition of workers and vacancies and the segmentation of search across groups [@barnichonFigura2015AggregateMatching; @elsbyMichaelsRatner2015Beveridge].

State and local cyclical designs use differential regional exposure to recessions or demand shifts. The identifying variation is cross-area business-cycle intensity or demand exposure. The unit is the state-year, metro-quarter, or region-time cell. The observed margins may include unemployment, vacancies, wages, or job-to-job mobility. The hidden margin is whether local variation identifies an aggregate equilibrium mechanism or only local relative adjustment.

Matched employer-employee evidence uses worker-firm spells or transitions. The identifying variation comes from cyclical movement across workers, firms, or matched panels. The observed margins are E-to-E moves, wage ladders, separations, and sometimes firm premiums. The hidden margin is the full opportunity set facing the worker and the general-equilibrium vacancy response [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders; @figueiredo2022WageCyclicality].

The measurement lesson is simple. National time-series evidence is closest to the macro labor object but weak on composition and mechanism. Local variation is often stronger on quasi-experimental design but may miss economy-wide equilibrium. Matched flow evidence is rich on mobility and wage ladders but typically less public and harder to reproduce pedagogically. The research frontier lies in combining these perspectives rather than forcing one design to answer every question [@barlevyFabermanHobijnSahin2024BeveridgeShifts].

### Bridge to Week 11

Week 10 studied cyclical labor-market adjustment: how shocks move unemployment, vacancies, separations, job-to-job mobility, wages, and match quality over the business cycle. Week 11 keeps those margins in view but changes the shock. The transition is from cyclical adjustment to structural adjustment under technology, automation, AI, and labor-demand restructuring. The same labor-market objects remain central; what changes is the persistence and source of the shock.

## Research Lab

The Week 10 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure and is intentionally bounded. The primary anchor is `@barnichonFigura2015AggregateMatching`, where the measured object is an aggregate matching residual rather than an individual worker outcome. The challenge anchor is `@elsbyMichaelsSolon2009InsOuts`, where the central task is to decompose unemployment into inflows and outflows. The optional extension anchor is `@karahanMichaelsPugsleySahinSchuh2017JobToJob`, where the margin of interest is job-to-job mobility rather than unemployment itself. The local handout lives at [labs/10-aggregate-fluctuations-and-labor-market-adjustment/lab.md](labs/10-aggregate-fluctuations-and-labor-market-adjustment/lab.md).

The key research habit is to force the object into the open before discussing results.

1. What aggregate labor-market object is being measured?
2. Is the design about stocks, flows, efficiency, wages, or job ladders?
3. Which margin is observed directly, and which one is inferred?
4. What cyclical comparison is being made?
5. Which hidden margin is offstage?

### Optional extension block

One extension pushes on Beveridge-curve shifts after 2020. The right question is not whether the Beveridge curve moved, but why: tighter hiring standards, vacancy composition, sectoral reallocation, search intensity, or segmentation [@barlevyFabermanHobijnSahin2024BeveridgeShifts].

A second extension pushes on job ladders and match quality. The relevant question is whether a weak labor market primarily raises unemployment or instead flattens upward mobility, lowers outside offers, and changes the wage ladder even for those who remain employed [@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders; @figueiredo2022WageCyclicality].

## Methods Box

Week 10 only works if the distinctions stay sharp.

1. Unemployment is a stock; job finding, separation, job-to-job mobility, and participation transitions are hazards.
2. Job finding, separation, job-to-job transitions, and participation margins are distinct empirical objects and should not be collapsed into a generic notion of “labor-market churn.”
3. Matching-efficiency residuals are not automatically structural efficiency; heterogeneity, search intensity, vacancy composition, and segmentation can move the same residual.
4. Cross-sectional reallocation across firms is not the same thing as aggregate unemployment dynamics.
5. Wage cyclicality for incumbents is not the same object as wage cyclicality for movers.
6. Measured wage cyclicality is not the same thing as pure wage rigidity once sorting and composition change over the cycle.
7. National time-series identification, local cyclical variation, and matched employer-employee evidence see different margins and should be treated as complements.
8. Every empirical claim should name the identifying variation, unit of observation, observed margin, and hidden margin left offstage.

## Reading ladder

### Ladder A. Canonical framework and the volatility puzzle

- `@rogersonShimerWright2005Survey` for a compact field-course survey of labor-market search models.
- `@shimer2005CyclicalBehavior` for the vacancy-unemployment volatility puzzle in the benchmark model.
- `@hall2005EquilibriumWageStickiness` for wage-stickiness amplification through surplus and vacancy creation.

### Ladder B. Flow accounting and Beveridge-curve interpretation

- `@elsbyMichaelsSolon2009InsOuts` for unemployment as an inflow-outflow object.
- `@elsbyMichaelsRatner2015Beveridge` for the Beveridge curve as a labor-market organizing device.
- `@barnichonFigura2015AggregateMatching` for heterogeneity inside aggregate matching residuals.

### Ladder C. Separations, reallocation, and job ladders

- `@mortensenPissarides1994JobCreation` for endogenous job creation and destruction.
- `@fujitaRamey2012EndogenousSeparation` for recession dynamics with endogenous separation.
- `@mueller2017SeparationsSorting` for separation, sorting, and cyclical unemployment.
- `@haltiwangerHyattKahnMcEntarfer2018CyclicalJobLadders` for cyclical job ladders and E-to-E upgrading.

### Ladder D. Wages, job-to-job transitions, and composition

- `@karahanMichaelsPugsleySahinSchuh2017JobToJob` for job-to-job transitions as a cyclical wage margin.
- `@figueiredo2022WageCyclicality` for wage cyclicality under labor-market sorting.
- `@barlevyFabermanHobijnSahin2024BeveridgeShifts` for recent evidence on why Beveridge-curve shifts differ across eras.

## Exercises / discussion prompts

1. Use Equations {eq}`eq:u-law-motion` and {eq}`eq:u-steady-state` to explain how two economies can have the same unemployment rate with different underlying labor-market risks.
2. Use Equations {eq}`eq:matching` through {eq}`eq:vacancy-filling` to explain why tightness raises the worker-side hazard but lowers the vacancy-side hazard.
3. Why is Equation {eq}`eq:matching-efficiency` not enough to identify a structural matching technology?
4. Compare the objects in Equations {eq}`eq:endogenous-separation` and {eq}`eq:ee-flow`. Which one governs job destruction risk and which one governs job-ladder mobility?
5. Use Equation {eq}`eq:wage-cyclicality` to explain how average wage growth can look weakly cyclical even when outside offers are highly cyclical.
6. Pick one paper from the reading ladder and name its identifying variation, unit of observation, observed margin, and most important hidden margin.

## Reproducibility or code lab note

The bounded Week 10 lab is fully local and synthetic. Students first reproduce a Barnichon-Figura-style aggregate matching exercise, then diagnose how much of a Beveridge-style movement is in observed stocks and how much is bundled into an inferred residual, and finally transfer the same reasoning to an Elsby-Michaels-Solon-style stock-flow decomposition and a small synthetic job-to-job cyclicality exercise anchored to `@karahanMichaelsPugsleySahinSchuh2017JobToJob`. The point is to make stocks, flows, efficiency residuals, and job ladders explicit without requiring confidential microdata.

## Slide companion note

The Week 10 slide deck lives at [slides/week10/10-aggregate-fluctuations-and-labor-market-adjustment.tex](slides/week10/10-aggregate-fluctuations-and-labor-market-adjustment.tex). It is slightly longer than a standard week because this is one of the heavier Labor II lectures, but it stays tightly organized around stocks and hazards, matching and the Beveridge curve, surplus and vacancy creation, separations, job ladders, wage cyclicality, empirical design, and the bridge to Week 11.
