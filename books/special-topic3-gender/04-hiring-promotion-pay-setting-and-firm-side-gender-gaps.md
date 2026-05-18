# Hiring, Promotion, Pay-Setting, And Firm-Side Gender Gaps

## Learning Objectives

By the end of Week 4, students should be able to:

1. distinguish gendered sorting into firms and jobs from differential treatment inside the same firm;
2. explain why firms are labor-market institutions that allocate rents, authority, schedules, metrics, promotion chances, and wage premiums;
3. map hiring screens, referrals, evaluations, promotions, supervision, task allocation, networks, bargaining, transparency, and retention to separate labor margins;
4. interpret firm-side evidence by naming the identifying variation, the observed margin, and the mechanism being measured;
5. compare audit or screening designs, personnel records, manager-assignment designs, matched employer-employee decompositions, policy reforms, and survey-linked administrative evidence;
6. connect Week 4 backward to worker-side sorting from Week 3 and forward to norms in Week 5 and policy incidence in Week 6.

## Opening Orientation

Week 4 moves inside organizations. The central question is how firms and internal labor markets produce gender differences in pay, promotion, authority, and retention. The week is not a generic discrimination lecture. It treats firms as active institutions that decide who enters, what information is used in screening, which tasks are visible, who has access to managers, how potential is rated, which jobs carry authority, how wages are set, and who finds it costly to stay.

The key discipline is to separate three channels. Workers may sort into firms and jobs with different wage premiums or career ladders. Conditional on entry, firms may treat workers differently through screening, evaluation, supervision, task assignment, networks, or promotion. Firms may also use pay-setting rules, bargaining procedures, transparency, and compliance practices that change how rents are divided. These channels interact, but they are not the same empirical object.

:::{admonition} Core points
:class: important

- Firms are labor-market institutions: they allocate jobs, authority, rents, schedules, performance metrics, promotion opportunities, and wage premiums.
- Gender gaps can come from sorting into firms and jobs, within-firm personnel processes, and firm-level pay-setting or bargaining rules.
- Hiring, promotion, task allocation, authority, pay-setting, retention, and exit are distinct margins; evidence should not collapse them into one firm-side gap.
- Worker sorting is not firm behavior. A within-firm mechanism requires evidence on what happens after workers enter the organization or face a firm policy.
- Personnel records, matched employer-employee data, manager-assignment designs, audits, policy reforms, and survey-linked administrative evidence are a major frontier of gender-and-labor research.

:::

## Bridge

Week 3 studied education, skills, aspirations, and occupational sorting. That material matters here because workers do not arrive at firms randomly. Early field choices, internships, search behavior, occupational entry, commuting constraints, and expected family timing affect which firms and jobs workers enter. A gender gap in exposure to high-premium firms may partly reflect pre-firm sorting.

Week 4 asks what happens next. Once workers enter firms, organizations screen, supervise, evaluate, assign tasks, set pay, structure promotion ladders, and create workplace conditions. Those decisions can amplify, offset, or transform the sorting that Week 3 described. The same person can face different wages and authority depending on the firm, manager, promotion process, network access, and pay-setting regime.

Week 5 will study norms, bargaining, identity, and institutions more directly. Week 6 will study policy incidence, including transparency, equal-pay rules, quotas, leave, childcare, and workplace protections. Week 4 builds the firm-side architecture those weeks need: before asking whether a norm or policy changes gender gaps, students need to know which firm margin it can move.

## Field Core

### Firms As Allocation Systems

A compact accounting object is useful:

```{math}
:label: eq-week4-firm-gap-map
\begin{aligned}
G_Y
&=
\Delta^{sort}_{Y}
+ \Delta^{personnel}_{Y}
+ \Delta^{pay}_{Y}
+ \Delta^{retention}_{Y}
+ \Delta^{interaction}_{Y}.
\end{aligned}
```

Here {math}`G_Y` is a gender-associated gap in a labor outcome {math}`Y`, such as wages, earnings, promotion, authority, hours, job quality, or retention. The term {math}`\Delta^{sort}_{Y}` captures sorting into firms, jobs, teams, schedules, and career ladders. The term {math}`\Delta^{personnel}_{Y}` captures within-firm screening, evaluation, supervision, promotion, networks, and task allocation. The term {math}`\Delta^{pay}_{Y}` captures firm wage premiums, bargaining, salary requests, pay scales, transparency, and compliance rules. The term {math}`\Delta^{retention}_{Y}` captures quits, exits, transfers, and avoidance of jobs with costly workplace conditions. The interaction term matters because pay-setting affects retention, task allocation affects promotion, and expected firm behavior can shape sorting before entry.

This is not an estimator. It is a map of claims. A matched employer-employee decomposition can separate firm-premium exposure from within-firm wage differences, but it usually says less about the informal interaction that produced a promotion. A manager rotation design can identify access to managers and promotion effects inside a firm, but it does not estimate national between-firm sorting. An audit or blind-screening design can isolate entry-stage treatment, but it may not observe downstream wages or authority.

```{include} assets/tables/04-firm-side-gap-mechanisms-map.md
```

### Sorting Into Firms And Jobs

The first channel is worker sorting into firms and jobs. Women and men may be attached to different employers, establishments, teams, schedules, occupations, or career tracks. These locations can differ in firm wage premiums, rent sharing, promotion ladders, managerial exposure, flexibility, harassment risk, and exit costs. Sorting can arise before the firm acts on a specific worker: field of study, search networks, commute preferences, information, anticipated discrimination, or expected care constraints may change the set of firms a worker applies to or accepts.

This channel must stay separate from firm treatment. If women are less likely to work at high-premium firms, the observed gap may reflect sorting into firms, employer screening, worker search, referrals, commuting constraints, or retention. The researcher needs data or design to say which one. Card, Cardoso, and Kline use matched employer-employee data to quantify how firm wage premiums and sorting contribute to the gender wage gap [@cardCardosoKline2016bargainingSortingGender]. The identifying object is a firm-side wage-premium decomposition using worker mobility and firm wage policies; the observed margin is wages and exposure to high-paying firms, not a direct measure of subjective promotion ratings.

The same point applies to competitive or high-variance workplaces. Field experiments on job entry show that job design and advertised compensation regimes can alter applicant pools [@floryLeibbrandtList2015CompetitiveWorkplaces]. That evidence belongs to the entry and sorting margin. It should not be read as proof about later promotion unless the design follows workers into internal careers.

### Hiring, Screening, And Entry

Hiring evidence asks whether firms filter applicants differently at the point of entry. A simple screening object is:

```{math}
:label: eq-week4-screening-object
H_{ij}
=
\mathbf{1}\{S_{ij}(X_i, A_i, G_i, R_i) \ge c_j\},
```

where {math}`H_{ij}` is advancement or hiring for applicant {math}`i` at firm or job {math}`j`, {math}`S_{ij}` is the screen, {math}`X_i` is productivity-relevant information, {math}`A_i` is availability or schedule information, {math}`G_i` is gender or a gender signal, {math}`R_i` is referral or network access, and {math}`c_j` is the cutoff. A blind or audit-style design changes what the evaluator observes while holding part of the application object fixed.

Goldin and Rouse are the classic hiring-screen anchor because blind auditions changed the information available to evaluators and observed advancement in orchestra hiring [@goldinRouse2000blindAuditions]. The identifying variation is the use of blind audition procedures; the observed margin is advancement or selection at entry. The paper is powerful because it isolates a screening rule. It does not directly estimate later mentoring, wages, task assignment, or retention.

Hiring also includes referrals and informal access. Referral networks can affect who learns about jobs, who gets vouched for, and whose application is interpreted as credible. These are firm-side processes when employers rely on referrals as a screening technology, but they can also reflect worker-side network formation before application. A credible design must say whether it observes applicant pools, referral use, callback rates, hiring, starting wages, or downstream progression.

```{include} assets/tables/04-hiring-promotion-and-pay-setting-map.md
```

### Promotion, Authority, And Leadership Pipelines

Promotion is not just delayed hiring. It is an internal allocation problem. Firms decide which workers receive stretch assignments, performance visibility, managerial sponsorship, client exposure, team leadership, training, and authority. A pipeline object can be written as:

```{math}
:label: eq-week4-promotion-pipeline
P_{i,t+1}
=
f(P_{it}, Q_{it}, M_{it}, N_{it}, T_{it}, E_{it}),
```

where {math}`P_{it}` is position or level, {math}`Q_{it}` is measured performance, {math}`M_{it}` is manager access, {math}`N_{it}` is network or sponsorship capital, {math}`T_{it}` is task assignment, and {math}`E_{it}` is evaluation or potential rating. The empirical question is whether promotion gaps remain after observing performance-relevant inputs and whether the design isolates a source of variation in manager access, rating rules, or assignments.

Cullen and Perez-Truglia study informal interactions with managers and career advancement [@cullenPerezTruglia2023oldBoysClub]. The key design uses within-firm variation in manager-worker contact and survey-linked measures of social interaction; the observed margins are schmoozing, promotion, and wage growth. The mechanism is not simply "men like men." The paper links access to managers, informal social channels, and career outcomes inside an organization.

Benson, Li, and Shue focus on subjective potential ratings and promotion [@bensonLiShue2026potentialPromotionGap]. The observed margin is the gap between realized performance, potential ratings, and subsequent promotion. This is a leadership-pipeline object: firms may evaluate "future potential" differently from current output, and that distinction matters when potential ratings allocate authority. The identifying challenge is to separate true forecast information from biased or strategically distorted evaluation.

Classic high-skill career evidence is also useful here. Bertrand, Goldin, and Katz show how hours, interruptions, and career structure generate dynamic gender gaps among young professionals [@bertrandGoldinKatz2010dynamicsGenderGap]. In Week 4, the lesson is that career ladders and promotion rules are organizational technologies: they convert availability, visibility, and continuous attachment into pay and authority.

### Networks, Supervision, And Informal Access

Networks become a firm-side mechanism when internal careers depend on access to managers, mentors, sponsors, clients, or information. Informal access can change the probability that a worker receives useful feedback, is nominated for a role, learns about an opening, or is seen as leadership material. Supervision also determines which actions are visible and how performance is interpreted.

The design challenge is that informal access is usually endogenous. Workers who are already on a fast track may spend more time with managers, and managers may invest in workers they already expect to promote. Quasi-random manager rotation, reassignment, or shift overlap can help isolate variation in access. Survey-linked administrative data can then measure hidden channels such as mentoring, social interaction, and perceived inclusion while administrative records observe promotions and wages. The tradeoff is that the data are often one firm or one occupation, so external validity must be argued rather than assumed.

### Task Allocation And Low-Promotability Work

Firms allocate work, not only wages. Some tasks build human capital, visibility, revenue, client relationships, or managerial authority. Others are necessary but weakly rewarded: committee service, mentoring without credit, scheduling help, routine coordination, support work, or "office housework." Gender gaps can emerge when women are asked to do more low-promotability work or when they face stronger expectations to accept it.

Babcock, Recalde, Vesterlund, and Weingart provide the anchor for low-promotability tasks [@babcockRecaldeVesterlundWeingart2017lowPromotabilityTasks]. The observed margin is acceptance and receipt of requests for tasks with low promotability. The identifying variation comes from experimental task-request environments. The implication for firms is direct: internal task allocation can change later promotion even if current wages and formal titles are unchanged.

This mechanism connects to evaluation. If output metrics ignore support tasks, then workers who do more of them may appear less productive on the metrics that matter for promotion. If supervisors value those tasks rhetorically but not in pay or authority, the organization can sustain a gendered career penalty without an explicit discriminatory wage rule.

### Firm Pay Premiums, Bargaining, And Pay-Setting

Firm-side wage gaps also arise because firms pay different wage premiums and divide rents differently. A compact matched employer-employee object is:

```{math}
:label: eq-week4-firm-premium-object
\begin{aligned}
w_{ijt}
&=
\alpha_i
+ \psi_j
+ X_{it}'\beta
+ \theta_j Female_i
+ \varepsilon_{ijt}.
\end{aligned}
```

The worker component {math}`\alpha_i` captures persistent worker pay differences. The firm premium {math}`\psi_j` captures the wage level associated with firm {math}`j`. The term {math}`\theta_j Female_i` represents gender differences in pay within the same firm or in access to the firm's rent. A gender wage gap can then come from lower exposure to high-{math}`\psi_j` firms, lower within-firm rent shares, or both.

Card, Cardoso, and Kline are the central anchor for this decomposition because they separate sorting across firms from bargaining or rent-sharing differences within firms [@cardCardosoKline2016bargainingSortingGender]. The observed margin is wages in matched employer-employee data. The identifying variation comes from worker mobility and firm wage premiums, not from an audit. Roussille adds a pay-setting margin by studying ask salaries and the role of salary requests in gender pay inequality [@rousseille2024askGap]. The observed margin is requested pay and wage outcomes; the mechanism is a wage-setting rule that can transform a request gap into an earnings gap.

The firm-pay object matters because equal productivity does not imply equal pay when wages include rents, outside offers, bargaining, salary histories, posted ranges, or manager discretion. A firm can narrow a gap by standardizing pay bands, limiting salary-history use, publishing ranges, auditing internal equity, changing negotiation rules, or altering how raises respond to outside offers. Each design changes a different margin.

### Policy And Firm Design Frontier

Firm-facing policy asks whether rules change how firms set wages, disclose information, comply with equal-pay requirements, or redesign jobs. Pay transparency and equal-pay laws are especially useful because they target the wage-setting institution rather than only worker choices.

Blundell, Duchini, Simion, and Turrell study pay transparency and gender equality [@blundellDuchiniSimionTurrell2025payTransparency]. The observed margins include pay disclosure, wage gaps, and firm responses to transparency requirements. The identifying variation comes from policy exposure and treated versus untreated firms or workers. Baker, Halberstam, Kroft, Mas, and Messacar provide another pay-transparency anchor using policy variation in Canada [@bakerHalberstamKroftMasMessacar2023PayTransparency]. These papers force students to ask whether a reform reduces gaps by changing bargaining, compressing wages, changing raises, changing sorting, or changing who remains at the firm.

Gentile Passaro, Kojima, and Pakzad-Hurson study equal pay for similar work [@gentilePassaroKojimaPakzadHurson2026equalPaySimilarWork]. This is a firm-design object: the policy target is the pay rule across comparable jobs, but firms may respond through job classification, task assignment, wage compression, compliance effort, or workforce composition. A credible policy analysis must observe the margin that moves, not only the post-reform average gap.

```{include} assets/tables/04-data-and-identification-map.md
```

### Retention, Exit, And Workplace Conditions

Retention is a firm-side outcome, not an afterthought. A worker who leaves a high-wage or authority-bearing path because of harassment, exclusion, unpredictable schedules, weak protection, or poor managerial support experiences a labor-market loss even if the departure is voluntary in the administrative data. Exit can also create selection: the workers observed inside a firm after several years are those who found the workplace tolerable, feasible, or worth the cost.

Folke and Rickne study sexual harassment and gender inequality in the labor market [@folkeRickne2022sexualHarassment]. The observed margins include workplace conditions, segregation, valuation, and labor-market inequality. The identification problem is not the same as a wage decomposition or audit. It combines nonwage workplace conditions with retention, sorting, and the cost of remaining in certain jobs. For Week 4, the main lesson is that authority and pay cannot be separated from the conditions under which workers must exercise that authority or earn that pay.

Retention also links Week 4 to Week 7 on violence, safety, mobility, and labor-market access. The mechanism appears here because firms create and enforce workplace conditions; it returns later as a broader safety and welfare object.

## Research Lab

The Week 4 research lab is organized as **Reproduce -> Diagnose -> Transfer**. The purpose is to train students to separate within-firm mechanism measurement from hiring-screen evidence and policy evidence.

**Reproduce.** The primary lab anchor is Cullen and Perez-Truglia on the old boys' club [@cullenPerezTruglia2023oldBoysClub]. Students use deterministic synthetic personnel data to reproduce a manager-access exercise. The observed margins are informal manager interaction, promotion, and wage growth. The identifying variation is simulated manager overlap or reassignment, which stands in for quasi-random access to managers.

**Diagnose.** Students classify each output as sorting, within-firm treatment, pay-setting, or retention. They write a design memo naming the treatment, comparison group, observed margin, and what would be required to interpret the estimate as a within-firm mechanism.

**Transfer.** The challenge anchor is Goldin and Rouse on blind auditions [@goldinRouse2000blindAuditions]. Students transfer the same diagnostic logic to a synthetic screening setting. The key contrast is that the blind-screen design observes entry-stage advancement, while the old-boys-club exercise observes internal career progression.

**Optional frontier prompt.** Students can extend the memo to pay transparency [@blundellDuchiniSimionTurrell2025payTransparency] or subjective potential ratings [@bensonLiShue2026potentialPromotionGap]. The prompt asks which margin is observed, what variation identifies it, and whether the paper measures a reduced-form policy effect or a within-firm mechanism.

Open research questions for the lab:

1. When do informal networks reflect productivity information, favoritism, sponsorship, or exclusion?
2. Which manager-assignment designs plausibly isolate access to authority rather than worker sorting?
3. How should a researcher connect an entry-stage audit to later wage and promotion outcomes?
4. Which pay-setting reforms reduce gaps by changing bargaining rather than compressing wages or changing sorting?
5. What data would jointly observe referrals, manager access, task allocation, pay rules, promotion, and exit?

## Methods Box

:::{admonition} Methods Box: Name The Variation And The Margin
:class: note

**Audit and screening designs.** Use randomized identity signals, blind procedures, or audit-style applications. Best for entry-stage advancement or hiring. Weak for downstream promotion unless linked to later records.

**Personnel records and promotion models.** Use internal data on ratings, performance, levels, assignments, pay, and promotions. Strong for observing career margins; identification depends on the source of variation in managers, tasks, ratings, or rules.

**Manager rotation or quasi-random assignment.** Use reassignment, overlap, shift timing, or rotation to isolate access to managers or supervisors. The observed margins are mentoring, interaction, performance visibility, promotion, and wage growth.

**Matched employer-employee decompositions.** Use worker mobility and firm wage premiums to separate sorting across firms from within-firm pay differences. Strong for firm-premium accounting; often indirect on mechanisms.

**Firm-policy reforms.** Use transparency, equal-pay, salary-history, disclosure, or audit mandates. The observed margins may be pay compression, raises, disclosure, applications, retention, segregation, or compliance.

**Survey-linked administrative evidence.** Link hidden mechanisms such as social interaction, mentoring, harassment, or beliefs to personnel outcomes. Strong on mechanism measurement; vulnerable to reporting and external-validity concerns.

**Reduced form versus mechanism.** A reduced-form policy or screen tells whether an intervention moved an outcome. Within-firm mechanism measurement asks which internal process moved and how it produced pay, promotion, authority, or exit.

:::

## Reading Ladder And References

**Start with firms as wage-setting institutions.** Card, Cardoso, and Kline are the core matched employer-employee reading on firm premiums, sorting, bargaining, and the gender wage gap [@cardCardosoKline2016bargainingSortingGender].

**Hiring and screening.** Goldin and Rouse anchor blind screening and entry-stage advancement [@goldinRouse2000blindAuditions]. Use Flory, Leibbrandt, and List as a related job-entry design about competitive workplaces and applicant sorting [@floryLeibbrandtList2015CompetitiveWorkplaces].

**Promotion, authority, and networks.** Cullen and Perez-Truglia are the primary within-firm network and promotion reading [@cullenPerezTruglia2023oldBoysClub]. Benson, Li, and Shue are the frontier anchor for subjective potential ratings and promotion gaps [@bensonLiShue2026potentialPromotionGap].

**Tasks and visibility.** Babcock, Recalde, Vesterlund, and Weingart anchor low-promotability tasks and internal allocation [@babcockRecaldeVesterlundWeingart2017lowPromotabilityTasks].

**Pay-setting, bargaining, and transparency.** Roussille studies salary requests as a pay-setting margin [@rousseille2024askGap]. Blundell, Duchini, Simion, and Turrell and Baker, Halberstam, Kroft, Mas, and Messacar anchor pay transparency [@blundellDuchiniSimionTurrell2025payTransparency; @bakerHalberstamKroftMasMessacar2023PayTransparency].

**Equal pay and policy design.** Gentile Passaro, Kojima, and Pakzad-Hurson are the frontier equal-pay reading; Bertrand, Black, Jensen, and Lleras-Muney are useful for leadership and quota policy context [@gentilePassaroKojimaPakzadHurson2026equalPaySimilarWork; @bertrandBlackJensenLlerasMuney2019BoardQuotas].

**Retention, exit, and workplace conditions.** Folke and Rickne connect workplace conditions, harassment, segregation, and labor-market inequality [@folkeRickne2022sexualHarassment].

```{include} assets/tables/04-frontier-and-reading-map.md
```

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week4-firm-gap-map` to classify a pay gap into sorting, personnel, pay-setting, retention, and interaction components. Which terms can be estimated with matched employer-employee data alone?
2. Compare Goldin and Rouse with Cullen and Perez-Truglia. What is the identifying variation in each paper, and which margin is observed?
3. In Equation {eq}`eq-week4-promotion-pipeline`, explain how task assignment {math}`T_{it}` can affect promotion even if measured performance {math}`Q_{it}` is unbiased.
4. Explain why salary requests can be a firm pay-setting mechanism rather than only a worker preference.
5. Design a study of pay transparency. State the treated unit, comparison group, outcome, identifying variation, and two possible firm adaptations.
6. Give one example where worker sorting and firm behavior would be observationally bundled. What data would help separate them?

## Reproducibility And Code Lab Note

The Week 4 code lab lives at `labs/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates local synthetic personnel and screening data, reproduces a manager-access promotion exercise, and transfers the same diagnostic logic to blind screening. It runs without confidential microdata.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-hiring-promotion-pay-setting-and-firm-side-gender-gaps.tex`. The deck is a conceptual map rather than a duplicate of the chapter. It defines the central question, bridges from Week 3, separates sorting from within-firm treatment, covers hiring, promotion, networks, low-promotability tasks, firm wage premiums, pay-setting, transparency, equal-pay policy, and bridges forward to Weeks 5 and 6.

## Bridge Forward

Week 5 turns to norms, bargaining, identity, and institutions. The Week 4 firm-side mechanisms are where many of those norms become labor-market outcomes: self-promotion, negotiation, leadership expectations, social access, and ideas about commitment operate through hiring screens, managers, tasks, pay rules, and promotion ladders.

Week 6 then asks which policies move which margins. Transparency, equal-pay rules, quotas, leave, childcare, and workplace protection can affect sorting, pay-setting, promotion, retention, or compliance. The empirical question is not simply whether a policy reduces a gap, but which firm margin moved and who benefited.
