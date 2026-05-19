# Transfer Data Notes

The transfer data describe a synthetic panel in which young workers choose between schooling and work.

## Variables

- `person_id`: synthetic person identifier.
- `period`: decision period.
- `age`: age at the start of the decision period.
- `schooling_years`: schooling state before the action.
- `experience_years`: work-experience state before the action.
- `tuition`: current tuition cost.
- `wage_offer`: offered wage if the person works.
- `choose_school`: action indicator for school.
- `work`: action indicator for work.
- `observed_wage`: wage observed when the person works.
- `synthetic_ability`: latent ability included only for data-generation transparency.

## Design interpretation

Students use this file to practice structural translation. The states are schooling and experience. The actions are school and work. The latent objects are preferences, expected returns, ability, and continuation values. The tuition-subsidy counterfactual is pedagogical and partial-equilibrium; it should not be read as a full lifecycle policy model.

## Main caveat

This transfer exercise is intentionally small. It illustrates dynamic feedback from actions to future states, but it does not model full expectations, borrowing constraints, fertility, occupation choice, equilibrium wages, or rich latent heterogeneity.
