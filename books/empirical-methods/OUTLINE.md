# Empirical Methods for Applied Economics

## Course Role

Empirical Methods for Applied Economics is the portfolio's standalone methods course for students who want to produce credible applied research. It is broader than labor economics, but it is written from the perspective of a labor economist who needs to move between policy variation, administrative data, experiments, structural models, machine learning, text, spatial data, and networks without losing the economic question.

The course should not become a generic econometrics notes sequence. Every block begins from an applied research problem: what parameter is useful, what comparison identifies it, what model or algorithm adds, and what evidence would convince a skeptical reader.

## Cumulative Logic

The core course is organized into four blocks.

1. **Traditional reduced-form / design-based methods** establish potential outcomes, experiments, selection-on-observables, DID, event studies, synthetic control, IV, RD, RKD, and bunching.
2. **Structural estimation** explains when economic structure is needed, how to estimate it, and how to use it for counterfactuals.
3. **Machine learning for applied economics** keeps prediction, regularization, heterogeneity, and causal ML connected to applied research design.
4. **Text, computation, and LLM-based methods** treats text and language models as measurement and workflow tools that require validation, documentation, and research discipline.

Two additional blocks are deliberately flexible. They can be added at the end of a full course, taught as separate mini-modules, or used as advanced methods add-ons for labor, urban, development, public, or organizational research.

## Internal Roadmap

- **Core Block 1:** Lectures 1 to 5, traditional reduced-form and design-based methods.
- **Core Block 2:** Lectures 6 to 8, structural estimation.
- **Core Block 3:** Lectures 9 to 11, machine learning for applied economics.
- **Core Block 4:** Lectures 12 to 14, text, computation, and LLM-based methods.
- **Flexible Optional Block 5:** Lectures 15 to 17, spatial methods.
- **Flexible Optional Block 6:** Lectures 18 to 20, network methods.

## Chapter Build Notes

Future lecture chapters should use the portfolio's layered format. The default section order is:

1. Learning Objectives
2. Opening Orientation
3. Core Points section containing the `Core points` admonition
4. Bridge
5. Field Core
6. Research Lab
7. Methods Box
8. optional block-summary section only at block endpoints
9. Reading Ladder And References
10. Exercises And Discussion Prompts
11. Reproducibility And Code Lab Note
12. Slide Companion Note
13. Bridge Forward

Use `Core Points` as the visible chapter heading and `Core points` as the admonition title. Do not use `Core materials` in empirical-methods chapters.

Use linked citation syntax in prose markdown, such as `[@imbensRubin2015]`. Draw references from this course's local `references.bib`; do not rely on the labor-series shared bibliography as the primary bibliography for this course.

## Core Blocks 1-4

## Block 1. Traditional Reduced-Form / Design-Based Methods

This block teaches the methods applied economists use most often to make credible claims from variation in the world. The sequence begins with potential outcomes and target parameters, adds selection-on-observables as an explicit design, then moves through experiments, panel designs, instruments, and discontinuities. The goal is to make students fluent in the language of identification before they specialize.

### Lecture 1. Potential Outcomes, Identification Logic, and Selection-On-Observables

**Central question:** What does it mean to identify a causal effect, and when can observables make a comparison credible?

This lecture defines potential outcomes, treatment assignment, estimands, counterfactuals, overlap, conditional independence, matching, reweighting, and regression adjustment. It treats selection-on-observables as a real design rather than as a weak default: students learn when rich covariates, institutional knowledge, and balance diagnostics can support a credible comparison, and when they cannot.

**Why it matters for applied economics research:** Every empirical paper needs a clear target parameter and a credible counterfactual, even when the design is later framed as experimental, quasi-experimental, structural, or predictive.

### Lecture 2. Experiments and Field Experiments

**Central question:** What do randomized experiments identify, and what remains hard after randomization?

This lecture covers random assignment, compliance, attrition, spillovers, clustered designs, power, pre-analysis plans, field implementation, and external validity. It emphasizes that experiments are not only a gold-standard design but also a discipline for defining treatments, outcomes, implementation channels, and welfare-relevant margins.

**Why it matters for applied economics research:** Experiments clarify causal mechanisms and policy design, but applied researchers still need to handle implementation, inference, interpretation, and portability.

### Lecture 3. DID, Event Studies, and Synthetic Control

**Central question:** How can panel or repeated-cross-section data identify effects when treatment timing varies across groups or places?

This lecture studies difference-in-differences, event-study designs, staggered adoption, pre-trends, treatment-effect heterogeneity, weighting problems, modern DID estimators, and synthetic control. Synthetic control remains in this lecture because it answers the same applied question as DID: how to construct a credible counterfactual path for treated units using untreated comparisons.

**Why it matters for applied economics research:** Many policy, labor-market, firm, regional, and institutional studies depend on comparing outcome paths before and after shocks.

### Lecture 4. Instrumental Variables

**Central question:** When can a source of external variation identify a causal effect for a meaningful population?

This lecture covers exclusion, relevance, monotonicity, local average treatment effects, weak instruments, first-stage interpretation, many-instrument concerns, shift-share designs, and the substantive content of an instrument. The emphasis is on making the instrument's economic story visible rather than treating IV as a mechanical correction.

**Why it matters for applied economics research:** IV is often the bridge between structural questions, policy variation, and observational data when treatment choice is endogenous.

### Lecture 5. Regression Discontinuity, RKD, and Bunching

**Central question:** What can be learned when rules, thresholds, kinks, or nonlinear incentives create local variation?

This lecture separates sharp and fuzzy RD, local polynomial estimation, bandwidth choice, manipulation tests, sorting, regression kink designs, and bunching around tax or program schedules. It stresses the difference between local causal effects at thresholds, behavioral responses to kinks, and sufficient-statistics interpretations of bunching.

**Why it matters for applied economics research:** Many applied settings are governed by administrative rules, eligibility cutoffs, nonlinear schedules, and incentives that create disciplined local comparisons.

## Block 2. Structural Estimation

This block teaches structure as a research choice rather than as a rival ideology to design-based work. Structural methods become useful when the question requires latent primitives, dynamic behavior, equilibrium response, welfare, or policy counterfactuals outside the observed support. The block keeps identification, estimation, fit, computation, and economic interpretation tied together.

### Lecture 6. When and Why Structure? Static and Dynamic Decision Problems

**Central question:** When does an applied question require an economic model rather than only a credible comparison?

This lecture introduces structural estimation through discrete choice, static labor supply, dynamic schooling or job-search decisions, state variables, expectations, and latent preferences or technologies. Students learn to ask what is observed, what is latent, what the model adds, and what counterfactual would be impossible without structure.

**Why it matters for applied economics research:** Structural models are essential when policy evaluation depends on behavior under new rules, dynamic incentives, or welfare objects not directly observed in the data.

### Lecture 7. Structural Estimation in Practice: Identification, Moments, Likelihood, Simulation, and Fit

**Central question:** How do researchers take a structural model to data credibly?

This lecture covers identification arguments, likelihood, method of moments, simulated method of moments, indirect inference intuition, counterfactual validation, goodness of fit, sensitivity, and transparent reporting. The focus is not only computational implementation but also the connection between moments, primitives, and the substantive claim.

**Why it matters for applied economics research:** Structural estimates are persuasive only when readers can see which variation identifies the model and how well the model explains the empirical objects it claims to match.

### Lecture 8. Equilibrium Structural Work: Search, Spatial, Industry/Market, and Policy Counterfactuals

**Central question:** How do structural models change once individual decisions interact through markets, prices, locations, or firms?

This lecture studies equilibrium structure through search and matching, wage-setting, spatial equilibrium, industrial organization, market power, and general-equilibrium policy counterfactuals. It emphasizes the gains and risks of equilibrium modeling: richer incidence and welfare analysis, but stronger assumptions and heavier validation burdens.

**Why it matters for applied economics research:** Many applied policies reshape markets rather than only treated individuals, so credible research often needs a way to model equilibrium response.

## Block 3. Machine Learning for Applied Economics

This compact block teaches machine learning as a set of tools for prediction, measurement, heterogeneity, and causal estimation. The course avoids treating ML as a substitute for research design. Instead, it asks how regularization, sample splitting, high-dimensional controls, and flexible functions can help applied economists answer better-defined empirical questions.

### Lecture 9. Prediction, Regularization, and Applied Measurement

**Central question:** When is prediction itself the research object, and when is it an input into measurement or design?

This lecture covers train-test splits, cross-validation, regularization, model selection, overfitting, prediction loss, feature engineering, and interpretable measurement. Applications include risk scores, job-posting measures, occupational exposure, firm classification, and imputing missing or latent outcomes.

**Why it matters for applied economics research:** Prediction tools can create useful measurements and diagnostics, but only when the prediction target, training data, and research use are aligned.

### Lecture 10. High-Dimensional Controls, Heterogeneity, and Double/Debiased ML

**Central question:** How can flexible methods help estimate causal effects without turning nuisance prediction into the answer?

This lecture studies high-dimensional controls, orthogonalization, sample splitting, double/debiased ML, treatment heterogeneity, causal forests, and the distinction between prediction accuracy and valid causal inference. Students learn why nuisance functions are useful precisely because they are not the parameter of interest.

**Why it matters for applied economics research:** Modern data often contain many controls, firms, places, histories, and text-derived measures, and applied economists need tools that use them without overclaiming.

### Lecture 11. Causal ML, Policy Learning, and External Validity

**Central question:** How should researchers use heterogeneous treatment effects to guide policy or interpret portability?

This lecture covers individualized treatment effects, subgroup discovery, policy learning, targeting, uplift, fairness, external validity, and distribution shift. The emphasis is on how ML can organize heterogeneity while leaving welfare, constraints, and implementation as economic questions.

**Why it matters for applied economics research:** Applied policy work increasingly asks not only whether an intervention works, but for whom, under which constraints, and with what targeting rule.

## Block 4. Text, Computation, and LLM-Based Methods

This compact block treats text, documents, and language models as data-generating and measurement environments. Students learn to build text-as-data variables, validate extraction and classification workflows, and use LLMs in ways that are reproducible, auditable, and appropriate for applied economics research.

### Lecture 12. Text as Data and Computational Measurement

**Central question:** How can unstructured text become a credible economic measure?

This lecture covers corpora, preprocessing, dictionaries, supervised classification, topic models, embeddings, document-level outcomes, and measurement error. Applications include job ads, resumes, firm filings, policy text, union contracts, court documents, news, and open-ended survey responses.

**Why it matters for applied economics research:** Many economically important objects are written before they are numeric, and text methods let researchers study tasks, rules, beliefs, vacancies, contracts, and narratives at scale.

### Lecture 13. Extraction, Classification, Embeddings, and Validation

**Central question:** How should researchers validate text-derived variables before using them in causal or descriptive work?

This lecture studies labeled data, annotation protocols, inter-rater reliability, precision and recall, calibration, embedding-based similarity, benchmark sets, measurement error, human review, and model drift. It treats validation as part of identification because a biased measurement process can change the economic interpretation of downstream estimates.

**Why it matters for applied economics research:** Text-derived variables are persuasive only when readers understand what the algorithm measures, where it fails, and how those errors affect the research design.

### Lecture 14. LLM Workflows for Applied Research

**Central question:** How can language models support applied research without weakening reproducibility or evidentiary standards?

This lecture covers LLM-assisted coding, extraction, classification, summarization, synthetic labels, prompt documentation, retrieval, audit trails, privacy, hallucination risk, replication packages, and human-in-the-loop review. The focus is on using LLMs as research infrastructure, not as an authority that replaces validation.

**Why it matters for applied economics research:** LLMs can lower the cost of working with documents and code, but publishable research still requires transparent data construction, uncertainty assessment, and reproducible workflows.

## Flexible Optional Blocks

The following blocks are optional by design. They can be taught after the core, attached to relevant field courses, or offered as independent short methods modules.

## Flexible Optional Block 5. Spatial Methods

Spatial methods are increasingly central in applied economics because many policies, shocks, and markets are organized across places. This optional block moves from spatial data construction to spatial causal inference and then to quantitative spatial models.

### Lecture 15. Curating Maps and Spatial Data

**Central question:** How do researchers turn places, borders, distances, and exposure measures into usable empirical objects?

This lecture covers geocoding, shapefiles, projections, crosswalks, buffers, distance measures, commuting zones, administrative boundaries, raster data, spatial joins, and confidentiality. It emphasizes that spatial data work is not clerical: boundary choices and exposure definitions shape estimands.

**Why it matters for applied economics research:** Local labor, policy, environment, housing, development, and transportation studies depend on defensible place definitions and reproducible spatial measurement.

### Lecture 16. Causal Inference with Spatial Data

**Central question:** How do spatial spillovers, sorting, exposure, and correlated shocks change causal designs?

This lecture studies spatial clustering, Conley-style standard errors, spillovers, interference, exposure mappings, border designs, shift-share and place-based designs, spatial mismatch, and the modifiable areal unit problem. Students learn to diagnose whether geography is the source of identification, a threat to inference, or the mechanism itself.

**Why it matters for applied economics research:** Spatial dependence can create useful variation, but it can also invalidate standard comparisons when nearby units share shocks or affect one another.

### Lecture 17. Spatial Structural Modeling

**Central question:** When do applied questions require a model of how workers, firms, rents, amenities, and trade costs interact across space?

This lecture introduces quantitative spatial equilibrium models, commuting and migration flows, housing supply, local labor demand, amenities, incidence, and counterfactual policy analysis. The goal is to connect reduced-form place effects to structural objects such as moving costs, local productivity, welfare, and equilibrium adjustment.

**Why it matters for applied economics research:** Many place-based policies and shocks have incidence through wages, rents, migration, commuting, and firm location, which are difficult to evaluate with partial-equilibrium evidence alone.

## Flexible Optional Block 6. Network Methods

Network methods are useful when outcomes depend on relationships rather than only individual characteristics. This optional block teaches students to construct network data, use network structure in causal designs, and understand structural network models for peer effects, referrals, diffusion, and matching.

### Lecture 18. Curating Network Data and Descriptive Statistics

**Central question:** How should researchers define, measure, and summarize the relationships that shape economic outcomes?

This lecture covers nodes, edges, directed and weighted links, administrative and survey network data, co-worker and neighborhood networks, referrals, centrality, clustering, homophily, components, missing links, and privacy. It emphasizes that network definition is a substantive economic choice, not merely a data format.

**Why it matters for applied economics research:** Networks shape job information, referrals, peer effects, learning, diffusion, bargaining, and inequality across workers, firms, schools, and places.

### Lecture 19. Causal Inference with Network Data

**Central question:** How can researchers estimate effects when units influence one another through observed or latent links?

This lecture covers the reflection problem, peer effects, interference, spillovers, randomized saturation designs, network experiments, exposure mappings, partial interference, and inference under dependence. Students learn why network causality requires explicit assumptions about who affects whom and through which channel.

**Why it matters for applied economics research:** Many applied interventions operate through peers, managers, classmates, co-workers, firms, or neighborhoods, so individual-level treatment effects may miss the main mechanism.

### Lecture 20. Structural Modeling with Network Data

**Central question:** When is a model of network formation or network-mediated behavior needed for counterfactuals?

This lecture introduces structural peer-effects models, network formation, search and referral models, diffusion, matching, equilibrium behavior on networks, and policy counterfactuals that change links or information flows. The focus is on the extra discipline needed when links are endogenous and outcomes feed back into relationships.

**Why it matters for applied economics research:** Structural network models can evaluate policies that change relationships, information, and matching opportunities, but they require careful assumptions about formation, behavior, and equilibrium response.
