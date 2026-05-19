# Week 7 lab README

This folder contains the Week 7 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, estimates a Rust-style replacement model with likelihood and moment criteria, writes fit and inference diagnostics, and runs a simulated-moments transfer exercise for a simplified schooling/work lifecycle model.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/targeted_moment_fit.csv`, `moment_estimates.csv`, `variance_summary.csv`, and `counterfactual_uncertainty.csv`.
4. Write the Diagnose memo before opening the transfer outputs.
5. Use `output/transfer/smm_moment_fit.csv` and `policy_transfer_summary.csv` to write the Transfer memo.

## Notes

- The lab is inspired by structural estimation papers such as Rust, Todd and Wolpin, and Adda, Dustmann, and Stevens, but it is not an official replication of any paper.
- Synthetic data are included only to make identification, estimation, fit, counterfactuals, and inference concrete.
- Python is the public teaching path for this lab.
