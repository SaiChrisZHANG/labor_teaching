**ML algorithm quick guide**

| Algorithm family | Best suited for | Strengths | Main caveats in applied economics |
|---|---|---|---|
| Lasso / Elastic Net | High-dimensional controls, sparse measurement, baseline prediction | Stable shrinkage, useful for variable selection and nuisance prediction | Selection instability under collinearity; not a causal estimator by itself |
| Ridge | Dense prediction problems with many correlated covariates | Good predictive stability | Weak variable-selection interpretability |
| Random forests | Nonlinear prediction, interaction-heavy tabular data | Strong off-the-shelf predictive performance, robust defaults | Harder to interpret; can overfit subgroup patterns if used incautiously |
| Gradient boosting | Sharp prediction tasks, ranking, tabular prediction | Often strong predictive accuracy | Sensitive tuning; target leakage and calibration problems are common |
| Causal forests / GRF | Flexible treatment-effect heterogeneity | Built for heterogeneous effects rather than just prediction | Heterogeneity estimates can be noisy; policy conclusions require honest validation |
| Policy trees | Interpretable treatment rules | Easy to explain and implement | Can be unstable in small samples; may oversimplify the decision problem |
| SVM | Margin-based classification in moderate-dimensional spaces | Effective for some classification tasks | Less natural for treatment policy or welfare problems; limited interpretability |
| Neural networks | Large-scale unstructured or highly nonlinear problems | Powerful when feature learning matters | Data hungry, opaque, and often unnecessary for standard tabular economics settings |
| Clustering methods | Unsupervised grouping / typologies | Useful for exploratory segmentation | Clusters are not causal groups and should not be overinterpreted |
