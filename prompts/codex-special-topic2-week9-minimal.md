Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, @books/special-topic2-institutions/08-institutional-reform-implementation-and-labor-market-adjustment.md, @books/special-topic2-institutions/tables/08-*.md, and the Week 9 source-pack inputs in this edit pack.

Goal: turn the Week 9 source pack into a polished chapter package for the institutions course while preserving the course conventions and keeping the editable inputs minimal.

Week identity:
- Course: special-topic2-institutions
- Week: 9
- Canonical chapter path: `books/special-topic2-institutions/09-comparative-and-global-labor-market-institutions.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week9/09-comparative-and-global-labor-market-institutions.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/09-comparative-and-global-labor-market-institutions/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/09-comparative-and-global-labor-market-institutions.bib` into `books/special-topic2-institutions/references.bib`.
2. Deduplicate repeated BibTeX entries if introduced.
3. Keep only one canonical entry per cite key.
4. Do not modify Labor I, Labor II, or other special-topic bibliographies.

Required outputs:
1. `books/special-topic2-institutions/09-comparative-and-global-labor-market-institutions.md`
2. `books/special-topic2-institutions/slides/week9/09-comparative-and-global-labor-market-institutions.tex`
3. `books/special-topic2-institutions/labs/09-comparative-and-global-labor-market-institutions/lab.md`
4. `books/special-topic2-institutions/labs/09-comparative-and-global-labor-market-institutions/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic2-institutions/myst.yml` or `books/special-topic2-institutions/index.md` needed to wire Week 9 into the live book sequence

Non-negotiable special-topic conventions:
- Use valid MyST markdown syntax.
- Use a visible **Core points** box near the top.
- Do NOT add a default Extension box.
- Keep frontier material inside Field Core or Research Lab.
- Use linked citation syntax like `[@key]` in prose markdown.
- Do not use bare `@key` or backticked prose citations.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Slides must live only under `books/special-topic2-institutions/slides/week9/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic2-institutions/slides/week9/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The lecture must remain clearly distinct from Week 8.
- Week 8 was about reform, implementation, and heterogeneous adjustment.
- Week 9 must be comparative and global.
- The organizing question is:
  How do labor-market institutions differ across development settings, welfare states, migration regimes, and global production systems, and which lessons travel across contexts?

Required conceptual structure:
1. Comparative framework
   - formal rules versus effective implementation
   - coverage versus membership versus enforcement
   - institutional complementarities
   - public versus private regulation
   - national institutions versus transnational/global governance
2. Domain structure
   - employment protection / unemployment / welfare-state regimes
   - bargaining coverage and industrial relations systems
   - informality and development settings
   - migration regimes and labor-market integration
   - global supply chains / private labor standards / transnational governance
3. “How to make country-specific evidence matter” methodological/philosophical section or box
   - how to frame a country setting around a mechanism rather than around novelty alone
   - how to map a country into a broader comparative taxonomy
   - how to explain why a country is a useful laboratory for a labor question
   - how to discuss external validity / transportability honestly
   - main critiques:
     * too setting-specific
     * institutional bundles confound mechanism
     * incomparable measurement across countries
     * equilibrium feedback differs across settings
     * legal text is not enough without implementation
4. Comparative welfare / incidence / portability discussion
   - which lessons travel
   - which do not
   - why

The chapter should include:
- opening orientation explaining why this week follows Week 8
- Bridge / Field Core / Research Lab structure
- at least one explicit “Method / framing box” aimed at PhD students who want to use their own country setting
- three or more tables from this pack
- a real reading ladder with citations
- a clear bridge forward to Week 10

Paper requirements:
Use concrete papers, not abstract institutional talk.

Suggested comparative anchors from this pack’s bibliography:
- `@freeman2007LaborMarketInstitutions`
- `@boteroDjankovLaPortaLopezdeSilanesShleifer2004`
- `@blanchardWolfers2000`
- `@ulyssea2020InformalityReview`
- `@beerliPeriRuffnerSiegenthaler2021`
- `@locke2013PromiseLimitsPrivatePower`
- `@distelhorstHainmuellerLocke2017`
- `@guziKahanecMydlikova2021`
- `@allcott2015SiteSelectionBias`
- `@dehejiaPopElechesSamii2015ExternalValidity`

The lecture should show students:
- how comparative evidence changes interpretation of institutional effects
- why similar formal institutions can operate differently across contexts
- how migration regimes and global production systems extend the institutional comparison beyond closed national labor markets
- how to make a country-specific project legible and interesting to non-experts

Methods / empirical requirements:
- Explicitly connect comparative questions to empirical designs:
  - cross-country index construction and its limits
  - within-country reforms with comparative interpretation
  - border / region / firm exposure designs in open labor markets
  - comparative administrative microdata across institutional regimes
  - supply-chain audit / certification / governance data
  - historical-comparative institutional classification
- Do not present results without naming the identifying variation and the observed labor margin.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@boteroDjankovLaPortaLopezdeSilanesShleifer2004`
- Challenge anchor: `@beerliPeriRuffnerSiegenthaler2021`
- Optional extension anchor: `@distelhorstHainmuellerLocke2017`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
The deck should include, at minimum:
1. central question and distinction from Week 8
2. comparative taxonomy of labor-market institutions
3. welfare states, bargaining systems, and institutional complementarities
4. informality and development settings
5. migration regimes and labor-market integration
6. global supply chains and private regulation
7. method / philosophy box: how to make a country-specific setting broadly interesting
8. critics of comparative and country-specific evidence
9. what travels and what does not
10. bridge to Week 10

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 9 slides compile from the canonical path
4. Week 9 lab smoke test passes

Important implementation notes:
- If you add Week 9 to `index.md` or `myst.yml`, do so in the same style used by the other special topics.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- This is not a citation-style audit; just preserve linked citation syntax in any new markdown you create.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
