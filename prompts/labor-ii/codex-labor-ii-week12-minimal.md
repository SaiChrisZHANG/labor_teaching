Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/12-trade-offshoring-and-labor-market-adjustment.md, @books/labor-ii/assets/tables/12-trade-channels-map.md, @books/labor-ii/assets/tables/12-structural-change-and-transition-map.md, @books/labor-ii/assets/tables/12-global-evidence-and-frontier-map.md, and any existing Week 12 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 12 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 12
- Canonical chapter path: `books/labor-ii/12-trade-offshoring-and-labor-market-adjustment.md`
- Canonical slide path: `books/labor-ii/slides/week12/12-trade-offshoring-and-labor-market-adjustment.tex`
- Canonical lab path: `books/labor-ii/labs/12-trade-offshoring-and-labor-market-adjustment/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/12-trade-offshoring-and-labor-market-adjustment.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/12-trade-offshoring-and-labor-market-adjustment.md`
2. `books/labor-ii/slides/week12/12-trade-offshoring-and-labor-market-adjustment.tex`
3. `books/labor-ii/labs/12-trade-offshoring-and-labor-market-adjustment/lab.md`
4. `books/labor-ii/labs/12-trade-offshoring-and-labor-market-adjustment/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 12 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week12/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week12/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Use the exact week title: `Trade, Offshoring, and Labor Market Adjustment`.
- Keep the lecture organized around three linked objects:
  1. channels through which trade affects labor markets,
  2. trade-induced structural change and transition margins,
  3. evidence, welfare, and frontier questions.
- Do not let the week collapse into a generic trade lecture or a narrow import-competition lecture.
- This should be one of the longer Labor II weeks: a full 3-hour core chapter with a substantial optional extension block.
- Move cleanly from conceptual/theoretical framework to empirical evidence.
- Include all of the following:
  - one local-labor-market trade-exposure object,
  - one decomposition distinguishing import competition, export exposure, offshoring / intermediate-input channels, and structural-change channels,
  - one trade-and-adjustment framework linking sector price changes to wages, unemployment, nonparticipation, and welfare,
  - one structural-change object that clarifies how manufacturing-to-service transitions can arise after trade shocks,
  - one dynamic adjustment or event-study object that distinguishes short-run displacement from long-run reallocation,
  - one section on worker versus place adjustment,
  - one section on manufacturing-to-service transition evidence,
  - one section on global or cross-country evidence,
  - one section on new research directions,
  - four figures minimum,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 11 and forward to Week 13.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- The lecture should stay labor-focused throughout: workers, firms, regions, transitions, and labor-market institutions.

Methods requirements:
- Explicitly distinguish:
  - import competition versus export shocks,
  - goods-trade shocks versus offshoring / services-trade shocks,
  - worker-level, firm-level, and place-level treatment objects,
  - short-run displacement versus long-run adjustment,
  - incumbent-worker transitions versus entrant / returnee margins,
  - reduced-form Bartik / tariff-exposure designs versus structural or dynamic equilibrium approaches,
  - local labor market outcomes versus aggregate welfare statements.
- Do not present empirical results without naming:
  - the identifying variation,
  - the unit of observation,
  - the labor-market margin observed,
  - and the key offstage equilibrium or reallocation margin.
- Be explicit about which papers identify worker losses, which identify place effects, which identify sectoral reallocation, and which speak to aggregate or welfare questions.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@autorDornHanson2013ChinaSyndrome`.
- Secondary / challenge anchor: `@dixCarneiroKovak2017TradeLiberalizationRegionalDynamics`.
- Optional extension anchor: `@dauthFindeisenSuedekum2017TradeManufacturingJobsGermany`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab handout must be explicit about:
  1. which trade channel is being measured,
  2. whether the design identifies worker effects, place effects, or sector effects,
  3. what the key exposure measure is,
  4. what labor-market margins are observed,
  5. what transfer exercise students should run on a small public or synthetic dataset.
- The transfer exercise should not be a vague “do something with trade.” It should ask students to carry one exposure or adjustment idea into a bounded new setting.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and week repositioning,
  2. Week 11 to Week 12 bridge: technology shocks versus trade shocks,
  3. the channel map: import competition, export exposure, offshoring, input-cost, and structural-change channels,
  4. local exposure measures and what they identify,
  5. the China syndrome and U.S. local adjustment,
  6. Brazil and dynamic regional adjustment,
  7. Germany, structural change, and manufacturing-to-services transitions,
  8. offshoring / services trade as a distinct channel,
  9. worker versus place adjustment and welfare,
  10. global evidence and frontier directions,
  11. bridge to Week 13 synthesis.
- The deck can be longer than a standard week if needed, but it must remain cleanly structured.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 12 slides compile from the canonical path
4. Week 12 lab smoke test passes

Important implementation notes:
- If you add Week 12 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1–11 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/12-trade-channels-framework.png`
  - `assets/figures/12-trade-structural-change-transitions.png`
  - `assets/figures/12-trade-adjustment-worker-vs-place.png`
  - `assets/figures/12-trade-global-evidence-and-frontiers.png`
  - `assets/figures/12-trade-welfare-and-reallocation.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
