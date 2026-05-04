# Week 1 source pack — Labor Market Facts, Measurement, and Canonical Questions

## Purpose of this file

This is the intellectual control file for Week 1. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

Which labor market facts and measurement choices organize the rest of the labor sequence, and how do they discipline later claims about labor supply, human capital, inequality, discrimination, households, and institutions?

## Week identity

- Course: Labor I
- Week: 1
- Length: 3 hours
- Position in sequence: opening field-mapping module
- Goal: establish the core empirical objects, data architecture, and decomposition logic that recur throughout Labor I and Labor II

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. distinguish the main labor market outcome variables and their measurement units;
2. explain why labor economists separate levels, composition, transitions, and equilibrium objects;
3. interpret a small set of decisive stylized facts on participation, employment, unemployment, earnings, and dispersion;
4. connect these facts to later weeks on labor supply, human capital, households, discrimination, and institutions;
5. explain why descriptive measurement is not "just background" but part of the field's identification strategy.

## Tone and authorial voice

- This chapter should sound like a graduate field-course introduction, not a generic textbook overview.
- The prose should begin with objects and questions, then move to measurement, then to interpretation.
- The chapter should name concrete literatures early.
- Avoid placeholder phrases such as "add facts here" or "one paper on labor market facts".
- Every subsection should answer a real question.

## Canonical references for Week 1

These are the starter references that should appear in the Week 1 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core references

- `@katzMurphy1992`
- `@juhnMurphyPierce1993`
- `@katzAutor1999`
- `@acemogluAutor2011`
- `@autorKatzKearney2008`
- `@blauKahn2017`
- `@cardCardosoHeiningKline2018`
- `@dalyHobijn2017`

### Data and measurement references

- `@blsCpsOverview2025`
- `@blsEarnings2026`

## Section-level content requirements

### 1. Opening section: what counts as a labor-market fact?

This section should make four distinctions immediately:
- stocks versus flows;
- prices versus quantities;
- worker outcomes versus firm outcomes;
- levels versus composition-adjusted changes.

It should introduce the idea that labor economics relies on a relatively small set of repeated outcome objects:
- employment,
- unemployment,
- participation,
- hours,
- wages,
- earnings,
- compensation,
- worker transitions,
- inequality and gaps.

### 2. Measurement architecture

This section should state clearly that the Current Population Survey is the core source for U.S. labor-force status, hours, and many earnings measures `@blsCpsOverview2025; @blsEarnings2026`.

It should define the main objects students will see throughout the sequence:
- employment-population ratio,
- labor-force participation rate,
- unemployment rate,
- weekly earnings,
- hourly wages,
- hours worked,
- demographic and education groups.

### 3. Organizing stylized facts

The chapter should frame the facts around a few durable themes rather than a laundry list.

Recommended themes:
- participation and work attachment are highly heterogeneous across demographic groups and over the life cycle;
- observed wage and earnings dispersion reflect both prices and composition `@juhnMurphyPierce1993; @dalyHobijn2017`;
- inequality trends require both demand-side and worker-side interpretations `@katzMurphy1992; @autorKatzKearney2008; @acemogluAutor2011`;
- group gaps cannot be understood only through worker characteristics because occupations, firms, and institutions matter `@blauKahn2017; @cardCardosoHeiningKline2018`.

### 4. Why this matters for the rest of the sequence

The final substantive section should preview later weeks.

Minimum links:
- Week 2: labor supply uses the stock and flow concepts introduced here;
- human capital weeks build on wage/earnings measurement and decomposition;
- household and gender weeks rely on participation, hours, and group-gap measurement;
- Labor II revisits these same outcomes from the firm, friction, and institution side.

## Required formal objects

The retrofitted chapter should contain at least two equations and cross-reference them.

### Equation 1: labor-market accounting identity

Use an equation that links employment-population ratio, labor-force participation, and unemployment.

Suggested form:

```tex
\frac{E_t}{P_t} = \frac{L_t}{P_t}\left(1-u_t\right)
```

Interpretation: the employment-population ratio bundles together entry into the labor force and success in finding work conditional on search.

### Equation 2: composition versus within-group wage change

Use a simple decomposition that previews the Daly–Hobijn lab.

Suggested form:

```tex
\bar w_t = \sum_g s_{gt}\,\bar w_{gt}
```

Then explain that changes in aggregate wages can reflect changes in group shares `s_{gt}` or within-group wage changes `\bar w_{gt}`. Keep the explanation intuitive, but make the link to `@dalyHobijn2017` explicit.

## Required figures and tables

The week should have at least one empirical figure and two tables.

### Figure 1 (required): labor-market status dashboard

Create a line chart using FRED/BLS series for:
- labor-force participation rate,
- employment-population ratio,
- unemployment rate.

Preferred series IDs:
- `CIVPART`
- `EMRATIO`
- `UNRATE`

Preferred date range:
- 1976 to most recent available.

Figure purpose:
- show that different labor-market indicators answer different questions;
- visually motivate Equation 1.

Figure caption should explain that the unemployment rate is plotted on a secondary axis if needed and should cite the underlying public data source.

### Table 1 (required): measurement map

Create a table that maps each core labor-market object to:
- economic meaning,
- typical unit of observation,
- common U.S. data source,
- common analytical use in the sequence.

Minimum rows:
- employment,
- unemployment,
- labor-force participation,
- hours,
- hourly wage,
- weekly earnings,
- compensation,
- worker transitions.

This table can be conceptual rather than numerical.

### Table 2 (required): module roadmap table

Create a short table mapping Week 1 facts to later modules.

Minimum columns:
- Week 1 fact or object
- Later module(s)
- Why the object reappears

## Required references by section

Minimum expectations:
- opening field-map section: `@katzAutor1999` and `@acemogluAutor2011`
- inequality section: `@katzMurphy1992`, `@juhnMurphyPierce1993`, `@autorKatzKearney2008`
- group gaps / gender / firms section: `@blauKahn2017`, `@cardCardosoHeiningKline2018`
- measurement section: `@blsCpsOverview2025`, `@blsEarnings2026`
- composition section: `@dalyHobijn2017`

## Lab anchor

The Week 1 lab should be explicitly tied to `@dalyHobijn2017`.

### Reproduce

Students should reproduce a small composition-adjustment calculation or figure using the reduced pedagogical dataset.

### Transfer

Students should build a compact factbook for one chosen cut of the labor market, such as:
- sex,
- age bin,
- education group,
- region.

The transfer exercise should not become a new research project. It should be one bounded extension using the same accounting logic.

## Slide sync requirements

The slide deck should contain, at minimum:
1. one slide defining the week's central question;
2. one slide with the measurement architecture table or a simplified version;
3. one slide with the labor-market status figure;
4. one slide with Equation 1 and its interpretation;
5. one slide with the composition decomposition and the Daly–Hobijn bridge;
6. one slide previewing how Week 1 feeds later weeks.

## Editing rules

When you want to change Week 1 at the intellectual level, edit this file first.

Typical examples:
- adding or removing a core paper,
- changing which figure is required,
- changing the lab paper,
- deciding that a different equation should be central,
- changing the narrative emphasis of the week.

After editing this file, ask Codex to sync:
- `books/labor-i/01-labor-market-facts.md`
- `books/labor-i/slides/week1/01-labor-market-facts.tex`
- `books/labor-i/labs/01-labor-market-facts/lab.md`
- any figure/table assets required by the chapter.
