Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/04-search-matching-turnover-and-unemployment.md, @books/labor-ii/assets/tables/04-search-objects-map.md, @books/labor-ii/assets/tables/04-flows-separations-and-margins-map.md, @books/labor-ii/assets/tables/04-identification-and-evidence-map.md, and any existing Week 4 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 4 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 4
- Canonical chapter path: `books/labor-ii/04-search-matching-turnover-and-unemployment.md`
- Canonical slide path: `books/labor-ii/slides/week4/04-search-matching-turnover-and-unemployment.tex`
- Canonical lab path: `books/labor-ii/labs/04-search-matching-turnover-and-unemployment/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/04-search-matching-turnover-and-unemployment.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/04-search-matching-turnover-and-unemployment.md`
2. `books/labor-ii/slides/week4/04-search-matching-turnover-and-unemployment.tex`
3. `books/labor-ii/labs/04-search-matching-turnover-and-unemployment/lab.md`
4. `books/labor-ii/labs/04-search-matching-turnover-and-unemployment/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 4 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week4/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week4/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on search, matching, turnover, unemployment, job-to-job mobility, and on-the-job search; do not drift into a full bargaining lecture or into later monopsony material.
- This should be one of the heaviest weeks in the course: a full 3-hour core chapter with a substantial optional extension block.
- Include at least:
  - one matching-function object,
  - one flow-balance / steady-state unemployment derivation,
  - one section centered on separations, turnover, and churning,
  - one section centered on job-to-job transitions and on-the-job search,
  - one section centered on unemployment duration, search intensity, and the consequences of unemployment,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 3 and forward to Week 5.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Keep the lecture cleanly structured even though it is broad.

Methods requirements:
- Explicitly distinguish:
  - worker flows vs job flows,
  - separations vs layoffs vs job destruction vs churning,
  - unemployment-to-employment vs employment-to-unemployment vs job-to-job transitions,
  - unemployed search vs on-the-job search,
  - matching efficiency vs changes in job-seeker composition,
  - observed duration dependence vs causal duration effects vs dynamic selection,
  - reduced-form hazard evidence vs structural search interpretation.
- Do not present empirical results without naming the identifying variation, the unit of observation, the margin observed, and the most important unobserved object.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@hallSchulhoferWohl2018`.
- Secondary / challenge anchor: `@haltiwangerHyattKahnMcEntarfer2018`.
- Optional extension anchor: `@huckfeldt2022`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be unusually explicit about:
  1. which transition margin is being measured,
  2. which hazard or flow object is being approximated,
  3. what the limitations are relative to the original paper,
  4. how to transfer the design to a public CPS/JOLTS-style setting or a small synthetic job-ladder dataset.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 3 to Week 4 bridge,
  3. why search frictions matter,
  4. matching function, worker-side hazards, and vacancy-side hazards,
  5. flow unemployment and steady-state accounting,
  6. separations, turnover, layoffs, job destruction, and churning,
  7. job-to-job transitions, on-the-job search, and job ladders,
  8. unemployment duration, search intensity, and unemployment effects,
  9. empirical designs and what they identify,
  10. frontier extension: beliefs, digital search data, selective hiring, mismatch, and scarring,
  11. bridge to Week 5 wage-setting.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 4 slides compile from the canonical path
4. Week 4 lab smoke test passes

Important implementation notes:
- If you add Week 4 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1--3 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/04-search-course-map.png`
  - `assets/figures/04-worker-flows-and-hazards.png`
  - `assets/figures/04-beveridge-matching-efficiency.png`
  - `assets/figures/04-separation-churning-jobladder.png`
  - `assets/figures/04-unemployment-duration-and-scarring.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
