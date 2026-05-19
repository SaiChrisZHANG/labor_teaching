## Variance, bootstrap, and inference toolbox

| Tool | Best use case | What it estimates | Strengths | Main caveats |
| --- | --- | --- | --- | --- |
| Hessian / information matrix | Likelihood-based models with smooth objective | Local curvature-based asymptotic variance of primitive parameters | Fast and standard | Sensitive to numerical conditioning and misspecification |
| Sandwich / Godambe variance | Moment-based estimators and quasi-likelihood settings | Variance robust to generic moment covariance structure | Connects uncertainty to Jacobian and moment variability | Requires stable moment Jacobians and good finite-sample behavior |
| Delta method | Counterfactuals or welfare objects that are smooth functions of primitives | Approximate variance of nonlinear functions of estimated parameters | Easy to implement when gradients are available | Can be inaccurate for highly nonlinear or weakly identified objects |
| Nonparametric bootstrap | Complex estimators with difficult analytic variance | Sampling variability under empirical resampling | Flexible; propagates uncertainty through many steps | Computationally expensive; can fail under weak ID or unstable optimization |
| Parametric bootstrap | Structural models with trusted parametric DGP | Sampling variability under the estimated model | Useful for counterfactual propagation and small-sample diagnostics | Depends on model specification being good enough |
| Simulation replication / multi-seed checks | Simulation-based estimators (SMM, MSM, indirect inference) | Sensitivity to simulation noise | Reveals instability masked by asymptotic formulas | Not a substitute for identification; adds compute burden |
