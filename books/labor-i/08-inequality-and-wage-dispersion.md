---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Inequality and Wage Dispersion

## Learning Objectives

By the end of Week 8, students should be able to:

1. distinguish hourly wage inequality, annual earnings inequality, hours and employment inequality, total job-value inequality, and household inequality;
2. define quantile-based and variance-based inequality objects and explain why they answer different empirical questions;
3. write down and interpret a between-group versus within-group variance decomposition;
4. explain what residual inequality means in a descriptive wage equation and why it became central after [@juhnMurphyPierce1993];
5. connect the college premium, task polarization, institutions, firm premia, and sorting to different parts of the wage distribution rather than to one master mechanism;
6. interpret linked employer-employee decompositions in the spirit of [@cardCardosoHeiningKline2018] and [@songPriceGuvenenBloomVonWachter2019];
7. explain why Week 7's amenity logic implies that wage inequality and total labor-market value inequality are not the same object;
8. see why Week 9 discrimination and segmentation require this distributional architecture rather than replacing it.

## Opening Orientation

The economic question for the week is deliberately broader than in earlier modules: once Weeks 5 and 6 have explained how wages and households convert market opportunities into realized outcomes, and Week 7 has shown that wages do not exhaust job value, how should labor economists measure inequality and organize the mechanisms that shape the distribution of labor-market outcomes [@autorKatzKearney2008; @cardCardosoHeiningKline2018; @songPriceGuvenenBloomVonWachter2019]?

:::{admonition} Core materials
:class: tip
- inequality is multi-object, multi-mechanism, and multi-level
- upper-tail and lower-tail movements need not have the same cause
- descriptive decompositions are not causal designs, but they are strong theory discipline
- firm heterogeneity and amenities change how wage dispersion should be interpreted
:::

## Bridge

Week 5 put wage determination at the center of the worker side of labor economics. Week 6 showed that households transform wages into hours, participation, and realized earnings. Week 7 added the crucial correction that jobs are bundles of wages plus amenities, so measured pay is not the whole labor-market opportunity set. Week 8 now asks how those objects aggregate into inequality.

That move matters because inequality is not one number attached to one outcome. Hourly wages, annual earnings, hours, employment, total compensation, and household resources can all tell different stories. A rise in annual-earnings inequality may come from wider hourly wage dispersion, weaker hours for the lower tail, more nonemployment, or all three. A rise in wage inequality may overstate or understate welfare inequality if desirable amenities sort with high-pay jobs. Before students ask why inequality changed, they need to know which distribution they are studying and which margin is actually moving [@lemieux2006; @autorKatzKearney2008].


:::{admonition} Optional Extension Block
:class: note
- linked employer-employee decompositions, firm wage premia, and sorting in the spirit of [@cardCardosoHeiningKline2018]
- workplace concentration, rents, and distributional incidence in the spirit of [@songPriceGuvenenBloomVonWachter2019]
- supply, firms, institutions, and the full wage distribution in the spirit of [@haanwinckel2025]
:::

## Field Core

### Inequality is not one object

The first discipline is to separate the empirical object from the explanation. The weekly source pack insists on this because many disagreements in the inequality literature are really disagreements about what is being measured. For wage-setting questions, hourly wages are often the cleanest object because they strip out many hours and employment margins. For labor-market well-being, annual earnings are often more relevant because they incorporate the quantity of work supplied. For welfare-oriented questions, even annual earnings can be too narrow because Week 7 showed that workers care about schedule control, safety, stability, commute burden, and autonomy as part of compensation.

```{include} assets/tables/08-inequality-concepts-map.md
```

Table {numref}`tbl:ineq-concepts-map` should anchor the opening discussion. The field-course point is not that one object is universally best. It is that different objects answer different questions. That is why the same economy can exhibit moderate hourly wage dispersion, much larger annual earnings dispersion, and an even different ranking once total job value is monetized.

### Measurement architecture: distributions, percentiles, and interpretation

Let {math}`F_t(w)` denote the wage distribution in period {math}`t`, and let {math}`q_t(\tau)` denote its {math}`\tau`-quantile. The most teachable compact object for this week is

```{math}
:label: eq-week8-quantiles
q_t(\tau) = F_t^{-1}(\tau), \qquad D_t^{90-10} = q_t(0.9) - q_t(0.1).
```

Equation {eq}`eq-week8-quantiles` makes two ideas visible. First, inequality comparisons are comparisons of functions of distributions, not only of means. Second, upper-tail and lower-tail movements can be separated. The statistics {math}`p90-p50` and {math}`p50-p10` isolate the upper and lower halves of the wage distribution; a change in one need not imply the same change in the other [@autorKatzKearney2008].

```{figure} assets/figures/08-percentile-gap-series.png
:name: fig-week8-percentiles
Stylized percentile-gap series for log wages. The figure emphasizes that upper-tail and lower-tail inequality need not move together, even when the full {math}`p90-p10` spread rises.
```

Figure {numref}`fig-week8-percentiles` is the cleanest way to explain why quantile objects became canonical. If {math}`p90-p50` rises while {math}`p50-p10` is flat or falling, then a model aimed at the entire distribution is already too coarse. That is one reason the post-1980 literature split upper-tail inequality, lower-tail inequality, and middle compression into separate but related facts [@juhnMurphyPierce1993; @autorKatzKearney2008].

Variance-based measures play a different role. The log variance compresses the entire distribution into one scalar and is especially convenient for decomposition. But it weights the tails differently from percentile gaps and can react strongly to top-end changes. Top shares add yet another lens, especially when the upper tail becomes sufficiently influential that broad quantile summaries hide what is happening above the {math}`p90` or {math}`p95`. A serious chapter therefore teaches percentile gaps, log-variance measures, and the conceptual role of top shares without pretending they are interchangeable.

The measurement lesson from Week 7 belongs here too. If desirable amenities are concentrated among high-wage jobs, wage inequality understates inequality in total labor-market value. If workers accept lower wages for flexibility or safety, wage inequality can overstate welfare inequality. Measurement is therefore not separate from welfare interpretation; it disciplines it.

### Between-group, within-group, and residual inequality

Once the object is defined, the next question is where dispersion sits. A basic decomposition groups workers by education, occupation, place, industry, or firm and asks how much wage dispersion comes from gaps between group means versus inequality within groups. The compact variance accounting identity is

```{math}
:label: eq-week8-between-within
\operatorname{Var}(\log w) = \operatorname{Var}\!\left(\mathbb{E}[\log w \mid g]\right) + \mathbb{E}\!\left[\operatorname{Var}(\log w \mid g)\right].
```

Equation {eq}`eq-week8-between-within` is descriptive, but it is not trivial. If inequality rises because group means diverge, then compositional or price changes across observed categories are important. If inequality rises mostly within groups, then the field needs richer heterogeneity, unobservables, institutions, or firm-level margins to explain the data [@juhnMurphyPierce1993; @lemieux2006].

The wage-equation version of the same idea is

```{math}
:label: eq-week8-residual
\log w_{it} = X_{it}'\beta_t + u_{it},
```

where {math}`X_{it}` might include education, experience, gender, occupation, region, or other observables. Equation {eq}`eq-week8-residual` does not claim that the residual is a structural primitive. It says only that some part of inequality remains after conditioning on measured characteristics. The empirical surprise documented in the classic literature is that residual inequality increased substantially even when observable composition shifts alone were not large enough to explain the full rise [@juhnMurphyPierce1993; @lemieux2006].

Students should be taught to read the residual carefully. It is not "pure skill." It mixes unobserved productivity, rent sharing, measurement error, bargaining, job ladders, task differences, and omitted institutions. But the residual is still informative because it tells the field where simple observables stop being enough.

### Canonical facts: what changed and where in the distribution

The durable facts are easier to teach than the chronology of papers.

First, upper-tail wage inequality rose strongly after 1980. Second, lower-tail dynamics were more time-specific: institutional changes and macro conditions matter more for the lower half of the distribution than a single smooth long-run trend would suggest [@autorKatzKearney2008]. Third, the college premium increased, but it did not fully summarize all relevant inequality changes. Fourth, occupational and task patterns look polarized rather than uniformly skill-upgraded in many subperiods, especially once middle routine work is separated from both low-wage service work and high-skill abstract work [@autorDorn2013; @acemogluAutor2011].

```{figure} assets/figures/08-polarization-schematic.png
:name: fig-week8-polarization
Stylized employment-share changes under polarization. The point is not the exact magnitudes but the pattern: relative decline in middle routine work together with stronger low- and high-end growth.
```

Figure {numref}`fig-week8-polarization` is useful because it keeps polarization distinct from a one-dimensional skill-premium story. A rising college premium and a hollowing out of middle routine work can be related, but they are not identical facts. This is why the mechanism discussion has to separate broad supply-demand logic from task reallocation and lower-tail institutions [@katzMurphy1992; @autorDorn2013].

Composition also matters. If the workforce becomes more educated, older, more female, more urban, or more concentrated in particular sectors, raw inequality changes may mix prices and quantities. The great contribution of reweighting and decomposition work was to show how composition-adjusted distributions can tell a cleaner story about changes in returns, institutions, and residual dispersion [@diNardoFortinLemieux1996; @firpoFortinLemieux2009].

### Mechanism block I: supply, demand, tasks, and technology

The cleanest starting point is still Katz-Murphy style supply-demand logic. If relative demand for skill rises faster than relative supply, the skill premium increases [@katzMurphy1992; @katzAutor1999]. That logic remains foundational because it ties Week 8 back to Week 4 human capital and Week 5 returns to skill. Workers differ in accumulated skill, firms demand bundles of tasks, and equilibrium prices adjust.

But that framework is not the end of the story. The task-based literature makes clear that technology can substitute more directly for routine middle tasks while complementing abstract tasks and leaving many low-wage service tasks less exposed to direct automation. This generates a pattern that looks less like a smooth rise in one latent skill price and more like distributional reshaping across occupations and tasks [@acemogluAutor2011; @autorDorn2013].

The right classroom discipline is to ask what each mechanism explains well. Supply-demand logic is strong on long-run skill premiums. Task-based logic is strong on middle compression and occupational reallocation. Neither one by itself explains every lower-tail movement, every firm pattern, or every place-based divergence.

### Mechanism block II: institutions and the lower tail

Lower-tail and middle-distribution movements are hard to read without institutions. Minimum wages, unions, bargaining norms, and wage-setting rules compress or decompress specific parts of the distribution rather than shifting all percentiles equally. This is one reason the lower tail is often more episodic and policy-sensitive than the persistent upper-tail rise [@diNardoFortinLemieux1996; @autorKatzKearney2008].

DiNardo, Fortin, and Lemieux provide the conceptual bridge here. Their counterfactual reweighting logic asks how the wage distribution would have looked under alternative compositions or institutional environments without requiring the researcher to pretend that one reduced-form coefficient summarizes the entire distribution [@diNardoFortinLemieux1996]. The field-course lesson is not just a method lesson. It is substantive: institutional explanations are often segment-specific. A fall in union coverage or a change in the minimum wage can matter a lot for {math}`p50-p10` while saying far less about the top tail.

That is why Week 8 should resist global narratives. Institutions can be central for the lower tail and still be incomplete as an explanation for upper-tail growth. Conversely, a technology-based account may fit upper-tail or middle reallocation facts and still leave the lower tail underexplained.

### Mechanism block III: firms, rents, sorting, and geography

The modern frontier added a new level of analysis: the employer. In linked employer-employee data, one can write

```{math}
:label: eq-week8-akm
\log w_{it} = \alpha_i + \psi_{J(i,t)} + X_{it}'\beta + \varepsilon_{it},
```

where {math}`\alpha_i` is a worker effect, {math}`\psi_{J(i,t)}` is the wage premium paid by the worker's firm, and {math}`X_{it}` captures observables. Equation {eq}`eq-week8-akm` is not the whole truth about wage setting, but it sharply organizes the question. How much inequality reflects persistent worker heterogeneity, how much reflects wage-setting differences across firms, and how much reflects positive sorting between high-wage workers and high-premium firms [@cardCardosoHeiningKline2018; @songPriceGuvenenBloomVonWachter2019]?

```{figure} assets/figures/08-inequality-component-decomposition.png
:name: fig-week8-decomposition
Conceptual stacked decomposition of wage-dispersion components. It visualizes the accounting distinction among between-group terms, within-group residual inequality, firm premia, and worker-firm sorting.
```

Figure {numref}`fig-week8-decomposition` helps because students can otherwise treat firm inequality as a separate topic rather than as a decomposition of worker outcomes. The firm block changed the field because it showed that between-firm pay dispersion and worker-firm sorting can account for a meaningful share of wage inequality. It also opened the door to place-based interpretations, since local labor markets differ in industry mix, firm composition, outside options, and rent-sharing environments [@cardCardosoHeiningKline2018; @songPriceGuvenenBloomVonWachter2019].

Geography enters naturally here. If high-premium firms cluster spatially, wage inequality becomes partly an allocation problem across places as well as across firms. This is not yet Week 10 mobility, but it is the bridge to it. Where workers live and which firms they can reach become part of the architecture of inequality.

### Welfare, total labor-market value, and the bridge from Week 7

Week 7's most important gift to Week 8 is skepticism about wages as a sufficient welfare statistic. A compact bridge object is

```{math}
:label: eq-week8-job-value
v_i = w_i + a_i,
```

where {math}`w_i` is wages and {math}`a_i` is the monetized value of amenities, schedule quality, stability, safety, or other nonwage job attributes. Equation {eq}`eq-week8-job-value` is deliberately spare. Its job is to stop students from unconsciously equating wage dispersion with inequality in labor-market opportunity sets.

```{figure} assets/figures/08-wage-vs-total-job-value.png
:name: fig-week8-value
Conceptual comparison of wage-only and total job-value rankings. Accounting for amenities can flatten, steepen, or reorder measured inequality depending on how nonwage job quality sorts across workers and firms.
```

Figure {numref}`fig-week8-value` shows why the bridge matters. If high-wage firms also offer safer conditions, more stable schedules, and lower risk, then inequality in total job value exceeds wage inequality. If some workers accept lower wages for flexibility or location, then wage inequality may overstate welfare inequality. Empirically, Week 8 still centers wages and earnings because those are far better observed than full job value. Conceptually, however, the Week 7 correction must remain in view [@cardCardosoHeiningKline2018].

## Research Lab

The bounded Week 8 lab is built around a local `Reproduce -> Diagnose -> Transfer` workflow that does not require restricted administrative data. The reproduction step uses a synthetic CPS-style file to recover a small inequality factbook in the spirit of [@autorKatzKearney2008]: percentile gaps, a college premium comparison, a between-versus-within decomposition, and a residual-inequality summary. This keeps the core inequality objects transparent and reproducible.

The diagnostic step asks students to separate descriptive decomposition from causal explanation. A rising residual component in Equation {eq}`eq-week8-residual` is not a stand-alone mechanism. Students must say what the residual may bundle together and which facts it helps discipline. The transfer step then moves to a synthetic linked employer-employee panel that supports a simple worker-firm decomposition in the spirit of [@cardCardosoHeiningKline2018] and [@songPriceGuvenenBloomVonWachter2019]. The aim is not to mimic confidential-data scale. It is to teach the logic of worker effects, firm premia, and sorting.

An optional extension note points students toward [@haanwinckel2025] for a broader synthesis of supply, firms, institutions, and the wage distribution. The bounded path stays deliberately local and pedagogical. It teaches the architecture of modern inequality analysis without pretending that a teaching dataset can replicate the entire administrative-data frontier.

Open research questions should remain visible:

1. Which parts of rising inequality are best understood as price changes versus allocation changes?
2. How robust are firm-premium decompositions to design choices, connected-set restrictions, and imperfect mobility?
3. When do amenities amplify wage inequality and when do they offset it?
4. Which inequality object is best for policy incidence when hours, employment, and household insurance move at the same time?
5. How should Week 9 discrimination work separate group-specific barriers from general dispersion in firms, tasks, and places?

## Methods Box

### Methods Box 1: distributional statistics and decomposition

Use Equation {eq}`eq-week8-quantiles` when the question is where in the distribution change occurs. Use Equation {eq}`eq-week8-between-within` when the question is how much inequality lives between observed groups versus within them. Use Equation {eq}`eq-week8-residual` when you need a compact descriptive accounting of what observables do and do not explain. The main discipline is to keep these objects descriptive unless the design truly identifies a causal counterfactual [@juhnMurphyPierce1993; @firpoFortinLemieux2009].

### Methods Box 2: linked employer-employee inequality methods

Equation {eq}`eq-week8-akm` is powerful because it makes firm heterogeneity explicit, but it needs panel mobility, a connected worker-firm graph, and careful interpretation. It is an accounting framework for worker effects, firm premia, and sorting. It is not automatically a model of bargaining, rents, monopsony, or welfare without further structure [@cardCardosoHeiningKline2018; @songPriceGuvenenBloomVonWachter2019].

```{include} assets/tables/08-empirical-toolkit-map.md
```

Table {numref}`tbl:ineq-toolkit-map` is the summary tool for the week. Each method answers a different inequality question, requires different data, and comes with a different limitation. Students should leave Week 8 knowing why papers that all study "inequality" can still be asking fundamentally different empirical questions.

```{include} assets/tables/08-mechanism-map.md
```

Table {numref}`tbl:ineq-mechanism-map` is the parallel mechanism summary. It prevents the lecture from collapsing into either a one-mechanism story or an unstructured list of facts.

## Reading Ladder And References

### Bridge

- Katz and Murphy on relative supply, relative demand, and wage structure [@katzMurphy1992]
- Juhn, Murphy, and Pierce on observed versus residual inequality [@juhnMurphyPierce1993]
- Autor, Katz, and Kearney for the field's compact map of upper-tail, lower-tail, and polarization facts [@autorKatzKearney2008]

### Field Core

- Katz and Autor on the broader wage-structure synthesis [@katzAutor1999]
- DiNardo, Fortin, and Lemieux on composition and institutional counterfactuals [@diNardoFortinLemieux1996]
- Lemieux on composition, residual inequality, and interpretation [@lemieux2006]
- Acemoglu and Autor on task-based technology and wage structure [@acemogluAutor2011]
- Autor and Dorn on task polarization and middle compression [@autorDorn2013]
- Firpo, Fortin, and Lemieux on distributional methods beyond means [@firpoFortinLemieux2009]

### Research Lab

- Card, Cardoso, Heining, and Kline on worker-firm heterogeneity and sorting [@cardCardosoHeiningKline2018]
- Song, Price, Guvenen, Bloom, von Wachter on firming-up inequality through firms and rents [@songPriceGuvenenBloomVonWachter2019]
- Haanwinckel as an optional frontier extension linking distributional mechanisms in a broader equilibrium frame [@haanwinckel2025]

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week8-quantiles` to explain why a rise in {math}`p90-p50` does not imply the same change in {math}`p50-p10`.
2. In Table {numref}`tbl:ineq-concepts-map`, which empirical object is best for a policy question about labor-force attachment, and which is best for a question about wage-setting? Why are they different?
3. Equation {eq}`eq-week8-between-within` is descriptive. Give one reason it is still highly informative for theory choice.
4. In Equation {eq}`eq-week8-residual`, why is it a mistake to interpret {math}`u_{it}` as a single structural force such as "technology"?
5. Compare the explanatory reach of Katz-Murphy style supply-demand logic and task-polarization logic. Which facts does each fit best?
6. Why can minimum wages or unions change {math}`p50-p10` more strongly than {math}`p90-p50`?
7. Use Equation {eq}`eq-week8-akm` to explain how firm premia and positive sorting can both raise wage inequality.
8. In Equation {eq}`eq-week8-job-value`, under what sorting pattern would total labor-market value inequality exceed wage inequality?
9. Why does Week 8 have to come before Week 9 discrimination and segmentation if the class wants to interpret group gaps carefully?

## Reproducibility And Code Lab Note

The Week 8 lab follows the standard bounded `Reproduce -> Diagnose -> Transfer` path. Students first build a synthetic inequality factbook in the spirit of [@autorKatzKearney2008], then diagnose what percentile gaps, between-within decompositions, and residual inequality do and do not identify, and finally transfer the workflow to a synthetic worker-firm decomposition in the spirit of [@cardCardosoHeiningKline2018] and [@songPriceGuvenenBloomVonWachter2019]. The bounded workflow is documented in [labs/08-inequality-and-wage-dispersion/lab.md](labs/08-inequality-and-wage-dispersion/lab.md).

## Slide Companion Note

The Week 8 deck should not reproduce the chapter verbatim. It should isolate the week's architecture: why the module is heavier than usual, how Weeks 5--7 feed into distributional analysis, which inequality objects matter, how percentile gaps differ from variance decompositions, why the lower tail and upper tail need not share a mechanism, what linked employer-employee data changed, and why Week 9 discrimination must be read against this broader inequality map. The canonical source is [slides/week8/08-inequality-and-wage-dispersion.tex](slides/week8/08-inequality-and-wage-dispersion.tex).

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
