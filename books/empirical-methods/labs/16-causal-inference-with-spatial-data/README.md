# Week 16 lab README

This folder contains the Week 16 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, estimates a contiguous-border design, diagnoses spatial identification risks, and transfers the design logic to shift-share exposure diagnostics.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/border_design_estimates.csv` and `conley_cutoff_sensitivity.csv`.
4. Write the Diagnose memo using `border_balance.csv`, `pair_balance_audit.csv`, `spillover_exposure_audit.csv`, and `comparison_set_sensitivity.csv`.
5. Use `output/transfer/shift_share_exposure.csv`, `dominant_contributions.csv`, `share_diagnostics.csv`, and `transfer_estimates.csv` to write the Transfer memo.

## Notes

- The lab is inspired by contiguous-border designs and modern shift-share diagnostics.
- It is not an official replication of any published paper.
- The lab does not require proprietary shapefiles, confidential county data, or live geocoding.
- Python is the public teaching path for this lab.
