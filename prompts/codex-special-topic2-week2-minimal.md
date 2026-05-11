Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/02-labor-law-enforcement-and-state-capacity.md`
- `bibliography/02-labor-law-enforcement-and-state-capacity.bib`
- `tables/02-labor-law-dimensions-map.md`
- `tables/02-enforcement-and-state-capacity-map.md`
- `tables/02-identification-and-outcomes-map.md`
- `tables/02-frontier-questions-map.md`

Goal: draft the canonical Week 2 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 2
- Canonical chapter path: `books/special-topic2-institutions/02-labor-law-enforcement-and-state-capacity.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week2/02-labor-law-enforcement-and-state-capacity.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/02-labor-law-enforcement-and-state-capacity/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/02-labor-law-enforcement-and-state-capacity.bib` into `books/special-topic2-institutions/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key.
3. Do not duplicate citation keys.

Non-negotiable course conventions:
- Use valid MyST markdown syntax.
- All prose citations must render as linked citations like `[@citekey]`; do not leave bare `@citekey` or backticked citation keys in prose.
- Inline math in markdown should use `{math}`...`` if needed; do not use `\(...\)` in markdown.
- Include a visible **Core points** box near the top.
- Do NOT add a default Extension box.
- Keep the course labor-focused.
- Use the course-local bibliography as the primary bibliography for this course.

Topic boundary:
- This week is about labor law, enforcement, and state capacity as labor-market institutions.
- It should focus on the labor-market consequences of legal protection, compliance, implementation, and administrative capacity.
- It should not become a generic law-and-economics lecture.
- It should not drift into generic public administration.
- The labor-market connection must remain explicit throughout.

Content requirements:
- Follow the established structure:
  1. opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Make clear distinctions among:
  - law on the books,
  - effective law in practice,
  - enforcement intensity,
  - worker knowledge of rights,
  - realized compliance,
  - labor-market incidence.
- Keep the lecture centered on labor-market outcomes rather than legal doctrine.
- Include the formal–informal margin as one of the core equilibrium margins.

Narrative backbone:
Use this week’s anchor papers explicitly:
- MacLeod on labor law and employment contracts `[@macleod2011]`
- Autor, Donohue, and Schwab on wrongful-discharge laws `[@autorDonohueSchwab2004]`
- Almeida and Carneiro on enforcement and informality `[@almeidaCarneiro2012]`
- Bertrand and Crépon on worker knowledge of labor law `[@bertrandCrepon2021]`
- Amengual on pathways to enforcement `[@amengual2014]`
- Berliner et al. on state capacity and labor rights `[@berlinerGreenleafLakeNoveck2015]`
- Ronconi as an optional frontier measurement anchor `[@ronconi2024]`

Formal / conceptual requirements:
The chapter must include at least:
1. one explicit distinction between legal rules and effective law, for example:
```{math}
:label: eq:effective-law-week2
L^{eff}_{jt} = L^{book}_{jt} \times E_{jt} \times K_{jt},
```
with clear explanation that this is a pedagogical device separating the legal rule, enforcement, and knowledge/implementation margins;

2. one section on labor law as a labor-market object, covering:
- hiring / contract form
- dismissal / employment protection
- wage and hours rules
- mandated benefits
- anti-retaliation / dispute resolution
- inspection / sanction regimes

3. one section on enforcement as a labor-market institution:
- inspectors, courts, sanctions, complaints, bureaucratic reach, discretion
- why enforcement is selective and costly

4. one section on state capacity:
- administrative reach
- territorial heterogeneity
- observability of firms/workers
- complementarity with worker organization or social linkages

5. one section on worker knowledge and implementation:
- legal information,
- awareness of rights,
- why knowledge can be a separate implementation margin from inspection

6. one section on equilibrium margins:
- employment
- wages
- compliance/benefits
- formality vs informality
- firm/worker sorting

Methods requirements:
- Explicitly distinguish:
  - legal adoption/repeal and court-made variation,
  - inspection-access or inspector-allocation designs,
  - worker-information experiments,
  - comparative institutional indices,
  - matched employer–employee or firm-administrative evidence,
  - cross-country state-capacity / labor-rights designs.
- Make clear what each design identifies:
  - law on the books,
  - enforcement,
  - knowledge,
  - or effective compliance.
- Do not present results without naming the observed margin and the identifying variation.

Field Core requirements:
Move cleanly through:
1. why labor law matters in labor economics,
2. labor law on paper vs in practice,
3. enforcement as institution,
4. state capacity and heterogeneity,
5. worker knowledge and implementation,
6. formal–informal margin and incidence,
7. empirical designs and evidence,
8. forward bridge to Week 3.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary anchor: `[@almeidaCarneiro2012]`
- Secondary / challenge anchor: `[@autorDonohueSchwab2004]`
- Optional extension anchor: `[@bertrandCrepon2021]`
- The bounded pedagogical path must run locally without confidential microdata.
- The lab should help students diagnose whether a paper identifies:
  - law,
  - enforcement,
  - worker knowledge,
  - or effective compliance.
- Bounded transfer ideas:
  - apply an inspection/intensity design to another labor standard,
  - compare formalization vs wage incidence margins,
  - compare information vs enforcement as separate implementation treatments.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. central question and bridge from Week 1
  2. law on the books vs law in practice
  3. labor-law dimensions
  4. enforcement as institution
  5. state capacity and heterogeneity
  6. worker knowledge / implementation
  7. informality and equilibrium adjustment
  8. empirical designs and what they identify
  9. bridge to Week 3

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 2 slides compile from the canonical path.
4. Week 2 lab smoke test passes.

Important implementation notes:
- If you add Week 2 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week2/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
