---
title: LLM Workflows for Applied Research
bibliography:
  - bibliography/14-llm-workflows-for-applied-research.bib
---

# LLM Workflows for Applied Research

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish between using LLMs as research assistants, as coders/annotators, as synthetic subjects, and as simulation engines;
2. explain when an LLM-assisted workflow improves an applied economics project and when it mainly adds unvalidated noise;
3. formalize the key objects created by LLM workflows and the risks they introduce for downstream inference;
4. describe how to document prompts, model versions, retrieval, benchmark sets, and human-review pipelines;
5. defend or reject an LLM workflow using the standards of reproducibility, auditability, and economic interpretation expected in applied research.

## Opening Orientation

Lectures 12 and 13 treated unstructured data as an input into economic measurement and then asked how to validate the resulting variables. Lecture 14 goes one step further: it treats large language models as **research infrastructure**. Researchers now use LLMs to code text, extract structured variables, annotate documents, synthesize labels, prototype experiments, generate simulated respondents, and even build agent-based economic environments. These uses are increasingly common in frontier work, but they are not interchangeable.

The central question is not whether LLMs are “good” or “bad” for research. The question is: **what economic object is the LLM generating, what assumptions does that workflow impose, and how can the workflow be documented and validated so that the resulting evidence remains credible?** Recent economics-facing papers and guides emphasize that LLMs can lower the cost of many research tasks, but they only create publishable evidence when researchers retain control over benchmarking, uncertainty, and reproducibility [@korinek2024genai; @korinek2025agents].

::: {.admonition title="Core points"}
- LLMs can support applied research as assistants, coders, synthetic subjects, or simulation engines, but each use case has different evidentiary risks.
- A prompt/model/workflow is part of the measurement process and must be documented like any other research instrument.
- LLM-generated variables and simulated behaviors are only useful when benchmarked against human labels, known facts, or economically meaningful external validation targets.
- LLMs can accelerate research, but they do not replace identification logic, validation, or reproducible workflows.
- The right question is not “Can the model do this?” but “What exactly is the model measuring or simulating, and how would errors change the economic claim?”
:::

## Bridge

Lecture 12 focused on turning unstructured inputs into variables. Lecture 13 focused on validating those variables. Lecture 14 asks what happens when the model itself becomes part of the research workflow: when it helps define variables, label data, generate responses, or simulate environments. The continuity with the earlier lectures is important: LLMs may reduce labor in coding and synthesis, but they do not relax the standards for economic interpretation.

## Field Core

### 1. Four roles for LLMs in applied economics

It helps to separate four distinct research roles:

1. **Research assistant**: coding, summarization, literature mapping, drafting code, extracting fields from documents.
2. **Coder / annotator / measurement device**: turning raw text or other unstructured objects into structured variables.
3. **Synthetic subject**: producing responses to experimental prompts, survey vignettes, or institutional scenarios.
4. **Simulation engine / agent environment**: representing behavior or interaction in a stylized economy or institutional environment.

These roles differ in what the model output means. In the first role, the model is a labor-saving tool. In the second, it is a measurement device. In the third and fourth, it becomes part of the object of analysis.

A generic extraction/measurement mapping is:

```{math}
:label: eq:llm-extraction
\hat z_i = g_{\theta}(x_i, p_i, r_i),
```

where `x_i` is the raw unstructured object, `p_i` is the prompt or instruction set, `r_i` is any retrieval/context layer, and `\theta` indexes model and workflow choices. Downstream empirical work often treats `\hat z_i` as if it were data:

```{math}
:label: eq:downstream-use
Y_i = \alpha + \beta \hat z_i + u_i.
```

The key point is that the mapping from `x_i` to `\hat z_i` is not mechanical in the way a standard administrative variable often is. It is a designed, model-dependent transformation.

### 2. LLMs as research assistants and coders

The most defensible LLM use case is often as a research assistant. Korinek’s guide emphasizes tasks like coding help, document summarization, data cleaning support, prompt-based extraction, and workflow orchestration as realistic uses for economists [@korinek2024genai]. Korinek’s later AI-agents guide extends this to multi-step research workflows in which the model plans tasks, calls tools, and produces research artifacts, but the core warning remains: agentic assistance raises the stakes for logging, checkpointing, and reproducibility [@korinek2025agents].

When LLMs are used to produce data—e.g. classify contracts, identify job-task content, or score labor-market mismatch—they move from assistant to measurement device. Chen et al. provide an economics example by using LLMs in the role of a human-resources specialist to recover overlooked information in categorical labor-market data [@chen2024mismatch]. Choi provides a useful general benchmark for empirical legal/data extraction workflows: the credibility question is not whether the model can produce plausible outputs, but whether the researcher can specify a stable prompt protocol, benchmark the outputs, and explain how any remaining errors affect the substantive claim [@choi2023llmlegal].

This leads to a practical decomposition:

```{math}
:label: eq:workflow-risk
\text{Research risk} = \text{prompt risk} + \text{model risk} + \text{benchmark risk} + \text{transport risk}.
```

This is not a literal econometric decomposition, but it is a useful way to teach students that workflow choices are part of inference.

### 3. LLMs as synthetic subjects

A more ambitious use is to treat LLMs as simulated economic agents or synthetic survey/experimental subjects. Horton, Filippas, and Manning’s "Homo Silicus" paper is the natural anchor here: it argues that LLMs can be treated as implicit computational models of humans and can therefore be placed into experimental scenarios to study behavior under alternative designs [@horton2023homosilicus]. Manning et al. push this further in “Automated Social Science,” where language models appear as both scientist-support tools and synthetic subjects [@manning2024automated].

A generic subject-generation mapping is:

```{math}
:label: eq:synthetic-subject
a_i = s_{\theta}(e_i, p_i, c_i),
```

where `a_i` is the simulated action/response, `e_i` is the environment, `p_i` the prompt/persona/instruction design, and `c_i` the contextual information supplied to the model.

The empirical question is then not “does the model answer sensibly?” but “under what tasks does the model reproduce patterns that are informative about human behavior, and when is it merely reflecting its training data or prompt artifacts?” Synthetic subjects can be useful for pilot testing, mechanism exploration, or stress-testing experimental designs, but they are not substitutes for human subjects when the target estimand is actual human behavior.

### 4. LLMs as simulation machines

A still more ambitious use is to embed LLMs in simulated institutional or economic environments. One can formalize this as a transition system:

```{math}
:label: eq:llm-simulation
x_{t+1} = f_{\theta}(x_t, a_t, \varepsilon_t),
```

where `x_t` is the current state, `a_t` is the LLM-generated or LLM-mediated action, and `\varepsilon_t` is exogenous noise. In practice, this can mean multi-agent negotiation, simulated survey populations, policy games, or institutional scenario exploration.

The appeal is obvious: such systems can generate synthetic interactions at low marginal cost. The danger is also obvious: once the model is both the generator of behavior and part of the environment, validation becomes much harder. The relevant standard is not whether the simulation “looks realistic,” but whether it reproduces well-defined empirical regularities or provides disciplined comparative statics tied to a transparent benchmark.

### 5. Retrieval, prompt logging, and audit trails

Applied research should treat prompt workflows like research instruments. At minimum, a serious workflow should preserve:

- model name and version;
- prompt templates;
- retrieval corpus/version and retrieval settings;
- temperature / decoding choices;
- batch size and query order where relevant;
- human-review procedures;
- benchmark sets and evaluation scripts;
- post-processing rules.

A useful classroom rule is: **if another researcher cannot rerun the exact prompt workflow and understand where the final variables came from, then the workflow is not yet publication-ready.**

### 6. Privacy, hallucination, and reproducibility

LLMs create three recurring problems for applied work:

1. **Privacy/confidentiality**: documents may contain sensitive information and cannot always be sent to external APIs.
2. **Hallucination / unsupported completion**: the model may generate structured outputs that look plausible but are ungrounded.
3. **Version drift / reproducibility**: closed models and changing APIs can make reruns unstable.

This is why the best economics use cases tend to be either:
- well-benchmarked extraction/classification tasks with clear human comparison,
- carefully documented assistant workflows where the model does not directly determine the final published variable,
- or synthetic-subject/simulation exercises that are presented as exploratory or benchmarked research infrastructure rather than final evidence.

## Research Lab

### Primary anchor

Use [@chen2024mismatch] as the main reproduction anchor. The pedagogical object is not to recreate the whole paper, but to reproduce the core workflow: using an LLM to map rich textual or categorical information into a structured labor-market measure.

### Reproduce

Students should reproduce a bounded extraction/classification workflow on a small corpus:
- define the economic object to be extracted;
- implement a documented prompt/template;
- generate structured outputs;
- compare the outputs with a small benchmark set.

### Diagnose

Students should diagnose:
- sensitivity to prompt wording;
- sensitivity to model choice or settings if feasible;
- failure modes on subgroup or edge cases;
- what errors would imply for a downstream regression or descriptive claim.

### Transfer

Students should transfer the workflow to a new domain or prompt context, for example:
- from job-match suitability to resume–job classification,
- from document extraction to contract-clause identification,
- from one labor-market domain to another.

### Challenge anchor

Use [@horton2023homosilicus] or [@manning2024automated] as the challenge/extension anchor. Students can compare measurement-oriented use of LLMs with synthetic-subject or simulation-oriented use and explain why the validation standard changes.

## Methods Box

Students who want technical depth should look to:
- [@korinek2024genai] and [@korinek2025agents] for economists’ practical workflows;
- [@choi2023llmlegal] for extraction/classification workflows and benchmarking logic;
- [@horton2023homosilicus] and [@manning2024automated] for synthetic-subject and automated-social-science uses.

The practical lesson is not to memorize one “best prompt,” but to learn how to document a pipeline, benchmark it, and explain why the resulting object is economically meaningful.

## Reading Ladder And References

### Core methodological anchors
- [@korinek2024genai]
- [@korinek2025agents]
- [@horton2023homosilicus]
- [@manning2024automated]

### Measurement / extraction applications
- [@chen2024mismatch]
- [@choi2023llmlegal]

### Frontier / simulation / research-infrastructure direction
- [@horton2023homosilicus]
- [@manning2024automated]
- [@korinek2025agents]

## Exercises And Discussion Prompts

1. Give one example where an LLM should be treated primarily as a research assistant and one where it should be treated as a measurement device. Why are the validation standards different?
2. Suppose an LLM-coded variable has strong average agreement but poor subgroup stability. What does that imply for downstream causal or heterogeneity analysis?
3. When, if ever, should LLM-generated synthetic subjects be used to motivate a new economics experiment?
4. Design a prompt log and audit trail for a paper that uses LLMs to code labor contracts.
5. Give one use case where LLM simulation may be informative and one where it would likely be misleading.

## Reproducibility And Code Lab Note

The Week 14 lab should provide a small, benchmarked extraction workflow with a reduced teaching corpus and logged prompts. The smoke path should avoid any dependence on live APIs and instead use synthetic or cached outputs where necessary.

## Slide Companion Note

Slides should emphasize the distinction between three uses of LLMs: assistants, coders, and simulated agents. The final slides should also include a “minimum publication-ready workflow” slide that lists prompt logging, benchmarking, human review, and audit trails.

## Bridge Forward

Lecture 14 closes Block 4 by showing that LLMs are not a shortcut around research design. They are best understood as powerful but fallible infrastructure for measurement, coding, simulation, and workflow orchestration. The empirical methods course ends when students can decide not only how to use these tools, but also when not to use them.
