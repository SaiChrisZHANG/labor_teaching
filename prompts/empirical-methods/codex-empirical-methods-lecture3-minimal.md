Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib

If helpful, also inspect:
- the Lecture 3 source pack if it exists in the repo
- the Lecture 3 slide file if it exists
- the Lecture 3 lab folder if it exists

Goal: draft Lecture 3 of the Empirical Methods course as a polished chapter, matching the established portfolio workflow and conventions.

Canonical output files:
- `books/empirical-methods/03-did-event-studies-and-synthetic-control.md`
- `books/empirical-methods/slides/week3/03-did-event-studies-and-synthetic-control.tex`
- `books/empirical-methods/labs/03-did-event-studies-and-synthetic-control/`

Use these input materials as the intellectual source of truth:
- `empirical_methods_lecture3_edit_pack/source/03-did-event-studies-and-synthetic-control.md`
- `empirical_methods_lecture3_edit_pack/bibliography/03-did-event-studies-and-synthetic-control.bib`
- all markdown files under `empirical_methods_lecture3_edit_pack/tables/`

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@goodmanBacon2021]`
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
1. Teach DID, event studies, and synthetic control as design logics, not just estimators.
2. Include the key equations:
   - canonical 2x2 DID estimand
   - parallel-trends restriction
   - TWFE event-study specification
   - group-time ATT notation for staggered adoption
   - imputation-style ATT logic for modern DID
   - synthetic-control weighting problem and post-treatment treatment effect
   - a cluster-robust variance estimator at a transparent level
3. Make explicit for each design:
   - when it is best used
   - what it identifies
   - what it does not identify
   - the main implementation caveats
   - how to interpret the resulting estimates
4. Include a substantial section on **modern DID methods**:
   - why staggered TWFE can be biased under heterogeneous effects
   - the logic of the bias (forbidden comparisons / contamination / weighting problems)
   - what Goodman-Bacon decomposition teaches
   - what Sun-Abraham, Callaway-Sant'Anna, and Borusyak-Jaravel-Spiess are correcting
   - practical rules for when each modern estimator is most useful
5. Include a substantial section on **variance and clustering**:
   - serial correlation
   - clustering level choice
   - few-cluster problems
   - wild cluster bootstrap or related practical remedies
   - why standard errors can look precise when the design is not
6. Treat synthetic control as part of the panel comparative-toolkit family connected to DID/event studies, not as an unrelated method.
7. Keep the lecture research-oriented:
   students should leave knowing when these methods are strongest, when they fail, how to defend identification, and how to build a publishable applied project.
8. Avoid vague method descriptions: any method discussed should come with actual usable implementation details and caveats.

Recommended paper spine:
- Card and Krueger as the classical DID anchor
- Bertrand, Duflo, and Mullainathan on serial correlation / inference discipline
- Goodman-Bacon on staggered-DID decomposition
- Callaway and Sant'Anna on group-time ATT estimation
- Sun and Abraham on event-study contamination correction
- Borusyak, Jaravel, and Spiess on imputation-based DID
- Abadie, Diamond, and Hainmueller on synthetic control
- Roth on pre-trends / specification caution
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 3 slide deck under the canonical path:
  `books/empirical-methods/slides/week3/03-did-event-studies-and-synthetic-control.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on 2x2 DID and parallel trends
  - one slide on event studies and dynamic treatment paths
  - one slide on why staggered TWFE can fail
  - one slide comparing modern DID estimators
  - one slide on clustering / serial correlation / inference
  - one slide on synthetic control
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week3/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use Card and Krueger as the main reproduction anchor
- use a modern DID paper (Goodman-Bacon / Callaway-Sant'Anna / Sun-Abraham / BJS) as the diagnosis anchor
- use synthetic control as the transfer/extension anchor when useful
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
- do not turn it into a generic panel-data notes dump
- preserve the applied-research orientation from the course outline
- the key learning goal is design logic:
  when each design is best, what it identifies, what can go wrong, and how to make practical estimation choices
- use equations to clarify, not to overwhelm
- modern DID implementation guidance should be concrete enough that a student could choose an estimator and justify it

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 3 slides from the canonical path
3. if a bounded Lecture 3 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the modern DID section clearly explains the bias corrections and practical rules
6. whether the variance / clustering section is explicit and usable
7. whether the Lecture 3 slides compile from the canonical path
8. whether the Lecture 3 lab folder now exists and follows the standard structure
9. whether the strict build passes
10. any manual follow-up points
