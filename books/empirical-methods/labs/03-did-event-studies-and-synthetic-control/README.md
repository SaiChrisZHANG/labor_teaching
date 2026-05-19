# Week 3 lab README

This folder contains the Week 3 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs the reproduce/diagnose workflow, runs the synthetic-control transfer workflow, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md` and `lab.md`.
3. Inspect `output/reproduced/card_krueger_did_estimates.csv`, `group_time_att.csv`, `modern_did_comparison.csv`, and `event_time_support.csv`.
4. Write the Diagnose memo before beginning the synthetic-control transfer exercise.
5. Use the transfer data as a template for a bounded city, state, firm, or market-level synthetic-control project.

## Notes

- The lab is inspired by Card and Krueger and by the modern DID/synthetic-control literature, but it is not an official replication of any paper.
- Synthetic data are included only to make design logic concrete and testable.
- Python is the public teaching path for this lab.
