## Theory-to-Applied Bridge

| Research setting | Why prediction enters | Typical prediction target | Representative implementation | Main caveat |
|---|---|---|---|---|
| Job postings and skill demand | Raw text must be structured before economic analysis | Skill labels, occupation labels, technology mentions | Supervised text classification with train/test validation | Target labels may not align with the economics construct |
| Administrative job titles | Titles are noisy and not analysis-ready | Occupation code or task group | Supervised classification using labeled HR records | Classification error may be systematic across sectors/firms |
| Remote work / AI exposure | Exposure is not directly observed in surveys | Exposure score, feasibility score | Text-based scoring and supervised classification | Transportability across occupations and time is fragile |
| Risk-score environments | Outcome probabilities matter directly | Predicted attrition/default/take-up | Penalized classification, calibration diagnostics | A useful score is not automatically policy-invariant |
| Missing or latent outcomes | Some objects are partially observed | Imputed outcome/proxy measure | Predictive imputation with validation | Imputation error may contaminate downstream estimation |
