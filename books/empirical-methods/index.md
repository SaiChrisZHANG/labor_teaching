# Empirical Methods for Applied Economics

Empirical Methods for Applied Economics is a research-facing methods course for students who want to conduct credible applied economics research. The course is broader than labor economics, but it is written from a labor-economics user perspective: students learn methods because they need to answer questions about workers, firms, households, places, policies, markets, and institutions with real data.

The course exists as a separate methods course because the labor sequence and special-topic courses use empirical methods constantly, but they cannot teach the full architecture behind them. This course gives that architecture its own home. It connects design-based causal inference, structural estimation, machine learning, text and LLM workflows, spatial methods, and network methods through one applied-research discipline: define the economic question, state the counterfactual, understand the data-generating process, validate the measurement, and explain what the evidence can and cannot support.

## Prerequisites

- Graduate econometrics or a strong equivalent
- Graduate microeconomic theory or comfort with economic models
- Prior exposure to applied empirical papers in labor, public, development, urban, industrial organization, or related fields
- Working knowledge of Python or willingness to use Python for reproducible labs
- Labor I or Labor II is useful for examples, but not required

## What Students Will Be Able To Do

By the end of the course, students should be able to:

1. translate applied research questions into estimands, counterfactuals, data requirements, and identification claims;
2. evaluate experiments, selection-on-observables designs, DID/event studies, synthetic controls, IV, RD, RKD, and bunching designs;
3. explain when structural estimation is necessary and how identification, estimation, fit, and counterfactuals work together;
4. use machine learning for prediction, measurement, heterogeneity, and causal estimation without confusing flexible prediction with identification;
5. build and validate text, computational, and LLM-based research workflows;
6. recognize when spatial or network structure changes measurement, inference, identification, or equilibrium interpretation.

## Course Format

The course is organized in blocks rather than as a flat list of methods. The core course has four blocks: traditional reduced-form and design-based methods; structural estimation; machine learning for applied economics; and text, computation, and LLM-based methods. Two additional blocks on spatial methods and network methods are flexible by design. They can be taught at the end of a full course, as short advanced modules, or as methods add-ons for field courses.

This is a reading-heavy and research-oriented course for PhD students and advanced MA students. Lectures should pair methodological logic with applied economics examples, research design discussion, and reproducibility-oriented labs. The goal is not to memorize estimators. The goal is to learn how applied economists make credible claims.

## Complement To The Portfolio

Labor I supplies worker-side economic objects: labor supply, human capital, households, wages, inequality, mobility, discrimination, and policy. Labor II adds firms, frictions, wage-setting, institutions, market power, and shocks. The special-topic courses deepen substantive areas such as behavioral labor, institutions, gender, technology, urban labor, health and population, and labor-market design.

Empirical Methods complements all of them by making the research toolkit explicit. It teaches students how to choose among designs, models, algorithms, and data workflows when moving from a substantive economic question to a publishable empirical project.

## Block-By-Block Course Map

**Block 1: Traditional Reduced-Form / Design-Based Methods.** Students learn potential outcomes, identification logic, selection-on-observables, matching and reweighting, experiments, DID, event studies, synthetic control, IV, RD, RKD, and bunching. This is the core toolkit used most often in applied economics papers.

**Block 2: Structural Estimation.** Students study when and why economic structure is useful, how models are identified and estimated, and how structural work supports welfare and policy counterfactuals in static, dynamic, and equilibrium settings.

**Block 3: Machine Learning for Applied Economics.** Students learn how prediction, regularization, high-dimensional controls, heterogeneity, causal forests, double/debiased ML, and policy learning can support applied research when paired with clear research design.

**Block 4: Text, Computation, and LLM-Based Methods.** Students learn how to turn text, documents, job ads, contracts, open-ended responses, and LLM-assisted workflows into auditable and validated research inputs.

**Flexible Block 5: Spatial Methods.** This optional block covers spatial data construction, maps, exposure measures, spatial causal inference, spillovers, spatial dependence, and quantitative spatial models.

**Flexible Block 6: Network Methods.** This optional block covers network data construction, descriptive network statistics, peer effects, interference, network experiments, and structural models of network behavior or formation.

## Research Orientation

The course is designed to help students leave with better research instincts. A successful student should be able to read an applied paper and identify the estimand, source of variation, identifying assumptions, measurement strategy, validation evidence, inference problem, and counterfactual claim. They should also be able to design their own empirical project with enough discipline that the method serves the question rather than becoming the question.

## Current Modules

### Core Blocks 1-4

**Block 1: Traditional Reduced-Form / Design-Based Methods**

- [Lecture 1. Potential Outcomes, Identification Logic, And Selection-On-Observables](01-potential-outcomes-identification-logic-and-selection-on-observables.md)
- [Lecture 2. Experiments And Field Experiments](02-experiments-and-field-experiments.md)
- [Lecture 3. DID, Event Studies, And Synthetic Control](03-did-event-studies-and-synthetic-control.md)
- [Lecture 4. Instrumental Variables, 2SLS, And Instrument Design](04-instrumental-variables-2sls-and-instrument-design.md)
- [Lecture 5. Regression Discontinuity, RKD, Bunching, And Local Designs](05-regression-discontinuity-rkd-bunching-and-local-designs.md)

**Block 2: Structural Estimation**

- [Lecture 6. When And Why Structure? Static And Dynamic Decision Problems](06-when-and-why-structure-static-and-dynamic-decision-problems.md)
- [Lecture 7. Structural Estimation In Practice: Identification, Moments, Likelihood, Simulation, And Fit](07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.md)
- [Lecture 8. Equilibrium Structural Work: Search, Spatial, Industry/Market, And Policy Counterfactuals](08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.md)

**Block 3: Machine Learning For Applied Economics**

- [Lecture 9. Prediction, Regularization, And Applied Measurement](09-prediction-regularization-and-applied-measurement.md)
- [Lecture 10. High-Dimensional Controls, Heterogeneity, And Double/Debiased ML](10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md)
- [Lecture 11. Causal ML, Policy Learning, And External Validity](11-causal-ml-policy-learning-and-external-validity.md)

**Block 4: Text, Computation, And LLM-Based Methods**

- [Lecture 12. Text As Data And Computational Measurement](12-text-as-data-and-computational-measurement.md)
- [Lecture 13. Extraction, Classification, Embeddings, And Validation](13-extraction-classification-embeddings-and-validation.md)
- [Lecture 14. LLM Workflows For Applied Research](14-llm-workflows-for-applied-research.md)

### Flexible Optional Blocks 5-6

**Flexible Optional Block 5: Spatial Methods**

- [Lecture 15. Curating Maps And Spatial Data](15-curating-maps-and-spatial-data.md)
- [Lecture 16. Causal Inference With Spatial Data](16-causal-inference-with-spatial-data.md)
- [Lecture 17. Spatial Structural Modeling](17-spatial-structural-modeling.md)

**Flexible Optional Block 6: Network Methods**

- [Lecture 18. Curating Network Data And Descriptive Statistics](18-curating-network-data-and-descriptive-statistics.md)
- [Lecture 19. Causal Inference With Network Data](19-causal-inference-with-network-data.md)
- [Lecture 20. Structural Modeling With Network Data](20-structural-modeling-with-network-data.md)
