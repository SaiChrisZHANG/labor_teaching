Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib

If helpful, also inspect:
- the Lecture 5 source pack if it exists in the repo
- the Lecture 5 slide file if it exists
- the Lecture 5 lab folder if it exists

Goal: draft Lecture 5 of the Empirical Methods course as a polished chapter, matching the established portfolio workflow and conventions.

Canonical output files:
- `books/empirical-methods/05-regression-discontinuity-rkd-bunching-and-local-designs.md`
- `books/empirical-methods/slides/week5/05-regression-discontinuity-rkd-bunching-and-local-designs.tex`
- `books/empirical-methods/labs/05-regression-discontinuity-rkd-bunching-and-local-designs/`

Use these input materials as the intellectual source of truth:
- `empirical_methods_lecture5_edit_pack/source/05-regression-discontinuity-rkd-bunching-and-local-designs.md`
- `empirical_methods_lecture5_edit_pack/bibliography/05-regression-discontinuity-rkd-bunching-and-local-designs.bib`
- all markdown files under `empirical_methods_lecture5_edit_pack/tables/`

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@lee2008]`
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
1. Teach RD, RKD, bunching, and related local-threshold designs as a design logic, not as a collection of software commands.
2. Include the key equations:
   - sharp RD estimand as a discontinuity in conditional expectations
   - fuzzy RD as a local Wald ratio
   - local-polynomial weighted least-squares objective or its practical equivalent
   - RKD estimand as a slope discontinuity ratio
   - bunching excess-mass / elasticity logic at a kink or notch
3. Make explicit for RD/RKD/bunching:
   - when the method is best used
   - what it identifies
   - what it does not identify
   - the main implementation caveats
   - how to interpret the resulting estimates
4. Include a substantial modern RD section covering:
   - local polynomial estimation
   - triangular weighting vs other kernels / weights
   - optimal bandwidth choice
   - robust bias correction (`rdrobust` logic)
   - honest inference / smoothness-based intervals (`rdhonest` logic)
   - whether, when, and why to add covariates
   - why high-order global polynomials are discouraged
5. Include a substantial section on time RD and spatial RD:
   - RD with time as running variable
   - how time RD differs from event studies and interrupted time series
   - serial correlation / seasonality / anticipation issues
   - spatial RD with one-dimensional borders and multi-dimensional boundaries
   - what makes geographic continuity assumptions credible or not
6. Include a substantial section on bunching:
   - kinks vs notches
   - the identifying role of the optimization model
   - when bunching is convincing and when it is fragile
7. Keep the lecture research-oriented:
   students should leave knowing how to evaluate an RD-style design and how to choose among local designs.
8. Avoid vague method descriptions: every method or software/tool discussed must come with usable implementation details and caveats.
9. This is the last lecture of Block 1, so include a **separate extra component** (not taking away the main RD time) that summarizes the causal inference block:
   - how selection-on-observables, experiments, DID/event study/synthetic control, IV, and RD deal with SUTVA/interference risks
   - best scenarios for each
   - main strengths and weaknesses
   - a rough credibility / publication-quality hierarchy used in applied economics
   - but make clear that any ranking is heuristic and context-dependent, not mechanical

Recommended paper spine:
- Hahn, Todd, and van der Klaauw for RD identification
- Imbens and Lemieux and/or Lee and Lemieux for RD practice
- Lee (2008) as a canonical applied RD anchor
- Calonico, Cattaneo, and Titiunik on robust bias correction / `rdrobust`
- Armstrong and Kolesár on honest inference / `rdhonest`
- Gelman and Imbens on polynomial pitfalls
- Hausman and Rapson on regression discontinuity in time
- Dell (2010) as a canonical spatial RD application
- Saez (2010) and/or Kleven-style work on bunching
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 5 slide deck under the canonical path:
  `books/empirical-methods/slides/week5/05-regression-discontinuity-rkd-bunching-and-local-designs.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on sharp vs fuzzy RD
  - one slide on local polynomial estimation, bandwidths, and weights
  - one slide on `rdrobust` and `rdhonest`
  - one slide on covariates and polynomial pitfalls
  - one slide on time RD vs event study
  - one slide on spatial RD
  - one slide on RKD and bunching
  - one slide on the causal-inference-block summary
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week5/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use Lee (2008) or another canonical applied RD paper as the main reproduction anchor
- use a modern RD diagnostics / inference paper as the diagnosis anchor
- use either a spatial RD or bunching application as the transfer anchor
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
- do not turn it into a generic textbook RD chapter
- preserve the applied-research orientation from the course outline
- the key learning goal is design logic:
  when RD-style methods are best, what they identify, what can go wrong, and how to evaluate whether a threshold design is believable
- the causal-inference-block summary should be its own short concluding component / box / section and must not crowd out the main RD material
- use equations to clarify, not to overwhelm
- include practical implementation guidance for bandwidth, weights, covariates, clustering, and specification choices

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 5 slides from the canonical path
3. if a bounded Lecture 5 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the modern RD section is concrete and implementation-aware
6. whether time RD, spatial RD, RKD, and bunching are all discussed clearly
7. whether the causal-inference-block summary is present as a separate component
8. whether the Lecture 5 slides compile from the canonical path
9. whether the Lecture 5 lab folder now exists and follows the standard structure
10. whether the strict build passes
11. any manual follow-up points
