Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/15-curating-maps-and-spatial-data.md if it exists
- @books/empirical-methods/16-causal-inference-with-spatial-data.md if it exists

If helpful, also inspect:
- the Lecture 17 source pack if it exists in the repo
- the Lecture 17 slide file if it exists
- the Lecture 17 lab folder if it exists

Goal: create or refresh Lecture 17 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/17-spatial-structural-modeling.md`
- `books/empirical-methods/slides/week17/17-spatial-structural-modeling.tex`
- `books/empirical-methods/labs/17-spatial-structural-modeling/`

Use these input materials as the intellectual source of truth if they exist:
- `empirical_methods_lecture17_edit_pack/source/17-spatial-structural-modeling.md`
- `empirical_methods_lecture17_edit_pack/bibliography/17-spatial-structural-modeling.bib`
- all markdown files under `empirical_methods_lecture17_edit_pack/tables/`

This is a lecture-drafting / sync task using the established empirical-methods conventions.

Non-negotiable Lecture 17 identity:
- The lecture must stay methods-focused and research-oriented.
- The lecture must explain when equilibrium spatial models are necessary rather than optional.
- It must connect reduced-form place effects to structural objects like moving costs, commuting costs, local productivity, amenities, rents, and welfare.
- It must include gravity-style models as a subfamily of spatial structural work, not as the whole lecture.
- It must include a separate summary component for the whole spatial methods block:
  - where the literature is now
  - what the main active frontiers are
  - what future opportunities look like

Required structure:
1. Opening Orientation
2. Core points
3. Bridge
4. Field Core
5. Research Lab
6. Methods Box
7. Reading Ladder And References
8. Exercises And Discussion Prompts
9. Reproducibility And Code Lab Note
10. Slide Companion Note
11. Bridge Forward

Required Lecture 17 content:
A. Why equilibrium spatial modeling is sometimes necessary
B. Core spatial equilibrium objects:
   - indirect utility
   - location choice / migration
   - commuting
   - wages and rents
   - amenities
   - housing supply / congestion
   - labor demand / firm location
C. Static vs dynamic quantitative spatial models
D. Gravity-style trade / commuting / migration blocks as one family of tractable equilibrium structure
E. Identification, calibration, estimation, fit, and counterfactual interpretation
F. Summary of the spatial methods block:
   - what Lectures 15–17 together give students
   - where the literature currently is
   - frontier opportunities / open research questions

Slides requirements:
- create the Lecture 17 slide deck under the canonical path:
  `books/empirical-methods/slides/week17/17-spatial-structural-modeling.tex`
- use the same professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the core equilibrium map
  - one slide on when reduced-form is not enough
  - one slide on gravity-style building blocks
  - one slide on identification / calibration / fit
  - one slide on the spatial methods block summary
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week17/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that is central to spatial structural equilibrium
- use one challenge/extension paper that pushes into dynamic or frontier spatial modeling
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

Implementation notes:
- keep the lecture methods-focused, not a generic spatial economics lecture
- preserve the distinction between:
  (i) curating spatial data
  (ii) causal inference with space
  (iii) structural equilibrium in space
- the summary of the spatial block should be a separate extra component, not a substitute for the core spatial structural lecture
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 17 slides from the canonical path
3. if a bounded Lecture 17 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 17 slides compile from the canonical path
5. whether the Lecture 17 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
