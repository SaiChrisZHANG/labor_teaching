Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/tables/ if relevant, and this week pack:
- `source/08-comparative-and-global-gender-in-labor-market-development.md`
- `bibliography/08-comparative-and-global-gender-in-labor-market-development.bib`
- `tables/08-comparative-regimes-and-mechanisms-map.md`
- `tables/08-global-evidence-map.md`
- `tables/08-country-setting-framing-box.md`
- `tables/08-frontier-and-reading-map.md`

Goal: turn the Week 8 source pack into a polished chapter package for Special Topic 3 (Gender Study).

Week identity:
- Course: `special-topic3-gender`
- Week: 8
- Canonical chapter path:
  `books/special-topic3-gender/08-comparative-and-global-gender-in-labor-market-development.md`
- Canonical slide path:
  `books/special-topic3-gender/slides/week8/08-comparative-and-global-gender-in-labor-market-development.tex`
- Canonical lab path:
  `books/special-topic3-gender/labs/08-comparative-and-global-gender-in-labor-market-development/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/08-comparative-and-global-gender-in-labor-market-development.bib`
   into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key.
3. Do not duplicate citation keys.

Special-topic conventions:
- Every chapter must include a clearly visible **Core points** box near the top.
- Do NOT add a default Extension / Optional Extension box.
- If there is genuine frontier content, surface it inside Field Core or Research Lab.
- Use linked citations in prose markdown only: `[@citekey]`.
- Do not leave bare `@citekey` or backticked prose citations.
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``.
- Use the course-local bibliography.
- Keep edits minimal and reviewable.

Required outputs:
1. `books/special-topic3-gender/08-comparative-and-global-gender-in-labor-market-development.md`
2. `books/special-topic3-gender/slides/week8/08-comparative-and-global-gender-in-labor-market-development.tex`
3. `books/special-topic3-gender/labs/08-comparative-and-global-gender-in-labor-market-development/lab.md`
4. `books/special-topic3-gender/labs/08-comparative-and-global-gender-in-labor-market-development/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 8 into the book

Content requirements:
- Keep the chapter labor-focused, not a generic development or comparative institutions lecture.
- The central question is:
  “Which gender-and-labor mechanisms travel across countries, and which depend on development, institutions, norms, and labor-market structure?”
- The chapter must distinguish clearly between:
  1. portable mechanisms
  2. setting-specific institutional detail
  3. policy transferability vs external validity
- It must include a practical “how to sell country-specific evidence” layer for students with home-country research interests.

Required visible structure:
1. opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references block if already part of the chapter style
7. forward bridge to Week 9 / Week 10 where appropriate

Required substantive elements:
- a comparative framework for cross-country gender-and-labor research
- distinction between labor supply, labor demand, care infrastructure, sectoral structure, formality, mobility, legal regime, and norms
- discussion of what it means for a mechanism to “travel”
- one explicit section on:
  “How to frame country-specific evidence for a broader audience”
- one explicit section on:
  “Common critiques of country-specific comparative work”
- clear use of both classic and recent global/comparative papers
- at least four tables from this pack integrated into the lecture
- a strong research-ladder / project-generation section

Methods / framing requirements:
- Include a clearly labeled box or subsection on how to make country-specific work broadly interesting.
- That section should teach students to:
  - identify the labor mechanism
  - map the country setting into a comparative taxonomy
  - explain why the setting gives leverage
  - distinguish internal validity, transportability, and external validity
  - be explicit about what should and should not generalize
- Also include key critiques:
  - overclaiming generalizability
  - insufficient mechanism articulation
  - country-as-exotic-case framing
  - weak comparison group logic
  - inability to connect to broader labor-market objects

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- Include, at minimum:
  1. central question and why comparative gender research matters
  2. comparative taxonomy of gender-and-labor regimes
  3. portable mechanisms vs setting-specific detail
  4. labor supply, care, and service-sector development
  5. formality, migration, law, and public employment
  6. recent global evidence and frontier work
  7. how to sell country-specific research
  8. critiques and what makes comparative work persuasive
  9. bridge to final synthesis / research design week

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@olivettiPetrongolo2017`.
- Secondary / challenge anchor: `@jayachandran2021`.
- Optional extension anchor: `@goldbergGottliebLallMehta2025ggdi`.
- The bounded student path must run locally without restricted confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 8 slides compile from the canonical path
4. Week 8 lab smoke test passes

Important implementation notes:
- If you add Week 8 to `index.md` or `myst.yml`, do so in the same style already used in the book.
- Keep filenames stable.
- Do not leave duplicate slide sources or duplicate build artifacts in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
