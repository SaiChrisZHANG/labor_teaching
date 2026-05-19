# Selection, Trend, and Inference Diagnostics for DID

| Design question | What to check | Why it matters | Practical response |
|---|---|---|---|
| Are treated and control units plausible comparisons? | Levels, pre-treatment trends, composition | DID needs untreated trend comparability, not just post-period overlap | Plot outcomes, covariates, and composition over time |
| Is treatment staggered? | Cohort timing and treatment shares | TWFE can use already-treated units as controls | Move beyond naive TWFE when effects are heterogeneous |
| Are dynamic effects important? | Event-time path | Static DID can hide timing and persistence | Use cohort-consistent event-study estimators |
| Are errors serially correlated? | Persistence of outcome and treatment | Naive SEs can dramatically overstate precision | Cluster at treatment level; consider few-cluster fixes |
| Are there anticipation or reversals? | Policy announcement, phased implementation, treatment exits | Timing mismeasurement breaks interpretation | Redefine event time and restrict estimand if needed |
| Is control support weak? | Few untreated units or poor pre-fit | DID may extrapolate badly | Consider synthetic control or synthetic DID |
