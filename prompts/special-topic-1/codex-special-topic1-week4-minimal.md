Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic1-behavioral/OUTLINE.md, @books/special-topic1-behavioral/index.md, @books/special-topic1-behavioral/myst.yml, @books/special-topic1-behavioral/references.bib, @books/special-topic1-behavioral/sources/04-attention-salience-complexity-and-learning.md, @books/special-topic1-behavioral/assets/tables/04-attention-salience-complexity-map.md, @books/special-topic1-behavioral/assets/tables/04-dynamic-learning-and-information-acquisition-map.md, and @books/special-topic1-behavioral/assets/tables/04-identification-and-welfare-map.md.

Goal: turn the Behavioral Labor Week 4 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 1 — Behavioral Labor
- Week: 4
- Canonical chapter path: `books/special-topic1-behavioral/04-attention-salience-complexity-and-learning.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week4/04-attention-salience-complexity-and-learning.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/04-attention-salience-complexity-and-learning/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/04-attention-salience-complexity-and-learning.bib` into `books/special-topic1-behavioral/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic1-behavioral/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic1-behavioral/04-attention-salience-complexity-and-learning.md`
2. `books/special-topic1-behavioral/slides/week4/04-attention-salience-complexity-and-learning.tex`
3. `books/special-topic1-behavioral/labs/04-attention-salience-complexity-and-learning/lab.md`
4. `books/special-topic1-behavioral/labs/04-attention-salience-complexity-and-learning/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic1-behavioral/myst.yml` or `books/special-topic1-behavioral/index.md` needed to wire Week 4 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@dellaVigna2009]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic1-behavioral/slides/week4/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic1-behavioral/slides/week4/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic-boundary requirement:
- This week is about **attention, salience, complexity, learning, and endogenous information acquisition in labor**.
- It should stay labor-focused and not drift into generic behavioral public economics or generic psychology.
- Learning is central: attention/salience/complexity are dynamic because workers and firms learn over time, receive information, acquire costly information, and sometimes redesign the information environment.
- The main labor domains should be:
  - labor supply under taxes/benefits and nonlinear schedules,
  - workplace incentives and effort,
  - benefit take-up and claiming,
  - retirement saving / payroll-linked saving,
  - training / upskilling / policy navigation where complexity and attention matter.
- Job search may be used briefly as a bridge from Week 3, but it should not be the main organizing focus.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- Keep the week anchored to DellaVigna’s framework, but isolate the focus to **nonstandard decision-making through attention, salience, complexity, and learning**.
- The chapter should show students that these are not static wedges. It should make clear that:
  - workers learn schedules, rules, and incentive environments over time,
  - workers choose whether to acquire costly information,
  - firms and policymakers can make incentives more or less legible,
  - the same worker may look more or less “biased” depending on experience, exposure, and information design.
- Make the dynamic frontier explicit:
  - endogenous information acquisition,
  - learning from repeated interactions,
  - the difference between low salience, true misperception, and slow learning,
  - when complexity is a design choice rather than an exogenous feature.

Formal / conceptual requirements:
Include at least:
1. one benchmark labor-choice object with transparent incentives, for example a worker choosing hours, effort, or take-up under a known schedule;

2. one attention / salience wedge, e.g. a perceived incentive schedule:
```{math}
:label: eq:salience-week4
a_i \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i) \quad \text{s.t.} \quad \tilde{T}_i(a) \neq T(a),
```
with text explaining that the worker reacts to a perceived rather than actual tax/benefit or incentive schedule;

3. one complexity / information-acquisition object, for example:
```{math}
:label: eq:learning-week4
a_{it}, m_{it} \in \arg\max \tilde{U}_{it}(a;\theta_i,b_{it}) - C(m_{it})
\quad \text{with} \quad
b_{i,t+1}=B(b_{it},m_{it},x_{it+1}),
```
where {math}`m_{it}` is endogenous information acquisition or attention effort and {math}`b_{it}` evolves through learning;

4. one distinction among:
  - low salience,
  - complexity / opaque mapping from actions to payoffs,
  - true lack of information,
  - endogenous information acquisition,
  - dynamic learning;

5. one subsection on labor supply and benefit schedules:
  - EITC / tax-benefit schedules,
  - bunching attenuation,
  - learning schedules over time,
  - local knowledge or information diffusion;

6. one subsection on benefit take-up / claiming / policy navigation:
  - frictions in claiming or program take-up,
  - reminder/simplification designs,
  - why reduced-form treatment effects do not automatically identify the same object;

7. one subsection on workplace incentives and effort:
  - opaque compensation formulas,
  - bounded rationality and contract complexity,
  - how effort provision differs when incentives are difficult to decode;

8. one short subsection on work-linked savings / retirement / training:
  - defaults, disclosure, and planning complexity,
  - learning about retirement or social-security incentives,
  - how attention and salience affect dynamic labor and savings choices;

9. one welfare section explaining:
  - why welfare depends on whether inattention is stable, state-dependent, or reduced by learning,
  - why simplification and information provision can have heterogeneous effects,
  - why firm/policy design choices matter.

Methods requirements:
- Explicitly distinguish:
  - information letters and randomized information provision,
  - simplification / salience / disclosure interventions,
  - quasi-experimental changes in schedules or rules combined with learning variation,
  - monitored information-acquisition designs,
  - workplace incentive experiments,
  - structural models with learning or endogenous information acquisition.
- Make clear what each design identifies and what it cannot separately identify.
- In particular, distinguish empirically among:
  - mistakes about a schedule,
  - optimization frictions,
  - lack of attention,
  - lack of information,
  - dynamic learning.
- Do not present results without naming the observed labor margin and the behavioral object inferred.

Suggested empirical anchors:
- labor supply and learning schedules: `[@kostolMyhre2021]`
- knowledge diffusion / salience in the EITC: `[@chettyFriedmanSaez2013]`
- take-up and psychological frictions: `[@bhargavaManoli2015]`
- Social Security information and older-worker responses: `[@liebmanLuttmer2015]`
- incentive opacity and workplace effort: `[@abelerHuffmanRaymond2025]`
- endogenous attention / costly information acquisition frontier: `[@bartosBauerChytilovaMatejka2016]`

Field Core requirements:
- This should be one of the more frontier-facing weeks in the course.
- Move cleanly from:
  1. benchmark transparent labor choice,
  2. salience and perceived incentives,
  3. complexity and opacity,
  4. learning and endogenous information acquisition,
  5. labor-supply / take-up / claiming applications,
  6. workplace-incentive applications,
  7. savings / retirement / training applications,
  8. welfare and design implications.
- The chapter should make clear that the frontier is increasingly dynamic rather than static.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@kostolMyhre2021]`
- Secondary / challenge anchor: `[@bhargavaManoli2015]`
- Optional extension anchor: `[@abelerHuffmanRaymond2025]`
- The lab should teach students how to diagnose:
  - what information/salience/complexity object is changed,
  - whether the design identifies learning, attention, or simplification,
  - what labor margin is observed,
  - how to transfer the design to another labor setting.
- Bounded transfer ideas:
  - apply information/salience logic to another worker-policy margin,
  - adapt a complexity design to an incentive or training environment,
  - build a simple pedagogical simulation of learning under opaque schedules.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and bridge from Week 3
  2. DellaVigna taxonomy with Week 4 highlighted
  3. benchmark transparent labor choice
  4. salience vs complexity vs information vs learning
  5. labor supply under nonlinear tax-benefit schedules
  6. take-up, claiming, and policy navigation
  7. opaque incentives and effort
  8. endogenous information acquisition frontier
  9. methods / identification map
  10. bridge to Week 5

Validation requirements:
1. strict book build:
   `conda run -n research jupyter book build --html --strict`
2. preview check:
   `conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 4 slides compile from the canonical path
4. Week 4 lab smoke test passes

Important implementation notes:
- If you add Week 4 to `index.md` or `myst.yml`, do so in the same style that earlier weeks use.
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
