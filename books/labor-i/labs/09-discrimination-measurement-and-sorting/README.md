# Week 9 lab README

This folder contains the Week 9 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week9_synthetic_data.py

conda run -n research python src/reproduce_bertrand_mullainathan.py \
  --input original/reduced/bertrand_mullainathan_callback_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_discrimination_report_cards.py \
  --input transfer/data/employer_report_card_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the local synthetic teaching files and verify the environment.
2. Run the bounded callback-gap reproduction in the spirit of [@bertrandMullainathan2004].
3. Read `original/source-notes.md` before interpreting the outputs as a literal paper replication.
4. Use the transfer step to move from an average callback effect to employer-level report cards in the spirit of [@klineRoseWalters2024].
5. Treat the optional extension in `lab.md` as a bridge to task-based discrimination in [@hurstRubinsteinShimizu2024].

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official papers remain the benchmark sources for closer replication or re-analysis.
