Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/18-curating-network-data-and-descriptive-statistics.md if it exists
- @books/empirical-methods/19-causal-inference-with-network-data.md if it exists

If helpful, also inspect:
- the Lecture 19 source pack if it exists in the repo
- the Lecture 19 slide file if it exists
- the Lecture 19 lab folder if it exists

Goal: create or refresh Lecture 19 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/19-causal-inference-with-network-data.md`
- `books/empirical-methods/slides/week19/19-causal-inference-with-network-data.tex`
- `books/empirical-methods/labs/19-causal-inference-with-network-data/`

Use these as the intellectual source of truth:
1. the week source pack under `empirical_methods_lecture19_edit_pack/source/`
2. the week bibliography under `empirical_methods_lecture19_edit_pack/bibliography/`
3. the week tables under `empirical_methods_lecture19_edit_pack/tables/`

This is a lecture-drafting / sync task, not a fresh course redesign.

Non-negotiable lecture identity:
- The lecture is about **causal inference with network data**, not general network analysis.
- It must explain how network structure changes identification, estimation, inference, and interpretation.
- It must cover:
  - reflection problem
  - peer effects
  - interference and spillovers
  - exposure mappings
  - randomized saturation and network experiments
  - partial interference
  - inference under dependence
  - dyadic/network-targeted econometric methods
- It must be research-oriented and paper-anchored.
- It must explain when network-targeted methods are needed beyond the methods already taught in Lectures 1–5.

Empirical-methods defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only
- if you merge week-specific bibliography entries into `references.bib`, deduplicate repeated BibTeX entries

Required chapter structure:
1. Learning Objectives
2. Opening Orientation
3. Core points
4. Bridge
5. Field Core
6. Methods Box
7. Research Lab
8. Reading Ladder And References
9. Exercises And Discussion Prompts
10. Reproducibility And Code Lab Note
11. Slide Companion Note
12. Bridge Forward

Lecture requirements:
- include the key conceptual and mathematical objects:
  - linear-in-means / reflection formulation
  - potential outcomes under interference
  - exposure mappings
  - saturation-design intuition
  - dyadic dependence and dyadic-robust inference
- explain what each method identifies, its assumptions, its failure modes, and practical use cases
- tie each major issue to a strong paper students can use as a template
- emphasize that network definition itself is substantive

Methods Box requirements:
- create a dedicated Methods Box for network-targeted methods
- it should cover:
  - exposure mappings
  - randomization inference / permutation logic where relevant
  - dyadic-robust variance estimation / inference under dyadic dependence
  - leave-one-out peer measures and reflection caveats
  - graph- or saturation-based experimental designs
- keep it practical rather than fully technical, but do not stay vague

Slides requirements:
- create the Lecture 19 slide deck under the canonical path:
  `books/empirical-methods/slides/week19/19-causal-inference-with-network-data.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the reflection problem
  - one slide on interference / exposure mappings
  - one slide on network-targeted econometric methods
  - one slide on dyadic inference
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week19/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper for a labor-relevant network/peer-effects design
- use one challenge/extension paper that introduces either explicit network interference or referral-network design
- keep the lab student-facing and concrete
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `smoke.sh`
  - `src/`
  - `output/reproduced/`
  - `output/transfer/`
  - reduced or synthetic teaching-path data if needed
- do not invent replication packages
- be conservative if replication availability is uncertain

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 19 slides from the canonical path
3. if a bounded Lecture 19 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 19 slides compile from the canonical path
5. whether the Lecture 19 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
