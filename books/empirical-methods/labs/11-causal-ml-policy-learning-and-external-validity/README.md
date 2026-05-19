# Week 11 lab README

This folder contains the Week 11 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, learns feasible job-training assignment rules, evaluates policy value and regret on held-out data, audits overlap and fairness, and then transfers the source-trained rule to a shifted target population.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/policy_value_comparison.csv` and `learned_policy_rule.csv`.
4. Write the Diagnose memo using `overlap_diagnostics.csv` and `fairness_audit.csv`.
5. Use `output/transfer/policy_transfer_values.csv`, `source_vs_target_covariates.csv`, and `transport_weight_summary.csv` to write the Transfer memo.

## Notes

- The lab is inspired by applied economics work on empirical welfare maximization, policy learning, algorithmic assignment, and external validity.
- It is not an official replication of any published paper.
- Synthetic data are included only to make policy value, regret, targeting, fairness, and transportability concrete.
- Python is the public teaching path for this lab.
