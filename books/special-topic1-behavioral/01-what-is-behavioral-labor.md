# What Is Behavioral Labor?

## Learning Objectives

By the end of Week 1, students should be able to:

1. define Behavioral Labor relative to the benchmark worker and firm models from Labor I and Labor II;
2. classify labor-market deviations into nonstandard preferences, nonstandard beliefs, nonstandard decision-making, and firm/market/policy responses;
3. distinguish a reduced-form behavioral effect from a structural behavioral model, a welfare claim, and an equilibrium response;
4. match empirical designs to the behavioral object and labor margin they identify;
5. explain why Behavioral Labor is a labor field rather than general behavioral economics with workplace examples.

## Opening Orientation

Behavioral Labor starts from a familiar labor question: how do people choose work, search, effort, training, jobs, and program participation? The course changes the object by asking when the answer depends on self-control, reference points, social meaning, mistaken beliefs, limited attention, complexity, or organizational design. Labor is a natural domain for this move because labor decisions are repeated, high-stakes, dynamic, social, mediated by firms, and often implemented through policy rules that workers must notice and understand.

:::{admonition} Core points
:class: important

- Behavioral Labor is not a bag of biases. It is a disciplined way to map behavioral wedges into labor-market objects.
- The benchmark matters: preferences, beliefs, attention, and response wedges imply different tests and different welfare questions.
- Labor is distinctive because workers, households, firms, and policy systems jointly shape the realized choice environment.
- Evidence must state the margin identified and the behavioral object inferred. A treatment effect is not automatically a structural parameter or a welfare claim.
- Week 1 bridges back to Labor I Week 12 and forward to Week 2 on nonstandard preferences in work, effort, savings, and training.

:::

## Bridge

Labor I supplied the worker-side architecture: labor supply, human capital, job amenities, household allocation, policy exposure, and an introductory Week 12 bridge on behavioral frictions. Labor II supplied the firm and market architecture: labor demand, search frictions, contracts, wage setting, institutions, shocks, and equilibrium adjustment. Behavioral Labor reorganizes both around behavioral wedges and design.

The standard labor model remains the starting point. A worker chooses an action from a feasible set, trades off payoffs and costs, and responds to prices, constraints, and information. A firm offers jobs, contracts, schedules, or policies while anticipating worker response. The behavioral move is not to abandon optimization; it is to ask whether the problem the worker solves is the same problem the analyst writes down.

That distinction is especially important in labor markets. A worker can face a repeated decision with short-run costs and delayed gains, such as training or exercise. A job seeker can have noisy feedback and mistaken beliefs about job-finding probabilities. A household can make labor choices under gender norms or identity costs. A worker can respond to a tax, benefit, default, or application rule only if it is salient enough to enter the perceived choice set. A firm can then design incentives, screening, reminders, commitment devices, monitoring, or contracts around those predictable responses.

This is why Behavioral Labor is not simply general behavioral economics applied to jobs. The labor objects are not decorative examples. The field is organized around labor margins: hours, effort, search, training, take-up, job choice, household allocation, contract response, and wage-setting environments.

## Field Core

### The Benchmark Labor-Choice Object

A compact benchmark is:

```{math}
:label: eq:behavioral-labor-benchmark
a_i^\star \in \arg\max_{a \in \mathcal{A}} U_i(a;\theta_i)
\quad \text{s.t.} \quad c_i = g(a, p, y_i).
```

Here {math}`a` can be hours, effort, search intensity, training, application behavior, job choice, or program take-up. The vector {math}`\theta_i` summarizes standard preference parameters, {math}`p` summarizes prices and policy rules, and {math}`g(\cdot)` maps actions into consumption, wages, employment, or other payoff-relevant objects.

Behavioral Labor asks when the relevant problem is instead:

```{math}
:label: eq:behavioral-wedge
a_i^{B} \in \arg\max_{a \in \mathcal{A}_i(\lambda_i)}
\tilde{U}_i(a;\theta_i,\beta_i,r_i,\eta_i)
\quad \text{s.t.} \quad \tilde{g}_i(a \mid b_i,\lambda_i).
```

The notation is deliberately modular. Parameters such as {math}`\beta_i`, {math}`r_i`, and {math}`\eta_i` can represent present bias, reference dependence, reciprocity, social preferences, or identity. The object {math}`b_i` summarizes beliefs and subjective expectations. The parameter {math}`\lambda_i` captures attention, salience, complexity, or limited consideration. The environment {math}`\tilde{g}_i(\cdot)` may differ from the statutory or contractual environment because workers perceive incentives imperfectly, firms redesign contracts, or policy delivery changes effective exposure.

The observed gap is:

```{math}
:label: eq:behavioral-choice-gap
\Delta_i^a = a_i^{B} - a_i^\star.
```

This gap is not yet a welfare loss. It is a diagnostic object. The same observed response could reflect true constraints, standard heterogeneity, low returns, belief errors, present bias, attention limits, or employer response.

### Taxonomy: From DellaVigna To Labor Wedges

DellaVigna's field taxonomy gives the opening map: nonstandard preferences, nonstandard beliefs, and nonstandard decision-making, with market and policy responses becoming essential once behavioral regularities are predictable [@dellaVigna2009; @dellaVigna2018]. The labor translation is narrower and more demanding. For each paper, ask four questions:

1. What is the labor benchmark?
2. Which behavioral wedge changes the prediction?
3. Which margin is identified?
4. What do firms, markets, households, or policies do in response?

```{figure} assets/figures/01-taxonomy-to-labor-domains.png
:name: fig:taxonomy-to-labor-domains
:alt: Taxonomy map linking behavioral wedges to labor domains.
:width: 100%

Behavioral Labor maps preference, belief, attention, and response wedges into labor supply, search, training, contracts, households, and policy design.
```

```{include} assets/tables/01-taxonomy-map.md
```

### Where Behavioral Wedges Matter In Labor

Labor supply and effort are repeated dynamic decisions. Present bias can make costly current effort too low relative to a long-run plan, while reference points can make workers respond sharply around earnings targets or perceived fair wages. Job search is a belief-intensive activity: workers choose search intensity and reservation behavior under uncertainty about offer arrival, wage distributions, duration dependence, and their own future motivation. Training and human capital involve immediate costs and delayed returns, so low take-up can reflect true low returns, credit constraints, inaccurate beliefs, or self-control problems.

Inside firms, contracts and workplace relationships create behavioral objects that standard spot-market models often compress. Workers interpret bonuses, gifts, monitoring, deadlines, and fairness signals. Managers may deliberately simplify incentives, frame rewards, screen for motivation, or exploit naivete. Households add another layer: relative income, gender identity, social norms, and bargaining can alter labor supply and occupational sorting [@bertrandKamenicaPan2015; @akerlofKranton2000]. Worker-facing public policy adds salience and take-up margins because statutory incentives only matter when workers encounter and understand them [@chetty2015].

```{figure} assets/figures/01-benchmark-vs-behavioral-wedge.png
:name: fig:benchmark-vs-behavioral-wedge
:alt: Benchmark labor-choice problem with behavioral wedges entering preferences, beliefs, attention, and environment design.
:width: 100%

Behavioral wedges enter the worker problem before the observed action and may also enter through firms or policy environments.
```

```{include} assets/tables/01-labor-domains-map.md
```

### Evidence, Models, Welfare, And Equilibrium Are Different Claims

Week 1 sets a discipline that will return throughout the course.

A **reduced-form behavioral effect** says that an intervention changed a labor outcome on a specific margin. For example, a commitment contract can raise exercise attendance or a search message can raise applications. The estimand is a causal effect of a design feature on a behavior.

A **structural behavioral model** interprets behavior through a parameterized choice problem, such as present bias, mistaken beliefs, social preferences, or limited attention. This can support counterfactuals, but only after the model separates behavioral mechanisms from constraints and heterogeneity [@dellaVigna2018].

A **welfare claim** needs a normative benchmark. If the worker's decision utility differs from experienced or long-run utility, the analyst must say whose preferences count, whether the worker is sophisticated, and whether the intervention helps the worker reach a welfare-relevant choice [@chetty2015].

An **equilibrium response** asks how firms, markets, households, and policy systems adapt. A firm may exploit inattention, offset self-control problems through commitment devices, or redesign contracts to make incentives salient. Equilibrium can mask a behavioral wedge, amplify it, or shift its incidence.

```{math}
:label: eq:welfare-internality
I_i(a_i^{B}) =
V_i(a_i^\dagger) - V_i(a_i^{B}),
```

where {math}`V_i(\cdot)` is the welfare-relevant utility representation and {math}`a_i^\dagger` is the action the analyst treats as normatively relevant. The internality {math}`I_i` is hard to measure because {math}`a_i^\dagger` is not usually observed and may differ across workers.

```{figure} assets/figures/01-welfare-equilibrium-caution.png
:name: fig:welfare-equilibrium-caution
:alt: Flow from behavioral wedge through worker choice, firm and policy response, observed outcome, and welfare interpretation.
:width: 100%

A behavioral effect becomes a welfare statement only after specifying the normative benchmark and the relevant firm, market, or policy response.
```

## Research Lab

The opening research lab uses [@royerStehrSydnor2015] as the primary anchor because it is labor-facing, experimentally grounded, and useful for teaching the distinction between incentives, commitment, and habit formation. Workers in a real firm setting face exercise incentives and commitment opportunities. The design lets students ask whether short-run incentives raise participation, whether workers demand commitment against their own future behavior, and whether temporary intervention generates durable habit formation.

The challenge anchor is [@altmannFalkJaegerZimmermann2018], which moves the course toward beliefs, information, and motivation in job search. Students should see that the same framework can classify what is identified: a message may change beliefs, attention, or motivation, and the labor margin is search behavior and job finding. The optional frontier anchor is [@bertrandKamenicaPan2015], which shows how identity and norms can shape household labor allocation and gendered labor-market outcomes.

The lab workflow is **Reproduce -> Diagnose -> Transfer**:

1. **Reproduce:** Build and analyze a bounded synthetic worker wellness experiment in the spirit of [@royerStehrSydnor2015]. The smoke path estimates treatment-arm differences in participation, commitment take-up, and post-incentive persistence.
2. **Diagnose:** State the margin identified and the behavioral object inferred. Separate incentive response from commitment demand and habit formation.
3. **Transfer:** Apply the same classification logic to a synthetic job-search information intervention inspired by [@altmannFalkJaegerZimmermann2018].

The bounded path does not use confidential employer microdata. Its purpose is pedagogical: students learn how to classify a behavioral labor design before moving to richer empirical work.

## Methods Box

```{figure} assets/figures/01-methods-identification-map.png
:name: fig:methods-identification-map
:alt: Methods map linking design types to identified behavioral objects and labor margins.
:width: 100%

Behavioral labor evidence must map the design to the identified object and the labor margin.
```

```{include} assets/tables/01-methods-and-welfare-map.md
```

Field experiments and framed field experiments identify causal effects of incentives, commitment offers, social signals, or information on labor behavior. They are powerful because they manipulate the environment directly, but the treatment effect is not automatically a deep parameter.

Information and salience interventions identify whether behavior changes when beliefs or attention are moved. They are central for job search, training, application behavior, and benefit take-up, but the interpretation must separate information from motivation and administrative support.

Administrative nudges and policy design experiments identify the role of reminders, defaults, simplification, timing, and friction costs in actual policy environments. They are often closest to implementation, but welfare depends on whether the nudge helps workers reach a better choice or merely increases a target outcome.

Observational designs with measured beliefs or preferences help connect heterogeneity in behavioral objects to outcomes, especially when randomization is infeasible. Their main burden is selection and measurement error.

Structural behavioral estimation is most useful when the question is mechanism, counterfactual policy, or welfare. The price is model dependence, so the estimated wedge must be disciplined by the labor margin and the design.

## Reading Ladder And References

**Core framing.** Start with [@dellaVigna2009] for the field evidence map and [@dellaVigna2018] for the structural behavioral perspective. Read them as taxonomies, not as a list of curiosities.

**Welfare and policy framing.** Read [@chetty2015] for a pragmatic account of how behavioral economics enters public policy and why welfare statements require a disciplined normative object.

**Labor-facing anchor papers.** Use [@dellaVignaPaserman2005] for impatience and job search, [@royerStehrSydnor2015] for incentives, commitment, and habit formation among workers, [@altmannFalkJaegerZimmermann2018] for job-search information and motivation, and [@bertrandKamenicaPan2015] for identity and household labor allocation.

**Optional theoretical anchor.** Use [@akerlofKranton2000] to understand why identity can enter utility and why this matters for labor allocation rather than only for social psychology.

## Exercises And Discussion Prompts

1. Take one labor margin from Labor I, such as hours, training, or benefit take-up. Write the benchmark choice problem, then add one preference wedge, one belief wedge, and one attention wedge. Which wedge would be easiest to identify?
2. Consider a field experiment that sends job seekers information about application returns. What margin is identified? What behavioral object is inferred? What standard explanations remain?
3. Suppose a firm observes that workers underrespond to a complex bonus. List one exploitative response, one welfare-improving response, and one response that makes the behavioral wedge harder to detect.
4. Pick one paper in the reading ladder. Classify it as primarily reduced-form evidence, structural modeling, welfare analysis, or equilibrium analysis. Defend the classification.

## Reproducibility And Code Lab Note

The Week 1 lab lives at `labs/01-what-is-behavioral-labor/`. It is deliberately bounded and synthetic. Students run a local smoke path that creates a Royer-Stehr-Sydnor-style worker wellness dataset, reproduces a treatment-arm factbook, and transfers the logic to a job-search information design. The lab teaches classification and diagnosis rather than official replication with confidential employer data.

## Slide Companion Note

The Week 1 slide deck lives at `slides/week1/01-what-is-behavioral-labor.tex`. The deck is a conceptual map, not a duplicate of this chapter: it defines the central question, locates Behavioral Labor relative to Labor I and Labor II, introduces the benchmark and taxonomy, and ends with methods, welfare, equilibrium cautions, and the bridge to Week 2 on nonstandard preferences.

## Bridge Forward

Week 2 moves from the full taxonomy to the first major mechanism family: nonstandard preferences. The core questions become sharper. When does present bias change labor supply, effort, savings, search, or training? When do reference dependence, reciprocity, and identity change workplace behavior or household allocation? And when does the evidence identify a preference wedge rather than constraints, beliefs, or organizational design?
