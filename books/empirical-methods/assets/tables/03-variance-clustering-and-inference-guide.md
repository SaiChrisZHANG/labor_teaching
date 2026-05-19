## Variance, Clustering, and Inference Guide

| Problem | Why it matters in DID / event studies | Preferred response | Practical caveat |
|---|---|---|---|
| Serial correlation | Outcomes and treatment are persistent over time, so naive SEs overreject | Cluster at the treatment-assignment or residual-dependence level | Few clusters can still make cluster-robust SEs unreliable |
| Few treated clusters | Conventional cluster-robust inference is weak in small-\(G\) settings | Use wild-cluster bootstrap or randomization inference | Report the number of treated clusters explicitly |
| Spatial correlation | Policies often vary by place; nearby units may share shocks | Consider spatial or two-way clustering | The right clustering level depends on the assignment process, not convenience |
| Unit-level persistence plus staggered timing | Event-study coefficients can look precise for the wrong reason | Combine correct estimator with correct inference | Modern DID fixes weighting, not inference, by itself |
| Single treated unit / aggregate policy | Conventional asymptotics are weak | Use placebo/permutation logic in SCM or synthetic DID | Inference is design-specific and often visual/diagnostic |
