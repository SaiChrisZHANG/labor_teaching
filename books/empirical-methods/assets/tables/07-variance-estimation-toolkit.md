## Variance estimation: bootstrap, delta method, and related choices

| Method | What it does | When it is useful | Practical caveat |
| --- | --- | --- | --- |
| Inverse Hessian / information matrix | Uses curvature of the criterion/likelihood | Smooth likelihood-based estimation with well-behaved optimization | Fragile under misspecification or poor numerics |
| Sandwich / OPG estimator | Uses Jacobian + score/moment covariance | M-estimation and misspecification-robust inference | Requires stable gradients and clear definition of moment dependence |
| Delta method | Maps parameter variance into variance of functions/counterfactuals | Elasticities, welfare objects, counterfactual policy effects | Linear approximation may be weak for highly nonlinear objects |
| Bootstrap | Re-estimates model on resampled data | Multi-step estimators, hard analytic variance, nonlinear functionals | Computationally expensive; resampling scheme must match dependence |
| Cluster/bootstrap variants | Resamples at cluster/unit level | Worker-firm panels, geographic panels, policy clusters | Wrong resampling level can invalidate inference |
| Two-step corrections (Murphy–Topel style) | Adjusts for first-stage/generated-regressor uncertainty | Two-step structural or semi-structural procedures | Easy to underreport if first-stage uncertainty is ignored |
| Simulation-aware checks | Separates data variance from simulation noise | SMM/indirect inference or complex Monte Carlo routines | Too few simulation draws can make standard errors misleading |
