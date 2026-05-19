Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md if it exists

If helpful, also inspect:
- the lecture 11 source pack if it exists in the repo
- the lecture 11 slide file if it exists
- the lecture 11 lab folder if it exists

Goal: draft Lecture 11 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs.

Canonical output files:
- `books/empirical-methods/11-causal-ml-policy-learning-and-external-validity.md`
- `books/empirical-methods/slides/week11/11-causal-ml-policy-learning-and-external-validity.tex`
- `books/empirical-methods/labs/11-causal-ml-policy-learning-and-external-validity/`

Use these as the intellectual source of truth if they exist:
- `empirical_methods_lecture11_edit_pack/source/11-causal-ml-policy-learning-and-external-validity.md`
- `empirical_methods_lecture11_edit_pack/bibliography/11-causal-ml-policy-learning-and-external-validity.bib`
- all markdown files under `empirical_methods_lecture11_edit_pack/tables/`

This is a week-drafting / sync task using the established empirical-methods conventions.

Non-negotiable Lecture 11 identity:
- This lecture must be clearly distinct from Lecture 10.
- Lecture 10 covered high-dimensional controls, orthogonalization, DML, and heterogeneity estimation.
- Lecture 11 must focus on what researchers do **after** heterogeneity is estimated:
  - policy learning
  - targeting
  - subgroup discovery
  - welfare/value functions
  - external validity / transportability / distribution shift
  - fairness and deployment constraints
- It must remain a methods-for-applied-economics lecture, not a generic ML lecture.

Core questions the lecture must answer:
1. When is heterogeneity itself the object of interest?
2. When is policy learning the object of interest?
3. What is the difference between estimating CATEs and choosing a policy rule?
4. How do external validity and transportability problems change the interpretation of heterogeneity estimates?
5. How should researchers think about fairness, feasibility, and implementation once targeting rules are proposed?

Required chapter structure:
1. Learning Objectives
2. Opening Orientation
3. Core points box
4. Bridge
5. Field Core
6. Research Lab
7. Methods Box
8. Reading Ladder And References
9. Exercises And Discussion Prompts
10. Reproducibility And Code Lab Note
11. Slide Companion Note
12. Bridge Forward

Required methodological content:
- define CATE / IATE / subgroup effects
- define policy value and regret
- explain empirical welfare maximization / policy learning intuition
- explain uplift / targeting logic
- explain transportability / distribution shift / external validity logic
- distinguish prediction, causal effect estimation, and decision rules
- discuss why the same heterogeneity estimate may not justify the same policy in a new population
- include a compact but explicit “ML section summary” that lists common ML algorithms and where they are most suitable

Required equations / formal objects:
- `tau(x) = E[Y(1)-Y(0) | X=x]`
- policy rule `pi(x)`
- policy value `V(pi) = E[Y(pi(X))]`
- regret `R(pi) = V(pi*) - V(pi)`
- a simple doubly robust / orthogonal score object can be referenced when connecting back to Lecture 10
- a simple transportability / target-weighting idea should appear conceptually or mathematically

ML section summary requirements:
Create a short explicit summary section or boxed component listing common ML algorithms and their most common uses/caveats in applied economics, for example:
- lasso / ridge / elastic net
- random forest / gradient boosting
- causal forests / generalized random forests
- policy trees
- SVM
- neural nets
- clustering methods where relevant
The point is not to teach all of them fully, but to tell students:
- when they are most suitable
- what they are bad at
- what caveats matter in applied work

Important design distinction from Lecture 10:
- Lecture 10 = nuisance control, orthogonalization, valid effect estimation under high dimensionality
- Lecture 11 = turning heterogeneity into decision rules and assessing portability/external validity

Signature paper anchors:
Use real economics papers to anchor the lecture. Prioritize:
- Athey & Wager / Wager & Athey / Athey-Tibshirani-Wager
- Kitagawa & Tetenov
- Athey & Wager on policy learning with observational data
- Bansak et al. on algorithmic assignment / targeting
- Allcott on site selection bias / external validity
- Vivalt / Dehejia-Pop-Eleches-Samii / related transportability work
You may refine the list, but the lecture must be anchored in actual applied economics papers, not just method notes.

Slides requirements:
- create the lecture 11 slide deck under the canonical path
- use the same default professional beamer style as the rest of the empirical methods course
- include:
  - one slide distinguishing Lecture 10 from 11
  - one slide on CATE vs policy rule
  - one slide on policy value / regret
  - one slide on external validity / transportability
  - one slide on fairness / implementation constraints
  - one slide with the ML algorithm quick guide
  - one slide on the Research Lab design

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow:
  Reproduce → Diagnose → Transfer
- use a primary anchor that is central to policy learning or algorithmic targeting
- use a secondary / challenge / extension anchor that raises portability or external-validity concerns
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
- be conservative about replication-package claims

Implementation notes:
- the lecture should be research-oriented rather than a generic ML lecture
- methods discussed in the chapter should always come with usable implementation details and caveats
- keep the difference from Lecture 10 visible throughout
- do not overclaim transportability; be explicit about when external validity is weak
- preserve linked citations only in prose markdown

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 11 slides from the canonical path
3. if the Lecture 11 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 11 slides compile from the canonical path
5. whether the Lecture 11 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
