Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic7-labor-design/index.md
- @books/special-topic7-labor-design/OUTLINE.md
- @books/special-topic7-labor-design/myst.yml
- @books/special-topic7-labor-design/references.bib
- @books/special-topic7-labor-design/03-contracts-incentives-screening-and-moral-hazard.md if it exists

Goal: draft Week 4 of the Labor Market Design, Contracting, and Mechanism Design course as a polished chapter, matching the established special-topic workflow and conventions.

Canonical output files:
- `books/special-topic7-labor-design/04-assignment-wages-platforms-and-pricing-rules.md`
- `books/special-topic7-labor-design/slides/week4/04-assignment-wages-platforms-and-pricing-rules.tex`
- `books/special-topic7-labor-design/labs/04-assignment-wages-platforms-and-pricing-rules/`

Use these input materials as the intellectual source of truth:
- `special_topic7_labor_design_week4_edit_pack/source/04-assignment-wages-platforms-and-pricing-rules.md`
- `special_topic7_labor_design_week4_edit_pack/bibliography/04-assignment-wages-platforms-and-pricing-rules.bib`
- all markdown files under `special_topic7_labor_design_week4_edit_pack/tables/`

Non-negotiable course conventions:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown, e.g. `[@pallais2014inefficient]`
- course-local bibliography only:
  `books/special-topic7-labor-design/references.bib`
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
1. Keep the lecture labor-focused, even when discussing algorithms and platforms.
2. Introduce a compact theoretical framework in which an intermediary/platform chooses:
   - visibility / ranking rules
   - matching / assignment rules
   - wage / price / commission rules
   - monitoring / evaluation rules
   and explain how those choices affect allocation, bargaining power, risk, and worker welfare.
3. Make clear that platform and wage rules can improve information and reduce frictions, but can also shift surplus or risk onto workers.
4. Include a theory-to-applied bridge showing how algorithm design questions become empirical labor papers.
5. Include a dedicated methodology box on frontier experimental designs in this area, such as:
   - platform A/B tests
   - randomized information / reputation disclosure
   - randomized recommendation / guarantee / ranking interventions
   - wage-floor or pay-rule experiments
   - natural experiments from platform policy changes or rule redesigns
   - survey / conjoint / lab-in-the-field designs to study platform preferences, fairness, or algorithm aversion
6. Keep the applied papers central. Theory should organize the lecture, not dominate it.
7. Make room for both:
   - online labor markets and hiring platforms
   - gig / ride-hailing / platform work settings
8. Treat this week as a frontier lecture on assignment, pricing, and platform governance in labor markets.

Slides requirements:
- create the Week 4 slide deck under the canonical path:
  `books/special-topic7-labor-design/slides/week4/04-assignment-wages-platforms-and-pricing-rules.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the intermediary objective / algorithmic-rule framework
  - one slide on assignment / visibility / ranking
  - one slide on wages / prices / commissions / transparency
  - one slide on worker welfare / flexibility / risk
  - one slide on frontier experimental methods
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week4/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic7-labor-design/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- use one primary anchor paper that turns a platform-rule or assignment-rule change into a clear applied labor design
- use one challenge / extension paper that illustrates either:
  - platform steering / ranking
  - wage / pay-rule design
  - or worker welfare on platforms
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
- Suggested empirical anchors include Pallais (2014), Barach and Horton (2019/2021), Horton-Johari-Kircher (2024), Stanton and Thomas (2021), Chen et al. on flexibility in ride-hailing, Davis and Samaniego de la Parra (2024), Arnold-Quach-Taska (2025), and other high-quality frontier platform papers where appropriate.
- Keep the distinction clear between:
  (i) assignment / visibility rules,
  (ii) wage / pricing rules,
  (iii) platform governance / risk allocation,
  (iv) worker welfare and flexibility.
- If the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily.

Validation:
1. run a strict build:
   `cd books/special-topic7-labor-design && conda run -n research jupyter book build --html --strict`
2. compile the Week 4 slides from the canonical path
3. if a bounded Week 4 lab path is created, ensure it follows the standard folder structure
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Core points box and methods/theory-to-applied sections are present
5. whether the Week 4 slides compile from the canonical path
6. whether the strict build passes
7. any manual follow-up points
