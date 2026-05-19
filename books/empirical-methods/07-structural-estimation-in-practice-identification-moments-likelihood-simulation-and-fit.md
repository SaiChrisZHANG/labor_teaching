# Lecture 7. Structural Estimation In Practice: Identification, Moments, Likelihood, Simulation, And Fit

## Learning Objectives

By the end of this lecture, students should be able to:

1. map a structural model's primitives to the observed variation that identifies them;
2. distinguish likelihood, method of moments, GMM, simulated method of moments, and indirect inference as practical estimation strategies;
3. explain how weighting matrices, targeted moments, and overidentification shape what a model is forced to explain;
4. evaluate fit, validation evidence, counterfactual discipline, and transparent reporting in structural papers;
5. estimate and report uncertainty using information-matrix logic, OPG/sandwich logic, the delta method, bootstrap methods, cluster or panel resampling, and simulation-aware checks;
6. decide when likelihood is worth its distributional cost, when moments are enough, when simulation is unavoidable, and when a counterfactual has moved too far from identifying support.

## Opening Orientation

Lecture 6 asked when an applied research question requires structure at all. Lecture 7 asks the next question: **how do researchers take a structural model to data credibly?** The answer is not "estimate the most complicated model." The answer is to build a visible chain from observed variation to latent primitives, from latent primitives to model fit, from fit to counterfactual claims, and from counterfactual claims to transparent uncertainty.

This lecture is the second lecture of Block 2: Structural Estimation. It treats estimation as a research-design problem. Likelihood, moments, simulated moments, and indirect inference are not just computational menus. They are choices about which pieces of the data discipline the economic model. A likelihood forces the model to explain a full density. A moments estimator forces the model to explain selected empirical objects. A simulated estimator forces the researcher to make simulation error, numerical approximation, and state-space limits visible. A credible structural paper says why that choice is appropriate for the question.

The paper spine is deliberately practical. Rust shows likelihood-based dynamic discrete-choice estimation in a setting where replacement timing disciplines latent continuation values and costs [@rust1987optimal]. Berry, Levinsohn, and Pakes plus Nevo show why moments, instruments, simulation, fit, and counterfactual discipline became central in applied structural work [@berryLevinsohnPakes1995; @nevo2000maturity]. Todd and Wolpin show how experimental variation can validate a dynamic model before broader policy counterfactuals are taken seriously [@todd2006assessing]. Low, Meghir, and Pistaferri and Adda, Dustmann, and Stevens show how labor and lifecycle questions require moments, dynamics, and uncertainty to be tied directly to the economic object [@low2010wage; @adda2017career]. Newey and McFadden, Pakes and Pollard, Gourieroux, Monfort, and Renault, Murphy and Topel, Keane, and Aguirregabiria and Mira provide the estimation and implementation language [@newey1994large; @pakes1989simulation; @gourieroux1993indirect; @murphy1985estimation; @keane2010structural; @aguirregabiria2010dynamic].

## Core Points

:::{admonition} Core points
:class: important

- Structural credibility comes from the full chain: **identification -> estimation -> fit -> counterfactual discipline -> inference**.
- Identification is a statement about which observed variation disciplines which latent primitive, not a generic property of having a model.
- Likelihood is attractive when the full stochastic model is credible and tractable; moments are attractive when economically meaningful objects are easier to defend than a full density.
- Simulation is useful when the model has no closed-form likelihood or moments, but simulation noise becomes part of the research design.
- Weighting matrices and targeted moments determine the model's empirical obligations. They are substantive choices, not only numerical tuning.
- Fit must include targeted and untargeted objects, validation where possible, and an explicit statement about the distance between the counterfactual and the identifying support.
- Inference is not a footnote. Structural papers should say whether uncertainty comes from a Hessian, OPG/sandwich formula, GMM formula, delta method, bootstrap, cluster bootstrap, two-step correction, or simulation-aware procedure.
:::

## Bridge

Block 1 taught students to ask what comparison identifies a causal estimand. Lecture 6 added the structural question: what latent primitives, dynamic incentives, welfare objects, or counterfactual environments require a model? Lecture 7 keeps both habits. A structural estimator is credible only when the reader can see how the data move the primitives and how the primitives support the target counterfactual.

The central bridge from Lecture 6 is the model-to-data mapping. Suppose the researcher observes choices, outcomes, states, prices, policy rules, or histories, but not preferences, costs, beliefs, technologies, information sets, or welfare. Estimation chooses a criterion that compares observed empirical objects to model-implied objects. The criterion is therefore part of the identification argument. If the paper estimates a schooling model using only enrollment rates, readers should be cautious about wage or fertility counterfactuals unless those objects are also disciplined by data. If the paper estimates a search model using only unemployment durations, accepted-wage counterfactuals need extra validation.

Lecture 8 will move from individual structural estimation to equilibrium structural work. Lecture 7 stays closer to the estimator: likelihood, moments, simulation, fit, and inference.

## Field Core

### A. Identification In Structural Models: Observed Variation Versus Latent Primitives

A structural model is identified when the primitives that matter for the research question are disciplined by variation in the observed data under stated assumptions. This sounds abstract, but the applied checklist is concrete:

1. What primitive is latent?
2. Which observed behavior, transition, outcome, or distribution depends on that primitive?
3. What variation moves that observed object?
4. Could another primitive or omitted state generate the same movement?
5. Which exclusion, normalization, shock, support, or equilibrium assumption breaks the observational equivalence?
6. Which counterfactual uses the primitive most heavily?

The contrast with reduced-form work is useful. A design-based paper often asks whether one observed comparison identifies an effect. A structural paper often asks whether several observed objects jointly identify several latent primitives. In a replacement model, replacement hazards by state help discipline replacement costs and maintenance costs, while state transitions discipline continuation values. In a schooling model, enrollment, wages, grade progression, household composition, and policy variation may jointly discipline schooling preferences, skill accumulation, constraints, and fertility-schooling tradeoffs. In a lifecycle risk model, earnings dynamics, labor supply, savings, and employment transitions jointly discipline wage risk, employment risk, insurance, and preferences.

A compact way to write the identification problem is:

```{math}
:label: eq:em7-data-map
\underbrace{\widehat h_N(Y_i,X_i,S_i,P_i)}_{\text{empirical objects}}
\quad \Longleftrightarrow \quad
\underbrace{h(\theta; \mathcal M)}_{\text{model-implied objects from primitives}},
```

where {math}`Y_i` are outcomes, {math}`X_i` are covariates, {math}`S_i` are states or histories, {math}`P_i` are prices or policy rules, {math}`\theta` are latent primitives, and {math}`\mathcal M` denotes the maintained model. Identification asks whether the mapping from {math}`\theta` to {math}`h(\theta; \mathcal M)` is sufficiently informative over the observed support.

The hardest structural identification problems arise when different primitives predict similar behavior. High unemployment durations could reflect low offer arrival rates, high reservation wages, search costs, benefit generosity, beliefs, skill depreciation, or demand conditions. Low schooling could reflect tuition, liquidity constraints, preferences, expected returns, family shocks, or local labor demand. A credible structural paper does not hide this. It explains which moments separate these mechanisms and which parameters remain normalized, calibrated, weakly identified, or sensitivity-tested.

```{include} assets/tables/07-structural-estimation-diagnostics.md
```

### B. Likelihood, Moments, GMM, SMM, And Indirect Inference

The estimator defines how the model meets the data. The same economic model can be estimated with a full likelihood, a set of moments, simulated moments, or auxiliary statistics. The right choice depends on the question, the model's tractability, the credibility of distributional assumptions, and the empirical objects that readers need to see.

#### Likelihood-Based Estimation

If the structural model implies a density or probability for the observed data, maximum likelihood chooses parameters that make the observed sample most likely:

```{math}
:label: eq:em7-likelihood
\widehat\theta_{\mathrm{ML}}
=
\arg\max_{\theta\in\Theta}
\ell_N(\theta)
=
\arg\max_{\theta\in\Theta}
\sum_{i=1}^N \log f_\theta(y_i \mid x_i,s_i,p_i).
```

For panel or dynamic choice data, the likelihood often factors into choice probabilities, transition probabilities, and outcome densities:

```{math}
:label: eq:em7-dynamic-likelihood
\ell_N(\theta)
=
\sum_{i=1}^N\sum_{t=1}^{T_i}
\left[
\log \Pr_\theta(a_{it}\mid s_{it},p_{it})
+
\log f_\theta(y_{it},s_{i,t+1}\mid a_{it},s_{it},p_{it})
\right].
```

Likelihood is useful when the researcher can defend the full stochastic model and solve the model reliably. It can be efficient under correct specification because it uses the full density. The cost is that misspecified shocks, measurement error, transition laws, or latent-type distributions can move the estimates. In practice, likelihood-based structural work should report the state space, the likelihood contribution, treatment of initial conditions, latent heterogeneity, numerical optimizer, convergence checks, and whether the reported likelihood includes all observed objects or only selected pieces.

The score condition is:

```{math}
:label: eq:em7-score
\frac{1}{N}\sum_{i=1}^N
s_i(\widehat\theta)
=
\frac{1}{N}\sum_{i=1}^N
\frac{\partial \log f_{\widehat\theta}(y_i \mid x_i,s_i,p_i)}
{\partial \theta}
=0.
```

This score equation makes the connection to moments visible: likelihood estimation is also a moment condition, but the moments are scores implied by the full probability model.

#### Method Of Moments And GMM

Many structural papers do not want to commit to a full density. They instead choose moments that are economically meaningful and informative for the primitives. Let {math}`g_i(\theta)` be a vector of moment functions such that:

```{math}
:label: eq:em7-moment-condition
\mathbb E[g_i(\theta_0)] = 0.
```

The sample moments are:

```{math}
:label: eq:em7-sample-moments
\widehat g_N(\theta)
=
\frac{1}{N}\sum_{i=1}^N g_i(\theta).
```

GMM chooses parameters that make the sample moments close to zero:

```{math}
:label: eq:em7-gmm
\widehat\theta_{\mathrm{GMM}}
=
\arg\min_{\theta\in\Theta}
Q_N(\theta)
=
\arg\min_{\theta\in\Theta}
\widehat g_N(\theta)' W_N \widehat g_N(\theta).
```

In structural applications, the moments may be written as a difference between empirical and model-implied objects:

```{math}
:label: eq:em7-moment-match
\widehat g_N(\theta)
=
\widehat m_N^{data} - m^{model}(\theta).
```

This makes the applied interpretation transparent. If the moments are employment rates by age, wage growth by experience, transition rates across states, choice shares by price bins, or distributional quantiles, then readers can see which empirical objects the model is being forced to explain.

GMM is preferable when targeted moments are more defensible than a full joint density, when the model is complex but produces interpretable empirical analogues, or when the question centers on a limited set of primitives. Its weakness is that the moment set can omit behavior that matters for the counterfactual.

#### Simulated Method Of Moments

When {math}`m^{model}(\theta)` has no closed form, the researcher simulates the model. Let {math}`u_r` denote simulation draws and {math}`R` the number of simulated samples. The simulated moment analogue is:

```{math}
:label: eq:em7-simulated-moments
\widehat m_R^{sim}(\theta)
=
\frac{1}{R}\sum_{r=1}^R m(y_r^{sim}(\theta,u_r)).
```

The simulated method of moments criterion is:

```{math}
:label: eq:em7-smm
\widehat\theta_{\mathrm{SMM}}
=
\arg\min_{\theta\in\Theta}
\left[
\widehat m_N^{data}
-
\widehat m_R^{sim}(\theta)
\right]'
W_N
\left[
\widehat m_N^{data}
-
\widehat m_R^{sim}(\theta)
\right].
```

SMM is valuable when the model is easy to simulate but hard to integrate analytically. Dynamic career models, lifecycle models, search models, and heterogeneous-agent models often use this logic. The implementation caveat is sharp: simulation error is not decorative noise. It can change the criterion surface, produce local minima, and make reported standard errors too optimistic. Applied papers should say how many simulation draws are used, whether common random numbers are held fixed across parameter values, whether estimates are stable across seeds, and whether simulation error is small relative to sampling error [@pakes1989simulation].

#### Indirect Inference

Indirect inference is useful when the structural model is simulable but a direct likelihood or direct moment mapping is awkward. The researcher estimates an auxiliary model or statistic {math}`a(\cdot)` on the real data and on simulated data, then chooses structural parameters so the auxiliary objects align:

```{math}
:label: eq:em7-indirect
\widehat\theta_{\mathrm{II}}
=
\arg\min_{\theta\in\Theta}
\left[
\widehat a_N^{data}
-
\widehat a_R^{sim}(\theta)
\right]'
W_N
\left[
\widehat a_N^{data}
-
\widehat a_R^{sim}(\theta)
\right].
```

The auxiliary model can be a reduced-form regression, a hazard model, a transition matrix, a set of distributional statistics, or another estimator whose behavior is easy to explain. The advantage is communication: readers often understand the auxiliary statistics. The danger is that the auxiliary statistics may not capture the behavioral margins that matter for the structural counterfactual [@gourieroux1993indirect].

```{include} assets/tables/07-estimation-workflow-map.md
```

### C. Weighting Matrices, Overidentification, And Targeted Moments

Moments-based estimation makes the moment choice visible, but it also creates a new responsibility: the researcher must explain the weighting matrix. The GMM weighting matrix {math}`W_N` determines which discrepancies the criterion punishes most. If all moments are equally weighted even though some are noisy and some are precise, the estimator may chase noise. If the inverse variance matrix is used mechanically, the estimator may put high weight on precise but substantively peripheral moments. Both choices are research choices.

Let:

```{math}
:label: eq:em7-moment-covariance
S
=
\mathbb E[g_i(\theta_0)g_i(\theta_0)'].
```

The asymptotically efficient weighting matrix for a correctly specified GMM problem is:

```{math}
:label: eq:em7-optimal-weight
W^\ast = S^{-1}.
```

In practice, researchers often use a two-step procedure: estimate with a simple weighting matrix, estimate the moment covariance at the preliminary estimate, then re-estimate with {math}`\widehat S^{-1}`. This is efficient asymptotically, but it can be unstable when moments are many, highly correlated, weakly informative, or simulated with noise. A transparent paper reports the baseline moment list, moment scaling, weighting matrix, sensitivity to alternative weights, and whether any moments dominate the criterion.

Overidentification means there are more moments than parameters. This is useful because the model cannot match everything by construction. The overidentifying restrictions statistic is:

```{math}
:label: eq:em7-j-stat
J_N
=
N\,\widehat g_N(\widehat\theta)'
\widehat W_N
\widehat g_N(\widehat\theta).
```

Under standard regularity conditions and correct specification, {math}`J_N` has an asymptotic chi-square distribution with degrees of freedom equal to the number of moments minus the number of estimated parameters. The applied interpretation should be cautious. A rejected overidentification test may reveal misspecification, poor measurement, simulation noise, or an overly ambitious moment set. A non-rejection does not prove the counterfactual is credible, especially when moments are weak or few.

Targeted moments also define the scope of trust. If a dynamic schooling model targets enrollment and grade progression but not wages, then wage counterfactuals need external validation. If a lifecycle model targets wage variance but not employment transitions, then employment-risk counterfactuals are weak. If a demand model targets market shares but not substitution patterns, merger or price counterfactuals are fragile. The moment table is therefore the empirical contract of the structural paper.

### D. Fit, Validation, Counterfactual Discipline, And Transparent Reporting

Good structural fit is not one number. It is a disciplined comparison between the model and the empirical objects that matter for the question. The minimum reporting package should include:

- targeted moments and their model-implied counterparts;
- untargeted moments that matter for the counterfactual;
- distributional fit, not only means, when heterogeneity is central;
- qualitative comparative statics that the model should get right;
- sensitivity to moment sets, weighting matrices, calibrated parameters, initial conditions, and latent-type choices;
- validation against experimental, quasi-experimental, holdout, or out-of-sample variation when available;
- a statement about how far the counterfactual moves from observed support.

Todd and Wolpin are a useful validation anchor because the model is assessed against experimental variation before being used for broader schooling-policy simulations [@todd2006assessing]. The general lesson is wider than that paper: validation is most persuasive when it asks the model to predict behavior that was not directly targeted during estimation but is close to the counterfactual margin.

Counterfactual discipline begins by naming what changes and what stays fixed. Suppose a policy changes from {math}`p_0` to {math}`p_1`. A structural estimate maps primitives into decision rules, transition laws, outcomes, and welfare:

```{math}
:label: eq:em7-counterfactual-map
\widehat\theta
\quad\Longrightarrow\quad
\left\{
\sigma_{\widehat\theta}(a\mid s;p),
F_{\widehat\theta}(s'\mid s,a;p),
Y_{\widehat\theta}(p),
W_{\widehat\theta}(p)
\right\}.
```

The counterfactual claim is:

```{math}
:label: eq:em7-counterfactual-effect
\widehat\Delta_Y(p_1,p_0)
=
\frac{1}{N}\sum_{i=1}^N
\left[
Y_i(p_1;\widehat\theta)-Y_i(p_0;\widehat\theta)
\right].
```

This object can be useful precisely because {math}`Y_i(p_1)` may not be observed. It is credible only if the primitives and behavioral rules used to simulate {math}`p_1` are disciplined for that margin. Counterfactuals close to observed price variation, policy variation, or state transitions are usually easier to defend. Counterfactuals that change the menu, information set, equilibrium environment, or support of state variables need stronger validation and more explicit caveats.

Transparent reporting should also separate primitive parameters from policy objects. Readers need to know whether a conclusion depends on one tightly identified primitive, a combination of weakly identified primitives, a calibrated discount factor, a normalized utility scale, or a simulated equilibrium closure.

```{include} assets/tables/07-theory-to-applied-bridge.md
```

### E. Variance Estimation And Inference

Structural estimation does not end with a point estimate. The reader needs uncertainty for primitive parameters, model-implied moments, elasticities, welfare objects, and counterfactuals. The right variance estimator depends on the estimator, the dependence structure, the number of moments, the simulation design, and the smoothness of the counterfactual function.

#### Hessian And Information Matrix

For likelihood-based models, a classical variance approximation uses curvature of the log likelihood. Let:

```{math}
:label: eq:em7-hessian
\widehat A
=
-
\frac{1}{N}
\sum_{i=1}^N
\frac{\partial^2 \log f_{\widehat\theta}(y_i\mid x_i,s_i,p_i)}
{\partial\theta\partial\theta'}.
```

Under correct specification and standard regularity conditions:

```{math}
:label: eq:em7-information-var
\widehat{\operatorname{Var}}(\widehat\theta)
\approx
\frac{1}{N}\widehat A^{-1}.
```

This is fast and common. It can be fragile when the likelihood is misspecified, the optimizer is near a boundary, the criterion surface is flat, finite-sample behavior is poor, or numerical derivatives are unstable.

#### OPG And Sandwich Logic

The outer product of gradients uses scores:

```{math}
:label: eq:em7-opg
\widehat B
=
\frac{1}{N}\sum_{i=1}^N
s_i(\widehat\theta)s_i(\widehat\theta)'.
```

The sandwich variance is:

```{math}
:label: eq:em7-sandwich
\widehat{\operatorname{Var}}(\widehat\theta)
\approx
\frac{1}{N}
\widehat A^{-1}\widehat B\widehat A^{-1}.
```

The sandwich form is useful for M-estimators and quasi-likelihood settings because it separates curvature from score variability. In panel, market, classroom, firm, or geography settings, {math}`\widehat B` should be built at the independent sampling level. If workers are nested in firms, students in schools, or observations in policy clusters, iid score sums can understate uncertainty.

#### GMM Asymptotic Variance

For GMM, let:

```{math}
:label: eq:em7-gmm-jacobian
G
=
\mathbb E
\left[
\frac{\partial g_i(\theta_0)}
{\partial\theta'}
\right],
\qquad
S
=
\mathbb E[g_i(\theta_0)g_i(\theta_0)'].
```

The generic GMM variance sketch is:

```{math}
:label: eq:em7-gmm-var
\operatorname{Avar}(\widehat\theta)
=
\frac{1}{N}
\left(G'WG\right)^{-1}
G'WSWG
\left(G'WG\right)^{-1}.
```

With the optimal weighting matrix {math}`W=S^{-1}`, this simplifies to:

```{math}
:label: eq:em7-gmm-opt-var
\operatorname{Avar}(\widehat\theta)
=
\frac{1}{N}
\left(G'S^{-1}G\right)^{-1}.
```

These formulas are helpful, but applied researchers should not present them as magic. They require stable moment Jacobians, enough support, appropriate clustering or dependence adjustment, and a criterion that is smooth enough for local linearization to be informative [@newey1994large].

#### Delta Method For Counterfactual Functions

Many structural objects are functions of parameters rather than parameters themselves. Let a welfare measure, elasticity, or counterfactual effect be:

```{math}
:label: eq:em7-counterfactual-function
\tau = \psi(\theta).
```

The delta method uses a first-order approximation:

```{math}
:label: eq:em7-delta-expansion
\psi(\widehat\theta)
\approx
\psi(\theta_0)
+
\nabla_\theta\psi(\theta_0)'
(\widehat\theta-\theta_0).
```

The estimated variance is:

```{math}
:label: eq:em7-delta-var
\widehat{\operatorname{Var}}(\psi(\widehat\theta))
\approx
\widehat D_\psi
\widehat{\operatorname{Var}}(\widehat\theta)
\widehat D_\psi',
\qquad
\widehat D_\psi
=
\left.
\frac{\partial \psi(\theta)}
{\partial\theta'}
\right|_{\theta=\widehat\theta}.
```

The delta method is often practical for elasticities, welfare measures, and counterfactual summaries. It is less reliable when the counterfactual is highly nonlinear, the parameter is weakly identified, the optimum is near a boundary, or the model simulation creates discontinuities.

#### Bootstrap And Resampling Logic

The bootstrap estimates uncertainty by repeatedly resampling the data, re-estimating the model, and studying the empirical distribution of the estimator. A generic bootstrap draw is:

```{math}
:label: eq:em7-bootstrap
\widehat\theta^{*(b)}
=
\widehat\theta(Y_1^{*(b)},\ldots,Y_N^{*(b)}),
\qquad
b=1,\ldots,B.
```

The bootstrap variance estimate is:

```{math}
:label: eq:em7-bootstrap-var
\widehat{\operatorname{Var}}^\ast(\widehat\theta)
=
\frac{1}{B-1}
\sum_{b=1}^B
\left(
\widehat\theta^{*(b)}
-
\bar\theta^\ast
\right)
\left(
\widehat\theta^{*(b)}
-
\bar\theta^\ast
\right)'.
```

The same logic applies to a counterfactual function:

```{math}
:label: eq:em7-bootstrap-function
\widehat F^\ast_\psi(t)
=
\frac{1}{B}
\sum_{b=1}^B
\mathbf 1
\left\{
\psi(\widehat\theta^{*(b)}) \le t
\right\}.
```

The bootstrap is attractive when the estimator is multi-step, nonlinear, simulation-based, or analytically awkward. It is expensive because the full model must be re-estimated many times. It can also be misleading under weak identification, non-smooth objectives, unstable optimization, or the wrong resampling scheme.

For structural work with dependence, resampling must occur at the right level. In worker-firm panels, resample workers, firms, matches, or clusters according to the sampling design and source of variation. In market-level demand models, resample markets or clusters, not individual product observations if market shocks are shared. In dynamic panels, block or cluster resampling may be needed to preserve histories. In simulated models, use common random numbers when comparing parameter values, report sensitivity across simulation seeds, and separate sampling uncertainty from simulation noise.

#### Two-Step And Generated-Regressor Concerns

Structural estimators often use first-stage objects: wage processes, policy-rule estimates, transition matrices, propensity scores, text-derived measures, or estimated choice probabilities. Treating these as known can understate uncertainty. Murphy and Topel give the classic warning for two-step estimators [@murphy1985estimation]. The applied rule is simple: if a generated object materially enters the structural criterion or counterfactual, report whether the standard errors incorporate its uncertainty. A bootstrap that re-runs the full first-stage and second-stage pipeline is often the most transparent teaching solution, although it can be computationally costly.

```{include} assets/tables/07-variance-estimation-toolkit.md
```

### F. Practical Decision Rules

**Prefer likelihood when** the full stochastic structure is credible, the model implies a tractable density, the distributional assumptions are central to the economic story, and efficiency matters. Likelihood is also natural when individual histories and transitions can be written as a coherent probability model. Report the likelihood contribution, initial conditions, latent heterogeneity, state-space solution, optimizer, convergence, and curvature diagnostics.

**Prefer moments or GMM when** the research question can be disciplined by interpretable empirical objects and a full density would require questionable assumptions. Moments are often easier to communicate because the reader can see the target: wage growth by experience, choice shares by prices, transition rates by state, employment rates by age, savings distributions, or policy-response slopes. Report the full moment list, scaling, weighting matrix, sensitivity to weights, targeted versus untargeted fit, and overidentification diagnostics.

**Prefer simulation when** the model is analytically intractable but produces realistic simulated histories. Simulation is common in dynamic, lifecycle, heterogeneous-agent, and equilibrium settings. Report the number of draws, random seeds, use of common random numbers, approximation choices, state-space discretization, optimizer behavior, and whether simulation noise is small enough for inference.

**Prefer indirect inference when** direct estimation is hard but there is a clear auxiliary representation whose coefficients or statistics capture the behavioral margins that matter. The auxiliary model should be chosen for economic relevance, not convenience alone.

**Treat fit as convincing when** the model matches targeted moments, performs reasonably on untargeted objects linked to the counterfactual, gets key comparative statics right, survives transparent sensitivity checks, and is validated against independent variation when possible.

**Treat fit as weak when** the model only fits averages, misses state-specific behavior, cannot match transitions, relies on moments unrelated to the counterfactual, has unstable estimates across weighting matrices or seeds, or uses a counterfactual that changes incentives far outside observed support.

```{include} assets/tables/07-variance-bootstrap-and-inference.md
```

### G. Theory-To-Applied: How Structural Estimation Becomes An Applied Economics Paper

A structural paper becomes persuasive when the economic question, identifying variation, estimation strategy, fit evidence, counterfactual, and inference all point at the same object. The following anchors are useful because each one makes a different implementation choice visible.

**Rust.** The economic question is how replacement costs and continuation values shape dynamic maintenance decisions. The observed variation is replacement timing across mileage states and transition behavior after continuation or replacement. The likelihood is natural because the dynamic discrete-choice model implies state-specific choice probabilities and transition components. Fit is assessed by comparing observed and model-implied replacement behavior across states. The credible counterfactuals are close to the replacement-cost and maintenance-cost margins disciplined by the model; broad counterfactuals about new technologies or unmodeled operating environments would need additional validation. Uncertainty should be read through the likelihood curvature, model specification, and sensitivity to transitions and state support [@rust1987optimal].

**Berry, Levinsohn, and Pakes; Nevo.** The economic question is how differentiated-product demand and supply primitives support price, merger, or policy counterfactuals. The identifying variation comes from market shares, product characteristics, prices, instruments, substitution patterns, and market-level variation. Moments and simulation are natural because random-coefficients demand generates market-level moments and integrals that are easier to simulate than to express in closed form. Fit is not only share fit; credible counterfactuals require substitution patterns, elasticities, and price-cost implications to be plausible. The implementation lesson for labor students is not that every structural paper should become an industrial-organization paper. It is that moments, instruments, simulation, local minima, and counterfactual validation are part of one credibility chain [@berryLevinsohnPakes1995; @nevo2000maturity].

**Todd and Wolpin.** The economic question is how a schooling subsidy changes schooling and fertility behavior beyond the exact experimental rule. The identifying variation includes policy-experimental variation and household behavior over time. The structural model is useful because the policy changes dynamic paths, not only a one-period outcome. Fit and validation are central: the experiment is used to assess whether the model can reproduce policy responses before using it for broader counterfactuals. Uncertainty should be interpreted with attention to the dynamic model, the validation exercise, and the counterfactual distance from observed policy variation [@todd2006assessing].

**Low, Meghir, and Pistaferri.** The economic question is how wage risk and employment risk affect lifecycle labor supply and insurance. The identifying variation comes from earnings dynamics, employment transitions, labor supply, and lifecycle histories. Moments are attractive because the target primitives are risk processes, preferences, and insurance mechanisms, not a single full-density object. Fit must be judged against lifecycle profiles and risk-related behavior. Counterfactuals are credible when they operate on the risk and insurance margins disciplined by those moments [@low2010wage].

**Adda, Dustmann, and Stevens.** The economic question is how children affect women's careers over the lifecycle. The observed data include fertility timing, employment, wages, and career histories. The model is useful because the costs unfold dynamically and interact with choices over time. Simulation and moments help connect observed histories to latent preferences, constraints, and career processes. Fit must be state-specific and dynamic; a model that matches average employment but misses persistence or wage paths would be weak for career-cost counterfactuals [@adda2017career].

The common template is:

1. define the economic question and counterfactual;
2. name the latent primitives;
3. show the data variation that disciplines each primitive;
4. choose likelihood, moments, simulation, or auxiliary statistics for a reason;
5. report targeted and untargeted fit;
6. report uncertainty for primitives and counterfactuals;
7. state where the counterfactual is close to support and where it extrapolates.

## Research Lab

The Lecture 7 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a reduced synthetic teaching path. It is inspired by the estimation logic in Rust and by dynamic/lifecycle applications such as Todd and Wolpin and Adda, Dustmann, and Stevens, but it is not an official replication package and does not claim to reproduce published magnitudes [@rust1987optimal; @todd2006assessing; @adda2017career].

**Reproduce.** Students estimate a small Rust-style replacement model on deterministic synthetic panel data. They compute empirical replacement moments by state, estimate a likelihood-style dynamic choice model, estimate a moments/GMM analogue, compare targeted fit, and calculate a replacement-cost counterfactual.

**Diagnose.** Students inspect which mileage-state variation identifies replacement and maintenance primitives, which moments carry the criterion, how the weighting matrix changes the estimates, whether untargeted state support is good enough, how simulation noise affects an SMM analogue, and how cluster bootstrap and delta-method uncertainty compare for a counterfactual.

**Transfer.** Students move to a small lifecycle schooling/work simulation. The transfer anchor is dynamic human-capital and lifecycle structure rather than an exact frontier replication. Students estimate a simulated-moments teaching model for schooling responses, run a tuition-subsidy counterfactual, and write a memo about which moments discipline preferences, which objects remain assumed, and why full validation would require richer data.

The bounded lab is pedagogically realistic because it makes the full credibility chain executable: identification, estimation, fit, counterfactual discipline, and inference.

## Methods Box

### A Practical Structural Estimation Checklist

1. **Start from the paper's economic object.** State the policy, welfare, or behavioral counterfactual before choosing an estimator.
2. **Make the data map explicit.** List observed choices, outcomes, states, prices, policies, and histories. Then list latent preferences, costs, beliefs, technologies, constraints, and shocks.
3. **Connect each primitive to variation.** For every key parameter, say which moment, likelihood component, transition, price variation, policy rule, or experiment disciplines it.
4. **Choose the estimator for a reason.** Likelihood uses a full density; GMM uses selected moments; SMM simulates intractable objects; indirect inference matches auxiliary statistics.
5. **Scale and weight moments transparently.** Poor scaling can make a criterion arbitrary. Optimal weights can overemphasize precise but substantively minor moments.
6. **Separate targeted from untargeted fit.** A model should not be praised only for matching the moments it was told to match.
7. **Report counterfactual distance.** Say which support, price range, policy variation, state distribution, or equilibrium condition anchors the counterfactual.
8. **Report uncertainty for the object readers use.** A table of primitive standard errors is incomplete if the paper's conclusion depends on a welfare effect or policy simulation.
9. **Respect dependence.** Cluster or block resampling should follow the sampling and identification structure.
10. **Track numerical approximation.** Record state grids, tolerances, optimizer starts, simulation draws, random seeds, convergence failures, and sensitivity checks.

## Reading Ladder And References

```{include} assets/tables/07-reading-architecture.md
```

**Orientation.** Start with Keane and Aguirregabiria and Mira for the broad structural-estimation landscape and the dynamic discrete-choice toolkit [@keane2010structural; @aguirregabiria2010dynamic].

**Likelihood and dynamic choice.** Read Rust with Hotz and Miller. Rust is the canonical likelihood-based dynamic discrete-choice benchmark, while Hotz and Miller show why conditional choice probabilities can reduce computational burden [@rust1987optimal; @hotz1993conditional].

**Moments, simulation, and indirect inference.** Read Newey and McFadden for large-sample estimation and GMM logic, Pakes and Pollard for simulation estimators, and Gourieroux, Monfort, and Renault for indirect inference [@newey1994large; @pakes1989simulation; @gourieroux1993indirect].

**Moments and counterfactual discipline.** Read Berry, Levinsohn, and Pakes with Nevo for differentiated-products demand as a clean example of moments, instruments, simulation, fit, and policy counterfactuals [@berryLevinsohnPakes1995; @nevo2000maturity].

**Labor and lifecycle anchors.** Read Todd and Wolpin, Low, Meghir, and Pistaferri, and Adda, Dustmann, and Stevens for labor-facing dynamic structural work where validation, moments, and counterfactual discipline matter [@todd2006assessing; @low2010wage; @adda2017career].

**Inference.** Read Murphy and Topel when first-stage or generated objects enter the structural estimator, and return to Newey and McFadden for the shared M-estimation and GMM language [@murphy1985estimation; @newey1994large].

## Exercises And Discussion Prompts

1. Choose a structural paper and write its identification map: latent primitives, observed objects, identifying variation, and key assumptions.
2. When would a full likelihood be more convincing than GMM? When would it be less convincing?
3. Write a GMM criterion for a job-search model using unemployment duration, accepted wages, and re-employment rates. Which moments discipline which primitives?
4. Explain why the optimal weighting matrix {eq}`eq:em7-optimal-weight` is not automatically the best persuasive weighting matrix in a small applied sample.
5. Give an example where a model can fit targeted moments well but still fail for the intended counterfactual.
6. In an SMM estimator, why might common random numbers help the optimizer? Why do they not solve identification?
7. Compare the delta method in {eq}`eq:em7-delta-var` with the bootstrap in {eq}`eq:em7-bootstrap-var` for a nonlinear welfare counterfactual.
8. Design a cluster bootstrap for a worker-firm structural model. What is the independent sampling unit, and why?
9. Name a two-step structural estimation problem where first-stage uncertainty would be easy to underreport.
10. Write a referee-style paragraph evaluating whether a structural counterfactual is close enough to the variation that identifies the primitives.

## Reproducibility And Code Lab Note

The canonical Lecture 7 lab path is:

`labs/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit/`

The lab uses Python and deterministic synthetic teaching data. The smoke path creates a reduced replacement panel, estimates likelihood and moments versions of a small dynamic choice model, writes targeted and untargeted fit diagnostics, runs cluster bootstrap and delta-method counterfactual uncertainty, checks simulation-noise sensitivity for SMM, and then transfers the same logic to a simulated lifecycle schooling/work setting.

The lab is intentionally conservative. It does not claim official replication of Rust, Todd and Wolpin, or Adda, Dustmann, and Stevens. Its purpose is to make structural implementation choices visible and testable in a bounded local workflow.

## Slide Companion Note

The canonical Lecture 7 slide path is:

`slides/week7/07-structural-estimation-in-practice-identification-moments-likelihood-simulation-and-fit.tex`

The deck mirrors the chapter without duplicating it. It defines the identification problem, compares likelihood, moments, simulation, and indirect inference, explains weighting matrices and targeted moments, summarizes fit and counterfactual discipline, gives a compact inference slide, maps theory to applied examples, lists credibility threats, and closes with the Research Lab design.

## Bridge Forward

Lecture 7 explains how researchers estimate, validate, and report uncertainty for structural models in practice. Lecture 8 extends the same discipline to equilibrium structural work. The next challenge is that individual primitives are no longer the only objects to discipline. Prices, firms, markets, locations, matching, and equilibrium feedback become part of the identification, fit, counterfactual, and inference problem.
