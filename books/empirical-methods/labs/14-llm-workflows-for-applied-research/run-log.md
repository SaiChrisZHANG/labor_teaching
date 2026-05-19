# Week 14 lab run log

Use this file to record local runs of the Week 14 smoke path.

## Smoke Path

```bash
ENV_NAME=research bash smoke.sh
```

Expected outputs:

- `original/reduced/labor_mismatch_documents_synthetic.csv`
- `transfer/data/workforce_case_notes_synthetic.csv`
- `output/reproduced/prompt_log.csv`
- `output/reproduced/structured_outputs.csv`
- `output/reproduced/classification_metrics.csv`
- `output/reproduced/prompt_sensitivity.csv`
- `output/reproduced/subgroup_stability.csv`
- `output/reproduced/human_review_queue.csv`
- `output/reproduced/downstream_estimates.csv`
- `output/transfer/transport_metrics.csv`
- `output/transfer/vocabulary_shift.csv`
- `output/transfer/benchmark_redesign_notes.csv`

## Notes

- The smoke path uses deterministic synthetic data.
- No live model API is called.
- Treat non-fatal environment warnings as acceptable only if the required outputs are created.
