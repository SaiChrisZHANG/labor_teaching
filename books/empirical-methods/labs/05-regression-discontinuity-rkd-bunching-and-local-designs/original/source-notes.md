# Source Notes

The Week 5 reproduce path is a synthetic close-election RD exercise inspired by Lee-style electoral RD logic.

## Synthetic setting

- `vote_margin` is the running variable, centered at zero.
- `won_seat` is the sharp treatment indicator.
- `next_vote_share` is the outcome.
- `pre_turnout`, `party_strength`, and `district_income` are predetermined covariates used for continuity diagnostics and optional precision adjustment.
- `synthetic_true_effect` is included only because this is a teaching dataset. Students should not treat an observed true effect as available in real RD work.

## Design interpretation

The local comparison is between candidates who barely lost and barely won. The teaching estimand is the local effect of barely winning office on next-election vote share. The dataset is constructed to avoid precise manipulation near zero, but students still need to run density and covariate diagnostics.

## Not an official replication

The dataset does not reproduce official published estimates. It is a bounded teaching path for estimating, diagnosing, and interpreting RD designs.
