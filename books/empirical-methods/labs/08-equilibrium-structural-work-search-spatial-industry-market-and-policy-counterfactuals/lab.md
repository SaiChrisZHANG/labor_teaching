# Code Lab 08: Equilibrium Structural Work

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 8 - equilibrium structural work  
**Associated chapter:** `08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.md`  
**Lab slug:** `08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** structural estimation basics, fixed-point intuition, demand elasticity intuition, basic `pandas`  
**Core economic question:** When is equilibrium structure worth the extra assumptions?  
**Core design / estimator:** spatial fixed point, equilibrium counterfactual, sensitivity diagnosis, compact market-equilibrium transfer  
**Source paper spine:** Hsieh and Moretti [@hsiehMoretti2019], Berry-Levinsohn-Pakes [@berryLevinsohnPakes1995], and Nevo [@nevo2001]

## Why This Lab Exists

Lecture 8 argues that equilibrium structural work is useful when individual decisions interact through markets, firms, prices, locations, or flows. This lab makes that logic executable at teaching scale. Students first reproduce the architecture of a spatial-equilibrium counterfactual inspired by Hsieh and Moretti: housing constraints in productive cities affect rents, population allocation, output, and welfare. They then diagnose which assumptions move the result. Finally, they transfer the logic to a market-equilibrium pass-through exercise inspired by BLP/Nevo-style differentiated-product work.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on equilibrium objects, fixed points, incidence, welfare, and validation burdens.

## Learning Objectives

By the end of this lab, students should be able to:

1. solve a compact spatial-equilibrium fixed point;
2. distinguish wages, rents, output, and welfare in an equilibrium counterfactual;
3. explain which spatial-equilibrium objects are observed and which are imposed by closure;
4. diagnose sensitivity to housing-supply and mobility assumptions;
5. estimate a compact demand equation for a market-equilibrium transfer exercise;
6. recover markups and marginal costs under a simple pricing rule;
7. simulate a marginal-cost shock and interpret pass-through;
8. compare spatial incidence with product-market incidence.

## Required Local Structure

```text
labs/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      spatial_equilibrium_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      market_equilibrium_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_spatial_equilibrium.py
    transfer_market_equilibrium.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs three steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_spatial_equilibrium.py --input original/reduced/spatial_equilibrium_synthetic.csv --outdir output/reproduced
python src/transfer_market_equilibrium.py --input transfer/data/market_equilibrium_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Spatial-Equilibrium Counterfactual

### Objective

Compute a bounded Hsieh-Moretti-style housing relaxation counterfactual.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/baseline_equilibrium.csv`.
4. Open `output/reproduced/housing_counterfactual.csv`.
5. Open `output/reproduced/aggregate_counterfactual_summary.csv`.
6. Inspect `output/reproduced/spatial_incidence.png`.

### Required Questions

- What is the equilibrium fixed point?
- Why are wages alone not a welfare object?
- Which cities gain population after the housing relaxation?
- How do rents change when constraints are relaxed?
- What is the aggregate output object?
- Why is this not an official Hsieh-Moretti replication?

### Minimum Output

- one paragraph describing the fixed point;
- one table or paragraph summarizing output, rent, population, and welfare changes;
- one sentence explaining why the exercise is a teaching reproduction of logic rather than a data replication.

## Part II. Diagnose Equilibrium Assumptions

### Objective

Evaluate whether the spatial counterfactual is disciplined by data or by closure assumptions.

### Student Tasks

1. Open `output/reproduced/equilibrium_moment_fit.csv`.
2. Open `output/reproduced/assumption_map.csv`.
3. Open `output/reproduced/spatial_sensitivity.csv`.
4. Write a one-page Diagnose memo.

### Required Prompts

- Which objects are observed in the synthetic data?
- Which objects are calibrated or imposed by the model?
- Does the counterfactual depend more on housing supply or mobility?
- Which untargeted moments would a publishable paper need?
- Where would a reduced-form design stop?

### Minimum Output

- one observed-versus-latent paragraph;
- one sensitivity paragraph;
- one validation paragraph;
- one final sentence stating whether the equilibrium model is buying a necessary object.

## Part III. Transfer To Market Equilibrium

### Objective

Use a compact differentiated-product market model to simulate pass-through after a marginal-cost shock.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/demand_estimates.csv`.
3. Open `output/transfer/markup_recovery.csv`.
4. Open `output/transfer/market_counterfactual_summary.csv`.
5. Inspect `output/transfer/market_pass_through.png`.
6. Write a short Transfer memo.

### Required Prompts

- What does the demand coefficient identify in this teaching path?
- How are markups recovered?
- What is the equilibrium pricing rule?
- How does pass-through differ from the spatial incidence channel?
- What would a publishable BLP/Nevo-style paper need that this lab omits?

### Minimum Output

- one demand and markup paragraph;
- one cost-shock counterfactual paragraph;
- one paragraph comparing spatial equilibrium with market equilibrium;
- one paragraph on validation and missing instruments.

## Deliverables Checklist

- [ ] run log;
- [ ] spatial fixed-point description;
- [ ] baseline and counterfactual spatial tables;
- [ ] spatial incidence figure;
- [ ] assumption map;
- [ ] sensitivity memo;
- [ ] market demand estimates;
- [ ] markup recovery table;
- [ ] market counterfactual table;
- [ ] pass-through figure;
- [ ] final paragraph stating what equilibrium structure adds and what remains assumption-dependent.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Spatial fixed-point interpretation | 25 |
| Incidence and welfare interpretation | 20 |
| Diagnosis of assumptions and sensitivity | 25 |
| Market-equilibrium transfer | 20 |
| Code organization and communication | 10 |

## Instructor Notes

- The spatial data and market data are synthetic and intentionally small enough for local smoke testing.
- The spatial solver is a teaching fixed point over population, wages, rents, and utility; it is not a frontier quantitative spatial model.
- The market transfer uses a simple logit demand and single-product pricing rule; it omits the instruments, ownership structure, and random coefficients needed for publishable differentiated-product work.
- The important learning outcome is not numerical accuracy. It is the ability to see what the equilibrium closure is doing.
