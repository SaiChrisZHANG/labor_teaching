# Code Lab 09: Prediction, Regularization, And Applied Measurement

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 9 - prediction, regularization, and applied measurement  
**Associated chapter:** `09-prediction-regularization-and-applied-measurement.md`  
**Lab slug:** `09-prediction-regularization-and-applied-measurement`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** train/test logic, basic linear regression intuition, basic `pandas`  
**Core economic question:** When is prediction itself the research object, and when is it an input into measurement or design?  
**Core design / estimator:** train/test validation, cross-validation, ridge/lasso/elastic-net regularization, calibration and transportability diagnostics  
**Source paper spine:** Dahlhaus et al. [@dahlhausFromOnlineJob2025], Ikudo [@ikudoOccupationalClassificationsMachine2018], and Hansen et al. [@hansenRemoteWorkAcross2023]

## Why This Lab Exists

Lecture 9 argues that prediction is useful in applied economics only when the predicted object is tied to a research use. This lab makes that discipline executable. Students first reproduce the architecture of a job-posting measurement exercise inspired by Dahlhaus et al.: define a label, train a prediction rule, tune regularization, and validate the predicted object. They then diagnose whether the output is credible for downstream economics. Finally, they transfer the measurement object to terse occupation titles in the spirit of Ikudo and evaluate transportability.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on prediction targets, regularization, calibration, leakage, class imbalance, and downstream measurement.

## Learning Objectives

By the end of this lab, students should be able to:

1. define a prediction target and loss in economics language;
2. split data into training and test samples without using the test set for tuning;
3. tune ridge, lasso, and elastic-net penalties with cross-validation;
4. compare regularized models to simple baselines;
5. report calibration, subgroup performance, and feature-weight diagnostics;
6. identify target leakage before modeling;
7. evaluate whether a predicted score can be used as a downstream economic measure;
8. diagnose transportability when a posting classifier is applied to occupation titles.

## Required Local Structure

```text
labs/09-prediction-regularization-and-applied-measurement/
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
      job_postings_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      occupation_titles_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_prediction_measurement.py
    transfer_occupation_measurement.py
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
python src/reproduce_prediction_measurement.py --input original/reduced/job_postings_synthetic.csv --outdir output/reproduced
python src/transfer_occupation_measurement.py --train-input original/reduced/job_postings_synthetic.csv --input transfer/data/occupation_titles_synthetic.csv --outdir output/transfer --reproduced-outdir output/reproduced
```

## Part I. Reproduce A Job-Posting Measurement Workflow

### Objective

Train and evaluate a technology-intensive posting classifier using regularized prediction rules.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/cv_results.csv`.
4. Open `output/reproduced/train_test_metrics.csv`.
5. Open `output/reproduced/top_feature_weights.csv`.
6. Inspect `output/reproduced/calibration_by_bin.png`.

### Required Questions

- What is the prediction target?
- Why is this target an economic measurement object rather than a generic label?
- Which model and penalty did cross-validation select?
- Does the selected model beat the keyword rule on held-out Brier loss?
- How should the top feature weights be interpreted?
- Why is this not an official replication of any job-postings paper?

### Minimum Output

- one paragraph defining the target, features, and loss;
- one table or paragraph comparing baselines with ridge, lasso, and elastic net;
- one sentence explaining why the exercise is a teaching reproduction of logic rather than a data replication.

## Part II. Diagnose Measurement Credibility

### Objective

Evaluate whether the predicted posting score is fit for downstream economics.

### Student Tasks

1. Open `output/reproduced/calibration_by_bin.csv`.
2. Open `output/reproduced/subgroup_performance.csv`.
3. Open `output/reproduced/leakage_audit.csv`.
4. Open `output/reproduced/feature_stability.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Is the score calibrated enough to be interpreted as a probability?
- Does performance vary by sector or region?
- Which variable is leakage, and why?
- Would lasso-selected variables be stable enough to support substantive interpretation?
- What would go wrong if classification error were correlated with the policy or treatment in a later design?

### Minimum Output

- one calibration paragraph;
- one subgroup-error paragraph;
- one leakage paragraph;
- one final sentence stating whether the score is fit for a downstream labor-demand design.

## Part III. Transfer To Occupation-Title Measurement

### Objective

Use the posting classifier on terse occupation titles and diagnose transportability.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/transport_metrics.csv`.
3. Open `output/transfer/vocabulary_coverage.csv`.
4. Open `output/transfer/occupation_confusion_matrix.csv`.
5. Inspect `output/transfer/transfer_calibration_by_bin.png`.
6. Write a short Transfer memo.

### Required Prompts

- What changes when the input text is a short raw title rather than a full posting?
- Which title groups have low vocabulary coverage?
- Does calibration survive the transfer?
- Would the title classifier be credible for a study of occupational mobility by region?
- What human validation sample would a publishable paper need?

### Minimum Output

- one transfer-performance paragraph;
- one vocabulary and calibration paragraph;
- one paragraph on downstream use and validation;
- one paragraph comparing posting measurement with occupation-title measurement.

## Deliverables Checklist

- [ ] run log;
- [ ] train/test model comparison;
- [ ] cross-validation interpretation;
- [ ] calibration figure and table;
- [ ] subgroup performance memo;
- [ ] leakage audit paragraph;
- [ ] feature-weight or feature-stability discussion;
- [ ] transportability metrics;
- [ ] vocabulary coverage table;
- [ ] occupation-title transfer memo;
- [ ] final paragraph stating when prediction is fit for the economics question.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Prediction target and train/test interpretation | 20 |
| Regularization and tuning interpretation | 20 |
| Calibration, leakage, and subgroup diagnostics | 30 |
| Transfer and transportability analysis | 20 |
| Code organization and communication | 10 |

## Instructor Notes

- The synthetic posting and title files are intentionally small enough for local smoke testing.
- The regularized estimators use transparent teaching implementations rather than external ML packages.
- The transfer exercise is deliberately imperfect: the point is to show why a high-performing posting model may not transport to short administrative titles.
- The important learning outcome is not leaderboard accuracy. It is the ability to defend a predicted object as an economic measure.
