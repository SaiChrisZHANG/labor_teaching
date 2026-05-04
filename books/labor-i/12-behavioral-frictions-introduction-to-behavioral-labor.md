---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Behavioral Frictions and an Introduction to Behavioral Labor

## Learning objectives

By the end of Week 12, students should be able to:

1. explain why behavioral labor is organized around worker-side labor objects rather than around an unstructured list of biases;
2. state the rational worker benchmark and identify where nonstandard preferences, beliefs, and decision-making enter it;
3. connect present bias, fairness, reciprocity, identity, beliefs, salience, and complexity to hours, effort, search, training, job choice, and take-up;
4. distinguish a behavioral wedge from standard heterogeneity, liquidity constraints, or institutional frictions;
5. explain how firms, managers, and policymakers respond when workers are behaviorally bounded;
6. interpret field experiments, expectation-based designs, quasi-experiments, and structural estimation as complementary identification tools rather than substitutes;
7. separate positive labor-market response from normative welfare evaluation under behavioral departures from revealed preference;
8. connect Week 12 back to [Week 3](03-dynamic-labor-supply.md), [Week 7](07-job-amenities-compensating-differentials.md), and [Week 11](11-public-policy-targeting-workers.md);
9. explain why this week is a bridge from Labor I into a full Behavioral Labor field course.

The economic question for the week is cumulative. Labor I has spent the semester building a worker-side benchmark for hours, effort, schooling, job choice, household allocation, mobility, and policy response. Week 12 asks how those objects change when workers or organizations systematically depart from the fully rational benchmark through nonstandard preferences, nonstandard beliefs, or nonstandard decision-making [@dellavigna2009; @dellavigna2018]. The goal is not to teach "biases." The goal is to teach a disciplined map for when behavioral departures create distinctive labor predictions, distinctive empirical designs, and distinctive welfare problems.

## Bridge

Week 12 is an introduction to Behavioral Labor, not a grab bag of psychological facts. The labor question is always relative to a benchmark. Which worker-side choice object is at stake? Which standard alternative is being ruled out? Which observed margin moves: hours, effort, search, training, take-up, or job choice? DellaVigna's taxonomy is useful precisely because it is portable across labor contexts: nonstandard preferences change what workers want, nonstandard beliefs change what workers think, and nonstandard decision-making changes how workers map incentives into action [@dellavigna2009].

This is also where the semester's earlier weeks get reinterpreted. [Week 3](03-dynamic-labor-supply.md) gave us dynamic labor supply and continuation values; Week 12 asks what happens when immediate costs loom too large or workers misforecast their own future behavior. [Week 7](07-job-amenities-compensating-differentials.md) taught us that wages are not the whole job; Week 12 asks what happens when job attributes are salient, identity-laden, or evaluated relative to reference points. [Week 11](11-public-policy-targeting-workers.md) taught us that statutory policy is not the same thing as effective exposure; Week 12 asks what happens when complexity, reminders, and simplification are not side details but first-order labor-market mechanisms.

```{figure} assets/figures/12-dellavigna-taxonomy-to-labor.png
:name: fig-week12-taxonomy
DellaVigna's framework becomes labor-economics content only when it is mapped into worker-side margins such as hours, effort, search, training, job choice, and take-up, and then linked to employer and policy responses.
```

```{include} assets/tables/12-behavioral-taxonomy-map.md
```

Figure {numref}`fig-week12-taxonomy` and Table {numref}`tbl:week12-taxonomy-map` provide the week's conceptual map. They discipline the lecture in two ways. First, they keep the focus on labor objects rather than on generic consumer anomalies. Second, they remind us that behavioral labor is strongest when it generates distinctive comparative statics about work, search, incentives, and contract design, not when it merely rationalizes residual variation after the fact.

:::{admonition} Core Material
:class: tip
- begin from a rational labor benchmark and ask where the wedge enters;
- map mechanisms into labor objects, not into generic behavioral vocabulary;
- distinguish worker behavior from employer, manager, and policymaker response;
- separate positive response from normative welfare claims.
:::

:::{admonition} Optional Extension Block
:class: note
- structural estimation of dynamic self-control in job search [@dellaVignaPaserman2005; @dellavigna2018];
- behavioral personnel economics and motivational design [@dellaVignaPope2018; @dellaVignaListMalmendierRao2022; @abelerHuffmanRaymond2025];
- a field map for a stand-alone Behavioral Labor course centered on self-control, beliefs, norms, attention, and welfare.
:::

## Field Core

### Benchmark labor choice and the behavioral wedge

The natural benchmark is the same worker-side object that underlies much of Labor I:

```{math}
:label: eq-week12-benchmark
\max_{h \in \mathcal{H}} \; U(c,h)
\quad \text{subject to} \quad
c = y + w h - T(w h + y).
```

Equation {eq}`eq-week12-benchmark` is intentionally spare. In the standard model, the worker understands the budget set, forms correct beliefs about returns and constraints, and chooses {math}`h` to maximize stable preferences. Once we move beyond the frictionless benchmark, it is useful to write the same object in wedge form:

```{math}
:label: eq-week12-wedge
a_i \in \arg\max_{a \in \mathcal{A}}
\left\{
\tilde{\mathbb{E}}_i \left[u_i\!\left(c(a),x(a)\right)\right]
- \tilde{\kappa}_i(a)
\right\},
```

where {math}`a` is a labor action such as hours, effort, search intensity, or training; {math}`\tilde{\mathbb{E}}_i` denotes possibly distorted beliefs; and {math}`\tilde{\kappa}_i(a)` allows perceived or effective costs to differ from standard costs. Behavioral labor is the study of which part of Equation {eq}`eq-week12-wedge` is misspecified, which labor margin moves because of it, and what evidence distinguishes that interpretation from standard alternatives such as heterogeneity, liquidity constraints, firm-side constraints, or search frictions.

```{figure} assets/figures/12-benchmark-vs-behavioral-wedges.png
:name: fig-week12-wedges
The behavioral wedge can enter through utility, beliefs, or the mapping from the true contract into the perceived contract. That decomposition disciplines both theory and empirical design.
```

Figure {numref}`fig-week12-wedges` is the workhorse interpretation device for the rest of the chapter. Present bias is a preference wedge. Overoptimistic beliefs about future self-control are a belief wedge. Incentive opacity and salience are decision-mapping wedges. The same observed low take-up or muted effort response can look very different depending on which wedge is active.

### Nonstandard preferences in labor

The first class of departures changes the worker's objective itself. The central intertemporal object is quasi-hyperbolic discounting:

```{math}
:label: eq-week12-present-bias
U_t
=
u(c_t,h_t)
+
\beta \sum_{s=t+1}^{T} \delta^{\,s-t} u(c_s,h_s),
\qquad \beta \in (0,1].
```

Equation {eq}`eq-week12-present-bias` is the natural bridge back to Week 3. When {math}`\beta < 1`, immediate effort, search, study, or enrollment costs loom too large relative to future gains. That logic is what makes self-control relevant for job search duration, training completion, workplace habits, and commitment demand [@laibson1997; @odonoghueRabin1999; @dellaVignaPaserman2005; @royerStehrSydnor2015]. The behavioral claim is not merely that workers are impatient. Standard exponential impatience already exists inside the benchmark. The distinctive claim is dynamic inconsistency: the worker who wants to search hard next week may not search hard when next week arrives.

Present bias is powerful in labor because many labor objects are investment objects. Search today raises the chance of a future offer. Training today raises a future wage path. Preventive workplace habits or attendance routines impose immediate discomfort for delayed productivity or health gains. That is why demand for commitment can be informative. If workers voluntarily choose commitment devices in settings where the static benchmark predicts no reason to do so, the researcher has evidence that standard impatience may be insufficient [@royerStehrSydnor2015].

The second preference-based class involves reference dependence, fairness, reciprocity, and identity. A compact effort object is

```{math}
:label: eq-week12-fairness
u_i
=
w_i - \psi(e_i)
+ \alpha_i \big(w_i - r_i\big)
+ \rho_i G_i e_i,
```

where {math}`r_i` is a reference wage or fairness benchmark and {math}`G_i` captures employer generosity or a gift. Equation {eq}`eq-week12-fairness` nests two classic labor ideas. First, effort can fall when the actual wage is perceived as unfair relative to a reference wage [@akerlof1982; @akerlofYellen1990]. Second, effort can rise because workers reciprocate generous treatment or because organizational gifts alter the relational contract, not merely the piece rate [@dellaVignaListMalmendierRao2022]. The standard alternative being ruled out is simple spot-market effort under fully private incentives. If workers work harder after a gift even when the monetary return to effort is unchanged, the researcher needs either a behavioral social-preference channel or a rich repeated-game channel that reproduces the same comparative statics.

Identity belongs in the same section because job choice and labor supply are often evaluated relative to social meaning rather than only to income and leisure. Gender norms, occupation stereotypes, or mission orientation can change who enters a job, which tasks are accepted, and how workers trade pay against meaning. The Week 7 connection matters here: amenities are not only nonwage components of utility; they are also objects whose salience and social interpretation may be endogenous to identity.

### Nonstandard beliefs in labor

The second class of departures changes what workers think they are choosing. A compact subjective-return object is

```{math}
:label: eq-week12-beliefs
\tilde{R}_{it}
=
\mathbb{E}_{it}^{\,s}\!\left[w_{t+1}(k_{t+1}) - w_t(k_t)\right]
\neq
\mathbb{E}_{it}\!\left[w_{t+1}(k_{t+1}) - w_t(k_t)\right],
```

where {math}`\mathbb{E}_{it}^{\,s}` denotes a subjective expectation. Equation {eq}`eq-week12-beliefs` can describe perceived returns to search, training, or occupational switching; perceived job-finding probabilities; or beliefs about how hard future effort will feel. Subjective beliefs matter because workers optimize against perceived rather than true returns. That is why expectation-based measurement is not an optional add-on. It is often necessary to know whether muted search, low take-up, or underinvestment reflects distorted beliefs, low objective returns, or low liquidity.

Job search is the cleanest labor application. DellaVigna and Paserman show that dynamic search behavior can be read through the lens of present bias and sophistication, but that interpretation depends on what workers believe about future behavior and about the arrival of offers [@dellaVignaPaserman2005]. More broadly, perceived returns to training, mismeasured job quality, and overoptimistic beliefs about future self-control can all produce behavior that superficially resembles standard low-return environments. The empirical task is therefore to separate a belief distortion from researcher measurement error and from omitted heterogeneity in opportunity sets.

Belief distortions also matter for policy take-up. A worker may know that a tax credit exists but misunderstand her eligibility, expected payment, or filing burden. In that case the take-up failure is neither a stable preference against the program nor a simple taste for leisure. It is a labor-market response to a perceived payoff schedule that differs from the statutory one. This is the direct bridge to Week 11.

### Nonstandard decision-making in labor

The third class of departures changes how the true environment is processed. A useful opacity object is

```{math}
:label: eq-week12-opacity
\tilde{w}
=
\lambda w + (1-\lambda)\bar{w},
\qquad 0 \leq \lambda \leq 1,
```

where {math}`\tilde{w}` is the effective perceived incentive, {math}`w` is the true incentive, and {math}`\bar{w}` is a simpler reference reward. Equation {eq}`eq-week12-opacity` captures limited attention, framing, and complexity in one line. Workers may respond strongly to simple, salient incentives and weakly to nonlinear or opaque ones, not because the marginal utility of income is low, but because the contract is not fully perceived [@chetty2012; @abelerHuffmanRaymond2025].

This is where behavioral labor most visibly overlaps with public policy and personnel economics. Piece rates, bonus thresholds, training subsidies, and filing rules can all be objectively large yet behaviorally small if workers do not perceive them. Conversely, reminders, simplification, and motivational framing can generate substantial changes without changing the true budget set. The standard alternative being ruled out is not "no response"; it is "workers fully understand the same contract we wrote down."

Opacity matters for contract design because complexity is not neutral. A contract that would be equivalent under full rationality need not be equivalent under bounded attention. Abeler, Huffman, and Raymond's incentive-complexity design is a direct example: the labor response depends on which contract features workers actually perceive, and the resulting effort can differ substantially from the fully rational benchmark [@abelerHuffmanRaymond2025].

### Rational responses by firms, managers, and policymakers

Behavioral labor is not only about worker mistakes. Once employers and policymakers recognize systematic departures from the benchmark, they redesign the environment. The important question is when organizations exploit a bias, when they accommodate it, and when they offset it.

In the workplace, firms can simplify or complicate incentives, use gifts or recognition, screen for sophistication, offer commitment devices, or choose monitoring and feedback technologies that make desired effort more salient. The same environment that attenuates one friction can amplify another. Repetition and experience may reduce naive misperception, but repeated opaque contracting can also teach workers the wrong simple rule. Market discipline can weed out some dominated choices, yet relational contracts, onboarding, and internal labor markets can sustain fairness and reciprocity channels that the spot-market model misses [@dellavigna2009; @dellaVignaListMalmendierRao2022; @abelerHuffmanRaymond2025].

For policymakers, the response menu is similarly wide: simplify, remind, commit, inform, default, or regulate contract complexity. The Week 11 lesson matters: when a policy response changes behavior by changing salience or burden rather than by changing statutory generosity, the relevant treatment is delivery design itself. Behavioral labor therefore sits naturally between labor theory and implementation.

### Empirical design and behavioral labor

Behavioral claims are only persuasive when they rule out a standard alternative. Field experiments help when they isolate gifts, reminders, incentive complexity, or framing while holding true monetary incentives fixed. Expectation elicitation helps when it measures the subjective object directly. Quasi-experiments help when they generate exogenous changes in timing, salience, or commitment opportunities that standard models would not interpret the same way. Structural estimation helps when the question is not only whether a wedge exists, but which wedge it is and how it changes policy counterfactuals [@dellavigna2018].

```{figure} assets/figures/12-behavioral-labor-design-map.png
:name: fig-week12-design
The design problem in behavioral labor is a matching problem: the identifying variation has to isolate whether the wedge comes from preferences, beliefs, or decision-making, and which standard alternative is being ruled out.
```

```{include} assets/tables/12-identification-map.md
```

Figure {numref}`fig-week12-design` and Table {numref}`tbl:week12-identification-map` summarize the empirical toolkit. The central methodological point is triangulation. A field experiment can show that simplification raises response. An expectation measure can show that workers misunderstood the original schedule. A structural model can then evaluate whether the welfare gain from simplification depends on naivete, sophistication, or heterogeneity in cognitive cost. DellaVigna's 2018 chapter is useful precisely because it frames behavioral estimation as a disciplined complement to reduced-form work rather than as a substitute for it [@dellavigna2018].

### Welfare and behavioral policy interpretation

Behavioral labor raises a welfare problem, not only a prediction problem. A compact way to write the distinction is

```{math}
:label: eq-week12-welfare
W_i(a)
=
U_i^{LR}(a) - U_i^{LR}(a_i^{obs}),
\qquad
\big(a_i^{obs} \neq a_i^{\star}\big)
\text{ does not imply }
W_i(a_i^{\star}) > 0
\text{ without assumptions.}
```

Equation {eq}`eq-week12-welfare` makes the core warning explicit. Observed action {math}`a_i^{obs}` need not reveal the long-run or normative preference object {math}`U_i^{LR}`. But it does not follow that every deviation from the benchmark justifies paternalism. Welfare depends on the normative benchmark, worker sophistication, market learning, internalities versus externalities, and whether the intervention targets information, commitment, or coercion.

That is why positive response is not the same thing as normative improvement. A reminder that raises take-up may improve welfare if workers were inattentive to a program they would endorse ex ante. The same reminder may be normatively ambiguous if it also pushes some workers into choices they do not value once attention is restored. Commitment devices are attractive because voluntary demand for commitment is direct evidence that some workers anticipate self-control problems, but even there demand can understate value when workers are partially naive [@laibson1997; @odonoghueRabin1999].

```{figure} assets/figures/12-market-responses-and-welfare.png
:name: fig-week12-welfare
Behavioral labor requires moving from observed response to a three-part interpretation: worker mechanism, employer or policy response, and welfare benchmark.
```

```{include} assets/tables/12-welfare-policy-map.md
```

Figure {numref}`fig-week12-welfare` and Table {numref}`tbl:week12-welfare-policy-map` are the week's final discipline devices. They force us to ask whether a contract redesign or policy simplification changed true incentives, changed perceived incentives, changed commitment opportunities, or changed measured outcomes without changing underlying welfare. Labor economists should be especially cautious when reduced-form evidence is strong but the welfare benchmark remains underspecified.

### Capstone bridge to a Behavioral Labor course

Week 12 should end with a field map rather than with a verdict on whether labor markets are "behavioral." The map has seven durable research programs:

1. self-control and dynamic labor supply, search, and training;
2. fairness, reciprocity, and gift exchange at work;
3. identity, mission, and social norms in job choice and labor supply;
4. salience, limited attention, and incentive complexity;
5. subjective beliefs, expectations, and perceived returns;
6. employer design and behavioral personnel economics;
7. welfare analysis under behavioral departures from revealed preference.

That map is the bridge from Labor I into a stand-alone Behavioral Labor course. Labor I uses it to reinterpret worker-side choice under frictions. A full Behavioral Labor course would go mechanism by mechanism, paper by paper, with deeper structural and welfare analysis. The point of Week 12 is that students should now know what questions to ask when a labor result is described as behavioral: relative to what benchmark, on which labor margin, with what identifying variation, and with what welfare object?

## Research Lab

The bounded Week 12 lab follows the course's standard `Reproduce -> Diagnose -> Transfer` workflow. The reproduction step uses deterministic synthetic data in the spirit of [@abelerHuffmanRaymond2025] to show how contract complexity changes effective perceived incentives and therefore effort. The diagnosis step asks students to separate true incentives from perceived incentives and to explain why low response to a complex schedule does not by itself imply weak labor supply. The transfer step moves to a synthetic workplace gift-exchange design in the spirit of [@dellaVignaListMalmendierRao2022], where a nonpecuniary gift can raise extra work even when the return to the employer is held fixed. The challenge block then reconnects the week to dynamic self-control through [@royerStehrSydnor2015].

The local path is intentionally bounded. Students do not need proprietary employer data or a full field-experiment replication package to learn the identification logic of incentive opacity, gift exchange, and commitment demand. The lab is built around a transparent local workflow that can run entirely from synthetic teaching files while preserving the mechanism-centered logic of the original papers.

## Methods Box

### Methods Box 1: field experiments identify mechanisms only when the monetary benchmark is held fixed

Behavioral labor uses field experiments most convincingly when the design changes gifts, complexity, reminders, or commitment opportunities while keeping the true return to effort or take-up transparent. A gift-exchange experiment rules out the pure spot-market model only if the monetary contract is otherwise comparable. A complexity experiment rules out "workers simply dislike effort" only if true incentives are held fixed while perceived incentives change [@dellaVignaListMalmendierRao2022; @abelerHuffmanRaymond2025].

### Methods Box 2: expectation and survey designs are needed when beliefs are the object

If the claim concerns perceived returns, eligibility, or job-finding beliefs, the researcher often needs direct measurement of the subjective object. Otherwise a belief distortion is hard to distinguish from researcher measurement error or omitted heterogeneity in opportunity sets. In behavioral labor, expectation data are not decorative. They are often part of the identifying design.

### Methods Box 3: quasi-experimental behavioral interpretation requires a standard alternative

Behavioral interpretation from quasi-experiments is strongest when a reform changes timing, salience, default rules, or commitment opportunities in ways the standard model would not treat as equivalent. The point is not that every deadline effect is behavioral. The point is that a design can isolate whether the same statutory incentive has different effects once attention, timing, or complexity changes.

### Methods Box 4: structural behavioral estimation is most useful when the question is policy or welfare

DellaVigna's central methodological argument is that structural behavioral work is especially valuable when reduced-form evidence alone cannot distinguish naivete from sophistication, one wedge from another, or positive response from normative welfare [@dellavigna2018]. In labor, that means structural estimation is often most informative for dynamic search, commitment, contract design, and welfare analysis, where heterogeneity and counterfactual policy design are first-order concerns.

## Reading ladder

### Framework and synthesis

- DellaVigna's field-survey taxonomy remains the canonical entry point [@dellavigna2009].
- DellaVigna's structural chapter is the best guide to identification, heterogeneity, and policy counterfactuals [@dellavigna2018].

### Labor-focused preference and motivation papers

- DellaVigna and Paserman on dynamic self-control in job search [@dellaVignaPaserman2005].
- Royer, Stehr, and Sydnor on incentives, commitment, and habit formation among workers [@royerStehrSydnor2015].
- DellaVigna, List, Malmendier, and Rao on social preferences and gift exchange at work [@dellaVignaListMalmendierRao2022].
- DellaVigna and Pope on effort, motivation, and the interpretation of behavioral mechanisms in real-effort settings [@dellaVignaPope2018].

### Classic behavioral-labor bridges

- Akerlof on gift exchange and labor contracts [@akerlof1982].
- Akerlof and Yellen on fairness and effort [@akerlofYellen1990].
- Laibson, O'Donoghue, and Rabin on present bias and dynamic inconsistency [@laibson1997; @odonoghueRabin1999].
- K{\H{o}}szegi and Rabin on reference-dependent preferences [@koszegiRabin2006].
- Abeler, Huffman, and Raymond on incentive opacity and effort provision [@abelerHuffmanRaymond2025].

## Exercises / discussion prompts

1. In Equation {eq}`eq-week12-benchmark`, which assumptions define the rational worker benchmark?
2. In Equation {eq}`eq-week12-wedge`, how would you represent a pure belief distortion versus a pure attention distortion?
3. Why does Equation {eq}`eq-week12-present-bias` connect Week 12 directly back to [Week 3](03-dynamic-labor-supply.md)?
4. What evidence would persuade you that a workplace gift effect reflects reciprocity rather than an omitted repeated-game incentive?
5. In Equation {eq}`eq-week12-beliefs`, what empirical design would best distinguish subjective-return error from low objective returns?
6. Why can the same true contract generate different responses under Equation {eq}`eq-week12-opacity`?
7. Which standard alternative must be ruled out before calling a deadline or reminder effect behavioral?
8. Why is Table {numref}`tbl:week12-identification-map` a warning against one-design interpretations?
9. What additional assumptions are needed before turning a positive response into a welfare claim in Equation {eq}`eq-week12-welfare`?
10. How would you explain the difference between a worker-side behavioral friction and an employer-side rational response to a first-year PhD student?
11. Which parts of Week 12 belong inside Labor I, and which parts naturally belong in a full Behavioral Labor course?

## Reproducibility or code lab note

The Week 12 lab uses a bounded local workflow rather than proprietary employer data. Students first reproduce a synthetic incentive-complexity factbook in the spirit of [@abelerHuffmanRaymond2025], then diagnose the mechanism as incentive opacity rather than low underlying responsiveness, and finally transfer the workflow to a synthetic gift-exchange setting in the spirit of [@dellaVignaListMalmendierRao2022]. The student-facing workflow is documented in [labs/12-behavioral-frictions-introduction-to-behavioral-labor/lab.md](labs/12-behavioral-frictions-introduction-to-behavioral-labor/lab.md).

## Slide companion note

The Week 12 deck should open by explaining why this is an introduction to Behavioral Labor rather than a list of biases, then move through the DellaVigna taxonomy, the benchmark labor-choice object, preference, belief, and decision-making wedges, employer and policy response, the empirical design toolkit, welfare interpretation, and a final field map that bridges Labor I into a full Behavioral Labor course. The canonical source is [slides/week12/12-behavioral-frictions-introduction-to-behavioral-labor.tex](slides/week12/12-behavioral-frictions-introduction-to-behavioral-labor.tex).
