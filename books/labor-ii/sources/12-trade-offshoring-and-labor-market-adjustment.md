# Week 12 source pack — Trade, Offshoring, and Labor Market Adjustment

## Central question

How do trade and offshoring shocks transmit through workers, firms, sectors, and places, and what determines short-run dislocation versus longer-run adjustment?

## Why this week belongs here

This week follows Technology, Automation, AI, and Labor Market. The comparison is part of the point.

- Technology changes tasks, production methods, and skill demand from inside the production process.
- Trade changes relative prices, competitive pressure, export opportunities, input access, and the location of production across firms, sectors, and places.
- In practice, technology and trade often interact, but this lecture should keep the trade channels explicit rather than letting them dissolve into a generic “globalization” narrative.

This week should also make clear why trade is not just a demand shock to manufacturing. It can affect labor markets through multiple linked channels:
1. import competition,
2. export expansion,
3. offshoring / fragmentation / services-trade channels,
4. intermediate-input and cost channels,
5. structural change across sectors and regions,
6. labor reallocation frictions and transition costs.

## Core framing for the chapter

The lecture should be organized as a research framework, not as a bucket of famous papers.

Use the following logic:

1. **What are the channels?**
   Trade affects local labor markets through sectoral price changes, import competition, export demand, offshoring, intermediate-input access, and induced changes in the composition of production.

2. **Which labor-market margins move?**
   Wages, employment, unemployment, nonparticipation, sector switching, occupation/task switching, migration, firm exit/entry, and worker sorting.

3. **How does structural change happen?**
   Trade can accelerate or dampen movement from manufacturing into services, but the mechanisms matter:
   - incumbent workers may not move smoothly,
   - entrants and returnees may account for much of the observed reallocation,
   - transition costs and skill transferability matter,
   - export and import channels need not offset one another symmetrically.

4. **What does the empirical literature actually identify?**
   Local exposure designs, tariff reforms, border/FTA variation, linked worker-firm panels, and structural equilibrium frameworks speak to different margins.

5. **What are the welfare and research-frontier questions?**
   Worker losses can coexist with aggregate gains; place adjustment can differ from people adjustment; and recent work increasingly asks about long-run transitions, service reallocation, supply chains, labor market power, and global heterogeneity.

## Bridge section requirements

The Bridge section should:
- connect back to Week 11 by contrasting technology shocks with trade shocks,
- review the main labor-market objects students already know from Weeks 4–10:
  - labor demand,
  - turnover and search,
  - wage-setting,
  - monopsony,
  - regulation,
  - cyclical adjustment,
- explain that Week 12 asks how an external product-market shock propagates through those same labor-market institutions and frictions.

## Field Core requirements

The Field Core should be longer than a normal week and should move in this order.

### 1. Channel map

Start with a clean taxonomy.

Required channels:
- import competition,
- export market access,
- offshoring / tasks performed abroad,
- cheaper intermediate inputs,
- firm selection / productivity reallocation,
- structural change between manufacturing and services,
- regional and worker mobility frictions.

This must be presented as a map, not as a loose paragraph.

### 2. Non-negotiable formal objects

The final chapter must contain all of the following formal objects.

#### A. Local trade exposure / reduced-form object

Use a canonical exposure equation such as a Bartik-style or tariff-exposure object:

```{math}
:label: eq:trade_exposure
\text{Exposure}_r = \sum_s \omega_{rs,0}\,\Delta \text{TradeShock}_s
```

where {math}`\omega_{rs,0}` is an initial employment or wage-share weight and {math}`\Delta \text{TradeShock}_s` is a sector-level change in import competition, tariffs, or export demand.

Explain what changes when the unit is:
- region,
- worker,
- firm,
- local labor market.

#### B. Trade shock to labor-market outcomes

Include a reduced-form labor-market response equation:

```{math}
:label: eq:trade_labor_outcome
\Delta y_r = \beta \,\text{Exposure}_r + X_r'\Gamma + \varepsilon_r
```

and state explicitly that the observed margin {math}`y_r` could be:
- employment,
- wages,
- unemployment,
- nonparticipation,
- sector shares,
- mobility,
- earnings over horizons.

#### C. Trade-induced structural change object

Include a two-sector manufacturing/services object that makes structural change explicit. It does not need to be fully general equilibrium, but it must make transparent why trade can reallocate labor toward services.

At minimum, include an object like:

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

and interpret this as a guide for thinking about trade-induced structural change, not as a fully sufficient empirical model.

#### D. Dynamic adjustment / transition object

Include at least one object that distinguishes short-run displacement from long-run adjustment, for example an event-study or distributed-lag response to tariff cuts or import exposure.

#### E. Worker-versus-place welfare object

The chapter must explicitly distinguish worker losses, place losses, and aggregate welfare. It should be clear that:
- local employment losses do not automatically map one-for-one into individual lifetime losses,
- worker reallocation can mitigate or delay losses,
- aggregate welfare statements require stronger structure than local reduced-form estimates.

### 3. Canonical empirical sequence

Use the following backbone.

#### A. U.S. local import competition
- `@autorDornHanson2013ChinaSyndrome`
- `@pierceSchott2016SurprisinglySwiftDecline`

This section should establish the local-labor-market exposure logic, manufacturing decline, wage/employment effects, and the difference between trade shocks and other concurrent shocks.

#### B. Dynamic regional adjustment in Brazil
- `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`

This should be the core section on dynamic adjustment, persistence, and why short-run regional estimates can understate or mischaracterize long-run transition dynamics.

#### C. Manufacturing-to-service transition in Germany
- `@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany`

This should be the key structural-change section. Be explicit that the transition margin is not simply incumbent manufacturing workers smoothly moving into services.

#### D. Trade-induced structural change and the skill premium
- `@cravinoSotelo2019TradeInducedStructuralChange`

Use this to connect trade to sectoral reallocation and inequality through relative prices, demand, and skill intensity.

#### E. General framework for labor-market adjustment and welfare
- `@kimVogel2021TradeShocksLaborMarketAdjustment`
- `@caliendoDvorkinParro2019TradeLaborMarketDynamics`

Use these to show what a more structured labor-market-adjustment framework adds beyond local reduced-form estimates.

#### F. Long-run FTA evidence / newer direction
- `@kovakMorrow2025LongRunCUSFTA`

Use this section to foreshadow where the literature is going:
- long-run worker panels,
- import vs export asymmetry,
- matched administrative data,
- worker trajectories rather than only place trajectories.

### 4. Offshoring / services-trade channel

Do not treat offshoring as a side comment.

Use at least one classic anchor:
- `@feenstraHanson1999OutsourcingHighTechnologyWages`

The purpose is not to turn the week into an outsourcing history lesson. The purpose is to make clear that offshoring / fragmentation / services trade is a distinct transmission channel from classic final-goods import competition.

### 5. New directions section

This section must be real, not generic.

Recommended buckets:
- people versus places and long-run worker tracking,
- structural change into services and the role of entrants / returnees,
- services trade, fragmentation, and white-collar offshoring,
- trade and labor market power / concentration,
- trade shocks under supply-chain risk, policy uncertainty, or re-globalization,
- global and comparative evidence rather than U.S.-only framing,
- welfare and policy evaluation across local labor markets.

## Empirical and methods requirements

The final chapter must distinguish:
- import competition vs export exposure,
- tariff-reform designs vs import-penetration designs,
- worker-level vs place-level treatment and outcomes,
- goods-trade vs offshoring/services-trade channels,
- reduced-form exposure papers vs dynamic / structural equilibrium papers,
- short-run displacement vs long-run adjustment,
- incumbents vs entrants / returnees,
- distributional outcomes vs welfare conclusions.

Do not let any section say “trade hurts workers” or “trade helps workers” without clarifying:
- which workers,
- through which channel,
- at what horizon,
- in which unit of observation,
- and relative to what counterfactual.

## Research Lab requirements

The Research Lab should be especially strong this week.

### Lab logic
Use Reproduce -> Diagnose -> Transfer.

### Primary lab anchor
- `@autorDornHanson2013ChinaSyndrome`

### Secondary / challenge anchor
- `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`

### Optional extension anchor
- `@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany`

### What students should learn
- how a local-exposure design is constructed,
- why import shocks are often instrumented,
- what margin is actually observed,
- why transition and equilibrium margins matter,
- how to move from a reduced-form place-level estimate to a more careful interpretation.

### Transfer exercise direction
A good bounded transfer exercise is:
- build a small synthetic or public region-sector exposure measure,
- estimate one reduced-form relationship on employment-share, unemployment, or sector-share change,
- compare what changes when the outcome is:
  - manufacturing employment share,
  - services employment share,
  - unemployment,
  - earnings.

The lab should force students to say which channel their transfer exercise is actually about.

## Tables to use

Use these editable tables:
- `assets/tables/12-trade-channels-map.md`
- `assets/tables/12-structural-change-and-transition-map.md`
- `assets/tables/12-global-evidence-and-frontier-map.md`

## Figure needs

If figures are needed and do not yet exist, create them at these stable paths:
- `assets/figures/12-trade-channels-framework.png`
- `assets/figures/12-trade-structural-change-transitions.png`
- `assets/figures/12-trade-adjustment-worker-vs-place.png`
- `assets/figures/12-trade-global-evidence-and-frontiers.png`
- `assets/figures/12-trade-welfare-and-reallocation.png`

## Slide guidance

The slide deck should be longer than a standard week if needed, but it must remain tightly structured.

Required arc:
1. central question and why trade is not just a demand shock,
2. Week 11 to Week 12 bridge,
3. trade channels map,
4. exposure measures and what they identify,
5. U.S. local import competition,
6. Brazil and dynamic regional adjustment,
7. Germany and manufacturing-to-service transitions,
8. trade-induced structural change,
9. offshoring / services trade,
10. worker vs place adjustment and welfare,
11. global evidence and frontier questions,
12. bridge to Week 13.

## Editorial priorities

The week should feel like an advanced PhD labor-economics lecture on trade, not a trade lecture with a short labor section attached.
