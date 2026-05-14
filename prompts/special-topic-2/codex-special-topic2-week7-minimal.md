Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and these Week 7 inputs:

- source markdown: `source/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.md`
- week bibliography: `bibliography/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.bib`
- tables:
  - `tables/07-persistence-channels-map.md`
  - `tables/07-historical-methods-box.md`
  - `tables/07-historical-data-sources-map.md`
  - `tables/07-frontier-and-reading-map.md`

Goal: turn the Special Topic 2 Week 7 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Labor Markets and Political/Cultural Institutions
- Week: 7
- Canonical chapter path:
  `books/special-topic2-institutions/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.md`
- Canonical slide path:
  `books/special-topic2-institutions/slides/week7/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.tex`
- Canonical lab path:
  `books/special-topic2-institutions/labs/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from the week bibliography into:
   `books/special-topic2-institutions/references.bib`
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key.
3. Do not duplicate citation keys.

Non-negotiable special-topic conventions:
- Use valid MyST markdown syntax.
- Core points box is required near the top.
- Do NOT add a default Extension box.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use linked citation syntax in prose markdown.
- Slides must live only under `books/special-topic2-institutions/slides/week7/`.
- Slide compilation outputs should live alongside the `.tex` source.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Required outputs:
1. `books/special-topic2-institutions/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.md`
2. `books/special-topic2-institutions/slides/week7/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.tex`
3. `books/special-topic2-institutions/labs/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality/lab.md`
4. `books/special-topic2-institutions/labs/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic2-institutions/myst.yml` or `index.md` needed to wire Week 7 into the book

Content requirements:
- Follow the established opening orientation / Core points / Bridge / Field Core / Research Lab structure.
- Treat this as a heavier week with a dedicated methods layer.
- Keep the week labor-focused: historical persistence claims must always be tied to a labor mechanism.
- Make clear the distinction between:
  - persistence through labor coercion and employer power
  - persistence through migration regimes and mobility constraints
  - persistence through land, schooling, local public goods, and occupational structure
  - persistence through networks, information, and political rights that affect labor allocation
- Do not allow the chapter to drift into generic economic history or generic political economy.

Required formal/conceptual content:
- include a clear distinction between:
  - serial correlation / persistent fundamentals
  - path dependence / dynamic increasing returns
  - institutional persistence through concrete labor-market mechanisms
- include one explicit persistence framework or decomposition in words and notation if useful
- include a visible **Methods box** inside the chapter
- include a visible **Historical data sources** section or box
- include a strong warning against overclaiming persistence without a labor mechanism

Required methods coverage:
The Methods box must clearly summarize major historical-identification strategies commonly used in this research area, with representative papers. At minimum cover:
1. border/discontinuity designs from historical institutional boundaries
2. wars/conflicts or abrupt political shocks as treatments
3. regime abolition / liberalization / institutional reform as treatments
4. linked historical census / archival microdata strategies
5. lineage / ancestry / ethnic-share or other persistence proxies when used carefully
6. spatial and historical GIS designs where relevant

Required data-source coverage:
The chapter must identify core data sources used in this area, such as:
- historical census and linked census data
- archives and court/labor-contract records
- school, parish, and local public-goods archives
- cadastral maps, colonial maps, and GIS layers
- war/conflict records and military/defense data
- administrative records and digitized newspapers where relevant

Core paper expectations:
Use the week bibliography and make the lecture feel like a real frontier course, not just a classic-history week. The chapter should visibly engage:
- classic labor-history / coercion anchors
- comparative/global persistence evidence
- at least one or two more recent papers
- methods and data issues as a real research agenda

A strong minimum reading spine should include some combination of:
- @dell2010mita
- @naiduYuchtman2013coercive
- @markevichZhuravskaya2018serfdom
- @aizerBooneLlerasMuneyVogel2020wwii
- @jonesSchmick2025reconstruction
- plus any other relevant frontier/global papers from the week bib

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@dell2010mita`
- Secondary / challenge anchor: `@naiduYuchtman2013coercive`
- Optional extension anchors may include:
  - `@markevichZhuravskaya2018serfdom`
  - `@jonesSchmick2025reconstruction`
- The bounded student path must run locally without confidential data.
- If the original replication materials are too heavy, create a reduced pedagogical path and explain that clearly.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
The deck should use the repo's Beamer conventions and include, at minimum:
1. central question and course reorientation
2. why historical institutions belong in labor economics
3. what counts as persistence and what does not
4. coercion, labor power, and contract enforcement
5. migration regimes, mobility, and occupational structure
6. schooling / public goods / local institutions and labor outcomes
7. methods box: major historical designs
8. data box: where historical labor researchers get data
9. representative papers and research frontier
10. bridge to Week 8

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 7 slides compile from the canonical path
4. Week 7 lab smoke test passes

Important implementation notes:
- If you add Week 7 to `index.md` or `myst.yml`, do so in the same style already used by the book.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Do not rewrite other weeks.
- Preserve linked citation style and the special-topic structure conventions.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
