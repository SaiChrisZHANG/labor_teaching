# Week 18 lab README

This folder contains the Week 18 code lab for Empirical Methods.

## Fast Start

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path creates deterministic synthetic teaching data, constructs a neighborhood-employer network exposure object, diagnoses edge and boundary choices, and transfers the curation logic to a directed referral-program setting.

## Recommended Workflow

1. Run `smoke.sh` to verify the local environment.
2. Read `original/source-notes.md`, `transfer/data-notes.md`, and `lab.md`.
3. Inspect `output/reproduced/neighborhood_employer_bipartite.csv`, `network_summary_by_worker.csv`, and `descriptive_relationship.csv`.
4. Write the Diagnose memo using `definition_sensitivity.csv`, `missing_link_audit.csv`, `projection_audit.csv`, and `boundary_truncation_audit.csv`.
5. Use `output/transfer/referral_graph_metrics.csv`, `applicant_access_metrics.csv`, and `referral_inequality_summary.csv` to write the Transfer memo.

## Notes

- The lab is inspired by residential labor-market network, referral, and referral-inequality research.
- It is not an official replication of any published paper.
- The lab does not require confidential administrative data, survey rosters, or live platform records.
- Python is the public teaching path for this lab.
