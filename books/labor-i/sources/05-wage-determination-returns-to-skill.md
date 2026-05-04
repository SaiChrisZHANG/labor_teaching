# Week 5 source pack — Wage Determination and Returns to Skill

## Purpose of this file

This is the intellectual control file for Week 5. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do observed wages map worker skill, schooling, experience, amenities, rents, and sorting, and what exactly do empirical designs recover when they estimate a "return to skill" or a "return to education"?

## Week identity

- Course: Labor I
- Week: 5
- Length: 3 hours core, with an optional 45--75 minute extension block on worker--firm decompositions or spatial sorting
- Position in sequence: this is the payoff week after Week 4 human-capital accumulation and before Week 6 households and time allocation
- Goal: connect human-capital investment to wage outcomes, introduce the Mincer benchmark, show where selection and treatment-effect heterogeneity complicate interpretation, and then broaden wage determination to include firm and location sorting rather than worker skill alone

## Why this week matters

Week 5 is the point where the course stops treating wages as a simple reduced-form outcome and starts treating them as objects that embed:
- accumulated productive capacity,
- prices of skill,
- compensating differentials,
- worker selection into schooling and occupations,
- sorting across firms and places,
- and sometimes rents.

Students should leave this week understanding that a wage regression coefficient is never self-interpreting. The chapter should repeatedly ask: **what object is this estimate actually measuring?**

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. distinguish wages, earnings, hourly pay, lifetime earnings, productivity, and rents;
2. write down and interpret a Mincer-style wage equation, including what OLS does and does not recover;
3. explain ability bias, selection, and comparative advantage in returns-to-schooling work;
4. explain why IV returns to schooling are often local objects rather than universal parameters;
5. distinguish productive returns from compensating differentials and firm or location wage premia;
6. explain how worker--firm and worker--place sorting alter the interpretation of observed education premia;
7. connect classical Roy-selection logic to modern decomposition work on firms and spatial sorting;
8. preview why Week 8 inequality and Week 9 discrimination/segmentation need this week's measurement discipline.

## Tone and authorial voice

- This chapter should read like a labor field-course chapter, not like a generic education-economics survey.
- It should open by saying that Week 4 treated skills as accumulated states, while Week 5 asks how markets translate those states into observed pay.
- The chapter should make clear that the Mincer equation is a benchmark decomposition device, not the truth.
- The chapter should not collapse all wage differences into human capital. It should explicitly separate productive differences, compensating differentials, sorting, and rents.
- The chapter should be empirically disciplined: every major object should be linked to a concrete identification problem.

## Canonical references for Week 5

These are the starter references that should appear in the Week 5 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core benchmark and selection references

- `@roy1951`
- `@mincer1974`
- `@willisRosen1979`
- `@card1999`
- `@heckmanLochnerTodd2006`

### Returns-to-schooling identification references

- `@oreopoulos2006`
- `@stephensYang2014`
- `@carneiroHeckmanVytlacil2011`

### Sorting, firms, and place references

- `@abowdKramarzMargolis1999`
- `@cardCardosoHeiningKline2018`
- `@engbomMoser2017`
- `@diamond2016`

### Bridge to later weeks

- `@juhnMurphyPierce1993`
- `@katzAutor1999`

## Section-level content requirements

### 1. Opening: from human-capital accumulation to wage determination

This section must explicitly connect back to Week 4:
- Week 4 asked how skill is accumulated;
- Week 5 asks how accumulated skill is translated into observed wages.

The opening should make four points quickly:
- wages are not the same as productivity;
- returns to schooling are not the same as returns to skill;
- observed premia combine prices, quantities, sorting, and sometimes rents;
- identification requires specifying the parameter of interest before choosing an empirical design.

### 2. The Mincer benchmark and what it buys us

This is the chapter's organizing benchmark.

Minimum content:
- write a Mincer-style log wage equation;
- connect schooling and experience coefficients to a human-capital interpretation;
- explain why the benchmark is useful even when it is misspecified;
- distinguish wages from annual earnings and explain why hours matter.

This section should also preview the core interpretation problem:
- the schooling coefficient is descriptive unless stronger assumptions make it causal.

### 3. Selection, comparative advantage, and heterogeneity

This section should teach the Roy/Willis--Rosen logic in a compact but serious way.

Minimum content:
- workers select schooling, occupations, or locations based on potential outcomes and costs;
- comparative advantage implies heterogeneous returns;
- observed wage premia reflect who selects into which schooling or sector;
- OLS, IV, and structural approaches answer different questions.

This section should make clear that selection is not only "ability bias" in the simple omitted-variable sense; it is also endogenous sorting on gains.

### 4. Causal returns to education: what does IV estimate?

This section should be design-centered.

Minimum content:
- explain the logic of compulsory-schooling instruments and regression discontinuity or law-based variation;
- distinguish OLS, IV, ATE, and LATE-style objects;
- explain why different schooling instruments may identify different groups and different margins;
- emphasize that policy relevance depends on the margin being moved.

This section should explicitly use the Oreopoulos and Stephens--Yang contrast to show that design credibility and target-parameter credibility are separate questions.

### 5. Wages are also shaped by jobs, firms, and places

This section is crucial because it prevents the week from becoming a one-dimensional returns-to-schooling chapter.

Minimum content:
- wage dispersion can reflect worker heterogeneity, firm wage premia, job ladders, or location-specific pay and amenities;
- education may raise wages partly by changing access to better-paying firms or cities;
- firm or location sorting therefore mediates observed returns to schooling;
- this is a bridge to later weeks on amenities, mobility, and inequality.

This section should use modern decomposition language without getting lost in implementation details.

### 6. What empirical designs identify in wage-determination research

Organize this section by design bucket, not by chronology.

Minimum buckets:
- descriptive wage equations;
- compulsory-schooling or law-based IV designs;
- fixed-effects matched employer--employee decompositions;
- spatial or firm-sorting designs;
- structural selection models.

For each bucket, state clearly:
- the variation used,
- the estimand targeted,
- what can be learned,
- and the main interpretive threat.

### 7. Optional extension block

The chapter should contain an explicit extension block that can be taught as an extra session, assigned as reading, or pushed into appendix slides.

Use one or both of:
- worker--firm wage decompositions and what firm premia mean;
- spatial sorting and the idea that returns to skill are partly location-mediated.

## Required formal objects

The retrofitted chapter should contain at least four formal objects and cross-reference them.

### Equation 1: Mincer benchmark

Use a compact Mincer-style equation such as:

```tex
\log w_i = \alpha + \rho s_i + \beta_1 x_i + \beta_2 x_i^2 + \varepsilon_i
```

Interpretation:
- `\rho` is a descriptive schooling premium under weak assumptions;
- the equation is a benchmark decomposition, not automatically a causal model.

### Equation 2: potential-outcomes or marginal-return object

Use a compact causal-return representation such as:

```tex
Y_i(s) = \mu_i + g_i(s)
```

or an equivalent formulation that makes heterogeneity in returns explicit.

Interpretation:
- returns to schooling may vary across individuals;
- selection on gains creates a gap between descriptive premia and policy-relevant treatment effects.

### Equation 3: LATE-style IV object

Write a compact expression making clear that IV with a schooling instrument identifies a local object, e.g.

```tex
\beta^{IV} = E\left[\frac{Y_i(1)-Y_i(0)}{S_i(1)-S_i(0)} \middle| \text{compliers} \right]
```

or an equivalent local-return statement.

Interpretation:
- IV returns depend on the margin shifted by the instrument;
- different instruments need not recover the same parameter.

### Equation 4: worker--firm wage decomposition

Use a compact AKM-style decomposition such as:

```tex
\log w_{it} = \alpha_i + \psi_{j(i,t)} + x_{it}'\beta + \varepsilon_{it}
```

Interpretation:
- observed wage differences may reflect worker effects and firm effects;
- education premia may partly operate through access to better-paying firms.

## Required figures and tables

The week should have at least three figures and two tables.

### Figure 1 (required): stylized Mincer wage profiles by schooling

Create a conceptual figure with experience or age on the horizontal axis and log wages on the vertical axis.
Use multiple schooling groups to show:
- level differences,
- slope differences,
- and concavity.

Purpose:
- visualize why "returns to schooling" can mean different things over the life cycle.

### Figure 2 (required): OLS versus IV return estimates as conceptually different objects

Create a stylized comparison of:
- descriptive OLS return,
- IV/LATE return,
- and an optional marginal-policy-return object.

Purpose:
- emphasize that design changes the parameter, not just the standard error.

### Figure 3 (encouraged): worker-skill and firm-premium sorting schematic

Create a conceptual figure showing positive sorting between worker skill and firm wage premia.

Purpose:
- make visible why education can raise wages partly by changing access to firms.

### Table 1 (required): parameter map for returns-to-schooling research

Use `assets/tables/05-returns-parameter-map.md`.
This table should distinguish:
- descriptive wage premia,
- ATE,
- LATE,
- marginal policy effects,
- and firm-mediated returns.

### Table 2 (required): sources of wage dispersion map

Use `assets/tables/05-wage-dispersion-map.md`.
This table should distinguish:
- worker skill,
- firm premia,
- amenities,
- rents,
- and place-specific effects.

## Core narrative arc

The chapter should follow this narrative:
1. Mincer gives a useful first-pass map of wage differences.
2. But schooling choices are endogenous, so observed premia need not be causal.
3. IV designs recover local returns that depend on the margin shifted.
4. Even then, wage determination is not only about worker skill because firms and places matter.
5. Therefore wage determination research must always align design, estimand, and interpretation.

## Lecture timing blueprint

### Core 3-hour lecture

**Block 1 (75 minutes):**
- opening bridge from Week 4
- Mincer benchmark
- descriptive versus causal returns
- Roy selection and heterogeneous gains intuition

**Block 2 (60 minutes):**
- compulsory-schooling IV logic
- OLS versus IV versus local parameters
- design map and identification threats

**Block 3 (45 minutes):**
- firms, locations, and sorting
- worker--firm decomposition intuition
- bridge to Week 8 inequality and Week 9 segmentation/discrimination

### Optional extension block (45--75 minutes)

Use this for one or both:
- deeper worker--firm decomposition material;
- Diamond-style place sorting and welfare consequences of skill sorting.

## Code lab design

This week's lab should follow the standard `Reproduce -> Diagnose -> Transfer -> Reflect` structure.

### Primary anchor

- `@oreopoulos2006`

Why:
- clean causal-returns-to-schooling anchor;
- official AEA replication package;
- directly supports the OLS/IV/LATE section.

### Secondary / challenge anchor

- `@stephensYang2014`

Why:
- excellent foil showing that law-based IV designs depend heavily on trend assumptions and research design details.

### Optional sorting anchor

- `@engbomMoser2017` or `@diamond2016`

Why:
- these make the important point that some returns to schooling work through access to firms or cities rather than only within-job pay.

### Bounded pedagogical transfer idea

Students should do one bounded extension such as:
- estimate a Mincer-style return to schooling on a public micro dataset and compare subgroups;
- compare OLS estimates across cohorts or locations;
- decompose a schooling premium into within- and between-group components using a public or synthetic dataset;
- extend a public wage regression by adding a simple industry, geography, or firm-proxy control.

The local smoke-test path must avoid any dependence on restricted matched employer--employee data.

## Research questions to seed in the chapter

Seed at least five research questions such as:
- when does an observed schooling premium mostly reflect sorting rather than human-capital accumulation?
- how stable are IV returns across policy margins?
- how much of returns to education operate through access to better firms or cities?
- when do wage premia reflect amenities or rents rather than productivity?
- what parameter should policy makers care about when evaluating a schooling subsidy?

## Bridge to later weeks

The conclusion should make three transitions explicit:
- to Week 6: household choices alter both observed schooling decisions and wage offers;
- to Week 7: compensating differentials mean wages alone are incomplete welfare objects;
- to Week 8: inequality research depends on decomposing wage differences into worker, firm, and market components.

## Writing instructions for Codex

When this source pack is turned into the actual chapter, Codex should:
- write a chapter that sounds like a serious labor field-course chapter rather than a generic survey;
- use valid MyST syntax and `{math}` roles for inline math in markdown;
- use at least three real citations in the opening half of the chapter;
- integrate the provided figures and tables with labeled cross-references;
- keep the optional extension block clearly marked so the 3-hour core remains teachable.
