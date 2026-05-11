Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, @books/special-topic2-institutions/09-comparative-and-global-labor-market-institutions.md, @books/special-topic2-institutions/tables/09-*.md, and the Week 10 source-pack inputs in this edit pack.

Goal: turn the Week 10 source pack into a polished chapter package for the institutions course while preserving the course conventions and keeping the editable inputs minimal.

Week identity:
- Course: special-topic2-institutions
- Week: 10
- Canonical chapter path: `books/special-topic2-institutions/10-synthesis-frontier-questions-and-student-research-designs.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week10/10-synthesis-frontier-questions-and-student-research-designs.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/10-synthesis-frontier-questions-and-student-research-designs/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/10-synthesis-frontier-questions-and-student-research-designs.bib` into `books/special-topic2-institutions/references.bib`.
2. Deduplicate repeated BibTeX entries if introduced.
3. Keep only one canonical entry per cite key.
4. Do not modify Labor I, Labor II, or other special-topic bibliographies.

Required outputs:
1. `books/special-topic2-institutions/10-synthesis-frontier-questions-and-student-research-designs.md`
2. `books/special-topic2-institutions/slides/week10/10-synthesis-frontier-questions-and-student-research-designs.tex`
3. `books/special-topic2-institutions/labs/10-synthesis-frontier-questions-and-student-research-designs/lab.md`
4. `books/special-topic2-institutions/labs/10-synthesis-frontier-questions-and-student-research-designs/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic2-institutions/myst.yml` or `books/special-topic2-institutions/index.md` needed to wire Week 10 into the live book sequence

Non-negotiable special-topic conventions:
- Use valid MyST markdown syntax.
- Use a visible **Core points** box near the top.
- Do NOT add a default Extension box.
- Keep frontier material inside Field Core or Research Lab.
- Use linked citation syntax like `[@key]` in prose markdown.
- Do not use bare `@key` or backticked prose citations.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Slides must live only under `books/special-topic2-institutions/slides/week10/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic2-institutions/slides/week10/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- This is a synthesis and research-design capstone, not a light recap.
- The chapter must integrate the whole course and leave students ready to formulate their own projects.
- It must include a clear philosophical layer answering:
  Why is historical/cultural/institutional labor research a vibrant field worth doing?
- It must give students a systematic answer to the relevance challenge:
  how to explain to others why an institutions/culture/history paper matters for labor economics today.

Required conceptual structure:
1. Course synthesis
   - formal institutions, informal institutions, hierarchy, persistence, reform, and comparative perspective
   - how these objects map into work, wages, bargaining, mobility, inequality, and worker welfare
2. Research architecture
   - choose a labor outcome
   - specify the institutional mechanism
   - define the comparison group / counterfactual
   - assess threats to identification
   - discuss portability / external validity
   - state the welfare or distributional object
3. Philosophical / relevance section or box
   - why historical and cultural labor research is not antiquarian or merely descriptive
   - why institutions and culture remain central to modern labor-market allocation
   - how to defend country-specific or historical settings to non-expert audiences
   - mechanism-first relevance rather than setting novelty alone
   - what makes a setting a useful laboratory for a broader labor question
   - what the main critiques are, and how to answer them honestly
4. Frontier directions
   - where the boundary of labor, development, history, political economy, and culture is currently productive
   - what kinds of linked data, methods, or institutional settings are especially promising
5. Student research design workshop
   - make the chapter genuinely usable for project generation

The chapter should include:
- opening orientation tying the whole course together
- Bridge / Field Core / Research Lab structure
- one explicit “Why this field matters” philosophical box or section
- one explicit research-design template students can actually use
- three or more tables from this pack
- a real reading ladder with citations
- a clear closing bridge to dissertation-quality work and adjacent fields

Paper requirements:
Use concrete papers, not abstract exhortation.
The week should pull from across the course to show what a real institutions-and-labor research agenda looks like.

Suggested anchors from this pack’s bibliography:
- `@freeman2007LaborMarketInstitutions`
- `@macleod2007GreatExpectationsLawEmploymentContracts`
- `@ulyssea2020InformalityReview`
- `@jagerNaiduSchoefer2025CollectiveBargainingReview`
- `@dell2010Mita`
- `@naiduYuchtman2013CoerciveContractEnforcement`
- `@alesinaAlganCahucGiuliano2015FamilyValues`
- `@munshiRosenzweig2006TraditionalInstitutionsModernWorld`
- `@autorDonohueSchwab2004`
- `@almeidaCarneiro2012`
- `@beerliPeriRuffnerSiegenthaler2021`
- `@distelhorstHainmuellerLocke2017`

The lecture should show students how a strong institutions-and-labor project can contribute through:
- a clearly identified labor margin
- a sharp institutional mechanism
- a setting that yields leverage
- credible design rather than broad historical narrative
- portability and comparison
- welfare or distributional relevance

Methods / empirical requirements:
- Include a concise methodological section or box on:
  - when institutional detail is an advantage rather than a narrowness problem
  - how to move from a country/historical setting to a broader labor claim
  - common threats: bundled institutions, implementation differences, survivorship in archives, selection, shifting comparison groups, portability failures
- Connect settings to designs:
  - legal/institutional discontinuities
  - policy reforms
  - archival and historical administrative data
  - cross-region / cross-country comparisons
  - shift-share and network-based strategies
  - linked census / registry / employer-worker datasets
- Do not present “historical relevance” or “cultural relevance” as self-evident; show the mechanism.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@dell2010Mita`
- Challenge anchor: `@naiduYuchtman2013CoerciveContractEnforcement`
- Optional extension anchor: `@beerliPeriRuffnerSiegenthaler2021`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.
- The lab should culminate in a short project memo template or research-design transfer exercise.

Slide requirements:
The deck should include, at minimum:
1. central question and capstone framing
2. synthesis map of the course
3. why institutions/culture/history matter for labor economics now
4. a mechanism-first defense of relevance
5. research architecture: outcome -> mechanism -> design -> welfare
6. portability / external-validity / comparison discussion
7. main critiques and how to answer them
8. frontier directions
9. project memo template
10. closing bridge to dissertation research and adjacent fields

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 10 slides compile from the canonical path
4. Week 10 lab smoke test passes

Important implementation notes:
- If you add Week 10 to `index.md` or `myst.yml`, do so in the same style used by the other special topics.
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
