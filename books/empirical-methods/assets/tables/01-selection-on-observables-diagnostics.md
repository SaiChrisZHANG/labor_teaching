:::{table} Selection-on-observables diagnostics and robustness toolkit
:label: tbl:soo-diagnostics
| Object | Practical question | Typical evidence | Main failure mode |
| --- | --- | --- | --- |
| Target estimand | Am I estimating ATE, ATT, or something else? | Explicit parameter statement and sample definition | Estimand drift across specifications |
| Covariate balance | Do treated and untreated units look comparable after adjustment? | Standardized differences, Love plots, weighted balance tables | Balance on observables but not on true selection margins |
| Overlap / support | Are the treated units represented in untreated support? | Propensity score histograms, support trimming, overlap plots | Extreme weights and extrapolation |
| Outcome-model dependence | Does the result rely on one functional form? | Linear vs flexible adjustment, interaction models | Hidden extrapolation and misspecification |
| Matching design | Are matched pairs/groups economically similar? | Exact matching variables, nearest-neighbor rules, calipers | Poor matches on substantively important covariates |
| Weighting stability | Are a few observations driving the estimate? | Weight distributions, trimmed IPW, stabilized weights | Near-zero or near-one propensity scores |
| Sensitivity to unobservables | How strong would omitted selection need to be? | Oster/Altonji-Elder-Taber style sensitivity checks, Rosenbaum-style logic | False confidence from observables-only diagnostics |
| Interpretation | What assumption makes this causal? | Plain-language design justification tied to institutions | Treating an estimator as a design |
:::
