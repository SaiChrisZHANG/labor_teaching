# Code Lab 14: LLM Workflows For Applied Research

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 14 - LLM workflows for applied research  
**Associated chapter:** `14-llm-workflows-for-applied-research.md`  
**Lab slug:** `14-llm-workflows-for-applied-research`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** validation metrics, text-as-data measurement, basic regressions, `pandas`  
**Core economic question:** When can an LLM-assisted workflow produce a credible research variable rather than only a plausible output?  
**Core design / estimator:** schema-bound extraction, prompt logs, benchmark validation, prompt sensitivity, subgroup diagnostics, audit flags, downstream slope comparison, transfer diagnostics  
**Source paper spine:** Korinek [@korinek2024genai; @korinek2025agents], Chen and coauthors [@chen2024mismatch], Choi [@choi2023llmlegal], Horton, Filippas, and Manning [@horton2023homosilicus], and Manning, Zhu, and Horton [@manning2024automated]

## Why This Lab Exists

Lecture 14 treats LLMs as research infrastructure. This lab makes that idea executable without depending on a live model API. Students work with synthetic labor-market documents and a deterministic teaching surrogate that mimics the shape of an LLM extraction workflow: prompt templates, schema-bound outputs, raw-output logs, benchmark labels, human-review flags, and transfer diagnostics.

The lab is not an official replication. It is a bounded teaching path for the workflow standards that a real LLM-assisted applied-economics project would need.

## Learning Objectives

By the end of this lab, students should be able to:

1. define the economic object behind an LLM-coded variable;
2. document a prompt, schema, model version, retrieval context, and post-processing rule;
3. compare LLM-style structured outputs with benchmark labels;
4. diagnose prompt sensitivity, subgroup instability, and unsupported outputs;
5. route ambiguous or influential cases to human review;
6. explain how a generated variable changes a downstream association;
7. transfer a workflow to a new domain without assuming portability.

## Required Local Structure

```text
labs/14-llm-workflows-for-applied-research/
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
      labor_mismatch_documents_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      workforce_case_notes_synthetic.csv
  src/
    llm_teaching_surrogate.py
    make_synthetic_data.py
    reproduce_llm_workflow.py
    transfer_llm_workflow.py
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
python src/reproduce_llm_workflow.py --input original/reduced/labor_mismatch_documents_synthetic.csv --outdir output/reproduced
python src/transfer_llm_workflow.py --source-input original/reduced/labor_mismatch_documents_synthetic.csv --input transfer/data/workforce_case_notes_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Structured LLM Workflow

### Objective

Construct a labor-market mismatch variable from synthetic document bundles using a documented prompt/schema workflow.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/prompt_log.csv`.
4. Open `output/reproduced/structured_outputs.csv`.
5. Open `output/reproduced/classification_metrics.csv`.
6. Open `output/reproduced/run_manifest.json`.

### Required Questions

- What is the target construct: skill mismatch, credential mismatch, schedule mismatch, placement readiness, or general employability?
- Which fields in the prompt log would be necessary in a replication package?
- Does the structured output respect the schema?
- How well does the rubric prompt match the benchmark labels?
- What is gained by keeping raw outputs as well as parsed fields?

### Minimum Output

- one paragraph defining the economic object;
- one paragraph explaining the prompt/schema/model/retrieval record;
- one table or paragraph summarizing benchmark performance;
- one sentence explaining why this is a teaching reproduction of workflow logic rather than an official replication.

## Part II. Diagnose Prompt, Benchmark, And Audit Risk

### Objective

Evaluate whether the LLM-coded mismatch variable is credible enough for applied economics.

### Student Tasks

1. Open `output/reproduced/prompt_sensitivity.csv`.
2. Open `output/reproduced/subgroup_stability.csv`.
3. Open `output/reproduced/hallucination_audit.csv`.
4. Open `output/reproduced/human_review_queue.csv`.
5. Open `output/reproduced/downstream_estimates.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Which records change labels across conservative, rubric, and expansive prompts?
- Which sector, region, occupation group, or document type has the weakest validation diagnostics?
- Which cases are unsupported, false positives, false negatives, or otherwise review-worthy?
- How much does the downstream slope change when the benchmark variable is replaced by the generated variable?
- What cases would you require a human reviewer to adjudicate before publication?

### Minimum Output

- one prompt-sensitivity paragraph;
- one subgroup-diagnostics paragraph;
- one audit-trail paragraph;
- one downstream-estimate paragraph;
- one final sentence stating whether the generated measure is ready for descriptive, causal, or structural use.

## Part III. Transfer The Workflow To Case Notes

### Objective

Transfer the source workflow to synthetic workforce-agency case notes with different vocabulary and document structure.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/vocabulary_shift.csv`.
3. Open `output/transfer/transport_metrics.csv`.
4. Open `output/transfer/transfer_prompt_sensitivity.csv`.
5. Open `output/transfer/benchmark_redesign_notes.csv`.
6. Write a short Transfer memo.

### Required Prompts

- Which transfer-domain terms are outside the source vocabulary?
- Does the adapted prompt improve performance, or does it change the construct?
- What new benchmark labels would be required before using the workflow in a real workforce-agency project?
- Which privacy constraints would affect prompt logging and replication?
- What synthetic examples or aggregate diagnostics should be released if raw case notes cannot be shared?

### Minimum Output

- one source-transfer vocabulary paragraph;
- one transport-performance paragraph;
- one benchmark-redesign paragraph;
- one privacy and replication paragraph.

## Deliverables Checklist

- [ ] run log;
- [ ] target-construct definition;
- [ ] prompt/schema/model/retrieval documentation paragraph;
- [ ] benchmark metric comparison;
- [ ] prompt-sensitivity memo;
- [ ] subgroup diagnostics memo;
- [ ] audit and human-review queue memo;
- [ ] downstream slope comparison;
- [ ] source-transfer vocabulary comparison;
- [ ] benchmark-redesign memo;
- [ ] final paragraph separating workflow usefulness from evidentiary sufficiency.

## Suggested Grading Rubric

- **Economic object:** The memo defines the variable before discussing model output.
- **Replication discipline:** The memo uses the prompt log, schema, raw outputs, and run manifest.
- **Validation discipline:** The memo reports benchmark, subgroup, sensitivity, and audit diagnostics.
- **Downstream interpretation:** The memo explains how generated-variable error changes the economics.
- **Transfer conservatism:** The memo does not assume source-domain validation travels to case notes.
