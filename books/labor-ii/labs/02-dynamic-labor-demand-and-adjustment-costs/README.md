# Week 2 lab README

This folder contains the Week 2 code lab for Labor II.

## Fast start

```bash
conda run -n research python src/reproduce_dibiasi_adjustment.py \
  --input original/reduced/dibiasi_adjustment_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_dynamic_adjustment.py \
  --input transfer/data/dynamic_adjustment_scenarios.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Run the reduced pedagogical scripts to verify the environment.
2. Read `original/source-notes.md`.
3. Write the diagnose memo before extending the transfer exercise.
4. Keep the transfer path focused on convex versus nonconvex adjustment and policy timing.

## Notes

- Synthetic data are included only to keep the pipeline local and deterministic.
- `@dibiasiMikoschSarferaz2025` is the design anchor, not a full shipped replication package.
- `@caballeroEngelHaltiwanger1997` is the challenge bridge for lumpiness.
- `@saezSchoeferSeim2019` is the optional extension bridge for policy timing and incidence.
