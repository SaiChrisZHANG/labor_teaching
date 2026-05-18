---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Wage Posting, Bargaining, and Wage-Setting

## Learning Objectives

By the end of Week 5, students should be able to:

1. explain why a search model is incomplete until it specifies how wages are set;
2. distinguish posted wages, individualized bargaining, standardized pay rules, and collective or administrative wage-setting;
3. explain how search frictions generate wage dispersion, job ladders, and retention pressure even among similar workers;
4. separate reservation wages, outside offers, the value of nonemployment, and bargaining threat points;
5. connect wage-setting protocols to rent-sharing, pass-through, and firm wage premia without collapsing those objects together;
6. evaluate empirical evidence by naming the identifying variation, observed unit, observed margin, and the key latent object left unresolved;
7. connect Week 4 search models to Week 6 monopsony and labor market power.

## Opening Orientation

The economic question for Week 5 is central to Labor II: once a worker and a firm meet in a frictional labor market, what protocol converts match surplus into pay, and how can we tell in the data whether the relevant protocol is posting, bargaining, a standardized wage rule, or something in between [@burdettMortensen1998; @hallMilgrom2008; @mortensen2003]?

:::{admonition} Core materials
:class: tip
- wage-setting protocols convert match surplus into pay in frictional labor markets
- posted wages, bargaining, standardized pay, and discretionary pay are distinct regimes
- outside offers, the value of nonemployment, and retention pressure shape wages differently
- empirical wage-setting evidence identifies protocols and margins rather than a generic wage equation
- Week 5 is the bridge from search theory to monopsony and labor market power
:::

## Bridge

Week 4 taught students to think in terms of meetings, hazards, separations, and job ladders. But a meeting technology does not by itself determine wages. Once outside options, employed search, and retention pressure exist, the wage is no longer an anonymous competitive parameter. It becomes the outcome of a wage-setting protocol: a posted wage, a bargained wage, a rule-based schedule, or a pay outcome constrained by internal or institutional norms.

The bridge back to Week 4 is therefore precise. Search theory gave us unemployment-to-employment hazards, employment-to-employment mobility, and vacancy-filling congestion. Week 5 asks how those same flow objects discipline the wage each match receives. The bridge forward to Week 6 is equally precise. Week 5 is about the protocol that maps surplus into wages. Week 6 is about the elasticity and conduct environment in which that protocol operates.

```{figure} assets/figures/05-wage-setting-course-map.png
:name: fig-lii-w5-course-map
Week 5 sits between search and monopsony. It converts worker flows and outside options into wage-setting protocols, then turns those protocols into empirical wage objects.
```

Figure {numref}`fig-lii-w5-course-map` is the course repositioning figure for the week. Wage-setting is the bridge from search as a mobility theory to later topics such as labor market power, policy incidence, and firm wage premia.

### Why search models need a wage-setting protocol

Under a competitive benchmark, the wage is the market-clearing price of labor and identical workers in identical jobs should not exhibit persistent wage dispersion once relevant amenities and productivity are held fixed. That benchmark is analytically useful, but it is not a sufficient description of the frictional labor market students saw in Week 4. If offers arrive sequentially, vacancies take time to fill, employed workers receive outside opportunities, and firms worry about retention, then identical matches need not pay identical wages [@mortensen2003].

The acceptance problem is already enough to see the break from the competitive benchmark:

```{math}
:label: eq-lii-w5-acceptance
w \geq w^R
\quad \Leftrightarrow \quad
V^E(w) \geq V^U.
```

Equation {eq}`eq-lii-w5-acceptance` says that employment is accepted when the value of the job at wage {math}`w` exceeds the value of nonemployment {math}`V^U`. This is only an acceptance object. It is not yet a posting object, a bargaining object, or a standardized wage rule. That distinction is the organizing logic of the entire week.

```{include} assets/tables/05-wage-setting-regimes-map.md
```

Table {numref}`tbl:wage-setting-regimes-week5` is the opening taxonomy. It is useful because it says exactly what is endogenous in each regime. Under posting, the firm chooses a wage schedule while anticipating recruiting or retention responses. Under bargaining, the wage is a joint outcome. Under standardized pay, the match does not fully customize the wage at all. Under discretionary pay, managerial choice or local bargaining may matter even inside a large firm.

## Field Core

### Competitive wages versus frictional wage setting

The clean benchmark contrast is this: in a competitive model, labor supply to a single firm is effectively infinitely elastic at the market wage, so a given firm does not need a separate wage-setting problem. In a frictional setting, labor supply to the firm is shaped by search, turnover, and outside options. Wages therefore depend on how the firm recruits and retains workers, how the worker can leave, and whether internal wage rules compress or decentralize pay.

That is why Week 5 treats "wage-setting" as a protocol for converting surplus into pay rather than as a synonym for "the wage equation." Two jobs can face the same product market and the same production technology yet pay differently because the wage-setting protocol differs. A salary schedule, a take-it-or-leave-it posted wage, and a bilateral negotiation do not load the same information into wages.

### Wage posting, search, and the logic of wage dispersion

The canonical posted-wage object begins with a firm choosing compensation while anticipating how recruiting and retention respond:

```{math}
:label: eq-lii-w5-posting
\max_w \; \pi(w) = (p - w)\,\ell(w),
```

where {math}`p` is match productivity and {math}`\ell(w)` is the labor supply or staffing response induced by the posted wage. Equation {eq}`eq-lii-w5-posting` is the basic logic behind wage posting: the firm picks a wage because the wage changes both profits per worker and the probability of attracting and keeping workers [@burdettMortensen1998].

```{figure} assets/figures/05-posting-vs-bargaining.png
:name: fig-lii-w5-posting-bargaining
Posted wages and individualized bargaining solve different economic problems. Posting makes the wage part of the firm's recruiting strategy, while bargaining makes it part of a bilateral surplus-splitting protocol.
```

In the Burdett--Mortensen logic, on-the-job search means some firms post higher wages to retain workers who can otherwise climb the job ladder. Wage dispersion then need not signal only heterogeneous productivity. It can reflect equilibrium wage-setting in a frictional market with employed search, poaching, and retention [@burdettMortensen1998; @mortensen2003]. The posted wage object is therefore not just an offer level. It is also a recruiting and retention policy.

This is the first place to connect directly back to Week 4. Job ladders create a worker-side mobility option even when an observed outside offer is not in hand. That is why a posted-wage equilibrium can generate persistent wage dispersion and systematic quit patterns without requiring a fresh bilateral negotiation in every match.

[@lachowskaMasSaggioWoodbury2022] is especially useful here because it asks whether wage changes in one job transmit to another job held by the same worker. The identifying variation comes from shocks to compensation in a worker's secondary job. The unit of observation is the dual-jobholder spell. The observed margins are primary-job wage responses and separations. The key latent object is the full menu of unobserved offers and employer responses available to the worker. That makes the paper ideal for Week 5: it is explicit about the difference between a posting prediction and a bargaining prediction.

### Bargaining, outside options, and the Hall--Milgrom critique

The bilateral bargaining benchmark shifts the wage from a one-sided posting choice to a joint surplus-splitting problem:

```{math}
:label: eq-lii-w5-bargaining
w^* = \arg\max_w \left[V^E(w)-V^U\right]^\beta \left[J(w)-V\right]^{1-\beta},
```

where {math}`\beta` summarizes worker bargaining power, {math}`V^E(w)-V^U` is the worker surplus from employment, and {math}`J(w)-V` is the firm's continuation surplus. Equation {eq}`eq-lii-w5-bargaining` is deliberately compact, but it makes clear that the wage is no longer chosen only by the firm.

```{include} assets/tables/05-bargaining-objects-and-observables.md
```

Table {numref}`tbl:bargaining-objects-week5` is essential because the Week 5 vocabulary is often misused. A reservation wage is an acceptance cutoff. An outside offer is a realized alternative. The value of nonemployment is a fallback-value object. A threat point is protocol-specific: it depends on what happens if bargaining breaks down or is delayed. These are not interchangeable terms.

Hall and Milgrom's contribution is exactly to challenge the idea that the relevant threat point is always immediate exit into unemployment. If bargaining can break down into delay rather than permanent separation, the link between unemployment conditions and wages can be weaker than a simple outside-option interpretation suggests [@hallMilgrom2008]. That matters for comparative statics and for empirical interpretation. A weak reduced-form link between unemployment and wages does not by itself imply that outside options are irrelevant. It may instead imply that the bargaining protocol is different.

### Wages and the value of nonemployment

Week 5 also needs a careful section on a modern empirical object that students often conflate with observed outside offers:

```{math}
:label: eq-lii-w5-nonemployment-pass
\Delta \log w_{it} = \rho \, \Delta \log V^U_{it} + \varepsilon_{it}.
```

Equation {eq}`eq-lii-w5-nonemployment-pass` asks how much an exogenous change in the value of nonemployment passes through to wages. The object {math}`V^U` is more primitive than a realized competing offer. It includes benefits, expectations, search conditions, and other determinants of the worker's fallback value.

```{figure} assets/figures/05-outside-options-and-wage-setting.png
:name: fig-lii-w5-outside-options
Week 5 separates the value of nonemployment, realized outside offers, reservation wages, and bargaining threat points. Empirically, these objects are related but not identical.
```

[@jaegerSchoeferYoungZweimueller2020] is the field-core empirical anchor because the paper names the object explicitly. The identifying variation comes from quasi-experimental shifts in fallback values. The unit of observation is the worker or worker-firm relationship. The observed margin is wage pass-through. The key latent object is the full dynamic opportunity set facing the worker, including any unobserved offers and beliefs about future search. This is exactly why the paper belongs in Week 5 rather than only in a policy week: it teaches students to separate the value of nonemployment from a realized outside offer.

Week 5 should also be explicit that pass-through from outside-option shocks and pass-through from firm shocks are different empirical questions. A wage response to more generous nonemployment benefits is not the same object as a wage response to higher firm value added. The first speaks to fallback values. The second speaks to rent-sharing. Conflating the two makes later monopsony discussions much less clear.

### Standardized versus discretionary wage-setting inside firms

The interior of the firm matters because many large employers do not bargain from scratch for every job. Some use grades, steps, internal equity rules, or occupation-level pay cells. Others leave more room for manager discretion, individualized offers, or responses to outside bids.

```{figure} assets/figures/05-standardized-vs-discretionary-pay.png
:name: fig-lii-w5-standardized-discretionary
Standardized pay compresses wages within job cells and makes progression more transparent. Discretionary pay leaves more room for bargaining, local managerial choice, and within-cell inequality.
```

[@massenkoffWilmers2023] is a good empirical bridge because it studies the decline of standardized pay rates and links that decline to wage stagnation and changing within-firm wage-setting practices. The identifying variation comes from changes in observed rate structures over time. The unit of observation is the occupation-establishment or worker-job cell. The observed margins include the prevalence of standardized rates, wage compression, and within-cell dispersion. The key latent object is the informal discretion that may coexist with formal schedules. [@biasi2021] adds a policy-relevant version of the same logic: teacher labor markets reveal how salary schedules and flexible pay generate different sorting and staffing outcomes, with school districts or teachers as the observed units and the nonwage job bundle still partly latent.

The main Week 5 lesson is not that one regime is universally better. It is that the wage rule itself is a substantive economic object. Standardization can compress wages and limit within-job bargaining. Discretion can facilitate targeted retention and local adaptation, but it can also amplify inequality and obscure the wage-setting protocol that students are trying to identify.

### Empirical designs and what they identify

```{include} assets/tables/05-identification-and-pass-through-map.md
```

Table {numref}`tbl:identification-pass-through-week5` should organize the empirical lecture by design family rather than by chronology.

Dual-jobholder or revealed-preference tests use wage shifts in a secondary job or in a realized outside opportunity. The unit is the worker-job spell. The observed margin is whether wages respond in-place or whether separation is the main adjustment margin. The hardest latent object is the full offer set the worker faces, not only the realized second job. That is why [@lachowskaMasSaggioWoodbury2022] is informative but not fully structural.

Policy or institutional reforms to pay rules use contract expirations, salary-schedule changes, or flexibility reforms. The unit may be the worker, school district, or establishment. The observed margins are wage compression, mobility, sorting, and composition. The hardest latent object is the set of simultaneously changing nonwage conditions. [@biasi2021] is especially useful because the pay rule changes are clear while amenities and mission differences remain important.

Outside-option or nonemployment-value designs use shocks to benefits, eligibility, or fallback values. The unit is typically the worker or worker-firm match. The observed margin is wage pass-through, mobility, or retention. The hardest latent object is the full counterfactual search environment that the worker expects.

Matched worker-firm designs with firm shocks use variation in value added, productivity, demand, or revenues. The unit is the worker-firm relationship. The observed margin is wage pass-through, firm wage premia, or rent-sharing. The hardest latent object is how much of the wage effect reflects sorting, match quality, or changing composition. [@cardCardosoHeiningKline2018] and [@rudanko2023] are the natural anchors here because they separate firm wage premia, wage dispersion, and frictional wage setting without claiming that reduced-form pass-through by itself fully identifies the protocol.

Survey and establishment-by-occupation evidence on wage rules or bargaining protocols can say much more about what firms report doing, but it remains difficult to map self-reports one-to-one into structural primitives. [@caldwellHaegeleHeining2025] is a useful frontier anchor precisely because bargaining intensity, wage inequality, and protocol heterogeneity are likely to coexist inside the same labor market.

### Rent-sharing, pass-through, and the bridge to market power

The firm-side pass-through object that bridges Week 5 to Week 6 can be written compactly as

```{math}
:label: eq-lii-w5-rentshare
\Delta \log w_{ijt} = \theta \, \Delta \log \mathrm{VA}_{jt} + \alpha_i + \psi_j + \varepsilon_{ijt}.
```

Equation {eq}`eq-lii-w5-rentshare` treats wage-setting as the transmission of a firm-side shock into pay. The object {math}`\theta` is not a complete structural wage-setting parameter. It is a reduced-form pass-through object whose interpretation depends on sorting, bargaining, internal wage rules, and the elasticity of labor supply to the firm [@cardCardosoHeiningKline2018; @rudanko2023].

```{figure} assets/figures/05-rent-sharing-pass-through.png
:name: fig-lii-w5-rent-sharing
Pass-through depends on which shock moves the problem. Wage responses to firm-side surplus shocks and wage responses to outside-option shocks are related but distinct empirical objects.
```

This is the key bridge to Week 6. Week 5 says that posted wages, bargaining, and wage rules determine how a given match responds to opportunities and shocks. Week 6 will ask how much conduct power firms have because workers do not face perfectly elastic labor supply. The two weeks are complements. Wage posting and bargaining are protocols; monopsony is about the labor-supply and conduct environment in which those protocols operate.

## Research Lab

The optional extension block for Week 5 should feel like a research workshop on wage-setting heterogeneity, not a miscellaneous appendix. One strong line of inquiry asks how worker beliefs about outside options shape bargaining and retention. A second asks how within-firm inequality changes when more pay is discretionary rather than standardized. A third asks how pay transparency, salary-history restrictions, or algorithmic offer management reshape the mapping from outside options to wages. A fourth asks how measured pass-through interacts with monopsony metrics once the firm's labor supply curve is not infinitely elastic [@massenkoffWilmers2023; @rudanko2023; @caldwellHaegeleHeining2025].

[@bhullerMoeneMogstadVestad2022] is useful for the frontier discussion because it reminds students that collective bargaining and coordinated wage-setting are not merely policy add-ons. They are alternative wage-setting protocols that can compress pay, reshape outside options, and change what a bargaining or pass-through estimate means. The extension block should therefore ask students to name the data opportunity, the identifying variation, the observed margin, and the unresolved latent object in any frontier paper they read.

The bounded Week 5 lab follows `Reproduce -> Diagnose -> Transfer`. The reproduction anchor is [@lachowskaMasSaggioWoodbury2022], where the protocol under test is posting versus bargaining and the key observed margin is whether a wage shock in one job changes wages or separations in another job held by the same worker. The transfer anchor is [@massenkoffWilmers2023], where the protocol under study is a wage-rule change from standardized to less standardized pay, and the key observed margin is compression versus dispersion within comparable job cells. [@biasi2021] is the optional extension because public teacher salary schedules make it easier to transfer the same logic to open data.

## Methods Box

Week 5 only works if the objects stay separate.

1. Posted wages versus individualized bargaining versus standardized wage schedules: these are different protocols, not interchangeable labels for "the wage."
2. Reservation wages versus outside offers versus the value of nonemployment: an acceptance cutoff, a realized alternative, and a fallback value are not the same object.
3. Worker outside options versus bargaining threat points: the relevant disagreement payoff depends on the bargaining protocol, especially once Hall--Milgrom-style delay is allowed.
4. Pass-through from firm shocks versus pass-through from outside-option shocks: both are wage responses, but they move different primitives.
5. Firm wage premia versus worker sorting versus match-specific rents: a firm effect in matched data is not automatically a pure bargaining or monopsony parameter.
6. Reduced-form rent-sharing evidence versus structural wage-setting interpretation: pass-through estimates discipline theory, but they do not on their own reveal the entire protocol or all equilibrium spillovers.
7. Evidence without design language is not enough: every empirical result in this week should be reported with the identifying variation, unit of observation, observed margin, and most important latent object.

## Reading Ladder And References

### Required / field core

- [@burdettMortensen1998] for wage posting, job ladders, and equilibrium wage dispersion.
- [@hallMilgrom2008] for why bargaining protocol assumptions matter and why delay can weaken the unemployment-wage link.
- [@jaegerSchoeferYoungZweimueller2020] for the value of nonemployment as a wage-setting object.
- [@lachowskaMasSaggioWoodbury2022] for a direct empirical test of posting versus bargaining using dual jobholders.

### Strong empirical complements

- [@massenkoffWilmers2023] for standardized versus discretionary pay-setting inside firms.
- [@biasi2021] for salary schedules, flexible pay, and worker sorting in teacher labor markets.
- [@cardCardosoHeiningKline2018] for firm wage premia, inequality, and the limits of a purely worker-side wage interpretation.

### Optional / frontier / bridge to Week 6

- [@mortensen2003] for the broader frictional wage-setting perspective.
- [@rudanko2023] for firm wages in a frictional labor market and the bridge to market power.
- [@bhullerMoeneMogstadVestad2022] for collective bargaining as a wage-setting protocol rather than an institutional afterthought.
- [@caldwellHaegeleHeining2025] for frontier work on bargaining and inequality.

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-lii-w5-acceptance` to explain why a reservation wage is not the same thing as a realized outside offer.
2. Compare Equations {eq}`eq-lii-w5-posting` and {eq}`eq-lii-w5-bargaining`. Which margins move if the worker receives a stronger outside option under each protocol?
3. Why does Hall--Milgrom imply that a weak empirical unemployment-wage gradient need not mean that wage-setting is purely rigid?
4. In [@lachowskaMasSaggioWoodbury2022], what varies, what unit is observed, what margin is observed, and what key wage-setting object remains latent?
5. In [@jaegerSchoeferYoungZweimueller2020], why is the value of nonemployment conceptually more primitive than an observed outside offer?
6. Use Figure {numref}`fig-lii-w5-standardized-discretionary` to explain how standardized and discretionary pay regimes could produce different within-job wage distributions even with similar workers.
7. Why does Equation {eq}`eq-lii-w5-rentshare` not by itself reveal whether observed wage pass-through reflects bargaining, firm wage premia, or match-specific rents?
8. Propose one transfer design using a public teacher salary schedule dataset, a public contract dataset, or a small synthetic offer-and-separation panel. Name the observed unit, the observed margin, and the main latent object.

## Reproducibility And Code Lab Note

The Week 5 lab is built around `Reproduce -> Diagnose -> Transfer`. The bounded reproduction path uses a local synthetic dual-jobholder panel inspired by [@lachowskaMasSaggioWoodbury2022] so students can measure whether an outside wage shock primarily changes incumbent wages or separations. The diagnose step forces students to say whether the paper is testing posting or bargaining, what the observed outside-option margin is, what the main identification challenge is, and what remains latent. The transfer step then uses a synthetic wage-rule panel anchored to [@massenkoffWilmers2023] so students can compare standardized and discretionary pay compression, while [@biasi2021] is the optional extension to public teacher salary schedules. The local handout lives at [labs/05-wage-posting-bargaining-and-wage-setting/lab.md](labs/05-wage-posting-bargaining-and-wage-setting/lab.md).

## Slide Companion Note

The slide deck at [slides/week5/05-wage-posting-bargaining-and-wage-setting.tex](slides/week5/05-wage-posting-bargaining-and-wage-setting.tex) should stay tighter than the chapter. It should cover the central question and course repositioning, the Week 4 to Week 5 bridge, why search models need a wage-setting protocol, wage posting and dispersion, bargaining and Hall--Milgrom, wages and the value of nonemployment, standardized versus discretionary pay-setting, empirical designs and what they identify, rent-sharing and pass-through, the frontier extension block, and the bridge to Week 6 monopsony.

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
