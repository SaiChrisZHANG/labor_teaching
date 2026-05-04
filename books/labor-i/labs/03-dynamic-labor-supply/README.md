# Week 3 lab README

This folder contains the Week 3 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week3_synthetic_data.py

conda run -n research python src/reproduce_fehr_goette_design.py \
  --input original/reduced/fehr_goette_shift_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_dynamic_response.py \
  --input transfer/data/fehr_goette_persistence_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the synthetic teaching files and verify the environment.
2. Run the bounded reproduction in the spirit of `@fehrGoette2007`.
3. Read `original/source-notes.md` before interpreting the output as a paper replication.
4. Use the transfer step to compare immediate bonus responses across persistence environments.
5. Treat the lifecycle extension in `lab.md` as optional and conceptually linked to `@attanasioLowSanchezMarcos2008`.

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official replication materials remain the benchmark source for a closer reproduction.
