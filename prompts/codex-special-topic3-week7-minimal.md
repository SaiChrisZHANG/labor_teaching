Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/05-social-norms-bargaining-and-institutions-shaping-gendered-work.md if it exists, and @books/special-topic3-gender/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md if it exists.

Also read these editable inputs for Week 7:
- `bibliography/07-violence-safety-mobility-and-labor-market-access.bib`
- `source/07-violence-safety-mobility-and-labor-market-access.md`
- all table markdown files in `tables/`

Goal: turn the Gender Study Week 7 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Gender Study
- Week: 7
- Canonical chapter path: `books/special-topic3-gender/07-violence-safety-mobility-and-labor-market-access.md`
- Canonical slide path: `books/special-topic3-gender/slides/week7/07-violence-safety-mobility-and-labor-market-access.tex`
- Canonical lab path: `books/special-topic3-gender/labs/07-violence-safety-mobility-and-labor-market-access/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/07-violence-safety-mobility-and-labor-market-access.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any are introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/07-violence-safety-mobility-and-labor-market-access.md`
2. `books/special-topic3-gender/slides/week7/07-violence-safety-mobility-and-labor-market-access.tex`
3. `books/special-topic3-gender/labs/07-violence-safety-mobility-and-labor-market-access/lab.md`
4. `books/special-topic3-gender/labs/07-violence-safety-mobility-and-labor-market-access/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 7 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use linked citation syntax in prose markdown: `[@citekey]`.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Every special-topics chapter must contain a clearly visible **Core points** box near the top.
- Do not add a default Extension box. If frontier material is surfaced, do it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic3-gender/slides/week7/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week7/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Key lecture logic:
- Keep Week 7 distinct from Week 6.
- Week 6 is a policy-incidence lecture about which labor-market margins gender policies move and who bears incidence.
- Week 7 is not a policy shop. It is about **safety, violence, mobility, and reproductive autonomy as constraints on the feasible set and on worker welfare**.
- Reproductive access (birth control, abortion access, fertility treatment / IVF) should be treated here as access-to-work / timing / option-set margins, not just as policy debates.
- The chapter should explain how hidden harms enter labor economics through participation, search, job acceptance, occupation choice, mobility, quits, retention, sorting, and welfare.
- Include a short bridge back to Week 6 where appropriate, but do not let Week 7 collapse into another policy lecture.

Content requirements:
- Follow the established Bridge / Field Core / Research Lab structure.
- Treat safety as a labor-market constraint and welfare object, not a separate social issue.
- Include at least:
  - one explicit feasible-set / utility / search-margin framing,
  - one workplace-harassment / workplace-violence block,
  - one domestic-violence / intimate-partner-violence block,
  - one commuting / public-space safety / mobility block,
  - one reproductive-autonomy block covering birth control, abortion access, and IVF/fertility-treatment access,
  - one reporting / hidden-harm / measurement discussion,
  - four tables,
  - a real reading ladder with citations,
  - a clear bridge back to Week 6 and forward to Week 8.
- Keep the lecture longer and richer than an ordinary week.
- Use the provided tables if they fit; improve captions/labels if needed, but keep paths stable.

Research focus requirements:
- The lecture must feel like a frontier field lecture, not a generic social-problems lecture.
- Show students how researchers actually study:
  - invisible harms,
  - reduced mobility / constrained search,
  - workplace sorting under harassment risk,
  - labor-market consequences of domestic violence,
  - reproductive autonomy as a timing / feasible-set margin.
- Make room for recent and high-interest work, including the recent office-relationships paper as one workplace-harassment / workplace-power angle.
- Explain where the main identification challenges are and what kinds of data help.

Methods requirements:
- Explicitly distinguish:
  - safety as a price/disutility margin,
  - safety as a mobility/search margin,
  - safety as a retention/exit margin,
  - safety as a hidden welfare margin not fully visible in wages/employment,
  - reproductive autonomy as a timing/control margin.
- Identify the actual research designs used:
  - administrative linkage,
  - randomized mobility/transport interventions,
  - legal/judicial quasi-experiments,
  - IV using fertility treatment,
  - workplace survey + admin linkages,
  - boundary/policy discontinuities when relevant.
- Do not present results without naming the identification strategy and the labor margin observed.

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `@adamsPrasslHuttunenNixZhang2024`.
- Secondary / challenge anchor: `@folkeRickne2022`.
- Optional extension anchor: `@macdonaldMontonenNix2025`.
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why Week 7 is distinct from Week 6,
  2. safety and reproductive autonomy as labor constraints,
  3. domestic violence / intimate-partner violence,
  4. workplace harassment / workplace violence,
  5. mobility, commuting, and public-space safety,
  6. birth control, abortion access, and IVF as labor-market timing/control margins,
  7. hidden harms, reporting, and welfare,
  8. research designs and what they identify,
  9. bridge to Week 8.

Important implementation notes:
- If you add Week 7 to `index.md` or `myst.yml`, do so in the same style the course already uses.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 7 slides compile from the canonical path
4. Week 7 lab smoke test passes

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
