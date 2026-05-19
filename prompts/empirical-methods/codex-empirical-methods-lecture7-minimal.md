Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/06-when-and-why-structure-static-and-dynamic-decision-problems.md if it exists

If helpful, also inspect:
- the Lecture 7 source pack if it exists in the repo
- nearby empirical-methods lectures for chapter-structure consistency
- any existing slides/lab folders for Lecture 7

Goal: create or refresh Lecture 7 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs.

Canonical output files:
- `books/empirical-methods/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.md`
- `books/empirical-methods/slides/week7/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.tex`
- `books/empirical-methods/labs/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit/`

Use these as the intellectual source of truth:
1. the course outline and block architecture
2. the lecture-specific source markdown / bibliography / tables for Lecture 7 if they exist in the local workspace
3. the design conventions established in earlier empirical-methods lectures

This is a chapter/slides/lab drafting task using the established empirical-methods workflow.

Non-negotiable lecture identity:
- Lecture 7 is the second lecture of Block 2: Structural Estimation.
- It must explain how researchers take a structural model to data credibly.
- It must stay research-oriented:
  - what variation identifies the primitives
  - which moments/likelihood pieces carry the identifying power
  - when moments are enough and when full likelihood is worth the cost
  - how simulation enters estimation
  - how to judge fit and counterfactual credibility
  - how to estimate variance and report uncertainty transparently
- Necessary equations are required. They should illustrate the mathematics behind:
  - likelihood-based estimation
  - GMM / method of moments
  - simulated method of moments
  - indirect inference intuition
  - optimal weighting matrices
  - asymptotic variance
  - bootstrap / resampling logic
  - delta-method logic for functions of parameters

Special course conventions to preserve:
- linked citations only in prose markdown
- course-local bibliography only: `books/empirical-methods/references.bib`
- `Opening Orientation`
- `Core points` box
- `Bridge`
- `Field Core`
- `Research Lab`
- `Methods Box`
- `Reading Ladder And References`
- `Exercises And Discussion Prompts`
- `Reproducibility And Code Lab Note`
- `Slide Companion Note`
- `Bridge Forward`

Required Field Core content:
A. Identification in structural models: observed variation vs latent primitives
B. Likelihood, moments, GMM, SMM, and indirect inference
C. Weighting matrices, overidentification, and targeted moments
D. Fit, validation, counterfactual discipline, and transparent reporting
E. Variance estimation and inference:
   - Hessian / information matrix
   - OPG / sandwich logic
   - delta method
   - bootstrap
   - cluster bootstrap or resampling when dependence matters
   - simulation error and numerical approximation issues
   - two-step / generated-regressor variance concerns when relevant
F. Practical decision rules:
   - when likelihood is preferable
   - when moments are preferable
   - when simulation is unavoidable
   - when fit is convincing or not

Required equations / math:
- generic likelihood objective
- sample moment condition objective / GMM criterion
- simulated method of moments criterion
- indirect inference intuition via auxiliary statistics
- asymptotic variance sketch for GMM / M-estimation
- delta-method approximation for a counterfactual function of estimated parameters
- bootstrap logic for empirical distribution of an estimator

Theory-to-applied requirement:
- include a clearly labeled section or subsection that shows how a structural estimation problem becomes an applied economics paper
- use high-quality anchor papers to show:
  - the economic question
  - the identifying variation
  - why moments/likelihood/simulation were chosen
  - how fit was assessed
  - what counterfactuals were credible
  - how uncertainty was reported

Strong anchor papers to use if feasible:
- Rust (1987)
- Nevo (2000 or 2001)
- Berry, Levinsohn, and Pakes (1995) or a practical exposition built around it
- Todd and Wolpin (2006)
- Low, Meghir, and Pistaferri (2010)
- Adda, Dustmann, and Stevens (2017)
- Keane (2010) or Aguirregabiria and Mira (2010) as overview / orientation
- include implementation-oriented references for variance/inference if useful
Be conservative if exact replication availability is uncertain.

Variance / inference requirement:
- make bootstrapping and other variance estimators explicit, not a footnote
- discuss when asymptotic formulas are fragile
- discuss dependence / clustering issues when simulated or panel-based moments are used
- discuss practical tradeoffs between computational cost and inferential reliability

Slides requirements:
- create the Lecture 7 slide deck under the canonical path
- use the same professional default beamer workflow as elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on identification in structural models
  - one slide on likelihood vs moments vs simulation
  - one slide on weighting matrices and targeted moments
  - one slide on fit / validation / counterfactual discipline
  - one slide on bootstrap / delta method / variance estimation
  - one slide on theory-to-applied examples
  - one slide on limitations / credibility threats
  - one slide on the Research Lab design
- do not create duplicate slide files outside `slides/week7/`

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose one primary anchor that is pedagogically realistic for a bounded teaching reproduction of estimation/fit/inference logic
- choose one challenge / transfer anchor that illustrates dynamic or lifecycle structure and the role of moments/simulation
- it is acceptable to use a reduced synthetic pedagogical path if full official replication materials are uncertain or unavailable
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `smoke.sh`
  - `src/`
  - `output/reproduced/`
  - `output/transfer/`
  - reduced or synthetic teaching-path data if needed
- be conservative about official replication availability
- do not overclaim exact replication if the teaching path is pedagogical

Implementation notes:
- make the implementation caveats concrete, not vague prose
- every method discussed should come with usable implementation details or explicit caveats
- emphasize that structural credibility comes from the full chain:
  identification -> estimation -> fit -> counterfactual discipline -> inference
- preserve consistency with the empirical-methods course architecture

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 7 slides from the canonical path
3. if the Lecture 7 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 7 slides compile from the canonical path
5. whether the Lecture 7 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
