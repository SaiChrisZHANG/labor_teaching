---
title: Extraction, Classification, Embeddings, and Validation
bibliography:
  - bibliography/13-extraction-classification-embeddings-and-validation.bib
---

# Extraction, Classification, Embeddings, and Validation

## Learning Objectives

By the end of this lecture, students should be able to:

1. design a validation strategy for text-, image-, audio-, or video-derived variables;
2. distinguish precision, recall, calibration, inter-rater reliability, subgroup performance, and transportability;
3. explain how measurement error in constructed variables changes downstream descriptive and causal interpretation;
4. identify when human review, benchmark sets, and re-labeling are essential;
5. defend an unstructured-data measure in the style expected in applied economics research.

## Opening Orientation

Lecture 12 asked how raw unstructured objects become economic variables. Lecture 13 asks a harder question: **how do we know what those variables actually measure?** In applied work, validation is not a cosmetic appendix. It is part of identification. If the algorithm systematically mismeasures a variable for certain places, groups, or periods, then the economic estimate downstream may be biased or may answer a different question than the one the researcher claims.

This lecture therefore treats validation as an empirical design problem. The issue is not just predictive accuracy. It is whether the constructed variable is sufficiently stable, interpretable, and portable for the research use.

::: {.admonition title="Core points"}
- Validation is part of identification when unstructured data are used to build economic variables.
- High average accuracy is not enough; subgroup performance, calibration, and drift matter.
- Annotation protocols and benchmark design shape what the algorithm learns.
- Human review and external validation are often necessary, not optional.
- If measurement error is correlated with treatment, subgroup, place, or time, downstream economic interpretation can change sharply.
:::

## Bridge

Lecture 12 treated extraction and variable construction as the main task. Lecture 13 asks how to validate those variables before they enter regressions, treatment-effect estimation, or policy evaluation. The core lesson is simple: **a biased measurement process can generate a biased economic result, even when the econometric design downstream is impeccable.**

## Field Core

### 1. What needs to be validated?

Validation has at least five layers:

1. **Construct validity**: does the variable represent the intended economic object?
2. **Prediction/classification validity**: how well does the algorithm recover the labeled target?
3. **Subgroup validity**: does performance differ systematically across populations or contexts?
4. **Temporal/domain validity**: does the model travel across time, geography, platforms, or institutions?
5. **Downstream validity**: how do remaining errors affect descriptive, causal, or welfare inference?

A paper can do well on one layer and poorly on another. Applied researchers need to know which layer matters for their claim.

### 2. Basic validation metrics

Suppose a classifier predicts a binary label. Then

```{math}
:label: eq:precision
\text{Precision} = \frac{TP}{TP + FP}
```

```{math}
:label: eq:recall
\text{Recall} = \frac{TP}{TP + FN}
```

```{math}
:label: eq:f1
F_1 = 2 \cdot \frac{\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}}
```

These metrics answer different questions:
- precision asks how many predicted positives are truly positive;
- recall asks how many true positives were recovered;
- `F_1` summarizes their tradeoff.

But accuracy metrics alone are rarely enough. If the output is probabilistic, calibration matters:

```{math}
:label: eq:calibration
E[Y \mid \hat p = p] = p.
```

A poorly calibrated model can rank observations well and still be unusable for policy or measurement thresholds.

### 3. Human labels, annotation protocols, and inter-rater reliability

When the latent variable is not directly observed, benchmark labels are themselves constructed. That means researchers must specify:
- who labels,
- what instructions they receive,
- how disagreements are handled,
- whether expert and nonexpert labels differ,
- and whether the benchmark measures the economic construct or just a proxy for it.

A common reliability statistic is Cohen’s kappa, which adjusts for chance agreement:

```{math}
:label: eq:kappa
\kappa = \frac{p_o - p_e}{1 - p_e},
```

where `p_o` is observed agreement and `p_e` is expected agreement under chance.

A high kappa is useful, but not sufficient. Labelers can agree on the wrong construct if the labeling protocol is poorly aligned with the economic question.

### 4. Measurement error and downstream economics

Suppose the researcher uses a constructed variable `\tilde X_i` in a downstream model:

```{math}
:label: eq:measurement-error
\tilde X_i = X_i + \nu_i.
```

If `\nu_i` is classical and independent, attenuation may be the main problem. In practice, unstructured-data errors are often **nonclassical**:
- correlated with subgroup identity,
- correlated with treatment,
- correlated with location or time,
- or shaped by institutional language.

That means the bias can change sign, not just magnitude.

In a binary classification setting, differential false positives or false negatives can also create spurious subgroup gaps, fake event-study dynamics, or misleading treatment heterogeneity.

### 5. Embeddings, similarity, and external validation

Embedding-based measures are attractive because they generalize beyond exact keywords. But they are also harder to interpret. Validation should therefore include:
- human inspection of nearest neighbors,
- comparisons to independent benchmark measures,
- subgroup performance,
- sensitivity to prompt/template/representation choices,
- stability across corpora or time.

A measure built from embeddings is credible when the researcher shows not only that it “works,” but **what variation it is actually picking up**.

### 6. Drift, transportability, and model decay

Unstructured measures can fail because the environment changes:
- new vocabulary,
- different visual environments,
- changes in recording quality,
- new platform or institutional rules,
- new composition of workers/firms/locations.

This is model drift. A variable that was valid in one context may become misleading in another.

A strong applied paper therefore asks:
- does the measure transport?
- if not, what exactly breaks?
- does re-labeling or re-calibration fix it?
- is the target itself stable over time?

### 7. How applied papers defend their choices

A strong economics paper using unstructured data typically does four things:

1. **Defines the benchmark carefully**  
2. **Shows performance metrics that match the research use**  
3. **Tests subgroup/domain robustness**  
4. **Discusses downstream economic implications of residual error**  

This is where many papers are weakest. They report one headline accuracy number and move on. The better papers treat measurement as a design problem with failure modes.

## Research Lab

### Primary anchor papers

**Hansen, Lambert, Bloom, Davis, Sadun, and Taska**  
*Remote Work across Jobs, Companies, and Space*

A strong primary anchor because it combines human labels, model construction, and economic interpretation of the resulting measure.

**Jean et al.**  
*Combining Satellite Imagery and Machine Learning to Predict Poverty*

A good image-based contrast where the benchmark and transfer problem differ from text classification.

### Additional validation anchors

- **Haaland et al.** on open-ended responses and LLM-supported analysis
- **Gorodnichenko, Pham, and Talavera** on audio-derived measures
- **Blattman et al.** on qualitative validation and measurement error

### Reproduce

Reproduce a bounded validation workflow:
- labeled data split,
- baseline and flexible classifier,
- confusion matrix,
- precision / recall / F1,
- calibration or threshold comparison,
- one subgroup breakdown.

### Diagnose

Ask:
- what does the benchmark really measure?
- are mistakes systematic across subgroups or time?
- does the algorithm drift in a new domain?
- how would the downstream economic regression change if the error were differential?

### Transfer

Transfer the validation logic to a second modality or domain:
- text → image
- text → open-ended survey responses
- image → new geography
- audio → new institution/time period

The purpose is to teach students that extraction is only half the empirical design. The other half is defending the measure.

## Methods Box

Students who want deeper technical detail should look at:
- **text / NLP**: Gentzkow–Kelly–Taddy, plus standard NLP resources
- **open-ended / LLM-assisted analysis**: Haaland et al.
- **qualitative validation**: Blattman et al.
- **image validation**: Jean et al. and satellite-imagery measurement reviews
- **audio**: Gorodnichenko–Pham–Talavera and related speech-feature work
- **measurement error**: Bound on survey/error logic and related work on nonclassical measurement error

The central idea is not to memorize metrics, but to align the metric, benchmark, and economic use.

## Reading Ladder And References

### Core readings
1. Gentzkow, Kelly, and Taddy — *Text as Data*
2. Hansen et al. — *Remote Work across Jobs, Companies, and Space*
3. Haaland et al. — *Understanding Economic Behavior Using Open-ended Survey Responses and Large Language Models*

### Validation and measurement-error readings
4. Blattman et al. — *Measuring the Measurement Error*
5. Bound — survey and measurement-error logic
6. Jean et al. — image-based validation against survey outcomes
7. Gorodnichenko, Pham, and Talavera — audio-derived validation example

### Optional methods resources
8. Devlin et al. — BERT
9. He et al. — ResNet
10. Baevski et al. — wav2vec 2.0
11. Radford et al. — CLIP

## Exercises And Discussion Prompts

1. A classifier has high precision but low recall. When is that acceptable in applied economics work?
2. Why might subgroup-specific validation matter more than average validation?
3. What is the difference between inter-rater reliability and construct validity?
4. Suppose a text-derived variable is measured with differential error across treated and control units. How could this distort a DID estimate?
5. What kinds of transport problems are most likely for image, audio, and text measures?

## Reproducibility And Code Lab Note

A good Lecture 13 lab should generate:
- confusion matrix,
- calibration plot,
- subgroup metrics,
- sensitivity to threshold choice,
- and a transfer/domain-shift comparison.

Where full official data are unavailable locally, a bounded synthetic or reduced path is acceptable as long as it illustrates the validation logic faithfully.

## Slide Companion Note

The slide deck should emphasize:
- validation as identification,
- the confusion-matrix / calibration logic,
- benchmark and annotation design,
- subgroup performance,
- and the downstream economics of measurement error.

This lecture works best when students see why “good enough ML performance” is not the same thing as a defensible economic measure.

## Bridge Forward

This concludes Block 4. Across Lectures 12 and 13, the course moves from **constructing** variables out of unstructured data to **defending** them. The larger lesson for applied economics is that computational tools are valuable when they sharpen measurement and design—not when they substitute for them.
