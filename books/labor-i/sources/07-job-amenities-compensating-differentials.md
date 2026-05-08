# Week 7 source pack — Job Amenities and Compensating Differentials

## Purpose of this file

This is the intellectual control file for Week 7. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do workers trade wages against nonwage job attributes, how do firms price and bundle job quality, and why do empirical estimates of compensating differentials often depart from the clean hedonic benchmark?

## Week identity

- Course: Labor I
- Week: 7
- Length: 3 hours core, with an optional 45--90 minute extension block on risky jobs, modern job design, remote work, or search-friction models of amenities
- Position in sequence: this is the hinge week after Week 6 households/family allocation and before Week 8 inequality and wage dispersion
- Goal: show that labor-market compensation includes both wages and working conditions, teach the canonical equalizing-differences framework, explain why hedonic regressions are often fragile, and connect modern experimental/revealed-preference evidence on amenities to wage structure and inequality

## Why this week matters

Week 7 is where Labor I stops treating wages as the full object of worker welfare. Students should see that:
- workers choose jobs, not just wages;
- amenities such as schedule control, flexibility, risk, commute burden, autonomy, prestige, safety, and remote work are part of compensation;
- equalizing-differences theory is one of the deepest equilibrium ideas in labor economics, but it is empirically difficult because preferences, job attributes, search frictions, and information are all heterogeneous;
- wage inequality can look very different once we account for differences in working conditions.

This week should make clear that job quality is not a soft, peripheral topic. It is a central reason why wage data alone can mismeasure welfare, inequality, sorting, and policy incidence.

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. define compensating differentials and explain their equilibrium logic;
2. distinguish wage inequality from total-compensation or job-quality inequality;
3. explain the canonical Rosen hedonic framework and its equalizing-differences condition;
4. explain why simple cross-sectional hedonic wage regressions can fail under sorting, frictions, multidimensional amenities, or mismeasurement;
5. distinguish classic risk-premium evidence from modern stated-preference, field-experimental, or revealed-preference approaches;
6. explain how schedule unpredictability, remote work, commute costs, and safety risks can all be treated as amenities or disamenities;
7. connect amenities to worker sorting, family constraints, and inequality;
8. see why Week 8 inequality and Week 9 discrimination/segmentation must distinguish wages from broader job quality.

## Tone and authorial voice

- This chapter should read like a labor field-course chapter, not like a human-resources or management note.
- It should open by saying that Week 5 studied how wages are determined and Week 6 studied how households transform wage opportunities into observed labor supply; Week 7 asks why even identical wages can represent very different jobs.
- The chapter should make the equilibrium logic vivid, but it should not pretend the frictionless hedonic model is empirically sufficient.
- The chapter should clearly separate:
  - theory of equalizing differences,
  - reasons the theory is hard to test,
  - modern empirical strategies that recover willingness to pay for job amenities more credibly.
- The chapter should connect amenities to modern labor questions: schedule control, job safety, remote work, working conditions, and the structure of wage inequality.

## Canonical references for Week 7

These are the starter references that should appear in the Week 7 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core theory and equilibrium references

- [@rosen1986]
- [@hwangMortensenReed1998]
- [@bonhommeJolivet2009]

### Risk and classic compensating-differentials references

- [@viscusiAldy2003]

### Modern experimental and revealed-preference references

- [@masPallais2017]
- [@maestasMullenPowellVonWachterWenger2023]
- [@sorkin2018]

### Optional synthesis and inequality references

- [@hamermesh1999]
- [@cardCardosoHeiningKline2018]

## Section-level content requirements

### 1. Opening: jobs are bundles, not wages

This section must explicitly connect back to Weeks 5 and 6:
- Week 5 treated wages and returns as key labor-market outcomes;
- Week 6 showed households transform wages into family choices;
- Week 7 says the object workers value is a full job bundle, not the wage alone.

The opening should make four points quickly:
- a job can be high wage and low amenity, or lower wage and high amenity;
- nonwage attributes affect both worker welfare and firm wage-setting;
- worker sorting implies that observed wage gaps are not automatically welfare gaps;
- inequality analysis can be misleading if job quality is omitted.

### 2. Canonical theory: equalizing differences and hedonic equilibrium

Minimum content:
- define an amenity/disamenity {math}`a` and a wage schedule {math}`w(a)`;
- explain that in a competitive equilibrium workers sort across jobs by preferences for {math}`a` and firms choose {math}`a` based on cost/productivity tradeoffs;
- derive the worker-side condition relating the wage-amenity slope to the marginal rate of substitution;
- explain that observed hedonic slopes reflect both worker heterogeneity and firm heterogeneity.

This section should teach the core idea cleanly: if markets work frictionlessly and workers are informed, unpleasant jobs must compensate workers along the margin.

### 3. Why simple hedonic wage regressions often fail

Minimum content:
- amenities are multidimensional and often imperfectly measured;
- workers sort on unobserved taste and skill;
- firms differ in productivity and may bundle multiple amenities together;
- information frictions, search frictions, and mobility costs break the simplest equalizing-differences logic.

This section should explain why empirical failures do not automatically invalidate the theory. They often reveal frictions, heterogeneity, and equilibrium selection problems.

### 4. Empirical strategies

Organize by design, not by chronology.

Minimum content:
- risk premiums and the value of statistical life;
- hedonic wage regressions and why they are fragile;
- stated-preference / discrete-choice / conjoint designs;
- revealed-preference or worker-flow methods that recover job value from choices.

This section should make clear which designs estimate:
- a reduced-form wage-amenity tradeoff,
- a willingness-to-pay parameter,
- or a broader revealed-preference ranking of firms/jobs.

### 5. Modern amenities: schedule control, remote work, and job design

This is the empirical center of the chapter.

Minimum content:
- schedule unpredictability versus worker-controlled flexibility;
- remote work and commute-related job quality;
- autonomy, workload, and other broader working conditions;
- why family structure and care constraints from Week 6 can shift valuations of the same amenity.

This section should explicitly connect Mas--Pallais to the broader working-conditions measurement in Maestas et al.

### 6. Amenities, sorting, and inequality

Minimum content:
- total compensation is wages plus job quality;
- workers with stronger outside options may sort into better amenities, not just higher wages;
- accounting for amenities can either attenuate or amplify measured inequality depending on sorting patterns;
- the interpretation of wage gaps changes when job quality differs systematically by worker group or firm type.

This section should prepare students for Week 8 by saying that wage dispersion is not the same thing as inequality in labor-market value.

### 7. Optional extension block

The chapter should contain an explicit extension block that can be taught as an extra session, assigned as reading, or moved to appendix slides.

Use one or both of:
- risky jobs, the value of statistical life, and regulatory incidence;
- search-friction or revealed-preference models of firm/job ranking and nonwage value.

## Required formal objects

The retrofitted chapter should contain at least four formal objects and cross-reference them.

### Equation 1: worker utility / indirect utility over wages and amenities

Use a compact worker-side object such as:

```tex
U = u(c, \ell, a), \qquad c = w + y
```

or an indirect-utility object {math}`V(w,a)`.

Interpretation:
- jobs are valued along multiple dimensions;
- the sign of the amenity term depends on whether {math}`a` is a good (flexibility, safety, autonomy) or a bad (risk, unpredictability, long commute).

### Equation 2: worker-side equalizing-differentials condition

Use a compact first-order condition such as:

```tex
\frac{dw(a)}{da} = - \frac{V_a(w,a)}{V_w(w,a)}
```

Interpretation:
- the equilibrium wage slope compensates workers at the margin for worse job attributes;
- heterogeneity in {math}`V_a/V_w` implies heterogeneous willingness to pay and sorting.

### Equation 3: firm-side amenity cost or profit problem

Use a compact firm-side object such as:

```tex
\pi = p f(n, a) - w(a)n - C(a)
```

or a reduced-form amenity-cost schedule.

Interpretation:
- firms differ in the cost or productivity consequences of supplying amenities;
- equilibrium amenity provision depends on both worker demand and firm cost heterogeneity.

### Equation 4: modern discrete-choice / willingness-to-pay object

Use a compact discrete-choice setup such as:

```tex
U_{ij} = \beta_w w_{ij} + \beta_a a_{ij} + X_{ij}'\gamma + \varepsilon_{ij}
```

Interpretation:
- experimental or stated-preference designs estimate how workers value specific job attributes;
- willingness to pay is often recovered as {math}`-\beta_a / \beta_w`.

## Required figures and tables

The week should have at least three figures and two tables.

### Figure 1 (required): hedonic wage-amenity equilibrium

Create a conceptual figure with:
- worker indifference curves in wage-amenity space,
- an equilibrium wage-amenity schedule,
- at least two worker types with different amenity valuations.

Purpose:
- make the equalizing-differences intuition concrete.

### Figure 2 (required): willingness to pay for selected amenities

Use a clean bar chart or dot plot for a few stylized amenities:
- predictable schedule,
- remote work option,
- lower injury risk,
- shorter commute,
- worker-controlled flexibility.

Purpose:
- make the idea of heterogeneous amenity valuations legible.

### Figure 3 (required): wage inequality versus total job value

Create a conceptual figure showing how ranking workers or jobs by wages alone can differ from ranking them by wages plus job-quality value.

Purpose:
- bridge to Week 8 inequality and wage dispersion.

### Table 1 (required): amenity taxonomy

This table should classify job attributes into:
- risks and physical conditions,
- schedule and timing,
- location/commute/remote work,
- autonomy/monitoring/work intensity,
- prestige/meaning/social environment.

### Table 2 (required): empirical design map

This table should map:
- hedonic regressions,
- risk-premium studies,
- discrete-choice / conjoint experiments,
- worker-flow / revealed-preference methods,

to the objects they identify, strengths, and principal threats.

## Required citations / arguments that must appear

The chapter should explicitly make the following points with citations:

1. Rosen's equalizing-differences framework is the canonical equilibrium benchmark for wage-amenity tradeoffs.
2. Search frictions and worker/firm heterogeneity complicate the link between observed wages and underlying willingness to pay.
3. Modern experimental evidence shows workers value some amenities very highly, but valuations are heterogeneous.
4. Working conditions are quantitatively important for the structure of wages and inequality.

## Code lab design

Week 7 is a very good week for the standard two-part lab structure.

### Primary lab anchor

- [@masPallais2017]

Why:
- excellent for teaching willingness to pay for amenities,
- clean bridge from theory to modern discrete choice,
- official AEA replication materials.

### Secondary or challenge anchor

- [@maestasMullenPowellVonWachterWenger2023]

Why:
- expands the object from a few job attributes to a richer working-conditions bundle,
- connects directly to inequality and wage structure,
- official AEA replication materials.

### Optional extension anchor

- [@sorkin2018]

Why:
- good bridge from explicit amenity attributes to revealed-preference rankings of firms/jobs,
- useful for optional extension on worker flows, ranking, and firm heterogeneity.

## Transfer exercise ideas for the lab

The student extension should be bounded and feasible. Good options:

1. Code a small hand-built job-posting dataset (for one occupation or metro area) with a few amenities:
   - remote/hybrid,
   - predictable schedule,
   - weekend/night requirement,
   - posted pay range,
   - travel/physical requirements.

2. Use a public occupational dataset (for example O*NET-style descriptors if you decide to include them later) and estimate how wages co-move with a small set of amenity proxies.

3. Reuse the discrete-choice logic on a synthetic or reduced teaching dataset and estimate willingness to pay for one added amenity.

The bounded pedagogical path should not require proprietary microdata.

## Reading ladder

### Core required reading

- [@rosen1986]
- [@masPallais2017]
- [@maestasMullenPowellVonWachterWenger2023]

### Recommended supporting reading

- [@hwangMortensenReed1998]
- [@bonhommeJolivet2009]
- [@viscusiAldy2003]

### Optional extension reading

- [@sorkin2018]
- [@hamermesh1999]

## Explicit bridge to other weeks

The chapter must explicitly say:
- Week 6 showed family structure changes the valuation of job bundles; the same amenity can be worth more to workers facing care constraints.
- Week 8 will ask how wage dispersion and inequality look different once job quality enters the picture.
- Week 9 will ask whether disadvantaged groups systematically receive worse jobs as well as lower wages, and how that affects the interpretation of labor-market inequality.

## What the finished chapter should feel like

By the end, students should feel that:
- equalizing differences is one of the core equilibrium ideas in labor economics;
- empirical work on amenities is hard precisely because the theory is about sorting and heterogeneous valuations;
- modern labor economics has moved from naive hedonic regressions toward designs that recover willingness to pay more directly;
- job quality is essential for understanding both labor supply and inequality.
