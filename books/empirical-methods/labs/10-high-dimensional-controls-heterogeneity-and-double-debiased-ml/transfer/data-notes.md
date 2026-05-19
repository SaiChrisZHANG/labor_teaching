# Transfer Data Notes

The youth-program file is a deterministic synthetic dataset inspired by applied economics work that uses causal forests to study treatment-effect heterogeneity [@davisUsingCausalForests2017; @wagerEstimationInferenceHeterogeneous2018].

It is not an official replication file and does not contain program administrative records or restricted data.

The transfer target is heterogeneity in the effect of `program_offer` on `summer_employed`. The main substantive heterogeneity dimension is `baseline_risk`, with overlap diagnostics by risk group. The synthetic column `true_cate` is included only for teaching checks; students should interpret real research outputs without access to a true effect.
