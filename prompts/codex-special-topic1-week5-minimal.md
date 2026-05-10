Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/sources/05-incentives-contracts-reciprocity-and-workplace-behavior.md, @books/special-topic1-behavioral/assets/tables/05-incentives-monitoring-and-supervision-map.md, @books/special-topic1-behavioral/assets/tables/05-workplace-behavior-frontier-map.md, and @books/special-topic1-behavioral/assets/tables/05-identification-and-design-map.md.

Goal: turn the Behavioral Labor Week 5 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 5
- Canonical chapter path: `books/special-topic1-behavioral/05-incentives-contracts-reciprocity-and-workplace-behavior.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week5/05-incentives-contracts-reciprocity-and-workplace-behavior.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/05-incentives-contracts-reciprocity-and-workplace-behavior/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/05-incentives-contracts-reciprocity-and-workplace-behavior.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/05-incentives-contracts-reciprocity-and-workplace-behavior.md`
2. `books/special-topic1-behavioral/slides/week5/05-incentives-contracts-reciprocity-and-workplace-behavior.tex`
3. `books/special-topic1-behavioral/labs/05-incentives-contracts-reciprocity-and-workplace-behavior/lab.md`
4. `books/special-topic1-behavioral/labs/05-incentives-contracts-reciprocity-and-workplace-behavior/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 5 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVignaListMalmendierRao2022]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week5/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week5/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This week is about incentives, contracts, reciprocity, monitoring, supervision, and workplace behavior inside firms.
- It should stay labor-focused and workplace-focused.
- It should not become a generic behavioral game-theory week, a generic contract-theory week, or a generic management survey.
- The central applications should be:
  - effort under incentive contracts,
  - reciprocity and gift exchange,
  - monitoring and supervision,
  - subjective versus objective evaluation,
  - reference-dependent and loss-framed incentives,
  - performance pay and heterogeneous responses,
  - gaming and unintended consequences of contract design,
  - algorithmic or digital monitoring as a frontier extension.
- It may briefly mention mission/meaning/fairness if useful, but it should remain anchored to workplace incentives and employer–worker interactions.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Use the source-pack arc:
  - benchmark effort and contract problem,
  - incentives plus monitoring,
  - reciprocity and gift exchange,
  - reference-dependent and loss-framed incentives,
  - supervision and subjective evaluation,
  - performance pay, heterogeneity, and sorting,
  - output vs productivity vs gaming,
  - frontier monitoring / algorithmic management.
- Make the chapter concrete. Do not just list behavioral preference types.
- Show students how labor economists actually use these objects in applied workplace research.

Formal / conceptual requirements:
Include at least:
1. one benchmark effort / contract problem:
```{math}
:label: eq:benchmark-effort-week5
\max_{e \ge 0} \; u\!\left(w(y(e))\right) - c(e)
```

2. one behavioral-contract object that makes clear contracts can operate through generosity, framing, reciprocity, and monitoring:
```{math}
:label: eq:behavioral-contract-week5
\max_{e \ge 0} \; u\!\left(w(y(e),m)\right) - c(e) + B\!\left(g_i, r_i, f_i, s_i, m_i; e\right)
```

3. one explicit subjective-evaluation / influence-activity object that distinguishes productive effort from effort aimed at pleasing a supervisor:
```{math}
:label: eq:subjective-evaluation-week5
\max_{e,a \ge 0} \; u\!\left(w\big(z(e), \hat q^S(e,a)\big)\right) - c(e) - \psi(a)
```
where `{math}`a`` denotes influence activity or relationship-building effort directed at the evaluator.

4. one explicit reference-dependent or loss-framed object:
```{math}
:label: eq:loss-framing-week5
U(e) = u\!\left(w(y(e))\right) - c(e) + \lambda \min\{0,\, b(e)-r\}
```

5. one contract-choice / sorting object that distinguishes treatment from selection:
```{math}
:label: eq:contract-sorting-week5
k_i^\star \in \arg\max_{k \in \mathcal{K}} \; \mathbb{E}\!\left[U_i\!\left(w_k(y_i(e),m), e\right)\right]
```

6. one clear distinction between:
  - extra work vs productivity,
  - monitoring vs motivation,
  - objective vs subjective evaluation,
  - stronger incentives vs better organizational outcomes,
  - average effects vs heterogeneous responses.

Empirical anchors to use:
- reciprocity / gift exchange:
  - `[@kubeMarechalPuppe2012]`
  - `[@dellaVignaListMalmendierRao2022]`
- motivation benchmark:
  - `[@dellaVignaPope2018]`
- performance-pay heterogeneity:
  - `[@bandieraFischerPratYtsma2021]`
- loss framing / unintended consequences:
  - `[@hossainList2012]`
  - `[@pierceReesJonesBlank2025]`
- monitoring and supervision:
  - `[@kelley2024monitoring]`
  - `[@deJanvrySadouletSuriWang2023]`
  - `[@macleod2003subjective]`

Field Core requirements:
- This should be one of the more concrete and empirically rich weeks in the course.
- The chapter should explicitly show how behavioral labor speaks to modern personnel economics.
- Monitoring and supervision should be a named part of the week, not just an implicit subtheme.
- The frontier should be clear:
  - measuring whether monitoring complements or crowds out intrinsic/reciprocal motivation,
  - subjective evaluation and influence activities,
  - separating productivity from observable effort and gaming,
  - when workers respond to monitoring versus pay,
  - digital or algorithmic monitoring as a new empirical domain.
- Do not bury the frontier. Make it visible inside Field Core and Research Lab.

Methods requirements:
- Explicitly distinguish:
  - gift / generosity field experiments,
  - framing experiments in real workplaces,
  - randomized monitoring or supervision intensity,
  - subjective-evaluation designs,
  - real-effort experiments with contract variation,
  - contract-choice / sorting designs,
  - organizational data that reveal gaming or multitasking distortions.
- Do not present empirical results without naming:
  - the behavioral object,
  - the labor margin,
  - the outcome metric,
  - whether the design identifies treatment, sorting, monitoring, or evaluation effects.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@dellaVignaListMalmendierRao2022]`
- Secondary / challenge anchor: `[@kelley2024monitoring]`
- Optional frontier extension: `[@deJanvrySadouletSuriWang2023]`
- The lab should train students to diagnose:
  - what behavioral object is shifted,
  - whether the design changes pay, monitoring, evaluation, or relational treatment,
  - whether the outcome is productivity, extra work, or influence/gaming,
  - how the design could transfer to digital or remote-supervision settings.
- The bounded student path must run locally without confidential data.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Weeks 2–4
  2. workplace behavior as a behavioral-labor domain
  3. benchmark effort and contract problem
  4. incentives plus monitoring
  5. reciprocity and gift exchange
  6. subjective evaluation and supervision
  7. reference dependence and loss framing
  8. performance pay, heterogeneity, and sorting
  9. productivity vs extra work vs gaming
  10. frontier monitoring / algorithmic management
  11. bridge to Week 6

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 5 slides compile from the canonical path
4. Week 5 lab smoke test passes

Important implementation notes:
- If you add Week 5 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic1-behavioral/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Keep the chapter labor-focused and research-facing rather than generic.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
