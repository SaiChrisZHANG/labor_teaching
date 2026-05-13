---
title: Week 3 source pack — Spatial Mismatch, Segregation, Neighborhood Effects, and Job Access
bibliography:
  - ../bibliography/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.bib
---

# Week 3. Spatial Mismatch, Segregation, Neighborhood Effects, and Job Access

## Week identity

**Central question:** How do residential segregation and neighborhood exposure shape access to jobs, networks, and long-run labor-market opportunity?

**Why this is specifically labor economics:** Segregation and neighborhoods matter when they change job search, hiring networks, human-capital accumulation, commuting feasibility, earnings, employment, and intergenerational mobility.

## Core design goal

This week should turn the broad idea of “unequal access” into a disciplined labor-research architecture. Students should leave knowing that spatial mismatch, employer discrimination, residential labor-market networks, neighborhood peers, school quality, local institutions, and safety are **different mechanisms**. They can generate similar reduced-form gaps, but they imply different counterfactuals, different empirical designs, and different policy levers.

The lecture is **not** a generic neighborhood-effects week. It is a labor-market week about how space produces unequal job access and unequal long-run labor opportunity.

## What the chapter should do

### Opening orientation
The opening should explain why Week 1 and Week 2 are not enough. Even inside the same city, workers can face sharply different labor-market sets because:
- jobs are not evenly distributed across space,
- commuting technologies differ,
- neighborhoods create or block access to information and referrals,
- employers may use residential cues as information or stigma,
- childhood neighborhood environments affect later labor-market trajectories,
- schools, public goods, and local safety shape human capital and job access.

### Core points box
The required **Core points** box should summarize at least the following:
- unequal labor-market access is produced by multiple mechanisms, not just distance to jobs;
- proximity to jobs is not the same thing as access to jobs;
- neighborhood effects and sorting must be carefully separated;
- good research design in this field isolates one mechanism at a time;
- geography, data, and institutional context determine what can be learned.

## Required section structure

### 1. Bridge
Use this section to move from Week 2’s aggregate access framework to unequal access within cities and across neighborhoods.

Must distinguish:
- aggregate opportunity vs unequal opportunity,
- residence-based disadvantage vs workplace-based disadvantage,
- descriptive segregation vs causal effects of neighborhoods,
- current access effects vs long-run exposure effects.

### 2. Field Core

The Field Core should be organized into **five blocks**.

#### Block A. From aggregate access to unequal access
Explain why a metro area with strong labor demand can still generate unequal labor outcomes across neighborhoods. This block should define:
- spatial mismatch,
- residential segregation,
- neighborhood exposure,
- and local opportunity as distinct but related objects.

#### Block B. Mechanisms of unequal labor-market access
This section should lay out the main mechanism taxonomy:

1. **distance to jobs / commuting friction**
2. **transit access and travel-time inequality**
3. **employer discrimination or address stigma**
4. **residential labor-market networks and referrals**
5. **neighborhood peers and social capital**
6. **schools, public goods, and local institutions**
7. **local safety and neighborhood conditions**

The text should emphasize that each mechanism implies a different research design and policy counterfactual.

#### Block C. Segregation, networks, and job access
This section should develop:
- classic spatial mismatch intuition,
- racial/spatial job segregation,
- neighborhood referral networks,
- and job suburbanization as a labor-market mechanism.

Students should understand why “there are jobs somewhere in the metro area” is not enough.

#### Block D. Neighborhood exposure and long-run labor outcomes
This section should move from current access to longer-run labor-market opportunity. It should cover:
- age-at-move logic,
- cumulative exposure,
- childhood neighborhoods and later earnings/employment,
- and why neighborhood effects can operate through schools, peers, safety, institutions, and expectations.

The lecture should keep the focus on labor outcomes: later earnings, employment, occupational mobility, and intergenerational labor opportunity.

#### Block E. Methodological box: what a good empirical design looks like
This is a required section.

The chapter should include a dedicated methods box or clearly marked methodological subsection covering:

##### Main empirical design families
1. **Mover / age-at-move designs**
2. **Cohort exposure / cumulative exposure designs**
3. **Policy shocks**
   - MTO, public housing demolition, transit expansions, job suburbanization, boundary redrawing, related quasi-experiments
4. **School-attendance or school-admission designs**
5. **Audit / correspondence experiments**
6. **Matched employer-employee / network designs**

##### What a credible design should do
A good empirical design in this field should:
- isolate one mechanism rather than bundling many together,
- define the relevant geography and labor market,
- measure actual access rather than relying on loose proxies,
- distinguish residence, workplace, school, and neighborhood channels,
- address residential sorting,
- discuss equilibrium sorting/displacement where relevant,
- state clearly which labor margin is being identified.

### 3. Research Lab
The Research Lab should show students how to turn spatial inequality into a labor paper.

It should teach them to ask:
- is this a current job-access problem or a long-run exposure problem?
- is the proposed mechanism distance, networks, discrimination, peers, schools, or safety?
- what data would distinguish those channels?
- is the design identifying a neighborhood effect or a sorting effect?
- what spatial scale is actually relevant?

The lab should also train students to map questions to designs:
- job suburbanization -> establishment relocation or local-demand exposure
- neighborhood effects -> mover or exposure-timing design
- employer stigma -> audit/correspondence design
- network access -> matched employer-employee or coworker-neighbor designs
- school/zone effects -> boundary or admission design

## Formal / conceptual requirements

The chapter should include, at minimum:

### Job-access object
```{math}
:label: eq:job-access-week3
A_i = \sum_j v_j \exp\{-\kappa \tau_{ij}\}
```
where `{math}`v_j`` captures local job opportunities and `{math}`\tau_{ij}`` is generalized travel cost.

### Mechanism decomposition
```{math}
:label: eq:mechanism-decomp-week3
Y_i = \beta_A A_i + \beta_N N_i + \beta_P P_i + \beta_S S_i + u_i
```
where `{math}`A_i`` is access, `{math}`N_i`` networks, `{math}`P_i`` neighborhood or peer environment, and `{math}`S_i`` schools or local institutions.

### Exposure timing logic
```{math}
:label: eq:exposure-week3
Y_i = \alpha + \theta \, \text{Exposure}_{ig} + \lambda_g + \varepsilon_i
```
used only as a framing device for why age, timing, and duration of neighborhood exposure matter.

## Must-cover papers

### Mechanisms and mismatch framing
- `[@kainHousingSegregationNegro1968]`
- `[@gobillonSelodZenou2007]`

### Networks and spatial access
- `[@bayerRossTopa2008]`
- `[@hellersteinMcInerneyNeumark2011]`
- `[@hellersteinKutzbachNeumark2014]`
- `[@millerWhenWorkMoves2023]`

### Causal neighborhood exposure
- `[@chettyHendrenKatz2016]`
- `[@chettyHendren2018]`
- `[@chynPublicHousingDemolition2018]`
- `[@bergmanChettyDeLucaEtAl2024]`

### Employer beliefs and stigma
- `[@phillipsDoLowWageEmployers2020]`

### Methods / identification / institutions
- `[@graham2016]`
- `[@blackDoBetterSchools1999]`
- `[@monarrezSchoolAttendance2021]`

## Methods and measurement requirements

The chapter should explicitly distinguish:
- access to jobs vs realized employment,
- neighborhood effects vs residential sorting,
- neighborhood channels vs school channels,
- residence-based vs workplace-based measurement,
- current labor-market access vs childhood exposure,
- descriptive segregation vs causal labor-market barriers.

The required methods box should explain why the following designs are useful:
- mover designs,
- cohort effects,
- policy shocks,
- school admission or school-boundary designs,
- audits,
- matched employer-employee network designs.

It should also discuss common data sources:
- LEHD / LODES / QWI,
- Census / ACS / Decennial Census,
- Opportunity Atlas / tax-linked mobility data,
- school assignment and boundary data,
- transit / GTFS / travel-time matrices,
- audit/correspondence data,
- administrative relocation or housing-program data,
- establishment-level data for suburbanization or relocation.

## Required tables to use

The chapter should use these tables explicitly:
- `../tables/03-mechanisms-map.md`
- `../tables/03-empirical-designs-box.md`
- `../tables/03-good-design-checklist.md`
- `../tables/03-data-and-measurement-map.md`

## Reading ladder logic

Organize the reading ladder as:
1. spatial mismatch foundations,
2. segregation and network mechanisms,
3. causal neighborhood exposure,
4. modern policy-shock and mover designs,
5. measurement and identification challenges.

## Slides requirements

Slides must:
- keep the same repo conventions,
- live only under `books/special-topic4-urban/slides/week3/`,
- use the `research` environment conventions,
- include a visible methods box / design map.

At minimum, the deck should include:
1. central question and why this is labor economics,
2. from aggregate access to unequal access,
3. mechanism taxonomy,
4. spatial mismatch vs networks vs neighborhood effects,
5. job suburbanization and unequal access,
6. mover designs and policy shocks,
7. school-boundary / audit / matched-firm designs,
8. what a good empirical design looks like,
9. bridge to later weeks.

## Lab requirements

Build the week around **Reproduce -> Diagnose -> Transfer**.

Primary lab anchor:
- `[@chettyHendrenKatz2016]`

Secondary / challenge anchor:
- `[@millerWhenWorkMoves2023]`

Optional extension anchor:
- `[@bergmanChettyDeLucaEtAl2024]`

The bounded student path must run locally without confidential microdata.

The lab should train students to distinguish:
- access from employment,
- neighborhood effects from sorting,
- schools from neighborhoods,
- movers designs from policy shocks,
- and mechanism-specific from omnibus neighborhood claims.
