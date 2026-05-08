# Week 3 lab README

This folder contains the Week 3 code lab for Labor II.

## Fast start

```bash
conda run -n research python src/reproduce_friebel_team_incentives.py \
  --input original/reduced/friebel_team_incentives_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_personnel_assignment.py \
  --input transfer/data/personnel_assignment_scenarios.csv \
  --outdir output/transfer
```

## Recommended workflow

1. Run the reduced pedagogical scripts to verify the environment.
2. Read `original/source-notes.md`.
3. Write the diagnose memo before extending the transfer exercise.
4. Keep the transfer path focused on assignment versus incentives rather than expanding into a full personnel-data project.

## Notes

- Synthetic data are included only to keep the pipeline local and deterministic.
- [@friebelHeinzKruegerZubanov2017] is the primary design anchor, not a full shipped replication package.
- [@bensonLiShue2019] is the challenge bridge for promotions and assignment.
- [@emanuelHarrington2024] is the optional extension bridge for selection versus treatment in remote-work settings.
