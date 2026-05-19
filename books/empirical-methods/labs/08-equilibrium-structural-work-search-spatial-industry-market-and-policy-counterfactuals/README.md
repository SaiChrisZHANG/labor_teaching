# Week 8 lab README

This folder contains the Week 8 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, computes a Hsieh-Moretti-style spatial-equilibrium counterfactual, writes diagnosis and sensitivity outputs, and transfers the same equilibrium logic to a compact BLP/Nevo-style market-equilibrium pass-through exercise.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/aggregate_counterfactual_summary.csv`, `spatial_sensitivity.csv`, and `equilibrium_moment_fit.csv`.
4. Write the Diagnose memo before opening the market-transfer outputs.
5. Use `output/transfer/demand_estimates.csv`, `markup_recovery.csv`, and `market_counterfactual_summary.csv` to write the Transfer memo.

## Notes

- The lab is inspired by equilibrium structural papers such as Hsieh and Moretti, Berry-Levinsohn-Pakes, and Nevo, but it is not an official replication of any paper.
- Synthetic data are included only to make equilibrium fixed points, incidence, welfare, and validation burdens concrete.
- Python is the public teaching path for this lab.
