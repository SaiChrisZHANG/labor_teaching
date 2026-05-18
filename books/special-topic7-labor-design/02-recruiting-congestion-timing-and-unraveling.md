# Recruiting, Congestion, Timing, And Unraveling

## Learning Objectives

By the end of Week 2, students should be able to:

1. explain why recruiting-process frictions can generate misallocation even when worker and firm fundamentals are well aligned;
2. distinguish congestion, interview bottlenecks, exploding offers, early contracting, and unraveling as separate labor-market design failures;
3. identify within-vacancy margins including applicant pools, screening standards, recruiting intensity, wage information, offer timing, and vacancy-to-hire conversion;
4. connect professional labor-market timing evidence to modern vacancy, application, and job-posting data;
5. turn a recruiting-design question into an empirical labor paper with a frictive object, observed margin, data requirement, counterfactual, and identification strategy.

The central question is this: why do decentralized hiring markets often move too early, too fast, or too chaotically?

## Opening Orientation

Week 1 asked why some labor markets use centralized matching rules. Week 2 studies the decentralized recruiting processes that make those rules attractive in the first place. The key idea is that many matching failures arise inside the recruiting process rather than from worker or firm fundamentals alone. Applications, interviews, signals, wage information, offer deadlines, and acceptances are organized over time; each stage can create strategic behavior and congestion before the final match is ever observed.

This week is theory-heavy because timing and congestion are equilibrium objects. Firms issue early or exploding offers partly because they fear losing candidates to rivals. Workers accept offers early partly because waiting is risky. Application overload can be privately rational for workers and still socially costly for recruiters and other applicants. But the week is also empirically active. Modern labor data increasingly observe job posts, applications, recruiter actions, interviews, wages, vacancy durations, and hires, which means the black box between vacancy and hire can be studied directly.

The main labor object is the recruiting funnel: vacancy posted, applicant pool formed, applicants screened, interviews allocated, offers issued, offers accepted, and positions filled. Vacancy counts alone do not reveal this process. Two firms can post the same number of vacancies and produce different hires because they use different wages, search effort, screening standards, interview capacity, deadlines, and follow-up policies [@davisFabermanHaltiwanger2013; @carrilloTudelaMenzioVisschers2023].

:::{admonition} Core points
:class: important

- Recruiting frictions often operate through within-vacancy margins: applicant pools, screening standards, interview bottlenecks, recruiting intensity, wage information, offer timing, and vacancy yields.
- Congestion and unraveling are labor-market design problems, not residual details after worker and firm fundamentals have been modeled.
- Exploding offers and early contracting can be privately rational while reducing market thickness, information quality, mobility, and worker welfare.
- Professional labor markets such as gastroenterology fellowships, clinical psychology, law firms, clerkships, and medical training markets show that timing institutions are labor-market institutions.
- A strong empirical paper maps a specific recruiting-design failure to an observed margin, a meaningful counterfactual, and a labor-market welfare or fairness object.

:::

## Bridge

The bridge from Week 1 is direct. Centralized matching can improve labor allocation when decentralized recruiting destroys thickness or makes offers arrive before information is ready. But the mechanism is not magic: it is a response to particular process failures. Week 2 opens those failures.

Labor II gives the background search language: vacancies, matching functions, job-finding rates, recruiting intensity, and wage posting. Market design adds a sharper institutional question: how do rules about applications, interviews, deadlines, information disclosure, and offer timing change equilibrium behavior? A recruiting market can fail because workers and firms are poor matches, but it can also fail because the process makes good matches hard to discover, compare, or wait for.

The distinction matters for policy. If the problem is worker skill, the intervention may be training or screening. If the problem is wage opacity, the intervention may be disclosure. If the problem is interview bottlenecks, the intervention may be application limits, signals, or queue design. If the problem is unraveling, the intervention may be timing coordination or a centralized match. Week 2 teaches students to name the frictive object before naming the solution.

## Field Core

### Recruiting Frictions Versus Worker And Firm Fundamentals

A useful first diagnostic is to ask whether the observed failure comes from fundamentals or from process design. Fundamentals include worker skill, firm productivity, job amenities, location preferences, and wage capacity. Process design includes the rules and technologies that govern how workers and firms find each other: posting language, wage disclosure, application costs, applicant ranking, interview slots, callback speed, offer deadlines, and acceptance windows.

The distinction is not always clean. A high-wage vacancy may attract more applications because the job is better, because wage information improves directed search, or because the platform ranks high-wage jobs more visibly. A long vacancy duration may reflect low demand for the job, high hiring standards, too little recruiter effort, slow interviewing, or strategic waiting for a better applicant. The empirical problem is to separate the labor-market object from the process that reveals it.

Recruiting-process failures tend to show up as:

- many applications with low interview conversion;
- interview slots filled before strong applicants arrive;
- high-quality applicants applying to the same visible jobs while other vacancies remain thin;
- firms screening slowly or holding standards fixed while vacancy duration rises;
- early offers made before later information arrives;
- workers accepting dominated offers because deadlines are short;
- firms and workers investing in timing strategies instead of match quality.

Those are not small implementation details. They determine who receives interviews, who can wait, who bears risk, and which vacancies convert into hires.

```{include} assets/tables/02-core-process-map.md
```

### The Vacancy As A Recruiting Funnel

Many baseline search models treat a posted vacancy as the employer-side unit of labor demand. Week 2 asks what happens inside the vacancy. A vacancy has at least seven margins:

1. **Applicant pool size.** How many workers apply?
2. **Applicant composition.** Which applicants apply, and how well do they fit?
3. **Screening technology.** How costly is it to review applicants and distinguish fit?
4. **Interview capacity.** How many serious candidates can be evaluated?
5. **Hiring standards.** How selective is the firm conditional on applications?
6. **Recruiting intensity.** How much effort, wage generosity, advertising, or follow-up does the firm use?
7. **Offer timing and yield.** How quickly are offers made, how long can workers hold them, and how many accepted hires result?

Let {math}`A_v` denote applications to vacancy {math}`v`, {math}`I_v` interviews, {math}`O_v` offers, and {math}`H_v` hires. Three simple yield measures already open the black box:

```{math}
:label: eq:week2-recruiting-yields
\text{interview yield}_v = \frac{I_v}{A_v},
\qquad
\text{offer yield}_v = \frac{O_v}{I_v},
\qquad
\text{vacancy yield}_v = \frac{H_v}{A_v}.
```

These objects can move in different directions. Wage transparency might increase applicant quality and reduce wasted applications. Application caps might reduce applicant volume but improve recruiter attention. Higher hiring standards might lower vacancy yield even when applicant quality is high. Recruiting intensity might increase hires per vacancy without changing the number of posted vacancies. The empirical task is to observe enough of the funnel to distinguish these mechanisms.

Establishment-level evidence shows that vacancy behavior varies across employers in ways that vacancy counts alone cannot explain [@davisFabermanHaltiwanger2013]. Carrillo-Tudela, Menzio, and Visschers make the recruiting-policy margin explicit by connecting firm recruiting choices, job-filling rates, and matching efficiency [@carrilloTudelaMenzioVisschers2023]. That is why this week treats within-vacancy margins as central objects rather than residual details.

### Congestion, Applicant Behavior, And Directed Search

Congestion arises when privately rational search behavior imposes costs on others. Workers may apply broadly because applications are cheap and uncertainty is high. Firms then face larger, noisier applicant pools, which can make screening slower or less accurate. Workers respond by sending still more applications because each application has a lower callback probability. This feedback can generate a congested equilibrium even when many potentially good matches exist.

Directed search can reduce congestion if workers observe enough information to target vacancies where their fit and acceptance probability are high. Wage information is one important example. Online job-board evidence shows that applicants respond to posted wages and job attributes, so the design of job postings changes where applications go [@banfiVillenaRoldan2019]. Wage transparency can alter both applicant volume and applicant selection, which makes it a recruiting-design intervention rather than only a pay-policy intervention [@cullen2024; @balgovaTekleselassieHenselWitte2025].

The same logic applies to platform rankings, recommendations, and visibility rules. Intermediaries can reduce search costs and improve matches, but they can also concentrate attention on already-visible jobs or workers [@stantonThomas2016; @horton2017]. A platform that changes application costs, displays queue length, limits applications, introduces preference signals, or auto-pauses overloaded vacancies is not only changing user interface design. It is changing labor-market congestion.

### Interview Bottlenecks And Hiring Standards

Interview capacity is often the binding scarce resource. Firms may receive hundreds of applications, but only a small number of candidates can be seriously evaluated. That turns interview slots into an allocation device. If interview allocation is noisy, early, or biased toward visible signals, match quality can suffer even when the applicant pool contains strong candidates.

Hiring standards are also endogenous. A firm facing a thick applicant pool may raise standards and wait. A firm facing a thin pool may lower standards, raise wages, advertise harder, or extend deadlines. A firm with limited recruiter bandwidth may leave positions unfilled even when a suitable applicant exists in the pool. These choices are labor-demand behavior, not merely administrative slack.

Older firm-level evidence on hiring procedures already emphasized that firms differ in how they recruit and screen workers [@holzer1987hiring]. Modern vacancy and application data make those procedures more measurable. The frontier question is not simply whether a vacancy exists, but whether the vacancy is worked: how intensely it is advertised, how quickly applicants are reviewed, how interview slots are rationed, how standards adjust, and how offers convert into accepted hires.

### Timing, Exploding Offers, Early Contracting, And Unraveling

Unraveling occurs when transactions move inefficiently early. In labor markets, unraveling often emerges from strategic timing. A firm makes an early offer because it fears losing a candidate. The candidate accepts because waiting risks having no offer later. Other firms and workers then move earlier too. The market loses thickness because choices are made before all participants and information arrive.

Roth and Xing's study of timing institutions shows that many markets develop rules, norms, or bottlenecks because decentralized timing is unstable [@rothXing1994]. Their analysis of clinical psychologists highlights how turnaround time and offer bottlenecks can make decentralized matching perform poorly [@rothXing1997]. Niederle and Roth's work on gastroenterology fellowships is especially useful for labor economics because it studies a professional labor market with and without a centralized match, connecting unraveling to mobility, hiring practices, wages, and placement outcomes [@niederleRoth2003; @niederleRoth2007].

Exploding offers are a sharp example. A short deadline can help a firm lock in a candidate before competitors act. But it also shifts risk to workers, reduces comparison across jobs, and can prevent later-arriving information from improving the match. Experimental and institutional work on exploding offers emphasizes that market culture and rules can determine whether participants wait for better information or race toward early commitments [@niederleRoth2009].

Unraveling matters because it changes:

- who can afford to wait;
- whether candidates with later signals are disadvantaged;
- whether firms compete on match quality or deadline pressure;
- whether small or less-connected programs lose access to candidates;
- whether early information networks become a source of inequality;
- whether the market remains thick enough for good matching.

Professional labor markets make these stakes visible. Gastroenterology fellowships, medical training transitions, law firms, clerkships, clinical psychology internships, and other entry markets are not abstract examples. They allocate career starts, training opportunities, employer staffing, geographic mobility, and prestige. Timing rules are therefore labor-market institutions [@roth2012timing; @ashlagiEtAl2023].

### Coordinated, Centralized, And Decentralized Design Responses

The welfare comparison is not simply "centralized good, decentralized bad." A centralized clearinghouse can preserve thickness and reduce early contracting, but it can also require participants to report preferences before learning is complete. A timing rule can slow the race, but it may be hard to enforce. Wage disclosure can improve directed search, but it may change bargaining and applicant composition. Application caps can reduce congestion, but they may disadvantage workers who need many draws.

The right design depends on the margin being fixed:

- **Congestion.** Use application costs, caps, signals, queue information, recommendation rules, or vacancy auto-pausing.
- **Interview bottlenecks.** Use structured screening, interview limits, staged disclosure, or better fit information.
- **Wage opacity.** Use wage posting, pay ranges, or transparency mandates.
- **Recruiting intensity.** Use employer incentives, recruiter capacity, vacancy management, or wage adjustments.
- **Unraveling.** Use timing coordination, offer-hold periods, centralized clearing, or participation rules.
- **Market thickness.** Use common dates, pooled clearing, or policies that reduce off-cycle contracting.

The design lesson is comparative. Name the failure, identify the margin, and ask whether the intervention targets that margin or only changes its symptoms.

### Empirical And Descriptive Evidence From Professional Labor Markets

The classic timing literature remains central because it shows how recruiting-process failures are observed institutionally. Before modern platform data, economists documented offer timing, bottlenecks, early commitments, centralized clearing, and market culture in professional labor markets [@rothXing1994; @rothXing1997; @niederleRoth2003; @niederleRoth2007; @niederleRoth2009].

Gastroenterology fellowships are a key teaching case. The market's movement between decentralized hiring and centralized matching gives students a concrete way to ask what timing coordination changes. Does it widen the scope of the market? Does it change mobility? Does it change wages or hiring practices? Does participation in the match select particular programs or fellows? These are empirical labor questions, not only mechanism-design questions.

Law firms and clerkships provide a complementary lesson. When prestige, networks, and early signals matter, unraveling can allocate opportunity before later performance information arrives. Timing reforms may improve fairness or reduce strategic pressure, but they can also be fragile if high-prestige participants defect. The central labor question is which workers bear the cost of early timing and which employers gain from it.

### Modern Data From Vacancies, Applications, And Job Posts

Modern recruiting data let researchers observe margins that older timing studies could only infer. Useful data sources include:

- employer vacancy records with posting dates, wages, recruiter actions, and closing dates;
- job-board data with applications, applicant characteristics, posting attributes, and platform rankings;
- interview and callback logs;
- offer timing and acceptance records;
- wage transparency or pay-range policy variation;
- linked employer-employee data connecting vacancies to hires, starting wages, and retention;
- platform experiments that change information, application costs, or visibility.

These data let the empirical design align more closely with the theory. A congestion paper needs applications and queues. A wage-information paper needs posted wages, applicant composition, and application behavior. A recruiting-intensity paper needs employer actions and vacancy yields. A timing paper needs offer dates and acceptance deadlines. A welfare paper needs downstream outcomes such as match quality, wages, retention, mobility, or worker risk.

The frontier literature is active because these objects are now measurable. Job search intensity and search duration can be studied directly [@fabermanKudlyak2019]. Vacancy duration and entry wages can be linked to worker and firm outcomes [@muellerOsterSchmieder2023]. Online markets permit experiments or quasi-experiments on congestion, application behavior, and queue design [@pallais2014; @horton2021autopause; @horton2024congestion; @fradkinHeMarinescu2024].

```{include} assets/tables/02-empirical-designs-box.md
```

### How A Recruiting-Design Question Becomes An Empirical Labor Paper

A credible empirical paper in this area should make five choices explicit.

**1. What is the frictive object?** The paper should name the failure precisely: application congestion, interview bottlenecks, wage opacity, early contracting, exploding offers, low vacancy yield, slow recruiting effort, excessive standards, or queueing at attractive jobs.

**2. What margin is observed?** The observed margin should correspond to the failure: applications per vacancy, applicant composition, interview-to-application conversion, offer timing, acceptance timing, vacancy duration, vacancy yield, posted wage, queue position, or eventual hire quality.

**3. What data are needed?** The data requirement follows from the theory. A within-vacancy paper needs vacancy, application, interview, offer, and hire records. A timing paper needs offer dates, deadlines, acceptance decisions, and market participation. A wage-information paper needs posting content and applicant behavior. A welfare paper needs post-hire outcomes.

**4. What counterfactual is meaningful?** The comparison might be a centralized match, a later common offer date, an offer-hold period, wage disclosure, an application cap, a preference-signaling system, a platform ranking change, or a recruiter-capacity shock. The counterfactual should fix the named margin rather than simply improve a final outcome.

**5. How is the effect identified?** Identification can come from institutional regime changes, staggered policy adoption, platform experiments, employer policy variation, shocks to recruiter capacity, discontinuities in visibility or eligibility, or structural models disciplined by observed applications and hires. The design must address equilibrium response: workers may change where they apply, firms may change standards, and high-prestige participants may defect from timing rules.

```{include} assets/tables/02-theory-to-empirical-bridge.md
```

The practical standard is translation. A paper should move from institution to friction, from friction to observed margin, from observed margin to counterfactual, and from counterfactual to welfare or fairness. Without that chain, it is easy to mistake a descriptive recruiting fact for a labor-market design result.

### Threats To Interpretation

Several threats are common.

**Endogenous participation.** Programs or firms may join centralized systems, timing regimes, or platforms selectively. Regime comparisons must ask whether participants changed alongside the rule.

**Unobserved standards.** A lower fill rate may mean fewer qualified applicants, higher standards, lower recruiter effort, or a better outside option. Without screening or interview data, the mechanism is hard to pin down.

**Equilibrium displacement.** Application caps, wage disclosure, or queue information may move congestion across vacancies rather than eliminate it.

**Incomplete welfare measurement.** Faster hiring is not necessarily better if it lowers match quality, shifts risk to workers, or worsens access for applicants without early information.

**Timing-rule enforceability.** A rule that works for compliant participants may fail if high-prestige firms or candidates can contract outside it.

These threats are not reasons to avoid the topic. They are the discipline that turns market-design intuition into applied labor economics.

## Research Lab

The Week 2 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Carrillo-Tudela, Menzio, and Visschers on recruitment policies, job-filling rates, and matching efficiency because it makes within-vacancy margins and recruiting intensity central [@carrilloTudelaMenzioVisschers2023]. The challenge anchor is Niederle and Roth on gastroenterology and centralized clearing because it illustrates unraveling, timing design, and the empirical value of observing markets with and without a match [@niederleRoth2003; @niederleRoth2007]. Roth and Xing provide the broader timing-institution frame [@rothXing1994].

The lab is not an official replication package for any paper. It uses deterministic synthetic vacancy-funnel and timing data to practice the empirical architecture. That conservatism is deliberate: the teaching path should not imply access to confidential employer recruiting logs, proprietary job-board data, or official professional-market offer files.

**Reproduce.** Students recreate a reduced fact about within-vacancy margins: vacancies with higher recruiting intensity, clearer wage information, and more interview capacity have higher vacancy-to-hire conversion and shorter durations in the synthetic teaching data. The goal is to reproduce the logic of opening the vacancy black box, not to reproduce official estimates.

**Diagnose.** Students decompose the gap between high- and low-yield vacancies into applicant-pool size, applicant quality, interview bottlenecks, offer timing, and standards. They classify which margins are observed directly and which remain latent. They also compare a stylized early-offer regime with a coordinated timing regime to see how unraveling can change acceptance timing and match quality.

**Transfer.** Students adapt the same research design to one neighboring labor market: application congestion on an online platform, wage disclosure in job posts, clerkship timing, fellowship matching, or public-service recruiting. The transfer memo must state the institution, frictive object, observed margin, required data, counterfactual design, identification strategy, welfare object, and main threat.

```{include} assets/tables/02-reading-and-lab-map.md
```

## Methods Box

:::{admonition} Methods Box: Recruiting Design As Empirical Labor Evidence
:class: note

**Start with the process map.** Write down the sequence from vacancy to application, interview, offer, acceptance, and hire before choosing an estimator.

**Open the vacancy black box.** Vacancy counts are not enough. Measure applicant pools, screening, interview capacity, standards, recruiting effort, wage information, offer timing, and yield.

**Name the equilibrium margin.** Congestion, unraveling, and exploding offers are strategic responses to the timing and capacity environment.

**Make the counterfactual institutional.** Compare a real rule or feasible design: centralized clearing, offer-hold period, timing rule, wage disclosure, application cap, signal, queue display, or platform ranking change.

**Track equilibrium response.** Workers can reallocate applications, firms can change standards, and high-status participants can move off mechanism.

**Keep welfare broader than speed.** Faster vacancy filling may be valuable, but the welfare object may also include match quality, wages, risk, access, fairness, retention, and mobility.

:::

## Reading Ladder And References

**Core timing and unraveling.** Start with Roth and Xing on timing imperfections and bottlenecks, then read Niederle and Roth on gastroenterology with and without a centralized match and on exploding offers as market culture [@rothXing1994; @rothXing1997; @niederleRoth2003; @niederleRoth2007; @niederleRoth2009]. Roth's timing overview is a useful synthesis for professional labor markets [@roth2012timing].

**Within-vacancy empirical core.** Read Davis, Faberman, and Haltiwanger on establishment-level vacancy and hiring behavior, then Carrillo-Tudela, Menzio, and Visschers on recruitment policies, job-filling rates, and matching efficiency [@davisFabermanHaltiwanger2013; @carrilloTudelaMenzioVisschers2023].

**Applications, information, and platforms.** Use Banfi and Villena-Roldan for directed search and wage information, Cullen for pay transparency, Pallais for entry-level hiring inefficiency, Stanton and Thomas for online hiring intermediaries, and Horton for recommendation experiments [@banfiVillenaRoldan2019; @cullen2024; @pallais2014; @stantonThomas2016; @horton2017].

**Frontier and modern data.** Use Faberman and Kudlyak on search intensity, Mueller, Oster, and Schmieder on vacancy durations and entry wages, Horton and coauthors on platform congestion, Fradkin, He, and Marinescu on competition avoidance versus herding, and Vohra on unraveling and inefficient matching [@fabermanKudlyak2019; @muellerOsterSchmieder2023; @horton2021autopause; @horton2024congestion; @fradkinHeMarinescu2024; @vohra2025unraveling].

## Exercises And Discussion Prompts

1. Give one example of a labor-market inefficiency that is primarily a within-vacancy problem rather than a vacancy-posting problem.
2. Why can exploding offers be privately rational yet socially inefficient?
3. What data would distinguish too many applicants from bad applicant composition, too few interview slots, overly strict standards, and low offer acceptance?
4. Compare a centralized clearinghouse, a timing rule, an offer-hold period, an application cap, and a wage-disclosure reform as solutions to decentralized recruiting failures.
5. Choose one professional entry market. What evidence would show that it has unraveled?
6. In a vacancy-level dataset, which variables would you need to measure recruiting intensity rather than only labor demand?
7. Suppose wage transparency increases applications to high-wage jobs and reduces applications to low-wage jobs. What welfare objects should be reported?
8. Design an empirical paper around a recruiting intervention. State the frictive object, observed margin, data, counterfactual, identification strategy, and welfare object.
9. What might go wrong if a timing rule is adopted by low-prestige employers but ignored by high-prestige employers?
10. When is faster vacancy filling a welfare improvement, and when might it be a warning sign?

## Reproducibility And Code Lab Note

The Week 2 code lab lives at `labs/02-recruiting-congestion-timing-and-unraveling/`. It is a bounded synthetic teaching path, not an official replication of Carrillo-Tudela, Menzio, and Visschers, Niederle and Roth, or Roth and Xing. The smoke path creates deterministic vacancy-funnel data; reproduces a compact within-vacancy yield summary; diagnoses recruiting intensity, wage transparency, interview bottlenecks, standards, and timing; and writes transfer prompts for neighboring labor markets.

The lab is conservative by design. It does not claim access to proprietary vacancy records, job-board applications, employer interview logs, professional-market offer files, or official replication packages. Its goal is to help students practice how a recruiting-process theory becomes an empirical labor design.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-recruiting-congestion-timing-and-unraveling.tex`. The deck mirrors the chapter structure without duplicating the prose: it opens with recruiting frictions versus worker and firm fundamentals, isolates congestion, vacancy yields, within-vacancy margins, exploding offers, and unraveling, connects professional-market evidence to modern vacancy and application data, and closes with the theory-to-empirical bridge and Research Lab workflow.

## Bridge Forward

Week 3 moves from recruiting-process design to labor contracts, screening, incentives, and moral hazard. The bridge is natural: once a worker and firm reach an employment relationship, the next design question is how contracts allocate risk, elicit effort, reveal information, and sustain cooperation when type, effort, and commitment are imperfectly observed.
