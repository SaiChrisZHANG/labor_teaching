# Transfer data notes

The transfer data follow individuals through a short schooling/work lifecycle. Each row contains a person-period observation with schooling, experience, tuition, wage offers, schooling choice, work status, and observed wages for workers.

The transfer script fits a wage-offer mapping and estimates a reduced simulated-moments model for schooling choices. The targeted moments are schooling rates by period and final lifecycle summaries. The counterfactual lowers tuition and simulates schooling, work, experience, and wage-offer paths.

This path is useful for learning SMM logic, but it omits the objects a full frontier lifecycle paper would need: rich expectations, borrowing constraints, fertility, occupation choice, latent types, measurement error, equilibrium wage response, and validation against policy variation.
