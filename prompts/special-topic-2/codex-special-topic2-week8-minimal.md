Read @AGENTS.md, @docs/repo-workflow.md, @docs/special-topics-roadmap.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, @books/special-topic2-institutions/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.md, @books/special-topic2-institutions/tables/07-*.md, and the Week 8 source-pack inputs in this edit pack.

Goal: turn the Week 8 source pack into a polished chapter package for the institutions course while preserving the course conventions and keeping the editable inputs minimal.

Week identity:
- Course: special-topic2-institutions
- Week: 8
- Canonical chapter path: `books/special-topic2-institutions/08-institutional-reform-implementation-and-labor-market-adjustment.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week8/08-institutional-reform-implementation-and-labor-market-adjustment.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/08-institutional-reform-implementation-and-labor-market-adjustment/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/08-institutional-reform-implementation-and-labor-market-adjustment.bib` into `books/special-topic2-institutions/references.bib`.
2. Deduplicate repeated BibTeX entries if introduced.
3. Keep only one canonical entry per cite key.
4. Do not modify Labor I, Labor II, or other special-topic bibliographies.

Required outputs:
1. `books/special-topic2-institutions/08-institutional-reform-implementation-and-labor-market-adjustment.md`
2. `books/special-topic2-institutions/slides/week8/08-institutional-reform-implementation-and-labor-market-adjustment.tex`
3. `books/special-topic2-institutions/labs/08-institutional-reform-implementation-and-labor-market-adjustment/lab.md`
4. `books/special-topic2-institutions/labs/08-institutional-reform-implementation-and-labor-market-adjustment/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic2-institutions/myst.yml` or `books/special-topic2-institutions/index.md` needed to wire Week 8 into the live book sequence

Non-negotiable special-topic conventions:
- Use valid MyST markdown syntax.
- Use a visible **Core points** box near the top.
- Do NOT add a default Extension box.
- Keep frontier material inside Field Core or Research Lab.
- Use linked citation syntax like `[@key]` in prose markdown.
- Do not use bare `@key` or backticked prose citations.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Slides must live only under `books/special-topic2-institutions/slides/week8/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic2-institutions/slides/week8/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- The lecture must remain clearly distinct from Week 7.
- Week 7 was about persistence and historical path dependence.
- Week 8 must be about institutional reform, implementation, compliance, adaptation, and heterogeneous adjustment.
- The organizing question is:
  Why do similar institutional reforms produce different labor-market effects across places, firms, and workers?

Required conceptual structure:
1. Reform taxonomy:
   - legal reforms
   - enforcement expansions
   - formalization/compliance reforms
   - equal-opportunity / anti-discrimination / transparency reforms
   - administrative or decentralized implementation reforms
2. Transmission framework:
   - legal text
   - worker knowledge / beliefs
   - firm compliance / evasion / adaptation
   - state capacity / local implementation
   - equilibrium adjustment
3. Heterogeneity:
   - by firm size, sector, informality exposure, bargaining environment, worker type, local state capacity, and market structure
4. Welfare:
   - take-up, compliance, incidence, spillovers, inequality, and unintended margins

The chapter should include:
- opening orientation that distinguishes it from Week 7
- Bridge / Field Core / Research Lab structure
- one concise reform-transmission framework, possibly as a conceptual decomposition
- three or more tables from this pack
- a real reading ladder with citations
- a clear bridge forward to Week 9 and Week 10

Paper requirements:
The chapter should use concrete papers, not abstract policy talk.
At minimum, make serious use of these literatures:
- wrongful-discharge / dismissal protection reforms
- labor-law enforcement and implementation
- worker legal knowledge / beliefs
- formalization and compliance reforms
- procedural / transparency / equal-opportunity reforms
- one broader labor-market reform or administrative reform example

Suggested anchor papers from this pack’s bibliography:
- `@autorDonohueSchwab2004`
- `@almeidaCarneiro2012`
- `@bertrandCrepon2021`
- `@ulyssea2018`
- `@goldinRouse2000`
- `@bakerHalberstamKroftMasMessacar2023`
- `@blundellDuchiniSimionTurrell2025`
- `@dustmannFitzenbergerSchonbergSpitzOener2014`
- `@deAndradeBruhnMckenzie2016`

The lecture should make clear why reform effects differ:
- implementation varies
- firms adapt
- workers may not know their rights
- some reforms bind only for certain firm/worker margins
- informality and market structure alter incidence
- equilibrium responses change welfare interpretation

Methods / empirical requirements:
- Explicitly connect reform settings to empirical designs:
  - staggered adoption / event study
  - regression discontinuity or threshold designs
  - randomized information / enforcement interventions
  - border or local exposure designs
  - firm-worker administrative data and distributional analysis
- Do not present results without naming the identifying variation and the observed labor margin.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@bertrandCrepon2021`
- Challenge anchor: `@almeidaCarneiro2012`
- Optional extension anchor: `@bakerHalberstamKroftMasMessacar2023`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
The deck should include, at minimum:
1. central question and distinction from Week 7
2. reform taxonomy
3. reform-transmission framework
4. implementation and worker beliefs
5. firm adaptation and compliance
6. formalization / informality reform margins
7. equal-opportunity / transparency reforms
8. heterogeneity and equilibrium adjustment
9. welfare, spillovers, and frontier questions
10. bridge to Week 9

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 8 slides compile from the canonical path
4. Week 8 lab smoke test passes

Important implementation notes:
- If you add Week 8 to `index.md` or `myst.yml`, do so in the same style used by the other special topics.
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
