# Week 7 lab README

This folder contains the Week 7 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/build_week7_synthetic_data.py

conda run -n research python src/reproduce_mas_pallais_wtp.py \
  --input original/reduced/mas_pallais_job_choice_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_working_conditions_value.py \
  --input transfer/data/maestas_working_conditions_synthetic.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Generate the local synthetic teaching files and verify the environment.
2. Run the bounded reproduction in the spirit of [@masPallais2017].
3. Read `original/source-notes.md` before interpreting the outputs as a literal paper replication.
4. Use the transfer step to map broader working-conditions bundles into value-adjusted job rankings in the spirit of [@maestasMullenPowellVonWachterWenger2023].
5. Treat the optional extension in `lab.md` as a bridge to worker-flow revealed preference in [@sorkin2018].

## Notes

- The included data are synthetic and deterministic once generated.
- The smoke test verifies the bounded local workflow only.
- The official papers remain the benchmark sources for closer replication or re-analysis.
