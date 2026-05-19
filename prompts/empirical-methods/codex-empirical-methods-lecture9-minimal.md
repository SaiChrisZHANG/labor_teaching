Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/08-equilibrium-structural-work-search-spatial-industry-market-and-policy-counterfactuals.md if it exists
- @books/empirical-methods/09-prediction-regularization-and-applied-measurement.md if it exists

If helpful, also inspect:
- nearby empirical-methods lectures to match structure and tone
- the lecture 9 source pack if it exists in the repo
- the lecture 9 slide file if it exists
- the lecture 9 lab folder if it exists

Goal: create or refresh Lecture 9 of the Empirical Methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/09-prediction-regularization-and-applied-measurement.md`
- `books/empirical-methods/slides/week9/09-prediction-regularization-and-applied-measurement.tex`
- `books/empirical-methods/labs/09-prediction-regularization-and-applied-measurement/`

Use these as the intellectual source of truth if they exist locally:
- `empirical_methods_lecture9_edit_pack/source/09-prediction-regularization-and-applied-measurement.md`
- `empirical_methods_lecture9_edit_pack/bibliography/09-prediction-regularization-and-applied-measurement.bib`
- all markdown files under `empirical_methods_lecture9_edit_pack/tables/`

This is a lecture-drafting / sync task using the established empirical-methods conventions.

Non-negotiable Lecture 9 identity:
- This is not a generic machine-learning lecture.
- It must stay tightly tied to applied economics research.
- The lecture should teach prediction, regularization, and applied measurement as tools for better empirical economics.
- The key question is: when is prediction itself the research object, and when is it an input into measurement or design?
- The lecture must emphasize implementation details and caveats, not just abstract descriptions.
- Methods should be taught through signature economics papers that actually use them.

Required themes:
1. prediction targets, training/test logic, and generalization error
2. regularization (lasso, ridge, elastic net) and tuning
3. model selection, overfitting, and calibration
4. feature engineering and target leakage
5. prediction as measurement in economics (job postings, occupation classification, risk scores, latent outcome proxies)
6. how to decide whether the predictive object is fit for the downstream research question
7. implementation caveats: class imbalance, drift, transportability, instability, fairness, and interpretability

Required equations and math to include:
- train/test risk objective
- penalized loss for lasso / ridge / elastic net
- cross-validation objective
- bias–variance tradeoff intuition
- calibration / prediction-error logic
- optional classification threshold notation if useful

Required structure:
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

Special requirements:
- tie each method to real economics research papers
- include concrete implementation details/caveats whenever a method is introduced
- do not let method descriptions remain vague or purely textual
- show when a method is best used, what it identifies/measures, and what can go wrong
- make clear that ML is not a substitute for design

Suggested paper anchors (if consistent with local materials):
- Mullainathan and Spiess on ML as applied econometrics
- Belloni, Chernozhukov, and Hansen on high-dimensional methods
- Dahlhaus et al. on machine learning for structuring job postings
- Ikudo on machine-learning occupational classification
- one or two applied papers showing prediction used for labor or policy measurement

Slides requirements:
- create the Lecture 9 slide deck under the canonical path:
  `books/empirical-methods/slides/week9/09-prediction-regularization-and-applied-measurement.tex`
- use the same default professional beamer style used elsewhere in the repo
- slides should reflect the lecture structure
- include at minimum:
  - one slide on prediction vs causal design
  - one slide on lasso/ridge/elastic-net math and tuning
  - one slide on economics applications to measurement
  - one slide on implementation pitfalls
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week9/` folder

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary paper where ML is used to build or validate an economic measurement object
- use one challenge/extension paper that pushes on transportability, interpretation, or downstream use
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
- keep the lecture firmly in the applied-economics lane
- be explicit about practical package/workflow choices where useful (for example, sklearn-style regularization and cross-validation), but do not turn the lecture into software documentation
- prioritize economics papers over generic CS examples
- if the lecture already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 9 slides from the canonical path
3. if a bounded Lecture 9 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 9 slides compile from the canonical path
5. whether the Lecture 9 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
