Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/05-regression-discontinuity-rkd-bunching-and-local-designs.md if it exists

If helpful, also inspect:
- the Lecture 6 source pack if it exists in the repo
- nearby empirical-methods lectures for chapter-structure consistency
- any existing slides/lab folders for Lecture 6

Goal: create or refresh Lecture 6 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs.

Canonical output files:
- `books/empirical-methods/06-when-and-why-structure-static-and-dynamic-decision-problems.md`
- `books/empirical-methods/slides/week6/06-when-and-why-structure-static-and-dynamic-decision-problems.tex`
- `books/empirical-methods/labs/06-when-and-why-structure-static-and-dynamic-decision-problems/`

Use these as the intellectual source of truth:
1. the course outline and block architecture
2. the week-specific source markdown / bibliography / tables for Lecture 6 if they exist in the local workspace
3. the design conventions established in earlier empirical-methods lectures

This is a chapter/slides/lab drafting task using the established empirical-methods workflow.

Non-negotiable lecture identity:
- Lecture 6 is the opening lecture of Block 2: Structural Estimation.
- It must teach structure as a research choice, not as an ideological alternative to design-based work.
- The lecture must explain when structure is needed:
  - latent primitives
  - expectations
  - dynamic incentives
  - policy counterfactuals outside observed support
  - welfare objects not directly observed
  - equilibrium response not recoverable from reduced-form contrasts alone
- The lecture must stay research-oriented:
  - when this method is best
  - what it can identify
  - what it cannot identify
  - how to interpret results
  - where the main credibility threats live
  - what robustness and model-discipline should look like
- Necessary equations are required. They should illustrate the mathematics behind:
  - utility / value functions
  - Bellman recursion
  - latent shocks
  - policy counterfactuals
  - identification/estimation mapping
  - model fit / moments / likelihood logic

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
A. Why structure? What reduced-form methods leave latent
B. Static vs dynamic decision problems
C. States, actions, expectations, and latent heterogeneity
D. What is observed vs what is latent
E. Why counterfactuals and welfare often require structure
F. Major credibility threats:
   - functional form
   - misspecified expectations
   - weakly disciplined latent heterogeneity
   - poor fit off the estimation target
   - identification by assumption rather than by data variation

Required equations / math:
- utility in static discrete choice
- latent utility decomposition
- choice probability / logit-style mapping or CCP intuition
- Bellman equation for a dynamic decision problem
- value of continuing vs stopping / choosing among actions
- moments / likelihood / simulation objective sketch
- simple counterfactual mapping from primitives to policy outcomes

Theory-to-applied requirement:
- include a clearly labeled section or subsection that shows how a structural question becomes an applied economics paper
- use high-quality anchor papers to show:
  - the economic question
  - what is latent
  - why reduced-form is insufficient
  - what the model contributes
  - what the main threats are

Strong anchor papers to use if feasible:
- Rust (1987)
- Hotz and Miller (1993)
- Keane and Wolpin (1997)
- Todd and Wolpin (2006)
- Low, Meghir, and Pistaferri (2010)
- Adda, Dustmann, and Stevens (2017)
- Aguirregabiria and Mira (2010) or Keane (2010) as overview / orientation
Be conservative if exact replication availability is uncertain.

Slides requirements:
- create the Lecture 6 slide deck under the canonical path
- use the same professional default beamer workflow as elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on why structure?
  - one slide on static vs dynamic problems
  - one slide on states / actions / expectations / latent objects
  - one slide with Bellman-style math
  - one slide on estimation strategies (moments / likelihood / simulation)
  - one slide on theory-to-applied examples
  - one slide on limitations / credibility threats
  - one slide on the Research Lab design
- do not create duplicate slide files outside `slides/week6/`

Bibliography requirements:
- merge any missing entries from the lecture-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose one primary anchor that is pedagogically realistic for a bounded teaching reproduction
- choose one challenge / transfer anchor that illustrates dynamic or lifecycle structure
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
- emphasize that structure complements reduced-form work by answering different questions
- keep the lecture grounded in actual papers, not only theory
- make the applied guidance concrete: when structure is worth the cost, and when it is not
- include caveats on interpretation, fit, extrapolation, and model dependence
- preserve consistency with the empirical-methods course architecture

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Lecture 6 slides from the canonical path
3. if the Lecture 6 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Lecture 6 slides compile from the canonical path
5. whether the Lecture 6 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
