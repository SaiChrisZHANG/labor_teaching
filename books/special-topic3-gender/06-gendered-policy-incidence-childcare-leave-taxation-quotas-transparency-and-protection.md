# Gendered Policy Incidence: Childcare, Leave, Taxation, Quotas, Transparency, And Protection

Gender-related policy belongs in a labor course because the policies in this week operate through labor-market margins: participation, hours, attachment, wages, promotions, authority, sorting, safety, care allocation, and firm organization. The point is not to build a policy shop. The point is to learn how to use policy variation to understand gendered labor-market mechanisms.

The organizing question is therefore sharper than "did the gap close?" A reform can reduce an observed wage gap by compressing men's bonus growth, raise employment by shifting care to fathers, increase representation at the top without changing the pipeline beneath it, or improve welfare even when the measured wage gap barely moves. Incidence and margins matter because gender policy is mediated by households, firms, coworkers, markets, and future careers.

:::{admonition} Core points
:class: important

- Gender-related policies move different margins: participation, hours, attachment, pay, promotion, authority, sorting, care allocation, safety, and welfare.
- Incidence can fall on workers, firms, coworkers, households, children, and future careers rather than only on the nominal beneficiary.
- Firm response, implementation, and compliance are part of the treatment, not background noise.
- Welfare improvement is not the same object as average gap reduction.
- Policy variation can identify deeper labor mechanisms: time constraints, second-earner elasticities, bargaining, care allocation, promotion pipelines, pay-setting, legal credibility, and firm adjustment.

:::

## Learning Objectives

By the end of Week 6, students should be able to:

1. map a gender-related policy to the labor-market margins it can move;
2. distinguish average treatment effects on outcomes from incidence, equilibrium response, and welfare;
3. explain why firms are central actors in policy incidence rather than passive recipients of regulation;
4. compare childcare, leave, tax, quota, transparency, equal-pay, and protection policies as mechanisms and identification devices;
5. read policy papers by naming the treatment, treated unit, comparison group, margin, likely incidence, and mechanism claim;
6. design a research project that uses policy variation to identify a gendered labor-market mechanism without confusing policy evaluation with mechanism identification.

## Opening Orientation

This module orients the economic question, the labor-market object, and the empirical design issues before the layered sections begin.

## Bridge

Weeks 2 through 5 built the mechanisms that Week 6 now stress-tests. Week 2 showed that paid work is embedded in household production, care allocation, fertility timing, and bargaining. Week 3 showed that early choices, skills, aspirations, information, and occupational sorting shape the feasible set before workers reach firms. Week 4 moved inside organizations, where hiring, supervision, task allocation, pay-setting, promotion, authority, retention, and workplace conditions convert worker characteristics into careers. Week 5 added norms, identity, bargaining, and institutions: the social rules and expectations that can survive even when prices or formal laws change.

Policies are useful because they shift some of those constraints while leaving others visible. A childcare subsidy tests how much employment is constrained by care time, but it may also reveal whether care responsibilities are reallocated within households. A parental-leave reform tests whether attachment around birth is a key margin, but it may also expose promotion penalties if firms treat leave as a signal of lower future availability. Separate taxation tests secondary-earner incentives, but household bargaining and social norms mediate the response. Board quotas test leadership bottlenecks, but top-level representation may not move the broader pipeline. Pay transparency and equal-pay rules test firm pay-setting, but firms may adapt through bonuses, promotion timing, job classification, or workforce composition.

That is the point of the week. Policy is not a list of interventions to support or oppose. Policy is a set of shocks to a gendered labor-market system.

## Field Core

### A Policy-Incidence Framework

A policy evaluation often begins with an average treatment effect:

```{math}
:label: eq-week6-ate
\tau_m
=
E\!\left[Y_i^m(P_1)-Y_i^m(P_0)\right],
```

where {math}`Y_i^m` is outcome margin {math}`m` for worker or household {math}`i`, and {math}`P_1` and {math}`P_0` are the treated and untreated policy regimes. The margin {math}`m` matters. A policy can have a positive effect on employment, no effect on hourly wages, a negative effect on promotion probability, and an ambiguous effect on welfare. Calling all of these "the effect of the policy" hides the labor economics.

For this week, separate four objects:

1. **Average treatment effects on outcomes.** Did the policy change employment, hours, wages, bonuses, retention, promotions, fertility, safety, reporting, or child outcomes?
2. **Incidence.** Who receives the benefit or bears the cost after households, firms, coworkers, and markets adjust?
3. **Equilibrium and firm response.** How do firms change pay, staffing, schedules, job classifications, promotion criteria, hiring, compliance, reporting systems, or workplace organization?
4. **Welfare.** Does the reform improve utility, autonomy, insurance, safety, child welfare, household resources, firm surplus, or allocative efficiency?

A compact way to write the incidence problem is:

```{math}
:label: eq-week6-incidence-map
\Delta Y_{ifh}^m
=
\Delta Y_{ifh}^{m,\text{worker}}
+ \Delta Y_{ifh}^{m,\text{household}}
+ \Delta Y_{ifh}^{m,\text{firm}}
+ \Delta Y_{ifh}^{m,\text{coworker}}
+ \Delta Y_{ifh}^{m,\text{market}},
```

where {math}`i` is a worker, {math}`f` is a firm, {math}`h` is a household, and {math}`m` is the margin. The decomposition is not an estimator by itself. It is a discipline for interpretation. A childcare subsidy may move a worker component through lower time costs, a household component through reallocation of care, a firm component through changed schedules, and a market component through changes in wages or childcare prices. A transparency law may move pay-setting inside the firm, but its measured incidence can include slower wage growth for men, compression of bonuses, changes in retention, or shifts in hiring.

An explicit welfare object clarifies why gap reduction is not enough:

```{math}
:label: eq-week6-welfare-object
W(P)
=
\sum_i \omega_i U_i(c_i,h_i,\ell_i,a_i,s_i;P)
+ \sum_h \omega_h B_h(P)
+ \sum_f \omega_f \Pi_f(P)
+ \sum_k \omega_k C_k(P)
- \lambda G(P).
```

Here {math}`U_i` is worker utility over consumption {math}`c_i`, hours {math}`h_i`, nonmarket time {math}`\ell_i`, autonomy or authority {math}`a_i`, and safety or dignity {math}`s_i`; {math}`B_h` captures household allocation and bargaining; {math}`\Pi_f` is firm surplus; {math}`C_k` captures child or dependent outcomes; and {math}`G(P)` is the fiscal, administrative, or compliance cost. The weights are normative and often unstated in empirical papers. The equation is useful because it prevents a common error: treating a smaller average wage gap as proof that welfare rose for all relevant actors.

```{include} assets/tables/06-policy-to-margin-incidence-map.md
```

The table also gives a reading strategy. Do not begin by sorting papers into "childcare papers" or "quota papers." Begin by asking which column of the table the paper can actually fill. A study with strong wage data and weak household data may identify pay-setting but not household incidence. A study with rich household time-use data and no firm identifiers may identify care reallocation but not employer response. A paper with credible legal exposure may estimate a reduced-form effect while leaving implementation and compliance as the next research question. Those limits are not flaws if the paper is explicit about them; they are the map of the research frontier.

### Childcare And Care-Support Policies

Childcare policy is usually introduced as a female labor-supply policy. That is partly right, but too narrow. Childcare changes the price, availability, quality, and reliability of care. Those changes can affect participation, hours, job search, self-employment, occupation choice, firm sorting, fertility, household bargaining, child development, and the organization of work. The first research question is not "does childcare work?" It is: which time constraint was binding, for whom, and what else moved?

The classic Quebec childcare evidence shows why a single labor-supply coefficient is not enough. Universal childcare increased maternal employment, but the same policy also affected family well-being and child outcomes [@bakerGruberMilligan2008]. A labor economist should read that evidence as a multi-margin intervention: cheaper care changes mothers' work, household schedules, child environments, and the value of different job arrangements. The welfare object is therefore broader than maternal earnings.

Recent experimental work in Uganda makes the incidence point especially clear. Childcare subsidies increased labor supply and business activity for single mothers, but among couples the response partly ran through fathers' salaried employment [@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025]. That is a direct warning against treating "women targeted" as "women bear all incidence." If the subsidy relaxes a household constraint, the household can allocate the newly available time to the member with the highest return, the lowest search cost, the strongest bargaining position, or the most feasible job options.

Comparative legal and institutional evidence reinforces the same logic. Childcare laws around availability, affordability, and quality are associated with women's economic empowerment, but their effects depend on implementation, labor-demand conditions, informality, norms, and the age structure of children [@anukriti2025]. In a high-income setting, care support may move the return-to-work margin after childbirth. In a low-income or informal setting, it may move self-employment, hours, business development, or the possibility of stable wage work.

The main margin moved by childcare is often participation or hours, but the deeper labor question is about time constraints and care complementarities. If a childcare expansion produces large employment responses among mothers with young children, the evidence supports the claim that care time was binding. If employment does not respond but job quality improves, the binding margin may have been schedule reliability or ability to hold better jobs. If fathers respond, then childcare policy is revealing household allocation, not just maternal labor supply.

Likely firm responses include schedule redesign, changed retention policies, more predictable shifts, altered part-time/full-time composition, and differential recruiting of workers with care responsibilities. Firms may benefit from reduced turnover, but they may also face wage pressure if workers' outside options improve. Incidence can fall on workers, partners, children, childcare providers, employers, taxpayers, and coworkers who absorb schedule changes.

The frontier version of the childcare question is therefore not only whether subsidies raise maternal employment. It is whether the care market, the household, and the firm are complements or substitutes in producing attachment. Public care can crowd in paid work, shift bargaining power, change the timing of job search, change demand for private providers, and alter the value of predictable schedules. A serious empirical design tries to observe at least two of those margins. Otherwise the same treatment effect can be misread as a pure labor-supply elasticity when it is really a household reoptimization or local-care-market equilibrium effect.

### Parental Leave And Return-To-Work Policies

Parental leave policy is a dynamic career intervention. It changes income insurance around birth, job protection, leave duration, attachment, tenure, employer expectations, experience accumulation, and the timing of return to work. The same reform can increase short-run attachment and still worsen long-run earnings if it encourages longer interruptions or changes firm beliefs about future availability.

Short-duration paid leave evidence in the United States shows the attachment channel. Paid parental leave laws can raise women's labor-force attachment around childbirth [@byker2016]. That is an important margin because leaving employment after birth can sever job matches and reduce accumulated firm-specific human capital. But attachment is not the same object as long-run convergence.

Recent evidence on California's paid family leave is a useful caution. Bailey, Byker, Patel, and Ramnath use administrative tax data and a regression discontinuity design to study long-run effects, finding limited overall improvement in women's careers and negative effects for some first-time mothers [@baileyBykerPatelRamnath2025]. The lesson is not that leave is "bad." The lesson is that the policy moved some margins while leaving other mechanisms intact or even activating new ones: leave duration, labor supply timing, employer response, career progression, fertility, and household specialization can all change.

Long-run Austrian policy evidence makes the same point at a larger scale. Kleven, Landais, Posch, Steinhauer, and Zweimueller study decades of family-policy experimentation and find that large expansions in parental leave and childcare did little to close gender inequality overall [@klevenLandaisPoschSteinhauerZweimueller2024]. A policy can be generous, visible, and meaningful to households while still failing to undo the deeper allocation of care, career incentives, and firm-side penalties that produce gender gaps.

The primary margins for leave are attachment, tenure, return-to-work timing, experience, fertility, and promotion. The likely firm responses include replacement hiring, staffing buffers, delayed promotion, reassignment of clients or projects, changed evaluation windows, and statistical expectations about future leave. Coworkers can bear incidence if work is redistributed without compensation. Future careers can bear incidence if leave changes assignments, visibility, or promotion tracks.

For mechanism identification, leave reforms help distinguish at least three channels. First, if short leave increases return to the same employer, job continuity matters. Second, if long leave lowers later earnings conditional on return, human-capital depreciation or firm-side career penalties may matter. Third, if fathers' leave changes mothers' careers, household bargaining and norms around care allocation are part of the mechanism.

The broader family-policy literature is useful here because it forces a comparative perspective [@olivettiPetrongolo2017FamilyPolicies]. Policies that look similar on paper can differ in job protection, wage replacement, father eligibility, employer financing, public financing, take-up stigma, and coverage of informal or self-employed workers. Those details determine incidence. Employer-financed mandates may be capitalized into wages or hiring; public insurance may spread costs more broadly; weak job protection may insure income without preserving a match; strong job protection may preserve matches while changing promotion expectations. The policy label is less informative than the margin and financing rule.

### Taxation, Transfers, And Second-Earner Incentives

Tax and transfer policy is a gendered labor-market institution because many households have one primary earner and one secondary earner, and women are disproportionately represented among secondary earners. Joint taxation can create high effective marginal tax rates for the secondary earner. Means-tested transfers can create participation or hours notches. Child-related credits can change work incentives differently across family types.

The central margin is usually participation and hours, but the mechanism can be price response, household bargaining, social norms, childcare costs, or job availability. Bick and Fuchs-Schuendeln quantify the disincentive effects of joint taxation on married women's labor supply and show how separate taxation can generate large predicted increases in married women's hours [@bickFuchsSchuendeln2017]. The labor object is not only tax revenue. It is the labor supply of the marginal earner and the household allocation of paid and unpaid work.

The gender-based taxation argument pushes further by connecting tax design to the division of family chores [@alesinaIchinoKarabarbounis2011]. If women have higher labor-supply elasticities because social norms and household production make their market work more marginal, then uniform taxation may be inefficient and distributionally loaded. But the policy incidence is complex: changing the secondary-earner tax price can alter labor supply, home production, bargaining power, childcare demand, household income, and the distribution of leisure.

The likely firm response to tax and transfer incentives is less direct than in transparency or leave policy, but it is still present. Firms may change contract form, part-time opportunities, scheduling, formalization, benefit design, or recruitment if tax incentives change the supply of secondary earners. In settings with informality, tax and transfer design may affect whether women enter formal wage work, self-employment, or unpaid family work.

For researchers, tax reforms are useful because they offer variation in budget sets. But policy evaluation is not identical to mechanism identification. A tax reform may produce a reduced-form participation response, while the mechanism could be liquidity, childcare affordability, bargaining, social norms, or employer demand for part-time work. Strong papers therefore connect estimated elasticities to institutional details and household structure.

A useful diagnostic is to ask whether the reform changes the *price of work*, the *fixed cost of work*, or the *control of resources*. A lower secondary-earner marginal tax rate primarily changes the price of market hours. A childcare credit lowers a fixed cost and may operate only when care is actually available. A transfer paid to one spouse can change bargaining even if the household budget set is unchanged. These are distinct labor mechanisms. Treating them as one generic "work incentive" makes it difficult to compare studies or design a credible welfare calculation.

### Quotas, Representation, And Leadership Pipelines

Quotas and representation rules target authority, leadership, and access to organizational rents. Their central labor-market question is not whether representation at the targeted node changed. It usually does. The deeper question is whether changing representation at one node changes pipelines, promotion criteria, mentoring, networks, hiring, wages, bargaining, aspirations, or organizational priorities.

Norway's board quota is the anchor because it created a large change in board representation while producing limited broad-based labor-market gains for the wider group of highly qualified women [@bertrandBlackJensenLlerasMuney2019]. That result is powerful precisely because it separates top-level representation from general pipeline transformation. A board seat is a real authority outcome, but it may be too high in the hierarchy to change promotion rules below it unless firms actively rebuild the pipeline.

The primary margins are leadership access, promotion, authority, networks, and spillovers to younger cohorts. The likely firm responses include search for eligible candidates, changes in board composition, mentoring, pipeline investments, internal reallocation, compliance-focused appointment, and possible shifts in the value of credentials. Incidence can fall on targeted women, near-miss candidates, men displaced from positions, younger cohorts, shareholders, and workers affected by leadership decisions.

Quotas are also identification devices. If a quota changes top representation but not wages or promotion below the top, the bottleneck may lie earlier in the pipeline. If the quota changes promotion rates for women below the targeted level, the policy may have altered mentoring, visibility, or expectations. If younger women change educational or occupational choices in response, representation may operate through role-model or aspiration channels. If firms comply formally but isolate quota appointees from real authority, the policy changes nominal representation without changing power.

This is why quotas should not be read only as a policy category. They are tests of where the hierarchy binds.

The same logic applies to softer representation and pipeline interventions. A mentoring program, shortlist rule, leadership-training program, or promotion-panel reform may be less visible than a quota but closer to the bottleneck. The research question is whether the intervention changes the assignment of authority or only the composition of a formal body. A project that observes board seats but not committees, management responsibilities, pay, or later promotions can describe representation but says less about power. A project that observes internal vacancies, applicant pools, shortlists, promotions, and departures can separate pipeline expansion from reallocation among already-eligible workers.

### Transparency, Equal-Pay Rules, And Anti-Discrimination Enforcement

Transparency policies move information. Equal-pay rules move permissible pay structures. Anti-discrimination enforcement moves the expected cost of differential treatment, the documentation requirements around decisions, and the credibility of worker claims. These policies are central to labor economics because they target firm pay-setting, bonus allocation, job classification, promotion, bargaining, retention, and compliance.

Pay transparency evidence is especially useful because it shows firm response in the data. Baker, Halberstam, Kroft, Mas, and Messacar study salary-disclosure laws in Canada and find reductions in the gender pay gap [@bakerHalberstamKroftMasMessacar2023]. Blundell, Duchini, Simion, and Turrell study the UK gender pay gap reporting regime and show that pay transparency reduced the gap partly by slowing men's pay growth and bonus progression [@blundellDuchiniSimionTurrell2025]. That is an incidence result. The policy did not simply raise women's pay in a vacuum. It altered the pay-setting environment, public scrutiny, and firm wage dynamics.

The primary margins are wages, bonuses, raises, negotiation, retention, and sometimes promotions. The likely firm responses include wage compression, changed bonus rules, formal pay bands, altered raise timing, reclassification of jobs, changes in hiring, and investment in compliance reporting. Incidence can fall on lower-paid women, higher-paid men, managers with discretion, workers whose bonuses are compressed, firms that lose pay-setting flexibility, and future applicants who sort based on disclosed information.

Equal-pay-for-similar-work rules are a sharper regulatory intervention because they constrain within-firm price differences across comparable jobs. Gentile Passaro, Kojima, and Pakzad-Hurson show that such rules can induce workforce segregation and may widen some gender gaps depending on local market composition [@gentilePassaroKojimaPakzadHurson2026]. This is a central Week 6 lesson: if a policy constrains one margin, firms may adjust on another. The relevant response may be not only wage compliance, but also job assignment, job title inflation, task bundling, location of workers, or segregation across comparable roles.

Legal discrimination and protection data broaden the view. Hyland, Djankov, and Goldberg show that gendered laws are measurable labor-market institutions associated with women's workforce outcomes [@hylandDjankovGoldberg2020]. Formal legal equality can alter hiring, property rights, mobility, pay, and entrepreneurship, but the observed labor-market effect depends on enforcement and social credibility. A legal right that workers cannot safely claim is not the same treatment as a right backed by credible complaint processes and sanctions.

Anti-discrimination enforcement therefore raises an incidence question. Strong enforcement can protect workers and deter exclusion, but it can also change firms' documentation, screening, compliance costs, or willingness to use subjective evaluation. Weak enforcement may leave formal rights disconnected from labor-market behavior. The key empirical move is to observe which margin changed: hiring, wages, promotions, retention, reporting, or job assignment.

This is also where firm heterogeneity matters most. Large firms may have human-resources systems, legal staff, pay bands, and reporting infrastructure that make compliance feasible. Small firms may respond through informal reclassification, avoidance, or changes in hiring. High-rent firms may absorb compliance costs; low-margin firms may shift costs to wages, hours, or staffing. In matched employer-employee data, those differences are not nuisance heterogeneity. They are the mechanism.

### Flexible Scheduling, Workplace Protections, Reporting, And Compliance

Scheduling and workplace-protection policies sit between family policy and firm regulation. They affect the feasibility of work, the cost of remaining in a job, and the credibility of voice. Flexible scheduling may help workers combine care and paid work, but it may also create penalties if flexibility is stigmatized, assigned to low-promotion tracks, or rationed by managers. Protection rules can reduce harassment, retaliation, unsafe work, or dismissal risk, but only if workers believe reporting is feasible and firms respond.

Workplace harassment and reporting evidence belongs in a labor-policy week because reporting costs affect job choice, retention, authority, and wage interpretation. Bayer, Bhalotra, and Miller study why workplace sexual harassment is underreported, emphasizing the costs to women victims [@bayerBhalotraMiller2024]. Folke and Rickne show how sexual harassment connects to gender inequality in the labor market [@folkeRickne2022sexualHarassment]. The labor-market object is not only a reported incident. It is the feasible set of jobs, the cost of staying, the value of authority, and the risk attached to work.

Workplace violence evidence makes the same point in a more directly administrative setting. Adams-Prassl, Huttunen, Nix, and Zhang show how violence at work can be linked to labor outcomes, firm behavior, and worker mobility [@adamsPrasslHuttunenNixZhang2024]. For Week 6, the policy lesson is that protection is meaningful only when the reporting technology, retaliation environment, and enforcement process make the right usable. A formal rule may change measured reports without changing latent harm; a credible system may change retention, sorting, and welfare even if reports initially rise.

The primary margins are safety, reporting, retention, mobility, occupation choice, schedule feasibility, and welfare. The likely firm responses include compliance systems, human-resources documentation, training, grievance procedures, retaliation prevention, scheduling redesign, manager discipline, and sometimes defensive screening. Incidence can fall on workers who report, workers who do not report, coworkers, managers, firms, and future applicants.

This area also bridges to Week 7. Safety is not separate from labor economics. It changes reservation wages, commuting choices, occupations, mobility, authority, and the nonwage value of jobs.

```{include} assets/tables/06-firm-response-and-welfare-map.md
```

### What Good Policy Evidence Must Name

Across domains, a strong policy paper names the treatment and then refuses to stop there. It identifies the treated unit, comparison group, outcome margin, exposure rule, firm response, incidence channel, and welfare object. The same reduced-form design can support very different claims depending on which margins are observed.

For example, a threshold-based pay transparency design can estimate the effect of disclosure on the firm-level gender pay gap. That is an outcome effect. If the paper also observes bonus compression, wage growth by gender, hiring, retention, and occupational composition, it can speak to incidence and firm response. If it observes worker utility, job satisfaction, or outside offers, it can say more about welfare. Without those additional margins, a gap reduction should not be overinterpreted as a welfare gain.

Likewise, a childcare RCT can estimate labor-supply effects. If it also observes fathers' work, children's outcomes, household income, business investment, and time use, it can distinguish maternal time constraints from household reoptimization. If it does not observe firms, it should be cautious about claims involving employer accommodation or wage incidence.

The empirical discipline is simple but demanding: average effects answer "what changed"; incidence answers "who bore the change"; firm response answers "how the market adjusted"; welfare answers "whether the change improved the relevant social objective."

```{include} assets/tables/06-frontier-and-reading-map.md
```

## Research Lab

### Policy Variation As An Empirical Device

Policy variation is attractive because it can shift constraints that researchers otherwise struggle to observe. But a strong gender-policy paper does not stop at "the policy worked." It uses the policy to identify a deeper labor mechanism.

Childcare expansions can identify care-time constraints and household incidence. Leave reforms can identify attachment, experience accumulation, and dynamic career penalties. Tax reforms can identify second-earner elasticities and household specialization. Quotas can identify leadership bottlenecks and pipeline spillovers. Transparency and equal-pay rules can identify firm pay-setting, bonus allocation, classification, and compliance. Legal protections and reporting reforms can identify how safety and credibility affect labor supply, retention, and welfare.

```{include} assets/tables/06-policy-as-identification-device-map.md
```

### Reduced Form Is Not Mechanism Identification

A policy estimate has a natural reduced-form object:

```{math}
:label: eq-week6-reduced-form-policy
Y_{ift}
=
\alpha_i+\delta_f+\lambda_t+\beta P_{ft}+X_{ift}'\gamma+\varepsilon_{ift}.
```

The coefficient {math}`\beta` may be a credible estimate of a policy effect under the design assumptions. But it does not automatically reveal the mechanism. Suppose {math}`P_{ft}` is pay transparency exposure and {math}`Y_{ift}` is earnings. A negative effect on the gender gap could come from raises for women, slower raises for men, bonus compression, occupational reclassification, attrition of high-paid men, hiring of lower-paid men, or changes in promotion. The reduced form is a start, not the whole interpretation.

A mechanism-oriented design adds outcomes and structure:

```{math}
:label: eq-week6-mechanism-system
\begin{aligned}
Y_{ift} &= y(Wage_{ift}, Bonus_{ift}, Promotion_{ift}, Job_{ift}, Exit_{ift}),\\
A_{ft} &= a(P_{ft},C_f,M_f),\\
H_{ht} &= h(P_{ft},Care_{ht},Tax_{ht},Norm_{ht}),
\end{aligned}
```

where {math}`A_{ft}` represents firm adaptation and {math}`H_{ht}` represents household adaptation. The researcher does not need to estimate a full structural model in every paper, but the interpretation should say which adaptation is observed and which remains speculative.

### Practical Policy-As-Identification Checklist

Use the following checklist when reading or designing a paper:

1. **Policy rule.** What exactly changed, for whom, when, and with what enforcement?
2. **Treated unit.** Is treatment assigned to workers, households, firms, occupations, regions, births, or legal categories?
3. **Margin observed.** Are outcomes about participation, hours, wages, bonuses, promotion, retention, fertility, sorting, reporting, safety, welfare, or child outcomes?
4. **Counterfactual.** Which comparison group identifies the effect, and why would it have followed the same path absent the policy?
5. **Incidence.** Who likely gains or loses after adjustment: workers, partners, firms, coworkers, children, taxpayers, future cohorts?
6. **Firm response.** What margins can firms adjust, and are those margins observed?
7. **Household response.** Does the policy change bargaining, specialization, fertility timing, care allocation, or control over resources?
8. **Equilibrium.** Could sorting, prices, wages, childcare supply, or labor demand change?
9. **Welfare.** What welfare object is being claimed, and which welfare components are missing?
10. **Mechanism claim.** Does the evidence identify the mechanism, or only a reduced-form effect consistent with several mechanisms?

### Lab Design For Week 6

The Week 6 code lab uses the same discipline. It is organized as **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is Blundell, Duchini, Simion, and Turrell on pay transparency and gender equality [@blundellDuchiniSimionTurrell2025]. Students use deterministic synthetic firm-worker data to reproduce a reporting-threshold style exercise. The bounded path estimates firm-level gap changes and decomposes them into women's pay growth, men's pay growth, bonus changes, and retention.

**Diagnose.** Students classify each output as an average outcome effect, an incidence statement, a firm response, or a welfare-relevant but unobserved margin. The goal is to prevent a narrow "gap fell" interpretation.

**Transfer.** The challenge anchor is Gentile Passaro, Kojima, and Pakzad-Hurson on equal pay for similar work [@gentilePassaroKojimaPakzadHurson2026]. Students transfer the same diagnostic logic to a synthetic equal-pay rule where firms can respond through wage compression and job segregation.

**Optional extensions.** Students can write a design memo for paid family leave [@baileyBykerPatelRamnath2025], board quotas [@bertrandBlackJensenLlerasMuney2019], or childcare subsidies [@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025]. They should name the treatment, treated unit, margin, likely incidence, and what mechanism evidence would require.

### Student Project Ideas

1. **Transparency and bonuses.** Use a transparency reform to ask whether gender-gap reductions come from base pay, bonuses, promotions, or retention. The mechanism question is whether public disclosure changes bargaining, managerial discretion, or reputation costs.
2. **Childcare and household incidence.** Use a childcare expansion to test whether treated households increase mothers' work, fathers' work, total household earnings, or child outcomes. The mechanism question is whether childcare relaxes a maternal constraint or a household constraint.
3. **Leave duration and promotion timing.** Use variation in leave eligibility or duration to ask whether attachment improves while promotion slows. The mechanism question is whether firms treat leave as insurance, interruption, or a signal.
4. **Tax incentives and formal work.** Use tax or transfer variation to estimate secondary-earner labor supply, then test whether responses occur through formal employment, hours, self-employment, or job quality.
5. **Quotas and pipeline spillovers.** Use representation rules to ask whether women below the targeted level receive more promotions, mentoring, or authority. The mechanism question is whether the bottleneck sits at the top or earlier in the pipeline.
6. **Protection credibility.** Use reporting or harassment-protection reforms to ask whether formal rights change retention, reporting, mobility, and sorting. The mechanism question is whether workers believe protection is credible.

## Methods Box

:::{admonition} Methods Box: Separate Effects, Incidence, Response, And Welfare
:class: note

**Event studies and difference-in-differences.** Useful for reforms with rollout timing, thresholds, or exposure rules. Strong designs name the treated unit and test pre-trends. Mechanism claims require outcomes beyond the headline gap.

**Regression discontinuity and eligibility rules.** Useful for leave, tax, benefit, and reporting thresholds. The local estimate may be credible but may not generalize to all workers, firms, or policy intensities.

**Bunching and nonlinear-budget-set methods.** Useful for tax and transfer incentives. They estimate behavioral response to price changes, but household incidence and bargaining require additional data.

**Randomized experiments and phased rollouts.** Useful for childcare, financial control, reporting systems, or workplace interventions. The strongest designs observe both target and spillover actors.

**Matched employer-employee panels.** Essential for firm response. They can track wages, bonuses, promotions, retention, occupations, establishments, and sorting.

**Administrative legal or policy panels.** Useful for cross-region or cross-country legal variation. Interpretation depends on enforcement, measurement, and whether formal rules are actually binding.

**Decomposition and mediation.** Useful for asking which margins account for a policy effect, but not causal unless each component has a credible identification strategy.

**Welfare accounting.** Requires clarity about utility, income, nonmarket time, safety, autonomy, child outcomes, firm surplus, fiscal cost, and distributional weights. A smaller gap is evidence about equality of an observed outcome, not a complete welfare statement.

:::

## Reading Ladder And References

**Start with the broad architecture.** Cortes and Pan provide the family and child-related gender-gap overview that links this week to the rest of the course [@cortesPan2023]. Olivetti and Petrongolo are useful for family policies and gender gaps across high-income countries [@olivettiPetrongolo2017FamilyPolicies]. Kleven, Landais, Posch, Steinhauer, and Zweimueller show why decades of family-policy expansion need not imply broad gender convergence [@klevenLandaisPoschSteinhauerZweimueller2024].

**Childcare and care constraints.** Read Baker, Gruber, and Milligan for universal childcare and the multi-outcome nature of the intervention [@bakerGruberMilligan2008]. Then read Bjorvatn, Ferris, Gulesci, Nasgowitz, Somville, and Vandewalle for experimental evidence and household incidence [@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025]. Add Anukriti for comparative legal variation in childcare laws [@anukriti2025].

**Leave and long-run careers.** Read Byker for short-duration leave and attachment [@byker2016]. Then read Bailey, Byker, Patel, and Ramnath for long-run administrative evidence and the difference between attachment and career convergence [@baileyBykerPatelRamnath2025].

**Taxation and second-earner incentives.** Read Bick and Fuchs-Schuendeln for joint taxation and married women's labor supply [@bickFuchsSchuendeln2017]. Pair it with Alesina, Ichino, and Karabarbounis for the link between gender-based taxation and the division of family chores [@alesinaIchinoKarabarbounis2011].

**Quotas and leadership.** Read Bertrand, Black, Jensen, and Lleras-Muney for Norway's board quota and the distinction between top representation and broad labor-market spillovers [@bertrandBlackJensenLlerasMuney2019].

**Transparency, equal pay, and firm response.** Read Baker, Halberstam, Kroft, Mas, and Messacar on Canadian pay transparency [@bakerHalberstamKroftMasMessacar2023]. Then read Blundell, Duchini, Simion, and Turrell for the UK reporting regime and the role of men's pay growth and bonuses [@blundellDuchiniSimionTurrell2025]. Use Gentile Passaro, Kojima, and Pakzad-Hurson to see why equal-pay rules can induce firm reallocation and segregation [@gentilePassaroKojimaPakzadHurson2026].

**Legal protections, reporting, and safety.** Read Hyland, Djankov, and Goldberg for legal restrictions as labor-market institutions [@hylandDjankovGoldberg2020]. Read Bayer, Bhalotra, and Miller on reporting costs [@bayerBhalotraMiller2024], and connect to Folke and Rickne on harassment and labor-market inequality [@folkeRickne2022sexualHarassment].

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week6-incidence-map` to classify a childcare subsidy into worker, household, firm, coworker, and market components. Which components are typically observed?
2. A pay transparency reform reduces the mean gender pay gap. List four mechanisms consistent with that result and one outcome that would help distinguish each mechanism.
3. Explain why an increase in mothers' return-to-work after paid leave is not the same as long-run career convergence.
4. Use Equation {eq}`eq-week6-welfare-object` to compare a policy that reduces wage gaps through bonus compression with a policy that raises safety and retention but leaves wages unchanged.
5. Design a difference-in-differences study of an equal-pay rule. State the treated unit, comparison group, outcome margins, possible firm responses, and one incidence concern.
6. A board quota changes board composition but not the wages of younger women. Give three interpretations and the additional data needed to separate them.
7. Choose one policy from the reading ladder and write a one-page "policy as identification device" memo. The memo must separate reduced-form effects, mechanism claims, incidence, firm response, and welfare.

## Reproducibility And Code Lab Note

The Week 6 code lab lives at `labs/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path builds deterministic synthetic data, reproduces a pay-transparency reporting exercise inspired by [@blundellDuchiniSimionTurrell2025], and transfers the same diagnostic framework to an equal-pay-for-similar-work exercise inspired by [@gentilePassaroKojimaPakzadHurson2026]. It runs locally without confidential microdata.

## Slide Companion Note

The Week 6 slide deck lives at `slides/week6/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.tex`. The deck is a conceptual map. It defines the central question, bridges from Weeks 2 through 5, lays out the policy-to-margin framework, reviews childcare, leave, taxation, quotas, transparency, equal-pay rules, and protections, separates firm response from incidence and welfare, and closes by treating policy variation as an identification device.

## Bridge Forward

Week 7 turns from policy incidence to violence, safety, mobility, and labor-market access. Week 6 already introduced the key bridge: safety, credibility, reporting, and protection are labor-market objects because they change which jobs are feasible, which workers stay, how firms respond, and what wages mean as welfare measures. Week 7 studies those constraints directly.
