# Lecture 12. Text As Data And Computational Measurement

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain why unstructured data matter for applied economics research;
2. write a measurement model that maps a raw text, image, audio, video, or multimodal object into an economic variable;
3. distinguish dictionaries, supervised classification, embeddings, and multimodal features as extraction families;
4. diagnose modality-specific opportunities and pitfalls for text, images, audio, and video;
5. evaluate whether a computationally constructed measure is credible enough for descriptive, causal, or structural use;
6. design a Reproduce -> Diagnose -> Transfer lab for a job-posting or task-exposure measurement workflow.

## Opening Orientation

Lecture 12 begins the course block on text, computation, and LLM-based methods. The central question is: **how can unstructured data become credible economic measures?** This is not a generic NLP, computer-vision, speech, or video lecture. The object is applied-economics measurement: extracting information from raw documents, pixels, recordings, and multimodal traces so that researchers can study workers, firms, policies, places, tasks, beliefs, risks, institutions, and markets.

Many economically important variables are written, spoken, or seen before they are numeric. Job requirements appear in vacancy text. Firm expectations appear in earnings-call transcripts. Legal constraints appear in contracts and policy documents. Poverty, urban activity, and infrastructure appear in satellite and street-view imagery. Speech tone and delivery can carry economic information beyond transcripts. Video can preserve interaction, sequence, and nonverbal behavior. The econometric challenge is not to celebrate richer data. It is to say what latent economic object is being measured, why the raw modality contains signal about it, and how measurement error propagates into the downstream claim.

The paper spine makes that discipline concrete. Gentzkow, Kelly, and Taddy give the canonical economics overview of text as data [@gentzkowKellyTaddy2019]. Hansen and coauthors turn job-posting text into remote-work measures across jobs, companies, and space [@hansenRemoteWorkAcross2023]. Webb maps patent text to task descriptions to construct AI exposure [@webb2020impactAI]. Hassan and coauthors use earnings-call transcripts to measure firm exposure to epidemic disease risk [@hassanHollanderVanLentSchwedelerTahoun2020]. Jean and coauthors show how satellite imagery can proxy poverty when validated against survey ground truth [@jeanBurkeXieDavisLobellErmon2016]. Baragwanath and coauthors use satellite imagery to detect urban markets [@baragwanathGoldblattVogel2018]. Gorodnichenko, Pham, and Talavera treat voice itself as an economic information channel [@gorodnichenkoPhamTalavera2023]. Haaland and coauthors connect open-ended responses and LLM-assisted coding to economic measurement [@haalandRothStantchevaWohlfart2024].

## Core Points

:::{admonition} Core points
:class: important

- Unstructured data are useful when they recover latent economic objects that are otherwise missing, costly, delayed, or measured crudely.
- The main empirical question is not whether an algorithm is impressive. It is whether the constructed measure aligns with the research use.
- Text, images, audio, video, and multimodal records differ in data-generating process, labeling burden, portability, and privacy risk.
- Dictionaries, supervised classification, embeddings, and multimodal representations imply different economic interpretations.
- Measurement error from computational extraction can bias descriptive aggregates, treatment-effect estimates, exposure measures, welfare analysis, and structural primitives.
- A strong economics paper defends the mapping from raw signal to economic variable, validates it against independent evidence, and reports where the measure fails.
:::

## Bridge

Lectures 9 to 11 introduced prediction, regularization, high-dimensional controls, heterogeneity, policy learning, and external validity. Lecture 12 shifts the object. In Lecture 9, prediction often created or evaluated a score. In Lecture 10, prediction estimated nuisance functions. In Lecture 11, prediction and causal heterogeneity entered policy rules. Here the outcome, covariate, treatment, exposure, task, or institutional variable may itself be hidden inside unstructured data.

That shift makes measurement design central. A job posting is not a remote-work variable until the researcher defines what remote work means, extracts signal from the posting, validates the mapping, and explains how errors affect comparisons across jobs, firms, places, and time. A satellite image is not poverty until the researcher links pixels to household welfare and shows where the proxy travels. A voice recording is not economic sentiment until the researcher separates acoustic information from speaker identity, recording conditions, and institutional context.

```{include} assets/tables/12-theory-to-applied-bridge.md
```

## Field Core

### A. From Raw Object To Economic Variable

Let {math}`U_i` denote a raw unstructured input for unit {math}`i`: a document, job ad, contract, image, audio clip, video, scan, or multimodal record. Let {math}`M_i` denote the constructed economic measure, such as remote-work feasibility, AI task exposure, epidemic-risk exposure, policy strictness, neighborhood quality, poverty, sentiment, tone, or interaction quality. A generic measurement model is:

```{math}
:label: eq:em12-measurement-model
M_i = g(U_i; \theta) + \varepsilon_i,
```

where {math}`g(\cdot)` is the extraction rule or learned model, {math}`\theta` collects parameters, prompts, dictionaries, labels, embeddings, thresholds, or model weights, and {math}`\varepsilon_i` is measurement error relative to the intended economic object.

The notation forces three applied questions.

First, what is the latent object? A remote-work score, an AI-exposure score, and a firm-risk score are not generic text labels. They encode different counterfactual questions and different economic mechanisms. Second, what raw modality contains signal about that object? Vacancy text may reveal task requirements; satellite imagery may reveal built environment; speech audio may reveal tone not contained in transcripts. Third, how will errors matter downstream? A noisy measure used only for descriptive aggregates has one burden. A measure used as a treatment, outcome, running variable, instrument, structural primitive, or policy input has a heavier burden.

### B. Core Extraction Families

The starting taxonomy is not "which model is newest?" It is "what kind of mapping from {math}`U_i` to {math}`M_i` is defensible?"

```{include} assets/tables/12-extraction-workflow-and-algorithm-choices.md
```

**Dictionaries, rules, and regular expressions** work well when the concept is explicit and stable. A vacancy that says "remote work permitted" or a contract that contains a noncompete clause can often be measured with transparent rules. A simple dictionary-share measure is:

```{math}
:label: eq:em12-dictionary-share
D_i(S)
=
\frac{1}{N_i}
\sum_{t \in U_i}
\mathbf 1\{t \in S\},
```

where {math}`S` is a researcher-defined set of terms and {math}`N_i` is the number of tokens or units in the object. The strength is auditability. The risk is brittleness: synonyms, negation, boilerplate, changing language, and strategic wording can break the measure.

**Supervised classification** is useful when the target can be labeled. A researcher might ask humans to label postings as remote-feasible, documents as containing wage transparency, or images as containing visible infrastructure. A generic empirical risk minimization problem is:

```{math}
:label: eq:em12-erm
\widehat f
=
\arg\min_{f \in \mathcal F}
\frac{1}{n}\sum_{i=1}^{n} L(y_i, f(x_i))
+ \lambda P(f),
```

where {math}`y_i` is a labeled target, {math}`x_i` are features extracted from {math}`U_i`, {math}`L` is a loss function, and {math}`P(f)` penalizes complexity. The key economics question is whether the label definition matches the downstream research object. High test accuracy on the wrong target is still the wrong measure.

**Embeddings and similarity methods** are useful when exact words are too narrow and semantic distance matters. Let {math}`h(t)` map a token, phrase, image patch, audio segment, or document chunk into a vector. A document-level embedding can be written as:

```{math}
:label: eq:em12-embedding-aggregate
e_i
=
\frac{1}{N_i}
\sum_{t \in U_i} h(t),
\qquad
S_i(c)=
\frac{e_i'c}{\|e_i\|\|c\|},
```

where {math}`c` is a reference concept vector, such as a task description, technology description, disease-risk concept, or policy domain. Similarity can broaden measurement beyond exact keywords, but the resulting variable may measure semantic proximity rather than causal exposure, task substitutability, or institutional salience.

**Multimodal features** combine text, images, audio, and video. A firm-call measure might combine transcript topics with vocal tone. A neighborhood measure might combine street-view images with local text reviews and satellite data. A workplace interaction measure might combine transcripts, audio, and video. The practical rule is to use the least complex modality that credibly measures the object, then add modalities only when they contribute economically relevant signal that can be validated.

### C. Modality-Specific Opportunities And Pitfalls

```{include} assets/tables/12-modality-to-economic-object-map.md
```

**Text and documents.** Text is the dominant modality in economics because institutions write things down. Job ads, resumes, firm filings, earnings calls, policy text, contracts, court documents, news, open-ended survey responses, and administrative case notes can all reveal tasks, rules, risks, beliefs, narratives, and constraints. The opportunity is scale plus institutional richness. The pitfalls are semantic drift, boilerplate, strategic disclosure, translation, legal drafting conventions, changing platforms, and labels embedded in later metadata.

Hansen and coauthors show the strength of job-posting text for measuring remote work [@hansenRemoteWorkAcross2023]. Webb shows how semantic mapping between patents and task descriptions defines an exposure measure [@webb2020impactAI]. Hassan and coauthors show how firm-call text can identify exposure to epidemic risks before standard outcomes move [@hassanHollanderVanLentSchwedelerTahoun2020]. Haaland and coauthors emphasize that open-ended responses can recover motives, beliefs, and narratives, but only with explicit annotation and validation discipline [@haalandRothStantchevaWohlfart2024].

**Images, satellite, street-view, and scans.** Images are useful when the economic object is spatial, physical, infrastructural, environmental, or visual. Satellite imagery can proxy poverty or market activity in places with sparse surveys. Street-view images can measure built environment, roads, storefronts, or neighborhood amenities. Scans and forms can turn paper archives into structured data. The opportunity is broad coverage and fine spatial granularity. The pitfalls are domain mismatch, clouds and image quality, changing sensors, seasonal differences, omitted context, proxy instability, and the risk that visually salient features are not welfare-relevant.

Jean and coauthors validate satellite-image predictions against survey ground truth, making the measurement target explicit [@jeanBurkeXieDavisLobellErmon2016]. Baragwanath and coauthors use remotely sensed imagery to detect urban markets, which illustrates how image-derived measures can define economic geography [@baragwanathGoldblattVogel2018].

**Audio and speech.** Audio matters when tone, pace, pitch, pauses, fluency, stress, accent, or emotional delivery carry information beyond transcript content. It can appear in central-bank communication, interviews, call centers, workplace recordings, and open-ended survey responses. The opportunity is that speech preserves information lost in text. The pitfalls are especially serious: audio can encode identity markers, recording quality, room acoustics, interviewer behavior, and social context. A model that appears to predict sentiment or confidence may partly measure gender, race, class, language background, or microphone quality.

Gorodnichenko, Pham, and Talavera show that voice can carry market-relevant information in monetary-policy communication [@gorodnichenkoPhamTalavera2023]. The lesson for applied economics is not that every recording should become an audio model. It is that if the voice itself is the object, the validation burden must separate substantive signal from identity and recording artifacts.

**Video and multimodal records.** Video is still a frontier modality in economics, but it matters when interaction, sequencing, attention, gesture, or joint audio-visual content are central. It may be useful for classroom interactions, workplace safety, interviews, meetings, courtroom behavior, service encounters, or task execution. The pitfalls are high labeling cost, privacy, consent, storage, model opacity, and unclear economic mapping. Video can be seductive because it contains many signals. That is exactly why the economic object must be sharply defined before extraction begins.

### D. Measurement Error In Downstream Analysis

Suppose the intended latent measure is {math}`M_i^*`, but the researcher observes the constructed measure:

```{math}
:label: eq:em12-measurement-error
\widehat M_i = M_i^* + \eta_i.
```

If the downstream descriptive or causal equation is:

```{math}
:label: eq:em12-downstream-model
Y_i = \alpha + \beta M_i^* + \nu_i,
```

then replacing {math}`M_i^*` with {math}`\widehat M_i` changes the estimand. Under classical measurement error with {math}`\eta_i` uncorrelated with {math}`M_i^*` and {math}`\nu_i`, a bivariate regression is attenuated:

```{math}
:label: eq:em12-attenuation
\operatorname{plim}\widehat\beta_{\widehat M}
=
\beta
\cdot
\frac{\operatorname{Var}(M_i^*)}
{\operatorname{Var}(M_i^*)+\operatorname{Var}(\eta_i)}.
```

In many unstructured-data settings, errors are not classical. They may vary by firm, region, occupation, language, class, race, gender, platform, image quality, or recording setting. If {math}`\eta_i` is correlated with treatment timing, outcomes, policy exposure, sample inclusion, or group membership, downstream estimates can be biased in unknown directions. A remote-work classifier that misses blue-collar hybrid arrangements will distort comparisons across occupations. A satellite poverty proxy trained in one country may mismeasure welfare in another. An audio model may confuse uncertainty with speaker identity or recording quality.

This is why validation is part of identification. If the constructed measure is central to the identifying variation, then mismeasurement can change what variation the paper actually uses.

### E. What A Good Applied Paper Does

A strong applied-economics paper using unstructured data usually does six things.

1. It defines the latent economic object before choosing the algorithm.
2. It explains why the raw modality contains signal about that object.
3. It documents the corpus, sampling, preprocessing, labeling, training, thresholds, and aggregation.
4. It benchmarks the measure against human labels, independent data, known aggregates, or theory-relevant validation checks.
5. It reports subgroup, time, geography, platform, modality, and domain-shift diagnostics.
6. It explains how measurement error affects descriptive, causal, structural, or policy interpretation.

The computational step should be legible enough that a reader can ask: if this variable is wrong, where is it wrong, and what would that do to the economics result?

## Research Lab

The Week 12 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. The primary anchor is a bounded teaching analogue of job-posting remote-work measurement, inspired by Hansen and coauthors [@hansenRemoteWorkAcross2023]. The lab is not an official replication because the course does not ship proprietary vacancy data or paper-specific labels. Instead, it creates deterministic synthetic data that make the measurement logic transparent.

### Reproduce

Students build a remote-work measure from synthetic job-posting text. They compare a dictionary share, an embedding-style similarity score, and a supervised classifier. The point is to reproduce the empirical architecture:

- define the target label;
- split data into train, validation, and test samples;
- construct transparent dictionary and similarity baselines;
- estimate a supervised score;
- aggregate raw text into an economic variable;
- report classification and calibration diagnostics.

### Diagnose

Students then ask whether the measure is usable for applied work:

- What is the latent object: remote-work feasibility, explicit remote permission, hybrid flexibility, or task portability?
- Which terms drive the dictionary measure?
- Does the supervised model fail differently by sector, region, or occupation?
- Does the embedding-style similarity score measure remote work or generic digital work?
- How does measurement error affect a downstream association between remote feasibility and applicant interest?
- Which features would leak future information into the measurement process?

### Transfer

Students transfer the same measurement logic to a small multimodal setting. The transfer file contains synthetic records with policy text, an image-based infrastructure score, an audio clarity score, and a video interaction score. The exercise asks whether the source text model should be reused, whether multimodal features add economically meaningful signal, and what would need human validation before any real paper used the measure.

The purpose is not to claim that text, images, audio, and video are interchangeable. It is to make students re-justify the mapping from raw signal to economic variable whenever the modality or population changes.

## Methods Box

Students who want to go deeper technically should treat the following as resources, not as a mandate to turn the lecture into an engineering class.

**Text and social-science NLP.** Gentzkow, Kelly, and Taddy provide the economics entry point, while Grimmer, Roberts, and Stewart give a broader social-science framework for text-as-data measurement [@gentzkowKellyTaddy2019; @grimmerRobertsStewart2022]. Transformer-based language models such as BERT are useful technical background for modern text representations [@devlinChangLeeToutanova2019].

**Images and remote sensing.** Jean and coauthors are the applied-economics anchor for satellite imagery and poverty measurement [@jeanBurkeXieDavisLobellErmon2016]. ResNet is a standard technical reference for deep visual representations [@heZhangRenSun2016].

**Audio and speech.** Gorodnichenko, Pham, and Talavera are the economic application anchor for voice as information [@gorodnichenkoPhamTalavera2023]. wav2vec 2.0 is a useful technical reference for self-supervised speech representations [@baevskiZhouMohamedAuli2020].

**Multimodal representation.** CLIP is a useful reference for joint image-text representation learning [@radfordKimHallacyRameshGohAgarwal2021]. In applied economics, the central question remains whether the learned representation measures the object needed for the paper.

## Reading Ladder And References

```{include} assets/tables/12-reading-architecture.md
```

**First pass: measurement logic.** Read Gentzkow, Kelly, and Taddy for the basic text-as-data architecture, then map each element to the measurement equation in this lecture [@gentzkowKellyTaddy2019].

**Second pass: labor and firm applications.** Read Hansen and coauthors on remote work, Webb on AI exposure, and Hassan and coauthors on epidemic-risk exposure [@hansenRemoteWorkAcross2023; @webb2020impactAI; @hassanHollanderVanLentSchwedelerTahoun2020].

**Third pass: modality expansion.** Read Jean and coauthors for satellite imagery, Baragwanath and coauthors for urban-market imagery, and Gorodnichenko, Pham, and Talavera for voice as economic information [@jeanBurkeXieDavisLobellErmon2016; @baragwanathGoldblattVogel2018; @gorodnichenkoPhamTalavera2023].

**Fourth pass: open-ended and LLM-assisted measurement.** Read Haaland and coauthors for open-ended responses and LLM-assisted coding, then connect their validation logic to Lecture 13 [@haalandRothStantchevaWohlfart2024].

## Exercises And Discussion Prompts

1. Give one economics setting where a dictionary is better than a supervised classifier, and one where it is worse. What feature of the latent object drives the difference?
2. A job-posting classifier has high test accuracy but lower recall for service-sector vacancies. How would that affect a study of remote-work access by occupation?
3. Compare Hansen and coauthors with Webb. How does the constructed variable differ, and how does that change the validation burden?
4. Suppose satellite imagery predicts poverty well in one country but fails in another. Is this a prediction problem, a measurement problem, or an external-validity problem?
5. In an audio study, which validation checks would help separate vocal tone from speaker identity and recording quality?
6. Design a small human-labeling protocol for open-ended survey responses. What labels, annotators, agreement checks, and audit samples would you report?
7. If a constructed variable is later used as a treatment, outcome, running variable, or instrument, which measurement failures become most serious?

## Reproducibility And Code Lab Note

The canonical lab lives at:

```text
labs/12-text-as-data-and-computational-measurement/
```

The lab uses Python and deterministic synthetic data. It includes:

- `lab.md` and `README.md`;
- a smoke test in `smoke.sh`;
- source scripts under `src/`;
- reduced synthetic source data under `original/reduced/`;
- transfer data under `transfer/data/`;
- reproduced outputs under `output/reproduced/`;
- transfer outputs under `output/transfer/`.

The lab should be cited as a teaching path, not an official replication. It is designed to make the measurement model executable with a small sample, transparent dictionaries, simple embeddings, supervised classification, subgroup diagnostics, and a multimodal transfer exercise.

## Slide Companion Note

The Week 12 slide deck should not duplicate the chapter. It should give students the conceptual map:

- why unstructured data matter for economics;
- the measurement model from raw object to economic variable;
- extraction families and what they imply;
- text, image, audio, video, and multimodal examples;
- modality-specific failure modes;
- the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is:

```text
slides/week12/12-text-as-data-and-computational-measurement.tex
```

## Bridge Forward

Lecture 13 turns from construction to validation. Once a variable has been extracted from text, images, audio, video, or multimodal data, the central question becomes: what exactly does it measure, where does it fail, and how do those failures affect descriptive, causal, structural, or policy claims?
