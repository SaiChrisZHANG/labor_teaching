Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib
- @books/special-topic7-labor-design/02-recruiting-congestion-timing-and-unraveling.md if it exists
- @books/special-topic7-labor-design/03-contracts-incentives-screening-and-moral-hazard.md if it exists

If helpful, also inspect:
- the Week 3 source pack if it exists in the repo
- the Week 3 slide file if it exists
- the Week 3 lab folder if it exists

Goal: create or refresh Week 3 of the Labor Market Design, Contracting, and Mechanism Design course as a fully synchronized week with canonical chapter, slides, and lab outputs, matching the established special-topics workflow.

Canonical output files:
- `books/special-topic7-labor-design/03-contracts-incentives-screening-and-moral-hazard.md`
- `books/special-topic7-labor-design/slides/week3/03-contracts-incentives-screening-and-moral-hazard.tex`
- `books/special-topic7-labor-design/labs/03-contracts-incentives-screening-and-moral-hazard/`

Use these as the intellectual source of truth:
1. the existing canonical chapter file if it already exists:
   `books/special-topic7-labor-design/03-contracts-incentives-screening-and-moral-hazard.md`
2. if available, the week pack files under:
   - `special_topic7_labor_design_week3_edit_pack/source/`
   - `special_topic7_labor_design_week3_edit_pack/bibliography/`
   - `special_topic7_labor_design_week3_edit_pack/tables/`

This is a sync-and-complete task, not a fresh rewrite unless required.

Special-topics defaults to enforce:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only:
  `books/special-topic7-labor-design/references.bib`
- preserve the established special-topics chapter architecture

Required chapter structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading Ladder And References
7. Exercises And Discussion Prompts
8. Reproducibility And Code Lab Note
9. Slide Companion Note
10. Bridge Forward

Week 3 identity to preserve:
- start from a principal-agent framework to formalize effort, hidden action, hidden type, commitment problems, multitasking, and risk-sharing
- keep the employment relationship and within-firm incentive design visible at all times
- connect theory to applied labor research with concrete high-quality papers
- include a dedicated methods box on how the literature measures or elicits effort, commitment, type, and incentive response
- keep the lecture labor-focused rather than generic contract theory

Non-negotiable intellectual additions:
1. Principal-agent core
- The chapter must include a concise but explicit principal-agent framework:
  effort is costly and imperfectly observed; output depends on effort and noise; contracts trade off incentives, risk-sharing, multitasking distortions, and information revelation.
- Multitasking and relational/subjective evaluation should be visible, not treated as footnotes.

2. Theory-to-applied bridge
- There must be a clear subsection in Field Core on how a contract-theory question becomes an empirical labor paper.
- This should include:
  - what hidden object matters (effort, type, commitment, evaluator favoritism, multitasking, peer effects)
  - what observable margin is used
  - what institutional variation or experimental design identifies the mechanism
  - what labor-market welfare object is relevant

3. Methodology box
- Include a dedicated methods box on how the literature measures or elicits:
  - effort
  - commitment / self-control
  - hidden type
  - subjective evaluation / influence activities
- This box should mention methods such as:
  - output-based administrative data
  - contract-change field studies
  - randomized incentive experiments
  - subjective-evaluation audits / evaluator assignment designs
  - worker surveys linked to admin outcomes
  - digital traces / time-use / attendance records
  - structural estimation when hidden objects are not directly observed

Slides requirements:
- create the Week 3 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week3/03-contracts-incentives-screening-and-moral-hazard.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the principal-agent baseline
  - one slide on screening / hidden type
  - one slide on multitasking / subjective evaluation / relational incentives
  - one slide on theory-to-applied translation
  - one slide on frontier methods for effort, commitment, and hidden objects
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week3/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that turns a contract-theory question into a clear applied labor design
- use one challenge / extension paper that illustrates a different hidden object (e.g. commitment, subjective evaluation, or multitasking)
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

Suggested empirical anchors:
- primary anchor: Lazear (2000) on performance pay and productivity
- challenge / extension anchor: de Janvry et al. (2023) on subjective performance evaluation; or Kaur, Kremer, and Mullainathan on self-control / commitment at work
- if a more practical teaching path is needed, use reduced synthetic data that separate incentive effects from sorting effects

Implementation notes:
- keep the chapter labor-focused
- do not drift into generic mechanism design theory without a labor-market mechanism
- preserve the distinction between:
  (i) contracts that screen hidden types,
  (ii) contracts that elicit hidden effort,
  (iii) contracts that cope with multitasking / subjective evaluation / relational enforcement
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
2. compile the Week 3 slides from the canonical path
3. if the Week 3 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 3 slides compile from the canonical path
5. whether the Week 3 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
