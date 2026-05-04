# Week 1 lab README

This folder contains the Week 1 code lab for Labor I.

## Fast start

```bash
conda run -n research python src/reproduce_composition_adjustment.py   --input original/reduced/composition_panel_synthetic.csv   --outdir output/reproduced
conda run -n research python src/transfer_factbook.py   --input transfer/data/labor_micro_synthetic.csv   --date-col date   --status-col employment_status   --weight-col weight   --hours-col hours   --earnings-col weekly_earnings   --group-col group   --outdir output/transfer
```

## Recommended workflow

1. Run the reduced pedagogical scripts to verify the environment.
2. Read `original/source-notes.md`.
3. Inspect the official replication package once it is added to `original/official/`.
4. Write the design memo before beginning the transfer exercise.
5. Replace the synthetic transfer file with a real bounded dataset or extension sample.

## Notes

- Synthetic data are included only to make the pipeline concrete and testable.
- The official package remains the benchmark source for the reproduction step.
- Students should keep the transfer exercise to one figure or one table.
