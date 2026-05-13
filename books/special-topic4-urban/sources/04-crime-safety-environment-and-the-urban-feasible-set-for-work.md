---
title: Crime, Safety, Environment, and the Urban Feasible Set for Work
bibliography:
  - references.bib
---

# Week 4. Crime, Safety, Environment, and the Urban Feasible Set for Work

**Central question:** How do safety and environmental conditions change which jobs workers can take and how much work is worth?

This week treats crime, harassment, public safety, commuting risk, pollution, heat, noise, and environmental amenities as labor-market constraints rather than as background urban conditions. It also turns the problem around: when legal employment opportunities deteriorate, crime, informal activity, and risky survival strategies may become more attractive. The goal is to give students a genuinely two-sided framework for urban risk and labor-market behavior, not a one-sided “amenities” lecture.

**Why this is specifically labor economics:** Safety and environmental quality change the feasible set for work, the disutility of commuting and job tasks, worker productivity, reservation values, search radius, and the welfare value of wages. Labor-market opportunity also shapes the opportunity cost of crime, informal activity, and other risky outside options.

:::{admonition} Core points
:class: important
- Urban risk enters labor markets through feasibility, productivity, and welfare, not only through observed wages.
- Crime, harassment, pollution, heat, and noise change job search radius, hours, productivity, absenteeism, retention, and sorting.
- The relationship also runs the other direction: weak labor demand, job loss, and poor outside options can raise criminal activity or other risky alternatives.
- A good empirical design must separate exposure, selection, local equilibrium adjustment, and hidden harms that are not fully priced into wages.
:::

## Bridge

Week 1 introduced the city as a joint system of wages, commuting, amenities, rents, and outside options. Week 2 added housing and moving costs, and Week 3 showed that unequal neighborhoods create unequal access to jobs and networks. This week adds **risk**. In urban labor markets, workers do not just choose among jobs and places with different pay and commute times; they choose among jobs and places with different levels of safety, harassment, pollution, heat, and stress. The resulting labor-market margins are therefore about both **access** and **welfare**.

The key conceptual move is to analyze two margins together. First, risk and environmental exposure can shrink the feasible set of jobs, commute times, and work schedules available to workers. Second, labor-market opportunities themselves affect the opportunity cost of criminal activity and the incidence of unsafe or exploitative work. That makes this week naturally two-sided and equilibrium-oriented.

## Field Core

### 1. A two-sided framework: urban risk as a labor-market wedge and labor opportunities as a determinant of crime

Let worker utility from a job-place pair be increasing in wages and amenities, but decreasing in commuting burden and exposure to risk. In an urban setting, the relevant object is not just the nominal wage {math}`w`, but something closer to a real, risk-adjusted value of work:

```{math}
:label: eq:risk_adjusted_work
V_{ij\ell} = w_{ij\ell} - c(d_{i\ell}) - r_{i\ell} - e_{i\ell} + a_{\ell},
```

where {math}`d_{i\ell}` is the relevant commute or travel burden for worker {math}`i` to location {math}`\ell`, {math}`r_{i\ell}` is safety or harassment risk, {math}`e_{i\ell}` is environmental exposure, and {math}`a_{\ell}` is the amenity value of location {math}`\ell`. This is a deliberately reduced-form way to encode the idea that workers choose among *risk-adjusted* jobs, not jobs on a placeless menu.

The two-sided perspective adds a second margin: if legal employment opportunities fall, the return to criminal or risky alternatives can rise. A simple reduced-form object is

```{math}
:label: eq:crime_opportunity_cost
C_{\ell t} = \alpha - \beta \, O_{\ell t} + \gamma \, Z_{\ell t} + u_{\ell t},
```

where {math}`C_{\ell t}` is local criminal activity, {math}`O_{\ell t}` is the value of legal labor-market opportunity, and {math}`Z_{\ell t}` captures other local conditions. The substantive lesson is not that all crime is “labor supply to crime,” but that labor opportunities and urban risk interact in equilibrium.

### 2. Crime, safety, and workplace risk as constraints on the feasible set

Urban crime and public safety change labor behavior through several distinct margins:
- search radius and willingness to commute at certain times,
- willingness to accept jobs in high-risk sectors or neighborhoods,
- absenteeism and schedule choice,
- workplace exits and occupational sorting,
- compensating differentials and unpriced welfare losses.

A classic labor-market perspective on crime emphasizes labor opportunities. Gould, Weinberg, and Mustard show that local labor-market opportunities help explain crime variation in the United States [@gouldWeinbergMustard2002]. Freeman’s earlier work made the same point from the perspective of disadvantaged youth and the opportunity cost of criminal activity [@freeman1991]. In newer administrative data, job displacement can raise crime participation through a direct loss of formal opportunities, as in Colombia [@khannaMedinaNyshadhamTamayo2021].

Safety also matters *inside* labor markets. Workplace harassment and violence affect whether workers stay, sort, or accept certain jobs. Sexual harassment can contribute to segregation and inequality by pushing workers away from otherwise high-paying workplaces [@folkeRickne2022]. More broadly, safety affects the welfare value of employment even when wages do not move one-for-one with exposure [@sabiaDillsDeSimone2013].

### 3. Environment, productivity, hours, and the urban work margin

Environmental conditions alter labor outcomes through both extensive and intensive margins. Pollution can reduce labor supply by worsening health and raising the short-run cost of work [@hannaOliva2015]. It can also reduce worker productivity even when workers remain employed [@graffZivinNeidell2012; @changGraffZivinGrossNeidell2019]. Heat and extreme temperatures change time allocation and effective labor supply [@graffZivinNeidell2014], while noise and cognitive burden can reduce task performance even in indoor settings [@dean2024noise].

This literature matters for urban labor because exposure is rarely random across workers or neighborhoods. Low-income or otherwise constrained workers may be more exposed to pollution, heat, or dangerous commutes and less able to substitute away. That creates a wedge between nominal labor-market success and actual welfare.

### 4. Compensating differentials, hidden harms, and why wages can be misleading

In a frictionless world, riskier or more polluted jobs and neighborhoods might simply pay more. But in practice, compensating differentials are incomplete, uneven, or confounded by frictions. Workers may not fully observe risk; they may face limited mobility or liquidity; and exposure may be bundled with local labor-market power or neighborhood segregation. As a result, observed wages can be a poor welfare statistic.

The empirical question is therefore not merely whether risky places pay more. It is whether:
- workers understand the risks,
- they can avoid them,
- firms must compensate them,
- local rents capitalize the benefits of safer places,
- and equilibrium sorting shifts risk toward workers with fewer outside options.

This is where the week links back to Weeks 2 and 3. Housing markets, segregation, and network frictions can all keep workers exposed to local risk even when safer jobs or neighborhoods exist.

### 5. A framework for empirical work

A good research design in this area must begin by stating which object is moving:
- exposure to risk,
- legal labor opportunity,
- commuting feasibility,
- productivity,
- or welfare.

Then it must ask which margins respond:
- employment or participation,
- hours,
- search radius,
- sector/occupation choice,
- absenteeism,
- productivity,
- crime,
- or migration.

Only then can the design choose the right counterfactual. Many modern papers exploit environmental shocks, policy shocks, layoffs, quasi-random exposure, or rich panel data. But the hard part is not just identification; it is making sure the design maps clearly to the relevant labor mechanism.

## Research Lab

A natural replication anchor for this week is the labor-opportunity-to-crime design in [@gouldWeinbergMustard2002] or the displacement-to-crime design in [@khannaMedinaNyshadhamTamayo2021]. A natural environmental anchor is [@hannaOliva2015] or [@graffZivinNeidell2012]. Students should be encouraged to ask:
- which margin is measured directly and which is inferred,
- whether wages are capturing welfare,
- whether exposure is endogenous,
- and whether worker sorting or local equilibrium adjustment is doing part of the work.

A bounded extension could take one empirical design and ask whether the same framework works for:
- crime vs pollution,
- participation vs productivity,
- or local opportunity vs commute risk.

## Reading ladder

Core framing:
- [@gouldWeinbergMustard2002]
- [@khannaMedinaNyshadhamTamayo2021]
- [@hannaOliva2015]
- [@graffZivinNeidell2012]

Additional high-value papers:
- [@freeman1991]
- [@folkeRickne2022]
- [@sabiaDillsDeSimone2013]
- [@graffZivinNeidell2014]
- [@changGraffZivinGrossNeidell2019]
- [@dean2024noise]
- [@kirchmaierMastrobuoniVilla2024]
