Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/myst.yml
- @books/special-topic5-technology/references.bib
- @books/special-topic5-technology/01-technology-tasks-and-labor-market-adjustment-core-frameworks.md if it exists
- @books/special-topic5-technology/sources/02-automation-ai-and-labor-demand.md if it exists
- @books/special-topic5-technology/assets/tables/ if relevant
- @books/special-topic5-technology/assets/figures/ if relevant
- @books/special-topic5-technology/assets/scripts/ if relevant
- this week pack files:
  - `source/02-automation-ai-and-labor-demand.md`
  - `bibliography/02-automation-ai-and-labor-demand.bib`
  - all files under `tables/`

Goal: create the Week 2 chapter for `special-topic5-technology` as a polished research-facing lecture on automation, AI, and labor demand.

Canonical output paths:
- chapter:
  `books/special-topic5-technology/02-automation-ai-and-labor-demand.md`
- slides:
  `books/special-topic5-technology/slides/week2/02-automation-ai-and-labor-demand.tex`
- lab folder:
  `books/special-topic5-technology/labs/02-automation-ai-and-labor-demand/`

Course-specific design goals:
- This lecture is one of the core substantive weeks of the course.
- It must remain a labor-economics lecture, not a generic AI lecture.
- It should compare displacement, augmentation, output-demand effects, and new-task creation.
- It should explicitly connect AI/automation research to the broader historical literature on earlier technological change.
- It should help students understand that modern AI work sits inside a longer labor-demand literature, not outside it.
- It should treat measurement as a first-order issue, continuing the theme from Week 1.

Non-negotiable structural conventions:
- include a short opening orientation
- include a clearly visible **Core points** box near the top
- do NOT add a default extension box
- preserve the standard chapter architecture:
  - Bridge
  - Field Core
  - Research Lab
  - Reading Ladder And References
  - Exercises And Discussion Prompts
  - Reproducibility And Code Lab Note
  - Slide Companion Note
  - Bridge Forward
- use linked citations only in prose markdown: `[@key]`
- no bare `@key`
- no backticked prose citations

Bibliography rule:
- merge missing references from the week bibliography into:
  `books/special-topic5-technology/references.bib`
- deduplicate repeated BibTeX entries if needed
- keep one canonical cite key per reference

Required intellectual structure:
1. Start with the labor-demand question:
   - which tasks/workers are displaced?
   - which are augmented?
   - when do productivity/output effects offset displacement?
   - when do new tasks emerge?
2. Keep the lecture centered on labor-demand incidence:
   - occupations
   - establishments/firms
   - industries
   - local labor markets
3. Include a longer section comparing AI/automation research to earlier technological-change literatures.
   This section should be explicit and concrete, not just a paragraph.
   It should compare modern AI/robotics research with earlier work on:
   - mechanization / steam-era labor demand shifts
   - electrification and organizational change
   - computerization / ICT and skill demand
   - long-run occupational churn / technological disruption
4. Make clear what is distinctive about AI and what is not:
   - faster diffusion?
   - cognitive-task exposure?
   - firm-level reorganization?
   - measurement via text/postings/usage data?
   - uncertain general-equilibrium effects?
5. Keep measurement explicit:
   - robot exposure
   - task exposure
   - AI exposure
   - patent/text-based exposure
   - firm adoption measures
   - job-posting / vacancy measures
   - worker-level productivity/use data
6. Keep the lecture labor-focused rather than drifting into macro forecasting or pure technology studies.

Field Core requirements:
- include a compact theoretical backbone with the main demand channels
- include a section on causal incidence and why employment and wages can move differently
- include the historical-comparison section as a real subsection in Field Core
- include a measurement subsection that explains why different technology proxies identify different margins

Research Lab requirements:
- choose one primary paper for reproduction / deep reading
- choose one challenge / extension paper
- make the structure explicit:
  - Reproduce
  - Diagnose
  - Transfer
- prefer papers with realistic public-data or pedagogical replication potential
- if a full public replication package is uncertain, say so conservatively

Slides requirements:
- create the slide source under `slides/week2/`
- use the repo’s established beamer conventions
- slides should not be a dump of the chapter; they should present the lecture logic cleanly
- include the historical-comparison section in slides as one structured contrastive block

Implementation notes:
- keep edits minimal outside the target week
- if needed, update `myst.yml` and `index.md` so the week is wired correctly
- do not let `OUTLINE.md` appear as a live chapter if that is not the existing design
- do not rewrite Week 1 substantively

Suggested anchor references to make sure are used meaningfully if relevant:
- Autor, Levy, and Murnane
- Autor, “Why Are There Still So Many Jobs?”
- Acemoglu and Restrepo, “Automation and New Tasks”
- Acemoglu and Restrepo, “Robots and Jobs”
- Graetz and Michaels
- Acemoglu, Lelarge, and Restrepo
- Brynjolfsson, Li, and Raymond
- Aghion et al. on AI and labor demand
- Deming on technological disruption in the labor market
- Goldin and Katz on historical technology-skill complementarity
- historical mechanization / electrification references from the week bibliography

Validation:
1. run a strict build:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. compile slides if LaTeX tools are available
3. if anything breaks, fix the smallest issue and rerun

At the end, report:
1. files created/changed
2. whether the week was wired into the book
3. which references were merged into `references.bib`
4. what the Research Lab primary/challenge papers are
5. whether the historical-comparison section is explicit in both chapter and slides
6. pass/fail for the strict build
