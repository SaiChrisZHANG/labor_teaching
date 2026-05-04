# Week 5 lab README

This folder contains the Week 5 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week5_synthetic_data.py

conda run -n research python src/reproduce_oreopoulos_returns.py \
  --input original/reduced/oreopoulos_schooling_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_schooling_trends.py \
  --input transfer/data/stephens_yang_trends_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the local synthetic teaching files and verify the environment.
2. Run the bounded reproduction in the spirit of `@oreopoulos2006`.
3. Read `original/source-notes.md` before interpreting the outputs as a literal paper replication.
4. Use the transfer step to compare a pooled IV object with a trend-adjusted one in the spirit of `@stephensYang2014`.
5. Treat the optional sorting extension in `lab.md` as a conceptual bridge to `@engbomMoser2017` and `@diamond2016`.

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official papers remain the benchmark sources for a closer replication or re-analysis.
