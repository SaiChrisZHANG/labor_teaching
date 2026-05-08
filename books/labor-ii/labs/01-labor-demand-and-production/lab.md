# Code Lab 01: Static Labor Demand, Local Demand Shocks, and Incidence

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 1 — Labor demand and production  
**Associated chapter:** `01-labor-demand-and-production.md`  
**Lab slug:** `01-labor-demand-and-production`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 1 module, command-line basics, introductory `pandas`, comfort reading scatterplots and elasticity tables  
**Core economic question:** What does a local labor-demand design identify, and how does that differ from the conditional-versus-total decomposition in the static model?  
**Primary source anchor:** [@beaudryGreenSand2018]  
**Challenge anchor:** [@saezSchoeferSeim2019]  
**Optional extension anchor:** [@buttersSacksSeo2022]

## Why this lab exists

Week 1 should not end with a blackboard elasticity. [@beaudryGreenSand2018] is a strong pedagogical anchor because it makes students name the source of variation and the margin observed. A city-industry demand shift is not the same thing as a wage shock holding output fixed. The lab keeps that distinction explicit while staying runnable on local synthetic data.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a compact city-industry labor-demand relationship using the local synthetic panel;
2. explain why that relationship is closer to total labor demand than to conditional labor demand;
3. diagnose which margin is observed and what the identifying variation is doing;
4. transfer the Week 1 formulas to a stylized payroll-tax scenario file;
5. explain how the same static benchmark supports both local-demand and incidence applications.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact [@beaudryGreenSand2018]-style city-industry relationship.
- Diagnose the estimand in a short memo.
- Transfer the logic to one stylized labor-cost scenario file.
- Do not turn the lab into a full shift-share, equilibrium, or confidential-data replication.
- Keep the smoke test on the synthetic teaching path only.

## Lab roadmap

1. **Reproduce** a reduced local-demand relationship from the synthetic city-industry panel.
2. **Diagnose** the identifying variation and the observed margin.
3. **Transfer** the static formulas to payroll-tax and product-demand scenarios.
4. **Reflect** on what Week 1 can and cannot learn without dynamic adjustment or wage-setting.

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for [@beaudryGreenSand2018]. It is a synthetic teaching workflow inspired by the design logic of local demand shifts. The goal is to practice Week 1 reasoning cleanly, not to mimic the full data environment of the published paper.

### First commands to run

```bash
conda run -n research python src/reproduce_beaudry_city_industry.py \
  --input original/reduced/beaudry_city_industry_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_static_labor_demand.py \
  --input transfer/data/static_labor_demand_scenarios.csv \
  --outdir output/transfer
```

## Part I. Reproduce a bounded local-demand object

### Objective

Recover a compact relationship between local demand growth and employment growth, then relate that relationship back to the distinction between conditional and total labor demand.

### Student tasks

1. Read `original/source-notes.md`.
2. Run `src/reproduce_beaudry_city_industry.py`.
3. Inspect `output/reproduced/beaudry_city_industry_deltas.csv`.
4. Open `output/reproduced/beaudry_city_industry_scatter.png`.
5. Write a short note explaining why the object is not a pure conditional-demand elasticity.

### Required questions

- What varies in the bounded reproduction path?
- Which outcome margin is actually observed?
- Why is the resulting object closer to total labor demand than to conditional labor demand?
- What equilibrium or spillover effects are being suppressed by the synthetic teaching path?

## Part II. Diagnose the design

### Objective

Move from "the slope is positive" to "I know what that slope means."

### Student tasks

1. State the identifying variation in one sentence.
2. Name the observed margin in one sentence.
3. Explain whether the design primarily loads on substitution, scale, or both.
4. Say what would need to change for the design to identify something closer to conditional labor demand.

### Minimum output

- one short design memo;
- one annotated copy of the summary table;
- one paragraph connecting the reduced exercise to Equation 4 in the chapter.

## Part III. Transfer the Week 1 formulas

### Objective

Use the Week 1 static benchmark on a small scenario file that compares payroll-tax and product-demand environments.

### Student tasks

1. Run `src/transfer_static_labor_demand.py`.
2. Inspect `output/transfer/static_labor_demand_transfer_summary.csv`.
3. Compare conditional and total elasticities across the supplied scenarios.
4. Explain why the payroll-tax case is the natural bridge to [@saezSchoeferSeim2019].

### Acceptable transfer interpretations

- high labor-share sectors should show larger scale effects;
- low-substitutability sectors should show weaker conditional responses;
- weaker product-demand elasticity should mute total employment responses.

## Part IV. Optional extensions

Use one extension only.

1. Read [@saezSchoeferSeim2019] and explain how wage-setting complicates the clean Week 1 incidence benchmark.
2. Read [@buttersSacksSeo2022] and explain why multi-market firms can absorb local cost shocks through prices rather than local employment alone.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced scatterplot and delta table  
- [ ] one-page design memo  
- [ ] transfer summary table and figure  
- [ ] short bridge note to [@saezSchoeferSeim2019]  
- [ ] final reflection memo

## Instructor notes

- The bounded path is for local execution and smoke testing.
- The strongest classroom payoff comes from forcing the conditional-versus-total distinction into the design memo.
- Students should not treat the synthetic slope as a publishable elasticity estimate.
