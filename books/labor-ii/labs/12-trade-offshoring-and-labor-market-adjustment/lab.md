# Code Lab 12: Trade, Offshoring, and Labor Market Adjustment

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 12 --- Trade, Offshoring, and Labor Market Adjustment  
**Associated chapter:** `12-trade-offshoring-and-labor-market-adjustment.md`  
**Lab slug:** `12-trade-offshoring-and-labor-market-adjustment`  
**Scope tier:** Heavy shock-and-adjustment week  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 1, 4, 10, and 11; comfort with grouped data, weighted exposure objects, and the distinction between place effects and worker effects  
**Core economic question:** When trade exposure rises, which channel are we measuring, what unit is treated, which labor margin is observed, and what transition or equilibrium margin still sits offstage?  
**Primary source anchor:** `@autorDornHanson2013ChinaSyndrome`  
**Secondary / challenge anchor:** `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`  
**Optional extension anchor:** `@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany`

## Why this lab exists

Week 12 gets muddy when students move too quickly from a famous trade shock to a broad statement like "trade hurts workers." `@autorDornHanson2013ChinaSyndrome` is the right reproduction anchor because it forces the class to construct a local-labor-market trade-exposure object and to confront the fact that the resulting estimate is a place effect. `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics` is the right challenge anchor because it makes clear that one-period place effects are not the same as dynamic adjustment. `@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany` is the right optional extension because it shows why service-sector expansion is not enough to infer smooth incumbent-worker transition.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded local-labor-market import-exposure exercise inspired by `@autorDornHanson2013ChinaSyndrome`;
2. state explicitly whether the design identifies worker effects, firm effects, place effects, or sector effects;
3. name the trade channel being measured and the exposure object used to measure it;
4. distinguish manufacturing-share decline, service-share growth, unemployment, and nonparticipation as separate labor-market margins;
5. transfer one exposure idea to a bounded structural-change setting rather than a vague "do something with trade" exercise.

## Scope rules

This lab is intentionally bounded.

- Reproduce one commuting-zone-style import-exposure design from a local synthetic panel.
- Diagnose what the exposure coefficient does and does not identify.
- Transfer the same exposure logic to a synthetic structural-change panel with manufacturing and services outcomes.
- Keep the smoke path fully local and synthetic.
- Do not require restricted worker microdata, confidential customs records, or a full official replication package.

## Lab roadmap

1. **Reproduce** a bounded China-syndrome-style local exposure design.
2. **Diagnose** the channel, treatment object, observed margin, and hidden adjustment margin.
3. **Transfer** the exposure idea to a structural-change setting with service reallocation.
4. **Challenge** yourself by comparing one-period place incidence to dynamic regional adjustment.

## Part 0. Setup and orientation

### First commands to run

```bash
conda run -n research python src/reproduce_trade_exposure.py \
  --outdir output/reproduced

conda run -n research python src/transfer_trade_adjustment.py \
  --reproduced output/reproduced/cz_trade_panel.csv \
  --outdir output/transfer
```

### Before you interpret anything

Write down five things for each stage of the lab.

1. Which trade channel is being measured?
2. Does the design identify worker effects, firm effects, place effects, or sector effects?
3. What is the key exposure measure?
4. Which labor-market margins are observed?
5. Which transition or equilibrium margin remains offstage?

## Part I. Reproduce a bounded China-syndrome-style exposure design

### Objective

Recover a small commuting-zone panel in which baseline industrial composition maps sector-level import shocks into local labor-market exposure.

### Be explicit before you run anything

1. **Trade channel:** import competition.
2. **Design family:** local-labor-market shift-share exposure.
3. **Treatment object:** place effect, not worker treatment.
4. **Exposure measure:** baseline sector employment shares interacted with sector import-shock growth.
5. **Observed labor-market margins:** manufacturing employment-share change, unemployment change, nonparticipation change, and wage growth.
6. **Key offstage margins:** migration, worker retraining, export offsets, and aggregate consumer gains.

### Student tasks

1. Run `src/reproduce_trade_exposure.py`.
2. Inspect `output/reproduced/cz_trade_panel.csv`.
3. Inspect `output/reproduced/sector_trade_shocks.csv`.
4. Inspect `output/reproduced/trade_exposure_summary.csv`.
5. Open `output/reproduced/trade_exposure_margins.png`.
6. Write a short note explaining why the design identifies a place effect rather than an individual worker welfare effect.

### Required questions

- What exactly is the exposure measure weighting?
- Why is import competition the measured channel in this reproduction?
- Which outcome in the reproduced panel comes closest to adjustment on the extensive margin?

## Part II. Diagnose what the local exposure estimate does and does not identify

### Objective

Force the interpretation discipline that the chapter requires.

### Be explicit before you interpret the reproduced outputs

1. **Trade channel:** import competition.
2. **Treatment object:** place-level exposure.
3. **Unit of observation:** commuting-zone-year cell.
4. **Observed labor-market margins:** manufacturing share, unemployment, nonparticipation, and wage growth.
5. **Key offstage margin:** worker transitions across sectors and places.

### Student tasks

1. Inspect `output/reproduced/trade_exposure_relationships.csv`.
2. Explain why a negative manufacturing-share relationship is not enough to conclude that worker welfare fell one-for-one.
3. State whether the reproduction identifies worker, firm, place, or sector effects.
4. Write two sentences on what additional data would be needed to say more about worker trajectories.

## Part III. Transfer the exposure idea to structural change

### Objective

Carry one Week 12 exposure object into a bounded new setting with manufacturing-to-service reallocation.

### Concrete transfer exercise

Use the same local exposure measure, but compare how it relates to three distinct outcomes in the synthetic regional panel:

1. manufacturing employment-share decline,
2. service employment-share growth,
3. unemployment change.

Then explain whether the same trade shock appears to operate mainly through sectoral reallocation or labor-force distress in the transfer setting.

### Why this is the transfer exercise

It is narrow, reproducible, and on-theme. Students are not told to "do something with trade." They are asked to move one exposure idea into a structural-change setting and compare interpretation across outcomes.

### Be explicit before you interpret the transfer outputs

1. **Trade channel:** import competition plus associated structural-change pressure.
2. **Treatment object:** place-level exposure.
3. **Exposure measure:** imported from the reproduction step.
4. **Observed labor-market margins:** manufacturing share, service share, unemployment, and nonparticipation.
5. **Key offstage margins:** incumbent-worker moves versus entrant and returnee margins.

### Student tasks

1. Inspect `output/transfer/structural_change_transfer.csv`.
2. Inspect `output/transfer/transfer_adjustment_summary.csv`.
3. Open `output/transfer/trade_adjustment_transfer.png`.
4. Explain why service-share growth is not the same object as incumbent-worker recovery.

## Part IV. Challenge extension: dynamic regional adjustment

### Objective

Contrast one-period place incidence with multi-period regional adjustment inspired by `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`.

### Be explicit before you interpret the challenge outputs

1. **Trade channel:** tariff-reform exposure with persistent regional adjustment.
2. **Treatment object:** regional place effect over time.
3. **Unit of observation:** region-year cell.
4. **Observed labor-market margins:** earnings index, manufacturing share, service share, and unemployment.
5. **Key offstage margin:** long-run worker welfare for initially exposed cohorts.

### Student tasks

1. Inspect `output/transfer/dynamic_region_panel.csv`.
2. Inspect `output/transfer/dynamic_region_summary.csv`.
3. Compare the short-run and long-run horizons in the summary table.
4. Write two sentences on why dynamic regional recovery and worker recovery are not identical claims.

## Limitations relative to the original papers

Students should say these plainly.

1. The reproduction path uses a local synthetic commuting-zone panel rather than the original U.S. exposure environment in `@autorDornHanson2013ChinaSyndrome`.
2. The transfer path uses synthetic structural-change outcomes rather than actual service reallocation data.
3. The challenge path mimics dynamic regional adjustment but does not reproduce the full Brazilian tariff-reform design in `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`.
4. None of the bounded paths identify full worker welfare, aggregate gains from trade, or a complete dynamic equilibrium.

## Deliverables checklist

- [ ] reproduced commuting-zone trade panel and summary table  
- [ ] figure relating trade exposure to labor-market margins  
- [ ] diagnosis note on channel, unit, and hidden adjustment margin  
- [ ] structural-change transfer outputs  
- [ ] dynamic regional challenge outputs  
- [ ] short note on why service growth is not the same as incumbent-worker recovery  

## Instructor notes

- The highest-value discipline is forcing students to label the trade channel before interpreting coefficients.
- The second-highest-value discipline is forcing them to say whether the design identifies worker, place, or sector effects.
- The transfer exercise is intentionally narrow so Week 12 stays about structured interpretation rather than a loose globalization discussion.
