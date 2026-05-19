# Lecture 13. Extraction, Classification, Embeddings, And Validation

## Learning Objectives

By the end of this lecture, students should be able to:

1. design labeled-data, annotation, and benchmark protocols for text, image, audio, video, or multimodal measures;
2. interpret precision, recall, F1, calibration, subgroup performance, inter-rater reliability, and drift diagnostics;
3. explain why validation is part of identification when a constructed variable enters descriptive, causal, structural, or policy analysis;
4. use human review, embedding audits, and external validation to defend what an unstructured-data measure captures;
5. diagnose how measurement error changes downstream economic interpretation;
6. design a Reproduce -> Diagnose -> Transfer validation lab for a constructed variable.

## Opening Orientation

Lecture 12 asked how raw unstructured objects become economic variables. Lecture 13 asks the next question: **how do we know what those variables actually measure?** This is not another extraction lecture. The focus is validation, robustness, benchmark design, measurement error, subgroup performance, drift, and downstream interpretation.

The economic problem is sharper than generic predictive accuracy. A remote-work classifier, a poverty proxy from satellite imagery, an audio-derived tone measure, or a video-coded interaction measure may look accurate on average and still be unusable for the research claim. If the constructed variable is biased for treated firms, particular occupations, lower-income places, nonstandard speakers, or later years, then the downstream estimate may answer a different question than the one written in the paper.

The paper spine illustrates that validation is part of applied design. Gentzkow, Kelly, and Taddy give the economics framework for text-as-data validation [@gentzkowKellyTaddy2019]. Hansen and coauthors use labeled data and validation logic to defend remote-work measures from job postings [@hansenRemoteWorkAcross2023]. Haaland and coauthors show why open-ended responses and LLM-assisted coding need explicit protocols and human review [@haalandRothStantchevaWohlfart2024]. Jean and coauthors validate image-derived poverty predictions against survey ground truth [@jeanBurkeXieDavisLobellErmon2016]. Gorodnichenko, Pham, and Talavera show how audio-derived variables can be tied to market reactions rather than treated as opaque vocal scores [@gorodnichenkoPhamTalavera2023]. Blattman and coauthors, and Bound, Brown, and Mathiowetz, provide the broader warning that measurement itself can be the fragile part of an empirical design [@blattmanJamisonKoroknayPaliczRodriguesSheridan2016; @bound2001measurementError].

## Core Points

:::{admonition} Core points
:class: important

- Validation is part of identification when text, images, audio, video, or multimodal records are used to build economic variables.
- Benchmarks are designed objects: label definitions, annotators, adjudication, and held-out samples shape what the model learns.
- Precision, recall, F1, calibration, subgroup performance, and drift answer different questions. No single average metric is enough.
- Inter-rater reliability and human review diagnose whether labels are stable, but they do not by themselves prove construct validity.
- Embedding-based similarity needs external validation and neighbor audits because semantic proximity is not automatically an economic construct.
- Measurement error can bias descriptive aggregates, causal estimates, heterogeneity claims, and policy targeting, especially when errors are differential.
- A credible paper reports robustness, sensitivity, and transportability checks before interpreting the constructed measure economically.
:::

## Bridge

Lecture 12 framed unstructured-data work as a measurement problem. Lecture 13 makes that measurement problem auditable. The core move is to treat validation evidence as part of the research design, not as a software appendix.

```{include} assets/tables/13-theory-to-applied-bridge.md
```

The bridge from construction to validation is simple but demanding. If {math}`\widehat M_i` is a constructed economic measure from a raw object {math}`U_i`, the paper must say what benchmark or external evidence links {math}`\widehat M_i` to the latent object {math}`M_i^*`. Without that link, the regression, event study, decomposition, structural moment, or targeting rule is built on an object whose meaning is uncertain.

## Field Core

### A. Validation As Part Of Identification

Let {math}`U_i` be a raw unstructured record, such as a document, image, audio clip, video segment, or multimodal trace. Let {math}`M_i^*` be the intended economic object and let {math}`\widehat M_i` be the constructed measure. Lecture 12 emphasized the mapping:

```{math}
:label: eq:em13-measurement-map
\widehat M_i = g(U_i; \widehat\theta).
```

Lecture 13 asks whether {math}`\widehat M_i` is valid for the use at hand. That question has several layers:

- **Construct validity:** does the measure correspond to the intended economic object?
- **Benchmark validity:** do labels or ground truth represent the construct, or only a convenient proxy?
- **Predictive validity:** does the algorithm recover the benchmark in held-out data?
- **Subgroup validity:** does it work similarly by group, place, occupation, language, speaker, sensor, or time?
- **External validity:** does it travel beyond the labeled sample?
- **Downstream validity:** do remaining errors change the descriptive or causal interpretation?

Validation becomes identification when the constructed measure supplies the outcome, treatment, covariate, exposure, running variable, instrument, structural moment, or policy score. A clean downstream estimator cannot rescue a variable whose errors are correlated with the source of identifying variation.

### B. Labeled Data, Annotation Protocols, And Benchmark Construction

Benchmarks are not found; they are built. A researcher must decide the unit of labeling, label definition, annotator pool, instructions, examples, edge cases, adjudication rule, and held-out benchmark design. Those choices define the target the model learns.

```{include} assets/tables/13-annotation-and-benchmark-design.md
```

Suppose two annotators label the same binary construct. A common reliability statistic is Cohen's kappa:

```{math}
:label: eq:em13-kappa
\kappa = \frac{p_o - p_e}{1 - p_e},
```

where {math}`p_o` is observed agreement and {math}`p_e` is expected agreement under chance agreement. A high {math}`\kappa` is evidence that labelers can apply the rubric consistently. It is not evidence that the rubric is economically correct. Annotators can agree on a proxy that misses the latent construct, especially in settings with institutional jargon, ambiguous open-ended responses, nonstandard language, image artifacts, accent variation, or context-dependent video behavior.

Human review should therefore be designed, not improvised. A strong protocol includes written instructions, training examples, blind double coding, adjudication for disagreements, audit samples from model errors, and a plan for relabeling when drift appears.

### C. Precision, Recall, F1, And Calibration

For a binary classifier, the confusion matrix defines true positives {math}`TP`, false positives {math}`FP`, false negatives {math}`FN`, and true negatives {math}`TN`. Three basic metrics are:

```{math}
:label: eq:em13-precision
\text{Precision} = \frac{TP}{TP + FP},
```

```{math}
:label: eq:em13-recall
\text{Recall} = \frac{TP}{TP + FN},
```

```{math}
:label: eq:em13-f1
F_1
=
2\cdot
\frac{\text{Precision}\cdot\text{Recall}}
{\text{Precision}+\text{Recall}}.
```

Precision asks whether predicted positives are credible. Recall asks whether true positives were found. F1 summarizes one tradeoff, but it is not a welfare or research-design objective. A study of rare workplace-safety violations may prioritize recall. A study that flags firms for legal exposure may prioritize precision. A descriptive aggregate may need calibrated probabilities more than a hard threshold.

Calibration is the requirement that predicted probabilities correspond to realized frequencies:

```{math}
:label: eq:em13-calibration
E[Y \mid \widehat p = p] = p.
```

A model can rank cases well and still be poorly calibrated. That matters for threshold rules, policy targeting, subgroup prevalence estimates, cost-benefit calculations, and any paper that interprets the score as a probability or intensity.

```{include} assets/tables/13-validation-diagnostics.md
```

### D. Subgroup Performance, Fairness, And Drift

Average performance is not enough. Let {math}`G_i` denote a group, domain, occupation, region, time period, language, speaker type, sensor, platform, or institution. Validation should ask whether metrics differ across {math}`G_i`:

```{math}
:label: eq:em13-subgroup-error
\Pr(\widehat Y_i \neq Y_i \mid G_i = g).
```

Subgroup performance is a fairness issue when model errors burden some groups more than others. It is also an identification issue. If false negatives are higher for service-sector jobs, a study of remote work by occupation will understate access in those jobs. If an image poverty proxy works poorly in dense informal settlements, spatial inequality estimates may be distorted. If an audio model performs differently by gender, accent, or recording device, an apparent "tone" measure may partly capture identity or technology.

Drift extends the same logic over time and across domains. Vocabulary changes, firms update posting templates, image sensors change, speech recording quality improves, and video platforms create new interaction norms. A benchmark that was valid in 2021 may not validate a 2026 measure without relabeling or recalibration.

### E. Embedding-Based Similarity And External Validation

Embeddings help when exact words are too narrow. A text phrase, image, audio segment, video frame, or multimodal record can be represented by a vector {math}`e_i`; similarity to a concept vector {math}`c` is often summarized by cosine similarity:

```{math}
:label: eq:em13-cosine
S_i(c)
=
\frac{e_i'c}{\lVert e_i\rVert\lVert c\rVert}.
```

The attraction is generalization. The risk is that semantic similarity is not the same as an economic construct. "Remote," "digital," and "software" may be close in embedding space, but only some uses measure remote-work feasibility. A satellite image may be close to images from wealthy places because of roads, roofs, or lighting, but the welfare interpretation still needs external ground truth. An audio embedding may separate high- and low-confidence speech, but it may also separate recording environments or speaker identity.

External validation can include independent administrative data, survey measures, expert labels, known aggregates, placebo concepts, manual nearest-neighbor audits, or theory-relevant correlations. For embeddings, researchers should report examples of nearest neighbors, false positives, false negatives, and cases where similarity is high but economic interpretation is weak.

### F. Measurement Error And Downstream Economics

Suppose the intended variable is {math}`X_i`, but the researcher uses a constructed variable:

```{math}
:label: eq:em13-additive-error
\widetilde X_i = X_i + \nu_i.
```

If the downstream model is {math}`Y_i = \alpha + \beta X_i + \varepsilon_i`, using {math}`\widetilde X_i` instead changes the probability limit:

```{math}
:label: eq:em13-downstream-bias
\operatorname{plim}\widehat\beta_{\widetilde X}
=
\beta
\frac{\operatorname{Cov}(\widetilde X_i, \varepsilon_i - \beta\nu_i)}
{\operatorname{Var}(\widetilde X_i)}.
```

Under special classical-error assumptions, the main problem may be attenuation. In unstructured-data settings, those assumptions are often implausible. Errors may be correlated with treatment timing, group membership, outcomes, location, language, job family, platform, image quality, speaker identity, or recording device. Then the bias can move in either direction.

A binary misclassification setup makes the same point. Let:

```{math}
:label: eq:em13-binary-misclassification
\Pr(\widetilde X_i = 1 \mid X_i = 0, G_i=g) = \alpha_g,
\qquad
\Pr(\widetilde X_i = 0 \mid X_i = 1, G_i=g) = \delta_g.
```

If {math}`\alpha_g` or {math}`\delta_g` varies by treatment status, subgroup, place, or time, the measured gap can differ from the true gap. A DID estimate can pick up changing classifier error rather than changing remote-work access. A descriptive inequality measure can reflect subgroup-specific false negatives. A policy-targeting rule can allocate resources toward the best-measured groups rather than the most affected groups.

### G. Robustness, Sensitivity, And Transportability Checks

A defensible validation section usually includes several checks:

- compare dictionaries, supervised models, embeddings, and simple baselines;
- vary thresholds and report the precision-recall tradeoff;
- report calibration overall and by subgroup;
- hold out labels by time, place, firm, occupation, annotator, platform, sensor, or institution;
- audit false positives and false negatives manually;
- compare to external benchmarks not used in training;
- test whether conclusions survive reweighting, relabeling, or recalibration;
- show whether downstream estimates change when the constructed variable is replaced by stricter or looser measures.

Transportability is not automatic. A source benchmark defines a population, labeling standard, and time. A target application may have different language, visual environments, recording conditions, or institutional meanings. The applied question is whether the source validation evidence is relevant for the target economic comparison.

### H. How Applied Papers Defend Their Choices

Hansen and coauthors are useful because the constructed remote-work measure is not the final estimand by itself; it is used to compare jobs, firms, and places [@hansenRemoteWorkAcross2023]. The validation burden is therefore about both classification and economic interpretation: labels, model performance, and plausibility of cross-occupation and cross-place comparisons.

Jean and coauthors show why image-derived measures need external ground truth [@jeanBurkeXieDavisLobellErmon2016]. Satellite images contain many signals, but the economic object is poverty. The defense comes from benchmarking predictions against survey-based measures and studying where the image proxy travels.

Gorodnichenko, Pham, and Talavera illustrate an audio case [@gorodnichenkoPhamTalavera2023]. Voice features are useful only if the paper separates economically meaningful tone or information from speaker identity, institutional context, and recording artifacts.

Haaland and coauthors make annotation and LLM-assisted coding central rather than incidental [@haalandRothStantchevaWohlfart2024]. Open-ended responses can reveal motives, beliefs, and narratives, but the label, prompt, review, and audit protocol shape the object.

Blattman and coauthors show that even survey variables often need qualitative validation [@blattmanJamisonKoroknayPaliczRodriguesSheridan2016]. Bound, Brown, and Mathiowetz provide the classic measurement-error warning for survey data [@bound2001measurementError]. The lesson carries directly to computational measures: the benchmark can be wrong, the proxy can be unstable, and the error structure can be the empirical threat.

## Research Lab

The Week 13 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It centers on validating a constructed variable, not merely building it. The source task is a bounded synthetic teaching analogue of validating a remote-work feasibility measure from job postings. The transfer task moves the same validation design to service-record text with a small image-based infrastructure proxy.

### Reproduce

Students reproduce a validation workflow:

- create a labeled benchmark from two human raters plus adjudication;
- compute inter-rater reliability;
- fit a transparent dictionary score, an embedding-style similarity score, and a supervised baseline;
- report confusion matrices, precision, recall, F1, and calibration;
- compare subgroup performance across sectors, regions, and job families;
- compare model scores to an external audit proxy.

### Diagnose

Students diagnose validation failures:

- Which annotator disagreements reveal ambiguous target definitions?
- Which false positives and false negatives matter for the economic question?
- Does the model perform differently by sector, region, job family, or year?
- Are probabilities calibrated well enough for thresholding or prevalence estimates?
- How much does a noisy constructed measure change the downstream association with applicant interest?

### Transfer

Students transfer the validation logic to a new domain:

- apply the source model to service-record text;
- measure vocabulary and domain shift;
- compare the source text score with dictionary, embedding, image proxy, and combined scores;
- report transport metrics and subgroup performance;
- write a benchmark redesign memo before using the measure in a new paper.

The purpose is to train the reflex that a constructed variable must be defended where it will be used.

## Methods Box

Students who want deeper technical detail should treat these as resources for validation design, not as a mandate to chase model complexity.

**Text and social-science NLP.** Gentzkow, Kelly, and Taddy provide the economics entry point for text-as-data measurement and validation [@gentzkowKellyTaddy2019]. Grimmer, Roberts, and Stewart give a broader social-science treatment of text measurement, supervision, validation, and interpretation [@grimmerRobertsStewart2022].

**Open-ended and LLM-assisted coding.** Haaland and coauthors are the primary economics anchor for open-ended responses and LLM-assisted coding [@haalandRothStantchevaWohlfart2024]. Technical text-model references such as BERT are useful background, but the lecture's main standard is auditability [@devlinChangLeeToutanova2019].

**Images, audio, and multimodal representations.** Jean and coauthors anchor image-based measurement with external validation [@jeanBurkeXieDavisLobellErmon2016]. ResNet, wav2vec 2.0, and CLIP are useful technical references for visual, speech, and multimodal representations [@heZhangRenSun2016; @baevskiZhouMohamedAuli2020; @radfordKimHallacyRameshGohAgarwal2021]. In applied economics, these tools still need benchmark design, subgroup diagnostics, and transport checks.

**Measurement error.** Bound, Brown, and Mathiowetz provide the general measurement-error framework for survey data [@bound2001measurementError]. Blattman and coauthors show how qualitative validation can reveal what the benchmark itself misses [@blattmanJamisonKoroknayPaliczRodriguesSheridan2016].

## Reading Ladder And References

```{include} assets/tables/13-reading-architecture.md
```

**First pass: validation logic.** Read Gentzkow, Kelly, and Taddy for the economics of text-as-data validation, then connect their principles to the benchmark and diagnostic tables in this lecture [@gentzkowKellyTaddy2019].

**Second pass: applied validation examples.** Read Hansen and coauthors for job-posting classification and validation, Jean and coauthors for image-derived measurement, and Gorodnichenko, Pham, and Talavera for audio-derived variables [@hansenRemoteWorkAcross2023; @jeanBurkeXieDavisLobellErmon2016; @gorodnichenkoPhamTalavera2023].

**Third pass: human review and open-ended responses.** Read Haaland and coauthors on open-ended responses and LLM-assisted coding, then identify which parts of their workflow are annotation design, model validation, and human review [@haalandRothStantchevaWohlfart2024].

**Fourth pass: measurement-error interpretation.** Read Blattman and coauthors with Bound, Brown, and Mathiowetz to see why validation failure changes the economics, not only the machine-learning metric [@blattmanJamisonKoroknayPaliczRodriguesSheridan2016; @bound2001measurementError].

## Exercises And Discussion Prompts

1. A classifier has high precision but low recall. Give one applied-economics use where that is acceptable and one where it is not.
2. Design an annotation protocol for coding whether open-ended survey responses mention job search discouragement. What is the unit, label definition, annotator pool, adjudication rule, and audit sample?
3. A remote-work classifier has lower recall for production and care jobs. How would this affect a descriptive study of remote-work access by occupation?
4. A satellite-image poverty proxy validates well in one country and poorly in another. Is the failure predictive, conceptual, or transportability-related?
5. An audio model predicts market reactions to central-bank press conferences. What checks would help separate vocal tone from speaker identity and recording conditions?
6. Suppose {math}`\widetilde X_i = X_i + \nu_i` and {math}`\nu_i` is correlated with treatment timing. How could this distort an event-study estimate?
7. Choose one embedding-based measure from a paper or proposed project. What nearest-neighbor audit, external benchmark, and subgroup check would you require?
8. What validation evidence would be needed before using a constructed variable as a treatment, outcome, instrument, or policy-targeting score?

## Reproducibility And Code Lab Note

The canonical lab lives at:

```text
labs/13-extraction-classification-embeddings-and-validation/
```

The lab uses Python and deterministic synthetic data. It includes:

- `lab.md` and `README.md`;
- a smoke test in `smoke.sh`;
- source scripts under `src/`;
- synthetic source data under `original/reduced/`;
- shifted transfer data under `transfer/data/`;
- reproduced validation outputs under `output/reproduced/`;
- transfer validation outputs under `output/transfer/`.

The lab is a bounded teaching path, not an official replication. It is designed to make benchmark construction, human-label reliability, confusion matrices, calibration, subgroup performance, downstream measurement error, and domain transfer concrete.

## Slide Companion Note

The Week 13 slide deck should not duplicate the chapter. It should give students a compact map of:

- validation as part of identification;
- annotation and benchmark design;
- precision, recall, F1, and calibration;
- subgroup performance, fairness, and drift;
- measurement error in downstream economics;
- validation examples from the anchor papers;
- the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is:

```text
slides/week13/13-extraction-classification-embeddings-and-validation.tex
```

## Bridge Forward

Lecture 14 moves from validation of constructed variables to LLM workflows for applied research. The standard carries forward: language models can lower the cost of extraction, coding, summarization, and retrieval, but they do not lower the evidentiary burden. Prompts, labels, human review, audit trails, privacy, and replication packages are part of the empirical design.
