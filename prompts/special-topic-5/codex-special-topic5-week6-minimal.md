Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/myst.yml
- @books/special-topic5-technology/references.bib
- @books/special-topic5-technology/01-technology-tasks-and-labor-market-adjustment-core-frameworks.md if it exists
- @books/special-topic5-technology/02-automation-ai-and-labor-demand.md if it exists
- @books/special-topic5-technology/03-worker-adjustment-skills-training-and-career-transitions.md if it exists
- @books/special-topic5-technology/04-firms-hiring-management-and-organizational-response-to-new-technology.md if it exists
- @books/special-topic5-technology/05-technology-inequality-market-structure-and-labor-market-institutions.md if it exists

Use these as the intellectual source of truth for Week 6 if they exist:
- `special_topic5_technology_week6_edit_pack/source/06-synthesis-frontier-questions-and-student-research-designs.md`
- `special_topic5_technology_week6_edit_pack/bibliography/06-synthesis-frontier-questions-and-student-research-designs.bib`
- all markdown files under `special_topic5_technology_week6_edit_pack/tables/`

Goal: create or refresh Week 6 of the Technology, Innovation, and Labor course as a fully synchronized capstone week with canonical chapter, slides, and lab outputs, matching the established special-topic workflow.

Canonical output files:
- `books/special-topic5-technology/06-synthesis-frontier-questions-and-student-research-designs.md`
- `books/special-topic5-technology/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
- `books/special-topic5-technology/labs/06-synthesis-frontier-questions-and-student-research-designs/`

This is a sync-and-draft task for a capstone week, not a generic recap.

Non-negotiable week identity:
- This is the synthesis / frontier / student-research-design week.
- It must remain a labor-economics capstone, not a generic “future of work” recap.
- It must teach students how to turn technology questions into research designs about labor demand, worker adjustment, firms, market structure, institutions, inequality, and welfare.
- It must make explicit where the literature currently is, where the main open questions are, and how students can enter the field with credible projects.
- It must help students distinguish labor-focused technology research from generic technology studies, IO, macro, or management research.

Special-topics defaults to enforce:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only:
  `books/special-topic5-technology/references.bib`
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

Required Week 6 content:
A. Synthesis of the course into a research architecture:
   - technology margin
   - affected labor outcome
   - worker adjustment channel
   - firm response channel
   - market/equilibrium incidence
   - welfare/distributional object

B. Where the literature is:
   - task-based and automation frameworks
   - worker adjustment / training / skills
   - firm adoption / organization / AI attitudes
   - inequality / rents / institutions / global evidence
   - what is measured well and what is still poorly measured

C. Where the literature is going:
   - generative AI and worker use vs firm adoption
   - complementary organizational change
   - energy / electricity / compute infrastructure and labor
   - outsourcing / global service trade / new geography of work
   - measurement of technology and innovation
   - labor-market power / platform governance / worker voice in technology transitions

D. Research design guidance:
   - how to formulate a labor question rather than a technology question
   - how to choose a technology/adoption/exposure measure
   - how to choose the relevant unit (worker, firm, occupation, establishment, commuting zone, country)
   - how to think about counterfactuals and timing
   - what makes a design persuasive
   - common failure modes in this literature

E. A research opportunities section:
   - concrete project directions students could plausibly pursue
   - should include both empirical and measurement contributions
   - should clearly indicate which questions are saturated vs still open

Slides requirements:
- create the Week 6 slide deck under the canonical path:
  `books/special-topic5-technology/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on the technology→labor research architecture
  - one slide on where the literature is
  - one slide on frontier directions
  - one slide on research design choices
  - one slide on common failure modes
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week6/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic5-technology/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- choose a primary anchor that is central to the field and feasible for a bounded teaching reproduction
- choose a challenge/transfer anchor that pushes to a newer frontier (for example AI, organization, or market structure)
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
- This week should help students launch projects.
- Keep the language practical and research-facing.
- Be explicit about how to make a technology-and-labor paper broadly interesting.
- Distinguish clearly between:
  - technology measure
  - adoption / use / exposure
  - worker outcome
  - firm response
  - equilibrium incidence
  - welfare object

Validation:
1. run a strict build:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. compile the Week 6 slides from the canonical path
3. if a bounded Week 6 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 6 slides compile from the canonical path
5. whether the Week 6 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
