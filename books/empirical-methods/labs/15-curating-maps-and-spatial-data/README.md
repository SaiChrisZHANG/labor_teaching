# Week 15 lab README

This folder contains the Week 15 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, constructs a commuting-zone exposure object, diagnoses geography and crosswalk sensitivity, and transfers the curation logic to a job-access measurement task.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/cz_exposure.csv`, `tract_exposure_assignment.csv`, and `downstream_comparison.csv`.
4. Write the Diagnose memo using `maup_sensitivity.csv`, `crosswalk_weighting_sensitivity.csv`, `geocoding_jitter_sensitivity.csv`, and `boundary_edge_audit.csv`.
5. Use `output/transfer/job_access_measures.csv`, `access_group_comparison.csv`, and `buffer_vs_kernel_access.csv` to write the Transfer memo.

## Notes

- The lab is inspired by commuting-zone exposure work, tract-level neighborhood exposure work, and job-access research.
- It is not an official replication of any published paper.
- The lab does not require proprietary shapefiles, live geocoding, or routing APIs.
- Python is the public teaching path for this lab.
