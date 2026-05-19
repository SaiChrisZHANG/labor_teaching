# Week 12 lab README

This folder contains the Week 12 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, builds remote-work measures from job-posting text, diagnoses measurement error and subgroup failures, and transfers the same measurement logic to a small multimodal setting with policy text, image, audio, and video features.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/classification_metrics.csv`, `remote_measure_scores.csv`, and `measurement_error_downstream.csv`.
4. Write the Diagnose memo using `subgroup_measurement_error.csv`, `dictionary_sensitivity.csv`, and `leakage_audit.csv`.
5. Use `output/transfer/modality_ablation.csv`, `transfer_multimodal_scores.csv`, and `source_vs_transfer_vocabulary.csv` to write the Transfer memo.

## Notes

- The lab is inspired by applied economics work on job-posting text, remote-work measurement, task exposure, and multimodal computational measurement.
- It is not an official replication of any published paper.
- Synthetic data are included only to make the mapping from raw signal to economic variable concrete.
- Python is the public teaching path for this lab.
