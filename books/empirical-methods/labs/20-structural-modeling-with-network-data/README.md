# Week 20 lab README

This folder contains the Week 20 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, estimates a small structural link-formation and behavior-on-network workflow, diagnoses validation burdens, and transfers the logic to a referral-search counterfactual.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/formation_model_estimates.csv`, `network_moments.csv`, and `behavior_on_network_estimates.csv`.
4. Compare `output/reproduced/fixed_vs_endogenous_counterfactual.csv` with `counterfactual_sensitivity.csv`.
5. Use `output/transfer/referral_policy_counterfactuals.csv`, `referral_access_summary.csv`, and `transfer_prompts.csv` for the Transfer memo.

## Notes

- The primary structural-network anchor is Mele on dense network formation, with Graham on degree heterogeneity as the econometric companion.
- The transfer anchor is Galenianos on referral networks and inequality, with referral-search links to Dustmann, Glitz, Schonberg, and Bruderl.
- This is not an official replication of any published paper.
- The lab uses deterministic synthetic data to keep the teaching path public and reproducible.
- Python is the public teaching path for this lab.
