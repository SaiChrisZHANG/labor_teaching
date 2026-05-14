Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/11-technology-automation-ai-and-labor-market.md, @books/labor-ii/assets/tables/11-technology-margins-map.md, @books/labor-ii/assets/tables/11-evidence-by-margin-and-era.md, @books/labor-ii/assets/tables/11-data-design-and-research-opportunities.md, and any existing Week 11 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 11 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 11
- Canonical chapter path: `books/labor-ii/11-technology-automation-ai-and-labor-market.md`
- Canonical slide path: `books/labor-ii/slides/week11/11-technology-automation-ai-and-labor-market.tex`
- Canonical lab path: `books/labor-ii/labs/11-technology-automation-ai-and-labor-market/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/11-technology-automation-ai-and-labor-market.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/11-technology-automation-ai-and-labor-market.md`
2. `books/labor-ii/slides/week11/11-technology-automation-ai-and-labor-market.tex`
3. `books/labor-ii/labs/11-technology-automation-ai-and-labor-market/lab.md`
4. `books/labor-ii/labs/11-technology-automation-ai-and-labor-market/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 11 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week11/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week11/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Use the exact week title: `Technology, Automation, AI, and Labor Market`.
- Keep the lecture organized around three linked objects:
  1. supply-side effects,
  2. demand-side effects,
  3. market-level equilibrium effects.
- Do not treat the week as a narrow labor-demand lecture and do not let it collapse into a general AI essay.
- This should be one of the longer Labor II weeks: a full 3-hour core chapter with a substantial optional 90 minute extension block.
- Move cleanly from conceptual/theoretical framework to empirical evidence.
- Include all of the following:
  - one task-based production object,
  - one task-allocation or automation-boundary object,
  - one decomposition that distinguishes displacement from productivity / reinstatement / new-task effects,
  - one worker-adjustment or skill-obsolescence object,
  - one reduced-form exposure equation used in the empirical literature,
  - one section on historical perspective,
  - one section on cross-country or global evidence,
  - one section on worker adaptation and labor supply,
  - one section on contemporary AI evidence,
  - one section on data and measurement,
  - one explicit research-frontier section,
  - four figures minimum,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 10 and forward to Week 12.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- The lecture should be disciplined and structured even though it spans historical evidence, robots, AI, worker training, and equilibrium reallocation.

Methods requirements:
- Explicitly distinguish:
  - tasks vs occupations,
  - exposure vs adoption,
  - within-firm evidence vs local-labor-market equilibrium evidence,
  - direct displacement vs indirect productivity/output effects,
  - historical ICT/robot evidence vs very recent AI evidence,
  - skill obsolescence vs skill acquisition,
  - public occupation exposure measures vs actual use or realized treatment,
  - descriptive exposure maps vs causal adoption evidence.
- Do not present empirical results without naming:
  - the identifying variation,
  - the unit of observation,
  - the observed margin,
  - and the key offstage equilibrium margin.
- Be explicit about what each data source can and cannot identify.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@aghionEtAl2025HowDifferentUsesAI`.
- Secondary / challenge anchor: `@acemogluRestrepo2020RobotsJobs`.
- Optional extension anchor: `@brynjolfssonLiRaymond2025GenerativeAIWork`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. whether the design captures supply-side, demand-side, or market-level effects,
  2. whether the technology object is exposure or actual adoption,
  3. what the unit of observation is,
  4. what labor-market margin is observed,
  5. what transfer exercise students should run on a small public or synthetic dataset.
- The transfer exercise should not be a vague “do something with AI.” It should ask students to move one identification or exposure idea to a bounded new setting.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 10 to Week 11 bridge,
  3. why technology is not just a labor-demand topic,
  4. task-based framework: automation, augmentation, and new tasks,
  5. supply-side adjustment: learning, training, and obsolescence,
  6. demand-side evidence: robots, ICT, AI adoption, and vacancies,
  7. market-level equilibrium and reallocation,
  8. historical and global evidence,
  9. AI data and measurement,
  10. frontier research questions,
  11. bridge to Week 12 trade and offshoring.
- The deck can be slightly longer than a standard week if needed, but it must remain cleanly structured.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 11 slides compile from the canonical path
4. Week 11 lab smoke test passes

Important implementation notes:
- If you add Week 11 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1–10 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/11-task-based-technology-framework.png`
  - `assets/figures/11-supply-demand-market-effects.png`
  - `assets/figures/11-technology-adjustment-and-reallocation.png`
  - `assets/figures/11-historical-global-technology-evidence.png`
  - `assets/figures/11-ai-data-and-labor-market-measurement.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
