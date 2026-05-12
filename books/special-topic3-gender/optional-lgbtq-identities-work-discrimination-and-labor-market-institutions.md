# Optional Long Lecture. LGBTQ+ Identities, Work, Discrimination, And Labor-Market Institutions

This optional long lecture broadens the Gender Study sequence beyond male-female comparisons while staying squarely inside labor economics. The central question is: **how do sexual orientation, gender identity, workplace climate, disclosure, legal recognition, and employer institutions shape employment, earnings, hiring, benefits, and worker welfare?**

The lecture treats LGBTQ+ labor research as a substantive field. It is not a short add-on about identity categories. The economic objects are familiar from the rest of the course: access to jobs, screening, wages, hours, benefits, firm sorting, workplace treatment, legal protection, family-linked insurance, retention, safety, and welfare. The hard part is that the relevant identities and treatments are often only partly observed.

:::{admonition} Core points
:class: important

- LGBTQ+ labor research belongs in labor economics because it studies hiring, employment, wages, benefits, firm treatment, disclosure, legal protection, sorting, and worker welfare.
- Sexual orientation, gender identity, legal category, perceived identity, and disclosure are different empirical objects. A paper must say which object it observes.
- Hiring discrimination, within-job treatment, selection into firms, and selection out of the labor force are distinct margins.
- Legal recognition and legal protection can change employer behavior, worker beliefs, applications, benefits, and family labor supply, but law on the books is not the same object as workplace treatment.
- Wages and employment miss hidden harms: climate, concealment, harassment, safety, dignity, stress, and the option value of being able to move, disclose, or use benefits without penalty.

:::

## Learning Objectives

By the end of this optional lecture, students should be able to:

1. distinguish sexual orientation from gender identity as empirical labor-market objects;
2. separate underlying population membership from disclosure, visibility, legal category, and employer perception;
3. evaluate evidence on LGBTQ+ employment, earnings, occupation, benefits, hiring discrimination, workplace climate, and legal institutions;
4. state the identifying variation and observed margin in correspondence studies, large-employer audit platforms, administrative identity-linkage designs, policy/event-study designs, and survey/list experiments;
5. explain why transgender and nonbinary labor-market evidence creates distinct measurement, privacy, and design problems;
6. identify research opportunities where hidden harms, firm behavior, benefit design, and new data can make a frontier contribution;
7. carry the lesson into the final synthesis week by writing a labor-focused research design with a clear mechanism, comparison group, and welfare object.

## Bridge

Weeks 1 through 9 built the course around labor-market margins rather than one wage-gap statistic. Week 1 clarified measurement. Weeks 2 and 3 studied household allocation, care, human capital, expectations, and occupational sorting. Week 4 moved inside firms. Week 5 studied norms, bargaining, and institutions. Week 6 treated policy as an intervention with incidence. Week 7 made safety and hidden harms part of labor-market access. Week 8 asked which mechanisms travel across settings. Week 9 asked how new data and measurement choices change what researchers can identify.

This optional lecture applies that architecture to sexual orientation and gender identity. It asks how the familiar labor objects change when the measured category may be a same-sex couple, a direct sexual-orientation response, a gender-identity survey module, a legal gender-marker change, an employer-perceived signal, a disclosed identity, or a climate measure.

The forward bridge is the final synthesis lecture. If students can write a credible design in this field, they have learned the central habit of the course: begin with the labor object, define the measured identity object, name the observed margin, state the identifying variation, and avoid converting a partial outcome into a complete welfare claim.

## Field Core

### Why LGBTQ+ Labor Research Belongs In Labor Economics

The field now has full economics reviews. Badgett, Carpenter, Lee, and Sansone review the economics of sexual orientation and gender identity across family behavior, human capital, labor markets, discrimination, law, and policy [@badgettCarpenterLeeSansone2024review]. Badgett, Carpenter, and Sansone provide a compact Journal of Economic Perspectives overview that is especially useful for teaching because it connects measurement, marriage recognition, labor supply, benefits, and discrimination [@badgettCarpenterSansone2021lgbtqeconomics].

The core labor objects are:

- employment, participation, hours, and job retention;
- wages, earnings, occupations, tasks, and firm sorting;
- applications, callbacks, interviews, and offers;
- employer-sponsored benefits, partner recognition, insurance, and leave;
- climate, disclosure, harassment, safety, and wellbeing at work;
- legal protections, family recognition, and enforcement;
- welfare beyond observed wages and employment.

Older wage-gap evidence already made sexual orientation a labor-market question. Badgett estimates wage effects associated with sexual orientation discrimination using survey-based labor-market outcomes [@badgett1995WageEffects]. Klawitter synthesizes earnings estimates across studies and shows why the sign and size of gaps vary across groups, data, and specifications [@klawitter2015MetaAnalysis]. Those studies locate the field's first descriptive object. The newer frontier asks sharper design questions: which margin is observed, what varies, and which identity object does the data actually measure?

### Measurement: Identity, Disclosure, And Population Definition

Measurement is not a technical preface. It defines the estimand. Sexual orientation, gender identity, sex assigned at birth, legal sex, legal gender marker, partner sex, disclosure, presentation, and employer perception are related but not interchangeable.

```{include} assets/tables/10-lgbtq-measurement-and-core-outcomes-map.md
```

A same-sex couple variable in census-style data identifies partnered same-sex households. It does not identify all lesbian, gay, bisexual, queer, transgender, or nonbinary workers. A direct sexual-orientation question can identify self-reported orientation, but nonresponse and disclosure bias are part of the object. A gender-identity module can identify transgender and nonbinary respondents more directly, but small cells and privacy constraints become substantive design issues. An administrative gender-marker or name-change linkage can produce a high-fidelity panel for a selected group, but it does not represent every transgender worker.

This distinction changes interpretation. Suppose {math}`Y_i` is earnings and {math}`M_i` is the measured identity object. A descriptive gap,

```{math}
\Delta^Y = E[Y_i \mid M_i=1] - E[Y_i \mid M_i=0],
```

is a gap for the measured group, not necessarily for the underlying population. If {math}`M_i` is "same-sex partnered household," the estimate is about partnered households. If {math}`M_i` is a legal marker change, the estimate is about workers who made that administrative transition. If {math}`M_i` is a resume signal, the estimate is about employer response to that signal.

Carpenter and Lee illustrate the value and limits of administrative identity linkage. They use gender-marker and name-change information to identify a large group of transgender workers, then study earnings dynamics using within-person, sibling, and coworker comparisons [@carpenterLee2024transgenderearnings]. The observed margin is administrative earnings and employment. The identifying variation is not "random assignment to transgender status"; it is variation over time and across linked comparison groups for a high-fidelity but selected measured population.

### Employment, Earnings, Occupation, And Benefits

LGBTQ+ labor outcomes cannot be summarized by one average. The review evidence shows heterogeneity across gay men, lesbians, bisexual workers, transgender workers, nonbinary workers, partnered and unpartnered people, occupations, countries, and disclosure environments [@badgettCarpenterLeeSansone2024review; @badgettCarpenterSansone2021lgbtqeconomics].

**Employment and earnings.** Earnings and employment evidence identifies visible outcomes, not all welfare costs. Survey studies can compare self-identified groups, but they often face small cells and selection into disclosure. Administrative linkage can deliver large panels, but it measures administrative transitions and linked comparison groups. Carpenter, Eppink, and Gonzales use transgender-status and gender-identity measures in U.S. survey data to estimate socioeconomic differences; the observed margins are employment, poverty, and related socioeconomic outcomes, while the identifying variation is cross-sectional identity measurement rather than exogenous treatment [@carpenterEppinkGonzales2020TransgenderStatus].

**Occupation and firm sorting.** Sexual orientation and gender identity may affect occupation choice, applications, employer screening, and retention. Observed occupational gaps could reflect preference, anticipated discrimination, climate, safety, benefits, family constraints, or prior exclusion. A credible paper has to say whether it observes applications, accepted jobs, firm identifiers, moves, or post-hire treatment.

**Benefits and family-linked compensation.** Employer-sponsored benefits are labor-market institutions. Health insurance, partner benefits, spousal recognition, parental leave, and dependent coverage affect compensation and household labor supply. Carpenter, Postolek, and Warman study employer choices about same-sex domestic partner benefits around marriage equality; the observed margin is employer benefit provision, and the identifying variation comes from legal change that altered the relationship between marriage recognition and domestic partner benefits [@carpenterPostolekWarman2024sameSexBenefits]. Carpenter, Gonzales, McKay, and Sansone study how the Affordable Care Act dependent-coverage provision changed insurance coverage for people in same-sex couples; the observed margin is insurance coverage, and the identifying variation is policy exposure by age and eligibility [@carpenterGonzalesMckaySansone2021aca].

Benefits matter because they convert legal family recognition into labor-market compensation. A wage-only study would miss that channel.

### Hiring Discrimination And Access To Jobs

Hiring discrimination is one of the strongest parts of the field because the designs manipulate identity signals and observe employer response.

```{include} assets/tables/10-hiring-climate-benefits-and-law-map.md
```

Tilcsik's field experiment is the canonical U.S. anchor. The design sends otherwise similar resumes while varying a signal of gay identity; the observed margin is employer callback, and the identifying variation is randomized resume content [@tilcsik2011prideprejudice]. The estimate is sharp for discrimination at the callback stage. It does not identify post-hire wages, promotion, climate, or worker beliefs about whether to apply.

Weichselbaumer's correspondence experiment varies sexual-orientation and gender-presentation signals in job applications; the observed margin is employer invitation or response, and the identifying variation is randomized application content [@weichselbaumer2003sexualorientation]. The design is useful because it shows that sexual orientation can interact with gender presentation at the hiring margin.

Granberg, Andersson, and Ahmed provide field-experimental evidence on hiring discrimination against transgender applicants. The observed margin is employer response to applications, and the identifying variation is randomized transgender versus cisgender applicant signaling [@granbergAnderssonAhmed2020transhiring]. The paper belongs in the same methodological family as Tilcsik, but the measured identity object and signal differ.

Large-employer audit platforms push the design frontier. Kline, Rose, and Walters study systemic discrimination among large U.S. employers by sending randomized applications at scale; the observed margin is employer response, and the identifying variation is randomized applicant signals across many firms [@klineRoseWalters2021systemic]. The key labor-economics contribution is firm heterogeneity: discrimination can be concentrated in particular employers rather than evenly distributed across the market.

The teaching distinction is:

- hiring discrimination concerns access at the screening margin;
- within-job treatment concerns pay, assignments, promotion, climate, harassment, and retention after entry;
- selection into applications concerns whether workers choose or feel able to apply;
- sorting into firms concerns where workers end up conditional on search, screening, offers, benefits, and climate.

An audit can identify one margin cleanly while leaving the others open.

### Workplace Climate, Disclosure, Harassment, And Hidden Harms

Disclosure and workplace climate are labor-market objects because they affect job choice, retention, productivity, promotion, voice, safety, and welfare. They are also hard to measure. Standard wage and employment data usually do not observe concealment costs, harassment, anxiety about outing, manager support, coworker treatment, or the option value of moving to a safer firm.

Survey and list-experiment designs help when the object is stigma or support. Aksoy, Carpenter, and Sansone use a double list experiment and survey evidence to measure discrimination-relevant attitudes toward transgender people; the observed margin is reported and indirectly elicited support or stigma, and the identifying variation comes from list-experiment assignment and survey design [@aksoyCarpenterSansone2025understanding]. The design does not observe wages directly, but it measures a climate-relevant object that wage data often miss.

Climate studies should avoid two mistakes. First, do not treat disclosure as the same thing as identity. Disclosure can be a choice under constraint, a response to climate, or a signal employers and coworkers receive. Second, do not treat absence of a wage gap as absence of harm. A worker may retain earnings by concealing identity, avoiding certain firms, accepting a narrower job set, or bearing nonpecuniary costs.

A simple welfare object clarifies the issue:

```{math}
V_i =
E\left[
w_i - \phi h_i - \rho r_i - \psi H_i + B_i + A_i
\right],
```

where {math}`w_i` is compensation, {math}`h_i` is hours or effort cost, {math}`r_i` is risk, {math}`H_i` is hidden harm such as harassment or concealment, {math}`B_i` is benefit value, and {math}`A_i` is amenity, dignity, voice, or authority. Most datasets observe only pieces of this expression.

### Legal Institutions: Protection, Marriage, And Benefit Design

Law matters in this field, but the labor question is not simply whether a legal rule exists. The labor question is which margin changes: employer screening, worker applications, benefit design, insurance coverage, specialization within couples, disclosure, reporting, retention, or welfare.

**Anti-discrimination protection.** Legal protection can change employer behavior directly. It can also change worker beliefs about whether applying, disclosing, or reporting is safe. A policy/event-study design needs to state the variation in legal exposure, the affected population, the outcome observed, and whether the estimate captures employer compliance, worker response, or both.

**Marriage and family recognition.** Sansone studies same-sex marriage, employment, and discrimination. The observed margins include employment and labor-market behavior for same-sex couples, and the identifying variation comes from changes in marriage recognition across jurisdictions and time [@sansone2019pinkwork]. The labor object is not marriage alone; it is how legal recognition changes work, household specialization, employer treatment, and discrimination-relevant labor outcomes.

**Benefits and insurance.** Employer benefit design is a labor-market institution. Domestic partner benefits, spousal coverage, dependent coverage, and employer-sponsored insurance can mediate the labor effects of legal recognition. Carpenter, Postolek, and Warman show employer benefit responses to same-sex marriage recognition [@carpenterPostolekWarman2024sameSexBenefits]. Carpenter, Gonzales, McKay, and Sansone show how dependent coverage policy can affect insurance for same-sex couples [@carpenterGonzalesMckaySansone2021aca]. These papers turn benefits from background institutional detail into an outcome and mechanism.

The cleanest teaching habit is to separate legal recognition from actual treatment. A law may change formal eligibility without changing climate. A climate shift may change disclosure without changing formal benefits. A benefits reform may improve welfare without changing wages. These are different labor margins.

### Transgender And Nonbinary Labor-Market Evidence

Transgender and nonbinary labor-market research is one of the fastest-moving frontiers because the measurement problem is severe and the labor objects are central: hiring, earnings, benefits, documentation, legal protection, workplace climate, and safety.

Three empirical strategies are especially useful for students:

- **Correspondence and audit studies** randomize identity signals and observe callbacks or employer responses. Granberg, Andersson, and Ahmed identify callback discrimination at the hiring margin for transgender applicants [@granbergAnderssonAhmed2020transhiring]. Eames studies hiring discrimination at the intersection of sex and nonbinary gender identity using a resume-audit design; the observed margin is employer response, and the identifying variation is randomized resume information about sex and nonbinary identity [@eames2025].
- **Administrative identity-linkage designs** observe earnings and employment over time for high-fidelity measured groups. Carpenter and Lee use administrative markers and linked comparison groups to study transgender earnings dynamics [@carpenterLee2024transgenderearnings].
- **Survey and list-experiment designs** measure stigma, support, and perceptions that standard payroll data cannot see. Aksoy, Carpenter, and Sansone use list-experiment variation to study discrimination-relevant attitudes [@aksoyCarpenterSansone2025understanding].

The nonbinary frontier is particularly open. A nonbinary identity signal in an audit can identify employer response to a signal, but it does not measure all nonbinary workers. A survey can measure self-identification, but small cells and disclosure risk constrain heterogeneity. Administrative data may have no nonbinary category at all. This is not a reason to avoid the question. It is a reason to write the estimand carefully.

### Research Opportunities And Frontier Gaps

```{include} assets/tables/10-empirical-challenges-and-research-opportunities-map.md
```

The most promising contribution margins are:

**Link hiring to later careers.** Audits identify callback differences. Frontier work can connect screening to job entry, firm sorting, wages, promotion, retention, and climate. The hard design problem is linking a randomized or quasi-random hiring margin to post-hire outcomes without violating privacy or ethics.

**Measure hidden harms.** Climate, disclosure costs, harassment, and safety are central welfare objects. New work can link protected worker surveys, climate modules, complaint systems, turnover, absenteeism, health measures, and administrative labor outcomes. The design must distinguish prevalence from reporting and treatment from selection.

**Study worker beliefs and applications.** Legal protection may affect whether workers apply, disclose, bargain, report, or leave. Application data, survey experiments, and information treatments can separate employer discrimination from worker anticipation of discrimination.

**Open the firm black box.** Employer heterogeneity is a core labor-economics object. Large audits, personnel records, internal mobility data, benefits files, manager assignment, and policy rollouts can show whether barriers are concentrated in particular firms, occupations, supervisors, or benefit regimes.

**Improve transgender and nonbinary measurement.** Research needs privacy-safe designs that distinguish legal category, self-identified gender, perceived identity, administrative transition, and disclosure. The contribution can be methodological as well as substantive.

**Treat benefits as compensation.** Employer-sponsored insurance, leave, family recognition, and partner benefits are part of labor-market compensation. These margins are especially important when wages do not move but welfare does.

**Build comparative evidence.** Much of the strongest evidence comes from the United States and a small set of European settings. Comparative work should be mechanism-first: enforcement, benefits, family recognition, occupational structure, informality, public employment, and climate may all shape whether a result transports.

**Handle intersectionality with power and privacy.** LGBTQ+ labor outcomes interact with race, ethnicity, migration, disability, class, age, parenthood, and local institutions. Strong work pre-specifies aggregation, reports honest uncertainty, and protects disclosure.

## Research Lab

### Reproduce -> Diagnose -> Transfer

The optional LGBTQ+ lab is a bounded synthetic-data path. It is a teaching analog, not an official replication, and it does not require confidential audit, employer, benefits, survey, or administrative microdata.

**Reproduce.** The primary anchor is Tilcsik's correspondence experiment on employment discrimination against openly gay men [@tilcsik2011prideprejudice]. Students use deterministic synthetic audit data to reproduce callback-rate comparisons by identity signal, occupation, and employer climate. The observed margin is callback. The identifying variation is randomized identity signaling in otherwise comparable resumes.

**Diagnose.** Students compare the Tilcsik-style audit to transgender hiring evidence from Granberg, Andersson, and Ahmed [@granbergAnderssonAhmed2020transhiring]. They classify what each design observes well, what it misses, and why disclosure/visibility is not the same object as underlying population membership.

**Transfer.** Students transfer the design logic to policy and benefits evidence inspired by Sansone [@sansone2019pinkwork] and Carpenter, Postolek, and Warman [@carpenterPostolekWarman2024sameSexBenefits]. The transfer exercise distinguishes hiring discrimination from legal recognition, benefit design, and within-household labor-market response.

**Optional extensions.** Students can write design memos on administrative transgender earnings evidence [@carpenterLee2024transgenderearnings], large-employer audits [@klineRoseWalters2021systemic], or employer benefit responses [@carpenterPostolekWarman2024sameSexBenefits].

### Research-Design Checklist

A project pitch in this area should answer eight questions:

1. **Labor object.** Is the paper about employment, wages, applications, callbacks, benefits, firm sorting, climate, disclosure, harassment, safety, or welfare?
2. **Identity object.** Does the data measure sexual orientation, gender identity, legal category, same-sex partnership, disclosure, perceived identity, or an administrative transition?
3. **Observed margin.** Does the design observe applications, callbacks, accepted jobs, wages, benefits, climate, reports, retention, or family labor supply?
4. **Identifying variation.** Is the source of variation randomized resume signals, employer-level audit assignment, policy timing, administrative timing, survey/list-experiment assignment, or linked comparison groups?
5. **Population.** Is the estimate for applicants, employees, partnered couples, workers who disclose, workers in particular firms, or people with administrative marker changes?
6. **Sorting versus treatment.** Does the design observe selection into jobs or firms, treatment inside jobs, or both?
7. **Legal status versus workplace treatment.** Does legal recognition change formal eligibility, actual behavior, climate, or all three?
8. **Hidden welfare margin.** Which harms or benefits are invisible in wages and employment?

## Methods Box

:::{admonition} Methods Box: Distinguishing Margins In LGBTQ+ Labor Research
:class: note

**Sexual orientation versus gender identity.** Sexual orientation and gender identity are different empirical objects. Do not collapse them into one treatment unless the research question and measurement justify it.

**Disclosure versus membership.** An employer response to a resume signal identifies treatment of a visible or disclosed signal. It does not identify all outcomes for people who do not disclose or whose identity is not observed by the employer.

**Hiring discrimination versus within-job treatment.** Callback audits identify screening-stage discrimination. They do not identify pay-setting, task assignment, promotion, harassment, benefits, or retention after hire.

**Selection into firms versus firm treatment.** Lower employment or different firm sorting can arise from applications, offers, benefits, climate, safety, or anticipated discrimination. Within-firm evidence is needed for post-entry treatment.

**Legal protection versus actual workplace treatment.** Anti-discrimination law, marriage recognition, and benefit rules are institutional inputs. The observed margin may be employer compliance, worker beliefs, applications, insurance coverage, labor supply, or disclosure.

**Visible outcomes versus hidden harms.** Wages and employment are not complete welfare measures. Climate, concealment, harassment, safety, dignity, stress, and benefit access can change welfare even when earnings are unchanged.

**Design families.** Correspondence studies use randomized identity signals and observe callbacks. Large-employer audits add firm-level heterogeneity. Administrative identity-linkage designs observe earnings and employment for measured groups. Policy/event-study designs exploit legal timing and exposure. Survey/list experiments measure stigma and support when direct reporting is sensitive.

:::

## Reading Ladder And References

```{include} assets/tables/10-reading-and-lab-map.md
```

**Start with field framing.** Read Badgett, Carpenter, and Sansone for the compact JEP overview [@badgettCarpenterSansone2021lgbtqeconomics], then Badgett, Carpenter, Lee, and Sansone for the broader JEL review [@badgettCarpenterLeeSansone2024review]. Add Badgett's early wage paper and Klawitter's meta-analysis to see the field's descriptive starting point [@badgett1995WageEffects; @klawitter2015MetaAnalysis].

**Add hiring discrimination evidence.** Tilcsik is the primary field-experiment anchor for gay male hiring discrimination [@tilcsik2011prideprejudice]. Weichselbaumer extends the hiring logic to sexual orientation and gender presentation [@weichselbaumer2003sexualorientation]. Granberg, Andersson, and Ahmed add transgender applicant evidence [@granbergAnderssonAhmed2020transhiring]. Kline, Rose, and Walters show how large-scale employer audits can locate discrimination across firms [@klineRoseWalters2021systemic].

**Add law, recognition, and benefits.** Sansone connects marriage equality to employment and discrimination-relevant outcomes [@sansone2019pinkwork]. Carpenter, Postolek, and Warman study employer benefit design [@carpenterPostolekWarman2024sameSexBenefits]. Carpenter, Gonzales, McKay, and Sansone study dependent coverage and insurance for same-sex couples [@carpenterGonzalesMckaySansone2021aca].

**Add transgender and nonbinary frontiers.** Carpenter, Eppink, and Gonzales provide survey-based evidence on transgender socioeconomic outcomes [@carpenterEppinkGonzales2020TransgenderStatus]. Carpenter and Lee push the administrative earnings frontier [@carpenterLee2024transgenderearnings]. Aksoy, Carpenter, and Sansone measure discrimination-relevant attitudes with survey and list-experiment tools [@aksoyCarpenterSansone2025understanding]. Eames opens a nonbinary audit frontier [@eames2025].

## Exercises And Discussion Prompts

1. Pick one LGBTQ+ labor paper from the reading ladder. State the measured identity object, the observed labor margin, the identifying variation, and the missing welfare margin.
2. Compare Tilcsik-style hiring audits to Sansone-style policy/event-study evidence. Which design identifies employer screening? Which design identifies legal recognition effects? What does each miss?
3. Design a study of workplace disclosure. What is the treatment or variation? What outcome would reveal climate rather than only worker selection?
4. Rewrite a wage-gap claim as a welfare claim. Which terms in the welfare object are observed, and which are hidden?
5. Propose a transgender or nonbinary labor-market study that protects privacy while still distinguishing legal category, self-identified identity, perceived identity, and workplace treatment.
6. Write a final-synthesis proposal paragraph that begins with a labor object and only then introduces the identity measure, data source, and econometric design.

## Reproducibility And Code Lab Note

The optional LGBTQ+ lab lives at `labs/optional-lgbtq-identities-work-discrimination-and-labor-market-institutions/`. It uses deterministic synthetic data to practice audit reproduction, design diagnosis, and policy/benefits transfer. The smoke test runs only the bounded pedagogical path and does not require confidential microdata.

## Slide Companion Note

The slide deck lives under `slides/optional-lgbtq/`. The deck should not duplicate the chapter. It should define why LGBTQ+ labor research belongs in labor economics, bridge from Weeks 1 through 9, isolate measurement problems, compare evidence on earnings, hiring, climate, law, benefits, and transgender/nonbinary frontiers, and end with research opportunities and a bridge to the final synthesis lecture.

## Forward Bridge To Final Synthesis

The final synthesis lecture asks students to write credible research designs on gender and labor markets. This optional lecture makes the research-design problem sharper. A good project cannot say only "I study LGBTQ+ workers." It must say: here is the labor object, here is the identity measure, here is the observed margin, here is the identifying variation, here is the unobserved selection or hidden harm, and here is the welfare object. That is the bridge from an important topic to a publishable labor-economics design.
