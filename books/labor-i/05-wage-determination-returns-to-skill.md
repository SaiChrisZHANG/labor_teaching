---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Wage Determination and Returns to Skill

## Learning objectives

By the end of Week 5, students should be able to:

1. distinguish wages, earnings, hourly pay, lifetime earnings, productivity, and rents;
2. write down and interpret a Mincer-style wage equation and explain why it is a benchmark rather than a complete causal model;
3. explain why schooling premia are shaped by selection, comparative advantage, and heterogeneous returns;
4. distinguish descriptive OLS returns, IV/LATE-style returns, average treatment effects, and marginal policy effects;
5. explain how worker sorting across firms or places changes the interpretation of observed returns to schooling;
6. connect Week 5 wage-measurement discipline to Week 6 household decisions and Week 8 inequality decompositions;
7. map empirical designs to estimands, not just to identification slogans.

The economic question for the week is direct: if Week 4 treated skill as an accumulated state variable, how do labor markets translate that state into observed pay, and what exactly is being measured when an empirical paper reports a "return to schooling" or a "return to skill" [@mincer1974; @card1999; @heckmanLochnerTodd2006]?

## Bridge

Week 4 built the supply side of productive capacity. Workers invested in schooling, training, and earlier-life environments, and those investments changed the latent skill stock that later shows up in market outcomes. Week 5 asks what happens at the pricing stage. Observed wages are not direct readouts of productivity. They combine productive capacity, the market price of skill, hours, compensating differentials, access to better-paying jobs, and sometimes rents [@roy1951; @mincer1974; @willisRosen1979].

That distinction matters immediately. A wage premium for college is not automatically a pure return to human capital. It may partly reflect who selects into college, which firms hire college workers, which cities reward skill more steeply, and which jobs bundle better amenities with lower or higher pay [@card1999; @cardCardosoHeiningKline2018; @diamond2016]. The recurring Week 5 question is therefore not "is the coefficient positive?" but "what object does this estimate actually recover?"

### The Mincer benchmark and what it buys us

The canonical organizing benchmark is the Mincer wage equation:

```{math}
:label: eq-week5-mincer
\log w_i = \alpha + \rho s_i + \beta_1 x_i + \beta_2 x_i^2 + \varepsilon_i,
```

where {math}`w_i` is hourly wage, {math}`s_i` is schooling, and {math}`x_i` is potential experience. Equation {eq}`eq-week5-mincer` is useful because it turns a complicated wage-setting problem into a disciplined descriptive map: level differences, experience slopes, and lifecycle concavity can all be summarized in one compact object [@mincer1974; @heckmanLochnerTodd2006].

But Equation {eq}`eq-week5-mincer` does not interpret itself. The coefficient {math}`\rho` is a descriptive schooling premium unless stronger assumptions make it causal. Even in the cleanest case, it is a return to measured schooling in wages, not necessarily a return to latent skill. And once the outcome becomes annual earnings rather than hourly pay, hours decisions are folded into the coefficient as well. That is why Week 2 labor supply, Week 4 human capital, and Week 5 wage determination belong in sequence rather than in isolation.

```{figure} assets/figures/05-mincer-wage-profiles.png
:name: fig-week5-mincer
Stylized Mincer wage profiles by schooling group. The figure makes three teaching points at once: higher schooling can shift wage levels, alter experience slopes, and change the timing of concavity. That is why "the return to schooling" is not only a single intercept shift in practice.
```

Figure {numref}`fig-week5-mincer` is a useful first lecture picture because it shows why Mincer-style estimates remain central even when they are incomplete. They summarize wage differences over the life cycle, discipline calibration, and provide the natural baseline against which causal and structural approaches are compared.

### Core lecture map

:::{admonition} Core Material
:class: tip
- Mincer as benchmark wage accounting
- selection, comparative advantage, and heterogeneous gains
- OLS versus IV versus local return objects
- worker, firm, and place components of wage dispersion
- design-to-estimand discipline and the Week 6 / Week 8 bridges
:::

### Optional extension material

:::{admonition} Extension Block
:class: note
- deeper worker-firm decompositions in the spirit of `@abowdKramarzMargolis1999` and `@cardCardosoHeiningKline2018`
- spatial sorting and skill-price differences across cities in the spirit of `@diamond2016`
:::

## Field Core

### Selection, comparative advantage, and heterogeneous gains

The first reason not to overread Equation {eq}`eq-week5-mincer` is that workers choose schooling, occupations, and locations. In a compact potential-outcomes representation,

```{math}
:label: eq-week5-heterogeneous
Y_i(s) = \mu_i + g_i(s),
```

where {math}`Y_i(s)` is the wage outcome person {math}`i` would obtain at schooling level {math}`s`, {math}`\mu_i` captures baseline productivity or market position, and {math}`g_i(s)` allows the gain from schooling to vary across people. Equation {eq}`eq-week5-heterogeneous` is deliberately minimal, but it forces the right question: if returns vary across individuals, who selects into more schooling?

The Roy and Willis-Rosen logic is stronger than a simple omitted-variable story. Selection is not only "high-ability people have more schooling." It is also sorting on gains. Students choose schooling partly because the relative payoff to schooling differs across them, and those payoff differences can be linked to occupations, local labor markets, or access to firms [@roy1951; @willisRosen1979]. That is why the OLS coefficient in Equation {eq}`eq-week5-mincer` blends prices, quantities, and endogenous selection.

This is also the point where Week 4 matters. If earlier investments changed both skill levels and the return schedule {math}`g_i(s)`, then wage premia reflect cumulative advantage rather than one contemporaneous treatment. A field-course reading of returns-to-schooling evidence therefore has to distinguish three objects:

1. the descriptive gap in observed wages;
2. the causal effect of extra schooling for a specified margin;
3. the equilibrium pathway through which schooling changes access to occupations, firms, or places.

### What does IV estimate?

Compulsory-schooling laws and related institutional rules were important because they forced returns-to-education research to specify which causal object an instrument identifies [@card1999; @oreopoulos2006]. A compact local-return expression is

```{math}
:label: eq-week5-late
\beta^{IV}
=
E\left[
\frac{Y_i(1)-Y_i(0)}{S_i(1)-S_i(0)}
\middle|
S_i(1) > S_i(0)
\right].
```

Equation {eq}`eq-week5-late` is the Week 5 discipline in one line. IV is not merely "OLS with a better source of variation." It is a different estimand. The instrument identifies a local return for individuals whose schooling changes because the policy changes. Policy relevance depends on whether those compliers resemble the margin a policymaker cares about [@oreopoulos2006; @carneiroHeckmanVytlacil2011].

```{figure} assets/figures/05-ols-iv-late-objects.png
:name: fig-week5-ols-iv
Conceptual comparison of descriptive OLS, IV/LATE, and policy-induced marginal returns. The point is not that one line is always above another. The point is that different designs recover different objects because they move different schooling margins.
```

Figure {numref}`fig-week5-ols-iv` is helpful because it makes a point students often miss: changing the design changes the parameter, not only the standard error. Oreopoulos is valuable in class because compulsory-schooling laws "really matter" there; the first stage is economically meaningful, so the local-return interpretation is not cosmetic [@oreopoulos2006]. Stephens and Yang are equally valuable because they show that even a familiar instrument can be fragile if cohort trends or law coding are not handled carefully [@stephensYang2014]. Design credibility and target-parameter credibility are complements, not substitutes.

```{include} assets/tables/05-returns-parameter-map.md
```

Table {numref}`tbl:returns-parameter-map` is the cleanest way to keep the objects straight. OLS, ATE, LATE, marginal policy effects, and firm-mediated returns are not nested rhetorical refinements. They are distinct targets with distinct policy meanings.

### Wages are also shaped by jobs, firms, and places

If Week 5 stopped with OLS versus IV, it would still be too narrow. Wages are set inside labor markets with heterogeneous firms and heterogeneous places. A compact worker-firm decomposition is

```{math}
:label: eq-week5-akm
\log w_{it} = \alpha_i + \psi_{j(i,t)} + x_{it}'\beta + \varepsilon_{it},
```

where {math}`\alpha_i` is a worker effect, {math}`\psi_{j(i,t)}` is the premium associated with firm {math}`j`, and {math}`x_{it}` captures observables such as experience. Equation {eq}`eq-week5-akm` does not say that firm effects are pure rents or pure productivity; it says that observed wage dispersion can be decomposed into worker and firm components rather than being loaded entirely onto worker skill [@abowdKramarzMargolis1999; @cardCardosoHeiningKline2018].

```{figure} assets/figures/05-worker-firm-sorting-schematic.png
:name: fig-week5-sorting
Worker-firm sorting schematic. Education and other skill measures can raise wages partly by shifting workers toward firms with higher wage premia rather than only by raising pay within a fixed firm.
```

Figure {numref}`fig-week5-sorting` makes the firm-mediated channel visible. Engbom and Moser emphasize precisely this point for returns to education: part of the payoff to schooling can operate through access to higher-paying firms [@engbomMoser2017]. Diamond makes the analogous point for places: some returns to skill are mediated by sorting into cities with steeper skill premia, different rents, and different amenity bundles [@diamond2016].

```{include} assets/tables/05-wage-dispersion-map.md
```

Table {numref}`tbl:wage-dispersion-map` is the right transition from individual wage equations to broader inequality work. It separates productive skill, selection, firm premia, compensating differentials, and location effects. That separation is exactly what Week 8 inequality needs, because rising wage dispersion cannot be interpreted without knowing whether the movement came from skill prices, worker composition, firm dispersion, or sorting across markets [@juhnMurphyPierce1993; @katzAutor1999].

### What empirical designs identify in wage-determination research

Week 5 evidence is easiest to organize by design bucket rather than by paper chronology.

- Descriptive wage equations use cross-sectional or panel variation in schooling and experience to summarize conditional wage premia. They are useful for measurement, calibration, and lifecycle mapping, but the main threat is endogenous selection into schooling, occupations, and places.
- Compulsory-schooling or law-based IV designs use institutional variation in minimum schooling requirements or eligibility rules. They target local returns for the margin shifted by the law, and the main threat is that the instrument may be entangled with cohort trends, law coding, or other contemporaneous changes.
- Fixed-effects matched employer-employee decompositions use worker mobility across firms to separate worker and firm components. They are powerful for mapping wage dispersion, but interpretation remains contested because firm effects may bundle productivity, rents, bargaining, and amenities.
- Spatial or firm-sorting designs use variation across cities, regions, or employer access. They show that schooling can pay through market assignment, but the main threat is endogenous mobility into places or firms whose premiums are themselves equilibrium objects.
- Structural selection models use explicit assumptions on potential outcomes, costs, or marginal treatment effects. They can target policy-relevant counterfactuals, but they trade broader scope for stronger functional-form and support assumptions [@heckmanLochnerTodd2006; @carneiroHeckmanVytlacil2011].

### Why Week 5 is the bridge week

Week 5 is where Labor I stops treating wages as simple reduced-form outcomes. Week 6 will show that household formation, care constraints, marriage, and fertility change both schooling choices and observed wages because the relevant decision-maker is often a household rather than an isolated worker. Week 7 will add compensating differentials and job amenities, making it even clearer that wages are incomplete welfare objects. Week 8 will take the final step and ask how dispersion evolves across workers, firms, and markets. The conceptual discipline built here is therefore cumulative: separate the parameter, the design, and the equilibrium pathway before drawing distributional conclusions.

## Research Lab

The frontier challenge is not whether schooling matters, but which return object matters for the question at hand and through which market margin that return is realized. Modern wage-determination research sits at the intersection of human capital, selection, institutions, and market assignment. That is why Week 5 has to speak both to the classical returns-to-schooling literature and to modern worker-firm and worker-place decompositions [@oreopoulos2006; @cardCardosoHeiningKline2018; @engbomMoser2017].

The bounded Week 5 lab reflects that agenda in a teachable way. Students reproduce an `Oreopoulos`-style compulsory-schooling comparison on a deterministic synthetic dataset, diagnose why the OLS and IV estimates target different objects, and then transfer the workflow to a `Stephens and Yang`-style trend-sensitivity exercise. An optional reflection note asks how a measured schooling return might partly operate through access to better firms or cities in the spirit of `@engbomMoser2017` or `@diamond2016`.

The chapter should also leave students with open research questions:

1. When does an observed schooling premium mostly reflect sorting rather than human-capital accumulation?
2. How stable are IV returns across different compulsory-schooling margins or cohorts?
3. How much of the return to education operates through access to better firms rather than through within-firm pay?
4. When do wage premia reflect amenities or rents instead of productivity differences?
5. Which return object should policy makers care about when evaluating a schooling subsidy or completion reform?

## Methods Box

Week 5 adds one discipline to the Week 4 toolkit: never interpret a wage coefficient before naming the estimand and the market margin.

1. Start with Equation {eq}`eq-week5-mincer` as a benchmark accounting device, not as the final causal model.
2. Use Equation {eq}`eq-week5-heterogeneous` to ask whether returns vary across people and whether selection is on levels, on gains, or both.
3. Use Equation {eq}`eq-week5-late` to state clearly when IV identifies a local policy-margin return rather than a universal effect.
4. Use Equation {eq}`eq-week5-akm` to ask whether wage differences operate partly through firms or places instead of only within a worker-level return schedule.
5. Before using wage gaps for welfare or inequality claims, separate productivity, amenities, rents, and assignment effects.

## Reading ladder

### Bridge

- Roy on earnings distributions and selection [@roy1951]
- Mincer on schooling, experience, and earnings profiles [@mincer1974]
- Card's guide to causal returns to education [@card1999]

### Field Core

- Willis and Rosen on education and self-selection [@willisRosen1979]
- Heckman, Lochner, and Todd on earnings functions, treatment effects, and the limits of the Mincer equation [@heckmanLochnerTodd2006]
- Oreopoulos on compulsory-schooling IV when the first stage is economically meaningful [@oreopoulos2006]
- Stephens and Yang on trend sensitivity in compulsory-schooling designs [@stephensYang2014]
- Carneiro, Heckman, and Vytlacil on marginal returns and local policy objects [@carneiroHeckmanVytlacil2011]

### Research Lab

- Abowd, Kramarz, and Margolis on worker and firm components of wages [@abowdKramarzMargolis1999]
- Card, Cardoso, Heining, and Kline on firms and labor-market inequality [@cardCardosoHeiningKline2018]
- Engbom and Moser on returns to education through access to higher-paying firms [@engbomMoser2017]
- Diamond on diverging location choices by skill [@diamond2016]
- Juhn, Murphy, and Pierce and Katz and Autor for the bridge to rising wage inequality [@juhnMurphyPierce1993; @katzAutor1999]

## Exercises / discussion prompts

1. Equation {eq}`eq-week5-mincer` treats the schooling premium as one coefficient. Use Figure {numref}`fig-week5-mincer` to explain why lifecycle slope differences can still matter for interpretation even when the reported coefficient is a single average.
2. In Equation {eq}`eq-week5-heterogeneous`, what exactly distinguishes selection on levels from selection on gains, and why does the distinction matter for OLS interpretation?
3. Explain in words what Equation {eq}`eq-week5-late` identifies and why two valid instruments need not recover the same return.
4. Use Table {numref}`tbl:returns-parameter-map` to compare a descriptive OLS premium, a LATE, and a marginal policy effect. Which of the three is closest to the object a policymaker wants when expanding compulsory schooling?
5. Figure {numref}`fig-week5-sorting` shows positive worker-firm sorting. Give two reasons this can make the education premium larger even if within-firm pay schedules stay unchanged.
6. Why is Table {numref}`tbl:wage-dispersion-map` a necessary prelude to Week 8 inequality?
7. How might the household models from Week 6 change the interpretation of an estimated return to schooling for women or secondary earners?

## Reproducibility or code lab note

The Week 5 lab is organized around a bounded `Reproduce -> Diagnose -> Transfer -> Reflect` path that runs fully locally. Students reproduce one synthetic compulsory-schooling design in the spirit of `@oreopoulos2006`, diagnose why the resulting OLS and IV estimates are different empirical objects, and then transfer the workflow to a `@stephensYang2014`-style trend-sensitivity exercise. The smoke path avoids restricted matched employer-employee data and keeps the sorting extension optional and conceptual. The bounded workflow is documented in [labs/05-wage-determination-returns-to-skill/lab.md](labs/05-wage-determination-returns-to-skill/lab.md).

## Slide companion note

The Week 5 deck should isolate the pricing problem rather than reproduce the chapter. It should move from the Week 4 human-capital bridge to the Mincer benchmark, selection and heterogeneous gains, OLS versus IV/LATE interpretation, worker-firm or worker-place sorting, the parameter map table, and the bridges to Week 6 households and Week 8 inequality. The canonical source is [slides/week5/05-wage-determination-returns-to-skill.tex](slides/week5/05-wage-determination-returns-to-skill.tex).
