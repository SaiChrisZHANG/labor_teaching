# Week 2 lab README

This folder contains the Week 2 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/reproduce_saez_bunching.py \
  --input original/reduced/saez_bunching_synthetic.csv \
  --earnings-col earnings \
  --kink 30 \
  --bin-width 1 \
  --window 12 \
  --outdir output/reproduced

conda run -n research python src/transfer_bunching_design.py \
  --input transfer/data/saez_transfer_synthetic.csv \
  --earnings-col earnings \
  --group-col group \
  --kink 30 \
  --bin-width 2 \
  --window 14 \
  --outdir output/transfer
```

## Recommended workflow

1. Run the bounded synthetic path to verify the environment and plotting workflow.
2. Read `original/source-notes.md` to understand what the official [@saez2010] package would add.
3. Keep the reproduction target to one histogram or one binned-density object.
4. Use the transfer step for one alternative bin width, subgroup, or kink window only.
5. Document clearly which outputs come from the synthetic teaching path and which require external files.

## Notes

- The synthetic data are included only to make the bunching workflow testable and teachable.
- The official AEA replication package remains the benchmark source for a closer paper replication.
- The smoke test verifies the bounded teaching path only; it does not attempt to recreate the full publication pipeline.
