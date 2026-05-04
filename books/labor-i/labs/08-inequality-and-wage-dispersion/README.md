# Week 8 lab README

This folder contains the Week 8 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week8_synthetic_data.py

conda run -n research python src/reproduce_autor_katz_kearney_inequality.py \
  --input original/reduced/autor_katz_kearney_inequality_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_worker_firm_inequality.py \
  --input transfer/data/worker_firm_inequality_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the local synthetic teaching files and verify the environment.
2. Run the bounded inequality factbook reproduction in the spirit of `@autorKatzKearney2008`.
3. Read `original/source-notes.md` before interpreting the outputs as a literal paper replication.
4. Use the transfer step to move from repeated-cross-section inequality objects to a synthetic worker-firm decomposition in the spirit of `@cardCardosoHeiningKline2018` and `@songPriceGuvenenBloomVonWachter2019`.
5. Treat the optional extension in `lab.md` as a bridge to broader distributional synthesis in `@haanwinckel2025`.

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official papers remain the benchmark sources for closer replication or re-analysis.
