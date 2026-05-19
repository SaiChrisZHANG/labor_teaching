# Week 6 lab README

This folder contains the Week 6 code lab for Empirical Methods.

## Fast start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs a Rust-style dynamic replacement reproduce/diagnose workflow, runs a simplified career-choice transfer workflow, and writes outputs under `output/`.

## Recommended workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/replacement_estimates.csv`, `replacement_state_ccps.csv`, `state_support.csv`, and `counterfactual_replacement_cost.csv`.
4. Write the dynamic-choice Diagnose memo before beginning the career-choice transfer exercise.
5. Use the transfer data as a template for a bounded structural design memo.

## Notes

- The lab is inspired by dynamic discrete-choice and lifecycle career-choice papers, especially Rust and Keane-Wolpin, but it is not an official replication of any paper.
- Synthetic data are included only to make structural logic concrete and testable.
- Python is the public teaching path for this lab.
