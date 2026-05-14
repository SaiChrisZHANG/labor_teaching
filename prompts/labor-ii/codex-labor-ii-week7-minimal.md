Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/07-minimum-wages-and-wage-regulations.md, @books/labor-ii/assets/tables/07-employment-debate-map.md, @books/labor-ii/assets/tables/07-global-evidence-map.md, @books/labor-ii/assets/tables/07-wage-law-toolkit-map.md, and any existing Week 7 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 7 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 7
- Canonical chapter path: `books/labor-ii/07-minimum-wages-and-wage-regulations.md`
- Canonical slide path: `books/labor-ii/slides/week7/07-minimum-wages-and-wage-regulations.tex`
- Canonical lab path: `books/labor-ii/labs/07-minimum-wages-and-wage-regulations/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/07-minimum-wages-and-wage-regulations.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/07-minimum-wages-and-wage-regulations.md`
2. `books/labor-ii/slides/week7/07-minimum-wages-and-wage-regulations.tex`
3. `books/labor-ii/labs/07-minimum-wages-and-wage-regulations/lab.md`
4. `books/labor-ii/labs/07-minimum-wages-and-wage-regulations/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 7 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week7/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week7/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on minimum wages, wage regulations, employment effects, global evidence, and broader wage-law literatures; do not drift into the full unions lecture or the later general regulation/enforcement lecture.
- This should be one of the heavier policy weeks in Labor II: a full 3-hour core chapter with a substantial optional 90 minute extension block.
- Include at least:
  - one clean competitive benchmark under a wage floor,
  - one monopsony or frictional benchmark showing why a wage floor need not reduce employment one-for-one,
  - one explicit employment-debate section,
  - one section on hours, hiring, turnover, or reallocation margins,
  - one section on global evidence beyond the United States,
  - one section on wage law beyond minimum wages,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 6 and forward to Week 8.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Keep the lecture cleanly structured even though it spans theory, debates, empirical methods, global evidence, and adjacent wage-law topics.

Methods requirements:
- Explicitly distinguish:
  - wages vs employment vs hours vs turnover vs reallocation,
  - competitive vs monopsony or frictional predictions,
  - case-study / border designs vs national panel or event-study designs,
  - treatment intensity / bite measures vs nominal minimum-wage changes,
  - wage-law compliance vs legal incidence,
  - minimum-wage evidence vs evidence on pay transparency, equal-pay rules, or labor-standards enforcement.
- Do not present empirical results without naming the identifying variation, the unit of observation, the margin observed, and the key unobserved object.
- The chapter should be explicit about why different papers can disagree even when they study the same policy.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@cengizDubeLindnerZipperer2019`.
- Secondary / challenge anchor: `@dubeLesterReich2010`.
- Optional extension anchor: `@engbomMoser2022`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. whether the employment object is headcount, hours, or jobs below a threshold,
  2. what the treatment-intensity or bite object is,
  3. what the main identification challenge is,
  4. how to transfer the design to a small public or synthetic border panel, grouped wage-bin panel, or cross-region policy panel.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 6 to Week 7 bridge,
  3. competitive versus monopsony predictions under a wage floor,
  4. what exactly the employment debate is about,
  5. modern evidence on wages, jobs, hours, and reallocation,
  6. global evidence: U.S., Europe/Germany, and Latin America or emerging markets,
  7. wage law beyond minimum wages,
  8. empirical designs and what they identify,
  9. frontier extension: own-wage elasticities, compliance, and new data,
  10. bridge to Week 8 unions and worker voice.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 7 slides compile from the canonical path
4. Week 7 lab smoke test passes

Important implementation notes:
- If you add Week 7 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1--6 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/07-competitive-vs-monopsony-minimum-wage.png`
  - `assets/figures/07-employment-debate-landscape.png`
  - `assets/figures/07-global-minimum-wage-evidence-map.png`
  - `assets/figures/07-adjustment-margins-under-wage-floors.png`
  - `assets/figures/07-wage-law-toolkit.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
