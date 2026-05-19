# Code Lab 01: Selection-On-Observables As A Research Design

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 1 - Potential outcomes, identification logic, and selection-on-observables  
**Associated chapter:** `01-potential-outcomes-identification-logic-and-selection-on-observables.md`  
**Lab slug:** `01-potential-outcomes-identification-logic-and-selection-on-observables`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, basic regression, basic `pandas`, comfort reading diagnostic tables  
**Core economic question:** When can observed pre-treatment information make treated and untreated units credible counterfactuals for one another?  
**Core design / estimator:** selection-on-observables, matching, weighting, regression adjustment, and doubly robust logic  
**Source paper spine:** LaLonde [@lalonde1986], Dehejia and Wahba [@dehejiaWahba1999; @dehejiaWahba2002], Rosenbaum and Rubin [@rosenbaumRubin1983], and sensitivity-style work [@altonjiElderTaber2005; @oster2019]

## Why This Lab Exists

The lecture argues that selection-on-observables is a design, not a button. This lab makes that discipline concrete. Students work with a synthetic LaLonde-style training dataset that contains treatment status, pre-treatment earnings, demographics, and post-treatment earnings. The assignment is to estimate treatment effects several ways, then diagnose what each estimate requires us to believe about the missing potential outcome.

The lab does not reproduce official National Supported Work magnitudes. It reproduces the design logic: naive comparisons can be misleading; covariate adjustment can matter; common support and balance are not optional; and robustness to hidden selection is part of interpretation.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate naive, regression-adjusted, matching, IPW, and doubly robust comparisons on a bounded teaching dataset;
2. explain which target parameter each estimate is closest to;
3. diagnose balance, overlap, and weighting stability;
4. distinguish estimator choice from identifying assumption;
5. write a short design memo that states what is observed, what is missing, and what assumption links them;
6. transfer the same design logic to a new observational setting.

## Required Local Structure

```text
labs/01-potential-outcomes-identification-logic-and-selection-on-observables/
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
      training_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      workplace_training_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_selection_on_observables.py
    transfer_design_diagnostics.py
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
python src/reproduce_selection_on_observables.py --input original/reduced/training_synthetic.csv --outdir output/reproduced
python src/transfer_design_diagnostics.py --input transfer/data/workplace_training_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce The Design Logic

### Objective

Estimate how a training program affects post-treatment earnings under several versions of the comparison-group design.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path and open `output/reproduced/estimates.csv`.
3. Compare the naive difference, regression adjustment, nearest-neighbor matching, IPW, ATT weighting, and doubly robust estimates.
4. Write a short paragraph explaining why the estimates differ.

### Required Questions

- Which estimate is closest to an ATT?
- Which estimate targets the ATE most directly?
- Which estimates rely most heavily on the propensity-score model?
- Which estimates would become fragile if overlap were weak?

### Minimum Output

- `output/reproduced/estimates.csv`;
- one paragraph describing the target parameter and comparison group;
- one sentence stating the maintained identifying assumption.

## Part II. Diagnose The Design

### Objective

Move from "I estimated it" to "I know what the design requires."

### Student Tasks

1. Open `output/reproduced/balance_diagnostics.csv`.
2. Open `output/reproduced/overlap_summary.csv`.
3. Inspect the propensity-score overlap plot and balance plot.
4. Write a one-page Diagnose memo.

### Required Prompts

- Which covariates are most imbalanced before adjustment?
- Does weighting improve balance?
- Are there treated units without plausible untreated comparisons?
- Are a few observations likely to drive the weighted estimate?
- What unobserved variable would most threaten the design?

### Minimum Output

- one balance interpretation paragraph;
- one overlap interpretation paragraph;
- one omitted-variable paragraph using sensitivity language.

## Part III. Transfer The Design

### Objective

Use the same logic in a different observational setting: take-up of workplace training.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Run `src/transfer_design_diagnostics.py`.
3. Open `output/transfer/transfer_estimates.csv`.
4. State whether the design is closer to an ATT, ATE, or ATC question.
5. Write a short design memo for a real-data version of the project.

### Required Prompts

- Why do workers select into the training?
- Which observed variables proxy for that selection story?
- What remains unobserved?
- Would you defend a causal interpretation, a descriptive adjusted association, or a sensitivity exercise?
- What extra data would most improve the design?

### Minimum Output

- one transfer estimates table;
- one transfer balance table;
- one design memo with target parameter, assignment story, observables, and omitted-variable threat.

## Deliverables Checklist

- [ ] run log;
- [ ] reproduce estimates table;
- [ ] balance and overlap diagnosis;
- [ ] one-page Diagnose memo;
- [ ] transfer estimates and diagnostics;
- [ ] transfer design memo;
- [ ] final interpretation paragraph that states the maintained assumption.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Reproduction estimates and run log | 20 |
| Balance, overlap, and support diagnosis | 25 |
| Correct target-parameter interpretation | 20 |
| Transfer design memo | 25 |
| Code organization and communication | 10 |

## Instructor Notes

- The lab is intentionally synthetic so students can focus on design logic before wrestling with official replication-package details.
- The best class discussion compares estimates rather than picking a winner mechanically.
- The transfer exercise should be bounded. Students should not turn it into a full causal paper in Week 1.
