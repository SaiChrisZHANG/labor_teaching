# Violence, Safety, Mobility, And Labor-Market Access

Safety belongs in labor economics because it changes which jobs are actually available. A worker may face a posted vacancy, a market wage, and a formal right to work, but still have a constrained choice set if the commute is unsafe, the workplace is hostile, an abusive partner controls movement or income, or reproductive timing is not under the worker's control. Week 7 studies these constraints directly.

The central question is: **How do safety, harassment, violence, mobility constraints, and reproductive autonomy shape labor-market access and worker welfare?** This is not a policy-incidence lecture. Week 6 asked which policy margins move and who bears incidence. Week 7 asks what the feasible set looks like before policy evaluation begins.

:::{admonition} Core points
:class: important

- Safety changes the feasible set of jobs, commutes, schedules, and workplaces, not only the utility of a given job.
- Violence and harassment affect participation, search intensity, job acceptance, occupation choice, quits, retention, sorting, and welfare.
- Domestic violence and intimate-partner violence can constrain labor-market access through mobility control, physical and psychological costs, bargaining power, absenteeism, and outside options.
- Workplace harassment and workplace violence are labor-market mechanisms because they change retention, coworker composition, job quality, and the value of authority.
- Reproductive autonomy changes career timing and option value: birth control, abortion access, and fertility treatment shape education, work, family timing, and future feasible paths.
- Hidden harms are often missing from wage and employment data, so researchers need designs that observe reporting, search, mobility, exits, and welfare-relevant job quality.

:::

## Learning Objectives

By the end of Week 7, students should be able to:

1. model safety and reproductive autonomy as constraints on the worker feasible set rather than as background social issues;
2. distinguish safety as a price or disutility margin, a search and mobility margin, a retention or exit margin, and a hidden welfare margin;
3. explain how domestic violence, workplace harassment, workplace violence, commuting risk, and public-space safety affect labor supply, sorting, and welfare;
4. treat birth control, abortion access, and IVF or fertility-treatment access as labor-market timing and control margins;
5. identify the research designs used to study invisible harms: administrative linkage, survey-admin linkage, randomized mobility interventions, legal or judicial quasi-experiments, IVF-based instruments, and boundary or policy discontinuities;
6. read empirical evidence by naming the constraint, the data that make it visible, the observed labor margin, and the limits of the welfare claim;
7. design a bounded research exercise that separates reported incidents from latent exposure and labor-market response.

## Bridge

Week 6 treated gender-related policies as shocks to labor-market margins. Childcare, leave, taxation, quotas, transparency, equal-pay rules, and formal protections were useful because they revealed incidence across workers, households, firms, coworkers, and markets. Protection and reporting already appeared there, but as part of a policy architecture.

Week 7 changes the object. The point is not to ask whether a particular protection rule "works." The point is to ask what labor choices are available when safety, mobility, and reproductive control are themselves constraints. A formal job offer is not equivalent to an accessible job if the worker cannot safely commute, cannot credibly report harassment, anticipates retaliation, must preserve safety at home, or cannot control the timing of pregnancy and care responsibilities.

This bridge matters for interpretation. Week 6 warned that a wage-gap reduction is not a complete welfare statement. Week 7 shows why. A higher wage in a risky workplace may compensate for danger, reflect sorting into hostile jobs, or conceal severe welfare losses. A lower wage in a safer job may represent constrained sorting, but it may also raise welfare if the alternative was violence, harassment, or reproductive coercion. Labor economics needs wages, employment, and utility.

The forward bridge to Week 8 is comparative. Safety constraints, mobility systems, legal credibility, reproductive access, informality, and family institutions differ sharply across countries and regions. Week 8 asks which gender-and-labor mechanisms travel across settings and which depend on development, infrastructure, legal regimes, norms, and local labor demand.

## Field Core

### Feasible Sets, Utility, And Search Margins

The simplest labor-supply model lets a worker compare wages, hours, and nonmarket time. Week 7 expands the object. A job is a bundle of wage, schedule, commute, safety, dignity, authority, fertility timing, reporting risk, and future opportunity. The worker does not choose from all posted jobs. The worker chooses from jobs that are reachable, safe enough, compatible with household constraints, and feasible given control over current and future fertility.

Let {math}`\mathcal{J}` be the universe of possible jobs. Worker {math}`i` faces a constrained feasible set:

```{math}
:label: eq-week7-feasible-set
\mathcal{F}_{it}
=
\left\{
j\in\mathcal{J}_{t}:
m_{ijt}\leq \bar m_{it},
r_{ijt}\leq \bar r_{it},
q_{ijt}\geq \bar q_{it},
a_{it}\geq \bar a_{it}
\right\}.
```

Here {math}`m_{ijt}` is the mobility or commute burden, {math}`r_{ijt}` is safety or harassment risk, {math}`q_{ijt}` is the minimum job-quality and reporting environment needed to remain safely employed, and {math}`a_{it}` is control over fertility timing and future care commitments. The thresholds are worker-specific. They depend on household bargaining, local transportation, legal credibility, health, pregnancy risk, partner control, childcare, and prior exposure to violence.

Conditional on feasibility, the worker's job utility can be written as:

```{math}
:label: eq-week7-job-utility
U_{ijt}
=
w_{jt}
- \phi h_{jt}
- \kappa m_{ijt}
- \rho r_{ijt}
- \psi H_{ijt}
+ A_{ijt}
+ \Omega_{it}(T_{it})
+ \varepsilon_{ijt}.
```

The wage is {math}`w_{jt}`. Hours are {math}`h_{jt}`. Mobility costs are {math}`m_{ijt}`. Safety and harassment risk are {math}`r_{ijt}`. Hidden harm, fear, retaliation risk, stigma, and reporting costs are summarized by {math}`H_{ijt}`. Amenities and authority are {math}`A_{ijt}`. Reproductive control enters through {math}`\Omega_{it}(T_{it})`, the option value of controlling the timing of schooling, work, fertility, and care. The crucial feature is that wages do not summarize welfare.

The same logic applies to search. Suppose worker {math}`i` searches over job offers with search radius {math}`R_{it}` and acceptance set {math}`\mathcal{A}_{it}`:

```{math}
:label: eq-week7-search-margin
\mathcal{A}_{it}
=
\{j\in\mathcal{F}_{it}: U_{ijt}\geq U_{it}^{0}\}.
```

Safety can reduce applications by shrinking {math}`\mathcal{F}_{it}`; reduce acceptance by lowering {math}`U_{ijt}`; reduce retention by raising the value of exit; and reduce measured wages if workers sort into safer but lower-paid jobs. It can also raise observed wages for those who remain in risky jobs if the risk is compensated, which is why wage effects alone can mislead.

```{include} assets/tables/07-safety-constraints-map.md
```

### Domestic Violence And Intimate-Partner Violence

Domestic violence and intimate-partner violence enter labor economics through constraints on mobility, time, health, bargaining power, and outside options. They are not external to the labor market. An abusive partner can restrict search, monitor transportation, sabotage work, control income, increase absenteeism, and reduce the credibility of quitting or moving. Violence can also change the return to employment in either direction: work may improve outside options and bargaining power, but it may also trigger backlash when it threatens household control.

The labor margins are concrete. Participation can fall if violence makes regular work physically or psychologically costly. Search intensity can fall if applications, interviews, and commuting are monitored. Job acceptance can shift toward nearby, informal, flexible, or lower-visibility jobs. Hours can become unstable when violence creates health shocks or urgent care needs. Retention can fall if workplace absence or partner interference makes continued employment difficult. Welfare can fall even when the worker remains employed.

Heath studies women's labor-market opportunities, control of household resources, and domestic violence in Bangladesh [@heathMobilityResourcesIntimate2014]. The observed margins are women's access to work, control over resources, and violence exposure. The identification challenge is that employment opportunities, bargaining power, and violence are jointly determined: households with different norms, wealth, and local labor demand may differ on all three. The paper is therefore useful for mechanism discipline. It asks whether labor opportunities and resource control change domestic violence risk, while forcing students to ask what variation makes the comparison credible and which household mechanisms remain unobserved.

Aizer's evidence on the gender wage gap and domestic violence gives another labor-market angle [@aizer2010GenderWageGapDomesticViolence]. The design uses variation in relative labor-market opportunities as a proxy for bargaining power, with domestic violence as the outcome. The labor margin is not only female employment; it is the outside option embedded in wages and local labor demand. The interpretation is that labor-market prices can change household power and violence risk, but the welfare object must include safety as well as earnings.

Newer work such as Frankenthal's study of female labor productivity and domestic violence in Peru pushes the mechanism toward productivity shocks and local labor returns [@frankenthalFemaleLaborProductivity2024]. The key research question is not "does employment reduce violence?" in general. It is: which kind of work changes bargaining power, which kind changes threat or backlash, and which data can observe both the labor shock and the violence response?

For students, the main identification threats are selection into work, underreporting of violence, endogenous household formation, migration, local shocks that affect both labor demand and violence, and measurement error in partner control. Useful data include linked administrative police or court reports, employment records, health records, survey modules on violence and control, local labor-demand shocks, and credible timing around job access or resource-control changes.

### Workplace Harassment, Workplace Violence, And Power

Workplace harassment and workplace violence should not be collapsed into generic discrimination. Discrimination can operate through hiring, pay, promotion, and evaluation. Harassment and violence add a job-quality and safety constraint. They change the cost of staying, the value of authority, the risk attached to male-dominated settings, and the credibility of reporting. They can produce gendered sorting even when formal wages and titles look equal.

Folke and Rickne study sexual harassment and gender inequality in the labor market [@folkeRickne2022]. The design combines information on harassment exposure with labor-market outcomes to study how harassment risk is related to sorting, wages, and inequality. The observed margins include workplace conditions, quits, occupational composition, and wage-risk tradeoffs. The paper is central because it makes a nonwage condition part of labor-market inequality. A risky or hostile job may pay more, but the higher wage is not a welfare improvement if it compensates for harm or if workers with fewer alternatives bear the risk.

Adams-Prassl, Huttunen, Nix, and Zhang study violence against women at work using administrative linkage between police reports and labor-market records [@adamsPrasslHuttunenNixZhang2024]. The research design is powerful because the incident becomes visible in administrative data and can be linked to employers, coworkers, separations, hiring, and workplace composition. The observed labor margins include victim outcomes, coworker or firm spillovers, retention, and firm adjustment. The identification problem is still hard: reported violence is selected, and the event may coincide with workplace conditions that are not randomly assigned. But the linked data let researchers study responses that ordinary surveys or wage records would miss.

Bayer, Bhalotra, and Miller focus on why workplace sexual harassment is underreported and the costs of reporting to women victims [@bayerBhalotraMiller2024]. This paper belongs in Week 7 because reporting is a labor-market decision. If reporting creates retaliation risk, career costs, stigma, or dismissal risk, then administrative complaints understate exposure and overrepresent cases where expected benefits exceed expected costs. The observed margin is reporting behavior and its consequences, not only harassment incidence.

Power asymmetry is a frontier angle. Macdonald, Montonen, and Nix study romantic relationships with the boss [@macdonaldMontonenNix2025]. The labor-economics object is internal hierarchy: authority, promotion, retention, coworker spillovers, perceived fairness, and the boundary between consensual relationships and coercive or career-relevant power. This is not a gossip topic. It is an internal labor-market question about how hierarchy and private relationships can alter opportunity, risk, and worker beliefs about the rules of advancement.

Researchers need data that separate exposure, reporting, and response. Workplace surveys can measure latent exposure and perceived climate. Administrative data can measure separations, promotions, wages, sick leave, complaints, police reports, and firm composition. Matched employer-employee panels can show whether workers leave the firm, move to different establishments, change occupations, or remain with lower promotion. The best designs link the climate measure to the labor margin rather than treating harassment as an unobserved residual.

### Mobility, Commuting, And Public-Space Safety

Safety can bind before the worker reaches the workplace. A job is not fully accessible if the commute is costly, unreliable, or unsafe. Public-space harassment, transport risk, travel after dark, and household restrictions on movement can shrink search radius, reduce applications, change accepted jobs, and increase dependence on local or informal work. Mobility is therefore a labor-market access technology.

This point connects to earlier work on gendered job search. Le Barbanchon, Rathelot, and Roulet show that women trade off commute against wages differently in job search [@leBarbanchonRathelotRoulet2021commuteWageTradeoff]. Week 7 adds safety to that commute margin. A shorter commute may be chosen not only because time is costly, but because risk is concentrated in particular routes, times, transport modes, or public spaces.

Garlick, Field, and Vyborny study women's mobility and labor supply using experimental evidence from Pakistan [@garlickFieldVyborny2025]. The key design family is randomized mobility or transport intervention. The labor margins are applications, attendance, labor supply, job acceptance, and possibly hours or earnings. The advantage of random assignment is that it can move the mobility constraint directly rather than inferring it from where workers end up. The interpretation should still name the mechanism: safer or more reliable transport can affect work by lowering travel risk, reducing travel time, changing household permission constraints, improving access to vacancies, or raising search intensity.

Borker's work on perceived street-harassment risk and educational choices is useful as a pre-labor-market analogue [@borker2021SafetyFirst]. The margin is schooling and field choice rather than employment, but the same mechanism appears: safety changes the set of institutions or opportunities a young woman can realistically choose. Chen and Sekhri's work on gender-specific transportation costs and female time use is a complementary mobility and time-use framing [@chenSekhri2025]. The observed margin is not only whether women work, but how transport costs reshape time allocation.

Mobility constraints create difficult measurement problems. Non-applications are usually invisible. Standard labor-force data observe accepted jobs, not the vacancies never considered, the interviews skipped, the routes avoided, or the schedules refused. Useful data include application records, job-search platforms, randomized transport offers, GPS or commute information when ethically collected, time-use surveys, safety perceptions, household permission measures, and local crime or harassment reports. Even then, researchers must avoid overinterpreting absence from a job as preference when the feasible commute set is constrained.

### Reproductive Autonomy As Timing, Control, And Option Value

Reproductive autonomy is a labor-market issue because it changes the timing and feasibility of education, work, mobility, marriage, fertility, care, and career investment. Birth control, abortion access, and fertility treatment are often discussed as policy or health debates. In Week 7 they enter as control over the future path of labor supply and household production.

Birth control access changes expectations before pregnancy occurs. Goldin and Katz study the power of the pill using historical variation in access to oral contraceptives and show how fertility control changed women's career and marriage decisions [@goldinKatzPowerPill2002]. The observed margins are education, professional investment, marriage timing, and career commitment. The design is a historical/policy access design: variation in legal and institutional access shifts the ability to plan fertility, which changes the returns to long human-capital investments.

Abortion access and abortion denial affect labor-market trajectories because they change whether and when pregnancy becomes a binding constraint. Miller, Wherry, and Foster study the economic consequences of being denied an abortion [@millerWherryFoster2023]. The design compares women around abortion-provider gestational limits, using denial as a quasi-experimental shock to fertility and timing. The observed margins include labor-market and financial trajectories, not only immediate pregnancy outcomes. Londono-Velez and Saravia study the impact of being denied a wanted abortion on women and their children [@londonoVelezSaravia2025]. The relevant design family is legal or judicial quasi-experiment: access or denial changes fertility timing and downstream work, income, and family outcomes.

Fertility treatment and IVF add a different margin. IVF access can relax biological timing constraints for some workers, and IVF success can serve as an instrument for childbearing in research designs. Lundborg, Plug, and Rasmussen use IVF treatments to study whether women can have children and a career [@lundborgPlugRasmussen2017]. The observed margins are career trajectories, earnings, hours, and motherhood timing. The design is an IV strategy using fertility treatment success to isolate variation in childbearing among women seeking treatment. It is local to the population undergoing IVF, but it is valuable because fertility timing is otherwise deeply endogenous.

```{include} assets/tables/07-reproductive-autonomy-map.md
```

The unifying labor object is timing control. A worker deciding whether to enroll in a professional program, accept a promotion track, move for work, invest in firm-specific skills, or leave a hostile job evaluates not only current wages but future fertility and care constraints. Reproductive autonomy changes the option value of waiting, investing, moving, or staying. Lack of autonomy can shrink the feasible set today because it changes the probability distribution over future care obligations and health risks.

This is also where Week 7 must remain distinct from Week 6. We can evaluate contraception rules, abortion restrictions, or IVF coverage as policies, but the Week 7 question is prior: how does control over fertility timing enter labor supply, search, human-capital investment, and welfare? A policy reform is one source of variation. The economic object is the timing and control margin.

### Reporting, Hidden Harms, And Welfare

Hidden harms are central because measured wages and employment can move in the wrong direction relative to welfare. A worker may remain employed while experiencing fear, humiliation, coercion, physical danger, reproductive control, or reporting costs. Another worker may quit a high-wage job for a lower-wage safer job, lowering measured earnings but increasing welfare. A third may avoid an occupation entirely, creating occupational segregation without any observed workplace incident.

```{include} assets/tables/07-measurement-and-hidden-harms-map.md
```

The measurement problem has three layers.

First, exposure is latent. Many incidents are never reported to firms, police, courts, or surveys. Reporting depends on expected retaliation, trust, documentation, stigma, legal status, job security, and outside options. A rise in reports can mean more harm, lower reporting costs, better trust, or more credible enforcement.

Second, labor responses are selected. Workers who can exit may leave quickly; workers with fewer outside options may remain in unsafe jobs. If researchers observe only current workers, they may miss those who avoided the firm or occupation. If they observe only reported cases, they may miss the silent majority of exposure.

Third, welfare is not equal to wages plus employment. A risk premium can raise wages while welfare falls. Safety improvements can raise welfare even when wages do not move. Mobility access can increase option value even before measured employment rises. Reproductive control can change future utility through education and career timing long before a wage effect appears.

A useful welfare object is:

```{math}
:label: eq-week7-welfare-object
V_{it}
=
E_t
\sum_{\tau=t}^{T}
\beta^{\tau-t}
\left[
c_{i\tau}
- \phi h_{i\tau}
- \rho r_{i\tau}
- \psi H_{i\tau}
+ A_{i\tau}
+ \Omega_{i\tau}
\right].
```

The worker values consumption {math}`c`, dislikes hours {math}`h`, safety risk {math}`r`, and hidden harm {math}`H`, values amenities and authority {math}`A`, and gains option value {math}`\Omega` from control over timing and feasible future choices. A labor paper does not need to estimate every component. It does need to say which component is observed and which welfare components remain hidden.

## Research Lab

### Frontier Architecture

The frontier research problem is to make invisible constraints visible without pretending that reported incidents are random. Researchers study safety and reproductive autonomy by linking unusual data to standard labor outcomes: police reports to employer records, harassment surveys to tax or personnel data, randomized transport interventions to applications and employment, abortion access or denial to credit and employment panels, and IVF treatment success to career trajectories.

The strongest papers name three things. First, the constraint: violence, harassment, commute risk, reporting cost, reproductive timing, or fertility-control loss. Second, the labor margin: participation, search, applications, acceptance, occupation, quits, retention, wages, hours, promotions, financial distress, or welfare. Third, the source of identification: administrative event timing, survey-admin linkage, randomized mobility access, legal or judicial quasi-experiment, IVF-based IV, or boundary discontinuity.

### Studying Invisible Harms

Invisible harms require data beyond standard wage panels. Adams-Prassl, Huttunen, Nix, and Zhang use administrative linkage to observe workplace violence events and connect them to labor-market outcomes [@adamsPrasslHuttunenNixZhang2024]. The research frontier is the linkage itself: the event is rare and selected, but it is observed with employer connections and downstream labor outcomes. Students should ask whether the design identifies the effect of the event, the effect of reporting, or the response to a workplace environment that generated both.

Folke and Rickne show how sexual harassment can be studied as a source of labor-market inequality rather than a purely legal category [@folkeRickne2022]. The frontier move is to connect harassment risk to sorting and wage interpretation. A gender wage gap can be partly a compensating differential for hostile workplaces, partly a constraint that pushes workers away from high-paying jobs, and partly a hidden welfare loss not captured by either wage or employment.

Bayer, Bhalotra, and Miller sharpen the reporting problem [@bayerBhalotraMiller2024]. If reporting is costly, then a complaint database is an equilibrium outcome, not a clean exposure measure. Researchers need survey measures, anonymous reporting, workplace climate data, or designs that separate exposure from reporting behavior.

### Reduced Mobility And Constrained Search

Mobility constraints should be studied before accepted jobs. Randomized mobility or transport interventions, such as the design family represented by Garlick, Field, and Vyborny, can measure changes in labor supply or applications when travel risk or travel cost changes [@garlickFieldVyborny2025]. Platform data and job-application records can show search radius and acceptance sets. Time-use and commute data can show whether safer transport reallocates time toward market work, education, or care.

The main identification challenge is that observed commuting choices are endogenous. Workers who choose shorter commutes may differ in care responsibilities, risk preferences, household restrictions, and local job options. A credible design needs exogenous variation in mobility costs or safety, or data that observe the search process before acceptance.

### Workplace Sorting Under Harassment Risk

Harassment risk creates sorting across occupations, firms, teams, supervisors, and schedules. The high-risk job may pay more, but that does not imply workers are compensated fully. Some workers may avoid the occupation; some may enter and then quit; some may stay because outside options are weak. Workplace survey and administrative linkages are especially valuable because they can connect risk exposure to job-to-job moves, wage changes, promotions, and retention.

The recent office-relationships paper by Macdonald, Montonen, and Nix adds the internal hierarchy angle [@macdonaldMontonenNix2025]. Office relationships with a boss can affect not only the two people involved but coworkers' beliefs, promotion queues, retention, and perceptions of fairness. For researchers, the challenge is to distinguish consensual relationship effects, power asymmetry, favoritism, retaliation risk, and harassment-risk spillovers.

### Domestic Violence And Labor-Market Consequences

Domestic violence creates a two-sided labor-market problem. Labor opportunities can alter bargaining power and exposure to violence, while violence can reduce labor supply and job stability. Heath's Bangladesh evidence and Aizer's bargaining-power evidence make clear that employment, outside options, and violence are jointly determined [@heathMobilityResourcesIntimate2014; @aizer2010GenderWageGapDomesticViolence]. Strong research designs need timing, local labor-demand variation, administrative reports, health data, or resource-control shocks to separate these directions.

Researchers should also observe employer-side consequences when possible. Domestic violence can show up at work through absenteeism, schedule instability, job loss, requests for transfers, safety planning, or employer accommodations. Those margins are often invisible in standard household surveys.

### Reproductive Autonomy As A Feasible-Set Margin

Reproductive autonomy research is strongest when it links timing control to long-run labor outcomes. The pill evidence uses historical access variation to study education, career, and marriage timing [@goldinKatzPowerPill2002]. Abortion-denial evidence uses quasi-experimental denial around gestational limits or other access rules to study labor-market and financial trajectories [@millerWherryFoster2023; @londonoVelezSaravia2025]. IVF evidence uses treatment success as an instrument for fertility timing among women seeking treatment [@lundborgPlugRasmussen2017].

The identification challenge is that fertility timing is chosen jointly with schooling, work, health, marriage, and income. Good designs therefore move access or timing through an external rule, boundary, legal process, treatment success, or discontinuity. Good interpretation names the local population: teenagers gaining pill access, women near abortion-provider gestational limits, IVF patients, or workers near policy boundaries.

### Lab Design For Week 7

The Week 7 code lab is organized as **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is Adams-Prassl, Huttunen, Nix, and Zhang on violence against women at work [@adamsPrasslHuttunenNixZhang2024]. Students use deterministic synthetic employer-worker event data to reproduce a bounded administrative-linkage exercise. The script compares pre/post outcomes around workplace violence events and summarizes victim, coworker, and firm-response margins.

**Diagnose.** Students classify each output as exposure, reporting, retention, firm response, coworker spillover, or hidden welfare. The diagnostic question is whether the data identify a violence event, a reporting event, or a broader unsafe-workplace environment.

**Transfer.** The challenge anchor is Folke and Rickne on sexual harassment and gender inequality [@folkeRickne2022]. Students transfer the logic to a synthetic workplace-climate and sorting dataset. They ask whether harassment risk shows up as quits, wage-risk tradeoffs, occupational sorting, or hidden welfare loss.

**Optional extension.** Students write a design memo inspired by Macdonald, Montonen, and Nix on romantic relationships with the boss [@macdonaldMontonenNix2025]. The memo should state the hierarchy margin, the exposed group, the likely spillovers, and the data needed to distinguish power asymmetry from ordinary coworker relationships.

### Student Project Ideas

1. **Reporting costs and quits.** Link harassment reports to personnel data and ask whether reporting changes separation, promotion, or team assignment. State whether the treatment is exposure, reporting, or firm response.
2. **Commuting risk and application sets.** Use a transport intervention or platform data to measure whether safer mobility changes application radius before accepted jobs change.
3. **Domestic violence and work stability.** Link administrative violence reports to employment spells and absenteeism, with careful attention to underreporting and household selection.
4. **Harassment-risk sorting.** Combine survey climate data with employer records to ask whether high-risk teams have higher turnover, wage premia, or gendered promotion paths.
5. **Abortion denial and financial trajectories.** Use a legal or provider threshold design to separate pregnancy timing from prior economic disadvantage.
6. **IVF timing and career investments.** Use IVF treatment success as a local instrument for fertility timing and ask which career margins are observed.
7. **Office relationships and hierarchy.** Study whether relationships with supervisors change promotion, coworker exits, reporting, or perceived fairness.

```{include} assets/tables/07-frontier-and-reading-map.md
```

## Methods Box

:::{admonition} Methods Box: Designs For Safety, Mobility, And Reproductive Autonomy
:class: note

**Safety as a price or disutility margin.** Risk, harassment, and hostility enter utility like a negative amenity. Wage premia in risky jobs are not automatically welfare gains. Designs need to observe risk exposure, wages, sorting, and exits.

**Safety as a mobility and search margin.** Safety can shrink the application set before wages are observed. Randomized transport interventions, application data, commute data, and boundary variation help identify the search margin.

**Safety as a retention and exit margin.** Harassment and violence can cause quits, transfers, absenteeism, and job-to-job moves. Matched employer-employee panels, personnel records, and event studies around reported incidents can observe these margins.

**Safety as a hidden welfare margin.** Many harms are not reported and not priced. Survey-admin linkages, anonymous climate measures, health records, and welfare accounting are needed to avoid interpreting wages and employment as complete welfare.

**Reproductive autonomy as a timing and control margin.** Birth control, abortion access, and IVF change the timing of schooling, work, fertility, and care. Historical access variation, legal or judicial quasi-experiments, boundary discontinuities, and IVF-based IV designs are common identification strategies.

**Administrative linkage.** Police, court, health, or complaint records linked to employment records can reveal reported incidents and downstream labor outcomes. The main threat is selection into reporting.

**Workplace survey plus admin linkage.** Surveys can measure latent exposure and perceived climate; admin data can measure wages, promotions, quits, and firm response. The main threat is survey selection and measurement error.

**Randomized mobility or transport interventions.** Random assignment can move commute safety or reliability directly. The main margins are applications, labor supply, attendance, job acceptance, and time use.

**Legal and judicial quasi-experiments.** Access rules, provider thresholds, court decisions, or boundary discontinuities can change reproductive access or protection credibility. Interpretation must name the local population and the observed labor margin.

**IV using fertility treatment.** IVF success can instrument for childbearing among women seeking treatment. The estimate is local, but it is valuable for separating fertility timing from unobserved preferences and career plans.

:::

## Reading Ladder And References

**Start with the feasible-set logic.** Review the commute and job-search evidence from Le Barbanchon, Rathelot, and Roulet to see how search sets can differ by gender even before safety is explicit [@leBarbanchonRathelotRoulet2021commuteWageTradeoff]. Then use the Week 7 framework above to add safety, reporting, and reproductive control to the feasible set.

**Domestic violence and outside options.** Read Heath for the connection between labor opportunities, resource control, and domestic violence in Bangladesh [@heathMobilityResourcesIntimate2014]. Pair it with Aizer for the outside-option and bargaining-power channel in domestic violence [@aizer2010GenderWageGapDomesticViolence]. Use Frankenthal as a newer productivity-shock frontier prompt [@frankenthalFemaleLaborProductivity2024].

**Workplace harassment and violence.** Read Adams-Prassl, Huttunen, Nix, and Zhang for administrative linkage and workplace violence [@adamsPrasslHuttunenNixZhang2024]. Read Folke and Rickne for harassment as a source of labor-market inequality and sorting [@folkeRickne2022]. Add Bayer, Bhalotra, and Miller for reporting costs [@bayerBhalotraMiller2024].

**Workplace power and hierarchy.** Read Macdonald, Montonen, and Nix as a frontier internal-labor-market paper on relationships with the boss [@macdonaldMontonenNix2025]. Focus on hierarchy, spillovers, and identification rather than the sensational surface of the topic.

**Mobility and public-space safety.** Read Garlick, Field, and Vyborny for randomized mobility evidence from Pakistan [@garlickFieldVyborny2025]. Use Borker for the pre-labor-market education analogue of perceived street-harassment risk [@borker2021SafetyFirst]. Use Chen and Sekhri for a transport-cost and time-use extension [@chenSekhri2025].

**Reproductive autonomy.** Read Goldin and Katz for historical contraception access and career timing [@goldinKatzPowerPill2002]. Read Miller, Wherry, and Foster, and Londono-Velez and Saravia for abortion denial and downstream economic trajectories [@millerWherryFoster2023; @londonoVelezSaravia2025]. Read Lundborg, Plug, and Rasmussen for IVF-based identification of fertility and career effects [@lundborgPlugRasmussen2017].

**Optional synthesis.** Return to Week 6's policy-incidence logic after reading these papers. Ask which results are about constraints, which are about policy treatments, and which welfare components remain hidden.

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week7-feasible-set` to describe how an unsafe commute changes the feasible job set. Which data would let you observe the jobs never applied to?
2. A workplace violence paper uses police reports linked to employer records. List three reasons reported incidents may differ from true exposure and one diagnostic for each.
3. In Equation {eq}`eq-week7-job-utility`, explain how a risky job can have higher wages but lower welfare.
4. Compare domestic violence as a labor-supply constraint with domestic violence as an outcome affected by labor-market outside options. What design would help distinguish the two directions?
5. Design a randomized transport intervention. State the treated unit, the mobility constraint, the observed labor margin, and one spillover risk.
6. Use the reproductive-autonomy block to compare birth control access, abortion denial, and IVF success. Which designs identify timing control, and for which populations?
7. A firm observes low harassment reports after a new complaint system. Give four interpretations that differ in welfare implications.
8. Write a one-page research memo on harassment-risk sorting. The memo must state the exposure measure, labor margin, identification strategy, and hidden welfare component.

## Reproducibility And Code Lab Note

The Week 7 code lab lives at `labs/07-violence-safety-mobility-and-labor-market-access/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path builds deterministic synthetic data, reproduces an administrative-linkage style workplace-violence exercise inspired by [@adamsPrasslHuttunenNixZhang2024], and transfers the same diagnostic logic to a harassment-risk sorting exercise inspired by [@folkeRickne2022]. The optional extension is a design memo inspired by [@macdonaldMontonenNix2025]. The lab runs locally without confidential microdata.

## Slide Companion Note

The Week 7 slide deck lives at `slides/week7/07-violence-safety-mobility-and-labor-market-access.tex`. The deck defines why Week 7 is distinct from Week 6, models safety and reproductive autonomy as labor constraints, reviews domestic violence, workplace harassment and violence, mobility and commuting, birth control, abortion access, and IVF, then closes with hidden harms, research designs, and the bridge to Week 8.

## Bridge Forward

Week 8 moves to comparative and global gender in labor-market development. The safety constraints from Week 7 do not travel mechanically across settings. Public transport, legal credibility, informality, employer structure, reproductive access, family norms, and local labor demand shape whether the same mechanism appears as nonparticipation, occupational segregation, migration, informal work, fertility timing, or hidden welfare loss. That comparative variation is the next object.
