# Week 4 lab README

This folder contains the Week 4 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs the compulsory-schooling IV reproduce/diagnose workflow, runs the shift-share transfer workflow, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md` and `lab.md`.
3. Inspect `output/reproduced/iv_estimates.csv`, `first_stage_diagnostics.csv`, `balance_by_instrument.csv`, and `complier_profile.csv`.
4. Write the Diagnose memo before beginning the shift-share transfer exercise.
5. Use the transfer data as a template for a bounded instrument-design memo.

## Notes

- The lab is inspired by compulsory-schooling IV, leave-out leniency, and shift-share designs, but it is not an official replication of any paper.
- Synthetic data are included only to make design logic concrete and testable.
- Python is the public teaching path for this lab.
