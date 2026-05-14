Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/06-monopsony-measurement-and-sources-of-power.md, @books/labor-ii/assets/tables/06-monopsony-concepts-map.md, @books/labor-ii/assets/tables/06-measurement-and-identification-map.md, @books/labor-ii/assets/tables/06-sources-of-monopsony-power-map.md, and any existing Week 6 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 6 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 6
- Canonical chapter path: `books/labor-ii/06-monopsony-measurement-and-sources-of-power.md`
- Canonical slide path: `books/labor-ii/slides/week6/06-monopsony-measurement-and-sources-of-power.tex`
- Canonical lab path: `books/labor-ii/labs/06-monopsony-measurement-and-sources-of-power/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/06-monopsony-measurement-and-sources-of-power.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/06-monopsony-measurement-and-sources-of-power.md`
2. `books/labor-ii/slides/week6/06-monopsony-measurement-and-sources-of-power.tex`
3. `books/labor-ii/labs/06-monopsony-measurement-and-sources-of-power/lab.md`
4. `books/labor-ii/labs/06-monopsony-measurement-and-sources-of-power/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 6 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week6/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week6/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on monopsony, the measurement of monopsonistic power, and the sources of monopsony power; do not drift into the full institutions/policy block or the later minimum-wage and union lectures.
- This should be one of the heavier Labor II weeks: a full 3-hour core chapter with a substantial optional 75--90 minute extension block.
- Include at least:
  - one clean definition of monopsony as employer wage-setting power,
  - one contrast between classic one-firm monopsony and modern dynamic/search monopsony,
  - one labor-supply-to-the-firm object,
  - one markdown / marginal cost of labor object,
  - one section on why concentration is not the same thing as monopsony,
  - one section on the sources of monopsony power,
  - one empirical-design section,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 5 and forward to Week 7.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Keep the lecture cleanly structured even though it spans theory, measurement, and empirical evidence.

Methods requirements:
- Explicitly distinguish:
  - labor supply elasticity to the firm vs market labor supply,
  - markdowns vs firm wage premia vs rent-sharing,
  - concentration proxies vs causal evidence on market power,
  - classic static monopsony vs search-based/dynamic monopsony,
  - sources of power rooted in frictions/preferences vs sources rooted in employer concentration,
  - reduced-form merger or policy evidence vs structural measurement of labor market power.
- Do not present empirical results without naming the identifying variation, the unit of observation, the margin observed, and the key unobserved object.
- The chapter should be explicit about measurement problems, including why different monopsony measures need not agree numerically even when they point in the same conceptual direction.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@dubeJacobsNaiduSuri2020`.
- Secondary / challenge anchor: `@yehMacalusoHershbein2022`.
- Optional extension anchor: `@pragerSchmitt2021`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be unusually explicit about:
  1. what monopsony object each paper is measuring,
  2. whether the identifying variation comes from wages, concentration, mergers, or production-side moments,
  3. what key object remains unobserved,
  4. how to transfer the design to a public or synthetic setting such as online-task data, a stylized employer concentration panel, or a simulated plant markdown panel.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course repositioning,
  2. Week 5 to Week 6 bridge,
  3. what monopsony is and is not,
  4. classic monopsony versus modern dynamic/search monopsony,
  5. labor supply to the firm and wage-setting power,
  6. markdowns, marginal cost of labor, and measurement,
  7. concentration, outside options, and why proxies can mislead,
  8. empirical designs and what they identify,
  9. sources of monopsony power,
  10. frontier extension: new data, mergers, policy shocks, and unresolved measurement issues,
  11. bridge to Week 7 and the policy block.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 6 slides compile from the canonical path
4. Week 6 lab smoke test passes

Important implementation notes:
- If you add Week 6 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1--5 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/06-monopsony-course-map.png`
  - `assets/figures/06-classic-vs-modern-monopsony.png`
  - `assets/figures/06-labor-supply-to-the-firm.png`
  - `assets/figures/06-markdown-measurement-map.png`
  - `assets/figures/06-sources-of-monopsony-power.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
