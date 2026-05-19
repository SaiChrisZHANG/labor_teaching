# Week 13 lab README

This folder contains the Week 13 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, validates a constructed remote-work feasibility measure from labeled job-posting text, diagnoses calibration and subgroup failures, and transfers the validation workflow to shifted service-record text with a small image-based proxy.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/inter_rater_reliability.csv`, `classification_metrics.csv`, `confusion_matrix.csv`, and `calibration_by_bin.csv`.
4. Write the Diagnose memo using `subgroup_performance.csv`, `threshold_sensitivity.csv`, `error_audit.csv`, and `measurement_error_downstream.csv`.
5. Use `output/transfer/transport_metrics.csv`, `vocabulary_shift.csv`, `transfer_subgroup_performance.csv`, and `benchmark_redesign_notes.csv` to write the Transfer memo.

## Notes

- The lab is inspired by applied economics work on validation of unstructured-data measures.
- It is not an official replication of any published paper.
- Synthetic data are included only to make benchmark design, human review, calibration, subgroup performance, drift, and downstream measurement error concrete.
- Python is the public teaching path for this lab.
