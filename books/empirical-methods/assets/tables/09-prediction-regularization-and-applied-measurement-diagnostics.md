## Prediction and Regularization Diagnostics

| Design question | Main empirical object | Typical implementation choice | What can go wrong | Practical check |
|---|---|---|---|---|
| Is prediction the research object or an input? | Forecast, classification, or constructed measure | Define target and downstream use before modeling | A high-performing model solves the wrong problem | Write down the economic target and later use explicitly |
| Is overfitting likely? | In-sample fit vs out-of-sample fit | Holdout sample, cross-validation | Excellent training performance and poor generalization | Compare train, validation, and test loss |
| Is the model sparse or dense? | Variable importance structure | Lasso for sparsity, ridge for dense shrinkage, elastic net for mixed settings | Unstable feature selection or poor predictive accuracy | Check tuning stability across folds |
| Is the model calibrated? | Predicted probabilities or scores | Reliability plots, subgroup checks | Good ranking but poor probability interpretation | Compare predicted vs realized frequencies |
| Will the measure travel? | Cross-context validity | Re-estimate or test across periods/places/firms | Drift, reclassification error, changing language | Validate on a different population or time period |
| Is fairness/subgroup accuracy important? | Heterogeneous prediction error | Group-specific diagnostics | Average accuracy masks systematic subgroup failure | Report subgroup loss/calibration |
