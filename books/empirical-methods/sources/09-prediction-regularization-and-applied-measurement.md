---
title: Prediction, Regularization, and Applied Measurement
bibliography:
  - references.bib
---

# Prediction, Regularization, and Applied Measurement

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish prediction as a research object from prediction as an input into measurement or design;
2. explain how train/test splits, cross-validation, and regularization control overfitting;
3. interpret lasso, ridge, and elastic net as estimators solving different bias–variance and sparsity tradeoffs;
4. assess when a predicted object is usable for downstream economics research;
5. diagnose practical risks such as target leakage, poor calibration, drift, class imbalance, and low transportability;
6. connect prediction tools to concrete economics applications such as risk scores, occupational exposure measures, job-posting classification, and latent-outcome imputation.

## Opening Orientation

This lecture treats machine learning as an empirical toolkit for applied economics rather than as a replacement for research design. The main question is not whether a model predicts well in isolation, but whether the prediction target, training data, evaluation metric, and downstream use line up with the economic object of interest. In applied work, a high-performing prediction model can still mislead if it is trained on the wrong population, if it leaks post-treatment information, if it is miscalibrated, or if the predicted object has no clear interpretation for the research question [@mullainathanMachineLearningApplied2017; @dahlhausFromOnlineJob2025].

## Core points

```{admonition} Core points
:class: important

- Prediction is sometimes the final object of interest, but often it is an intermediate measurement step in an applied research design.
- Regularization is valuable because applied datasets are high-dimensional, noisy, and prone to overfitting.
- Good predictive performance is not enough: economists must care about calibration, transportability, stability, and downstream interpretability.
- A predicted index, score, or classification is useful only if its training target matches the substantive object needed for the research design.
- Machine learning improves empirical economics most when it sharpens measurement, diagnostics, or heterogeneity analysis without replacing identification logic.
```

## Bridge

The first two blocks of the course emphasized credible comparisons and structural interpretation. This lecture starts Block 3 by asking a different question: when can flexible function approximation improve applied research, and when does it merely create an elaborate black box? The answer depends on whether the task is forecasting, classification, dimensionality reduction, or construction of a proxy for an otherwise latent economic object [@mullainathanMachineLearningApplied2017].

## Field Core

### 1. Prediction as object versus prediction as input

A useful starting distinction is between prediction as the final estimand and prediction as an input into another empirical design.

Prediction is the final object when the substantive question is itself predictive: default risk, worker attrition, hiring success, vacancy fill probability, or program take-up risk. Prediction is an input when the model is used to construct a variable later used in an economics design: a job-posting skill measure, an occupational code, an exposure index, a climate score, or an imputed latent outcome [@mullainathanMachineLearningApplied2017; @ikudoOccupationalClassificationsMachine2018; @dahlhausFromOnlineJob2025].

That distinction matters because the evaluation criteria differ. If prediction is the final object, out-of-sample performance is central. If prediction is an input into later research, calibration, measurement error, transportability, and interpretability often matter more than a small gain in predictive loss.

### 2. Training, testing, and generalization

Let \(Y_i\) be the prediction target and \(X_i\) the feature vector. A prediction rule \(\hat f(X_i)\) is judged by expected loss:

```{math}
:label: eq:prediction-risk
R(f) = \mathbb{E}[L(Y, f(X))].
```

In practice, we approximate this with empirical risk on a held-out sample. The point of train/test separation is not ritual; it is to estimate how well the rule generalizes beyond the training data.

Cross-validation chooses tuning parameters by minimizing an estimate of out-of-sample risk:

```{math}
:label: eq:cv
\hat \lambda = \arg\min_{\lambda \in \Lambda} \frac{1}{K}\sum_{k=1}^K \frac{1}{|V_k|}\sum_{i \in V_k} L\left(Y_i, \hat f_{-k,\lambda}(X_i)\right).
```

Students should leave this lecture understanding that generalization error is an empirical object, not a slogan. Any claim about prediction quality should answer: on which target population, under which loss, with what validation rule, and with what uncertainty?

### 3. Regularization: why and how

High-dimensional applied data create a classic bias–variance tradeoff. Regularization sacrifices some in-sample fit in order to reduce variance and improve out-of-sample performance.

For a linear model with parameters \(\beta\), lasso solves:

```{math}
:label: eq:lasso
\hat\beta^{lasso} = \arg\min_{\beta} \frac{1}{n}\sum_{i=1}^n (Y_i - X_i'\beta)^2 + \lambda \sum_{j=1}^p |\beta_j|.
```

Ridge replaces the \(\ell_1\) penalty with an \(\ell_2\) penalty:

```{math}
:label: eq:ridge
\hat\beta^{ridge} = \arg\min_{\beta} \frac{1}{n}\sum_{i=1}^n (Y_i - X_i'\beta)^2 + \lambda \sum_{j=1}^p \beta_j^2.
```

Elastic net combines both:

```{math}
:label: eq:elastic-net
\hat\beta^{EN} = \arg\min_{\beta} \frac{1}{n}\sum_{i=1}^n (Y_i - X_i'\beta)^2 + \lambda \left[ \alpha \sum_{j=1}^p |\beta_j| + (1-\alpha)\sum_{j=1}^p \beta_j^2 \right].
```

The key applied questions are:
- Is sparsity substantively plausible?
- Are predictors highly collinear?
- Is variable selection itself part of the economic interpretation, or merely a prediction device?
- Is the tuning rule stable across samples?

For economists, the most influential applied message from high-dimensional work is not “use lasso everywhere,” but “treat variable selection as part of the inferential problem” [@belloniHighDimensionalMethodsInference2014].

### 4. What prediction contributes to applied measurement

This is the section where ML becomes economics.

In modern applied work, prediction is often used to transform messy raw data into economically meaningful variables. Examples include:
- classifying occupations from raw HR job titles [@ikudoOccupationalClassificationsMachine2018];
- structuring online job postings into skills, tasks, or technology categories [@dahlhausFromOnlineJob2025; @turrellTransformingNaturallyOccurring2019];
- building remote-work feasibility or AI-exposure measures from text [@hansenRemoteWorkAcross2023];
- constructing risk scores or expected outcomes that feed into later policy or treatment analyses [@mullainathanMachineLearningApplied2017].

In all of these cases, the central economics question is whether the predicted object corresponds to the conceptual construct needed for the research design.

### 5. Implementation details and pitfalls

The most common failure in practice is not choosing the wrong algorithm. It is choosing the wrong target, the wrong split, or the wrong evaluation metric.

Important implementation checks include:
- **target leakage**: does a feature contain post-outcome or post-treatment information?
- **class imbalance**: are rare outcomes being predicted with misleadingly high average accuracy?
- **calibration**: does a predicted probability of 0.2 actually correspond to roughly 20 percent event frequency?
- **instability**: do selected features or scores change dramatically across folds or samples?
- **drift**: is the model trained in one period or context but used in another?
- **transportability**: does the predictive rule survive across firms, occupations, regions, or countries?
- **fairness and subgroup error**: are prediction errors systematically larger for groups that matter for the downstream economics question?

A measured empirical researcher should report these diagnostics explicitly. Prediction quality without implementation transparency is hard to evaluate and easy to oversell.

## Research Lab

### Primary anchor paper

A useful primary anchor is [@dahlhausFromOnlineJob2025], which shows how machine learning can turn raw online job postings into structured variables that support economic measurement. The key lesson is that the model is only useful because the predicted objects are clearly tied to downstream labor-market questions.

### Reproduce

Reproduce a bounded version of the paper’s core workflow using a small labeled text or occupation dataset:
- define the target labels clearly;
- train a simple classifier;
- evaluate out-of-sample performance;
- compare basic baseline rules to the regularized or ML model.

### Diagnose

Diagnose the economic credibility of the measurement object:
- is the label definition stable?
- is the training sample representative of the research population?
- is the classifier calibrated?
- what downstream research claim would fail if the classification error is systematic rather than random?

### Transfer

Transfer the design to a nearby applied problem such as:
- occupational coding from administrative job titles [@ikudoOccupationalClassificationsMachine2018];
- building a remote-work or AI-related posting measure [@hansenRemoteWorkAcross2023];
- constructing a technology or skill-intensity measure from text [@turrellTransformingNaturallyOccurring2019].

The goal is not to build the best classifier in the world. It is to learn how prediction becomes an economic measurement object that can be defended in a later empirical design.

## Methods Box

### Practical rules for applied economists

1. Start with the economics object, not the algorithm.
2. Write down the prediction target and loss before training.
3. Use training/validation/test separation honestly.
4. Prefer simple benchmarks before moving to complex models.
5. Report calibration and subgroup performance, not only average loss.
6. Treat variable selection as part of inference if the downstream task is causal or explanatory [@belloniHighDimensionalMethodsInference2014].
7. Ask whether the predicted object is portable to the population where the research claim will be made.

## Reading Ladder And References

### Core methodological readings

- [@mullainathanMachineLearningApplied2017]
- [@belloniHighDimensionalMethodsInference2014]

### Applied measurement and labor-market readings

- [@ikudoOccupationalClassificationsMachine2018]
- [@dahlhausFromOnlineJob2025]
- [@turrellTransformingNaturallyOccurring2019]
- [@hansenRemoteWorkAcross2023]

## Exercises And Discussion Prompts

1. Give one example where prediction is the final research object and one where it is only an input into later empirical work.
2. Why can a model with lower prediction loss still be worse for an economics application?
3. In what empirical settings is lasso more attractive than ridge, and vice versa?
4. Suppose a job-postings classifier has high average accuracy but poor subgroup calibration across regions. What downstream claims would this threaten?
5. What counts as target leakage in an administrative-data labor application?

## Reproducibility And Code Lab Note

The bounded teaching lab for this lecture should use a small labeled text or classification dataset and a transparent Python workflow that demonstrates:
- train/test separation,
- tuning via cross-validation,
- comparison of regularization choices,
- and downstream measurement diagnostics.

## Slide Companion Note

The lecture deck should include one slide each on:
- prediction versus design,
- penalized loss functions,
- job-posting / occupation-classification applications,
- implementation pitfalls,
- and the Research Lab workflow.

## Bridge Forward

Lecture 10 turns from prediction and measurement to heterogeneity and causal ML. The key transition is that Lecture 9 is mostly about building better empirical objects, whereas the next lecture asks how flexible learners can help estimate treatment heterogeneity and causal structure without discarding the logic of identification.
