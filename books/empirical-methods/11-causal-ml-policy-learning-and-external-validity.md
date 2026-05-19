# Lecture 11. Causal ML, Policy Learning, And External Validity

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when treatment-effect heterogeneity is itself the research object and when it is an input into a decision rule;
2. define individualized treatment effects, conditional average treatment effects, subgroup effects, policy rules, policy value, and regret;
3. distinguish prediction, causal effect estimation, and policy learning in applied-economics language;
4. explain empirical welfare maximization and policy learning as methods for choosing among feasible assignment rules;
5. use uplift and targeting logic without confusing high predicted outcomes with high treatment effects;
6. diagnose how external validity, transportability, and distribution shift change the interpretation of heterogeneous treatment effects;
7. evaluate fairness, feasibility, budget, capacity, legal, and implementation constraints before recommending a targeting rule;
8. identify which common ML algorithms are useful for nuisance prediction, measurement, heterogeneity, or policy choice, and state their applied caveats.

## Opening Orientation

Lecture 10 asked how flexible methods can estimate causal effects when controls, nuisance functions, and heterogeneity are high-dimensional. Lecture 11 asks what applied researchers do **after** they have estimated heterogeneity. The central question is: **when can heterogeneous treatment effects support a policy rule, and when should they remain descriptive evidence about mechanisms, populations, or external validity?**

The distinction matters because a conditional average treatment effect is not a policy. A CATE says how treatment effects vary with covariates under an identifying design. A policy rule says who should receive treatment under a welfare objective, capacity constraint, budget, information set, and implementation environment. Moving from the first object to the second adds economics.

The paper spine reflects that shift. Wager and Athey, and Athey, Tibshirani, and Wager, supply credible tools for estimating heterogeneity [@wagerEstimationInferenceHeterogeneous2018; @atheyGeneralizedRandomForests2019]. Kitagawa and Tetenov frame treatment choice as empirical welfare maximization [@KitagawaTetenov2018]. Athey and Wager show how policy learning can be done with observational data under appropriate causal assumptions [@atheyWager2021]. Bansak and coauthors give a concrete assignment application, while Allcott, Vivalt, and Dehejia, Pop-Eleches, and Samii make the portability problem visible [@BansakFerwerdaHainmuellerEtAl2018; @Allcott2015; @Vivalt2020; @DehejiaPopElechesSamii2021].

## Core Points

:::{admonition} Core points
:class: important

- Lecture 10 estimates effects with high-dimensional nuisance structure; Lecture 11 turns estimated heterogeneity into policy, targeting, and portability questions.
- Heterogeneity is the object when the research question is about mechanisms, incidence, or subgroup effects. Policy learning is the object when the research question is about which feasible rule should assign treatment.
- Estimating {math}`\tau(x)` is not the same as choosing {math}`\pi(x)`. A rule requires a value function, costs, constraints, uncertainty, and implementation details.
- Uplift and targeting require causal effects, not predicted levels. Treating workers with high predicted outcomes is not the same as treating workers with high predicted gains.
- External validity is harder when effects vary. A rule learned in one population may fail in another because covariates, treatment effects, institutions, prices, take-up, or constraints shift.
- Fairness and feasibility are part of policy design. A statistically high-value rule can be unacceptable or undeployable.
:::

## Bridge

Lecture 10 separated causal parameters from nuisance prediction. Its core discipline was: estimate outcome and treatment nuisance functions flexibly, use orthogonalization and sample splitting to protect the target effect, and treat CATEs as causal objects only under a credible design.

Lecture 11 keeps those tools but changes the target. The object is no longer only an ATE or CATE. It may be a rule, a value, a regret bound, a targeting frontier, or a portability claim. That shift changes what has to be reported. The researcher must still defend identification and overlap, but now also has to defend the policy class, welfare criterion, budget constraint, fairness constraint, source-to-target comparison, and implementation environment.

```{include} assets/tables/11-theory-to-applied-bridge.md
```

## Field Core

### A. Three Objects: Prediction, Effects, And Decisions

Machine learning enters applied economics through at least three distinct objects.

**Prediction.** A prediction rule estimates an outcome, label, risk, or score:

```{math}
:label: eq:em11-prediction
\widehat m(x) \approx \mathbb E[Y \mid X=x].
```

This is useful for measurement, risk classification, imputation, or triage. It is not a causal effect unless the research design supplies a counterfactual interpretation.

**Causal effect estimation.** A treatment-effect estimator compares potential outcomes:

```{math}
:label: eq:em11-cate
\tau(x)
=
\mathbb E\left[Y(1)-Y(0)\mid X=x\right].
```

This is the conditional average treatment effect. It answers: for units with covariates {math}`X=x`, how much does treatment change the outcome relative to non-treatment?

**Decision rules.** A policy maps observables into treatment assignment:

```{math}
:label: eq:em11-policy-rule
\pi(x)\in\{0,1\}.
```

It answers: given evidence, constraints, and a welfare objective, who should be assigned to treatment?

The three objects can use similar algorithms, but they are not interchangeable. A worker with high predicted employment absent treatment may have a low treatment effect. A worker with low predicted earnings may or may not gain from training. A policy rule should target gains net of costs and constraints, not predicted levels alone.

### B. IATEs, CATEs, And Subgroup Effects

The most individual object is the individualized treatment effect:

```{math}
:label: eq:em11-iate
\tau_i
=
Y_i(1)-Y_i(0).
```

For a single person, {math}`\tau_i` is usually not point-identified because only one potential outcome is observed. Researchers therefore estimate average objects. The CATE in {numref}`eq:em11-cate` averages over units with covariates {math}`X=x`. A subgroup effect averages over a policy-relevant group {math}`G`:

```{math}
:label: eq:em11-subgroup-effect
\tau_G
=
\mathbb E\left[Y(1)-Y(0)\mid X\in G\right].
```

Heterogeneity is itself the object of interest when the paper asks about incidence, mechanisms, or theory. Examples include whether a youth employment program helps high-risk applicants more than low-risk applicants, whether a wage subsidy has larger effects in thinner labor markets, or whether a job-search intervention changes outcomes more for workers with weaker networks.

Policy learning becomes the object when the paper asks how scarce treatment slots should be assigned. In that case, the subgroup effect is not enough. The researcher needs to know whether a rule improves welfare relative to alternatives, whether the rule can be implemented, and whether it remains credible outside the sample used to learn it.

### C. CATE Versus Policy Rule

In the simplest textbook case, if treatment is costless, capacity is unlimited, outcomes are valued equally, and CATEs are known, the optimal rule is:

```{math}
:label: eq:em11-simple-optimal-rule
\pi^*(x)
=
\mathbf 1\{\tau(x)\ge 0\}.
```

Applied settings rarely look like that. Treatment may be costly; slots may be scarce; policy makers may care about distributional weights; assignment may be constrained by law, administrative information, or political feasibility; take-up may be imperfect; and treatment may change behavior in ways not captured by the original experiment or observational design.

A more realistic statement is:

```{math}
:label: eq:em11-constrained-policy
\pi^*
\in
\arg\max_{\pi\in\Pi}
V(\pi),
```

where {math}`\Pi` is the feasible policy class. This class might contain simple score thresholds, shallow trees, site-level rules, or budget-constrained assignment rules. The policy class is an economic and institutional choice, not only a statistical tuning parameter.

### D. Policy Value And Regret

The value of a policy rule is the expected outcome under the treatment assignment induced by the rule:

```{math}
:label: eq:em11-policy-value
V(\pi)
=
\mathbb E\left[Y(\pi(X))\right].
```

For a binary treatment, this can be written as:

```{math}
:label: eq:em11-policy-value-potential-outcomes
V(\pi)
=
\mathbb E\left[
\pi(X)Y(1) + \left(1-\pi(X)\right)Y(0)
\right].
```

If treatment has cost {math}`c(X)` or if the outcome should be net of resource use, the relevant value becomes:

```{math}
:label: eq:em11-net-policy-value
V^{net}(\pi)
=
\mathbb E\left[
\pi(X)\left(Y(1)-c(X)\right)
+ \left(1-\pi(X)\right)Y(0)
\right].
```

Regret compares a candidate rule to the best rule in the policy class:

```{math}
:label: eq:em11-regret
R(\pi)
=
V(\pi^*)-V(\pi).
```

This is the core shift from effect estimation to decision analysis. A CATE estimate may be unbiased and still yield a poor policy if it is too noisy, optimized in sample, unconstrained, or applied where support is weak. Conversely, a simple rule can have low regret if it captures most decision-relevant heterogeneity while remaining stable and implementable.

### E. Empirical Welfare Maximization And Policy Learning

Empirical welfare maximization asks the researcher to choose the rule in {math}`\Pi` with the highest estimated value:

```{math}
:label: eq:em11-ewm
\widehat\pi
\in
\arg\max_{\pi\in\Pi}
\widehat V(\pi).
```

Kitagawa and Tetenov make this treatment-choice problem explicit: the target is not a coefficient but a rule that performs well by a welfare criterion [@KitagawaTetenov2018]. Athey and Wager extend policy learning to observational data by combining causal identification, orthogonal scores, and policy-value estimation [@atheyWager2021].

The practical questions are concrete:

- What policies are feasible enough to be included in {math}`\Pi`?
- Is treatment assignment randomized, quasi-random, or observational?
- How is {math}`\widehat V(\pi)` estimated?
- Is policy value evaluated on data not used to choose the rule?
- Does the rule respect capacity, budget, and fairness constraints?
- How much uncertainty surrounds value and regret?

A policy tree is one interpretable example of {math}`\Pi`. It might assign a training program based on baseline unemployment duration and prior earnings. A score-threshold rule is another. A highly flexible model that assigns everyone idiosyncratically may look better in sample but be harder to validate, explain, or deploy.

### F. Uplift And Targeting Logic

Targeting logic should be based on treatment effects or net treatment effects, not on predicted outcome levels. In marketing and policy settings this is often called uplift: prioritize units for whom treatment changes the outcome most.

For a job-training program, ranking applicants by predicted employment under treatment,

```{math}
:label: eq:em11-level-targeting
\mathbb E[Y(1)\mid X=x],
```

does not answer the targeting question. The policy question is closer to ranking by:

```{math}
:label: eq:em11-uplift-targeting
\mathbb E[Y(1)-Y(0)-c(X)\mid X=x].
```

This distinction is central in labor applications. A program may be most effective for applicants with weak baseline prospects, even though their predicted treated outcome remains below the outcome of advantaged applicants. Or it may be wasteful to target high-risk applicants if treatment effects are small, support is weak, or implementation costs are high.

Subgroup discovery can help, but it should be handled as evidence generation rather than as a final rule. Discovered subgroups need hold-out validation, standard errors or uncertainty intervals, support checks, and a statement of whether the dimension was theory-driven or exploratory.

### G. Doubly Robust Scores For Policy Value

Lecture 10's orthogonalization logic reappears in policy learning. Under unconfoundedness and overlap, define:

```{math}
:label: eq:em11-nuisance-functions
\mu_d(x)
=
\mathbb E[Y\mid D=d,X=x],
\qquad
e(x)
=
\Pr(D=1\mid X=x).
```

A doubly robust score for policy value is:

```{math}
:label: eq:em11-dr-policy-value
\Gamma_i(\pi)
=
\pi(X_i)
\left[
\widehat\mu_1(X_i)
+ \frac{D_i}{\widehat e(X_i)}
\left(Y_i-\widehat\mu_1(X_i)\right)
\right]
+ \left(1-\pi(X_i)\right)
\left[
\widehat\mu_0(X_i)
+ \frac{1-D_i}{1-\widehat e(X_i)}
\left(Y_i-\widehat\mu_0(X_i)\right)
\right].
```

Then:

```{math}
:label: eq:em11-dr-value-estimator
\widehat V_{DR}(\pi)
=
\frac{1}{n}
\sum_{i=1}^{n}
\Gamma_i(\pi).
```

This score is useful because it connects policy learning back to the Lecture 10 architecture: nuisance functions can be estimated flexibly, sample splitting can reduce overfitting, and policy value can be evaluated on held-out observations. But the score still relies on the causal design. It does not remove unobserved confounding, poor overlap, bad timing, or weak source-to-target comparability.

### H. External Validity, Transportability, And Distribution Shift

When effects vary, external validity becomes a first-order concern. Suppose a rule is learned in source population {math}`S` but is considered for target population {math}`T`. The target value is:

```{math}
:label: eq:em11-target-value
V_T(\pi)
=
\mathbb E_T\left[Y(\pi(X))\right].
```

Even if {math}`V_S(\pi)` is high, {math}`V_T(\pi)` can be low because the target population has different covariates, different treatment effects conditional on covariates, different implementation quality, different prices, different take-up, or different constraints.

A simple target-weighting idea writes:

```{math}
:label: eq:em11-target-weighting
\mathbb E_T[h(X)]
=
\mathbb E_S\left[\omega(X)h(X)\right],
\qquad
\omega(X)
=
\frac{f_T(X)}{f_S(X)}.
```

For policy value, this suggests:

```{math}
:label: eq:em11-weighted-policy-value
V_T(\pi)
\approx
\mathbb E_S\left[
\omega(X)
\left\{\mu_0(X)+\pi(X)\tau(X)\right\}
\right].
```

The approximation is fragile. It requires observed state variables rich enough to describe the source-target difference, common support where {math}`f_S(X)>0` whenever {math}`f_T(X)>0`, and stable potential-outcome functions after conditioning on {math}`X`. Those are substantive assumptions. Allcott's site-selection argument, Vivalt's evidence on generalizing impact evaluations, and Dehejia, Pop-Eleches, and Samii's local-to-global framework all push students to treat external validity as a design problem rather than an afterthought [@Allcott2015; @Vivalt2020; @DehejiaPopElechesSamii2021].

### I. Fairness, Feasibility, And Implementation Constraints

A policy rule can be statistically attractive and still be a bad recommendation. Applied economists should ask:

- Is the information required by the rule observable before assignment?
- Is the rule legal and administratively feasible?
- Does it create disparate impact across protected groups?
- Does it use variables that are proxies for protected status?
- Can workers, firms, schools, or caseworkers game the rule?
- Does the rule change take-up, stigma, search effort, or equilibrium behavior?
- Is the rule robust to staff capacity, local discretion, and political constraints?

Bansak and coauthors' refugee-assignment application is a useful anchor because it makes algorithmic assignment concrete: the object is not merely a prediction score, but an assignment rule with institutional constraints and outcomes that matter for integration [@BansakFerwerdaHainmuellerEtAl2018]. That kind of application should train students to ask where the data come from, which outcomes are optimized, who bears costs, and whether the assignment rule is legitimate.

### J. ML Section Summary

The point of this lecture is not to teach every machine-learning algorithm. The point is to know where common algorithms belong in applied work and where they do not.

```{include} assets/tables/11-ml-algorithm-quick-guide.md
```

The short version is:

- lasso, ridge, and elastic net are mainly shrinkage and nuisance-prediction tools;
- random forests and gradient boosting are powerful tabular prediction tools, but their feature importance measures are not causal;
- causal forests and generalized random forests estimate heterogeneity under a design, not policy optimality by themselves;
- policy trees are useful when the rule must be interpretable;
- SVMs and neural nets are rarely first-choice causal-policy tools for ordinary tabular economics data, though they can be useful for text, images, sequences, or classification;
- clustering is exploratory and descriptive unless linked to a credible causal or structural design.

### K. Diagnostics For Reporting

```{include} assets/tables/11-policy-learning-and-external-validity-diagnostics.md
```

The reporting discipline should be stronger than in a standard heterogeneity section. A credible paper reports the estimand, identifying assumptions, nuisance learners, policy class, value estimator, capacity constraint, validation split, source-target support, subgroup effects, fairness audit, and implementation caveats. If the result is exploratory, say so.

## Research Lab

The Week 11 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. The primary anchor is Kitagawa and Tetenov because the lab reproduces the logic of empirical welfare maximization and treatment choice [@KitagawaTetenov2018]. The secondary challenge anchor is the external-validity literature because students then ask whether a source-trained policy rule travels to a target population [@Allcott2015; @Vivalt2020; @DehejiaPopElechesSamii2021]. Bansak and coauthors provide the applied assignment motivation [@BansakFerwerdaHainmuellerEtAl2018].

### Reproduce

Students work with a deterministic synthetic job-training dataset. They estimate heterogeneous treatment effects and compare four policy rules:

- treat nobody;
- treat everybody;
- a simple baseline-risk threshold;
- a learned score-threshold rule subject to a capacity constraint.

The goal is to reproduce the **policy-learning logic**, not any published estimate:

- estimate outcome and propensity nuisance components;
- construct a doubly robust value score;
- select a feasible rule on a training sample;
- evaluate policy value and regret on a held-out sample;
- compare the learned rule with simple baselines.

### Diagnose

Students decide whether the learned policy is credible:

- Does the targeting rule exploit real heterogeneity or sample noise?
- Is the policy value evaluated honestly out of sample?
- Is overlap adequate for the targeted group?
- Are assignment rates very different across demographic groups?
- How sensitive is the rule to the capacity constraint and policy class?
- Would a simpler rule have nearly the same value with lower implementation burden?

The required memo should distinguish the value of a policy rule from the accuracy of a prediction model.

### Transfer

Students apply the source-trained rule to a shifted target population. The target sample has different covariate distributions and a weaker implementation environment. Students compare:

- source value versus target value;
- unweighted versus target-weighted source value;
- subgroup composition and support in source and target samples;
- fairness and capacity diagnostics after transfer.

The core lesson is that the same heterogeneity estimate may not justify the same policy in a new population. A rule learned in one program site can fail when the target population, treatment technology, budget, take-up, or institutions differ.

Minimum student deliverables are:

1. one Reproduce paragraph defining {math}`\pi(x)`, {math}`V(\pi)`, and the policy class;
2. one Diagnose paragraph interpreting value, regret, overlap, and fairness outputs;
3. one Transfer paragraph explaining whether the learned rule transports to the target population;
4. one final sentence stating what the policy-learning exercise identifies and what it does not identify.

## Methods Box

:::{admonition} Policy learning checklist
:class: note

1. **Name the object.** Is the paper estimating CATEs, discovering subgroups, or choosing a policy rule?
2. **State the design.** What identifies {math}`Y(1)-Y(0)` or policy value?
3. **Define the feasible policy class.** What rules can actually be implemented with pre-assignment information?
4. **Include costs and constraints.** Are there budget, capacity, legal, fairness, or administrative constraints?
5. **Estimate value honestly.** Evaluate {math}`\widehat V(\pi)` on held-out or cross-fit scores, not only in the sample used to choose {math}`\pi`.
6. **Report regret or comparisons.** Compare to treat-all, treat-none, simple rules, and current assignment.
7. **Check overlap where the rule acts.** Targeted units need credible treated and untreated comparisons.
8. **Audit fairness and feasibility.** Statistical optimality does not settle legitimacy or implementation.
9. **Assess transportability.** Compare source and target support, institutions, treatment technology, and constraints.
10. **Separate discovery from deployment.** Exploratory heterogeneity can motivate a rule; it does not by itself justify deployment.
:::

## Reading Ladder And References

```{include} assets/tables/11-reading-architecture.md
```

**First pass: heterogeneity tools.** Review Wager and Athey on causal forests and Athey, Tibshirani, and Wager on generalized random forests [@wagerEstimationInferenceHeterogeneous2018; @atheyGeneralizedRandomForests2019]. These papers connect Lecture 10's heterogeneity tools to the inputs used in Lecture 11.

**Second pass: policy learning.** Read Kitagawa and Tetenov on empirical welfare maximization, then Athey and Wager on policy learning with observational data [@KitagawaTetenov2018; @atheyWager2021].

**Third pass: assignment applications.** Read Bansak and coauthors for a concrete algorithmic-assignment application with institutional constraints [@BansakFerwerdaHainmuellerEtAl2018]. Athey and Imbens are useful for recursive partitioning and the logic of interpretable heterogeneity [@atheyImbens2016].

**External-validity pass.** Read Allcott on site selection bias, Vivalt on how much impact evaluations generalize, and Dehejia, Pop-Eleches, and Samii on local-to-global external validity [@Allcott2015; @Vivalt2020; @DehejiaPopElechesSamii2021].

## Exercises And Discussion Prompts

1. Give one applied setting where heterogeneity is the main research object and one where policy learning is the main object. What changes in the estimand?
2. Explain why {math}`\widehat{\tau}(x)` is not automatically a treatment rule. What additional information is needed?
3. Write the value of a treat-all rule, a treat-none rule, and a threshold rule for a binary treatment.
4. Derive how treatment costs change the simple rule {math}`\pi^*(x)=\mathbf 1\{\tau(x)\ge 0\}`.
5. A model predicts that high-skilled workers have the highest post-training earnings. Why does that not imply they should be targeted?
6. A policy tree has high in-sample value but low held-out value. What diagnostics would you inspect?
7. Suppose a rule targets mostly one demographic group. What fairness and interpretation questions should be reported before deployment?
8. A job-training rule learned in a large city is proposed for a rural region. What source-target comparisons are necessary before claiming external validity?
9. How does weak overlap in the targeted subgroup change the interpretation of policy value?
10. When might a transparent rule with slightly lower estimated value dominate a flexible rule with higher estimated value?

## Reproducibility And Code Lab Note

The canonical Lecture 11 lab folder is:

```text
labs/11-causal-ml-policy-learning-and-external-validity/
```

The lab uses deterministic synthetic data for a job-training policy-learning exercise and a source-to-target transportability exercise. It does not claim to reproduce the published estimates in Kitagawa and Tetenov, Bansak and coauthors, Allcott, Vivalt, or Dehejia, Pop-Eleches, and Samii. The purpose is to make policy value, regret, honest evaluation, fairness audits, and source-target shift concrete.

The smoke path runs:

```bash
ENV_NAME=research bash smoke.sh
```

Expected outputs include policy-value comparisons, learned-rule summaries, subgroup CATE estimates, overlap diagnostics, fairness audits, source-target covariate comparisons, target-weight summaries, transfer-value comparisons, and transfer design prompts.

## Slide Companion Note

The Week 11 slide deck should not duplicate the chapter. It should make the Lecture 10 versus Lecture 11 distinction explicit, define CATEs and policy rules, show policy value and regret, explain empirical welfare maximization, summarize external validity and transportability, surface fairness and implementation constraints, give a compact ML algorithm guide, and end with the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is `slides/week11/11-causal-ml-policy-learning-and-external-validity.tex`.

## Bridge Forward

Lecture 11 closes the core machine-learning block by showing that flexible methods become most useful when tied to economic objects: welfare, constraints, assignment, implementation, and portability. Lecture 12 turns to text as data and computational measurement. The bridge is direct: text and LLM workflows can produce features, labels, and scores that later enter prediction, causal estimation, or policy rules, but they require the same discipline about measurement, validation, and downstream use.
