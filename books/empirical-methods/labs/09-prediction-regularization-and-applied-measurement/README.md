# Week 9 lab README

This folder contains the Week 9 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, trains regularized prediction rules for a job-posting measurement task, writes calibration and subgroup diagnostics, and transfers the same measurement logic to occupational title classification.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/train_test_metrics.csv`, `cv_results.csv`, and `calibration_by_bin.csv`.
4. Write the Diagnose memo before opening the occupation-title transfer outputs.
5. Use `output/transfer/transport_metrics.csv`, `vocabulary_coverage.csv`, and `transfer_scores.csv` to write the Transfer memo.

## Notes

- The lab is inspired by applied economics papers that use ML for job-posting and occupational measurement, but it is not an official replication of any paper.
- Synthetic data are included only to make prediction targets, regularization, calibration, leakage, and transportability concrete.
- Python is the public teaching path for this lab.
