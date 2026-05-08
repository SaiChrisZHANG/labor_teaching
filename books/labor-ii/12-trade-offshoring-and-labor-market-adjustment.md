---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Trade, Offshoring, and Labor Market Adjustment

## Learning objectives

By the end of Week 12, students should be able to:

1. distinguish import competition, export exposure, offshoring, input-cost, and structural-change channels as separate trade shocks to labor markets;
2. construct and interpret a local labor-market trade-exposure object without confusing place-level exposure with worker-level treatment;
3. explain how trade shocks can move wages, employment, unemployment, nonparticipation, sector shares, and welfare over different horizons;
4. separate short-run displacement from long-run reallocation, and worker adjustment from place adjustment;
5. explain why manufacturing-to-service transition evidence is not the same as incumbent manufacturing workers smoothly switching sectors;
6. interpret empirical trade papers by naming the identifying variation, unit of observation, observed labor margin, and key offstage equilibrium margin;
7. connect reduced-form local-exposure evidence to structural and dynamic equilibrium approaches;
8. bridge Week 11 technology shocks to Week 12 trade shocks and bridge forward to Week 13 synthesis.

The economic question for Week 12 is explicit: how do trade and offshoring shocks transmit through workers, firms, sectors, and places, and what determines dislocation, reallocation, and welfare?

## Bridge

Week 11 treated technology as a shock generated inside production: automation changes tasks, firm organization, and worker adaptation from within the production process. Week 12 keeps the same labor-market objects onstage, but the shock now comes from outside the local production unit. Trade changes relative prices, competitive pressure, export opportunities, imported-input access, and the location of production across firms, sectors, and places.

That is why this week should not collapse into either a generic trade lecture or a single import-competition narrative. The labor-economics question is how an external product-market shock propagates through the mechanisms students already know from Labor II:

1. labor demand and scale effects from Weeks 1 and 2;
2. turnover, search, and unemployment from Week 4;
3. wage-setting and bargaining from Week 5;
4. monopsony and mobility frictions from Week 6;
5. regulation, insurance, and incidence from Weeks 7 through 9;
6. dynamic adjustment and reallocation from Weeks 10 and 11.

```{include} assets/tables/12-trade-channels-map.md
```

Table {numref}`tbl:trade-channels-map` is the opening discipline for the week. It keeps trade labor-focused by separating import competition, export expansion, offshoring, input-cost effects, structural change, and local reallocation rather than treating all of them as one undifferentiated globalization shock.

```{figure} assets/figures/12-trade-channels-framework.png
:name: fig-lii-w12-channel-framework
Week 12 organizes trade shocks as a channel map. Relative-price changes can move import competition, export demand, offshoring, input access, firm selection, and sectoral composition at the same time, but each channel reaches workers through different labor-market margins.
```

Figure {numref}`fig-lii-w12-channel-framework` previews the lecture structure. The key move is to map sectoral price and trade-cost changes into worker, firm, and place outcomes before making welfare statements.

:::{admonition} Core Material
:class: tip
- trade shocks reach labor markets through distinct channels such as import competition, export demand, offshoring, and input access
- worker, firm, and place adjustment are different objects that can move on different horizons
- local exposure is not the same object as worker-level treatment
- structural change and welfare require more discipline than one reduced-form coefficient
- Week 12 connects Labor II shock analysis to long-run reallocation
:::

:::{admonition} Optional Extension Block
:class: note
- broader frontier questions are surfaced later in the chapter under `Global evidence and frontier directions`
:::

## Field Core

### Trade as a labor-market shock

Trade shocks are not primitive labor shocks. They typically begin with changes in tariffs, foreign productivity, transportation costs, exchange rates, or supply-chain integration, and only then show up as labor-market shocks through firms, sectors, and places. That is why the same trade shock can look like plant contraction in one setting, export-led hiring in another, offshoring-driven task reorganization in a third, and service-sector expansion somewhere else [@autorDornHanson2013ChinaSyndrome; @dixCarneiroKovak2017TradeLiberalizationRegionalDynamics; @feenstraHanson1999OutsourcingHighTechnologyWages].

The week therefore turns on three linked objects.

1. Channels through which trade affects labor markets.
2. Transition margins through which workers and places adjust.
3. Welfare and research questions that require stronger structure than a single local reduced-form coefficient.

### Formal core: exposure, outcomes, structural change, dynamics, and welfare

The most common reduced-form organizing object is a local exposure measure:

```{math}
:label: eq:trade_exposure
\text{Exposure}_r = \sum_s \omega_{rs,0}\,\Delta \text{TradeShock}_s
```

where {math}`\omega_{rs,0}` is a baseline sector-share weight for region {math}`r` and {math}`\Delta \text{TradeShock}_s` is a sector-level change in import competition, tariffs, export demand, or offshoring exposure. Equation {eq}`eq:trade_exposure` is deliberately broad. When the unit is a commuting zone, {math}`\omega_{rs,0}` is often an initial employment share. When the unit is a worker, it may be a lagged industry attachment. When the unit is a firm, it may be a sales or input share. The treatment object changes with the unit.

The reduced-form labor outcome equation is then

```{math}
:label: eq:trade_labor_outcome
\Delta y_r = \beta \,\text{Exposure}_r + X_r'\Gamma + \varepsilon_r
```

where {math}`y_r` could be local employment, wages, unemployment, nonparticipation, earnings losses, sector shares, or migration. Equation {eq}`eq:trade_labor_outcome` is useful because it forces students to ask what the observed labor-market margin actually is before interpreting {math}`\beta`.

To make structural change explicit, the lecture needs a two-sector manufacturing-services object:

```{math}
:label: eq:structural_change
\Delta \log \frac{L_M}{L_S}
=
\underbrace{\eta_p \,\Delta \log \frac{P_M}{P_S}}_{\text{relative-price effect}}
+
\underbrace{\eta_y \,\Delta \log Y}_{\text{income / expenditure effect}}
+
\underbrace{\eta_a \,\Delta \log \frac{A_M}{A_S}}_{\text{productivity / task effect}}
```

Equation {eq}`eq:structural_change` is not a complete equilibrium model. It is a guide for interpreting why trade shocks can change manufacturing employment shares, service employment growth, and the skill premium at the same time [@cravinoSotelo2019TradeInducedStructuralChange]. A fall in relative manufacturing prices, changes in expenditure patterns as income changes, and productivity differences across sectors can all push labor away from manufacturing and toward services, but the labor-market consequences depend on who moves and how slowly.

Dynamic adjustment requires a separate object:

```{math}
:label: eq:trade_event_study
y_{rt+h} - y_{rt-1}
=
\sum_{h \in \mathcal{H}} \beta_h \,\text{Exposure}_{r}
+ X_{rt}'\Gamma_h + \varepsilon_{rt+h}
```

where the horizon-specific coefficients {math}`\beta_h` distinguish short-run displacement from medium-run and long-run adjustment. This is the key empirical bridge from local exposure papers to dynamic regional and worker-level evidence [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics; @kovakMorrow2025LongRunCUSFTA].

Finally, the week needs a worker-versus-place welfare accounting object:

```{math}
:label: eq:trade_welfare
\Delta W =
\sum_i \pi_i \,\Delta \text{RealIncome}_i
- \sum_i \text{TransitionCost}_i
- \sum_r \text{PlaceAdjustmentCost}_r
```

Equation {eq}`eq:trade_welfare` makes the non-negotiable point. Worker losses, place losses, and aggregate gains are not the same object. Place-level employment decline does not automatically reveal individual lifetime losses, and aggregate welfare claims require more structure than a local reduced-form coefficient [@kimVogel2021TradeShocksLaborMarketAdjustment; @caliendoDvorkinParro2019TradeLaborMarketDynamics].

### Local exposure measures and what they identify

The local-labor-market exposure design is the canonical reduced-form entry point. [@autorDornHanson2013ChinaSyndrome] maps national import growth from China into commuting-zone exposure using pre-period industrial composition. The identifying variation is differential baseline sector mix across commuting zones interacted with national industry exposure. The unit of observation is the commuting zone. The observed labor margins are manufacturing employment, broader employment, wages, unemployment, and nonparticipation. The key offstage margin is national equilibrium adjustment through prices, migration, firm entry and exit, and demand spillovers.

[@pierceSchott2016SurprisinglySwiftDecline] complements that local design by using U.S. policy variation tied to Permanent Normal Trade Relations. The identifying variation is industry exposure to policy uncertainty resolution around China trade integration. The unit of observation is the industry. The observed margin is manufacturing employment decline. The key offstage margins are local service offsets, worker transitions, and broader equilibrium pass-through.

The immediate lesson is that local import competition estimates identify place-level incidence under heterogeneous exposure, not a full welfare object. They are indispensable for labor incidence, but they are not a sufficient statistic for aggregate gains from trade.

```{figure} assets/figures/12-trade-welfare-and-reallocation.png
:name: fig-lii-w12-welfare-reallocation
Trade shocks move labor outcomes through short-run displacement, slower sectoral reallocation, migration, entry, and firm adjustment. Local reduced-form estimates are strongest on exposed margins, while welfare conclusions require additional structure on transition costs and reallocation.
```

Figure {numref}`fig-lii-w12-welfare-reallocation` is the warning label for the local design. It clarifies why import competition, export expansion, offshoring, and reallocation can all be active even when a paper estimates one dominant reduced-form coefficient.

### U.S. import competition: the China shock and local labor-market adjustment

The China-shock literature is the natural first empirical block because it makes the commuting-zone exposure logic transparent. In [@autorDornHanson2013ChinaSyndrome], rising Chinese import competition is associated with lower manufacturing employment, lower labor-force participation, and weaker wage outcomes in more exposed commuting zones. The design identifies place effects. It does not directly identify the lifetime loss of a particular worker, and it does not by itself recover equilibrium consumer gains or input-cost offsets.

[@pierceSchott2016SurprisinglySwiftDecline] sharpens the institutional narrative by linking the manufacturing decline to the policy environment around China trade rather than only to import-penetration accounting. That is useful in Labor II because it shows how trade transmission depends on firm exit, industry restructuring, and labor reallocation, not merely on a static demand curve.

The major methods lesson is the distinction between a trade channel and a labor margin.

1. Import competition is the channel.
2. Employment, wages, unemployment, and nonparticipation are the observed margins.
3. Migration, worker retraining, and sector switching are major offstage margins.
4. Aggregate welfare cannot be read directly off a commuting-zone coefficient.

### Dynamic regional adjustment: Brazil and horizon effects

[@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics] is the key dynamic-adjustment section for the course. The identifying variation is differential regional exposure to Brazil's tariff reform through pre-liberalization industrial composition. The unit of observation is the region over time. The observed margins include employment structure, earnings, and regional adjustment trajectories over long horizons. The crucial insight is that adjustment is not instantaneous. Regional labor markets can continue adjusting for many years after the initial tariff shock.

That dynamic perspective matters for three reasons. First, early local losses need not reveal long-run reallocation. Second, persistence itself is a labor-market fact that requires explanation: mobility frictions, slow sectoral entry, and imperfect worker transition all matter. Third, long-run place recovery does not imply that initially exposed workers are fully insured.

```{figure} assets/figures/12-trade-adjustment-worker-vs-place.png
:name: fig-lii-w12-worker-place
Worker and place adjustment can diverge sharply after trade shocks. Places can exhibit long persistence because migration, firm entry, and service growth are slow, while incumbent workers may experience displacement, delayed transitions, or exit from the labor force.
```

Figure {numref}`fig-lii-w12-worker-place` shows why Labor II needs both worker and place language. Place-level persistence does not reveal whether incumbent workers stay and lose, move and recover, or exit altogether.

### Manufacturing-to-service transitions and who actually adjusts

Trade-induced structural change is often summarized as manufacturing decline plus service growth, but that summary is too coarse for labor economics. The real question is how service growth happens and for whom. [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany] provides the core teaching object here. The identifying variation comes from differential German exposure to trade with Eastern Europe and China. The units of observation include regions and workers. The observed margins include manufacturing employment decline, service employment growth, and heterogeneity across adjustment margins. The key contribution is that service reallocation does not simply consist of incumbent manufacturing workers moving smoothly into service jobs.

```{include} assets/tables/12-structural-change-and-transition-map.md
```

Table {numref}`tbl:trade-structural-change-transition-map` keeps the transition margins separate: manufacturing-to-services, incumbent versus entrant or returnee margins, short-run displacement, long-run adjustment, and the link to skill and structural change.

```{figure} assets/figures/12-trade-structural-change-transitions.png
:name: fig-lii-w12-structural-change
Manufacturing-to-service transitions can occur through several margins at once: incumbent worker moves, new entrants, returnees, migration, and sectoral entry. Observed service growth after trade shocks should not be narrated as frictionless worker reallocation.
```

Figure {numref}`fig-lii-w12-structural-change` makes the non-negotiable point for the week: sectoral reallocation is not the same as incumbent-worker transition. That matters for both welfare and policy because entrants, returnees, and local service expansion can mask persistent losses for displaced manufacturing workers.

### Trade-induced structural change and inequality

[@cravinoSotelo2019TradeInducedStructuralChange] links trade to the skill premium through the structural-change channel rather than through a narrow import-competition narrative. The identifying object comes from a structured quantitative framework using cross-country differences in sectoral composition, trade, and expenditure responses. The unit of analysis is the country-sector equilibrium. The observed and inferred margins are sector shares, relative wages, and the skill premium. The key offstage labor margin in simpler reduced-form work is the expenditure and general-equilibrium side of the adjustment.

This is where Equation {eq}`eq:structural_change` earns its place. Trade can move labor demand not only by shrinking exposed manufacturing sectors, but also by changing relative prices, expenditure shares, and productivity in ways that alter the size and skill intensity of services. That is why manufacturing decline after trade integration need not map mechanically into one simple inequality story.

### Offshoring and services trade are distinct channels

Offshoring belongs in the week as its own transmission mechanism. [@feenstraHanson1999OutsourcingHighTechnologyWages] studies outsourcing and high-technology capital as linked forces affecting wages in the United States. The identifying variation is industry-level change in outsourcing intensity and capital use. The unit of observation is the industry. The observed margin is wages and relative demand. The key offstage margins are local equilibrium spillovers, worker transitions, and service-side reorganization.

The labor takeaway is not historical nostalgia about outsourcing. It is conceptual separation. Final-goods import competition, offshoring of production stages, imported business services, and cheaper intermediates do not identify the same labor-market object. Offshoring can change within-firm organization, task composition, and skill demand even when local import competition is modest.

### Worker versus place adjustment, welfare, and structured equilibrium

The week should now step beyond reduced-form place effects. [@kimVogel2021TradeShocksLaborMarketAdjustment] gives a tractable labor-market adjustment framework that connects trade shocks to unemployment, nonparticipation, and reallocation frictions. The identifying object is structural discipline rather than one single instrument. The units of analysis are workers, sectors, and markets embedded in equilibrium. The contribution is to clarify which margins must be modeled if we want to move from local incidence to welfare and policy.

[@caliendoDvorkinParro2019TradeLaborMarketDynamics] pushes further by bringing dynamic labor-market adjustment into a quantitative trade setting. The unit is an equilibrium economy with worker mobility and search frictions. The contribution is not to replace reduced-form evidence, but to show what must be added to interpret the transition path, unemployment risk, and welfare consequences of trade shocks. These frameworks are especially useful once students ask whether consumer gains, imported-input gains, and worker losses can coexist. The answer is yes, and the coexistence is precisely why local employment losses are not the same object as aggregate welfare.

### Global evidence and frontier directions

Week 12 should not end with a U.S.-only story. The contrast across the United States, Brazil, Germany, and cross-country structural-change frameworks shows that institutions, worker mobility, entry margins, and sector mix shape adjustment [@autorDornHanson2013ChinaSyndrome; @dixCarneiroKovak2017TradeLiberalizationRegionalDynamics; @dauthFindeisenSuedekum2017TradeManufacturingJobsGermany; @cravinoSotelo2019TradeInducedStructuralChange].

```{include} assets/tables/12-global-evidence-and-frontier-map.md
```

Table {numref}`tbl:trade-global-frontier-map` organizes the global evidence and frontier agenda: local U.S. place effects, Brazilian dynamic adjustment, German structural change, quantitative trade-and-labor frameworks, global structural change, and the move toward long-run worker panels.

```{figure} assets/figures/12-trade-global-evidence-and-frontiers.png
:name: fig-lii-w12-global-frontier
The current frontier moves from short-run place-level coefficients toward linked worker, firm, and regional adjustment paths across countries. Import and export asymmetries, service-sector transitions, and long-run trajectories are increasingly central.
```

The frontier section should be concrete rather than generic.

1. People versus places: long-run worker tracking is changing how the literature thinks about persistent local decline and recovery [@kovakMorrow2025LongRunCUSFTA].
2. Structural change into services: service growth after trade shocks often depends heavily on entrant, returnee, and local-entry margins rather than only incumbent worker switching [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany].
3. Import versus export asymmetry: import competition and export access can move labor markets in opposite directions and on different horizons [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics; @kovakMorrow2025LongRunCUSFTA].
4. Offshoring and white-collar fragmentation: services trade and imported tasks remain conceptually distinct from final-goods import competition [@feenstraHanson1999OutsourcingHighTechnologyWages].
5. Welfare and policy: local reduced-form evidence is crucial for incidence, but worker insurance, place policy, and aggregate evaluation require stronger equilibrium structure [@kimVogel2021TradeShocksLaborMarketAdjustment; @caliendoDvorkinParro2019TradeLaborMarketDynamics].

### Bridge to Week 13

Week 12 completes the major shock-and-adjustment block of Labor II. Week 11 asked how labor markets adjust when production technology changes from inside firms. Week 12 asked how labor markets adjust when product-market integration and global production fragmentation change relative prices and exposure from outside the firm. Week 13 can then synthesize the semester by asking how firm behavior, frictions, institutions, and shocks fit into one coherent labor-market research framework.

## Research Lab

The Week 12 lab follows the standard `Reproduce -> Diagnose -> Transfer` design and keeps the bounded student path fully local. The primary anchor is [@autorDornHanson2013ChinaSyndrome], where students build a small commuting-zone trade-exposure object and track place-level employment, unemployment, and nonparticipation margins. The challenge anchor is [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics], which turns the discussion from one-period incidence to multi-period adjustment. The optional extension anchor is [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany], which brings structural change and entry margins into the interpretation.

The local handout lives at [labs/12-trade-offshoring-and-labor-market-adjustment/lab.md](labs/12-trade-offshoring-and-labor-market-adjustment/lab.md). The key discipline is to force students to name the trade channel, the treatment object, the observed labor margin, and the key reallocation margin before they interpret any result.

## Methods Box

Keep these distinctions explicit throughout the week.

1. Import competition versus export exposure: they are different channels and need not offset symmetrically [@autorDornHanson2013ChinaSyndrome; @dixCarneiroKovak2017TradeLiberalizationRegionalDynamics].
2. Goods trade versus offshoring or services trade: imported final goods, imported intermediates, and fragmented tasks are not the same treatment object [@feenstraHanson1999OutsourcingHighTechnologyWages].
3. Worker-level, firm-level, and place-level treatment: baseline shares, sector attachment, and exposure objects change with the unit.
4. Short-run displacement versus long-run adjustment: event-time coefficients, dynamic regional evidence, and long-run worker panels answer different questions [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics; @kovakMorrow2025LongRunCUSFTA].
5. Incumbents versus entrants and returnees: sectoral service growth can occur without incumbent manufacturing workers being the ones who move [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany].
6. Reduced-form Bartik or tariff-exposure designs versus structural equilibrium approaches: each is informative, but they identify different objects [@autorDornHanson2013ChinaSyndrome; @caliendoDvorkinParro2019TradeLaborMarketDynamics].
7. Local labor-market outcomes versus aggregate welfare statements: local incidence is not the same object as national gains or losses [@kimVogel2021TradeShocksLaborMarketAdjustment].
8. Place effects versus worker losses: a region can partially recover even if initially displaced workers bear persistent losses, and worker recovery need not imply place recovery [@kovakMorrow2025LongRunCUSFTA].

## Reading ladder

### Ladder A. Core channel map and local exposure logic

- [@autorDornHanson2013ChinaSyndrome]
- [@pierceSchott2016SurprisinglySwiftDecline]
- [@feenstraHanson1999OutsourcingHighTechnologyWages]

### Ladder B. Dynamic adjustment and structural change

- [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics]
- [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany]
- [@cravinoSotelo2019TradeInducedStructuralChange]

### Ladder C. Welfare and equilibrium frameworks

- [@kimVogel2021TradeShocksLaborMarketAdjustment]
- [@caliendoDvorkinParro2019TradeLaborMarketDynamics]

### Ladder D. Long-run worker trajectories and frontier directions

- [@kovakMorrow2025LongRunCUSFTA]
- Optional revisit: [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany]

## Exercises / discussion prompts

1. Use Equations {eq}`eq:trade_exposure` and {eq}`eq:trade_labor_outcome` to explain why a commuting-zone import-exposure estimate is a place-level object rather than a worker-level treatment effect.
2. Why can import competition, export exposure, and offshoring generate different wage effects even when they all originate from trade integration?
3. Use Equation {eq}`eq:structural_change` to give two reasons why manufacturing-to-service transition after a trade shock need not imply incumbent-worker recovery.
4. Compare [@autorDornHanson2013ChinaSyndrome] and [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics]. What is the identifying variation, unit of observation, observed labor margin, and key offstage equilibrium margin in each paper?
5. Why is [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany] especially useful for distinguishing place reallocation from incumbent-worker transitions?
6. What additional assumptions or structure do [@kimVogel2021TradeShocksLaborMarketAdjustment] and [@caliendoDvorkinParro2019TradeLaborMarketDynamics] add before one can make welfare or policy statements?
7. Suppose a region loses manufacturing employment after an import shock but gains service employment later. What outcomes would you still need to observe before concluding that workers were fully insured?

## Reproducibility or code lab note

The bounded Week 12 lab is fully local and synthetic. Students first reproduce a compact China-syndrome-style commuting-zone exposure object and recover its relationship to manufacturing employment, unemployment, and nonparticipation. They then diagnose why that design identifies place effects rather than worker welfare. The transfer exercise asks them to carry the same exposure idea into a bounded structural-change setting by comparing manufacturing-share decline, service-share growth, and unemployment under a small synthetic region-year panel inspired by [@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics]. The optional extension asks them to reinterpret the same transition logic through the manufacturing-to-service evidence in [@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany].

## Slide companion note

The Week 12 slide deck lives at [slides/week12/12-trade-offshoring-and-labor-market-adjustment.tex](slides/week12/12-trade-offshoring-and-labor-market-adjustment.tex). It is longer than a standard week because this is one of the heavier Labor II lectures, but it stays tightly organized around the Week 11 to Week 12 bridge, the channel map, local exposure objects, the China shock, Brazil dynamic adjustment, Germany structural change, offshoring as a distinct channel, worker-versus-place adjustment, global evidence, and the bridge to Week 13.
