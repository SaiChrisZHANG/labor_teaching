Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib

If helpful, also inspect:
- the Lecture 4 source pack if it exists in the repo
- the Lecture 4 slide file if it exists
- the Lecture 4 lab folder if it exists

Goal: draft Lecture 4 of the Empirical Methods course as a polished chapter, matching the established portfolio workflow and conventions.

Canonical output files:
- `books/empirical-methods/04-instrumental-variables-2sls-and-instrument-design.md`
- `books/empirical-methods/slides/week4/04-instrumental-variables-2sls-and-instrument-design.tex`
- `books/empirical-methods/labs/04-instrumental-variables-2sls-and-instrument-design/`

Use these input materials as the intellectual source of truth:
- `empirical_methods_lecture4_edit_pack/source/04-instrumental-variables-2sls-and-instrument-design.md`
- `empirical_methods_lecture4_edit_pack/bibliography/04-instrumental-variables-2sls-and-instrument-design.bib`
- all markdown files under `empirical_methods_lecture4_edit_pack/tables/`

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@oreopoulos2006]`
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
1. Teach IV and 2SLS as a design logic, not just a regression recipe.
2. Include the key equations:
   - structural equation
   - first-stage equation
   - reduced-form equation
   - Wald estimand for a single instrument
   - 2SLS projection logic
   - LATE under monotonicity
   - a practical weak-IV diagnostic object
3. Make explicit for IV/2SLS:
   - when the method is best used
   - what it identifies
   - what it does not identify
   - the main implementation caveats
   - how to interpret the resulting estimates
4. Include a substantial section on the classic IV assumptions:
   - relevance
   - exclusion
   - independence / as-good-as-random assignment of the instrument
   - monotonicity
   - the substantive content of the first stage
5. Include a substantial section on limitations:
   - exclusion is not directly testable
   - LATE is local and complier-specific
   - monotonicity may fail or be hard to defend
   - weak instruments
   - many-instrument concerns
   - multiple-instrument weighting/interpretation issues
   - the danger that the instrument’s own economic content is more important than the mechanical estimator
6. Add a dedicated “instrument design gallery” inside the lecture:
   - shift-share / Bartik-style instruments
   - judge/caseworker leniency leave-out instruments
   - historical/legacy data instruments
   - policy eligibility / institutional-rule instruments
   - distance / cost / access instruments
7. For each instrument family, include:
   - one or more signature papers
   - the basic design logic
   - what the first stage means economically
   - the main exclusion threats
   - practical implementation and interpretation caveats
8. Discuss shift-share instruments carefully:
   - quasi-random shocks vs endogenous shares
   - why modern shift-share papers changed practice
   - how inference/clustering should reflect the shock structure
9. Discuss leave-out leniency instruments carefully:
   - why leave-one-out construction is used
   - what random assignment needs to look like
   - why exclusion can still fail if lenient decision-makers affect outcomes through other channels
10. Keep the lecture research-oriented:
   students should leave knowing how to evaluate an instrument and how to design one.
11. Avoid vague method descriptions: every method or instrument family discussed must come with usable implementation details and caveats.

Recommended paper spine:
- Angrist and Krueger on quarter-of-birth / compulsory-schooling style IV
- Card on college proximity
- Oreopoulos on compulsory-schooling LATE and ATE
- Autor, Kostøl, Mogstad, and Setzler on judge-leniency leave-out IV
- Borusyak, Hull, and Jaravel and/or Adão, Kolesár, and Morales on modern shift-share designs
- Acemoglu, Johnson, and Robinson as an example of a historical instrument plus the associated identification debate
- Mogstad, Torgovitsky, and Walters on multiple-instrument 2SLS interpretation
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 4 slide deck under the canonical path:
  `books/empirical-methods/slides/week4/04-instrumental-variables-2sls-and-instrument-design.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on why IV is needed
  - one slide on Wald and 2SLS
  - one slide on exclusion, relevance, independence, monotonicity
  - one slide on weak instruments / many instruments
  - one slide on the instrument design gallery
  - one slide on shift-share
  - one slide on leniency leave-out instruments
  - one slide on historical/distance/policy instruments
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week4/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use Oreopoulos (2006) or Angrist–Krueger as the main reproduction anchor
- use a modern instrument-design paper (judge leniency or shift-share) as the diagnosis anchor
- use another instrument family as the transfer anchor
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
- do not turn it into a generic textbook IV chapter
- preserve the applied-research orientation from the course outline
- the key learning goal is design logic:
  when IV is best, what it identifies, what can go wrong, and how to evaluate whether an instrument is believable
- the “instrument design gallery” should be concrete and paper-anchored
- use equations to clarify, not to overwhelm

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 4 slides from the canonical path
3. if a bounded Lecture 4 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the instrument-design gallery is concrete and paper-anchored
6. whether the limitations of IV are discussed honestly and explicitly
7. whether the Lecture 4 slides compile from the canonical path
8. whether the Lecture 4 lab folder now exists and follows the standard structure
9. whether the strict build passes
10. any manual follow-up points
