# Week 17 lab README

This folder contains the Week 17 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, estimates a commuting gravity block, solves a compact spatial-equilibrium counterfactual, diagnoses fit and sensitivity, and transfers the logic to a dynamic adjustment exercise.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/commuting_gravity_estimates.csv`, `commuting_openness.csv`, and `incidence_summary.csv`.
4. Write the Diagnose memo using `flow_fit_diagnostics.csv`, `parameter_audit.csv`, `counterfactual_sensitivity.csv`, and `diagnostic_prompts.csv`.
5. Use `output/transfer/dynamic_transition_path.csv`, `transition_summary.csv`, and `dynamic_frontier_prompts.csv` to write the Transfer memo.

## Notes

- The lab is inspired by spatial structural equilibrium work on commuting, migration, and local employment incidence.
- It is not an official replication of any published paper.
- The lab does not require confidential commuting microdata, proprietary routing data, or live geocoding.
- Python is the public teaching path for this lab.
