# Code Lab 17: Spatial Structural Modeling

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 17 - spatial structural modeling  
**Associated chapter:** `17-spatial-structural-modeling.md`  
**Lab slug:** `17-spatial-structural-modeling`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** logit choice intuition, fixed-point intuition, gravity regressions, weighted averages, `pandas`  
**Core economic question:** When do place effects need an equilibrium model of commuting, migration, wages, rents, housing, and welfare?  
**Core design / estimator:** commuting gravity block, compact spatial fixed point, fit and sensitivity diagnostics, dynamic adjustment transfer  
**Source paper spine:** Monte, Redding, and Rossi-Hansberg [@monteReddingRossiHansberg2018] and Greaney, Parkhomenko, and Van Nieuwerburgh [@GreaneyParkhomenkoVanNieuwerburgh2025]

## Why This Lab Exists

Lecture 17 argues that spatial structural modeling is useful when the research object is an equilibrium outcome rather than a local treatment effect. This lab makes that logic executable at teaching scale. Students estimate a gravity-style commuting relationship, solve a compact spatial equilibrium, diagnose which assumptions move the counterfactual, and transfer the logic to a dynamic adjustment setting.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on equilibrium objects, bilateral flows, incidence, welfare, fit, and counterfactual interpretation.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate a simple commuting gravity relationship from bilateral flows;
2. construct commuting openness by residence location;
3. solve a compact spatial-equilibrium counterfactual with wages, rents, residents, employment, and commuting;
4. compare fixed-flow and equilibrium interpretations of a local productivity shock;
5. diagnose targeted and untargeted fit in bilateral flows;
6. separate estimated, calibrated, observed, and imposed objects;
7. evaluate counterfactual sensitivity to commuting frictions and housing supply;
8. explain when a dynamic transition path changes the interpretation of a static spatial counterfactual.

## Required Local Structure

```text
labs/17-spatial-structural-modeling/
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
      locations_synthetic.csv
      bilateral_commuting_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      dynamic_policy_synthetic.csv
  src/
    spatial_model.py
    make_synthetic_data.py
    reproduce_spatial_flows.py
    diagnose_structural_fit.py
    transfer_dynamic_spatial.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs four steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_spatial_flows.py --locations original/reduced/locations_synthetic.csv --flows original/reduced/bilateral_commuting_synthetic.csv --outdir output/reproduced
python src/diagnose_structural_fit.py --locations original/reduced/locations_synthetic.csv --flows original/reduced/bilateral_commuting_synthetic.csv --outdir output/reproduced
python src/transfer_dynamic_spatial.py --locations original/reduced/locations_synthetic.csv --flows original/reduced/bilateral_commuting_synthetic.csv --policy transfer/data/dynamic_policy_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Commuting-Flow And Incidence Object

### Objective

Estimate a compact commuting gravity block and compare fixed-flow versus equilibrium interpretations of a local productivity shock.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/commuting_gravity_estimates.csv`.
4. Open `output/reproduced/commuting_openness.csv`.
5. Open `output/reproduced/baseline_equilibrium.csv`.
6. Open `output/reproduced/productivity_counterfactual.csv`.
7. Open `output/reproduced/incidence_summary.csv`.

### Required Questions

- What does the flow-cost coefficient in the gravity regression mean?
- Which locations are most open to commuting?
- How does the productivity shock change employment and residents in the shocked location?
- How does the fixed-flow interpretation differ from the equilibrium interpretation?
- Why are wages alone not a welfare object?
- Why is this not an official replication of Monte, Redding, and Rossi-Hansberg?

### Minimum Output

- one paragraph interpreting the gravity coefficient;
- one table or paragraph on commuting openness;
- one paragraph comparing fixed-flow and equilibrium incidence;
- one sentence stating that this is a synthetic teaching reproduction rather than an official replication.

## Part II. Diagnose Structural Fit And Assumptions

### Objective

Evaluate whether the model's counterfactual is disciplined by bilateral data or by closure assumptions.

### Student Tasks

1. Open `output/reproduced/flow_fit_diagnostics.csv`.
2. Open `output/reproduced/parameter_audit.csv`.
3. Open `output/reproduced/counterfactual_sensitivity.csv`.
4. Open `output/reproduced/diagnostic_prompts.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Which objects are estimated from flows?
- Which objects are calibrated, observed in synthetic data, or imposed by counterfactual design?
- Does the gravity block fit long-distance commuting as well as short-distance commuting?
- How sensitive is the counterfactual to commuting costs?
- How sensitive is rent incidence to housing supply?
- Where would a reduced-form spatial design stop?

### Minimum Output

- one targeted-fit paragraph;
- one estimated-versus-calibrated paragraph;
- one sensitivity paragraph;
- one validation paragraph;
- one final sentence stating whether equilibrium structure is needed for the question being asked.

## Part III. Transfer To Dynamic Spatial Adjustment

### Objective

Transfer the logic to a frontier-style dynamic setting where transition paths matter.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/dynamic_transition_path.csv`.
3. Open `output/transfer/transition_summary.csv`.
4. Open `output/transfer/dynamic_frontier_prompts.csv`.
5. Write a short Transfer memo.

### Required Prompts

- What changes between impact, medium-run, and long-run outcomes?
- Which locations bear transition costs when migration is slow?
- How does gradual rent adjustment alter incidence?
- What would a full dynamic urban model need beyond this teaching path?
- When is dynamic structure necessary rather than decorative?

### Minimum Output

- one transition-path paragraph;
- one paragraph comparing impact and long-run welfare;
- one paragraph identifying missing dynamic objects;
- one paragraph explaining whether the static model would answer the research question.

## Deliverables Checklist

- [ ] run log;
- [ ] gravity coefficient interpretation;
- [ ] commuting openness summary;
- [ ] fixed-flow versus equilibrium incidence memo;
- [ ] targeted and untargeted fit memo;
- [ ] parameter audit memo;
- [ ] sensitivity memo;
- [ ] dynamic transition memo;
- [ ] final paragraph explaining what spatial equilibrium structure adds and what remains assumption-dependent.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Commuting gravity interpretation | 20 |
| Equilibrium incidence interpretation | 25 |
| Fit, parameter, and sensitivity diagnosis | 30 |
| Dynamic transfer memo | 15 |
| Code organization and communication | 10 |

## Instructor Notes

- The locations, flows, and policy shock are synthetic and intentionally small enough for local smoke testing.
- The spatial solver is a teaching fixed point over residence-workplace choices, wages, rents, and utility; it is not a frontier quantitative spatial model.
- The dynamic transfer is an adjustment-path exercise, not a full dynamic programming model.
- The important learning outcome is not numerical accuracy. It is the ability to see what the equilibrium closure is doing.
