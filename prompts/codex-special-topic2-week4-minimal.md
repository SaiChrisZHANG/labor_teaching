Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic2-institutions/OUTLINE.md, @books/special-topic2-institutions/index.md, @books/special-topic2-institutions/myst.yml, @books/special-topic2-institutions/references.bib, and the files in this edit pack:
- `source/04-worker-voice-collective-action-and-bargaining-institutions.md`
- `bibliography/04-worker-voice-collective-action-and-bargaining-institutions.bib`
- `tables/04-collective-bargaining-concepts-map.md`
- `tables/04-organization-formation-and-coverage-map.md`
- `tables/04-spillovers-and-political-linkages-map.md`
- `tables/04-identification-and-frontier-map.md`

Goal: draft the canonical Week 4 chapter for Special Topic 2 (Labor Markets and Political/Cultural Institutions) from this source pack.

Week identity:
- Course: special-topic2-institutions
- Week: 4
- Canonical chapter path: `books/special-topic2-institutions/04-worker-voice-collective-action-and-bargaining-institutions.md`
- Canonical slide path: `books/special-topic2-institutions/slides/week4/04-worker-voice-collective-action-and-bargaining-institutions.tex`
- Canonical lab path: `books/special-topic2-institutions/labs/04-worker-voice-collective-action-and-bargaining-institutions/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/04-worker-voice-collective-action-and-bargaining-institutions.bib` into `books/special-topic2-institutions/references.bib`.
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
- This week is about worker voice, collective action, bargaining institutions, organization formation, coverage, spillovers, and a brief but explicit political spillover section.
- It should remain a labor-economics lecture, not become a generic political economy lecture.
- It should teach worker organization itself as an equilibrium and institutional object.
- It should explicitly cover both:
  - how unions / worker organizations form,
  - what collective institutions do once they exist.
- It should include political spillovers, but as an extension of labor institutions rather than the dominant focus.

Content requirements:
- Follow the established structure:
  1. opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Keep the lecture longer and more substantial than a standard week if needed.
- Make the comparative and organizational logic explicit.

Narrative backbone:
Use this week’s anchor papers explicitly:
- Jäger, Naidu, and Schoefer, “Collective Bargaining, Unions, and the Wage Structure: An International Perspective” `[@jagerNaiduSchoefer2024]`
- Freeman and Medoff, *What Do Unions Do?* `[@freemanMedoff1984]`
- DiNardo and Lee, “Economic Impacts of New Unionization on Private Sector Employers: 1984–2001” `[@dinardoLee2004]`
- Frandsen, “The Surprising Impacts of Unionization: Evidence from Matched Employer-Employee Data” `[@frandsen2021]`
- Pezold, Jäger, and Nüss, “Labor Market Tightness and Union Activity” `[@pezoldJagerNuss2023]`
- Harju, Jäger, and Schoefer, “Voice at Work” `[@harjuJagerSchoefer2021]`
- Jäger, Schoefer, and Heining, “The German Model of Industrial Relations” `[@jagerSchoeferHeining2022]`
- Fortin, Lemieux, and Lloyd, “Labor Market Institutions and the Distribution of Wages: The Role of Spillover Effects” `[@fortinLemieuxLloyd2021]`
- Freeman, “What Do Unions Do … to Voting?” `[@freeman2003]`
- Feigenbaum, Hertel-Fernandez, and Williamson, “Political Effects of Right-to-Work Laws” `[@feigenbaumHertelFernandezWilliamson2018]`
- Kaplan and Naidu, “Between Government and Market: The Political Economics of Labor Unions” `[@kaplanNaidu2024]`

Formal / conceptual requirements:
The chapter must include at least:
1. a clear distinction among:
- union membership,
- collective bargaining coverage,
- enterprise bargaining,
- sectoral bargaining,
- works councils,
- codetermination / board representation,
- strike threats and collective-action capacity;

2. one explicit section on how worker organizations form, covering:
- worker demand,
- organizing costs,
- employer opposition,
- legal thresholds / certification,
- labor-market tightness,
- institutional design;

3. one explicit wage / rent / coverage section;
4. one explicit voice / governance section;
5. one explicit spillovers section;
6. one explicit brief political spillovers / feedback section;
7. one comparative section linking bargaining regimes to country variation;

8. one pedagogical decomposition or object, for example:
```{math}
:label: eq:collective-surplus-week4
\Delta W = \Delta \pi_{workers} + \Delta \pi_{firms} + \Delta G,
```
or another compact decomposition that helps students think about wages, rents, and governance jointly.

Methods requirements:
- Explicitly distinguish:
  - close certification-election RD,
  - matched employer-employee event studies,
  - bargaining-right / right-to-work reforms,
  - threshold designs for representation institutions,
  - distributional decompositions for spillovers,
  - survey/field evidence on organizing demand.
- Make clear what each design identifies:
  - organization formation,
  - wages,
  - employment/payroll,
  - productivity/governance,
  - spillovers to uncovered workers,
  - voting / political participation.

Field Core requirements:
Move cleanly through:
1. why worker voice institutions arise,
2. what counts as collective institutions,
3. how unions / organizations form,
4. bargaining, wages, rents, and coverage,
5. worker voice, governance, and representation,
6. spillovers and inequality,
7. political spillovers and feedback,
8. comparative regimes,
9. bridge to Week 5.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary anchor: `[@dinardoLee2004]`
- Secondary / challenge anchor: `[@frandsen2021]`
- Spillover extension: `[@fortinLemieuxLloyd2021]`
- Voice / governance extension: `[@harjuJagerSchoefer2021]`
- Political spillover extension: `[@feigenbaumHertelFernandezWilliamson2018]`
- The bounded pedagogical path must run locally without confidential microdata.
- The lab should help students diagnose:
  - treatment on organized units,
  - organization-formation margins,
  - spillovers to uncovered workers,
  - downstream political outcomes.
- Bounded transfer ideas:
  - compare direct and spillover incidence,
  - reinterpret close-election designs through organization formation,
  - separate labor-market and political margins of the same institutional shock.

Slide requirements:
- Use the repo’s Beamer conventions.
- The deck should include, at minimum:
  1. central question and bridge from Week 3
  2. what counts as worker voice / collective institutions?
  3. how organizations form
  4. bargaining, wages, rents, and coverage
  5. voice, governance, and representation
  6. spillovers and inequality
  7. political spillovers and feedback
  8. empirical designs and what they identify
  9. bridge to Week 5

Validation requirements:
1. strict book build:
   `cd books/special-topic2-institutions && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic2-institutions && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 4 slides compile from the canonical path.
4. Week 4 lab smoke test passes.

Important implementation notes:
- If you add Week 4 to `index.md` or `myst.yml`, do so in the same style used by the other books.
- Keep slide sources only under `slides/week4/`.
- Do not leave duplicate slide sources or duplicate chapter files in the book root.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

At the end, report:
- files changed
- whether any bibliography entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
