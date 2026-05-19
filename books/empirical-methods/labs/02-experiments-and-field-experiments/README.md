# Week 2 lab README

This folder contains the Week 2 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs the reproduce and transfer scripts, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md` and `lab.md`.
3. Inspect `output/reproduced/experimental_estimates.csv`, `balance_by_assignment.csv`, `attrition_by_assignment.csv`, and `exposure_summary.csv`.
4. Write the Diagnose memo before beginning the transfer exercise.
5. Use the transfer data as a template for a bounded saturation, platform, or labor-market experiment with richer real data.

## Notes

- The lab is inspired by Duflo and Saez and by labor-market spillover designs, but it is not an official replication of any paper.
- Synthetic data are included only to make design logic concrete and testable.
- Python is the public teaching path for this lab.
