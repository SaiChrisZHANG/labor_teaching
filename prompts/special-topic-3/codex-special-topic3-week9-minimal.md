Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.md, @books/special-topic3-gender/assets/tables/09-data-design-toolkit-map.md, @books/special-topic3-gender/assets/tables/09-setting-to-methods-map.md, @books/special-topic3-gender/assets/tables/09-empirical-challenges-and-shortfalls-map.md, @books/special-topic3-gender/assets/tables/09-gender-measurement-and-identity-map.md, and @books/special-topic3-gender/assets/tables/09-research-opportunities-map.md.

Goal: turn the Gender Study Week 9 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Gender Study
- Week: 9
- Canonical chapter path: `books/special-topic3-gender/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.md`
- Canonical slide path: `books/special-topic3-gender/slides/week9/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.tex`
- Canonical lab path: `books/special-topic3-gender/labs/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.md`
2. `books/special-topic3-gender/slides/week9/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.tex`
3. `books/special-topic3-gender/labs/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research/lab.md`
4. `books/special-topic3-gender/labs/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 9 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use linked citations only in prose markdown: `[@citekey]`.
- Special-topic convention: include a clearly visible **Core points** box near the top.
- Do not add a default Extension box.
- Slides must live only under `books/special-topic3-gender/slides/week9/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week9/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established opening orientation -> Core points -> Bridge -> Field Core -> Research Lab structure.
- Keep the lecture labor-focused and methods-focused; do not drift into generic econometrics.
- Make the chapter longer and practically useful.
- Include a dedicated section on **empirical challenges and shortfalls in the existing literature**, linked back to earlier substantive weeks.
- Include a practical methods bridge that maps empirical settings to commonly used econometric tools.
- Make explicit that this week is designed to kick-start research careers.

At minimum, the final chapter should include:
1. a taxonomy of data families:
   - matched employer–employee data
   - administrative panels
   - audits and field experiments
   - surveys / expectations data
   - time-use data
   - job postings / text-as-data
   - platform data
   - measurement of gender identity and workplace climate
2. an explicit setting-to-methods section
3. a dedicated empirical challenges / shortfalls section
4. a measurement section on legal categories vs lived treatment, small cells, privacy, and intersectionality
5. a research opportunities section
6. a real reading ladder with citations
7. a clear bridge to the final capstone week

Methods requirements:
- Explicitly distinguish:
  - descriptive gap measurement vs causal identification
  - worker sorting vs firm treatment
  - within-firm vs between-firm gaps
  - incidence vs hidden harms
  - direct outcomes vs welfare objects
- Name actual econometric methods where appropriate, including:
  - event studies / dynamic treatment effects
  - worker and firm fixed-effects decompositions
  - audit / field experiment designs
  - application and search decompositions
  - time-budget decompositions
  - text-classification / text-as-data approaches
  - platform-data within-worker decompositions
- Do not discuss empirical settings without saying what the identifying variation is and what the observed margin is.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@fluchtmannGlennyHarmonMaibom2024]`
- Secondary / challenge anchors: `[@cardCardosoKline2016]`, `[@kuhnShen2023]`
- Optional extension anchors: `[@bakerHalberstamKroftMasMessacar2024]`, `[@cookDiamondHallListOyer2021]`, `[@eames2025]`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why methods matter,
  2. bridge from Weeks 2–8,
  3. taxonomy of data families,
  4. mapping empirical settings to econometric tools,
  5. matched employer–employee and administrative event-study methods,
  6. audits / field experiments / job postings / text,
  7. platform data and hidden harms,
  8. measurement of gender identity, climate, and intersectionality,
  9. empirical challenges and open gaps,
  10. bridge to Week 10 research-design synthesis.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 9 slides compile from the canonical path
4. Week 9 lab smoke test passes

Important implementation notes:
- If you add Week 9 to `index.md` or `myst.yml`, do so in the same style used elsewhere in the special-topic books.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
