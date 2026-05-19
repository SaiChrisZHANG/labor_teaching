# Transfer Data Notes

The bunching transfer path studies a synthetic earnings distribution with a tax kink at 50,000.

## Variables

- `observed_earnings`: earnings after synthetic response to the kink.
- `counterfactual_earnings_synthetic`: latent no-kink earnings, included only for data-generation transparency.
- `tax_kink`: the earnings threshold where the marginal tax rate changes.
- `lower_marginal_tax_rate`: marginal tax rate below the kink.
- `upper_marginal_tax_rate`: marginal tax rate above the kink.
- `synthetic_buncher`: indicator for agents moved by the synthetic response rule.

## Design interpretation

Students observe excess mass around the kink and fit a smooth counterfactual density excluding bins near the threshold. The normalized excess mass is mapped into a stylized elasticity using the change in the net-of-tax rate.

## Main caveat

Bunching is a design plus model exercise. The elasticity depends on the counterfactual density, bin width, excluded window, polynomial degree, salience, optimization frictions, and whether the response reflects real behavior or reporting.
