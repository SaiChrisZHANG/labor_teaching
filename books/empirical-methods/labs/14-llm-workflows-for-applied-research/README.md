# Week 14 lab README

This folder contains the Week 14 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, runs an API-free LLM-workflow surrogate, writes prompt logs and structured outputs, evaluates benchmark performance, diagnoses prompt sensitivity and audit flags, and transfers the workflow to a new workforce case-note domain.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/prompt_log.csv`, `structured_outputs.csv`, and `classification_metrics.csv`.
4. Write the Diagnose memo using `prompt_sensitivity.csv`, `subgroup_stability.csv`, `hallucination_audit.csv`, and `human_review_queue.csv`.
5. Use `output/transfer/transport_metrics.csv`, `vocabulary_shift.csv`, `transfer_prompt_sensitivity.csv`, and `benchmark_redesign_notes.csv` to write the Transfer memo.

## Notes

- The lab is inspired by economics work on LLM-assisted measurement, labor-market mismatch, document extraction, and synthetic social-science workflows.
- It is not an official replication of any published paper.
- The lab does not call a live model API; it uses a deterministic teaching surrogate so prompt logging and audit trails are reproducible.
- Python is the public teaching path for this lab.
