Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/sources/05-social-norms-bargaining-and-institutions-shaping-gendered-work.md, @books/special-topic3-gender/assets/tables/05-norms-and-methods-taxonomy.md, @books/special-topic3-gender/assets/tables/05-bargaining-and-institutions-map.md, @books/special-topic3-gender/assets/tables/05-margins-and-evidence-map.md, and @books/special-topic3-gender/assets/tables/05-frontier-and-reading-map.md.

Goal: turn the Gender Study Week 5 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: special-topic3-gender
- Week: 5
- Canonical chapter path: `books/special-topic3-gender/05-social-norms-bargaining-and-institutions-shaping-gendered-work.md`
- Canonical slide path: `books/special-topic3-gender/slides/week5/05-social-norms-bargaining-and-institutions-shaping-gendered-work.tex`
- Canonical lab path: `books/special-topic3-gender/labs/05-social-norms-bargaining-and-institutions-shaping-gendered-work/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/05-social-norms-bargaining-and-institutions-shaping-gendered-work.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/05-social-norms-bargaining-and-institutions-shaping-gendered-work.md`
2. `books/special-topic3-gender/slides/week5/05-social-norms-bargaining-and-institutions-shaping-gendered-work.tex`
3. `books/special-topic3-gender/labs/05-social-norms-bargaining-and-institutions-shaping-gendered-work/lab.md`
4. `books/special-topic3-gender/labs/05-social-norms-bargaining-and-institutions-shaping-gendered-work/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 5 into the book

Special-topic conventions to preserve:
- include a clearly visible **Core points** box near the top
- do **not** add a default Extension box
- use linked citations only in prose markdown
- use the course-local bibliography
- keep edits minimal and reviewable

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- Use real citation keys from `books/special-topic3-gender/references.bib`.
- Slides must live only under `books/special-topic3-gender/slides/week5/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week5/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Content requirements:
- Follow the established structure:
  1. short opening orientation,
  2. Core points box,
  3. Bridge,
  4. Field Core,
  5. Research Lab,
  6. reading ladder / references block.
- Keep the week focused on how **social norms**, **bargaining power**, and **formal/informal institutions** shape gendered work.
- Organize norms from a **methodological perspective**, not as a bucket of examples.
- Distinguish clearly between:
  1. **norms as preference/identity shifters**;
  2. **norms as beliefs about sanctions, reputation, or acceptability**;
  3. **norms as coordination devices in marriage, job search, and local labor markets**;
  4. **norms embedded in formal institutions or organizational rules**;
  5. **bargaining and threat-point channels**.
- Echo the institutions course logic: make explicit what counts as a **formal institution** and what counts as an **informal institution**, and how the two interact.
- Include a brief theoretical bargaining subsection with a gender margin. It can be compact, but it must be explicit.
- Students should leave the lecture able to separate:
  - norms from prices,
  - norms from pure legal constraints,
  - norms from selection,
  - bargaining channels from pure preferences,
  - and formal institutions from informal ones.

Substantive emphasis:
- This should be one of the most literature-rich weeks in the course.
- Use **at least 15 high-quality papers** across the chapter and reading ladder.
- Include both classic and recent frontier papers.
- Norm examples may include breadwinning, caregiving, competition, self-promotion, acceptable jobs, mobility/commuting, authority, and work-family expectations, but the narrative should stay mechanism-first.
- Make clear which papers speak to:
  - labor-force participation,
  - hours and specialization,
  - household bargaining,
  - education and labor-market investments,
  - job search / mobility / commuting,
  - workplace competition / authority,
  - formal legal institutions interacting with norms.

Required conceptual objects:
- one compact taxonomy of norms and institutions;
- one brief bargaining framework with a gender margin;
- one formal vs informal institution distinction;
- one framework showing how a norm changes a labor-market margin through beliefs, sanctions, bargaining, or coordination;
- one explicit bridge back to Week 2 and Week 3 and forward to Week 6.

Suggested bargaining object:
- A simple household or worker decision problem in which a norm term or sanction enters either utility, the feasible set, or the threat point.
- The point is not a full theorem but a clean way to show how gender norms alter labor supply, specialization, or career choices even when wages move.

Methods requirements:
- Explicitly distinguish:
  - migrant / second-generation / ancestry designs for culture transmission,
  - norm-misperception interventions,
  - household/bargaining designs,
  - historical-origin designs,
  - labor-market experiments on competition or job entry,
  - commuting/job-search revealed-preference designs,
  - cross-country legal-institutions evidence.
- Do not present empirical results without naming the identifying variation and the labor margin observed.

Empirical anchors to use:
Foundational / framing:
- `[@goldin2014grandGenderConvergence]`
- `[@lundbergPollak1996bargainingDistributionMarriage]`
- `[@jayachandran2021socialNormsBarrierEmployment]`

Culture / norms / labor supply:
- `[@fernandezFogli2009beliefsWorkFertility]`
- `[@fernandez2013evolutionFemaleLaborForceParticipation]`
- `[@alesinaGiulianoNunn2013originsGenderRoles]`
- `[@bertrandKamenicaPan2015genderIdentityRelativeIncome]`
- `[@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]`
- `[@bernhardtFieldPandeRigolSchanerTroyerMoore2018maleSocialStatus]`
- `[@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount]`

Marriage market / aspirations / labor investments:
- `[@bursztynFujiwaraPallais2017actingWife]`
- `[@andrewCattanCostaDiasFarquharsonKraftKrutikova2025revealedBeliefsMarriageMarket]`

Competition / workplace norms / mobility:
- `[@floryLeibbrandtList2015competitiveWorkplaces]`
- `[@bertrandGoldinKatz2010dynamicsGenderGapProfessionals]`
- `[@leBarbanchonRathelotRoulet2021commuteWageTradeoff]`

Formal institutions interacting with norms:
- `[@hylandDjankovGoldberg2020genderedLawsWorkforce]`

Lab requirements:
- Build the week around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]`
- Secondary / challenge anchor: `[@bertrandKamenicaPan2015genderIdentityRelativeIncome]`
- Optional extension anchor: `[@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount]` or `[@leBarbanchonRathelotRoulet2021commuteWageTradeoff]`
- The bounded student path must run locally without confidential microdata.
- The smoke test should only run the bounded pedagogical path.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and why norms/institutions matter for labor,
  2. Week 2 -> Week 5 bridge,
  3. formal vs informal institutions,
  4. methodological taxonomy of norms,
  5. brief bargaining framework with a gender margin,
  6. breadwinner / caregiving / marriage-market norms,
  7. competition / acceptable jobs / commuting / mobility,
  8. formal laws interacting with norms,
  9. empirical designs and what they identify,
  10. bridge to Week 6 policy incidence.

Implementation notes:
- If you add Week 5 to `index.md` or `myst.yml`, do so in the same style as the existing weeks.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- If any prose markdown still contains bare or backticked citations, normalize them to linked citations.
- Do not refer to a Week 6 identity/hierarchy lecture. In this course sequence, Week 6 is not an identity/hierarchy lecture. The forward bridge should point to the actual Week 6 policy-oriented material only.

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 5 slides compile from the canonical path.
4. Week 5 lab smoke test passes

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
