---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Synthesis, Student Research Designs, and the Bridge to Labor II

## Learning Objectives

By the end of Week 13, students should be able to:

1. explain how the main worker-side topics of Labor I fit together as one field rather than as a sequence of disconnected lectures;
2. distinguish a labor topic, a descriptive pattern, a mechanism, and a research question;
3. write down a compact worker-side framework that nests labor supply, human capital, amenities, household constraints, mobility, policy, and behavioral wedges;
4. state a clean labor object of interest and match it to an appropriate empirical design or model discipline;
5. identify when a project remains partial equilibrium and when firms, search, wage-setting, or institutions must be modeled explicitly;
6. diagnose common proposal failure modes and improve a weak labor idea into a feasible first project;
7. use Week 13's research-design studio to draft a concrete 2--3 page labor research memo;
8. explain how Labor I becomes Labor II once worker-side choices are embedded in firms, frictions, and market adjustment;
9. leave the first semester with a research agenda rather than with a stack of disconnected notes.

## Opening Orientation

The economic question for the week is cumulative: how do the worker-side pieces of labor economics fit together inside modern labor economics, and how can a student turn those pieces into a clean research design that naturally opens into Labor II? This final week is not a loose review session. It is a capstone and a research-design studio.

:::{admonition} Core materials
:class: tip
- Labor I gives the worker-side primitives of the field.
- A good labor question starts from a clear object such as hours, search, wages, amenities, mobility, or take-up.
- A good labor design then asks which mechanism moves that object and which variation isolates the mechanism.
- Week 13 turns topic knowledge into proposal discipline.
:::

## Bridge

Labor I has built the worker side of labor economics. Week 1 defined the objects the field measures. Weeks 2 and 3 modeled labor supply over static and dynamic horizons. Week 4 added human-capital accumulation. Week 5 connected skills, wages, and sorting. Week 6 showed that households and care constraints reshape worker choices. Week 7 added amenities and total job value. Weeks 8 and 9 turned individual choices into inequality, discrimination, and misallocation. Week 10 studied reallocation across jobs, places, and generations. Week 11 brought in policy, incentives, and insurance. Week 12 asked what happens when workers or organizations are behaviorally bounded. Week 13 makes those pieces legible as one research program.

The unifying claim is simple. Labor I studies how workers choose, invest, sort, and respond. Those choices generate observed outcomes such as participation, hours, wages, earnings, job quality, mobility, and inequality. But the worker side is indispensable and incomplete. The same worker-side question changes once firms choose wages, vacancies, schedules, training, and workplace design; once search frictions shape matching; once institutions constrain contracting; or once aggregate shocks alter opportunity sets [@acemogluAutor2011; @mortensenPissarides1994; @manning2003].

```{figure} assets/figures/04-lifecycle-human-capital-earnings.png
:name: fig-week13-human-capital-arc
Human-capital accumulation gives Labor I its dynamic backbone: current choices about schooling, training, and work shape future wage offers, job ladders, and inequality.
```

```{figure} assets/figures/07-wage-inequality-total-job-value.png
:name: fig-week13-total-job-value
Worker-side labor economics is not only about wages. Total job value combines pay with amenities, schedule quality, flexibility, risk, and other nonwage characteristics.
```

Figure {numref}`fig-week13-human-capital-arc` captures why the first semester is cumulative rather than episodic: labor supply, schooling, household constraints, and policy exposure all affect the dynamic path of skills and earnings. Figure {numref}`fig-week13-total-job-value` adds the Week 7 lesson that wages alone are not the object. A serious labor field course must track the broader utility-relevant bundle that workers face.


:::{admonition} Optional Extension Block
:class: note
- run a 60--90 minute memo studio in which students pick one anchor paper and draft a one-page proposal skeleton in class;
- use the final section of the lab to push strong students from partial-equilibrium worker questions into explicit Labor II extensions;
- ask each student to name the point at which a firm, market, or institution must enter the model.
:::

## Field Core

### The unified worker-side framework

The semester can be written as one compact worker problem:

```{math}
:label: eq-week13-worker-problem
V_{it}(x_{it})
=
\max_{h_t,s_t,j_t,m_t}
\left\{
u(c_t,1-h_t,a_{j_t},\ell_t;\theta_i)
- \chi_i(h_t,s_t,m_t)
+ \beta \mathbb{E}_t[V_{i,t+1}(x_{i,t+1})]
\right\},
```

subject to worker-side constraints generated by wages, taxes and transfers, household commitments, care needs, discrimination, information, and behavioral wedges. Equation {eq}`eq-week13-worker-problem` nests most of Labor I. Hours {math}`h_t` capture labor supply and effort. Skill investment {math}`s_t` captures schooling and training. Job choice {math}`j_t` captures wages and amenities. Mobility {math}`m_t` captures job-to-job moves, migration, and reallocation. Policy and behavioral wedges affect both the feasible set and the mapping from true opportunities into perceived opportunities.

The dynamic human-capital object then becomes

```{math}
:label: eq-week13-human-capital
k_{i,t+1} = g(k_{it}, s_t, x_{it}, \varepsilon_{i,t+1}),
```

which reminds us that current worker choices shape future opportunity sets [@becker1964; @benPorath1967]. This is why Weeks 2 through 5 are inseparable: labor supply today changes experience, training, and future wages; human-capital investments change later participation margins; and policy evaluation is often dynamic rather than static [@blundellMaCurdy1999; @card1999].

The job-value object is equally compact:

```{math}
:label: eq-week13-job-value
J_{ij} = w_{ij} + A_{ij} - C_{ij},
```

where {math}`w_{ij}` is pay, {math}`A_{ij}` is the amenity bundle, and {math}`C_{ij}` collects worker-specific costs such as commuting, schedule incompatibility, care conflicts, or migration cost. Equation {eq}`eq-week13-job-value` organizes Week 7 and also helps reinterpret Weeks 5, 8, and 10. Wage dispersion and mobility are often misread when the relevant object is total job value rather than wage alone [@rosen1986; @masPallais2017; @sorkin2018].

```{figure} assets/figures/08-inequality-component-decomposition.png
:name: fig-week13-inequality-components
Worker-side choices aggregate into dispersion through several channels at once: skills, jobs, households, policy, and sorting all contribute to measured inequality.
```

Figure {numref}`fig-week13-inequality-components` is the Week 8 reminder that inequality is not one mechanism. It is an outcome of accumulated worker-side choices, differential opportunity sets, and assignment across jobs and firms [@autorKatzKearney2008]. That is why Week 13 is necessarily synthetic. Labor I has spent the semester building the components that produce inequality, not merely describing the outcome.

### From topics to research questions

A topic is not yet a question. "Discrimination," "mobility," and "human capital" are field labels. A research question specifies an object, a mechanism, a margin, and a population. "How does schedule unpredictability affect labor-force attachment among low-wage parents?" is a question. "How do workers misperceive the returns to training, and does that misperception attenuate take-up?" is a question. "How much of local earnings inequality reflects worker skill versus assignment to firms with different wage premia?" is a question [@cardCardosoHeiningKline2018; @songEtAl2019].

A descriptive fact is not yet a mechanism. Rising upper-tail inequality, education wage premia, child penalties, amenity valuation, or group gaps all discipline theory, but they do not by themselves tell us whether the channel is labor supply, human capital, sorting, household bargaining, employer behavior, or institutions [@klevenLandaisSogaard2019; @neumark2018]. A mechanism is a story about how one margin moves and why. An identification strategy is then the separate question of how we learn whether that mechanism is causal.

Every good labor project therefore needs a well-defined object of interest. A compact causal object is

```{math}
:label: eq-week13-causal-estimand
\tau = \mathbb{E}[Y_i(1) - Y_i(0)],
```

or a more targeted variant such as an event-study path, a complier estimand, or a wage-premium decomposition. Equation {eq}`eq-week13-causal-estimand` is intentionally plain. Week 13 is not about preferring one econometric style. It is about refusing to proceed without a clear estimand.

```{include} assets/tables/13-research-idea-template.md
```

Table {numref}`tbl:week13-idea-template` provides the week's core discipline device. A labor idea becomes credible only when the topic is converted into a mechanism, object, data source, design, contribution, and explicit statement about whether firms or equilibrium matter.

### Mechanism, data, design, and contribution

The research-design pipeline in labor economics has five linked steps.

1. Name the object. Is the project about participation, hours, effort, skill investment, wages, amenities, mobility, job finding, take-up, or inequality?
2. Name the mechanism. Is the project about incentives, information, care constraints, discrimination, sorting, search, bargaining, firm wage-setting, or behavioral wedges?
3. Name the data. Which unit matters: worker, household, job, establishment, worker--firm match, or place?
4. Name the design. Which variation, model discipline, or measurement strategy isolates the mechanism from standard alternatives?
5. Name the contribution. Which labor literature changes if the result is true?

```{figure} assets/figures/12-behavioral-labor-design-map.png
:name: fig-week13-design-map
The research-design problem is a matching problem: the object, the mechanism, the data, and the design have to fit each other. Weak fit is one of the most common reasons student ideas fail.
```

Figure {numref}`fig-week13-design-map` comes from Week 12, but it is useful here because it generalizes. The same design discipline applies whether the mechanism is present bias, childcare constraints, discrimination, job amenities, or search frictions. One does not begin with a favorite estimator and then search for a labor topic. One begins with a labor object and asks which empirical design is informative for that object.

```{include} assets/tables/13-common-failure-modes.md
```

Table {numref}`tbl:week13-failure-modes` summarizes the mistakes that most often weaken a Week 13 proposal. The hidden equilibrium issue is especially important. A project can start as a clean worker-side exercise and still become incomplete once the treatment changes wages, vacancies, schedules, or firm composition.

### Assignment, sorting, and the point where Labor II enters

Many worker outcomes are assignment outcomes. A compact sorting object is

```{math}
:label: eq-week13-sorting
P(j \mid i) = f(k_i, z_i, a_j, w_j, d_{ij}),
```

where worker characteristics {math}`k_i` and {math}`z_i` interact with job wages {math}`w_j`, job amenities {math}`a_j`, and bilateral frictions {math}`d_{ij}`. Equation {eq}`eq-week13-sorting` makes explicit why Weeks 5, 7, 8, 9, and 10 are deeply connected. Wage determination, amenities, discrimination, mobility, and inequality all depend on who matches to which jobs and places [@roy1951; @diamond2016; @cardHeiningKline2013].

Once firm heterogeneity or labor-market power becomes central, a bridge-to-Labor-II object is unavoidable:

```{math}
:label: eq-week13-bridge
w_{ij} = \phi_i + \psi_j + \varepsilon_{ij},
```

or, in search language, a matching object such as {math}`M(U,V)`. Equation {eq}`eq-week13-bridge` is the cleanest reminder that modern labor economics is not only about worker heterogeneity. Firm effects, matching frictions, and wage-setting rules shape the observed wage distribution, mobility patterns, and policy incidence [@abowdKramarzMargolis1999; @mortensenPissarides1994; @burdettMortensen1998; @manning2003].

```{figure} assets/figures/05-worker-firm-sorting-schematic.png
:name: fig-week13-worker-firm-bridge
The bridge into Labor II begins when worker-side heterogeneity is embedded in firm heterogeneity, matching frictions, wage-setting, and job ladders.
```

Figure {numref}`fig-week13-worker-firm-bridge` is where the first semester opens into the second. A worker-side estimate of returns, amenities, discrimination, or mobility is often only the beginning. Labor II asks how firms generate, price, or respond to those worker-side margins.

```{include} assets/tables/13-labor-i-to-labor-ii-bridge-map.md
```

Table {numref}`tbl:week13-l1-l2-bridge` should be read as a boundary map. It tells students when a project can remain partial equilibrium and when it becomes misleading to ignore firm-side adjustment, search, or institutions.

### What makes a strong labor research question?

A strong labor question has four properties.

1. It is about a recognizably labor object. The project should change how we understand work, wages, skill, job quality, mobility, discrimination, or policy.
2. It has one central mechanism. If the proposal requires five channels to work, it is usually too broad for a first project.
3. It has a feasible empirical or theoretical discipline device. Good labor questions respect the available data and the variation needed to learn from them.
4. It knows where it sits relative to firms and equilibrium. Partial equilibrium can be a strength when it is explicit. It is a weakness only when it is hidden.

Weak questions fail one or more of these tests. Some are too broad and read like literature surveys. Some have a nice design but no labor contribution. Some have a plausible mechanism but no observable object. Some are really Labor II questions hiding inside Labor I language. Week 13 is about learning to tell the difference early.

### Research templates drawn from Labor I

The point of a template is not to give students prepackaged papers. The point is to show what a disciplined first move looks like.

1. Labor supply and constraints: ask how schedule volatility, benefit design, or information about net wages changes participation or hours at a clearly defined margin; use public panel, tax, or administrative data where timing variation is observable; stay worker-side if prices and schedules are taken as given, but move into Labor II if firms endogenously redesign hours.
2. Human capital and training: ask whether training take-up is limited by beliefs, liquidity, or timing of returns; use linked worker-course or education-administrative records when available; a reduced-form training question can remain in Labor I, but the project becomes Labor II once employer training policy or task assignment is central [@becker1964; @acemogluPischke1999].
3. Wage determination and sorting: ask whether a return-to-skill estimate changes once workers sort into firms or occupations with different premia; use matched worker--firm or occupation-level data when possible; the worker-side estimand is feasible in Labor I, but the interpretation increasingly requires firm heterogeneity and wage-setting [@cardCardosoHeiningKline2018; @songEtAl2019].
4. Households and care: ask how care shocks, childcare cost, or leave policy affects hours, earnings, and dynamic attachment; use household-linked administrative or survey panels with event timing; the project remains worker-side if the focus is household constraint relaxation, but Labor II enters once employer schedule flexibility or leave policy design drives treatment intensity [@chiappori1992; @klevenLandaisSogaard2019].
5. Job quality and amenities: ask how workers value flexibility, remote work, risk, or schedule control and how that valuation differs across groups; use survey-experimental or matched vacancy-worker data; a compensating-differentials exercise can start in Labor I, but amenity provision and competition quickly pull the project into Labor II [@rosen1986; @masPallais2017].
6. Inequality and discrimination: ask whether group gaps or wage dispersion reflect differential skill accumulation, differential assignment, unequal treatment, or different firm exposure; the cleanest designs often combine descriptive decomposition with quasi-experimental or audit evidence; these questions often begin in Labor I and then require Labor II once firm sorting or wage-setting becomes the key propagation mechanism [@autorKatzKearney2008; @neumark2018].
7. Mobility and reallocation: ask which workers move, why they move, and whether mobility changes earnings, match quality, or intergenerational opportunity; use linked panel, migration, or matched employer-employee data; the worker-side part concerns opportunity and cost, but Labor II begins once vacancy creation, local labor demand, or firm wage premia shape the reallocation margin [@kennanWalker2011; @jiaMolloySmithWozniak2023].
8. Behavioral wedges in labor: ask whether low response to a policy, job, or training opportunity reflects true preferences, distorted beliefs, or decision frictions; combine reduced-form contrasts with expectation or design variation when possible; a worker-side behavioral idea is legitimate in Labor I, but contract design and employer response immediately open into Behavioral Labor and Labor II [@dellavigna2009; @dellavigna2018].

```{include} assets/tables/13-anchor-paper-menu.md
```

Table {numref}`tbl:week13-anchor-menu` turns those templates into a bounded studio menu. The anchor papers are deliberately heterogeneous. Some are causal-return papers. Some are descriptive architecture papers. Some are already worker--firm bridge papers. That variety is a feature, because it shows that "good labor design" is not identical to one empirical style.

## Research Lab

Week 13's lab is a research-design studio rather than a heavy new replication. The bounded path uses a menu of anchor papers from earlier weeks and a deterministic local packet that helps students move from topic to mechanism, data, design, and contribution. The lab follows the course's standard `Reproduce -> Diagnose -> Propose` workflow.

### Student research memo studio

The required deliverable is a 2--3 page memo. Students should submit one clean idea, not a literature survey. A good memo contains:

1. one sentence that begins, "This paper asks...";
2. one paragraph defining the object and the population;
3. one paragraph stating the mechanism and the strongest standard alternative;
4. one paragraph on data and feasible measurement;
5. one paragraph on the design, estimand, or model discipline;
6. one paragraph on the labor contribution;
7. one paragraph stating whether the project is partial equilibrium or already needs Labor II tools.

The memo should be feasible as a first project. The goal is not to solve all of labor economics in one proposal. The goal is to show that the student can name a margin, isolate a mechanism, and locate the project inside the field.

### Where Labor I ends and Labor II begins

Labor I is the worker-side half of the field. It gives the primitives for modern labor economics: preferences, constraints, human-capital accumulation, household structure, job value, discrimination, mobility, policy response, and behavioral wedges. Labor II begins when those worker-side margins are embedded in firms, search, wage-setting, organizations, and institutions. The right way to read the bridge is therefore not as a handoff between unrelated courses. It is the move from worker-side primitives to market equilibrium and organizational response [@acemogluAutor2011; @manning2003].

### In-class workshop prompts

1. Take one Week 13 anchor paper and identify the single sentence that states its true object of interest.
2. Rewrite a broad topic such as "migration" or "discrimination" into a precise labor question with one margin and one target population.
3. State one way in which a clean worker-side design could fail once firms adjust wages, schedules, or vacancies.
4. Explain why the same empirical result can have a different interpretation under human-capital, sorting, household, or behavioral mechanisms.

## Methods Box

### Methods Box 1: design choice must match the labor object

Descriptive decomposition is appropriate when the question is how much of an outcome is accounted for by observable or latent components. Quasi-experimental variation is appropriate when the question is a causal policy or treatment effect. Event studies are appropriate when the timing path is substantively central. Audit and field experiments are especially useful when discrimination, information, incentives, or reciprocity are the mechanism. Matched worker--firm data become essential when assignment and firm heterogeneity are central. Structural or equilibrium models become more attractive once reduced-form contrasts cannot recover the object of interest or once policy counterfactuals depend on market adjustment [@autorKatzKearney2008; @neumark2018; @dellavigna2018].

### Methods Box 2: partial equilibrium is not a flaw when it is explicit

A student proposal does not need to solve general equilibrium on day one. Partial equilibrium is a problem only when equilibrium responses are first-order for the interpretation and are ignored. A careful Week 13 memo should name that boundary directly. If the treatment plausibly changes firm wage policies, vacancy posting, or amenity provision, the student should say so and frame that as the next step into Labor II rather than as an omitted afterthought.

### Methods Box 3: the assignment margin is often the hidden object

Many labor projects appear to be about wages or participation, but are really about who matches to which jobs, firms, occupations, or places. That is why sorting and selection problems recur across returns to schooling, job amenities, discrimination, migration, and inequality [@roy1951; @cardHeiningKline2013]. A strong Week 13 design names the assignment process rather than leaving it implicit.

### Methods Box 4: contribution is a field statement, not a moral statement

"This matters because inequality is important" is not a contribution. A contribution states what labor economists would understand differently if the result were true. Does the project change how we think about labor supply elasticities, human-capital formation, compensating differentials, firm wage premia, policy targeting, behavioral response, or the transmission of discrimination? That is the standard for a good proposal.

## Reading Ladder And References

### Semester synthesis

- Blundell and MaCurdy remains the best broad guide to worker-side labor supply, dynamic response, and the role of constraints [@blundellMaCurdy1999].
- Becker and Ben-Porath provide the classic human-capital backbone for thinking dynamically about worker investment [@becker1964; @benPorath1967].
- Card is the canonical reminder that even standard-looking returns questions depend on object definition and identification discipline [@card1999].

### Inequality, sorting, and the worker--firm bridge

- Autor, Katz, and Kearney is the core descriptive architecture reading for modern wage inequality [@autorKatzKearney2008].
- Card, Cardoso, Heining, and Kline and Song et al. are the cleanest bridge readings from worker heterogeneity to firm heterogeneity and wage-setting [@cardCardosoHeiningKline2018; @songEtAl2019].

### Discrimination, design, and behavioral wedges

- Neumark provides a rigorous map of discrimination designs and interpretation [@neumark2018].
- DellaVigna's survey and structural chapter remain the best short path from worker-side frictions to research design and welfare discipline [@dellavigna2009; @dellavigna2018].

### Bridge to Labor II

- Acemoglu and Autor is a broad bridge reading for where worker-side analysis meets tasks, technology, and labor demand [@acemogluAutor2011].
- Mortensen and Pissarides, Burdett and Mortensen, and Manning are the canonical starting points for matching, wage-setting, and labor-market power [@mortensenPissarides1994; @burdettMortensen1998; @manning2003].

## Exercises And Discussion Prompts

1. Write one paragraph explaining why a strong labor research question must distinguish the object of interest from the mechanism.
2. Choose one anchor paper from Table {numref}`tbl:week13-anchor-menu` and explain which of the six formal objects in this chapter it relies on most heavily.
3. Take a Week 6 or Week 7 style worker-side question and state the precise moment at which firm-side schedule setting or amenity provision makes Labor II tools necessary.
4. Propose one project that stays deliberately partial equilibrium and one project that requires worker--firm matched data from the start. Explain why.
5. Explain why a nice design without a labor contribution is just as weak as a plausible mechanism without a design.

## Reproducibility And Code Lab Note

The Week 13 lab lives in [books/labor-i/labs/13-synthesis-and-research-designs/lab.md](labs/13-synthesis-and-research-designs/lab.md). Its bounded path is intentionally local and data-light. Students build a small anchor-paper packet, reproduce a compact design map from that packet, diagnose the object and mechanism, and then generate a memo template for a chosen extension idea. The smoke path is narrow by design:

```bash
cd books/labor-i/labs/13-synthesis-and-research-designs
ENV_NAME=research bash smoke.sh
```

This is not a substitute for a full replication package. It is a studio that teaches how to move from a labor topic to a proposal with one estimand, one mechanism, and one explicit statement about the Labor I to Labor II boundary.

## Slide Companion Note

The companion deck is [books/labor-i/slides/week13/13-synthesis-and-research-designs.tex](slides/week13/13-synthesis-and-research-designs.tex). The slides should not duplicate the chapter. They should define why Week 13 is a synthesis week, show the architecture of Labor I, write down the compact worker-side framework, walk through the mechanism--data--design pipeline, surface common proposal failure modes, and end with the map of where Labor II begins.

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
