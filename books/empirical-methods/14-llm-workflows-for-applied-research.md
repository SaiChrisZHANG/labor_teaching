# Lecture 14. LLM Workflows For Applied Research

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish LLMs as research assistants, measurement devices, synthetic coders, simulated subjects, and simulation engines;
2. formalize LLM-assisted extraction, coding, response generation, and simulation workflows as designed research instruments;
3. explain when LLM outputs can become economic variables and when they should remain exploratory workflow support;
4. design prompt logs, retrieval records, benchmark sets, audit trails, and human-review protocols;
5. diagnose hallucination risk, prompt sensitivity, model drift, privacy constraints, and replication limits;
6. evaluate whether LLM-based evidence meets applied-economics standards for measurement, identification, and reproducibility.

## Opening Orientation

Lectures 12 and 13 treated unstructured records as inputs into economic measurement and then asked how to validate the resulting variables. Lecture 14 changes the object. The large language model is no longer only one possible classifier inside a text pipeline. It becomes part of the research infrastructure: it may draft code, search documents, extract structured fields, assign labels, summarize qualitative evidence, simulate survey respondents, or generate actions inside a stylized economic environment.

The central question is: **how can LLMs support applied research without weakening reproducibility or evidentiary standards?** This is not another text-as-data lecture. Lecture 12 asked how documents become variables. Lecture 13 asked how constructed variables are validated. Lecture 14 asks what happens when the model helps operate the research workflow itself.

The paper spine is intentionally frontier-facing but disciplined. Korinek explains how generative AI can help economists write, code, summarize, reason, and orchestrate research tasks [@korinek2024genai]. His work on AI agents extends that logic to multi-step tool-using workflows that require stronger logging and reproducibility discipline [@korinek2025agents]. Chen and coauthors provide an economics-oriented measurement application: using LLMs to recover information relevant to labor-market mismatch that is hidden in coarse categorical data [@chen2024mismatch]. Choi gives a useful benchmark from empirical legal research, where document extraction looks powerful only if prompts, schemas, benchmarks, and review rules are specified [@choi2023llmlegal]. Horton, Filippas, and Manning frame LLMs as simulated economic agents, while Manning, Zhu, and Horton study automated social science where models can appear as both scientist-support tools and synthetic subjects [@horton2023homosilicus; @manning2024automated].

The lecture's claim is conservative. LLMs can reduce the cost of working with documents, code, labels, and scenarios. They do not replace research design. A publishable applied paper still needs a clear economic object, validation evidence, privacy safeguards, and a replication path.

## Core Points

:::{admonition} Core points
:class: important

- LLMs can serve as research assistants, coders/extractors, synthetic annotators, simulated subjects, and simulation engines. These roles imply different evidentiary standards.
- A prompt, model, retrieval corpus, decoding setting, schema, and post-processing rule are part of the measurement instrument.
- LLM-generated variables require benchmark evidence, subgroup diagnostics, audit samples, and sensitivity checks before they enter descriptive, causal, structural, or policy analysis.
- Synthetic subjects and LLM agents are useful for pilots, mechanism exploration, and benchmarked scenario analysis, but they are not evidence about human behavior unless validated against human behavior.
- Replication requires prompt logs, model/version records, retrieval snapshots, raw and parsed outputs, human-review decisions, privacy documentation, and stable evaluation scripts.
- Hallucination risk is not only a factual-error problem. It is a measurement-error and research-design problem when unsupported outputs become data.
:::

## Bridge

Lecture 14 sits at the end of the course's text, computation, and LLM block. The bridge from the prior two lectures is direct: an LLM workflow can be useful only after the researcher says what it is doing.

```{include} assets/tables/14-theory-to-applied-bridge.md
```

The key distinction is role. If an LLM helps debug code or draft a cleaning script, the final published object can still be researcher-controlled. If an LLM labels whether a contract includes a noncompete, the model is a measurement device. If an LLM answers a survey vignette as a simulated worker, it is a synthetic subject. If an LLM negotiates, searches, or updates beliefs inside a simulated economy, it is part of the modeled environment.

Each role can be defensible. None should be treated as magic. The applied-economics standard is always the same: define the economic object, document the workflow, validate against relevant evidence, and explain how remaining errors affect the claim.

## Field Core

### A. Four Roles For LLMs In Applied Research

The first mistake is to ask whether "using an LLM" is acceptable. The better question is which research role the model plays.

```{include} assets/tables/14-workflow-and-algorithm-choices.md
```

**Research assistant.** The model supports researcher labor: code drafting, data-cleaning suggestions, literature triage, summarization, debugging, extraction-template drafting, or conversion of messy notes into a reproducible script. Korinek emphasizes these as high-value uses because the model can accelerate tasks while the researcher retains responsibility for the final design [@korinek2024genai]. Agentic workflows raise the stakes because the model may plan tool calls, modify files, and produce multi-step artifacts [@korinek2025agents].

**Coder, extractor, or data encoder.** The model produces structured data from unstructured or semi-structured records: labels, fields, categories, scores, or rationales. At this point, the model is not merely helping. It is part of the measurement process. Chen and coauthors' LLM-based labor-market mismatch setting is useful because the output is an economic variable, not a generic model demonstration [@chen2024mismatch]. Choi's empirical legal research guidance makes the same point in a document-heavy setting: stable schemas and benchmarks are what turn plausible extraction into research evidence [@choi2023llmlegal].

**Synthetic coder or annotator.** The model produces labels that mimic or supplement human coding. This can be useful when human annotation is expensive, but it does not eliminate the need for human benchmarks. Gilardi, Alizadeh, and Kubli show that ChatGPT can perform well on some text-annotation tasks, yet the research implication is not that all labels can be automated; it is that synthetic coding must be evaluated task by task [@gilardiAlizadehKubli2023].

**Synthetic subject or simulated respondent.** The model generates responses to survey questions, experiments, games, or institutional vignettes. Horton, Filippas, and Manning call this "Homo Silicus" to emphasize that the model is being treated as an implicit computational model of human behavior [@horton2023homosilicus]. Argyle and coauthors provide a related political-science example of simulated samples [@argyleBusbyFuldaGublerRyttingWingate2023]. For economics, the promise is pilot testing and mechanism exploration. The risk is mistaking prompt-conditioned completions for human behavioral evidence.

**Simulation engine or agent environment.** The model generates actions, narratives, state transitions, or interactions inside a simulated economy. This can help explore bargaining, job search, managerial decision-making, institutional compliance, or policy scenarios. But once the model helps generate both behavior and environment, validation becomes harder. Manning, Zhu, and Horton therefore treat automated social science as a research-infrastructure frontier rather than a substitute for empirical evidence [@manning2024automated].

### B. LLMs As Measurement And Data-Construction Tools

When the LLM constructs variables, the notation should make the workflow visible. Let {math}`x_i` be the raw record for unit {math}`i`: a job ad, resume, contract, open-ended response, court document, policy memo, case note, transcript, or combined document bundle. Let {math}`p_i` be the prompt or instruction template. Let {math}`r_i` be retrieved context, such as a coding rubric, examples, statute text, occupation taxonomy, or paper-specific schema. Let {math}`\theta` index the model, version, decoding settings, system prompt, tool configuration, and post-processing code. A generic LLM measurement mapping is:

```{math}
:label: eq:em14-llm-measurement
\widehat z_i = g_{\theta}(x_i, p_i, r_i).
```

The downstream paper often then uses the constructed object as if it were data:

```{math}
:label: eq:em14-downstream-use
Y_i = \alpha + \beta \widehat z_i + u_i.
```

The econometric issue is not that {math}`\widehat z_i` came from an LLM. The issue is whether {math}`\widehat z_i` measures the object required by the downstream equation. A model that accurately extracts whether a job ad mentions "remote" does not necessarily measure remote-work feasibility. A model that classifies whether a resume matches a vacancy may partly encode firm demand, worker credentials, prompt examples, or stereotypes about career paths. A model that summarizes a grievance file may omit facts that matter for legal or institutional interpretation.

The publication-ready workflow therefore needs several layers:

- a fixed schema that defines permissible fields and categories;
- a prompt template with examples and edge-case instructions;
- a retrieval corpus with versioned documents and retrieval settings;
- a benchmark set labeled or adjudicated independently of the model outputs being evaluated;
- raw model outputs preserved before cleaning;
- parsed outputs and post-processing rules;
- human-review rules for ambiguous, high-stakes, or low-confidence cases;
- diagnostics by subgroup, document type, time, language, and source institution.

The model output is not self-authenticating. It becomes a research object only after the workflow makes its origin and failure modes observable.

### C. Prompt, Model, Benchmark, And Transport Risk

LLM risk is often described as hallucination. That is too narrow for empirical work. A structured output can be factually plausible and still wrong for the economics.

```{include} assets/tables/14-llm-workflow-diagnostics.md
```

A useful classroom decomposition is:

```{math}
:label: eq:em14-risk-decomposition
R_{\text{workflow}}
=
R_{\text{prompt}}
+ R_{\text{model}}
+ R_{\text{retrieval}}
+ R_{\text{benchmark}}
+ R_{\text{transport}}
+ R_{\text{privacy}}.
```

This is not a structural identity. It is a checklist for research design.

**Prompt risk** appears when small wording changes alter labels or extracted values. If the result changes when the prompt says "classify conservatively" rather than "identify all possible cases," the paper must decide which target is substantively correct.

**Model risk** appears when different model versions, closed-model updates, decoding settings, or context-window behavior change outputs. Version drift is especially serious when the published replication package cannot call the original model.

**Retrieval risk** appears when the model answers from the wrong chunks, missing context, stale documents, or a retrieval index that is not preserved. Retrieval-augmented generation is useful, but the retrieval step itself becomes part of the data pipeline.

**Benchmark risk** appears when the "gold" labels are too small, too easy, too close to the prompt examples, or built from a different population than the applied sample.

**Transport risk** appears when a prompt validated on one document type, region, occupation, legal regime, language, or time period is reused elsewhere.

**Privacy risk** appears when raw documents contain confidential, personally identifiable, proprietary, or legally restricted information. An external API call can be a data-disclosure decision, not only a computing decision.

### D. LLMs As Synthetic Coders And Annotators

Synthetic coding can be attractive because human annotation is slow and expensive. An LLM can label thousands of open-ended responses, extract clauses from contracts, code job tasks, summarize case narratives, or generate a first pass over qualitative material. Haaland and coauthors show why open-ended survey responses can be valuable for economics, and why LLM-assisted coding requires explicit validation and review [@haalandRothStantchevaWohlfart2024].

The right design usually combines synthetic coding with human review rather than replacing human review entirely. A defensible protocol might:

- hand-label a stratified benchmark sample;
- run the LLM on the same cases using a fixed prompt and schema;
- compare precision, recall, calibration, and subgroup performance;
- route disagreements, low-confidence cases, and high-stakes cases to human review;
- report sensitivity to prompt wording and model version;
- preserve the prompt log and raw completions.

Synthetic labels are most useful when the target construct is clear, the benchmark is real, and the workflow is auditable. They are weakest when the construct is ambiguous, the labels require institutional expertise, the population shifts across domains, or the model is asked to infer unobserved motives without evidence.

### E. LLMs As Experimental Subjects Or Simulated Respondents

Synthetic subjects are conceptually different from synthetic coders. A synthetic coder labels existing records. A synthetic subject produces a hypothetical choice, belief, or response. Let {math}`e_i` denote the experimental environment or vignette, {math}`p_i` the persona or instruction prompt, and {math}`c_i` the context supplied to the model. A generic response mapping is:

```{math}
:label: eq:em14-synthetic-subject
a_i = s_{\theta}(e_i, p_i, c_i),
```

where {math}`a_i` is a simulated action, choice, survey answer, or message.

This can be useful. Researchers can pilot survey wording, explore which mechanisms a vignette evokes, stress-test an experimental design, or generate hypotheses about institutional scenarios before collecting expensive human data. Horton, Filippas, and Manning argue that LLMs can be informative when treated as simulated economic agents whose behavior is itself an object to be benchmarked [@horton2023homosilicus]. Manning, Zhu, and Horton extend the idea to workflows where models help generate experiments and participate as subjects [@manning2024automated].

But the estimand changes. If the target is human workers' labor-supply response to a tax schedule, an LLM response is not a direct estimate of that response. If the target is whether an experimental vignette is clear, synthetic subjects may be useful as a pilot diagnostic. If the target is how a model trained on large text corpora behaves in economic games, then the LLM itself is the object of study. Confusing these three uses produces overclaiming.

The minimum standard for synthetic-subject work is:

- benchmark the model on tasks where human behavior is already known;
- vary persona, wording, ordering, and context to measure prompt sensitivity;
- compare across model versions when possible;
- report when the model reproduces human patterns and when it fails;
- avoid presenting synthetic responses as evidence about humans without validation against humans.

### F. LLMs As Simulation Engines And Agent Environments

The frontier use is to place LLMs inside iterative environments. The model might act as a worker, firm, manager, recruiter, union, agency, judge, or platform. A simple state-transition object is:

```{math}
:label: eq:em14-agent-transition
x_{t+1} = f_{\theta}(x_t, a_t, \varepsilon_t),
```

where {math}`x_t` is the current state, {math}`a_t` is an action generated by an LLM or by a rule interacting with an LLM, and {math}`\varepsilon_t` is exogenous noise or a shock process.

This form makes simulation risk visible. The LLM may generate actions, interpret the state, update beliefs, summarize history, and produce the next state. The simulation can look rich because the narratives are fluent. Fluency is not validation. The relevant standard is whether the environment reproduces known empirical regularities, yields stable comparative statics under transparent state/action rules, and clarifies mechanisms rather than burying assumptions inside prompts.

For applied economics, LLM simulation is most credible as research infrastructure:

- scenario analysis before formal modeling;
- pilot testing of institutional rules;
- generation of hypotheses for survey or field experiments;
- stress testing whether an extraction or coding workflow handles edge cases;
- pedagogical simulation of labor-market matching, bargaining, or search.

It is least credible when it substitutes for observed behavior, when agents are given vague personas, when the transition rule is hidden in natural-language prompts, or when the paper interprets simulated equilibrium as empirical evidence without benchmarks.

### G. Prompt Logs, Retrieval, Audit Trails, And Human Review

An LLM workflow should be documented like a lab instrument. A minimum audit trail contains:

- project, task, unit of analysis, and intended economic object;
- model provider, model name, model version or date, and decoding settings;
- system prompt, user prompt template, examples, and schema;
- retrieval corpus version, chunking rule, embedding/retrieval settings, and retrieved passages;
- raw input identifier and raw output identifier for every unit;
- parsed fields, validation errors, post-processing code, and exclusion rules;
- human-review assignment, reviewer decision, adjudication rule, and final label;
- benchmark construction, evaluation code, and sensitivity scripts;
- privacy and data-handling notes.

The rule is simple: another researcher should be able to trace each published LLM-generated value from the raw input to the prompt, retrieval context, model output, parser, human review, and final dataset.

Human review should be allocated where it matters most. Review all high-stakes cases, cases with low confidence or schema violations, cases in underrepresented subgroups, and cases that drive downstream estimates. Review should not be informal memory. It should produce review fields that can be audited, such as `review_status`, `reviewer_id`, `adjudicated_label`, `reason_code`, and `date`.

### H. Replicability, Privacy, And Evidentiary Standards

LLM-based research has a replication problem even when the code is clean. Closed models may change. APIs may disappear. Decoding can be nondeterministic. Retrieval corpora can drift. Prompts can be revised during exploratory work. Confidential records may not be shareable. These constraints do not make LLM workflows unusable, but they do change what a replication package must contain.

A credible package should include the benchmark set, prompt templates, schema definitions, model/version metadata, raw outputs when shareable, parsed outputs, evaluation scripts, and a plan for rerunning or auditing the workflow when the original model is unavailable. For confidential data, researchers should provide synthetic examples, redacted prompt logs, aggregate diagnostics, secure review procedures, and clear statements about what cannot be released.

The evidentiary standard should rise with the role of the LLM output. If the model drafts code that the researcher checks, standard code review and tests may be enough. If the model creates the treatment variable, outcome, exposure, instrument, or structural moment, the paper needs measurement validation. If the model simulates agents, the paper needs behavioral benchmarks and humility about external validity. If the model processes confidential records, privacy review is part of the research design.

## Research Lab

The Week 14 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. The lab is a bounded synthetic teaching path, not an official replication of any paper. It is inspired by LLM-based labor-market measurement work such as Chen and coauthors [@chen2024mismatch], by document-extraction standards from Choi [@choi2023llmlegal], and by the broader LLM-research workflow guidance in Korinek [@korinek2024genai; @korinek2025agents].

### Reproduce

Students reproduce a small structured-data construction workflow. The source data are synthetic labor-market document bundles containing a job description and a worker or applicant note. A deterministic teaching surrogate stands in for an LLM so the lab can run without an API. Students:

- define a schema for mismatch coding;
- run a documented prompt template;
- generate structured outputs for each document;
- preserve prompt logs, model metadata, raw outputs, and parsed fields;
- compare the generated labels to a benchmark set;
- estimate how a constructed mismatch variable changes a downstream labor-market association.

The point is not to claim the surrogate is an LLM. The point is to make the workflow architecture executable and auditable.

### Diagnose

Students diagnose prompt sensitivity, benchmark dependence, subgroup stability, hallucination-like unsupported outputs, and downstream consequences:

- Do conservative and expansive prompts create different mismatch rates?
- Which subgroups or document types have the largest error rates?
- Which outputs violate the schema or lack textual support?
- How does using the LLM-coded variable instead of the benchmark variable change the downstream slope?
- Which cases should be routed to human review?

### Transfer

Students transfer the workflow to synthetic workforce-agency case notes. The transfer domain uses different language, a different document type, and different ambiguity. Students:

- apply the source prompt to the transfer sample;
- compare it with a domain-adapted prompt;
- evaluate transport metrics against a transfer benchmark;
- write a benchmark-redesign memo;
- identify which parts of the prompt log, retrieval record, and audit trail would need to change before a real paper used the workflow.

The lab's final memo asks students to separate three claims: the workflow can construct a variable, the variable validates against a benchmark, and the variable is credible for a downstream economics question.

## Methods Box

Students who want deeper technical study should treat these as resources for research design, not as a mandate to make the lecture an engineering course.

**LLM workflows for economists.** Korinek provides a practical guide to generative AI for economic research, with attention to writing, coding, reasoning, and research productivity [@korinek2024genai]. Korinek's agent paper is the natural next step for multi-tool and multi-step research workflows [@korinek2025agents].

**Measurement and extraction.** Chen and coauthors are the economics anchor for LLM-assisted labor-market measurement [@chen2024mismatch]. Choi is useful for schema-based extraction, benchmarking, and empirical-document workflows [@choi2023llmlegal]. Haaland and coauthors connect open-ended survey responses to LLM-assisted coding and human review [@haalandRothStantchevaWohlfart2024].

**Synthetic coding and synthetic subjects.** Gilardi, Alizadeh, and Kubli provide evidence on LLM text annotation [@gilardiAlizadehKubli2023]. Horton, Filippas, and Manning, Manning, Zhu, and Horton, and Argyle and coauthors are useful anchors for simulated respondents, automated social science, and the interpretation of synthetic samples [@horton2023homosilicus; @manning2024automated; @argyleBusbyFuldaGublerRyttingWingate2023].

**Validation and measurement error.** Lecture 14 inherits the validation standards from Lectures 12 and 13. The relevant technical resources include Gentzkow, Kelly, and Taddy for text-as-data measurement, Grimmer, Roberts, and Stewart for social-science text methods, and Bound, Brown, and Mathiowetz for measurement error [@gentzkowKellyTaddy2019; @grimmerRobertsStewart2022; @bound2001measurementError].

## Reading Ladder And References

```{include} assets/tables/14-reading-architecture.md
```

**First pass: workflow discipline.** Read Korinek on generative AI for economic research, then write down which uses are assistant roles and which create research data [@korinek2024genai].

**Second pass: extraction and measurement.** Read Chen and coauthors with Choi. Identify the schema, prompt protocol, benchmark, and validation evidence required before an LLM output becomes a publishable variable [@chen2024mismatch; @choi2023llmlegal].

**Third pass: open-ended responses and synthetic coding.** Read Haaland and coauthors and Gilardi, Alizadeh, and Kubli. Compare human-label and model-label workflows, then ask what human review remains necessary [@haalandRothStantchevaWohlfart2024; @gilardiAlizadehKubli2023].

**Fourth pass: synthetic subjects and agents.** Read Horton, Filippas, and Manning, then Manning, Zhu, and Horton. Focus on what is being estimated: human behavior, model behavior, or a tool for designing future empirical work [@horton2023homosilicus; @manning2024automated].

**Fifth pass: agentic workflow frontier.** Read Korinek on AI agents and connect it to replication-package design: what needs to be logged when a model plans, calls tools, edits files, and produces intermediate artifacts? [@korinek2025agents]

## Exercises And Discussion Prompts

1. Give one economics project where an LLM is best treated as a research assistant and one where it is a measurement device. What changes in the validation standard?
2. Suppose an LLM-coded noncompete variable has high average agreement with human labels but lower recall for small firms. How could this affect a study of wage effects?
3. Write a minimal prompt log for a project that extracts training requirements from job ads. Which fields are necessary for replication?
4. A prompt produces more positive labels when it includes the phrase "look for implicit evidence." Is that an improvement or a change in the estimand?
5. When should synthetic respondents be used to pilot a survey experiment, and when would they be misleading?
6. Design a validation benchmark for an LLM agent simulation of worker-firm bargaining. What known regularities should it reproduce before the simulation is useful?
7. A researcher cannot release confidential raw documents. What synthetic data, metadata, audit logs, and evaluation scripts should the replication package include?
8. In the downstream model {math}`Y_i = \alpha + \beta \widehat z_i + u_i`, what failures in {math}`\widehat z_i` are most dangerous if the research design compares firms before and after a policy shock?

## Reproducibility And Code Lab Note

The canonical lab lives at:

```text
labs/14-llm-workflows-for-applied-research/
```

The lab uses Python and deterministic synthetic data. It includes:

- `lab.md` and `README.md`;
- a smoke test in `smoke.sh`;
- source scripts under `src/`;
- synthetic source records under `original/reduced/`;
- transfer records under `transfer/data/`;
- reproduced outputs under `output/reproduced/`;
- transfer outputs under `output/transfer/`.

The smoke path does not call any live model API. It uses a deterministic teaching surrogate to make prompt logs, schema-constrained outputs, benchmark diagnostics, and transfer checks reproducible. In a real project, the same folder would also preserve raw model outputs, retrieval snapshots, privacy documentation, and human-review records.

## Slide Companion Note

The Week 14 slides should define LLMs as research infrastructure rather than as another text classifier. The deck should separate five roles: research assistant, coder/extractor, synthetic annotator, synthetic subject, and simulation engine. It should include the measurement mapping, downstream-use equation, synthetic-subject mapping, transition object, and the minimum publication-ready audit trail.

The final slides should leave students with a practical standard: an LLM workflow is ready for applied economics only when another researcher can trace the output, rerun or audit the workflow, inspect validation evidence, and understand how remaining errors affect the economic claim.

The canonical slide source is `slides/week14/14-llm-workflows-for-applied-research.tex`.

## Bridge Forward

Lecture 14 closes the core block on text, computation, and LLM-based methods. The next optional block turns to spatial methods. The link is measurement discipline. Whether the raw object is a document, prompt, map, satellite image, boundary file, commute flow, or network edge, applied research starts by defining the economic object and ends by explaining what the evidence can and cannot support.
