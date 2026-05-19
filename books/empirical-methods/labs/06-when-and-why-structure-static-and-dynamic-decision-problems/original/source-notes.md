# Source Notes

The Week 6 reproduce path is a synthetic dynamic replacement exercise inspired by Rust-style dynamic discrete-choice logic.

## Synthetic setting

- `unit_id` identifies the capital good.
- `period` is the decision period.
- `mileage_state` is the discrete state before the action.
- `replace` is the action: one if the unit is replaced and zero if it continues.
- `next_mileage_state` is the next-period state.
- `operating_cost` is an observed cost outcome.
- `true_replacement_probability` is included only because this is a teaching dataset.

## Design interpretation

The observed behavior is replacement by mileage state. The latent objects are replacement costs, maintenance costs, and continuation values. A static hazard can describe replacement probabilities, but it cannot explain how a replacement-cost counterfactual changes future states and option values.

## Not an official replication

The dataset does not reproduce official published estimates. It is a bounded teaching path for estimating, diagnosing, and interpreting dynamic discrete-choice models.
