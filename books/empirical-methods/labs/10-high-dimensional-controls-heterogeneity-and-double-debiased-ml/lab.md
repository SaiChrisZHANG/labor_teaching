# Code Lab 10: High-Dimensional Controls, Heterogeneity, And Double/Debiased ML

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 10 - high-dimensional controls, heterogeneity, and double/debiased ML  
**Associated chapter:** `10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md`  
**Lab slug:** `10-high-dimensional-controls-heterogeneity-and-double-debiased-ml`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** regression adjustment, lasso intuition, train/test logic, basic `pandas`  
**Core economic question:** How can flexible methods help estimate causal effects without turning nuisance prediction into the answer?  
**Core design / estimator:** post-double selection, cross-fitted residual-on-residual DML, overlap diagnostics, lightweight honest-tree heterogeneity  
**Source paper spine:** Dube et al. [@dubeMonopsonyOnlineLabor2020], Chernozhukov et al. [@chernozhukovDoubleDebiasedMachine2018], and Davis and Heller [@davisUsingCausalForests2017]

## Why This Lab Exists

Lecture 10 argues that high-dimensional controls and flexible learners are useful only when they serve a clear causal design. This lab makes that discipline executable. Students first reproduce the architecture of a double/debiased machine-learning estimate in a synthetic online labor-market setting inspired by Dube et al. They then diagnose whether the estimate is credible by examining overlap, nuisance fit, fold stability, and leakage. Finally, they transfer the logic to treatment-effect heterogeneity in a synthetic youth employment program inspired by causal-forest applications.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on orthogonalization, cross-fitting, post-double selection, overlap, honest heterogeneity, and reporting discipline.

## Learning Objectives

By the end of this lab, students should be able to:

1. define a low-dimensional causal target before training nuisance learners;
2. implement cross-fitted residual-on-residual DML;
3. compare low-dimensional OLS, high-dimensional OLS, post-double selection, and DML;
4. interpret outcome and treatment nuisance diagnostics without treating them as the answer;
5. audit overlap support and feature leakage;
6. diagnose fold instability and learner sensitivity;
7. estimate subgroup CATEs and compare them with a simple interaction benchmark;
8. explain why an honest heterogeneity split is not itself a causal mechanism.

## Required Local Structure

```text
labs/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml/
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
      online_labor_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      youth_program_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_dml_online_labor.py
    transfer_heterogeneity.py
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
python src/reproduce_dml_online_labor.py --input original/reduced/online_labor_synthetic.csv --outdir output/reproduced
python src/transfer_heterogeneity.py --input transfer/data/youth_program_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A DML Workflow

### Objective

Estimate the effect of high client concentration on log hourly wages in a synthetic online labor-market dataset.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/baseline_estimates.csv`.
4. Open `output/reproduced/post_double_selection_estimate.csv`.
5. Open `output/reproduced/dml_estimates.csv`.
6. Open `output/reproduced/residualized_scores.csv`.

### Required Questions

- What is the target parameter?
- Which controls are pre-treatment nuisance predictors?
- How does the DML estimate compare with low-dimensional and high-dimensional OLS?
- What nuisance functions are estimated before residualizing?
- Why is this not an official replication of Dube et al.?
- What does the DML estimate identify under the synthetic selection-on-observables design?

### Minimum Output

- one paragraph defining the outcome, treatment, controls, and target parameter;
- one table or paragraph comparing low-dimensional OLS, high-dimensional OLS, post-double selection, and DML;
- one sentence explaining why the exercise reproduces design logic rather than published estimates.

## Part II. Diagnose The Design

### Objective

Evaluate whether the DML result is credible and interpretable.

### Student Tasks

1. Open `output/reproduced/fold_diagnostics.csv`.
2. Open `output/reproduced/overlap_summary.csv`.
3. Inspect `output/reproduced/overlap_plot.png`.
4. Open `output/reproduced/learner_sensitivity.csv`.
5. Open `output/reproduced/leakage_audit.csv`.
6. Open `output/reproduced/selection_stability.csv`.
7. Write a one-page Diagnose memo.

### Required Prompts

- Is treatment overlap strong enough for the reported estimand?
- Do nuisance models predict outcome and treatment well enough to be useful, without becoming the target?
- Does the treatment estimate move across ridge penalties?
- Which feature is leakage, and why?
- Are selected controls stable enough to interpret substantively?
- What remaining identifying assumption is not tested by DML?

### Minimum Output

- one overlap paragraph;
- one nuisance and fold-stability paragraph;
- one leakage paragraph;
- one sentence stating whether DML sharpens a credible design or hides design uncertainty.

## Part III. Transfer To Heterogeneity

### Objective

Use a synthetic youth employment program to decide whether treatment-effect heterogeneity is substantively meaningful.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/interaction_benchmark.csv`.
3. Open `output/transfer/cate_by_risk.csv`.
4. Inspect `output/transfer/cate_by_risk.png`.
5. Open `output/transfer/honest_tree_effects.csv`.
6. Open `output/transfer/heterogeneity_validation.csv`.
7. Open `output/transfer/overlap_by_risk.csv`.
8. Write a short Transfer memo.

### Required Prompts

- Is baseline risk a substantively meaningful heterogeneity dimension?
- Do risk-group CATEs align with the simple interaction benchmark?
- Does the honest split validate on the evaluation half?
- Does overlap vary by risk group?
- What uncertainty would a publishable causal-forest paper need to report?
- Why is variable importance or a selected split not automatically a mechanism?

### Minimum Output

- one paragraph comparing interaction and subgroup CATE evidence;
- one paragraph on honest-tree validation;
- one paragraph on overlap and uncertainty;
- one final paragraph saying whether the heterogeneity claim is exploratory or confirmatory.

## Deliverables Checklist

- [ ] run log;
- [ ] target-parameter paragraph;
- [ ] baseline versus DML comparison;
- [ ] post-double-selection interpretation;
- [ ] fold diagnostics memo;
- [ ] overlap diagnostic;
- [ ] leakage audit paragraph;
- [ ] learner-sensitivity discussion;
- [ ] subgroup CATE table;
- [ ] honest-tree validation memo;
- [ ] final paragraph stating what the methods identify and what they do not identify.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| DML target and orthogonalization interpretation | 25 |
| Cross-fitting and nuisance diagnostics | 20 |
| Overlap, leakage, and learner sensitivity | 25 |
| Heterogeneity transfer and uncertainty | 20 |
| Code organization and communication | 10 |

## Instructor Notes

- The online labor and youth-program data are synthetic and intentionally small enough for local smoke testing.
- The DML script uses transparent ridge nuisance learners and a simple lasso-style selector for post-double selection.
- The heterogeneity transfer uses a lightweight honest-tree exercise rather than a frontier causal-forest package. The point is to teach honesty, support, and validation before package-specific syntax.
- The important learning outcome is not numerical accuracy. It is the ability to explain when high-dimensional causal tools help and when they are being abused.
