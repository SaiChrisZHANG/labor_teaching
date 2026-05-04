---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Mobility, Migration, and Intergenerational Transmission

## Learning objectives

By the end of Week 10, students should be able to:

1. distinguish employer, occupation, place, and intergenerational mobility objects;
2. interpret transition matrices, hazard rates, rank-rank slopes, and wage-growth objects as distinct labor-market statistics;
3. explain how linked employer-employee data changed the study of worker mobility and firm sorting;
4. write down a migration-choice object with Roy-style selection and moving frictions;
5. explain what lottery, reform, border, and exposure designs identify in mobility and migration research;
6. distinguish descriptive persistence objects from causal transmission mechanisms in intergenerational mobility;
7. connect place, firm, and occupational mobility to inequality persistence rather than treating them as separate topics;
8. see why Week 11 worker-side policy is partly about relaxing mobility frictions rather than only changing static incentives.

The economic question for the week is dynamic but still labor-economic at its core. Once Week 9 has shown that workers may enter segmented opportunity sets, Week 10 asks how workers move across employers, occupations, and places, how much those moves raise wages or job quality, and why labor-market position still persists so strongly across families [@jiaMolloySmithWozniak2023; @songPriceGuvenenBloomVonWachter2019; @chettyHendrenKlineSaezTurner2014].

## Bridge

Week 9 ended with a deliberately uncomfortable point: the opportunity set through which workers search, move, and bargain may already be segmented by identity, firm behavior, and local opportunity. Week 10 keeps that insight but changes the question. Instead of asking whether treatment differs across workers at a point in time, we ask who moves, where they move, what those moves buy them, and why mobility is so uneven across firms, places, and generations.

This week matters because mobility has two opposing interpretations. In one interpretation, mobility is a margin of adjustment that reallocates labor toward better matches, higher-paying firms, and more productive places. In the other, mobility is precisely the margin that constraints suppress: moving is costly, information is incomplete, credit is limited, housing is scarce, and networks are unequal [@diamond2016; @kennanWalker2011; @vanDoornikGomesSchoenherrSkrastins2024]. A low mobility rate can therefore mean either stable good matches or trapped workers. The empirical task is to tell those stories apart.

Week 10 also bridges directly into Week 11. If workers do not move because credit, information, migration restrictions, or family background limit access to opportunity, then worker-side policy is not only about taxes and transfers. It is also about mobility margins: search assistance, moving support, migration access, training ladders, and place-sensitive policy design.

:::{admonition} Core Material
:class: tip
- mobility is multi-object: employer, occupation, place, and generation are different margins
- linked data improved both measurement and identification
- migration is an investment and selection problem, not only a geographic fact
- intergenerational persistence is descriptive until a design or mechanism isolates why it occurs
:::

:::{admonition} Optional Extension Block
:class: note
- career persistence and occupational ladders in the spirit of [@haeckLaliberte2025]
- measurement correction for employer-to-employer mobility in the spirit of [@fujitaMoscariniPostelVinay2024]
- place effects, skill sorting, and housing constraints in the spirit of [@diamond2016]
:::

## Field Core

### Mobility objects after Week 9: transitions, hazards, and wage growth

The first discipline is not to say "mobility" as if it were one number. Let {math}`Q_{it}` denote a worker's employer-premium quartile, occupation tier, or place type at time {math}`t`, and let {math}`M_{it}` indicate a move between {math}`t` and {math}`t+1`. A transition-matrix object is

```{math}
:label: eq-week10-transition
P_{jk} = \Pr(Q_{i,t+1}=k \mid Q_{it}=j, M_{it}=1).
```

Equation {eq}`eq-week10-transition` is descriptive but central. It tells us whether mobility is mostly lateral, upward, or downward. A hazard object,

```{math}
:label: eq-week10-hazard
h_{it} = \Pr(M_{it}=1 \mid X_{it}, Z_t),
```

asks which workers move, from which starting positions, and under which aggregate conditions. Neither object is causal by itself. Both are measurement devices that organize the dynamic allocation problem.

```{figure} assets/figures/10-employer-mobility-transition-heatmap.png
:name: fig-week10-transition
Transition matrices summarize where movers go, not just whether they move. The same employer-to-employer rate can hide very different patterns of upgrading, downgrading, and persistence across firm or occupation ladders.
```

The labor interpretation becomes sharper once wage growth is attached to the move. With linked employer-employee data, the field can study whether wage gains are tied to movement toward higher-premium firms, occupational upgrading, or better places rather than merely to generic turnover [@abowdKramarzMargolis1999; @cardHeiningKline2013; @engbomMoser2017]. A compact wage-growth object is

```{math}
:label: eq-week10-wage-growth
\Delta \log w_{i,t+1} = \alpha + \beta M_{it} + \gamma \big(\psi_{f_{i,t+1}} - \psi_{f_{it}}\big) + \varepsilon_{it},
```

where {math}`\psi_f` is the firm wage premium. Equation {eq}`eq-week10-wage-growth` is useful because it keeps the lecture labor-focused. A move matters when it changes a worker's position on a firm, occupation, or place ladder, not simply because the worker's address changed.

Measurement improved substantially once researchers stopped relying only on household surveys to count employer-to-employer flows. Survey nonresponse, multiple-job ambiguity, and timing error can make job-to-job mobility look flatter and less cyclical than it really is. Measurement-correction work using richer linked records therefore changed a first-order labor fact, not a technical footnote [@fujitaMoscariniPostelVinay2024].

```{figure} assets/figures/10-employer-mobility-measurement-correction.png
:name: fig-week10-measurement-correction
Correcting employer-to-employer mobility measurement can materially change the estimated level and cyclicality of reallocation. This is measurement progress, not a causal design.
```

```{include} assets/tables/10-mobility-objects-map.md
```

Table {numref}`tbl:week10-mobility-objects` is the organizing map for the week's first hour. It prevents the lecture from collapsing employer changes, occupation switches, migration, and intergenerational persistence into one undifferentiated mobility bucket.

### Migration as investment, sorting, and Roy-style selection

Migration is a labor-market choice because workers compare opportunity sets across locations. In Roy-style form, a worker moves when the best outside location dominates the current one after costs:

```{math}
:label: eq-week10-roy
M_i = \mathbf{1}\left\{\max_{d \in \mathcal{D}} \big(\mu_d + r_d s_i + a_{id}\big) - \big(\mu_o + r_o s_i + a_{io}\big) - \kappa_{iod} > 0\right\}.
```

In Equation {eq}`eq-week10-roy`, {math}`\mu_d` is the destination wage level, {math}`r_d` is the destination return to skill, {math}`s_i` is worker skill, {math}`a_{id}` is an idiosyncratic match or amenity component, and {math}`\kappa_{iod}` is the moving cost from origin {math}`o` to destination {math}`d`. The object is labor-economic because the decision depends on wage ladders, skill prices, and moving frictions, not only on geography [@roy1951; @borjas1987; @kennanWalker2011].

```{figure} assets/figures/10-migration-selection-schematic.png
:name: fig-week10-migration-selection
Migration responds to both average wage differences and differential returns to skill. Selection into moving is therefore informative about opportunity sets and moving costs at the same time.
```

This framework disciplines three common mistakes. First, gross migration rates alone do not reveal whether high-skill workers are sorting toward high-return places. Second, destination wage gains are not automatically causal because movers are selected. Third, place choice is not separable from labor demand, housing, and amenities. Diamond shows why skill groups sort differently across cities when wages, amenities, and housing costs move together [@diamond2016]. Jia, Molloy, Smith, and Wozniak show how much modern internal-migration research is really about labor-market adjustment under heterogeneous local conditions [@jiaMolloySmithWozniak2023].

### Worker mobility and sorting through firms and occupations

Labor economists increasingly ask not just whether workers move, but whether mobility helps them climb wage ladders across employers and occupations. Linked employer-employee panels make that possible because they observe both the worker and the destination firm. The field's move from cross-sections to matched panels is therefore a conceptual upgrade: mobility can now be analyzed as reallocation across heterogeneous firms rather than as unexplained residual turnover [@abowdKramarzMargolis1999; @cardHeiningKline2013; @songPriceGuvenenBloomVonWachter2019].

The core empirical lesson is that firms matter for inequality persistence. If high-income or well-connected workers are more likely to move into high-premium firms, then employer mobility becomes a transmission mechanism for inequality rather than a neutral churn margin. If mobility into better firms is restricted by search frictions, employer practices, or geographic immobility, then wage growth becomes path dependent. This is one reason Week 10 belongs after Week 8 inequality and Week 9 discrimination. Mobility is one channel through which earlier segmentation either relaxes or reproduces itself.

### Credit, information, and moving frictions

Moving is costly in a literal sense. Search, transport, deposits, licensing, temporary unemployment, and family disruption all create liquidity and risk problems. That is why a clean lottery object,

```{math}
:label: eq-week10-lottery
\tau^{move} = \mathbb{E}[M_i(1) - M_i(0)],
```

is so valuable. Equation {eq}`eq-week10-lottery` asks what happens to labor mobility when access to funds changes for reasons unrelated to workers' underlying mobility taste or local labor demand. In the credit-lottery setting of [@vanDoornikGomesSchoenherrSkrastins2024], identifying variation comes from quasi-random or randomized financial access rather than from observed mover outcomes alone.

The substantive labor lesson is broader than one paper. Credit frictions can suppress distant job search, reduce willingness to separate from bad current matches, and limit occupational experimentation. Information frictions do something similar even without cash constraints: workers may not know which firms or places offer wage ladders worth the move. Week 11 policy will inherit this logic when it asks whether worker-directed interventions should change incentives, information, or liquidity.

### Migration reforms, exposure designs, and labor-market reallocation

Migration also responds to institutional change. A compact exposure-design object is

```{math}
:label: eq-week10-exposure
Y_{rt} = \alpha_r + \delta_t + \beta \big(\text{Exposure}_r \times \text{Post}_t\big) + X_{rt}'\Gamma + \varepsilon_{rt},
```

where {math}`r` indexes region, firm, or worker-market exposure to a migration reform. Equation {eq}`eq-week10-exposure` is not a generic difference-in-differences template pasted onto a labor topic. It is the design logic behind research asking whether new migration access changes firm performance, worker outcomes, or reallocation margins where pre-reform exposure differs [@beerliRuffnerSiegenthalerPeri2021].

The identifying variation must always be stated explicitly. In Beerli, Ruffner, Siegenthaler, and Peri, the relevant variation comes from the abolition of immigration restrictions together with differential pre-reform exposure across firms and markets [@beerliRuffnerSiegenthalerPeri2021]. In Foged and Peri, quasi-random dispersal rules create local immigration exposure that is more plausibly exogenous than raw immigrant shares [@fogedPeri2016]. These designs identify reduced-form labor-market responses to migration access. They do not by themselves isolate one pure structural channel because local equilibrium effects, occupational upgrading, and firm responses all move together.

### Intergenerational mobility: rank-rank objects and persistence across families

The most common modern summary of intergenerational relative mobility is the rank-rank slope:

```{math}
:label: eq-week10-rank-rank
R_i^{child} = \alpha + \beta R_i^{parent} + u_i,
```

where parent and child positions are measured as percentile ranks in their respective income or earnings distributions. A high {math}`\beta` means stronger persistence and lower relative mobility. The rank-rank object became so influential because it is interpretable, robust to heavy-tailed income distributions, and well suited to administrative data with wide coverage [@chettyHendrenKlineSaezTurner2014; @acciariPoloViolante2022].

Transition matrices remain useful companions to Equation {eq}`eq-week10-rank-rank`. A rank-rank slope tells us about average persistence; a quintile transition matrix shows where in the distribution the barriers are tightest. That distinction matters in labor. Upward mobility from the bottom, persistence at the top, and place-specific middle-class stability are different policy and theory problems.

```{figure} assets/figures/10-rank-rank-transmission-schematic.png
:name: fig-week10-rank-rank
Rank-rank objects summarize persistence, while mediation objects ask which channels carry it. Linked parent-child data made both the descriptive map and the mechanism decomposition substantially more credible.
```

Linked parent-child administrative data changed the field in the same way linked employer-employee data changed worker mobility research. They reduce classical linkage error, expand geographic coverage, and let researchers map mobility across places and cohorts rather than inferring persistence from small samples [@chettyHendrenKlineSaezTurner2014; @abramitzkyBoustanJacomePerez2021; @acciariPoloViolante2022]. But the resulting objects are still descriptive until the researcher makes a mechanism claim.

```{include} assets/tables/10-transmission-map.md
```

Table {numref}`tbl:week10-transmission` lists the main labor-market transmission channels. The key teaching discipline is that "family background" is not itself a mechanism. Skills, occupations, firms, networks, places, information, and credit are mechanisms.

### From persistence to mechanism: decomposition and mediation

To move from persistence to mechanism, researchers often study how the parent-rank coefficient changes when a candidate mediator set is introduced:

```{math}
:label: eq-week10-mediation
R_i^{child} = \alpha + \beta R_i^{parent} + \theta' C_i + \eta_i,
\qquad
\Delta \beta_C = \beta - \tilde{\beta}_C.
```

Equation {eq}`eq-week10-mediation` is not magic causality. It is a disciplined decomposition: {math}`\Delta \beta_C` shows how much of the parent-rank association is statistically accounted for by channels such as occupation, career path, firm assignment, place, or schooling. Its value is organizational. Its limit is that post-treatment and joint-determination problems remain unless the mediator is itself identified.

That warning matters especially for occupational and career transmission. Haeck and Laliberte show that career structure can account for a meaningful share of intergenerational mobility differences, but the interpretation of a career mediation result still depends on why children enter those careers in the first place [@haeckLaliberte2025]. Was the driver skill acquisition, neighborhood exposure, licensing barriers, family firms, or information networks? Week 10 should train students to ask that mechanism question before reading a decomposition as a causal answer.

### Empirical progress: what the field learned to measure and identify better

Week 10 should explicitly teach empirical progress rather than presenting disconnected findings.

First, linked employer-employee data changed worker mobility from a turnover topic into a firm-sorting topic. Researchers can now separate worker and firm components of wage growth, trace employer-to-employer flows, and study how mobility changes access to high-paying firms [@abowdKramarzMargolis1999; @cardHeiningKline2013; @engbomMoser2017].

Second, linked parent-child administrative data changed intergenerational mobility from a small-sample correlation topic into a broad mapping exercise across cohorts, places, and family structures [@chettyHendrenKlineSaezTurner2014; @abramitzkyBoustanJacomePerez2021; @acciariPoloViolante2022].

Third, reform, border, and exposure designs improved migration identification by tying labor-market responses to institutional changes rather than to raw mover comparisons [@beerliRuffnerSiegenthalerPeri2021; @fogedPeri2016]. The identifying variation is not "movers versus stayers"; it is differential exposure to a plausibly exogenous change.

Fourth, lottery-style designs make moving frictions legible by shifting liquidity or access directly [@vanDoornikGomesSchoenherrSkrastins2024]. These designs are especially valuable because they speak to whether low mobility reflects preferences or constraints.

Fifth, measurement-correction work matters in its own right. The field improved because it asked whether basic mobility rates were even being measured correctly [@fujitaMoscariniPostelVinay2024].

Finally, rank-rank and transition-matrix approaches improved descriptive clarity. They made mobility patterns easy to compare across places and cohorts, but they must still be paired with mechanism or design work before becoming causal narratives.

```{include} assets/tables/10-methods-design-map.md
```

Table {numref}`tbl:week10-methods-designs` is the empirical roadmap for the week's second half. It tells students what each design family identifies well and where it remains vulnerable.

## Research Lab

The bounded Week 10 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure. The reproduction step uses synthetic teaching data in the spirit of [@vanDoornikGomesSchoenherrSkrastins2024] to estimate how randomized credit access changes moving, employer switching, and wage growth. The diagnostic step asks students to explain why this identifies the effect of relaxing a mobility friction rather than the full return to migration. The transfer step then turns to an exposure-design panel in the spirit of [@beerliRuffnerSiegenthalerPeri2021], where students estimate how a migration reform changes local reallocation and worker outcomes in high- versus low-exposure markets.

The local path is deliberately bounded. Students do not need restricted linked employer-employee records or tax-based parent-child data to learn the core logic of Week 10. Optional extensions point them toward [@haeckLaliberte2025] for careers and intergenerational persistence and [@fujitaMoscariniPostelVinay2024] for measurement correction in employer-to-employer mobility.

The frontier research questions should stay visible:

1. When is low mobility efficient persistence in good matches, and when is it trapped labor?
2. How much of wage growth after a move reflects destination-firm premia, occupation upgrading, or geographic arbitrage?
3. Which worker-side policies matter most when mobility is limited by credit, information, or housing?
4. How much of intergenerational persistence operates through firms, occupations, or places rather than schooling alone?
5. Which descriptive mobility objects are stable enough to guide policy, and which remain sensitive to measurement correction?

## Methods Box

### Methods Box 1: linked data and measurement correction

Equations {eq}`eq-week10-transition`, {eq}`eq-week10-hazard`, and {eq}`eq-week10-wage-growth` become much more informative once worker and employer records are linked. The gain is not just sample size. It is the ability to observe the destination margin. Measurement-correction work such as [@fujitaMoscariniPostelVinay2024] is part of the same empirical progression because mismeasured employer-to-employer flows distort the basic labor reallocation object before any causal design begins.

### Methods Box 2: descriptive mobility versus causal mobility

Equation {eq}`eq-week10-rank-rank` describes persistence. Equation {eq}`eq-week10-mediation` organizes potential channels. Equation {eq}`eq-week10-lottery` identifies the effect of relaxing one friction. Equation {eq}`eq-week10-exposure` identifies reduced-form responses to a reform with differential exposure. The field improves when students keep those objects separate rather than asking one estimator to answer every mobility question.

## Reading ladder

### Bridge

- Roy on self-selection as an earnings-distribution problem [@roy1951]
- Borjas on migrant self-selection [@borjas1987]
- Kennan and Walker on expected income and migration choice [@kennanWalker2011]
- Jia, Molloy, Smith, and Wozniak for a modern migration overview [@jiaMolloySmithWozniak2023]

### Field Core

- Abowd, Kramarz, and Margolis on worker and firm wage components [@abowdKramarzMargolis1999]
- Card, Heining, and Kline on workplace heterogeneity and inequality [@cardHeiningKline2013]
- Engbom and Moser on returns to education through access to higher-paying firms [@engbomMoser2017]
- Song, Price, Guvenen, Bloom, and von Wachter on firm-based inequality persistence [@songPriceGuvenenBloomVonWachter2019]
- Beerli, Ruffner, Siegenthaler, and Peri on migration reform and labor-market performance [@beerliRuffnerSiegenthalerPeri2021]
- Foged and Peri on immigrant exposure and native worker adjustment [@fogedPeri2016]
- Chetty, Hendren, Kline, Saez, and Turner on modern intergenerational mobility measurement [@chettyHendrenKlineSaezTurner2014]

### Research Lab

- Van Doornik, Gomes, Schoenherr, and Skrastins on credit lotteries and labor mobility [@vanDoornikGomesSchoenherrSkrastins2024]
- Fujita, Moscarini, and Postel-Vinay on measuring employer-to-employer reallocation [@fujitaMoscariniPostelVinay2024]
- Abramitzky, Boustan, Jacome, and Perez on intergenerational mobility of immigrants [@abramitzkyBoustanJacomePerez2021]
- Acciari, Polo, and Violante on intergenerational mobility in Italy [@acciariPoloViolante2022]
- Haeck and Laliberte on careers and intergenerational mobility [@haeckLaliberte2025]
- Diamond on skill sorting across places [@diamond2016]

## Exercises / discussion prompts

1. Why is a transition matrix like Equation {eq}`eq-week10-transition` not a causal mobility estimate by itself?
2. What labor-market question does the hazard object in Equation {eq}`eq-week10-hazard` answer that a transition matrix does not?
3. In Equation {eq}`eq-week10-wage-growth`, what does the firm-premium term add beyond a generic mover indicator?
4. Use Equation {eq}`eq-week10-roy` to explain why destination wage gains among movers need not equal the average treatment effect of moving.
5. Why can a low migration rate reflect either efficient stability or severe moving frictions?
6. What is the identifying variation in a credit-lottery design like Equation {eq}`eq-week10-lottery`?
7. What is the identifying variation in an exposure design like Equation {eq}`eq-week10-exposure`?
8. Why are rank-rank slopes and quintile transition matrices complements rather than substitutes?
9. What does Equation {eq}`eq-week10-mediation` teach well, and what does it fail to identify on its own?
10. How do Week 8 inequality and Week 9 discrimination change the way we should interpret Week 10 mobility evidence?
11. Which worker-side policies in Week 11 would be most promising if mobility is mainly constrained by credit rather than by preferences?

## Reproducibility or code lab note

The Week 10 lab uses a bounded local workflow rather than restricted employer-employee or administrative tax data. Students first reproduce lottery-based mobility effects from a synthetic dataset in the spirit of [@vanDoornikGomesSchoenherrSkrastins2024], then diagnose the identifying margin, and finally transfer the workflow to a migration-reform exposure design in the spirit of [@beerliRuffnerSiegenthalerPeri2021]. The student-facing workflow is documented in [labs/10-mobility-migration-intergenerational-transmission/lab.md](labs/10-mobility-migration-intergenerational-transmission/lab.md).

## Slide companion note

The Week 10 deck should define mobility as a set of labor-market objects rather than as a single migration statistic. It should bridge directly from Week 9 segmentation, show transition, wage-growth, and rank-rank objects, explain Roy-style migration choice and moving frictions, isolate the logic of lottery and exposure designs, and end by making Week 11 policy look like the study of which frictions are relaxable. The canonical source is [slides/week10/10-mobility-migration-intergenerational-transmission.tex](slides/week10/10-mobility-migration-intergenerational-transmission.tex).
