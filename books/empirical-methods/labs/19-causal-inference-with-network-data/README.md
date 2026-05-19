# Week 19 lab README

This folder contains the Week 19 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, reproduces a workplace peer-exposure design, diagnoses reflection and interference risks, and transfers the logic to referral dyads with dependence-aware inference.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/team_saturation_summary.csv`, `leave_one_out_peer_measures.csv`, and `direct_spillover_estimates.csv`.
4. Write the Diagnose memo using `exposure_mapping_sensitivity.csv`, `reflection_diagnostics.csv`, `randomization_inference_summary.csv`, and `partial_interference_audit.csv`.
5. Use `output/transfer/dyadic_model_estimates.csv`, `dyadic_dependence_audit.csv`, and `referral_access_summary.csv` to write the Transfer memo.

## Notes

- The primary anchor is Cornelissen, Dustmann, and Schonberg on workplace peer effects.
- The transfer anchor is Pallais and Sands on referral experiments, with referral-network inequality as an extension.
- This is not an official replication of any published paper.
- The lab uses deterministic synthetic data to keep the teaching path public and reproducible.
- Python is the public teaching path for this lab.
