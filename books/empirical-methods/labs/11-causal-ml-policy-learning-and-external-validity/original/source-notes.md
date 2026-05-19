# Source Notes

The source file is a deterministic synthetic dataset for a job-training assignment problem. It is inspired by the logic of empirical welfare maximization and policy learning, but it is not an official replication of Kitagawa and Tetenov, Athey and Wager, Bansak et al., or any related paper.

Each row is an applicant observed before a possible training offer. The variables include:

- pre-assignment covariates: age, education, unemployment duration, prior earnings, digital skill, local unemployment, baseline risk, and region;
- `training_offer`, the observed treatment;
- `earnings_12mo`, the observed gross outcome;
- `training_cost`, used to define net policy value;
- synthetic potential-outcome columns used only for teaching diagnostics.

The public analysis path estimates nuisance functions from observed data and evaluates rules with held-out doubly robust policy-value scores. The synthetic truth columns are included so students can see why a teaching simulation can illustrate policy learning without claiming a real replication.
