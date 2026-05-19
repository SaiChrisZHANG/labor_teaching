# Week 1 lab README

This folder contains the Week 1 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs the reproduce and transfer scripts, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md` and `lab.md`.
3. Inspect `output/reproduced/estimates.csv`, `balance_diagnostics.csv`, and `overlap_summary.csv`.
4. Write the Diagnose memo before beginning the transfer exercise.
5. Use the transfer data as a template for a bounded observational design with richer real data.

## Notes

- The lab is inspired by LaLonde and Dehejia-Wahba, but it is not an official replication of the National Supported Work estimates.
- Synthetic data are included only to make the design logic concrete and testable.
- Python is the public teaching path for this lab.
