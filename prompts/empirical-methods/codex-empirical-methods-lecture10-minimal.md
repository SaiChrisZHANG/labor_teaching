Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/09-prediction-regularization-and-applied-measurement.md if it exists
- @books/empirical-methods/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md if it exists

If helpful, also inspect:
- nearby empirical-methods lectures to match structure and tone
- the Lecture 10 source pack if it exists in the repo
- the Lecture 10 slide file if it exists
- the Lecture 10 lab folder if it exists

Goal: create or refresh Lecture 10 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md`
- `books/empirical-methods/slides/week10/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.tex`
- `books/empirical-methods/labs/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml/`

Use these as the intellectual source of truth if they exist locally:
- `empirical_methods_lecture10_edit_pack/source/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md`
- `empirical_methods_lecture10_edit_pack/bibliography/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.bib`
- all markdown files under `empirical_methods_lecture10_edit_pack/tables/`

This is a lecture-drafting / sync task using the established empirical-methods conventions.

Non-negotiable course conventions:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@chernozhukovDoubleDebiasedMachine2018]`
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
1. Keep the lecture tightly tied to economics research rather than turning it into a generic ML lecture.
2. Teach the partially linear / orthogonal-score logic behind double/debiased ML.
3. Include the key equations:
   - partially linear model
   - nuisance functions for outcome and treatment
   - orthogonal score / residual-on-residual logic
   - cross-fitting / sample-splitting intuition
   - CATE notation
   - a causal-forest / heterogeneous-treatment-effects object
4. Make explicit for high-dimensional controls, DDML, and causal forests:
   - when the method is best used
   - what it identifies
   - what it does not identify
   - the main implementation caveats
   - how to interpret the resulting estimates
5. Include a substantial section on:
   - orthogonalization and why it protects inference from nuisance estimation error
   - sample splitting and cross-fitting
   - post-double selection and the role of lasso for controls
   - treatment-effect heterogeneity and when CATE is substantively meaningful
   - causal forests / generalized random forests as tools for detecting heterogeneity
6. Keep prediction accuracy clearly separate from valid causal inference.
7. Be concrete about practical implementation issues:
   - overlap support
   - feature leakage
   - nuisance-learner choice
   - hyperparameter tuning
   - instability across folds
   - uncertainty for heterogeneous effects
   - honest forests vs adaptive overfitting
8. Use important economics papers as anchors, not generic CS examples.
9. Avoid vague method descriptions: every major method should come with usable implementation details and caveats.
10. Keep a clear research-design perspective: students should leave knowing when these tools help and when they are being abused.

Recommended paper spine:
- Belloni, Chernozhukov, and Hansen on high-dimensional controls / post-double selection
- Chernozhukov et al. on double/debiased machine learning
- Wager and Athey and/or Athey, Tibshirani, and Wager on causal forests / generalized random forests
- Davis and Heller on using causal forests to predict treatment heterogeneity in an economics application
- Dube et al. on monopsony in online labor markets using double machine learning
You may refine the exact paper mix if needed, but preserve the design logic.

Slides requirements:
- create the Lecture 10 slide deck under the canonical path:
  `books/empirical-methods/slides/week10/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the lecture structure
- include:
  - one slide on why high-dimensional controls create new problems
  - one slide on post-double selection
  - one slide on orthogonalization / DML math
  - one slide on cross-fitting
  - one slide on CATE and causal forests
  - one slide on implementation pitfalls
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week10/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary applied-economics paper using causal forests or DML as the main reproduction anchor
- use one challenge/extension paper that pushes on heterogeneity, overlap, or interpretation
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
- keep the lecture methods-focused but not generic
- the main learning goal is correct use: when these tools are helpful, what assumptions do the work, and how to report them credibly
- emphasize that nuisance functions are useful precisely because they are not the parameter of interest
- include practical package/workflow references where useful (for example, DoubleML, EconML, grf), but do not turn the lecture into package documentation
- use equations to clarify, not to overwhelm

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 10 slides from the canonical path
3. if a bounded Lecture 10 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and key equations are present
5. whether the lecture is tied clearly to economics research papers
6. whether implementation caveats are explicit and concrete
7. whether the Lecture 10 slides compile from the canonical path
8. whether the Lecture 10 lab folder now exists and follows the standard structure
9. whether the strict build passes
10. any manual follow-up points
