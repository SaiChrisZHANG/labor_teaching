# Lecture 9. Prediction, Regularization, And Applied Measurement

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish prediction as a research object from prediction as an input into measurement or design;
2. define prediction targets, losses, train/test splits, and generalization error in applied economics language;
3. explain lasso, ridge, and elastic net as regularized estimators with different sparsity and bias-variance implications;
4. use cross-validation and holdout evaluation without confusing model selection with causal identification;
5. diagnose feature engineering choices, target leakage, calibration, class imbalance, drift, instability, fairness, and transportability;
6. evaluate whether a predicted object is fit for a downstream research question;
7. design a Reproduce -> Diagnose -> Transfer lab for prediction as economic measurement.

## Opening Orientation

Lecture 9 begins Block 3 by asking how prediction can serve applied economics without replacing research design. The central question is: **when is prediction itself the research object, and when is it an input into measurement or design?** This is not a generic machine-learning lecture. The goal is to understand prediction, regularization, model selection, and validation as tools for constructing and evaluating empirical objects in economics.

Prediction is the final object when the substantive question is itself predictive: which workers are likely to leave a firm, which applicants are likely to be hired, which vacancies are likely to fill, which households are likely to take up a program, or which loans are likely to default. Prediction is an input when a model turns messy data into a variable for later economic analysis: a job-posting skill measure, an occupational code, a remote-work feasibility score, a risk index, or an imputed latent outcome. The evaluation burden differs sharply across those uses.

The paper spine is deliberately applied. Mullainathan and Spiess explain what machine learning contributes to applied econometrics: prediction tasks, algorithmic regularization, honest validation, and a different relationship between model complexity and out-of-sample performance [@mullainathanMachineLearningApplied2017]. Belloni, Chernozhukov, and Hansen show why high-dimensional variable selection matters for structural and treatment-effect inference, especially when controls are numerous and selection is part of the empirical problem [@belloniHighDimensionalMethodsInference2014]. Ikudo uses machine learning to construct occupational classifications from noisy administrative job titles [@ikudoOccupationalClassificationsMachine2018]. Dahlhaus and coauthors use machine learning to structure online job postings into economic variables [@dahlhausFromOnlineJob2025]. Turrell and coauthors show how naturally occurring text data can be transformed into economic statistics, and Hansen and coauthors connect job and firm text to remote-work measurement across jobs, companies, and space [@turrellTransformingNaturallyOccurring2019; @hansenRemoteWorkAcross2023].

## Core Points

:::{admonition} Core points
:class: important

- Prediction can be the final empirical object, but in many economics papers it is an intermediate measurement step.
- The prediction target, training population, loss function, and downstream research use must be aligned before the algorithm matters.
- Regularization improves generalization by trading some in-sample fit for lower variance, but it can also change which variables appear substantively important.
- Cross-validation selects tuning parameters for prediction loss; it does not identify causal effects or validate a policy counterfactual.
- A predicted score, label, or index is useful only if it is calibrated, stable, transportable, and interpretable enough for the later economics claim.
- Feature engineering is part of research design because leakage, post-treatment variables, and changing language can turn a high-performing model into a bad measure.
- Machine learning is most valuable in applied economics when it improves measurement, diagnostics, or nuisance prediction while keeping the estimand and identification logic explicit.
:::

## Bridge

The first two blocks of the course emphasized credible comparisons and structural interpretation. Block 1 asked what variation identifies an estimand. Block 2 asked when economic structure is needed to recover latent primitives, welfare objects, and counterfactuals. Lecture 9 keeps those habits and adds a new object: a prediction rule.

The prediction rule is not automatically the research answer. A flexible model can predict wages, occupations, tasks, vacancies, program take-up, or risk. But the economist still has to say what the target means, why it is measured that way, who appears in the training data, what loss function is appropriate, and how errors affect the later research design. The machine-learning step therefore belongs inside the empirical design rather than outside it.

```{include} assets/tables/09-theory-to-applied-bridge.md
```

## Field Core

### A. Prediction As Object Versus Prediction As Input

Start by writing down the use case. Let {math}`Y_i` denote the target, {math}`X_i` the information available at prediction time, and {math}`\widehat f(X_i)` the prediction rule.

Prediction is the research object when the paper's question is about forecasting or risk. Examples include worker attrition risk, vacancy fill probability, program take-up, default risk, or expected case duration. The object is evaluated by out-of-sample loss, calibration, and sometimes policy usefulness under constraints.

Prediction is an input when {math}`\widehat f(X_i)` becomes a constructed variable for another design. In job-postings research, text must be transformed into skill labels, task measures, technology indicators, or occupation categories before economists can study labor demand [@dahlhausFromOnlineJob2025; @turrellTransformingNaturallyOccurring2019]. In administrative data, raw job titles may need to become occupational classifications before researchers can study mobility or task exposure [@ikudoOccupationalClassificationsMachine2018]. In remote-work research, a text-derived score may be used to compare jobs, firms, and places [@hansenRemoteWorkAcross2023].

The distinction matters because the diagnostics differ. If prediction is the final object, ranking and expected loss may be central. If prediction is an input, the researcher must also ask whether prediction error is correlated with treatment, time, firm type, region, worker group, or the outcome in the downstream model. A small gain in average predictive accuracy may be worthless if the measure fails in the subgroup or period that identifies the economic claim.

### B. Targets, Loss, Train/Test Logic, And Generalization

The population risk for a prediction rule is:

```{math}
:label: eq:em9-population-risk
R(f)
=
\mathbb E\left[L\left(Y,f(X)\right)\right],
```

where {math}`L(\cdot)` is the loss function. Squared error is common for continuous outcomes or scores; log loss or Brier loss is common for probabilities; zero-one loss, precision, recall, or F1 scores may matter for classification. The loss should match the economics use. If false negatives are costly because missed high-risk cases receive no support, average accuracy is the wrong headline metric.

With a training sample {math}`\mathcal I_{train}` and test sample {math}`\mathcal I_{test}`, the training rule solves an empirical problem such as:

```{math}
:label: eq:em9-training-risk
\widehat f
=
\arg\min_{f\in\mathcal F}
\frac{1}{|\mathcal I_{train}|}
\sum_{i\in\mathcal I_{train}}
L\left(Y_i,f(X_i)\right).
```

The honest test risk is then:

```{math}
:label: eq:em9-test-risk
\widehat R_{test}(\widehat f)
=
\frac{1}{|\mathcal I_{test}|}
\sum_{i\in\mathcal I_{test}}
L\left(Y_i,\widehat f(X_i)\right).
```

The split must respect the research use. Random splits are often fine for a first teaching exercise. Time splits are better when the model will be used in future periods. Firm, region, occupation, or market splits are better when the downstream question requires transport across groups. If a job-posting classifier is trained and tested on postings from the same firms, it may look strong while failing on new firms with different language.

Generalization error is not a slogan. It is an empirical claim about the target population. A careful paper reports:

- the target and loss;
- the training, validation, and test populations;
- whether tuning decisions touched the test set;
- uncertainty or sensitivity in test performance;
- subgroup performance for economically relevant groups.

### C. Regularization: Lasso, Ridge, Elastic Net, And Tuning

High-dimensional applied data often contain many possible predictors: worker histories, firms, locations, occupation codes, interactions, text terms, embeddings, and lagged outcomes. Unregularized models can overfit because they chase sample noise. Regularization changes the estimator by adding a penalty for model complexity.

For a linear prediction rule {math}`X_i'\beta`, lasso solves:

```{math}
:label: eq:em9-lasso
\widehat\beta^{lasso}
=
\arg\min_{\beta}
\frac{1}{n}\sum_{i=1}^{n}(Y_i-X_i'\beta)^2
+
\lambda\sum_{j=1}^{p}|\beta_j|.
```

Ridge uses an {math}`\ell_2` penalty:

```{math}
:label: eq:em9-ridge
\widehat\beta^{ridge}
=
\arg\min_{\beta}
\frac{1}{n}\sum_{i=1}^{n}(Y_i-X_i'\beta)^2
+
\lambda\sum_{j=1}^{p}\beta_j^2.
```

Elastic net combines both:

```{math}
:label: eq:em9-elastic-net
\widehat\beta^{EN}
=
\arg\min_{\beta}
\frac{1}{n}\sum_{i=1}^{n}(Y_i-X_i'\beta)^2
+
\lambda
\left[
\alpha\sum_{j=1}^{p}|\beta_j|
+
(1-\alpha)\sum_{j=1}^{p}\beta_j^2
\right].
```

The tuning parameter {math}`\lambda` controls shrinkage. Larger {math}`\lambda` usually reduces variance but increases bias. The elastic-net mixing parameter {math}`\alpha` controls the balance between sparse selection and dense shrinkage.

The applied interpretation is not mechanical:

- **Lasso** is useful when sparsity is plausible and variable selection is helpful, but selected variables can be unstable across folds or samples.
- **Ridge** is useful when many predictors carry small related signals, especially with collinear text or occupation features, but it does not select a small model.
- **Elastic net** is useful when predictors are grouped or collinear and some sparsity is still useful.

Cross-validation chooses tuning parameters by estimating held-out loss. With folds {math}`V_1,\ldots,V_K`, the criterion is:

```{math}
:label: eq:em9-cross-validation
\widehat\lambda
=
\arg\min_{\lambda\in\Lambda}
\frac{1}{K}
\sum_{k=1}^{K}
\frac{1}{|V_k|}
\sum_{i\in V_k}
L\left(Y_i,\widehat f_{-k,\lambda}(X_i)\right).
```

This selects a prediction rule. It does not make the selected controls exogenous, and it does not make the prediction rule policy-invariant. Belloni, Chernozhukov, and Hansen are important precisely because high-dimensional selection must be handled as part of the inference problem when the downstream object is structural or causal [@belloniHighDimensionalMethodsInference2014].

### D. Bias, Variance, Model Selection, And Calibration

Regularization is often explained through the bias-variance tradeoff. For a prediction rule evaluated at {math}`x`, a stylized squared-error decomposition is:

```{math}
:label: eq:em9-bias-variance
\mathbb E\left[
\left(Y-\widehat f(x)\right)^2\mid X=x
\right]
=
\sigma^2
+
\left(\mathbb E[\widehat f(x)]-f_0(x)\right)^2
+
\operatorname{Var}\left(\widehat f(x)\right),
```

where {math}`f_0(x)=\mathbb E[Y\mid X=x]` and {math}`\sigma^2` is irreducible noise. A more flexible model can reduce approximation bias but increase variance. Regularization accepts some bias to reduce variance and improve out-of-sample risk.

Model selection should compare meaningful baselines. A job-posting classifier should beat simple keyword rules, occupation fixed effects, or majority-class prediction before the researcher celebrates a complex model. A risk score should be compared to a parsimonious administrative benchmark. A text-derived measure should be validated against human labels or known external aggregates when available.

Calibration matters when a score is interpreted as a probability or intensity. A binary prediction score {math}`\widehat p_i` is calibrated if:

```{math}
:label: eq:em9-calibration
\mathbb E[Y_i\mid \widehat p_i=s]=s.
```

A common prediction-error diagnostic is the Brier score:

```{math}
:label: eq:em9-brier
\widehat B
=
\frac{1}{n}
\sum_{i=1}^{n}
\left(Y_i-\widehat p_i\right)^2.
```

For classification, a threshold rule can be written:

```{math}
:label: eq:em9-threshold
\widehat C_i(t)=\mathbf 1\{\widehat p_i\geq t\}.
```

Changing {math}`t` changes precision, recall, false positives, and false negatives. In applied economics, that choice is substantive. A policy triage rule, an audit sample, and an occupation classifier may require different thresholds even if they use the same score.

### E. Feature Engineering, Leakage, And Measurement Design

Feature engineering is not clerical. It defines what information the model is allowed to use. In economics applications, the main rule is simple: predictors must be available at the time and level at which the prediction is supposed to be made, and they must not encode the outcome or treatment assignment in disguise.

Target leakage occurs when a predictor contains information that would not be available at prediction time or that is downstream of the outcome. In labor applications, examples include:

- using post-hire performance when predicting hiring success from applications;
- using realized program participation when predicting take-up from pre-policy records;
- using edited job-posting metadata added after a vacancy is filled;
- using future occupation codes to classify current noisy job titles;
- using post-treatment text to construct a pre-treatment exposure measure.

Leakage can produce excellent test performance if the train/test split repeats the same mistake. The right check is conceptual as much as statistical: draw a timing diagram. When is {math}`Y_i` realized? When is {math}`X_i` observed? Who generates the labels? Could the feature be affected by the treatment, policy, outcome, or model decision?

Feature engineering also creates measurement choices. Job-posting text can be represented by skill dictionaries, bag-of-words features, embeddings, occupation-level aggregates, or human-labeled categories. Each representation answers a slightly different question. A dictionary may be transparent but miss synonyms. A supervised classifier may be accurate on labeled tasks but fragile when language shifts. An embedding may capture similarity but be harder to explain to a skeptical reader.

### F. Prediction As Applied Measurement

Prediction becomes economics when it turns unstructured or noisy material into a defensible economic variable. The examples below are useful because they force students to state the measurement object.

**Job postings.** Online postings contain text about occupations, skills, tasks, technologies, remote work, and working conditions. Dahlhaus and coauthors show how machine learning can structure naturally occurring job-posting data into variables usable for economic analysis [@dahlhausFromOnlineJob2025]. Turrell and coauthors make the broader measurement point: naturally occurring text can become economic statistics only after careful validation of labels, coverage, and errors [@turrellTransformingNaturallyOccurring2019].

**Occupational classification.** Administrative job titles are often noisy. Ikudo's occupational-classification work illustrates prediction as a way to map raw titles into a structured classification system [@ikudoOccupationalClassificationsMachine2018]. The downstream object may be occupational mobility, exposure to tasks, or wage changes by occupation. Classification error matters if it is systematic by firm, sector, country, or worker group.

**Remote work and exposure scores.** Hansen and coauthors measure remote work across jobs, companies, and space using large-scale job and firm data [@hansenRemoteWorkAcross2023]. A score of this kind is valuable only if it travels across occupations and places, and if changes in language do not masquerade as changes in the underlying economic object.

**Risk scores and latent outcome proxies.** Risk scores may be useful when prediction is the final object, but they are dangerous when treated as stable policy primitives. A predicted attrition score might rank workers well in the status quo while failing after a retention policy changes incentives. A latent outcome proxy might reduce missing-data problems while introducing error correlated with subgroup, firm, or region.

The key question is not whether the model is sophisticated. It is whether the predicted object is fit for its research use:

1. Does the training label match the economics construct?
2. Is the training population the population where the claim is made?
3. Does prediction error vary with the treatment, instrument, time period, location, firm type, or subgroup?
4. Would a different but equally accurate label definition change the paper's conclusion?
5. Is the predicted object stable enough to be used in a downstream causal, structural, or descriptive design?

### G. Implementation Caveats: What Can Go Wrong?

The most common failure is not choosing the wrong algorithm. It is building a strong prediction model for the wrong empirical object.

```{include} assets/tables/09-prediction-regularization-and-applied-measurement-diagnostics.md
```

Several caveats deserve special attention.

**Class imbalance.** If only 5 percent of vacancies are high-tech, a model can achieve 95 percent accuracy by predicting "not high-tech" for everyone. Report precision, recall, false positives, false negatives, and subgroup performance.

**Drift.** Language, firms, platforms, occupations, and administrative rules change. A model trained on pre-pandemic job postings may not transport to remote-work language after 2020. Time-split validation is often more informative than random-split validation.

**Transportability.** A model trained on one country, platform, firm group, or occupation may fail elsewhere. If the downstream research design compares regions or sectors, validate the model across those groups.

**Instability.** Lasso-selected variables can change across folds, especially when text terms are correlated. If variable selection is interpreted substantively, report selection stability.

**Fairness and subgroup error.** Average loss can hide systematic error by gender, race, age, region, occupation, or firm type. In economics, subgroup error can become a measurement-error problem that changes estimated gaps, treatment effects, or incidence.

**Interpretability.** Interpretability is not always about explaining every coefficient. It is about making the measurement object auditable. A reader should understand what the model was trained to predict, which inputs were allowed, how performance was checked, and where the model is likely to fail.

**Prediction under policy change.** A predictive rule trained in the status quo is not automatically policy-invariant. If a rule is used to allocate services, screen applicants, target enforcement, or change incentives, the data-generating process may change.

ML is therefore not a substitute for design. It can create better measures, stronger diagnostics, and flexible nuisance functions, but it cannot define the estimand, choose the counterfactual, or guarantee exogeneity.

## Research Lab

The Week 9 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. The primary anchor is Dahlhaus and coauthors because their paper uses machine learning to turn online job postings into structured economic measurement objects [@dahlhausFromOnlineJob2025]. The challenge anchor is Ikudo because occupational classification pushes on transportability, label definition, and downstream interpretation [@ikudoOccupationalClassificationsMachine2018]. Hansen and coauthors provide an additional extension for drift and transportability across jobs, companies, and space [@hansenRemoteWorkAcross2023].

### Reproduce

Students work with a small synthetic job-posting dataset. They define a technology-intensive posting label, create text and posting features, compare a keyword baseline with ridge, lasso, and elastic-net prediction rules, tune penalties with cross-validation, and evaluate held-out performance.

The goal is to reproduce the **logic** of prediction as measurement:

- state the target label and why it is economically meaningful;
- train only on information available at posting time;
- compare regularized models to transparent baselines;
- report test loss, classification metrics, and calibration;
- produce a posting-level score that could become a downstream measure.

### Diagnose

Students diagnose whether the predicted object is credible enough for later research. They inspect class balance, calibration bins, subgroup performance by sector and region, vocabulary coverage, feature-weight stability, and a leakage audit.

The required memo asks:

- which feature would be leakage if included and why;
- whether the model is calibrated enough to treat scores as probabilities;
- whether subgroup error would threaten a study of regional or sectoral labor demand;
- whether lasso-selected terms should be interpreted as economic evidence;
- what validation would be needed before using the score in a causal design.

### Transfer

Students transfer the measurement logic to a nearby problem: occupational coding from terse administrative job titles. The transfer script applies the job-posting classifier to a smaller occupation-title dataset and evaluates transportability. The exercise is designed to show why high performance on rich job-posting text may not carry over to short titles, different sectors, or later periods.

Minimum student deliverables are:

1. one Reproduce paragraph defining the prediction target, loss, tuning rule, and selected model;
2. one Diagnose paragraph interpreting calibration, subgroup performance, leakage risk, and measurement error;
3. one Transfer paragraph explaining what changes when the model is used on occupational titles rather than postings;
4. one final sentence saying whether the predicted object is fit for the downstream economics question.

## Methods Box

:::{admonition} Prediction-as-measurement checklist
:class: note

1. **Name the economic object.** Is the target a forecast, a label, a score, an exposure measure, or a proxy for a latent outcome?
2. **Name the downstream use.** Is prediction the final object, a constructed regressor, a sample-selection tool, a diagnostic, or a nuisance input?
3. **Draw the timing diagram.** Are all features observed before the outcome, treatment, or policy decision?
4. **Choose the loss.** Does the loss reflect the research cost of false positives, false negatives, misranking, or miscalibration?
5. **Separate train, validation, and test honestly.** Use time, firm, region, or occupation splits when the research use requires transport.
6. **Tune transparently.** Report the cross-validation grid, selected penalty, and whether performance is stable across folds.
7. **Benchmark simply.** Compare against majority rules, keyword rules, fixed effects, or simple administrative scores.
8. **Report calibration and subgroup error.** Average accuracy is not enough for economic measurement.
9. **Audit leakage and drift.** Exclude post-outcome features and validate across periods or populations.
10. **Carry uncertainty forward.** If the predicted object enters a later design, discuss how measurement error could change the estimate.
:::

## Reading Ladder And References

```{include} assets/tables/09-reading-architecture.md
```

**First pass: why prediction belongs in applied econometrics.** Read Mullainathan and Spiess for the broad applied-econometrics framing, then Belloni, Chernozhukov, and Hansen for why high-dimensional selection changes inference when controls and nuisance functions matter [@mullainathanMachineLearningApplied2017; @belloniHighDimensionalMethodsInference2014].

**Second pass: prediction as measurement.** Read Dahlhaus and coauthors on structuring job postings, Ikudo on occupational classifications, and Turrell and coauthors on turning naturally occurring text into economic statistics [@dahlhausFromOnlineJob2025; @ikudoOccupationalClassificationsMachine2018; @turrellTransformingNaturallyOccurring2019].

**Third pass: transportability and labor applications.** Read Hansen and coauthors for remote-work measurement across jobs, companies, and space, then return to the diagnostics in this lecture: label stability, subgroup error, drift, and downstream use [@hansenRemoteWorkAcross2023].

**Reference shelf.** Keep Varian nearby for the broader "big data and econometrics" perspective, but use it as background rather than as the main labor-economics anchor [@varian2014].

## Exercises And Discussion Prompts

1. Give one applied economics example where prediction is the final research object and one where prediction is only an input into later empirical work. For each, state the target, loss, and validation sample.
2. Suppose a job-postings classifier has lower test loss than a keyword baseline but worse calibration for small firms. Which downstream claims would be threatened?
3. In what empirical settings is lasso more attractive than ridge? In what settings is ridge more attractive than lasso?
4. Draw a timing diagram for an administrative-data prediction task. Name two features that would be valid and two that would create target leakage.
5. A model trained on 2018 job postings is used to measure remote work in 2023. What diagnostics would you require before trusting the trend?
6. A predicted occupational code is used as a treatment variable in a DID design. How could systematic classification error by treated sector change the estimand?
7. Choose one paper from the reading ladder. Write a referee-style paragraph explaining whether the predicted object is fit for the paper's downstream economics question.

## Reproducibility And Code Lab Note

The canonical Lecture 9 lab folder is:

```text
labs/09-prediction-regularization-and-applied-measurement/
```

The lab is a bounded teaching path. It creates deterministic synthetic job-posting and occupation-title data, trains regularized prediction rules, tunes penalties with cross-validation, diagnoses calibration and subgroup performance, audits leakage risk, and transfers the measurement object to occupational classification. It does not claim to reproduce the published estimates in Dahlhaus and coauthors, Ikudo, Turrell and coauthors, or Hansen and coauthors, and it does not invent an official replication package.

The smoke path runs:

```bash
ENV_NAME=research bash smoke.sh
```

Expected outputs include train/test metrics, cross-validation results, feature-weight summaries, calibration and subgroup diagnostics, posting-level measurement scores, transfer performance tables, and transportability prompts.

## Slide Companion Note

The Week 9 slide deck should not duplicate the chapter. It should define the prediction-versus-design question, show train/test and regularization math, distinguish lasso/ridge/elastic net and tuning, connect prediction to job-posting and occupation measurement, isolate implementation pitfalls, and end with the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is `slides/week9/09-prediction-regularization-and-applied-measurement.tex`.

## Bridge Forward

Lecture 10 turns from prediction and measurement to high-dimensional controls, heterogeneity, and double/debiased machine learning. The bridge is important: Lecture 9 treats prediction mainly as an object or measurement input. Lecture 10 asks how flexible learners can estimate nuisance functions or treatment heterogeneity without letting prediction accuracy replace identification.
