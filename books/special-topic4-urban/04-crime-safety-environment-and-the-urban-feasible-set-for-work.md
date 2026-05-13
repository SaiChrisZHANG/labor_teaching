# Crime, Safety, Environment, And The Urban Feasible Set For Work

## Learning Objectives

By the end of Week 4, students should be able to:

1. explain how crime, safety, harassment, pollution, heat, and noise change the feasible set for work;
2. analyze the two-sided relationship between urban risk and labor-market opportunity;
3. distinguish public-space risk, commuting risk, workplace risk, and environmental exposure as separate labor-market mechanisms;
4. evaluate empirical designs that use layoffs, local labor-demand shocks, environmental shocks, policy changes, and high-frequency exposure variation;
5. explain why nominal wages can be a poor welfare statistic when risk and exposure differ across workers and places;
6. design a bounded research exercise that separates exposure, opportunity, sorting, and welfare interpretation.

## Opening Orientation

Week 4 asks a labor question: how do safety and environmental conditions change which jobs workers can take and how much work is worth?

The week is not a general lecture on crime or environmental economics. Crime, harassment, public safety, pollution, heat, noise, and environmental amenities enter because they change job search, commuting, schedules, productivity, absenteeism, retention, sorting, and worker welfare. They also matter because the relationship runs in the other direction: weak labor demand, job loss, and low earnings prospects can change the opportunity cost of crime, informal activity, and other risky outside options.

The organizing idea is therefore two-sided. Urban risk can shrink the feasible set for work. Labor-market opportunity can shape risky activity. A complete urban-labor account must keep both sides visible.

:::{admonition} Core points
:class: important

- Urban risk enters labor markets through feasibility, productivity, and welfare, not only through observed wages.
- Crime, harassment, pollution, heat, and noise change job search radius, hours, productivity, absenteeism, retention, and sorting.
- The relationship also runs from labor markets to risk: weak demand, job loss, and poor outside options can raise crime, informal work, or risky survival strategies.
- Workplace safety and public-space safety are labor-market objects when they change job acceptance, retention, commuting, and occupational choice.
- Wages alone can be a poor welfare statistic when exposure is unequal, hidden, unpriced, or shifted toward workers with weak outside options.

:::

## Bridge

Week 1 defined the city as a linked system of jobs, residences, commuting costs, rents, amenities, risks, and outside options. Week 2 added housing and moving costs as constraints on labor-market adjustment. Week 3 showed that unequal neighborhoods create unequal access to jobs, networks, schools, and long-run opportunity. Week 4 takes one mechanism from that access framework -- local risk -- and studies it directly.

The new object is not just a job with wage {math}`w`. It is a job-place-time bundle with a wage, a commute, a schedule, an exposure profile, a safety profile, and an outside option. A night shift may be feasible for one worker and infeasible for another because the commute is unsafe. A high-paying job may be unattractive if harassment risk is high or pollution lowers health and productivity. A neighborhood with many reachable jobs may still provide weak opportunity if the safest commute windows do not match work schedules.

The labor discipline is to identify the margin. Does risk change employment, hours, search radius, accepted wages, productivity, absenteeism, retention, occupational sorting, crime, or migration? Does the empirical design move safety and exposure, or does it move legal labor opportunity? Does the result identify a welfare loss, a productivity effect, a compensating differential, or an equilibrium resorting pattern?

## Field Core

### Block A. A Two-Sided Urban Risk Framework

Start with a worker evaluating a job {math}`j`, residence {math}`r`, and workplace or activity location {math}`\ell`. A compact risk-adjusted value of work is:

```{math}
:label: eq:risk-adjusted-work-week4
V_{ijr\ell t}
=
w_{j\ell t}
- R_{rt}
- \tau_{ijr\ell t}
- \rho^{S}_{ijr\ell t}
- \rho^{E}_{ijr\ell t}
+ A_{rt}
+ \varepsilon_{ijr\ell t}.
```

The wage is only one term. {math}`R_{rt}` is housing cost, {math}`\tau_{ijr\ell t}` is generalized commuting and schedule cost, {math}`\rho^{S}_{ijr\ell t}` is safety, harassment, or violence risk, {math}`\rho^{E}_{ijr\ell t}` is environmental exposure, and {math}`A_{rt}` is local amenity value. Risk enters through multiple channels: direct disutility, stress, time constraints, health, productivity, and expected future costs.

The second side of the framework asks how legal labor opportunity affects crime or risky activity. Let {math}`O_{i\ell t}` be the value of legal opportunity, including expected formal earnings, job-finding probability, schedule feasibility, and credit or liquidity relief. A reduced-form participation index for criminal or risky activity is:

```{math}
:label: eq:crime-opportunity-cost-week4
\Pr(C_{i\ell t}=1)
=
F\left(
B_{i\ell t}
- p_{\ell t} F_i
- O_{i\ell t}
+ \eta_{i\ell t}
\right),
```

where {math}`B_{i\ell t}` is the private return or pressure from risky activity, {math}`p_{\ell t}F_i` is expected punishment or cost, and {math}`O_{i\ell t}` is the opportunity cost from legal work. The point is not to reduce crime to a simple labor-supply model. The point is to make opportunity costs, credit stress, local demand, and risky outside options part of the same urban-labor equilibrium.

```{include} assets/tables/04-two-sided-equilibrium-map.md
```

This two-sided framework prevents two mistakes. The first is treating crime and environmental quality as background amenities that only enter hedonic wage equations. The second is treating crime as disconnected from labor-market conditions. Urban risk and labor opportunity are jointly determined through workers, firms, households, local institutions, housing markets, commuting systems, and enforcement.

### Block B. Crime, Safety, And Workplace Risk As Labor-Market Constraints

Safety changes work before wages are observed. It can change whether a worker searches in a neighborhood, accepts a shift, uses a transit route, stays in an occupation, or exits a workplace. The same nominal job offer can have different value for workers facing different commuting risks, harassment risk, childcare pickup windows, or public-space exposure.

```{include} assets/tables/04-risk-and-feasible-set-map.md
```

The labor-opportunity side of the crime literature gives the first half of the research spine. Gould, Weinberg, and Mustard connect local labor-market opportunities to crime rates in the United States [@gouldWeinbergMustard2002]. Freeman frames crime among disadvantaged youth partly through the changing returns to legitimate work and risky alternatives [@freeman1991]. Khanna, Medina, Nyshadham, and Tamayo provide a modern matched-data design in which job loss, credit stress, and crime are connected after displacement [@khannaMedinaNyshadhamTamayo2021].

The risk-to-labor side is equally important. Crime and public safety change the timing of work and travel [@hamermesh1999CrimeTimingWork]. Street harassment and perceived risk can constrain educational and mobility choices that later affect labor-market opportunity [@borker2021SafetyFirst]. Crime is spatial and mobile, which means commuting systems, neighborhood exposure, and offender travel can affect who bears risk and when [@kirchmaierMastrobuoniVilla2024].

Workplace safety belongs in the same module. Harassment and violence are not just unpleasant job attributes; they can change retention, occupational sorting, promotion, and gender or racial inequality. Folke and Rickne show how sexual harassment can shape gender inequality in the labor market [@folkeRickne2022]. Sabia, Dills, and DeSimone connect sexual violence to labor-market outcomes, underscoring that safety can affect employment and earnings even when it is not priced cleanly into wages [@sabiaDillsDeSimone2013].

The mechanism discipline is to avoid bundling all safety effects together. Public-space risk may operate through commute routes and shift timing. Workplace harassment may operate through quits, internal mobility, or occupational sorting. Neighborhood crime may operate through search radius, stress, or firm location. Each mechanism implies a different counterfactual.

### Block C. Environment, Productivity, Hours, And The Urban Work Margin

Environmental exposure changes labor outcomes through health, cognition, fatigue, schedule choice, absenteeism, and productivity. Pollution can reduce labor supply by worsening health or raising the short-run cost of work, as in Hanna and Oliva's Mexico City natural experiment [@hannaOliva2015]. Pollution can also reduce output while workers remain on the job, which Graff Zivin and Neidell show using worker productivity data [@graffZivinNeidell2012]. Chang, Graff Zivin, Gross, and Neidell extend this logic to call-center workers, where cognitive and indoor productivity margins are central [@changGraffZivinGrossNeidell2019].

Heat adds another labor margin. Extreme temperatures affect time allocation, hours, and the productivity of work, especially when adaptation is costly or incomplete [@graffZivinNeidell2014]. Noise belongs here as well because it can impair cognition and task performance even in settings that look sheltered from outdoor exposure [@dean2024noise].

The urban-labor issue is unequal exposure. Workers differ in residence, commute mode, workplace ventilation, task flexibility, bargaining power, and ability to move or work remotely. A professional worker may avoid a heat or pollution shock through indoor work, schedule flexibility, or relocation. A delivery worker, warehouse worker, home health aide, construction worker, or transit-dependent service worker may have much less ability to substitute away. The same environmental shock can therefore widen labor-market inequality even if average employment changes little.

The right empirical question is not simply "does pollution matter?" It is: which labor margin changes, for whom, under what adaptation possibilities, and with what welfare interpretation?

### Block D. Compensating Differentials, Hidden Harms, And Welfare

In a frictionless compensating-differentials story, risky or polluted jobs and places pay more, and safer or cleaner places pay less or cost more in rent. That logic is useful, but it is not enough for this week.

Compensation can be incomplete for several reasons. Workers may not observe the full risk. Risk may be bundled with limited job access, low wealth, weak bargaining power, or residential segregation. Some harms occur through stress, fear, schedule restrictions, family constraints, or cumulative health costs that are not visible in wages. Firms may respond by changing staffing, surveillance, technology, or location. Landlords may capture safety improvements through rents. Workers with few outside options may remain exposed without receiving full compensation.

This is why nominal wages can be a poor welfare statistic. A worker with a higher wage but an unsafe commute, high harassment risk, and heavy pollution exposure may have lower welfare than a lower-wage worker with safer, cleaner, more flexible access. A wage regression that controls for place can also control away the very exposure that makes the place relevant.

```{include} assets/tables/04-welfare-and-hidden-harms-map.md
```

The practical welfare object is therefore closer to Equation {eq}`eq:risk-adjusted-work-week4` than to wages alone. A credible empirical interpretation should state whether observed wages are treated as compensation, as an outcome affected by risk, or as an incomplete proxy for welfare.

### Block E. Empirical Designs And Data

Good designs in this area begin by naming the moving object. Is the design moving legal labor opportunity, safety, environmental exposure, workplace risk, commute feasibility, or local amenity value? Then it names the margin: employment, hours, productivity, search radius, schedule choice, retention, crime, migration, rents, or wages.

```{include} assets/tables/04-data-and-methods-map.md
```

Five design families recur.

**Labor-opportunity shocks.** Layoffs, plant closures, industry shocks, or local demand shifts can identify how weak legal opportunity affects crime or risky activity. The threat is that job loss also moves income, credit, networks, mental health, and family constraints, so mechanism claims need care [@khannaMedinaNyshadhamTamayo2021].

**Environmental shocks.** Pollution changes from plant closures, inversions, wind, regulation, or weather can identify labor supply and productivity effects. The threat is endogenous sorting, adaptation, avoidance behavior, and unmeasured local shocks [@hannaOliva2015; @graffZivinNeidell2012].

**High-frequency productivity designs.** Worker-day or task-level data can compare the same worker under different exposure conditions. The advantage is tight measurement of productivity. The threat is selection into tasks, shifts, or days worked [@changGraffZivinGrossNeidell2019; @dean2024noise].

**Safety and commuting designs.** Transit changes, policing changes, lighting changes, public-space interventions, or route-level crime shocks can reveal schedule and search-radius effects. The threat is that safety, travel time, neighborhood composition, and local demand may move together.

**Workplace risk designs.** Surveys, complaints, HR records, administrative data, and linked payroll panels can study harassment, violence, and retention. The threat is reporting behavior: measured complaints are not the same as true exposure.

Across all designs, the researcher must confront selection and equilibrium. Workers sort away from risk when they can. Firms may relocate, change wages, or adjust tasks. Rents may capitalize safety or environmental improvements. Reduced-form estimates can therefore already include worker and firm responses.

## Research Lab

The Week 4 lab is a bounded synthetic exercise anchored on the displacement-to-crime design in Khanna, Medina, Nyshadham, and Tamayo [@khannaMedinaNyshadhamTamayo2021]. It does not reproduce their confidential administrative data or official estimates. Instead, it trains the design logic: use an event-study-style comparison around job loss to ask how formal labor opportunity, credit stress, and risky activity move together.

The lab follows the course workflow: **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** Students run a deterministic synthetic worker panel with displaced and comparison workers observed before and after a layoff. The script computes formal earnings, a legal-opportunity index, credit stress, and a crime-risk index by event time. The goal is to interpret the event-study object, not to claim an official replication.

**Diagnose.** Students classify mechanism claims into risk-to-labor, labor-to-crime, exposure sorting, welfare interpretation, and equilibrium adjustment. Each row asks for the labor object, counterfactual, data need, and main threat.

**Transfer.** Students apply the same logic to an environmental-productivity setting. A synthetic worker-day file changes heat, pollution, and noise exposure while holding worker identity fixed. The transfer exercise asks whether the outcome is hours, productivity, health, or welfare, and why wages alone miss the hidden harm.

A bounded extension is to add a commute-safety shock: hold the wage fixed, change route risk for late shifts, and compute whether the feasible job set changes even when employment does not. The extension should remain a design memo unless students can identify a credible source of local safety variation.

## Methods Box

:::{admonition} Methods Box: Exposure, Opportunity, And Welfare Objects
:class: note

The practical skill this week is to separate four objects that are often collapsed.

**Exposure.** What risk does the worker actually face? Measure residence, workplace, route, schedule, and task exposure separately when possible.

**Opportunity.** What is the value of the legal labor-market alternative? Wages, job-finding probabilities, hours, credit access, and commute feasibility can all enter.

**Response margin.** What moves: employment, hours, productivity, absenteeism, search radius, retention, crime, or migration?

**Welfare.** Does the outcome capture worker well-being, or only observed earnings? Hidden harms can persist even when wages and employment are unchanged.

The best empirical designs make Equation {eq}`eq:risk-adjusted-work-week4` operational: they measure the wage and at least one nonwage risk component, then explain whether the estimated effect is a productivity effect, labor-supply effect, opportunity-cost effect, or welfare effect.

:::

## Reading Ladder And References

**Two-sided crime and labor opportunity.** Start with Gould, Weinberg, and Mustard for local labor-market opportunity and crime, Freeman for disadvantaged youths and the opportunity cost of crime, and Khanna, Medina, Nyshadham, and Tamayo for a modern displacement, credit, and crime design [@gouldWeinbergMustard2002; @freeman1991; @khannaMedinaNyshadhamTamayo2021].

**Safety as a labor constraint.** Use Hamermesh on crime and the timing of work, Borker on street harassment and educational choices, Folke and Rickne on workplace harassment and gender inequality, and Sabia, Dills, and DeSimone on sexual violence and labor outcomes [@hamermesh1999CrimeTimingWork; @borker2021SafetyFirst; @folkeRickne2022; @sabiaDillsDeSimone2013].

**Pollution, heat, noise, and productivity.** Use Hanna and Oliva for pollution and labor supply, Graff Zivin and Neidell for pollution and worker productivity, Chang and coauthors for call-center productivity, Graff Zivin and Neidell for temperature and time allocation, and Dean for noise and productivity [@hannaOliva2015; @graffZivinNeidell2012; @changGraffZivinGrossNeidell2019; @graffZivinNeidell2014; @dean2024noise].

**Spatial risk and equilibrium.** Use Kirchmaier, Mastrobuoni, and Villa to think about the spatial movement of crime and why commuting, routes, and local exposure matter for urban risk [@kirchmaierMastrobuoniVilla2024].

## Exercises And Discussion Prompts

1. Rewrite Equation {eq}`eq:risk-adjusted-work-week4` for a worker choosing between a higher-wage night-shift job and a lower-wage day-shift job. Which terms determine whether the night shift is actually feasible?
2. A plant closure reduces pollution and also changes local employment. What data and design would you need to separate a labor-supply effect from a local-demand effect?
3. A layoff raises arrests in a matched administrative panel. Name three mechanisms besides the simple opportunity cost of time that could explain the result.
4. Choose one row from the risk feasible-set table. What is the labor-market object, the counterfactual, and the most credible design family?
5. Two neighborhoods have the same average wage, but one has higher commute risk and heat exposure. What additional outcomes would you need before making a welfare comparison?
6. Design a commute-safety intervention study. Which outcomes would show a change in feasible work even if employment stays constant?

## Reproducibility And Code Lab Note

The Week 4 code lab lives at `labs/04-crime-safety-environment-and-the-urban-feasible-set-for-work/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates a deterministic event-study-style displacement panel, diagnoses risk and opportunity mechanisms, transfers the framework to environmental productivity, and computes a risk-adjusted job ranking. It runs without confidential microdata or external downloads.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-crime-safety-environment-and-the-urban-feasible-set-for-work.tex`. The deck is a compact research-design map. It defines the two-sided equilibrium framework, separates safety, workplace risk, pollution, heat, and noise mechanisms, summarizes empirical designs and data, and closes with the welfare lesson that wages alone can miss hidden harms.

## Bridge Forward

Week 5 shifts from risk and exposure to local reallocation. The Week 4 lesson carries forward directly: after a local shock, wages, employment, crime, safety, environment, rents, commuting, and migration can all adjust. A credible urban-labor interpretation must say which margin moved and whose welfare changed.
