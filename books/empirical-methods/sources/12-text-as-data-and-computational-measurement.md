---
title: Text as Data and Computational Measurement
bibliography:
  - bibliography/12-text-as-data-and-computational-measurement.bib
---

# Text as Data and Computational Measurement

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish **prediction**, **classification**, and **measurement construction** when using unstructured data in economics;
2. explain how text, images, audio, and video enter applied research as **proxies for latent economic objects**;
3. identify when dictionaries, supervised learning, embeddings, or multimodal methods are most appropriate;
4. articulate the main implementation caveats: target definition, labeling, sample drift, domain mismatch, and measurement error propagation;
5. translate an unstructured-data idea into a credible **applied economics research design**.

## Opening Orientation

Many economic variables are **written, spoken, or seen before they are numeric**. Job requirements appear in vacancy text. Firm expectations appear in earnings-call transcripts. Neighborhood quality appears in images. Workplace climate can appear in speech or open-ended responses. The econometric problem is not just “run NLP.” It is: **what latent economic object are we trying to measure, from what raw signal, and with what validation burden?**

This lecture treats unstructured data as a **measurement environment**. The aim is not to replace economic design with machine learning, but to show how computational extraction can create variables that feed into descriptive, causal, and structural work.

::: {.admonition title="Core points"}
- Unstructured data are useful when they recover **latent economic objects** that are otherwise missing or measured crudely.
- The key empirical question is not whether an algorithm predicts well in isolation, but whether the resulting measure aligns with the **research use**.
- Text, images, audio, and video differ in data-generating process, labeling burden, and portability.
- Measurement error from computational extraction can bias downstream descriptive, causal, and welfare analysis.
- A strong paper defends not only the algorithm, but the mapping from raw signal to **economic interpretation**.
:::

## Bridge

Lectures 9–11 introduced prediction, regularization, and causal ML. Those tools were used mainly to predict outcomes, residualize nuisance functions, and organize heterogeneity. Lecture 12 shifts the question: **what if the outcome or covariate of interest is itself hidden inside unstructured data?** This is where prediction becomes measurement.

## Field Core

### 1. From raw objects to economic variables

Let `U_i` denote a raw unstructured object for unit `i`: a document, image, audio clip, or video. The researcher wants to construct an economic measure `M_i`, such as remote-work feasibility, task exposure, sentiment, legal stringency, neighborhood quality, or wage transparency.

```{math}
:label: eq:measurement-model
M_i = g(U_i; \theta) + \varepsilon_i
```

Equation [](#eq:measurement-model) makes two things explicit. First, measurement is a **modeling choice**: the researcher must specify the function `g`. Second, the resulting measure is not observed without error. That means downstream estimates inherit whatever bias, noise, and drift are embedded in the measurement process.

The central design question is: **what is the latent economic object, and why should the chosen transformation of raw data recover it?**

### 2. Core extraction families

A useful taxonomy is:

1. **Rules / dictionaries / regular expressions**  
   Good when the concept is tightly defined and the language is stable. Examples: whether a vacancy explicitly mentions salary, whether a contract contains a noncompete clause, whether a filing mentions epidemic risk.

2. **Supervised classification**  
   Good when the target can be labeled and the researcher cares about a relatively stable classification problem. Examples: remote-work feasibility, occupational task categories, document type, sentiment direction.

3. **Embeddings / similarity methods**  
   Good when exact keywords are too narrow and semantic similarity matters. Examples: comparing job text to task descriptions, measuring alignment between documents, clustering occupations or firms by text.

4. **Multimodal / image / audio / video features**  
   Good when the relevant information is visual, vocal, or jointly encoded across modalities. Examples: satellite imagery for poverty or urban activity, speech tone as an informational object, video or multimodal traces of interactions.

A generic supervised-learning construction solves:

```{math}
:label: eq:erm
\hat f = \arg\min_f \frac{1}{n}\sum_{i=1}^n L(y_i, f(x_i)) + \lambda P(f),
```

where `y_i` is a labeled target, `x_i` are features extracted from `U_i`, `L` is the loss function, and `P(f)` is a complexity penalty.

The economics question is never only the choice of learner. It is whether the target `y_i`, features `x_i`, and loss function align with the **economic use case**.

### 3. Modality-specific opportunities and pitfalls

#### Text and documents

Text remains the dominant modality in economics because institutions write down many things that matter:
- job ads,
- earnings calls,
- firm filings,
- policy text,
- contracts,
- court documents,
- open-ended surveys,
- news.

The strength of text is scale and institutional richness. The weakness is that meaning is context-dependent, strategic, and often unstable across place/time.

**Examples**
- Gentzkow, Kelly, and Taddy show how text becomes usable economic data through tokenization, representation, and supervised/unsupervised methods.
- Hansen et al. classify job postings to measure remote-work feasibility.
- Webb constructs task exposure to AI by matching patents and task descriptions.
- Hassan et al. use earnings-call text to measure firm-level exposure to epidemic diseases.

#### Images and satellite / street-view data

Images are useful when the object of interest is spatial, physical, or infrastructural:
- poverty,
- urban form,
- environmental exposure,
- neighborhood amenities,
- built environment,
- land use.

The strength of images is coverage and granularity. The weakness is that the link between pixels and economic concepts is often indirect and context-sensitive.

**Examples**
- Jean et al. use satellite imagery and machine learning to predict poverty.
- Baragwanath-style urban-market papers use remotely sensed imagery to define economic markets.

#### Audio and speech

Audio becomes economically meaningful when tone, clarity, emotion, fluency, or accent carry information:
- central-bank communication,
- open-ended survey responses,
- worker interviews,
- call-center interactions,
- speech patterns in labor markets.

The strength of audio is that it contains information beyond text. The weakness is that vocal features are highly context-dependent and can capture both substantive information and identity markers.

**Examples**
- Gorodnichenko, Pham, and Talavera show that vocal tone itself carries information in monetary-policy communication.
- Haaland et al. discuss speech recordings as part of the broader open-ended response toolkit.

#### Video and multimodal data

Video is still a frontier modality in economics, but it matters when interaction, sequencing, gesture, or joint audio-visual content are central. The promise is large; the validation burden is larger still.

A practical principle for applied work is:
- **use the least complex modality that credibly measures the object**,
- and only move to multimodal models when single-modality approaches are clearly insufficient.

### 4. Aggregation, embeddings, and variable construction

Many useful economic variables are document-level aggregates of smaller objects. For example, let token embedding `h(t)` map a token or phrase to a vector. A document-level embedding can be written as

```{math}
:label: eq:embedding-aggregate
e_i = \frac{1}{N_i}\sum_{t \in U_i} h(t),
```

where `N_i` is the number of tokens or units in object `U_i`. Similarity-based measures often compare `e_i` to another vector representation of a concept, occupation, task, or reference document.

This is powerful, but it raises a design question: is the researcher measuring **semantic similarity**, **topic prevalence**, **classification membership**, or **predictive risk**? Different methods imply different interpretations.

### 5. What a good applied paper does

A strong economics paper using unstructured data usually does five things:

1. defines the latent object clearly;
2. explains why the chosen raw modality contains signal about that object;
3. documents the labeling / training / preprocessing choices;
4. validates the measure against independent or human benchmarks;
5. shows how measurement error affects downstream interpretation.

This is why the most useful papers are not simply “NLP papers in economics.” They are papers where the computational step is tightly embedded in an economic argument.

## Research Lab

### Primary anchor paper

**Hansen, Lambert, Bloom, Davis, Sadun, and Taska**  
*Remote Work across Jobs, Companies, and Space*

This is a strong main anchor because it turns text from job postings into a new economic measure, links the construction to labor-market questions, and validates the classification with human-labeled data and cross-context evidence.

### Challenge / extension anchors

- **Webb**  
  *The Impact of Artificial Intelligence on the Labor Market*  
  A measurement paper that maps patents to task text, showing how extraction choices define the meaning of “technology exposure.”

- **Jean et al.**  
  *Combining Satellite Imagery and Machine Learning to Predict Poverty*  
  A good modality contrast: the same measurement logic extends to images, but the validation problem changes.

- **Gorodnichenko, Pham, and Talavera**  
  *The Voice of Monetary Policy*  
  A contrast case where audio features themselves become the measured object.

### Reproduce

Reproduce a bounded pedagogical version of a text-classification workflow:
- define a labeled target,
- split data into train/validation/test,
- build a simple classifier,
- report prediction and classification diagnostics,
- construct the economic measure for a small sample.

### Diagnose

Ask:
- What is the latent object?
- How sensitive is the constructed variable to labeling choices?
- Is the algorithm learning the intended economic concept or a shortcut?
- What are the likely sources of domain shift?

### Transfer

Move the same logic to a different unstructured setting:
- job ads → policy text
- job ads → open-ended survey responses
- text → image-based proxy
- text → audio-based proxy

The point is not that all modalities are interchangeable. The point is that the researcher must re-justify the mapping from raw signal to economic variable each time.

## Methods Box

Students who want to go deeper technically should look at:

- **Text / NLP**: Gentzkow–Kelly–Taddy; general NLP resources such as Jurafsky–Martin and Devlin et al. on BERT
- **Images / vision**: Jean et al.; computer-vision resources such as He et al. on ResNet
- **Audio / speech**: Gorodnichenko–Pham–Talavera; audio-representation resources such as Baevski et al. on wav2vec 2.0
- **Multimodal models**: resources such as Radford et al. on CLIP

For this course, the engineering details are secondary. What matters is understanding:
- what the model is extracting,
- why that matters economically,
- and how the resulting measure is validated.

## Reading Ladder And References

### Core readings
1. Gentzkow, Kelly, and Taddy — *Text as Data*
2. Hansen et al. — *Remote Work across Jobs, Companies, and Space*
3. Webb — *The Impact of Artificial Intelligence on the Labor Market*

### Applications and modality expansions
4. Hassan et al. — *Firm-Level Exposure to Epidemic Diseases: COVID-19, SARS, and H1N1*
5. Jean et al. — *Combining Satellite Imagery and Machine Learning to Predict Poverty*
6. Gorodnichenko, Pham, and Talavera — *The Voice of Monetary Policy*
7. Haaland et al. — *Understanding Economic Behavior Using Open-ended Survey Responses and Large Language Models*

### Optional methods resources
8. Devlin et al. — *BERT*
9. He et al. — *Deep Residual Learning for Image Recognition*
10. Baevski et al. — *wav2vec 2.0*
11. Radford et al. — *Learning Transferable Visual Models From Natural Language Supervision*

## Exercises And Discussion Prompts

1. Give one example where a dictionary is better than a classifier, and one where it is worse.
2. Why is a high out-of-sample prediction score not enough to justify an economic measure?
3. Compare Hansen et al. and Webb. How does the measurement target differ?
4. What kinds of measurement error are most likely when moving from text to image or audio data?
5. Suppose your constructed variable is used as a treatment or running variable downstream. Which validation problems become especially serious?

## Reproducibility And Code Lab Note

A good Week 12 lab should be lightweight and reproducible:
- small labeled sample,
- transparent preprocessing,
- explicit train/validation/test split,
- one simple baseline model,
- one more flexible model,
- reproducible output tables and diagnostics.

Where full official replication data are not available locally, a bounded synthetic or reduced path is perfectly acceptable as long as it illustrates the measurement logic faithfully.

## Slide Companion Note

The slide deck should emphasize:
- the measurement model,
- modality differences,
- paper-based examples,
- and the Reproduce → Diagnose → Transfer workflow.

This lecture works best when students see concrete applications rather than a catalog of algorithms.

## Bridge Forward

Lecture 13 turns from construction to **validation**. Once a variable has been extracted from text, images, audio, or video, the central question becomes: what exactly does it measure, where does it fail, and how do those failures affect causal or descriptive claims?
