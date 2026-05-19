# Code Lab 12: Text As Data And Computational Measurement

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 12 - text as data and computational measurement  
**Associated chapter:** `12-text-as-data-and-computational-measurement.md`  
**Lab slug:** `12-text-as-data-and-computational-measurement`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** train/test splits, regularization, basic prediction metrics, `pandas`  
**Core economic question:** How can raw unstructured records become credible economic variables for applied research?  
**Core design / estimator:** dictionary scores, embedding-style similarity, supervised classification, subgroup diagnostics, measurement-error propagation, multimodal transfer  
**Source paper spine:** Gentzkow, Kelly, and Taddy [@gentzkowKellyTaddy2019], Hansen and coauthors [@hansenRemoteWorkAcross2023], Webb [@webb2020impactAI], Jean and coauthors [@jeanBurkeXieDavisLobellErmon2016], Gorodnichenko, Pham, and Talavera [@gorodnichenkoPhamTalavera2023], and Haaland and coauthors [@haalandRothStantchevaWohlfart2024]

## Why This Lab Exists

Lecture 12 treats unstructured data as a measurement environment. This lab makes the idea executable. Students first reproduce a bounded job-posting workflow that constructs a remote-work measure from text. They then diagnose whether the measure is credible enough for downstream economics. Finally, they transfer the same logic to a small multimodal setting where text is combined with image, audio, and video features.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on the measurement architecture rather than proprietary data access.

## Learning Objectives

By the end of this lab, students should be able to:

1. define the latent object behind a text-derived economic measure;
2. build dictionary, embedding-style, and supervised measures from the same raw text;
3. compare model performance with held-out diagnostics;
4. detect subgroup-specific measurement errors;
5. explain how measurement error changes downstream regressions;
6. transfer a source text measurement workflow to a new setting without assuming portability;
7. evaluate whether image, audio, and video features add credible signal or only more opacity.

## Required Local Structure

```text
labs/12-text-as-data-and-computational-measurement/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      job_postings_remote_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      multimodal_work_records_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_computational_measurement.py
    transfer_multimodal_measurement.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs three steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_computational_measurement.py --input original/reduced/job_postings_remote_synthetic.csv --outdir output/reproduced
python src/transfer_multimodal_measurement.py --source-input original/reduced/job_postings_remote_synthetic.csv --input transfer/data/multimodal_work_records_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Computational Measurement Workflow

### Objective

Construct remote-work measures from synthetic job-posting text.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/classification_metrics.csv`.
4. Open `output/reproduced/remote_measure_scores.csv`.
5. Open `output/reproduced/top_terms.csv`.
6. Compare dictionary, embedding-style, and supervised scores.

### Required Questions

- What is the latent object: explicit remote permission, remote-work feasibility, hybrid flexibility, or task portability?
- Which score is most transparent?
- Which score performs best on the test split?
- Which score would be easiest for readers to audit in a paper?
- What human-labeling evidence would be needed before using the score in a real labor-market study?

### Minimum Output

- one paragraph defining the measurement target;
- one table or paragraph comparing held-out diagnostics;
- one sentence explaining why this is a teaching reproduction of measurement logic rather than a replication of a published estimate.

## Part II. Diagnose Measurement Error

### Objective

Evaluate whether the constructed variable is credible enough for downstream applied research.

### Student Tasks

1. Open `output/reproduced/subgroup_measurement_error.csv`.
2. Open `output/reproduced/dictionary_sensitivity.csv`.
3. Open `output/reproduced/measurement_error_downstream.csv`.
4. Open `output/reproduced/leakage_audit.csv`.
5. Write a one-page Diagnose memo.

### Required Prompts

- Which sector, region, or job family has the largest measurement error?
- Does the broad dictionary improve recall at the cost of precision?
- Is the supervised model learning remote work or generic digital work?
- How much does using a noisy constructed measure change the downstream slope?
- Which features would leak future information into the measurement step?

### Minimum Output

- one subgroup-error paragraph;
- one dictionary-sensitivity paragraph;
- one downstream-measurement-error paragraph;
- one final sentence stating whether the measure is ready for a descriptive, causal, or structural exercise.

## Part III. Transfer To A Multimodal Setting

### Objective

Apply the same measurement logic to synthetic records with text, image, audio, and video features.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/source_vs_transfer_vocabulary.csv`.
3. Open `output/transfer/modality_ablation.csv`.
4. Open `output/transfer/transfer_multimodal_scores.csv`.
5. Open `output/transfer/modality_failure_modes.csv`.
6. Write a short Transfer memo.

### Required Prompts

- How different is the transfer text from the source job postings?
- Does the source text model remain useful?
- Which modality appears to add signal, and which one creates the largest interpretation risk?
- Does the multimodal index improve accuracy enough to justify a higher validation burden?
- What would a real paper need before using image, audio, or video features as economic variables?

### Minimum Output

- one source-transfer comparison paragraph;
- one modality-ablation paragraph;
- one validation-burden paragraph;
- one paragraph explaining what would change if the multimodal measure entered a causal design.

## Deliverables Checklist

- [ ] run log;
- [ ] latent-object definition;
- [ ] held-out metric comparison;
- [ ] dictionary versus supervised versus embedding paragraph;
- [ ] subgroup measurement-error memo;
- [ ] downstream measurement-error paragraph;
- [ ] leakage audit note;
- [ ] source-transfer vocabulary comparison;
- [ ] modality-ablation memo;
- [ ] final paragraph stating what the exercise measures and what it does not measure.

## Suggested Grading Rubric

- **Measurement clarity:** The memo defines the economic object before discussing algorithms.
- **Diagnostic discipline:** The memo uses test metrics, subgroup error, and sensitivity checks.
- **Downstream interpretation:** The memo explains how constructed-variable error affects later analysis.
- **Transfer conservatism:** The memo does not assume that a source model travels to a new modality or population.
- **Research orientation:** The memo connects computational extraction to applied economics rather than software technique alone.
