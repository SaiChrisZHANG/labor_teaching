# Code Lab 10: Aggregate Fluctuations and Labor Market Adjustment

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 10 --- Aggregate fluctuations and labor market adjustment  
**Associated chapter:** `10-aggregate-fluctuations-and-labor-market-adjustment.md`  
**Lab slug:** `10-aggregate-fluctuations-and-labor-market-adjustment`  
**Scope tier:** Heavy aggregate-adjustment week  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 4 and 9, grouped-data intuition, basic `pandas`, simple plots, and comfort distinguishing measured hazards from inferred residuals  
**Core economic question:** Which aggregate labor-market object is being measured, which margin is directly observed, which margin is inferred, and how does that answer change when we move from matching residuals to stock-flow decompositions and job-to-job mobility?  
**Primary source anchor:** `@barnichonFigura2015AggregateMatching`  
**Secondary / challenge anchor:** `@elsbyMichaelsSolon2009InsOuts`  
**Optional extension anchor:** `@karahanMichaelsPugsleySahinSchuh2017JobToJob`

## Why this lab exists

Week 10 becomes muddy fast if students say “the labor market got worse” without naming whether they mean higher unemployment, lower job finding, higher separations, lower matching efficiency, weaker job ladders, or slower wage growth. `@barnichonFigura2015AggregateMatching` is the right reproduction anchor because it forces the distinction between observed stocks and an inferred matching residual. `@elsbyMichaelsSolon2009InsOuts` is the challenge anchor because it reminds us that unemployment is a stock governed by inflow and outflow hazards. `@karahanMichaelsPugsleySahinSchuh2017JobToJob` is the optional extension because cyclical wage growth also moves through employed search and direct job-to-job mobility.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded aggregate matching exercise and compute a matching-efficiency residual from synthetic aggregate data;
2. explain whether the measured object is about stocks, flows, efficiency, wages, or job ladders before interpreting any output;
3. distinguish the directly observed margins from the inferred margins in both Beveridge-style and stock-flow designs;
4. diagnose how unemployment changes using inflows and outflows rather than only the unemployment rate;
5. transfer the same logic to a small synthetic job-to-job and wage-cyclicality dataset.

## Scope rules

This lab is intentionally bounded.

- Reproduce one Barnichon-Figura-style aggregate matching object from a local synthetic panel.
- Diagnose one Elsby-Michaels-Solon-style unemployment stock-flow decomposition.
- Transfer the Week 10 framework to a synthetic job-to-job and wage-cyclicality panel.
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a full public-data download pipeline or a confidential matched employer-employee replication.

## Lab roadmap

1. **Reproduce** a bounded aggregate matching and Beveridge-curve exercise.
2. **Diagnose** what is observed directly and what is inferred when unemployment changes.
3. **Transfer** the same reasoning to job-to-job mobility and wage cyclicality.
4. **Extend** the analysis to another recession window, geography, or aggregation choice.

## Part 0. Setup and orientation

### First commands to run

```bash
conda run -n research python src/reproduce_aggregate_matching.py \
  --outdir output/reproduced

conda run -n research python src/transfer_cyclical_adjustment.py \
  --reproduced output/reproduced/aggregate_matching_panel.csv \
  --outdir output/transfer
```

### Before you interpret anything

Write down five things.

1. What aggregate labor-market object is being measured?
2. Is the design about stocks, flows, efficiency, wages, or job ladders?
3. Which margin is directly observed?
4. Which margin is inferred?
5. What cyclical comparison is being made?

## Part I. Reproduce a bounded Barnichon-Figura object

### Objective

Recover a compact aggregate panel with unemployment, vacancies, hires, tightness, and a matching-efficiency residual.

### Be explicit before you run anything

1. **Aggregate labor-market object being measured:** aggregate matching between unemployed workers and vacancies.
2. **Design category:** efficiency residual built from stocks and hires.
3. **Directly observed margins in the bounded file:** unemployment, vacancies, and hires.
4. **Inferred margin:** the matching-efficiency residual {math}`\mu_t = m_t / (u_t^{\alpha} v_t^{1-\alpha})`.
5. **Cyclical comparison:** pre-downturn, downturn, and recovery phases in a synthetic aggregate episode.

### Student tasks

1. Run `src/reproduce_aggregate_matching.py`.
2. Inspect `output/reproduced/aggregate_matching_panel.csv`.
3. Inspect `output/reproduced/aggregate_matching_summary.csv`.
4. Inspect `output/reproduced/aggregate_matching_counterfactual.csv`.
5. Open `output/reproduced/aggregate_matching_beveridge.png`.
6. Write a short note on why the residual should not immediately be interpreted as pure structural efficiency.

### Required questions

- What is directly observed in the reproduction path, and what is inferred?
- Why can a matching residual move even if the underlying matching technology is unchanged?
- Which labor-market margin is hidden if you only look at unemployment and vacancies?
- How does this design differ from a worker-level transition design?

## Part II. Diagnose unemployment as a stock-flow object

### Objective

Move from “unemployment rose” to a statement about inflows, outflows, and the hidden margins left out of the basic decomposition.

### Be explicit before you interpret the diagnosis outputs

1. **Aggregate labor-market object being measured:** the unemployment stock and its flow decomposition.
2. **Design category:** flows and hazards.
3. **Directly observed margin in the bounded path:** unemployment, job-finding rates, and separation rates in the synthetic panel.
4. **Inferred margin:** the contribution of inflows and outflows to observed unemployment changes.
5. **Cyclical comparison:** the same aggregate episode, now decomposed into job-loss and job-finding channels.

### Student tasks

1. Run `src/transfer_cyclical_adjustment.py`.
2. Inspect `output/transfer/stock_flow_decomposition.csv`.
3. Inspect `output/transfer/transfer_summary.csv`.
4. Open `output/transfer/cyclical_adjustment_transfer.png`.
5. Explain whether the downturn is mostly an inflow event, an outflow event, or both.

### Minimum output

- one short memo naming the observed stock, the hazard margins, and the main hidden margin still offstage;
- one paragraph comparing the matching residual design to the stock-flow design;
- one paragraph explaining why aggregate unemployment is not itself a sufficient statistic for labor slack.

## Part III. Transfer to job-to-job mobility and wage cyclicality

### Objective

Shift from unemployment and matching to employed search, direct job-to-job mobility, and wage growth.

### Be explicit before you interpret the transfer outputs

1. **Aggregate labor-market object being measured:** job-to-job mobility and wage growth over the cycle.
2. **Design category:** job ladders and wage cyclicality.
3. **Directly observed margin in the bounded transfer:** synthetic `E->E` rate and wage-growth components.
4. **Inferred margin:** how much average wage cyclicality is due to mover margins versus incumbent wages versus composition.
5. **Cyclical comparison:** tight versus slack phases in the same synthetic episode.

### Student tasks

1. Inspect `output/transfer/job_to_job_wage_panel.csv`.
2. Compare incumbent wage growth, mover wage growth, and the aggregate series.
3. Explain why a weak labor market can flatten wage growth by compressing job-to-job mobility even if incumbent wages barely move.
4. Write one paragraph connecting the transfer outputs back to `@karahanMichaelsPugsleySahinSchuh2017JobToJob`.

### Transfer directions you are allowed to propose

- a public aggregate Beveridge-curve exercise;
- a small CPS-style stock-flow exercise;
- a synthetic or public job-to-job panel with wage-growth decomposition;
- a short memo comparing unemployment, matching residuals, and job ladders as cyclical objects.

## Part IV. Optional extension

Choose one extension only.

1. Recompute the bounded outputs after changing the downturn severity and explain which margins respond first.
2. Use the synthetic job-to-job panel to design a mover-versus-incumbent wage-cyclicality exercise.
3. Write a short memo on what additional data would be required to turn the bounded matching residual into a stronger structural design.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path uses synthetic aggregate data; it does not reproduce the original heterogeneity-rich data environment in `@barnichonFigura2015AggregateMatching`.
2. The diagnosis path uses synthetic hazards; it does not reproduce the full CPS accounting and classification challenges in `@elsbyMichaelsSolon2009InsOuts`.
3. The transfer path uses synthetic job-to-job and wage-growth components; it does not recover the full matched worker-firm structure in `@karahanMichaelsPugsleySahinSchuh2017JobToJob`.
4. None of the bounded paths identify the full equilibrium search environment, the full offer distribution, or the complete general-equilibrium response of vacancies and wages.

## Deliverables checklist

- [ ] reproduced matching panel and summary table  
- [ ] reproduced Beveridge and matching-residual figure  
- [ ] diagnose memo on stocks versus flows  
- [ ] stock-flow decomposition table  
- [ ] transfer summary table and figure  
- [ ] short note on mover versus incumbent wage cyclicality  

## Instructor notes

- The biggest classroom payoff comes from forcing students to state whether the object is a stock, hazard, residual, or wage component before they start interpreting it.
- The second biggest payoff comes from making students separate unemployment adjustment from job-to-job adjustment.
- The bounded path is intentionally local and synthetic so that the core Week 10 reasoning is reproducible without proprietary microdata.
