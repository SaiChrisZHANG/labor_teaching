# Week 6 lab README

This folder contains the Week 6 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week6_synthetic_data.py

conda run -n research python src/reproduce_lundborg_ivf.py \
  --input original/reduced/lundborg_ivf_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_child_penalty_event_study.py \
  --input transfer/data/kleven_child_penalty_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the local synthetic teaching files and verify the environment.
2. Run the bounded reproduction in the spirit of `@lundborgPlugRasmussen2017`.
3. Read `original/source-notes.md` before interpreting the outputs as a literal paper replication.
4. Use the transfer step to trace dynamic child penalties in the spirit of `@klevenLandaisSogaard2019`.
5. Treat the optional extension in `lab.md` as a policy bridge to `@gelbach2002`, `@cortesTessada2011`, or `@klevenLandaisPoschSteinhauerZweimueller2024`.

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official papers remain the benchmark sources for closer replication or re-analysis.
