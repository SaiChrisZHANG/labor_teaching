# Week 1 lab README

This folder contains the Week 1 code lab for Labor II.

## Fast start

```bash
conda run -n research python src/reproduce_beaudry_city_industry.py \
  --input original/reduced/beaudry_city_industry_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_static_labor_demand.py \
  --input transfer/data/static_labor_demand_scenarios.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Run the reduced pedagogical scripts to verify the environment.
2. Read `original/source-notes.md`.
3. Write the design memo before extending the transfer exercise.
4. Keep the transfer path to one bounded scenario comparison.

## Notes

- Synthetic data are included only to keep the pipeline local and deterministic.
- [@beaudryGreenSand2018] is the design anchor, not a fully shipped replication package.
- [@saezSchoeferSeim2019] and [@buttersSacksSeo2022] are interpretation bridges for the transfer step.
