## Estimation workflow: likelihood, moments, simulation, and fit

| Workflow element | Main object | Best use case | Main caveat |
| --- | --- | --- | --- |
| Likelihood | Full data density | Strongly specified stochastic model and tractable likelihood | Sensitive to misspecification and numerical issues |
| Method of moments / GMM | Empirical moments | Researcher wants to discipline specific economically meaningful objects | Weighting and moment choice are substantive, not neutral |
| Simulated method of moments | Simulated moments from complex model | Dynamic models or models without closed-form moments | Simulation noise, computational cost, and weak moments |
| Indirect inference | Auxiliary statistics or reduced-form summary objects | Simulation easy but direct estimation hard | Auxiliary model may miss the true behavioral margins |
| Validation / fit | Targeted and untargeted moments, distributions, policy responses | Necessary in every structural paper | Good fit on targeted moments alone is not enough |
