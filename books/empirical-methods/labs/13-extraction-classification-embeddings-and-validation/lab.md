# Code Lab 13: Extraction, Classification, Embeddings, And Validation

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 13 - extraction, classification, embeddings, and validation  
**Associated chapter:** `13-extraction-classification-embeddings-and-validation.md`  
**Lab slug:** `13-extraction-classification-embeddings-and-validation`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** train/test splits, confusion matrices, basic prediction metrics, `pandas`  
**Core economic question:** When is a constructed unstructured-data variable credible enough for applied economics?  
**Core design / estimator:** annotation protocol, inter-rater reliability, dictionary baseline, embedding-style similarity, supervised baseline, calibration, subgroup diagnostics, downstream measurement-error audit, transfer validation  
**Source paper spine:** Gentzkow, Kelly, and Taddy [@gentzkowKellyTaddy2019], Hansen and coauthors [@hansenRemoteWorkAcross2023], Jean and coauthors [@jeanBurkeXieDavisLobellErmon2016], Gorodnichenko, Pham, and Talavera [@gorodnichenkoPhamTalavera2023], Haaland and coauthors [@haalandRothStantchevaWohlfart2024], Blattman and coauthors [@blattmanJamisonKoroknayPaliczRodriguesSheridan2016], and Bound, Brown, and Mathiowetz [@bound2001measurementError]

## Why This Lab Exists

Lecture 13 treats validation as part of identification. This lab makes that standard executable. Students do not only build a classifier. They construct and audit a benchmark, evaluate inter-rater reliability, compare diagnostics across methods, inspect subgroup failures, and ask how the constructed variable changes downstream economic interpretation.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on validation architecture rather than proprietary data access.

## Learning Objectives

By the end of this lab, students should be able to:

1. define the label and benchmark behind a constructed variable;
2. compute inter-rater reliability and explain what it does and does not prove;
3. compare precision, recall, F1, calibration, and threshold sensitivity;
4. diagnose subgroup performance and drift;
5. evaluate embedding-style similarity with external validation and human review;
6. show how measurement error changes a downstream slope;
7. transfer a validation protocol to a new domain before interpreting the measure.

## Required Local Structure

```text
labs/13-extraction-classification-embeddings-and-validation/
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
      validation_postings_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      service_records_shifted_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_validation_workflow.py
    transfer_validation_workflow.py
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
python src/reproduce_validation_workflow.py --input original/reduced/validation_postings_synthetic.csv --outdir output/reproduced
python src/transfer_validation_workflow.py --source-input original/reduced/validation_postings_synthetic.csv --input transfer/data/service_records_shifted_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Validation Workflow

### Objective

Validate a constructed remote-work feasibility measure from synthetic job-posting text.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/inter_rater_reliability.csv`.
4. Open `output/reproduced/classification_metrics.csv`.
5. Open `output/reproduced/confusion_matrix.csv`.
6. Open `output/reproduced/calibration_by_bin.csv`.
7. Compare dictionary, embedding-style, and supervised scores.

### Required Questions

- What is the target label: explicit remote permission, remote feasibility, hybrid flexibility, or task portability?
- What does the kappa statistic say about benchmark stability?
- Which method has the best precision, recall, F1, and calibration?
- Which metric is most relevant if the measure will be used for descriptive prevalence? Which if it will be used as a treatment variable?
- What human-review evidence would a real paper need before using this measure?

### Minimum Output

- one paragraph defining the benchmark;
- one paragraph interpreting inter-rater reliability;
- one table or paragraph comparing held-out diagnostics;
- one sentence explaining why validation is part of identification.

## Part II. Diagnose Validation Failures

### Objective

Evaluate whether the constructed variable is credible enough for downstream applied work.

### Student Tasks

1. Open `output/reproduced/subgroup_performance.csv`.
2. Open `output/reproduced/threshold_sensitivity.csv`.
3. Open `output/reproduced/error_audit.csv`.
4. Open `output/reproduced/external_validation.csv`.
5. Open `output/reproduced/measurement_error_downstream.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Which group has the largest false-negative or false-positive problem?
- Does the best threshold depend on the research use?
- Which false positives and false negatives would change an economic interpretation?
- Does embedding similarity validate against the external audit proxy?
- How much does the downstream slope change when the constructed measure replaces the simulation truth?

### Minimum Output

- one subgroup-performance paragraph;
- one calibration or threshold paragraph;
- one error-audit paragraph;
- one downstream measurement-error paragraph;
- one final sentence stating whether the measure is ready for descriptive, causal, or structural use.

## Part III. Transfer To A Shifted Domain

### Objective

Apply the source validation design to service-record text and an image-based infrastructure proxy.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/vocabulary_shift.csv`.
3. Open `output/transfer/transport_metrics.csv`.
4. Open `output/transfer/transfer_calibration_by_bin.csv`.
5. Open `output/transfer/transfer_subgroup_performance.csv`.
6. Open `output/transfer/benchmark_redesign_notes.csv`.
7. Write a short Transfer memo.

### Required Prompts

- How different is the transfer vocabulary from the source job-posting vocabulary?
- Does the source text model still validate in the new domain?
- Does the image proxy add signal or mostly introduce a new validation burden?
- Which subgroup or institution has the weakest transfer performance?
- What would need to be relabeled before a real paper used the measure?

### Minimum Output

- one source-transfer comparison paragraph;
- one transport-metrics paragraph;
- one benchmark-redesign paragraph;
- one paragraph explaining what would change if the transfer measure entered a causal design.

## Deliverables Checklist

- [ ] run log;
- [ ] benchmark-definition paragraph;
- [ ] inter-rater reliability interpretation;
- [ ] held-out metric comparison;
- [ ] confusion-matrix and calibration interpretation;
- [ ] subgroup validation memo;
- [ ] external-validation paragraph;
- [ ] downstream measurement-error paragraph;
- [ ] transfer vocabulary and transport memo;
- [ ] benchmark-redesign memo.

## Suggested Grading Rubric

- **Benchmark clarity:** The memo defines the economic object and label before discussing algorithms.
- **Diagnostic discipline:** The memo uses precision, recall, F1, calibration, and subgroup diagnostics appropriately.
- **Human-review logic:** The memo distinguishes inter-rater reliability from construct validity.
- **Downstream interpretation:** The memo explains how constructed-variable error affects later analysis.
- **Transfer conservatism:** The memo does not assume that source validation evidence travels automatically.
