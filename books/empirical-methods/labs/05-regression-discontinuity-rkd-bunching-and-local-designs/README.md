# Week 5 lab README

This folder contains the Week 5 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs the close-election RD reproduce/diagnose workflow, runs the tax-kink bunching transfer workflow, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/rd_estimates.csv`, `bandwidth_kernel_sensitivity.csv`, `covariate_continuity.csv`, and `density_check.csv`.
4. Write the RD Diagnose memo before beginning the bunching transfer exercise.
5. Use the transfer data as a template for a bounded bunching design memo.

## Notes

- The lab is inspired by close-election RD and tax-kink bunching designs, but it is not an official replication of any paper.
- Synthetic data are included only to make design logic concrete and testable.
- Python is the public teaching path for this lab.
