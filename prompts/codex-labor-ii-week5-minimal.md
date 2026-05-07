Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/05-wage-posting-bargaining-and-wage-setting.md, @books/labor-ii/assets/tables/05-wage-setting-regimes-map.md, @books/labor-ii/assets/tables/05-bargaining-objects-and-observables.md, @books/labor-ii/assets/tables/05-identification-and-pass-through-map.md, and any existing Week 5 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 5 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 5
- Canonical chapter path: `books/labor-ii/05-wage-posting-bargaining-and-wage-setting.md`
- Canonical slide path: `books/labor-ii/slides/week5/05-wage-posting-bargaining-and-wage-setting.tex`
- Canonical lab path: `books/labor-ii/labs/05-wage-posting-bargaining-and-wage-setting/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/05-wage-posting-bargaining-and-wage-setting.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/05-wage-posting-bargaining-and-wage-setting.md`
2. `books/labor-ii/slides/week5/05-wage-posting-bargaining-and-wage-setting.tex`
3. `books/labor-ii/labs/05-wage-posting-bargaining-and-wage-setting/lab.md`
4. `books/labor-ii/labs/05-wage-posting-bargaining-and-wage-setting/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 5 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week5/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week5/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on wage posting, bargaining, outside options, rent-sharing, and wage-setting institutions; do not drift into a full monopsony lecture, a full union/institutions lecture, or the later policy weeks.
- This should be one of the heavier weeks in the course: a full 3-hour core chapter with a substantial optional 75--90 minute extension block.
- Include at least:
  - one clean benchmark contrast between competitive wages and frictional wage setting,
  - one posted-wage object,
  - one bargaining object,
  - one section on outside options / the value of nonemployment,
  - one section on standardized versus discretionary wage-setting regimes inside firms,
  - one explicit bridge from search models to rent-sharing and pass-through evidence,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 4 and forward to Week 6.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Keep the lecture cleanly structured even though it covers multiple wage-setting protocols.

Methods requirements:
- Explicitly distinguish:
  - posted wages vs individualized bargaining vs standardized/administrative wage schedules,
  - reservation wages vs outside offers vs the value of nonemployment,
  - worker outside options vs threat points in bargaining,
  - wage pass-through from firm shocks vs pass-through from outside-option shocks,
  - firm wage premia vs worker sorting vs match-specific rents,
  - reduced-form rent-sharing evidence vs structural wage-setting interpretation.
- Do not present empirical results without naming the identifying variation, the unit of observation, the margin observed, and the key unobserved object.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@lachowskaMasSaggioWoodbury2022`.
- Secondary / challenge anchor: `@massenkoffWilmers2023`.
- Optional extension anchor: `@biasi2021`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be unusually explicit about:
  1. whether the original paper is testing posting, bargaining, or a wage-rule change,
  2. what the observable outside-option or wage-setting margin is,
  3. what the main identification challenge is,
  4. how to transfer the design to a public teacher-contract dataset, a public salary-schedule dataset, or a small synthetic offer-and-separation panel.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 4 to Week 5 bridge,
  3. why search models need a wage-setting protocol,
  4. wage posting and the logic of wage dispersion,
  5. bargaining, outside options, and the Hall--Milgrom critique,
  6. wages and the value of nonemployment,
  7. standardized versus discretionary pay-setting inside firms,
  8. empirical designs and what they identify,
  9. rent-sharing, pass-through, and bridges to market power,
  10. frontier extension: bargaining inequality, worker beliefs, pay transparency, and algorithmic pay-setting,
  11. bridge to Week 6 monopsony and labor market power.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 5 slides compile from the canonical path
4. Week 5 lab smoke test passes

Important implementation notes:
- If you add Week 5 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1--4 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/05-wage-setting-course-map.png`
  - `assets/figures/05-posting-vs-bargaining.png`
  - `assets/figures/05-outside-options-and-wage-setting.png`
  - `assets/figures/05-rent-sharing-pass-through.png`
  - `assets/figures/05-standardized-vs-discretionary-pay.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
