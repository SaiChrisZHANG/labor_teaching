# Week 6 source pack — Households, Family, Fertility, and Time Allocation

## Purpose of this file

This is the intellectual control file for Week 6. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do household structure, fertility, care demands, bargaining, and time-allocation constraints transform worker-level labor-supply and wage models into family-level labor-market outcomes?

## Week identity

- Course: Labor I
- Week: 6
- Length: 3 hours core, with an optional 45--90 minute extension block on child penalties, gender norms, or family-policy counterfactuals
- Position in sequence: this is the hinge week after Week 5 wage determination and before Week 7 job amenities and compensating differentials
- Goal: move from individual worker choice to joint household choice, introduce household production and collective models, treat fertility and care as labor-market shocks, and show how family structure helps generate persistent gender gaps in labor supply and earnings

## Why this week matters

Week 6 is where Labor I stops treating labor supply as an individual optimization problem only. Students should see that:
- observed hours and earnings are often household outcomes rather than purely individual outcomes;
- children and care needs change both the shadow price of time and the relevant choice set;
- intrahousehold bargaining, norms, and policy design matter for labor-market incidence;
- some of the most persistent gender gaps in modern labor markets are better understood as family-allocation phenomena than as pure market discrimination.

This week should make clear that household structure is not a side topic. It is one of the key channels through which labor supply, human capital, career progression, and wage inequality are jointly produced.

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. distinguish individual labor-supply models from household or family labor-supply models;
2. explain the roles of household production, childcare, and care constraints in time allocation;
3. distinguish unitary household models, collective models, and bargaining interpretations;
4. explain how marriage, fertility, and childbirth create dynamic labor-market shocks;
5. interpret child-penalty estimates and explain what event-study designs recover;
6. explain how policy instruments such as childcare, schooling, parental leave, or tax-transfer design affect family labor supply;
7. connect household models to modern gender-gap evidence without collapsing the analysis into a generic gender chapter;
8. see why Week 8 inequality and Week 9 discrimination/segmentation must account for household structure.

## Tone and authorial voice

- This chapter should read like a labor field-course chapter, not like a generic family-economics survey.
- It should open by saying that Week 5 treated wages as market outcomes, while Week 6 asks how families transform those wage opportunities into actual labor-market behavior.
- The chapter should be explicit that children are not merely "controls" in labor regressions; they are major reallocators of time, occupation choice, hours, and career trajectories.
- The chapter should connect theory and empirics tightly: each household model should be linked to a distinct empirical object.
- The chapter should not drift entirely into development or demography. Keep the center of gravity on labor supply, hours, earnings, and policy incidence.

## Canonical references for Week 6

These are the starter references that should appear in the Week 6 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core theory and household-allocation references

- [@becker1965]
- [@gronau1977]
- [@chiappori1992]
- [@lundbergPollakWales1997]
- [@blundellPistaferriSaportaEksten2016]

### Empirical family-labor and care-constraint references

- [@gelbach2002]
- [@cortesTessada2011]
- [@lundborgPlugRasmussen2017]
- [@klevenLandaisSogaard2019]
- [@cortesPan2023]

### Optional extension and policy references

- [@klevenLandaisPoschSteinhauerZweimueller2024]
- [@bertrandKamenicaPan2015]

## Section-level content requirements

### 1. Opening: from individual labor supply to family allocation

This section must explicitly connect back to Weeks 2--5:
- Weeks 2 and 3 treated labor supply as an individual intertemporal choice problem;
- Weeks 4 and 5 connected skill accumulation to wages;
- Week 6 asks why similar wage opportunities can produce very different labor-market choices once households, partners, and children are introduced.

The opening should make four points quickly:
- household decisions are joint decisions even when data are observed at the person level;
- care time, home production, and market substitutes alter labor-supply margins;
- children create dynamic reallocations of hours, occupations, and career progression;
- family policy changes can shift labor-market outcomes without changing pre-tax wages.

### 2. Household production and the allocation of time

Minimum content:
- time can be allocated to market work, home production/care, and leisure;
- home production makes labor supply depend on the price and availability of market substitutes;
- fertility and young children alter both the demand for care and the effective household budget set;
- this creates a bridge to childcare, school-start, and outsourcing evidence.

This section should make clear that time-use margins are central, not decorative.

### 3. Unitary, collective, and bargaining models of the household

Minimum content:
- define the unitary model and its pooling implications;
- explain why distribution factors and income-source shifts challenge pure pooling;
- introduce collective efficiency and the sharing-rule interpretation;
- connect intrahousehold bargaining to labor-supply incidence and policy design.

This section should state clearly that different household models generate different empirical tests.

### 4. Fertility, marriage, and caregiving as labor-market shocks

Minimum content:
- childbirth and caregiving change the timing of work, occupation, and career investment;
- marriage or partnership can generate specialization, coordination, or bargaining effects;
- empirical work often relies on fertility instruments, childcare/schooling shocks, or event studies around birth;
- the sign and size of effects differ by margin: participation, hours, occupation, wage growth, and firm choice.

This section should prepare students to understand why fertility designs and child-event studies are so prominent in modern labor and gender research.

### 5. Child penalties and the modern household-labor evidence

This is the empirical center of the chapter.

Minimum content:
- define the child-penalty concept in earnings, hours, participation, and wage growth;
- explain the event-study logic around first birth;
- show that child penalties are dynamic and persistent rather than one-period shocks;
- connect penalties to occupation, sector, and firm choice rather than only contemporaneous hours.

This section should explicitly connect the Lundborg IVF design to causal fertility effects and the Kleven Denmark design to dynamic decompositions of gender inequality.

### 6. Family policy, childcare, and market substitutes

Organize this section by policy or margin, not chronology.

Minimum content:
- public schooling or childcare access;
- parental leave and family-policy expansions;
- household outsourcing and close substitutes for home production;
- the incidence of these policies on participation, hours, and longer-run earnings.

The point is not to prove one universal policy conclusion. The point is to show that the same worker wage opportunities can generate very different outcomes depending on care institutions and household technology.

### 7. Optional extension block

The chapter should contain an explicit extension block that can be taught as an extra session, assigned as reading, or moved to appendix slides.

Use one or both of:
- child penalties, family policy, and the persistence of gender inequality;
- household bargaining, norms, and relative-income constraints inside couples.

## Required formal objects

The retrofitted chapter should contain at least four formal objects and cross-reference them.

### Equation 1: household time constraint

Use a compact time-allocation object such as:

```tex
T_i = h_i + n_i + \, \ell_i
```

where market work {math}`h_i`, home production or care {math}`n_i`, and leisure {math}`\ell_i` exhaust available time.

Interpretation:
- labor supply depends on the shadow value of home production and care time;
- childbirth or care shocks change the feasible allocation of time, not just the wage.

### Equation 2: household resource or household-production problem

Use a compact household problem such as:

```tex
\max U(c_f, c_m, \ell_f, \ell_m, q)
\quad \text{s.t.} \quad c_f + c_m + p_x x = w_f h_f + w_m h_m + y,
\quad q = F(n_f, n_m, x)
```

Interpretation:
- household choices jointly determine consumption, labor supply, and care output;
- market substitutes for care enter through {math}`x` and its price {math}`p_x`.

### Equation 3: collective or sharing-rule representation

Use a compact collective formulation such as:

```tex
\max \lambda U_f(\cdot) + (1-\lambda) U_m(\cdot)
```

or a two-stage sharing-rule representation.

Interpretation:
- distribution factors can alter choices even when total household income is unchanged;
- policy incidence depends on who receives resources and how bargaining weights respond.

### Equation 4: event-study child-penalty object

Use a compact event-study or penalty representation such as:

```tex
Y_{it} = \sum_{k \neq -1} \beta_k \mathbf{1}\{t - b_i = k\} + \alpha_i + \gamma_t + \varepsilon_{it}
```

or a directly normalized penalty object.

Interpretation:
- the arrival of children can be treated as a dynamic event;
- the object of interest is not only the short-run level shift but the full post-birth path.

## Required figures and tables

The week should have at least three figures and two tables.

### Figure 1 (required): household time-allocation schematic

Create a conceptual figure showing the division of time between market work, home production/care, and leisure for two household states: pre-child and post-child.

Purpose:
- make clear that childbirth changes the time-allocation problem, not just preferences.

### Figure 2 (required): stylized child-penalty event study

Create a conceptual event-study figure with years relative to first birth on the horizontal axis and log earnings or hours on the vertical axis, with separate lines for mothers and fathers.

Purpose:
- visualize dynamic divergence after childbirth.

### Figure 3 (required): childcare or household-service substitution schematic

Create a conceptual figure showing how a fall in the price of household-market substitutes or childcare can shift labor supply, especially for the high-opportunity-cost spouse.

Purpose:
- connect household production to market labor outcomes and policy design.

### Table 1 (required): household-model map

Use `assets/tables/06-household-model-map.md`.
This table should distinguish:
- unitary model,
- collective/bargaining model,
- dynamic family-labor model,
- child-event-study design,
- and outsourcing or care-substitute designs.

### Table 2 (required): policy-margin map

Use `assets/tables/06-policy-margin-map.md`.
This table should link policy or design buckets to the margin of adjustment:
- participation,
- hours,
- occupation/firm choice,
- earnings path,
- and time allocation.

## Lab spine and design

The chapter should support the standard lab structure: **Reproduce -> Diagnose -> Transfer**.

### Primary lab anchor

- [@lundborgPlugRasmussen2017]

Reason to anchor here:
- it is a clean causal fertility design using IVF-induced variation;
- it gives students an IV design that is substantively central to the week;
- there is an official AEA/openICPSR replication package.

### Secondary lab anchor

- [@klevenLandaisSogaard2019]

Reason to use as secondary or challenge anchor:
- it operationalizes child penalties with a dynamic event-study design;
- it turns a family event into a labor-market decomposition object;
- there is an official AEA/openICPSR replication package.

### Optional policy or outsourcing extension

Use one of:
- [@gelbach2002]
- [@cortesTessada2011]
- [@klevenLandaisPoschSteinhauerZweimueller2024]

### Transfer-exercise idea

The bounded pedagogical transfer should be something students can run without restricted administrative data. Good options include:
- simulate a child-penalty event study using a small public or synthetic panel;
- estimate a stylized maternal labor-supply response to childcare-cost or school-start variation on a public teaching dataset;
- build a simple joint labor-supply or outsourcing simulation with care-price shocks.

The smoke test should only run the bounded pedagogical path.

## Reading-ladder requirements

The chapter must contain a real reading ladder, not placeholders.

### Bridge / foundation readings

- [@becker1965]
- [@gronau1977]
- [@lundbergPollakWales1997]

### Field-core readings

- [@chiappori1992]
- [@blundellPistaferriSaportaEksten2016]
- [@lundborgPlugRasmussen2017]
- [@klevenLandaisSogaard2019]

### Frontier / synthesis readings

- [@cortesPan2023]
- [@klevenLandaisPoschSteinhauerZweimueller2024]
- [@bertrandKamenicaPan2015]

## Slide requirements

The slide deck should use the repo's Beamer conventions and include, at minimum:
1. central question and motivation,
2. Week 5 to Week 6 bridge,
3. household time-allocation problem,
4. unitary versus collective models,
5. fertility and childbirth as labor-market shocks,
6. child-penalty event-study figure,
7. household-model map table,
8. policy-margin map table,
9. bridge to Week 7 amenities and Week 8 inequality.

## Writing warnings

- Do not turn this into an all-purpose gender chapter. Keep the core labor-economics logic visible.
- Do not write "households matter" repeatedly without specifying the margin affected.
- Do not use inline math with `\(...\)` in markdown. Use valid MyST inline math syntax such as {math}`\lambda`, {math}`T_i`, or {math}`q = F(n_f, n_m, x)`.
- Do not bury the empirical designs. Students should be able to say exactly what the fertility-IV design identifies and what the child-event-study design identifies.
- Do not let family policy discussion become vague. State whether the policy changes time prices, bargaining incidence, participation constraints, or dynamic career costs.

## Sync instructions for Codex after drafting

When this source pack is turned into the full Week 6 package, Codex should:
1. draft the chapter markdown;
2. create slides only under `books/labor-i/slides/week6/`;
3. create the lab package under `books/labor-i/labs/06-households-family-fertility-time-allocation/`;
4. wire the week into `index.md` and `myst.yml` if needed;
5. validate the week with the standardized local workflow using the `research` conda environment.
