---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Human Capital and Skill Formation

## Learning objectives

By the end of Week 4, students should be able to:

1. write the human-capital investment problem as a dynamic tradeoff between current foregone earnings and future productivity;
2. interpret a Ben-Porath-style law of motion and relate it to lifecycle wage profiles;
3. distinguish schooling, employer training, learning-by-doing, and early-childhood investment as different accumulation margins;
4. explain why general training can be firm financed in imperfect labor markets;
5. define self-productivity and dynamic complementarity and connect them to labor-market inequality;
6. map reduced-form, experimental, and structural evidence into the human-capital framework;
7. explain how finance, information, and policy frictions distort investment choices and why that matters for Week 5 returns-to-skill evidence.

The economic question for the week is direct: if Week 3 treated labor supply as a timing problem given productive capacity, where does productive capacity itself come from, and why does its accumulation generate lifecycle wage growth and inequality?

## Bridge

Week 3 asked how workers shift labor across time when wages, taxes, and constraints vary over the life cycle. Week 4 takes one step back. Wages are not only prices that workers face. They are also outcomes of past investments in schooling, training, experience, and early-life environments. Once that is clear, observed age-earnings profiles stop looking like exogenous schedules and start looking like endogenous accumulation objects [@becker1962; @benPorath1967; @mincer1974].

The organizing idea is simple. Human capital is a productive state variable. Building it requires time, goods, attention, or foregone work today, but it raises future productivity. Schooling is one version of that tradeoff, early-career training is another, and parental investment in childhood is an earlier-life version of the same logic. The common structure is dynamic investment, even when the institutional details differ sharply across ages and settings [@becker1964; @heckman2006].

### A compact benchmark

Let {math}`h_t` denote productive human capital at age {math}`t`, and let {math}`i_t` denote current investment effort. A compact Ben-Porath-style law of motion is

```{math}
:label: eq-week4-law
h_{t+1} = (1-\delta_h) h_t + A_t i_t^{\alpha},
\qquad 0 < \alpha < 1.
```

Equation {eq}`eq-week4-law` says that human capital is cumulative, depreciates slowly, and rises with current investment. The crucial timing implication is immediate: the value of investing at age 20 is larger than the value of investing at age 55 because the remaining horizon over which higher productivity pays off is longer [@benPorath1967].

To connect the state variable to labor-market outcomes, let observed wages satisfy

```{math}
:label: eq-week4-wage
w_t = r_t h_t,
\qquad
\log w_t = \log r_t + \log h_t.
```

Equation {eq}`eq-week4-wage` makes the Week 4 to Week 5 bridge explicit. Wage growth can come from accumulation in {math}`h_t`, from changes in the price of skill {math}`r_t`, or from both. Week 5 will ask how wages map productivity into earnings in equilibrium. Week 4 asks how productive capacity reaches the market in the first place [@mincer1974; @willisRosen1979].

```{figure} assets/figures/04-lifecycle-human-capital-earnings.png
:name: fig-week4-lifecycle
Conceptual lifecycle profiles for latent human capital and observed earnings. The human-capital profile rises early because investment is intense when the remaining work horizon is long. Observed earnings continue to grow even as investment slows because the stock of skill remains high and its market price may continue to improve. The figure is schematic but organized around the logic in @benPorath1967 and @mincer1974.
```

Figure {numref}`fig-week4-lifecycle` is the shortest visual route from Week 3 to Week 4. The worker is no longer only choosing hours over time. The worker is also shaping future wages. That is why lifecycle labor supply and human-capital accumulation are complements rather than separate chapters.

:::{admonition} Core Material
:class: tip
- Ben-Porath accumulation and the lifecycle wage profile
- Schooling versus training as different investment margins
- General versus specific training under imperfect labor markets
- Self-productivity and dynamic complementarity
- Empirical design map and the main frictions
:::

:::{admonition} Optional Extension Block
:class: note
- deeper production-function estimation in the spirit of [@attanasioEtAl2020HumanCapital]
- credit constraints, schooling finance, and limited commitment in the spirit of [@lochnerMongeNaranjo2011]
:::

## Field Core

### Ben-Porath and the investment tradeoff

The cleanest way to see the Week 4 logic is to put current production and current investment in tension. If one unit of time can be spent working or accumulating skill, current earnings become the opportunity cost of investment. A reduced-form first-order condition can be written as

```{math}
:label: eq-week4-foc
\text{MC}_t(i_t)
=
\beta \, \mathbb{E}_t
\left[
\sum_{s=t+1}^{T}
\beta^{s-t-1}
\frac{\partial w_s}{\partial h_s}
\frac{\partial h_s}{\partial i_t}
\right].
```

Equation {eq}`eq-week4-foc` is deliberately compact. The left-hand side is the current marginal cost of investment, which includes foregone earnings, tuition, effort, and other inputs. The right-hand side is the discounted marginal value of the extra future wages generated by a higher human-capital stock. The remaining horizon matters because it scales the number of future periods over which the gain is realized [@becker1962; @benPorath1967].

That condition explains three broad facts. First, investment is front-loaded over the life cycle. Second, observed wages can rise with age even when explicit schooling has ended, because post-school experience and training continue to raise {math}`h_t`. Third, late-career wage flattening need not mean the worker stops learning entirely; it often means the shadow value of additional investment has fallen relative to its current cost [@mincer1974; @becker1964].

```{figure} assets/figures/04-investment-intensity-lifecycle.png
:name: fig-week4-investment
Stylized lifecycle investment intensity by accumulation margin. Formal schooling is front-loaded, employer training peaks early in the career, and learning-by-doing remains positive but modest later in life. The purpose is to visualize the foregone-earnings logic implied by Equation {eq}`eq-week4-foc`.
```

Figure {numref}`fig-week4-investment` helps keep the margins distinct. Schooling is the high-intensity, high-foregone-earnings phase. Training is often concentrated in the early career when firms and workers are still building productive matches. Learning-by-doing remains present later, but the investment share of time is lower.

### Schooling, college, and training as distinct margins

The standard error in teaching human capital is to treat years of schooling as the whole subject. Schooling is only one accumulation margin. Postsecondary sorting, job ladders, employer training, and task assignment are also mechanisms through which skill stocks evolve. Table {numref}`tbl:human-capital-taxonomy` is useful because it separates margins by inputs, timing, and the policy or friction most likely to distort them.

```{include} assets/tables/04-human-capital-taxonomy.md
```

Willis and Rosen are the right bridge from pure theory to labor-market heterogeneity because schooling choices reflect both returns and selection [@willisRosen1979]. Students do not face one common return schedule. They differ in preparation, credit access, information, and the occupations available conditional on completion. That is one reason Week 5 must separate observed wage gaps from causal returns to skill.

Training requires a second distinction: general versus specific human capital. In the frictionless Becker benchmark, firms should not finance transferable general training because workers can leave and capture the return elsewhere [@becker1964]. Yet general training is observed in real labor markets. Acemoglu and Pischke show why imperfect labor markets change the result: wage compression, search frictions, and limited outside options can let firms capture enough of the return to invest even in skills with broader market value [@acemogluPischke1999]. Autor makes the same point in an applied setting where intermediaries provide skills that are not perfectly specific to one employer [@autor2001].

The larger lesson is that training incidence is an incomplete proxy for human-capital investment. Workers can invest through low-wage apprenticeships, job-task progression, career mobility, or occupation-specific experience without labeling any of it “training” in survey data. Human-capital measurement therefore inherits the Week 1 problem of mapping latent productive objects into imperfect observed variables.

### Skill formation before labor-market entry

The Ben-Porath benchmark is powerful, but it is not enough if the production technology changes over childhood. A compact early-life skill-production function is

```{math}
:label: eq-week4-skill
\theta_{t+1} = f_t(\theta_t, I_t, P_t),
```

where {math}`\theta_t` is current skill, {math}`I_t` is investment, and {math}`P_t` summarizes parental time, quality, or environment. Equation {eq}`eq-week4-skill` broadens Equation {eq}`eq-week4-law` in two ways. It allows the technology to vary by developmental stage, and it makes the family an active producer of future labor-market capacity [@cunhaHeckman2007; @cunhaHeckman2008].

Two concepts organize the literature. Self-productivity means higher current skill raises future skill directly, even holding later inputs fixed. Dynamic complementarity means the marginal payoff to later investment is larger when earlier skill is higher. Together they explain why early disadvantage can persist and why the same late intervention may have different returns across children [@heckman2006; @cunhaHeckmanSchennach2010].

```{figure} assets/figures/04-dynamic-complementarity.png
:name: fig-week4-complementarity
Dynamic complementarity schematic. Later investment has a larger effect on next-period skill when baseline skill is already higher. The figure makes the interaction term intuitive without pretending that a single heatmap captures the full production function estimated in the early-childhood literature.
```

Figure {numref}`fig-week4-complementarity` clarifies why the early-childhood literature belongs inside labor economics rather than beside it. If early inputs change the slope of later investment returns, then childhood environments affect wages, employment, occupation choice, and inequality far downstream. The labor-market consequences are delayed, but the economic object is still productive capacity.

### Frictions, finance, and policy distortions

The frictionless optimum implied by Equations {eq}`eq-week4-law` through {eq}`eq-week4-foc` is rarely observed directly. Families may be borrowing constrained, schools may be unequally matched, workers may not know returns or program eligibility, and firms may underinvest when turnover is high or contracting is limited. Those distortions matter for both efficiency and inequality because high-return investments can be missed precisely where baseline resources are low [@lochnerMongeNaranjo2011; @deming2022].

Credit constraints are the cleanest formal extension. If tuition or early-childhood inputs must be financed before returns are realized, limited commitment or missing insurance can flatten investment gradients for high-ability but low-wealth individuals. Lochner and Monge-Naranjo show that the relevant friction is not a generic liquidity shortage but the joint structure of collateral, repayment, and the timing of returns [@lochnerMongeNaranjo2011]. In teaching terms, the key point is that schooling choice is an intertemporal finance problem, not only a taste-for-schooling problem.

Information frictions matter as well. Students and parents may misperceive returns, deadlines, or program quality. Policy therefore affects human capital not only through subsidies, but also through disclosure, advising, default rules, and support for completing complex application steps. That is why reduced-form effects of the same nominal subsidy can vary across settings even when the engineering cost of schooling is unchanged [@deming2022].

### What empirical designs identify

The Week 4 evidence is easiest to organize by design rather than by age or by paper chronology.

```{include} assets/tables/04-design-map.md
```

Table {numref}`tbl:human-capital-design-map` highlights a recurring identification issue. Most reduced-form designs identify the effect of one extra unit of schooling, one intervention, or one shift in financing at a particular margin. They do not identify the full technology in Equation {eq}`eq-week4-skill` without stronger structure. That is why the randomized intervention evidence and the structural production-function evidence should be seen as complements rather than competitors.

Angrist and Chen use draft-lottery variation to identify an extra-schooling margin induced by military service policy, which is useful precisely because it isolates one incentive shift rather than the full schooling problem [@angristChen2011]. Walters studies variation in Head Start inputs and shows that program impacts depend on center quality and input composition, which is informative about which margins inside the black box appear most productive [@walters2015]. Attanasio and coauthors go further by estimating a production function directly in a randomized setting, using measured parental investments to recover deeper parameters about self-productivity and complementarity [@attanasioEtAl2020HumanCapital].

The research reading should therefore stay disciplined about what each paper learns. Draft-lottery or aid designs are powerful for causal returns on a narrow schooling margin. Randomized early-childhood interventions identify bundled changes in inputs. Structural production-function work recovers more of the technology but pays for that scope with stronger assumptions. The right design choice depends on whether the target is a treatment effect, a production parameter, or a policy counterfactual.

### Bridge to Week 5

Week 4 does not say that wages equal skill one-for-one in data. Equation {eq}`eq-week4-wage` is a useful accounting bridge, not a complete wage-setting theory. Week 5 will relax the idea that the price of skill {math}`r_t` is exogenous and show how sorting, selection, and wage-setting institutions shape the measured return to human capital. The payoff from doing Week 4 first is that students can then separate two questions cleanly:

1. how skill is accumulated;
2. how markets price the skill that has been accumulated.

## Research Lab

The frontier challenge is no longer whether human capital matters. It is whether the relevant production margin is schooling, training, parental investment, job tasks, or finance, and whether the evidence identifies treatment effects or technology parameters. The modern literature has moved away from one-dimensional “years of education” thinking toward dynamic input systems in which timing, complementarities, and frictions interact [@cunhaHeckman2007; @attanasioEtAl2020HumanCapital].

That shift creates genuine research opportunities. How portable are production-function estimates across countries, cohorts, or delivery systems? When do employer-side frictions dominate family-side frictions? Which observed inputs proxy well for latent investments, and which merely co-move with them? The answer matters for labor economics because the eventual outcomes are labor-market objects: wages, employment, task content, promotion paths, and inequality.

The course lab reflects that research agenda in a bounded way. Students reproduce one local synthetic treatment-effect contrast in the spirit of [@attanasioEtAl2020HumanCapital], diagnose what that reduced-form contrast does and does not reveal about Equation {eq}`eq-week4-skill`, and then transfer the workflow to a quality-heterogeneity setting in the spirit of [@walters2015]. The optional instructor extension uses [@lochnerMongeNaranjo2011] to show how schooling finance changes the same underlying investment problem.

## Methods Box

Week 4 adds one discipline to the dynamic toolkit from Week 3: always separate the production technology from the pricing equation.

1. Write the law of motion for skill and identify the current investment margin.
2. State the current opportunity cost of investment explicitly, including foregone earnings where relevant.
3. Decide whether the evidence identifies a treatment effect on later outcomes, an input response, or a technology parameter.
4. Ask whether the distortion comes from finance, information, institutions, or imperfect labor markets.
5. Keep Equations {eq}`eq-week4-law`, {eq}`eq-week4-wage`, {eq}`eq-week4-foc`, and {eq}`eq-week4-skill` conceptually distinct before interpreting a wage return as a pure productivity return.

## Reading ladder

### Bridge

- Becker's original human-capital investment logic [@becker1962]
- Ben-Porath on lifecycle earnings as the outcome of human-capital production [@benPorath1967]
- Mincer on schooling, experience, and earnings profiles [@mincer1974]

### Field Core

- Willis and Rosen on schooling choice and selection [@willisRosen1979]
- Acemoglu and Pischke on why firms may finance general training in imperfect labor markets [@acemogluPischke1999]
- Autor on temporary-help firms and transferable skill provision [@autor2001]
- Cunha and Heckman on the technology of skill formation [@cunhaHeckman2007; @cunhaHeckman2008]
- Heckman on investing in disadvantaged children as a labor-market inequality question [@heckman2006]

### Research Lab

- Cunha, Heckman, and Schennach on estimating the skill-production technology [@cunhaHeckmanSchennach2010]
- Attanasio and coauthors on production-function estimation in a randomized intervention [@attanasioEtAl2020HumanCapital]
- Walters on input composition in Head Start [@walters2015]
- Heckman, Pinto, and Savelyev on mechanisms linking early intervention to adult outcomes [@heckmanPintoSavelyev2013]
- Lochner and Monge-Naranjo on schooling finance and credit constraints [@lochnerMongeNaranjo2011]
- Deming on why information, institutions, and market design still matter for human-capital investment [@deming2022]

## Exercises / discussion prompts

1. Use Equations {eq}`eq-week4-law` and {eq}`eq-week4-foc` to explain why the same subsidy can raise schooling sharply at age 18 but have a much smaller effect on training at age 45.
2. Figure {numref}`fig-week4-lifecycle` shows earnings rising after investment intensity has already started to decline. Why is that pattern consistent with the Ben-Porath benchmark?
3. What is the cleanest economic difference between general training in Becker's frictionless benchmark and in the imperfect-labor-market environment of Acemoglu and Pischke?
4. In Equation {eq}`eq-week4-skill`, which parameter or derivative best captures dynamic complementarity, and what policy implication follows from it?
5. Pick one row from Table {numref}`tbl:human-capital-design-map` and explain what object it identifies well and what object it cannot identify without stronger assumptions.
6. Why is Week 4 a necessary prerequisite for interpreting Week 5 returns-to-skill estimates?

## Reproducibility or code lab note

The Week 4 lab is organized around a bounded synthetic teaching path that mirrors the logic of [@attanasioEtAl2020HumanCapital] without requiring restricted or heavyweight external files. Students reproduce one treatment-induced investment and endline-skill contrast using the local synthetic dataset, diagnose what that contrast reveals about Equation {eq}`eq-week4-skill`, and then transfer the workflow to a center-quality heterogeneity exercise in the spirit of [@walters2015]. A short optional instructor extension connects the same investment problem to schooling finance using [@lochnerMongeNaranjo2011]. The bounded path and smoke test are documented in [labs/04-human-capital-skill-formation/lab.md](labs/04-human-capital-skill-formation/lab.md).

## Slide companion note

The Week 4 deck should isolate the accumulation problem, the lifecycle figures, the schooling-versus-training distinction, the self-productivity logic, the empirical design map, the main frictions, and the Week 5 bridge rather than reproducing the chapter. The canonical source is [slides/week4/04-human-capital-skill-formation.tex](slides/week4/04-human-capital-skill-formation.tex).
