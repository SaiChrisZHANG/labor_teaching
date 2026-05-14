Read @AGENTS.md, @docs/repo-workflow.md, @shared/bibliography/references.bib, @books/labor-ii/OUTLINE.md, @books/labor-ii/index.md, @books/labor-ii/myst.yml, @books/labor-ii/sources/03-personnel-economics-and-internal-labor-markets.md, @books/labor-ii/assets/tables/03-personnel-economics-map.md, @books/labor-ii/assets/tables/03-design-map.md, @books/labor-ii/assets/tables/03-frontier-opportunities-map.md, and any existing Week 3 figures under @books/labor-ii/assets/figures/.

Goal: turn the Labor II Week 3 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor II
- Week: 3
- Canonical chapter path: `books/labor-ii/03-personnel-economics-and-internal-labor-markets.md`
- Canonical slide path: `books/labor-ii/slides/week3/03-personnel-economics-and-internal-labor-markets.tex`
- Canonical lab path: `books/labor-ii/labs/03-personnel-economics-and-internal-labor-markets/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/03-personnel-economics-and-internal-labor-markets.bib` into `shared/bibliography/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `shared/bibliography/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/labor-ii/03-personnel-economics-and-internal-labor-markets.md`
2. `books/labor-ii/slides/week3/03-personnel-economics-and-internal-labor-markets.tex`
3. `books/labor-ii/labs/03-personnel-economics-and-internal-labor-markets/lab.md`
4. `books/labor-ii/labs/03-personnel-economics-and-internal-labor-markets/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/labor-ii/myst.yml` or `books/labor-ii/index.md` needed to wire Week 3 into the book
7. if the week needs schematic figures and they do not yet exist, create them under canonical paths in `books/labor-ii/assets/figures/` without creating extra editable source files unless necessary

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `shared/bibliography/references.bib`.
- Slides must live only under `books/labor-ii/slides/week3/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/labor-ii/slides/week3/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Keep the week focused on personnel economics and internal labor markets; do not drift into search equilibrium, bargaining, monopsony, or full labor-market matching.
- The lecture should make clear where personnel economics sits in Labor II: after static and dynamic labor demand, before search/matching and wage-setting, as the study of how firms organize, motivate, evaluate, assign, and retain workers inside the firm.
- Include at least:
  - one explicit definition or conceptual map of personnel economics,
  - one agency / incentives object,
  - one multitasking, subjective evaluation, or career-incentives discussion,
  - one promotions / assignment / Peter Principle section,
  - one managers, peers, or teams section,
  - one data-and-identification section,
  - one longer extension block on recent research directions, literature gaps, and new opportunities,
  - four figures,
  - three tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 2 and forward to Week 4.
- Use the supplied tables if they fit; if you improve captions or labels, keep paths stable.
- If figures do not yet exist, create simple clean schematic figures at stable canonical paths.
- Treat this as a full 3-hour core chapter with a substantial optional extension block, not a short note.

Methods requirements:
- Explicitly distinguish:
  - firm-side experiments versus quasi-experiments,
  - incentives affecting effort versus incentives affecting selection and sorting,
  - promotions as assignment versus promotions as incentives,
  - manager effects versus peer effects,
  - management-practice measurement versus causal management shocks,
  - remote-work or technology settings where selection and treatment must be separated,
  - internal policy variation versus public policy that changes workplace practices.
- Do not present empirical results without naming the identifying variation, the unit of analysis, the outcome margin observed, and the main external-validity caveat.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@friebelHeinzKruegerZubanov2017`.
- Secondary / challenge anchor: `@bensonLiShue2019`.
- Optional extension anchor: `@emanuelHarrington2024`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and course positioning,
  2. Week 2 to Week 3 bridge,
  3. what personnel economics studies inside firms,
  4. incentives, compensation, and agency,
  5. multitasking, subjective evaluation, and career incentives,
  6. promotions, assignment, and the Peter Principle,
  7. managers, peers, teams, and organizational spillovers,
  8. data, designs, and external-validity concerns,
  9. frontier extension: management, remote work, voice, digital traces, AI, and training,
  10. bridge to Week 4 search, turnover, and unemployment flows.

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 3 slides compile from the canonical path
4. Week 3 lab smoke test passes

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style that Labor II Weeks 1--2 use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/labor-ii/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If you add missing figures, keep their filenames exactly:
  - `assets/figures/03-personnel-economics-in-course-map.png`
  - `assets/figures/03-incentives-assignment-promotion.png`
  - `assets/figures/03-managers-peers-teams.png`
  - `assets/figures/03-data-design-frontier-map.png`
  - `assets/figures/03-research-opportunities-landscape.png`

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
