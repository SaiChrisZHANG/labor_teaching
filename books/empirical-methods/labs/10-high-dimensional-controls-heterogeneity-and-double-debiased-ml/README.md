# Week 10 lab README

This folder contains the Week 10 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, estimates a cross-fitted residual-on-residual DML effect for an online labor-market setting, runs post-double-selection diagnostics, and transfers the logic to a treatment-effect heterogeneity exercise.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/dml_estimates.csv`, `fold_diagnostics.csv`, and `overlap_summary.csv`.
4. Write the Diagnose memo before opening the heterogeneity transfer outputs.
5. Use `output/transfer/cate_by_risk.csv`, `honest_tree_effects.csv`, and `heterogeneity_validation.csv` to write the Transfer memo.

## Notes

- The lab is inspired by applied economics papers using double machine learning and causal forests, but it is not an official replication of any paper.
- Synthetic data are included only to make orthogonalization, cross-fitting, overlap, leakage, and heterogeneity interpretation concrete.
- Python is the public teaching path for this lab.
