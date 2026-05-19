Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/12-text-as-data-and-computational-measurement.md if it exists
- @books/empirical-methods/13-extraction-classification-embeddings-and-validation.md if it exists

Goal: create Lecture 14 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/14-llm-workflows-for-applied-research.md`
- `books/empirical-methods/slides/week14/14-llm-workflows-for-applied-research.tex`
- `books/empirical-methods/labs/14-llm-workflows-for-applied-research/`

Use these as the intellectual source of truth:
1. the lecture source pack and tables from this week-specific pack
2. the course outline
3. Lectures 12 and 13 as immediate predecessors

Lecture 14 identity to preserve:
- Lecture 14 is NOT another text-as-data or validation lecture.
- It focuses on LLMs as research infrastructure for applied economics.
- It must explicitly cover:
  A. LLMs as research assistants for coding, extraction, classification, summarization, and structured-data construction
  B. LLMs as synthetic coders / annotators / data encoders
  C. LLMs as experimental subjects or simulated respondents
  D. LLMs as simulation engines / agent environments for economic reasoning and scenario analysis
  E. Prompt logging, versioning, retrieval, audit trails, privacy, and human-in-the-loop review
  F. Replicability, hallucination risk, benchmark design, and evidentiary standards
- It should stay tightly connected to economics papers and implementation choices.
- It should be honest about current limitations and frontier status.

Non-negotiable content:
1. LLM-assisted research workflows and where they are actually useful
2. LLMs as measurement and data-construction tools
3. LLMs as synthetic experimental subjects / simulated respondents
4. LLMs as simulation machines for economic environments or agents
5. Prompt documentation, retrieval, and audit-trail design
6. Replication, privacy, and reproducibility constraints
7. Research Lab with Reproduce → Diagnose → Transfer workflow
8. Methods Box with references/resources for deeper technical study

Required chapter structure:
1. Opening Orientation
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Methods Box
7. Reading Ladder And References
8. Exercises And Discussion Prompts
9. Reproducibility And Code Lab Note
10. Slide Companion Note
11. Bridge Forward

Equations / formal objects that should appear:
- a generic LLM measurement / extraction mapping, e.g.
  `\hat z_i = g_\theta(x_i, p_i, r_i)`
- a downstream use equation, e.g.
  `Y_i = \alpha + \beta \hat z_i + u_i`
- a simulated-agent response mapping, e.g.
  `a_i = s_\theta(e_i, p_i, c_i)`
- a simulation / transition object for iterative environments if useful, e.g.
  `x_{t+1} = f_\theta(x_t, a_t, \varepsilon_t)`
- a simple risk decomposition or accuracy/reliability object if useful for workflow evaluation

Paper anchors to use if helpful:
- Korinek on generative AI / LLMs for economic research
- Korinek on AI agents for economic research
- Horton, Filippas, and Manning on LLMs as simulated economic agents
- Manning et al. on automated social science / scientist-and-subject workflows
- Chen et al. on LLM-based measurement for labor market mismatch
- Choi on LLMs for empirical legal research
- any additional primary-source papers that help anchor the workflow, as long as the lecture remains economics-oriented

Slides requirements:
- create the canonical slide deck:
  `books/empirical-methods/slides/week14/14-llm-workflows-for-applied-research.tex`
- use the same professional default beamer style already used elsewhere in the repo
- include one slide each on:
  - LLMs as research assistants
  - LLMs as coders / extractors
  - LLMs as experimental subjects
  - LLMs as simulation engines
  - replication / audit trails / privacy
  - research lab design
- do not create duplicate slide files outside `slides/week14/`

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- the lab should be bounded and concrete, such as:
  - reproduce a small structured-data extraction workflow from text
  - diagnose prompt sensitivity / model sensitivity / benchmark dependence
  - transfer to a new domain or prompt template
- if full official replication data are not present locally, create a bounded synthetic teaching path
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `smoke.sh`
  - `src/`
  - `output/reproduced/`
  - `output/transfer/`

Implementation notes:
- keep the lecture research-oriented, not a generic AI-tools lecture
- methods must be tied to concrete papers and implementation caveats
- explicitly distinguish:
  - using LLMs to build variables
  - using LLMs to simulate responses/agents
  - using LLMs to orchestrate research workflows
- stress that LLMs do not replace validation or design-based reasoning
- linked citations only in prose markdown
- preserve the course’s canonical structure and local bibliography policy

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Week 14 slides from the canonical path
3. if a bounded Week 14 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 14 slides compile from the canonical path
5. whether the Week 14 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
