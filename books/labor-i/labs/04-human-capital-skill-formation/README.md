# Week 4 lab README

This folder contains the Week 4 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week4_synthetic_data.py

conda run -n research python src/reproduce_attanasio_human_capital.py \
  --input original/reduced/attanasio_parenting_rct_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_skill_formation.py \
  --input transfer/data/walters_center_quality_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Run the bounded synthetic path to verify the environment and plotting workflow.
2. Read `original/source-notes.md` for the relationship between the local teaching data and [@attanasioEtAl2020HumanCapital].
3. Keep the reproduction target to one treatment-effect contrast and one compact figure.
4. Use the transfer step for one quality-heterogeneity comparison only.
5. Document clearly which outputs come from the synthetic path and which would require official external replication materials.

## Notes

- The synthetic data are included only to make the Week 4 workflow teachable and fully local.
- The official article and replication package remain the intellectual benchmark for a closer reproduction.
- The smoke test verifies the bounded teaching path only.
