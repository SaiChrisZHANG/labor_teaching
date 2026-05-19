| Design situation | Recommended baseline approach | Main caveat | Practical rule |
| --- | --- | --- | --- |
| Two groups, two periods, one sharp treatment date | Classical DID | Parallel trends must be persuasive, not assumed | Start with the clean 2x2 estimand before adding fixed effects machinery |
| Staggered treatment with heterogeneous effects | Group-time ATT or imputation-based DID | TWFE can use already-treated units as controls | Do not default to TWFE when timing is staggered |
| Dynamic treatment profile is the object | Interaction-weighted event study or imputation-based event-study aggregation | Naive event-study coefficients can be contaminated | Report clearly which event-time estimator is being used |
| One or very few treated units | Synthetic control | Donor-pool quality and pre-fit are central | Use synthetic control when treated units are unusual or conventional controls are weak |
| Anticipation likely | Explicit anticipation window / trimmed event times | Leads are not a free test of design validity | State and justify the anticipation structure directly |
| Treatment reversals / switching | Custom estimand or alternative design | Standard staggered-adoption formulas may not apply | Define the treatment path before choosing the estimator |
| Weak overlap in comparison units | Re-think treated/control set or donor pool | Estimation cannot fix a design with bad support | Diagnose support before estimating dynamic effects |
