Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib

If helpful, also inspect:
- the Lecture 1 source pack if it exists in the repo
- the Lecture 1 slide file if it exists
- the Lecture 1 lab folder if it exists

Goal: draft Lecture 1 of the Empirical Methods course as a polished chapter, matching the established portfolio workflow and conventions.

Canonical output files:
- `books/empirical-methods/01-potential-outcomes-identification-logic-and-selection-on-observables.md`
- `books/empirical-methods/slides/week1/01-potential-outcomes-identification-logic-and-selection-on-observables.tex`
- `books/empirical-methods/labs/01-potential-outcomes-identification-logic-and-selection-on-observables/`

Use these input materials as the intellectual source of truth:
- `empirical_methods_lecture1_edit_pack/source/01-potential-outcomes-identification-logic-and-selection-on-observables.md`
- `empirical_methods_lecture1_edit_pack/bibliography/01-potential-outcomes-identification-logic-and-selection-on-observables.bib`
- all markdown files under `empirical_methods_lecture1_edit_pack/tables/`

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@imbensRubin2015]`
- course-local bibliography only:
  `books/empirical-methods/references.bib`
- preserve the established chapter architecture:
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

This lecture’s intellectual requirements:
1. Start from potential outcomes and target estimands.
2. Make the logic of identification explicit:
   - what is observed
   - what is missing
   - what assumption links the two
3. Treat selection-on-observables as a real design rather than a weak default.
4. Include the core equations:
   - potential outcomes notation
   - ATE / ATT / ATC
   - selection bias decomposition
   - conditional independence / overlap
   - regression adjustment / matching / IPW / doubly-robust logic at a transparent level
5. Teach the method through papers:
   - when is selection-on-observables most credible?
   - what parameter is identified?
   - what are the limitations?
   - how should results be interpreted?
   - what robustness/sensitivity work is needed?
6. Include a dedicated theory-to-applied section using high-quality papers.
7. Include a methods/robustness section on:
   - balance diagnostics
   - overlap/common support
   - matching / weighting choices
   - sensitivity to unobservables
   - specification discipline
8. Keep the chapter research-oriented:
   students should leave knowing when this design is strongest, when it is weakest, and how to turn it into a publishable applied project.

Recommended paper spine:
- LaLonde as the design challenge anchor
- Dehejia and Wahba as the matching/selection-on-observables anchor
- Rosenbaum and Rubin as the propensity-score logic anchor
- Oster / Altonji-Elder-Taber / sensitivity-style work as robustness anchors
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 1 slide deck under the canonical path:
  `books/empirical-methods/slides/week1/01-potential-outcomes-identification-logic-and-selection-on-observables.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on target parameters
  - one slide on selection bias decomposition
  - one slide on conditional independence and overlap
  - one slide on matching / weighting / regression adjustment
  - one slide on diagnostics and robustness
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week1/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use LaLonde / Dehejia-Wahba as the main anchor
- if a second/challenge paper is useful, include it
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
- if full original data are not bundled, create a bounded synthetic or reduced pedagogical path

Implementation notes:
- keep the lecture methods-focused but not purely abstract
- do not turn it into a generic econometrics notes dump
- preserve the applied-economics orientation from the course outline
- the key learning goal is design logic:
  when the method is best, what it identifies, what it cannot identify, and how to defend robustness
- use equations to clarify, not to overwhelm

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 1 slides from the canonical path
3. if a bounded Lecture 1 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the Lecture 1 slides compile from the canonical path
6. whether the Lecture 1 lab folder now exists and follows the standard structure
7. whether the strict build passes
8. any manual follow-up points
