# Source Notes

The reproduction path is inspired by the design logic of Card and Krueger's New Jersey and Pennsylvania fast-food minimum-wage comparison. The lab does not reproduce the official data or published magnitudes. It creates a two-period, two-state restaurant panel so students can compute:

- pre and post means by treated and comparison state;
- the canonical 2x2 DID contrast;
- the equivalent fixed-effects regression coefficient;
- a warning about state-level clustering with very few clusters.

The diagnosis path creates a staggered-adoption county panel. Some counties adopt a policy earlier than others, some later, and some never. Treatment effects differ across cohorts and event time. This makes the failure mode of naive TWFE visible and gives students a bounded way to compare:

- naive TWFE;
- group-time ATT estimates using not-yet-treated controls;
- imputation-style ATT estimates based on untreated observations;
- event-time support and clustering diagnostics.

All data are deterministic and may be regenerated from `src/make_synthetic_data.py`.
