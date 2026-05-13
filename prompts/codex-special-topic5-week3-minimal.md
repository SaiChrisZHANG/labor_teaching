Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/myst.yml
- @books/special-topic5-technology/references.bib
- @books/special-topic5-technology/02-automation-ai-and-labor-demand.md if it exists

Goal: draft Week 3 of the Technology, Innovation, and Labor course as a polished chapter, matching the established special-topic workflow and conventions.

Canonical output files:
- `books/special-topic5-technology/03-worker-adjustment-skills-training-and-career-transitions.md`
- `books/special-topic5-technology/slides/week3/03-worker-adjustment-skills-training-and-career-transitions.tex`
- `books/special-topic5-technology/labs/03-worker-adjustment-skills-training-and-career-transitions/`

Use these input materials as the intellectual source of truth:
- `special_topic5_technology_week3_edit_pack/source/03-worker-adjustment-skills-training-and-career-transitions.md`
- `special_topic5_technology_week3_edit_pack/bibliography/03-worker-adjustment-skills-training-and-career-transitions.bib`
- all markdown files under `special_topic5_technology_week3_edit_pack/tables/`

Non-negotiable course conventions:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@autor2015]`
- course-local bibliography only:
  `books/special-topic5-technology/references.bib`
- preserve the established special-topics chapter architecture

Required chapter structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading ladder / references
7. Exercises / discussion prompts if consistent with the book
8. Bridge forward

This week’s intellectual requirements:
1. Keep the lecture centered on the supply side:
   - worker adjustment
   - skills
   - training
   - career transitions
   - welfare costs of displacement
2. Add a dedicated methodological box or subsection on frontier empirical designs used in this literature.
   It should explicitly discuss designs such as:
   - college/major cutoff RD and centralized admissions designs
   - training / retraining evaluations
   - matched employer–employee event studies around technology adoption
   - local labor-market exposure designs linked to training or retirement
   - worker-level patent / task / exposure measures
   - any other strong designs in this literature
3. Add a dedicated section on frictions in worker adjustment related to technology adoption, including:
   - distrust / skepticism
   - inertia / present bias / limited memory where relevant
   - information frictions
   - adjustment costs and switching frictions
   - implications for inequality
4. The chapter should make clear that a labor market can adjust in aggregate while specific workers bear persistent losses.
5. The methodological section should help students see what a strong empirical design looks like in this field, especially because training and skill accumulation are hard to measure.

Slides requirements:
- create the Week 3 slide deck under the canonical path:
  `books/special-topic5-technology/slides/week3/03-worker-adjustment-skills-training-and-career-transitions.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include a methods/design slide and a worker-frictions slide
- do not create duplicate slide files outside the canonical `slides/week3/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic5-technology/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- pick a realistic primary anchor from the week’s papers
- if a second/challenge paper is useful, include it
- keep the lab student-facing and concrete, not a vague methods note

Implementation notes:
- keep the chapter labor-focused, not a generic education or innovation lecture
- do not turn the methods material into a generic econometrics survey
- do not overclaim official replication materials unless clearly known from the repo/user context
- if a paper is a working paper or non-AEA source, cite it conservatively and accurately
- preserve the distinction between:
  (i) early skill/major/training choices,
  (ii) within-firm retraining and adaptation,
  (iii) later-career mobility and welfare costs

Validation:
1. run a strict build:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. compile the Week 3 slides from the canonical path
3. if a bounded Week 3 lab path is created, ensure it follows the standard folder structure
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and methods/frictions sections are present
5. whether the Week 3 slides compile from the canonical path
6. whether the strict build passes
7. any manual follow-up points
