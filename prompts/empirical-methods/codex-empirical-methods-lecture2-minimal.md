Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib

If helpful, also inspect:
- the Lecture 2 source pack if it exists in the repo
- the Lecture 2 slide file if it exists
- the Lecture 2 lab folder if it exists

Goal: draft Lecture 2 of the Empirical Methods course as a polished chapter, matching the established portfolio workflow and conventions.

Canonical output files:
- `books/empirical-methods/02-experiments-and-field-experiments.md`
- `books/empirical-methods/slides/week2/02-experiments-and-field-experiments.tex`
- `books/empirical-methods/labs/02-experiments-and-field-experiments/`

Use these input materials as the intellectual source of truth:
- `empirical_methods_lecture2_edit_pack/source/02-experiments-and-field-experiments.md`
- `empirical_methods_lecture2_edit_pack/bibliography/02-experiments-and-field-experiments.bib`
- all markdown files under `empirical_methods_lecture2_edit_pack/tables/`

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@dufloSaez2003]`
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
1. Start from randomized assignment as a design, not as a statistical ritual.
2. Make the logic of experiments explicit:
   - what randomization guarantees
   - which parameter is identified under which design
   - why compliance, spillovers, attrition, and implementation matter
3. Include the key equations:
   - random assignment independence
   - ATE under complete randomization
   - ITT
   - treatment take-up / first stage under encouragement
   - Wald/LATE logic for randomized encouragement
   - an exposure-mapping or spillover notation at a transparent level
4. Teach experiments through papers:
   - when are experiments the best design?
   - what do field experiments reveal that administrative quasi-experiments may not?
   - what are the limitations?
   - how should results be interpreted?
   - how do scale, external validity, and equilibrium response matter?
5. Include a dedicated theory-to-applied section using high-quality papers.
6. Include a methods/robustness section on:
   - individual vs clustered randomization
   - compliance and take-up
   - attrition and outcome measurement
   - spillovers / interference / saturation
   - power and minimum detectable effects at a conceptual level
   - ethics, implementation, and reproducibility
7. Keep the chapter research-oriented:
   students should leave knowing when experiments are strongest, when they are not enough, and how to turn them into a publishable applied project.

Recommended paper spine:
- Harrison and List as the field-experiment taxonomy anchor
- Duflo and Saez as the encouragement / spillover labor anchor
- Bertrand and Mullainathan as the audit / correspondence design anchor
- Bloom et al. as the firm-level randomized intervention anchor
- Pallais as the platform / labor-market design field experiment anchor
- Crépon et al. as the equilibrium / spillover caution anchor
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 2 slide deck under the canonical path:
  `books/empirical-methods/slides/week2/02-experiments-and-field-experiments.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on what randomization identifies
  - one slide on ITT, take-up, and LATE
  - one slide on audit / correspondence experiments
  - one slide on cluster randomization and spillovers
  - one slide on external validity / scale / equilibrium
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week2/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use Duflo and Saez as the main anchor
- use Crépon et al. or Pallais as a challenge / extension anchor
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
- do not turn it into a generic “RCT good / observational bad” lecture
- preserve the applied-economics orientation from the course outline
- the key learning goal is design logic:
  when experiments are strongest, what they identify, what they do not identify, and how to defend interpretation and robustness
- use equations to clarify, not to overwhelm

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 2 slides from the canonical path
3. if a bounded Lecture 2 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the Lecture 2 slides compile from the canonical path
6. whether the Lecture 2 lab folder now exists and follows the standard structure
7. whether the strict build passes
8. any manual follow-up points
