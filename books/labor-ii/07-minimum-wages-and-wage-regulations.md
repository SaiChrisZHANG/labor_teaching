---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Minimum Wages and Wage Regulations

## Learning objectives

By the end of Week 7, students should be able to:

1. explain why minimum wages are a direct policy test of competitive versus monopsonistic labor-market models;
2. distinguish wage effects, employment effects, hours effects, turnover effects, and reallocation effects;
3. state clearly what the employment debate is actually about and why different papers can disagree without studying different policies;
4. interpret minimum-wage evidence using the identifying variation, unit of observation, observed margin, and key unobserved object;
5. distinguish nominal minimum-wage changes from treatment-intensity or bite measures;
6. summarize what global evidence adds beyond the canonical U.S. debate;
7. connect minimum wages to adjacent wage-law literatures on enforcement, pay transparency, and equal-pay rules;
8. bridge backward to Week 6 monopsony and forward to Week 8 unions, bargaining, and worker voice.

The economic question for Week 7 is not only whether a wage floor changes employment. It is how wage floors reshape pay-setting, worker flows, hours, firm composition, compliance, and equilibrium adjustment once the competitive benchmark is no longer the only plausible description of labor markets [@cardKrueger1994; @dubeLesterReich2010; @cengizDubeLindnerZipperer2019; @dubeLindner2024].

## Bridge

Week 6 ended by treating monopsony as employer wage-setting power rather than as the special case of a literal one-employer town. Week 7 begins by asking what that shift does to the most famous labor-market policy debate. Under the competitive benchmark, a binding wage floor raises wages and moves firms up their labor-demand curve. Under monopsony or frictional settings, a wage floor can instead compress employer wage-setting power, raise wages, and reduce recruitment frictions enough that employment falls only slightly or may even rise over a range [@robinson1933; @manning2021monopsonyreview; @ashenfelterCardFarberRansom2022].

That is why minimum wages are the natural sequel to Week 6. They convert a positive theory of wage-setting power into a policy test. They also force discipline about margins. A paper can find large wage gains, small headcount changes, fewer sub-minimum jobs, lower turnover, some hours adjustment, and meaningful firm reallocation all at the same time. Those are not interchangeable outcomes. This week therefore keeps five distinctions explicit from the start.

1. wages versus employment;
2. headcount employment versus hours and hiring;
3. competitive predictions versus monopsony or frictional predictions;
4. legal policy changes versus treatment intensity or bite;
5. legal incidence versus observed incidence under imperfect compliance.

```{figure} assets/figures/07-competitive-vs-monopsony-minimum-wage.png
:name: fig-lii-w7-competitive-monopsony
Competitive and monopsonistic benchmarks make different employment predictions under the same binding wage floor. The minimum wage is therefore a policy test of labor-market structure, not only a policy level.
```

Figure {numref}`fig-lii-w7-competitive-monopsony` is the conceptual anchor for the week. The lecture begins with employment because that is the historically central controversy, but it quickly broadens to hours, turnover, worker reallocation, prices, and compliance. This broader map matters because the modern literature rarely argues that employers respond only on one margin [@dubeLindner2024; @dubeZipperer2024].

The forward bridge matters too. Week 8 asks what changes once wage determination is mediated not only by legal floors but also by unions, collective bargaining, and worker voice. Minimum wages are thus the first week in the policy block, not the last word on wage-setting institutions.

:::{admonition} Core Material
:class: tip
- minimum wages test competitive benchmarks against monopsony and other frictional benchmarks
- wages, headcount, hours, turnover, reallocation, and compliance are distinct margins
- treatment intensity or bite is often the relevant policy object rather than the nominal statutory change
- legal incidence and observed incidence can diverge under imperfect compliance
- modern minimum-wage debates are largely about which object a paper identifies
:::

:::{admonition} Optional Extension Block
:class: note
- frontier questions on spillovers, hiring standards, automation, and policy scale are surfaced later in the chapter under `Frontier extension block: unresolved questions and research opportunities`
:::

## Field Core

### Competitive, monopsony, and frictional benchmarks under a wage floor

The clean competitive benchmark is deliberately simple:

```{math}
:label: eq-lii-w7-competitive
N_t = D(w_t), \qquad w_t = \max\{w_t^\ast, \bar w_t\}.
```

Equation {eq}`eq-lii-w7-competitive` says that when the legal floor {math}`\bar w_t` exceeds the competitive wage {math}`w_t^\ast`, the observed wage rises and the firm moves along labor demand. In that benchmark, a binding floor raises pay and lowers employment. The mechanism is transparent: the firm does not face an upward-sloping labor supply to itself, so the policy acts like a pure increase in the wage price of labor.

The monopsony benchmark changes the logic:

```{math}
:label: eq-lii-w7-monopsony
N(\bar w) = S_f(\bar w), \qquad \text{for } w^m < \bar w < w^c.
```

Equation {eq}`eq-lii-w7-monopsony` states the knife-edge intuition students should remember. If the wage floor lies above the monopsony wage {math}`w^m` but below the competitive wage {math}`w^c`, employment can rise because the floor prevents the firm from exploiting an upward-sloping labor supply to the firm. This does not prove that observed minimum wages must raise employment. It shows why the sign of the employment effect is empirical rather than theory-free [@robinson1933; @manning2021monopsonyreview].

Search and frictional models push in the same direction even when the formal setup is not a textbook monopsony. If workers face imperfect information, geographic immobility, switching costs, or recruiting frictions, then a wage floor can reduce quit rates, improve applicant pools, or compress wage dispersion without mapping one-for-one into competitive employment losses. The right way to teach this is not to say that monopsony "solves" the minimum-wage debate. It is to say that Week 6 made non-competitive predictions plausible enough that students should not treat the competitive sign prediction as the only benchmark.

### Treatment intensity matters more than the nominal policy change

The modern literature rarely interprets a policy using only the statutory increase. The central object is usually policy bite:

```{math}
:label: eq-lii-w7-kaitz
K_{rt} = \frac{\bar w_{rt}}{\operatorname{median}(w_{rt})}.
```

Equation {eq}`eq-lii-w7-kaitz` is a compact Kaitz-style ratio. It reminds students that the same nominal minimum-wage increase can be nearly irrelevant in one labor market and highly binding in another. That difference helps explain why different papers, sectors, and countries can produce different estimates even when the legal rule has the same name.

Treatment intensity also clarifies why evidence on low-wage jobs, rather than on all jobs, is often more informative. If the policy binds only near the lower tail, then a null effect on total county employment may be too aggregated to reveal the relevant adjustment, while a grouped job-distribution or threshold design may detect substantial reshuffling below and just above the new floor [@cengizDubeLindnerZipperer2019].

### What exactly the employment debate is about

The employment debate is not a single disagreement over one elasticity. It is a disagreement over theory, identifying variation, units of observation, time horizon, and which employment margin counts as the relevant one.

`@cardKrueger1994` changed the debate by treating fast-food employment in New Jersey and Pennsylvania as an empirical design problem rather than a calibration exercise. The identifying variation is a state policy change. The unit of observation is the fast-food establishment. The observed margin is sector employment. The key unobserved object is what would have happened in treated stores absent the policy change. Their result was provocative because it challenged the default view that a binding wage floor must reduce employment in a low-wage sector.

`@neumarkWascher2007` pushed back by emphasizing broader panel evidence and the fragility of some case-study results. The identifying variation is mostly state-by-time minimum-wage changes across panels. The unit of observation is typically the state-year or subgroup-state-year cell. The observed margin is employment or employment rates for low-skill groups. The key unobserved object is differential trends across treated and comparison locations. Their critique mattered because it shifted the debate toward whether local shocks, policy timing, and composition differences are adequately controlled.

`@dubeLesterReich2010` reframed the issue with contiguous-border designs. The identifying variation is minimum-wage changes across state borders within local labor markets. The unit of observation is the county-pair by period panel, often focused on restaurants. The observed margin is employment and earnings in a low-wage sector. The key unobserved object is whether bordering counties provide a sufficiently credible local counterfactual. This design narrowed the debate from "treated states versus all other states" to "treated local labor markets versus adjacent comparison markets."

`@cengizDubeLindnerZipperer2019` then changed the outcome object itself. The identifying variation is state and federal minimum-wage changes over time. The unit of observation is a state-by-wage-bin panel built from administrative job counts. The observed margin is jobs below, at, and above the new floor rather than total employment alone. The key unobserved object is how much of the observed reshuffling reflects genuine employment effects versus reclassification, spillovers, or broader equilibrium change. This is why the paper matters pedagogically: it asks whether low-wage jobs disappear and where they reappear in the wage distribution.

```{include} assets/tables/07-employment-debate-map.md
```

Table {numref}`tbl:mw-debate-map` is useful because it states the debate in terms of data and observed margins rather than slogans. The central lesson is that "no employment effect" and "employment loss on some margins" are not logical opposites. A policy can leave headcount roughly stable while reducing hours, raising worker retention, changing hiring standards, shifting jobs above the threshold, or altering firm exit and entry.

```{figure} assets/figures/07-employment-debate-landscape.png
:name: fig-lii-w7-debate-landscape
The employment debate is about design, population, horizon, and the outcome margin. Different papers can disagree because they observe different slices of the same adjustment process.
```

Figure {numref}`fig-lii-w7-debate-landscape` turns the debate into a design map. It should discipline classroom discussion away from "which side wins?" and toward "what variation is identifying what margin over what horizon?"

### Modern evidence by margin: wages, jobs, hours, turnover, and reallocation

The cleanest area of agreement is on wages. Minimum-wage increases raise pay at the lower tail and compress the wage distribution near the new floor. The identifying variation is statutory wage-floor changes. The unit is usually the worker, establishment, or state-by-wage-bin cell. The observed margin is hourly pay or earnings. The key unobserved object is the counterfactual lower-tail wage path without the policy. On this margin, the literature is much more settled than on employment [@cengizDubeLindnerZipperer2019; @dubeLindner2024].

Low-wage job counts are the next core object. `@cengizDubeLindnerZipperer2019` shows why grouped wage-bin panels are helpful: they ask whether jobs below the new floor disappear and whether jobs just above the floor expand. The observed margin is not total employment alone but the composition of jobs across wage bins. That design helps reconcile strong wage effects with muted total employment effects.

Hours are conceptually distinct from headcount. `@jardimEtAl2022` is valuable in class because the identifying variation is a large city-specific increase, the unit is worker-job or payroll-based local observations, the observed margin includes hours and earnings, and the key unobserved object is whether Seattle would have tracked its synthetic control absent the policy. A discussion of this paper helps students see why a stable headcount can coexist with reduced hours for some low-wage workers.

Turnover, hiring, and separation margins matter because wage floors can alter the cost of vacancy filling and the value of keeping incumbent workers. In a frictional market, higher wages can reduce quits and lower vacancy durations even if the firm becomes more selective in hiring. `@butschek2022` is useful here because the identifying variation is again minimum-wage policy, the observed unit is employer or vacancy-level hiring, the observed margin is hiring standards or worker composition, and the key unobserved object is the quality or productivity distribution of applicants.

Firm reallocation matters because some of the policy response can occur through which firms survive, expand, or contract rather than through one representative establishment changing employment in isolation. This is especially important in settings with substantial firm heterogeneity, weak compliance, or large formal-informal margins. The observed unit may be the firm, plant, or local market. The observed margin may be firm entry, exit, wage upgrading, or reallocation across employers. The key unobserved object is the general-equilibrium counterfactual path of worker-firm matching.

```{figure} assets/figures/07-adjustment-margins-under-wage-floors.png
:name: fig-lii-w7-adjustment-margins
Employers can adjust on many margins under a wage floor. Headcount is only one branch of the response tree.
```

Figure {numref}`fig-lii-w7-adjustment-margins` is the second evidence backbone. It keeps the lecture from collapsing everything into a single employment elasticity and creates a direct bridge back to Week 2 adjustment costs and Week 4 worker flows.

### Global evidence beyond the United States

Global evidence matters because minimum-wage institutions are not uniform. Countries differ in whether the floor is national or regional, hourly or monthly, formal-sector-only or broader, strongly enforced or weakly enforced, and tightly linked or only loosely linked to collective bargaining.

The United States remains the canonical debate setting because of staggered state and local changes, large administrative data resources, and the long-running case-study versus panel dispute. The identifying variation is often local or state policy timing. The observed unit is usually a county, state, firm, or worker panel. The observed margins are wages, low-wage jobs, hours, or prices. The key unobserved object is the untreated local counterfactual under a common macro environment [@dubeLesterReich2010; @cengizDubeLindnerZipperer2019; @dubeZipperer2024].

Europe and Germany matter because they bring different institutional structure. National floors and stronger formal-sector coverage make the lecture less about whether a fast-food employment estimate is precisely zero and more about how wage floors change firm composition, job quality, prices, and reallocation under broader coverage. The same design language still applies: what varies is the reform timing and exposure, the unit is a firm, worker, or region panel, the observed margins include wages, hours, prices, and firm outcomes, and the key unobserved object is the untreated equilibrium path under national reform [@dubeLindner2024].

Brazil and other Latin American or emerging-market settings matter because informality and compliance become first-order objects rather than side comments. `@engbomMoser2022` is especially useful because the identifying variation comes from national minimum-wage changes interacting with differential exposure across workers and firms. The unit is a worker-firm or region panel. The observed margins include wages, earnings inequality, and reallocation. The key unobserved object is how formal and informal opportunities would have evolved without the policy. In these settings, minimum wages can have large distributional effects even when measured formal-sector employment losses are muted.

```{include} assets/tables/07-global-evidence-map.md
```

Table {numref}`tbl:global-mw-map` summarizes what students should learn from the global block. Global evidence is not merely a larger number of estimates. It is evidence under different institutions, different enforcement regimes, and different adjustment margins.

```{figure} assets/figures/07-global-minimum-wage-evidence-map.png
:name: fig-lii-w7-global-map
The global literature broadens the question from local U.S. employment effects to institutional heterogeneity in compliance, formality, reallocation, and distributional incidence.
```

Figure {numref}`fig-lii-w7-global-map` provides a clean classroom map of that heterogeneity. It helps students see why a national monthly floor in a high-informality economy is not the same empirical object as a local hourly floor in a U.S. border-county design.

### Wage law beyond minimum wages

Minimum wages are the natural entry point into wage law because they are simple to state and central to labor economics. But the broader literature asks how legal wage-setting rules change information, compliance, and within-firm wage structures.

Labor-standards enforcement is the closest extension because it asks whether the legal rule is even implemented in practice. `@almeidaCarneiro2012` and `@samaniegoFernandez2024` are useful precisely because the identifying variation comes from inspections, enforcement shocks, or changes in expected penalties. The unit is often the municipality, establishment, or worker. The observed margins are formality, wages, and employment transitions. The key unobserved object is the counterfactual compliance environment absent the enforcement change. These papers are the cleanest way to teach the distinction between legal incidence and observed incidence.

Pay transparency laws target wage-setting through information rather than through a direct floor. `@bakerHalberstamKroftMasMessacar2023` and `@gulyasSeitzSinha2023` ask what happens when workers or applicants learn more about pay schedules. The identifying variation is a disclosure reform. The unit is usually the worker, firm, vacancy, or occupation-region cell. The observed margins are wage gaps, wage compression, bargaining outcomes, or worker sorting. The key unobserved object is how beliefs, outside options, and internal wage policies would have evolved without the information shock.

Equal-pay rules extend the same logic to within-firm wage differentials. `@gentilePassaroKojimaPakzadHurson2026` is a useful course-facing reference because it frames equal-pay rules as restrictions on feasible within-firm wage differences for similar work. The identifying variation is legal reform or rule-induced constraint. The unit is the worker-job or firm-job cell. The observed margins are within-firm pay gaps, sorting, and wage compression. The key unobserved object is the unconstrained wage-setting rule that would otherwise have prevailed.

```{include} assets/tables/07-wage-law-toolkit-map.md
```

Table {numref}`tbl:wage-law-toolkit` keeps this extension section disciplined. The point is not to build a legal survey. The point is to ask what rule changes wage-setting, what margin it targets, what variation identifies it, and how it relates back to the conduct environment developed in Weeks 5 and 6.

```{figure} assets/figures/07-wage-law-toolkit.png
:name: fig-lii-w7-wage-law-toolkit
Wage law can operate through floors, information, equal-pay constraints, or enforcement. Each channel targets a different friction in wage-setting.
```

Figure {numref}`fig-lii-w7-wage-law-toolkit` broadens the lecture without losing focus. It shows that minimum wages sit inside a larger family of pay-setting rules rather than standing alone.

### Data and empirical designs: what modern papers identify

The first design bucket is the case study or contiguous-border design. What varies is local policy change at a border or in a narrow comparison setting. The unit is usually the establishment, county, or county pair. The observed margins are sector wages and employment. The key limitation is external validity and the possibility that local controls are still imperfect [@cardKrueger1994; @dubeLesterReich2010].

The second bucket is the national panel or stacked event-study design:

```{math}
:label: eq-lii-w7-event-study
Y_{rt} = \sum_{\ell \neq -1} \beta_\ell \mathbf{1}\{t-T_r=\ell\} + \alpha_r + \gamma_t + \varepsilon_{rt}.
```

Equation {eq}`eq-lii-w7-event-study` is the compact reduced-form object students should carry into applied work. What varies is treatment timing across regions. The unit is the region-time or subgroup-region-time cell. The observed margin could be wages, employment, hours, or prices. The key limitation is whether untreated potential outcomes satisfy the necessary parallel-trends or no-differential-pretrends assumptions over the relevant horizon [@dubeZipperer2024].

The third bucket is the threshold or wage-distribution design. What varies is the binding floor relative to the pre-policy wage distribution. The unit is the wage-bin by state-time cell. The observed margin is jobs below and around the threshold. The key limitation is interpreting bin reshuffling when workers, jobs, and reporting can all change [@cengizDubeLindnerZipperer2019].

The fourth bucket is synthetic-control or city-specific reform analysis. What varies is a large discrete local policy shift. The unit is a city, county, or treated labor market over time. The observed margin often includes hours and earnings as well as headcount. The key limitation is whether the synthetic counterfactual truly captures the treated area's untreated path [@jardimEtAl2022].

The fifth bucket is national reform with exposure-based identification. What varies is pre-reform exposure to the floor or differential bite across workers, firms, or regions. The unit is a worker, firm, or region panel. The observed margins include wages, inequality, reallocation, and informality. The key limitation is that exposure is rarely random and can be correlated with other structural differences [@engbomMoser2022].

The sixth bucket is enforcement and disclosure designs. What varies is inspection intensity, penalty risk, transparency mandates, or equal-pay rules. The unit is often the establishment, municipality, firm, or worker-job cell. The observed margins are compliance, wage compression, and within-firm inequality. The key limitation is that the law often changes both behavior and measurement of behavior at the same time [@almeidaCarneiro2012; @bakerHalberstamKroftMasMessacar2023; @gulyasSeitzSinha2023].

### Compliance, legal incidence, and observed incidence

The wage-law block only works if compliance is explicit:

```{math}
:label: eq-lii-w7-compliance
w_{it}^{obs} = (1-\theta_{it}) w_{it}^{rule} + \theta_{it} w_{it}^{noncomp}.
```

Equation {eq}`eq-lii-w7-compliance` is a compact reminder that the legal rule need not map one-for-one into observed wages. The parameter {math}`\theta_{it}` captures the extent to which noncompliance, evasion, or underenforcement keeps observed pay away from the statutory target. This matters especially in high-informality settings, but it is not irrelevant in rich economies. It is the cleanest way to distinguish legal incidence from observed incidence.

### Frontier extension block: unresolved questions and research opportunities

The optional ninety-minute extension block should ask what remains unsettled after the field's move away from the old "does it kill jobs?" framing.

First, own-wage elasticities and minimum-wage incidence remain closely linked. A market with low own-wage elasticity to the firm is precisely a market where minimum-wage predictions should differ most sharply from the competitive benchmark, but empirical work still struggles to line up reduced-form minimum-wage estimates with direct monopsony measures [@manning2021monopsonyreview; @dubeLindner2024].

Second, spillovers above the minimum remain important. Wage floors can compress not only jobs exactly at the threshold but also nearby pay scales, which affects inequality, internal wage ladders, and perhaps worker morale. That makes the policy partly about wage structure, not just about one point in the lower tail [@cengizDubeLindnerZipperer2019; @engbomMoser2022].

Third, hiring standards, automation, and quality upgrading remain active margins. If employers respond by raising required experience, upgrading capital, or changing customer service models, then low headcount losses could coexist with meaningful composition changes. This is one reason the field increasingly tracks hiring, vacancies, and job content alongside employment stocks [@butschek2022].

Fourth, local versus national reforms remain difficult to compare. Large city-specific hikes, border-county designs, and national reforms each identify different policy objects. Students should leave the extension block understanding that one paper's estimate may not transport cleanly to another institutional scale.

Fifth, compliance and worker sorting remain an underdeveloped connection point between the minimum-wage literature and the broader wage-law literature. Enforcement can change not only observed pay but also which firms attract which workers, whether formality rises, and whether legal protections become credible in practice [@almeidaCarneiro2012; @samaniegoFernandez2024].

## Research Lab

The Week 7 lab is built around `Reproduce -> Diagnose -> Transfer`.

The reproduction anchor is `@cengizDubeLindnerZipperer2019`. Students work with a bounded synthetic grouped wage-bin panel to track what happens to jobs below and just above a new minimum wage. The key lesson is that the employment object is low-wage jobs around the threshold, not total state employment.

The diagnose anchor is `@dubeLesterReich2010`. Students then compare that threshold-based job-distribution object to a contiguous-border design where the observed unit is a county pair and the outcome is restaurant employment and earnings. The point is to make the identification challenge explicit rather than rhetorical.

The optional extension anchor is `@engbomMoser2022`. Students are asked how they would transfer the same design logic to a national reform setting with heterogeneous bite, firm reallocation, and informality margins. The local handout lives at [labs/07-minimum-wages-and-wage-regulations/lab.md](labs/07-minimum-wages-and-wage-regulations/lab.md).

## Methods Box

Week 7 only works if ten distinctions stay visible throughout the lecture.

1. Wage effects are not employment effects.
2. Headcount employment is not hours, turnover, hiring, or reallocation.
3. Competitive predictions differ from monopsony or frictional predictions because the conduct environment differs.
4. Case studies and border designs answer different questions than national panel or stacked event-study designs.
5. Nominal minimum-wage changes are not the same as treatment-intensity or bite measures.
6. Job-distribution designs target jobs below and around the threshold, not total employment in the abstract.
7. Legal incidence can differ from observed incidence when compliance is incomplete.
8. Minimum-wage evidence is not the same as evidence on pay transparency, equal-pay rules, or labor-standards enforcement, even when all belong to wage law.
9. Every empirical claim should name the identifying variation, unit of observation, observed margin, and key unobserved object.
10. Different papers can disagree even under the same policy because they observe different populations, horizons, and margins.

## Reading ladder

### Required / field core

- `@dubeLindner2024` for the modern synthesis of minimum-wage theory, evidence, and policy interpretation.
- `@cengizDubeLindnerZipperer2019` for threshold-based low-wage job counts and the job-distribution approach.
- `@dubeLesterReich2010` for the contiguous-border design and the logic of local comparison markets.
- `@engbomMoser2022` for a global, distributional, and reallocation-oriented extension beyond the United States.

### Strong complements

- `@cardKrueger1994` for the fast-food case study that reorganized the debate.
- `@neumarkWascher2007` for the critique and broader panel perspective.
- `@jardimEtAl2022` for a large local increase with explicit hours and earnings margins.
- `@dubeZipperer2024` for dynamic design interpretation and quantitative synthesis.
- `@dube2019familyincome` for the distributional and household-incidence perspective.

### Wage-law extension

- `@almeidaCarneiro2012` for enforcement, formality, and compliance.
- `@samaniegoFernandez2024` for modern evidence on the cost of informal employment and labor-standards enforcement.
- `@bakerHalberstamKroftMasMessacar2023` and `@gulyasSeitzSinha2023` for pay transparency and information-based wage regulation.
- `@gentilePassaroKojimaPakzadHurson2026` for equal-pay constraints and within-firm wage structure.
- `@butschek2022` for hiring standards as a nonemployment margin under wage floors.

## Exercises / discussion prompts

1. Use Equations {eq}`eq-lii-w7-competitive` and {eq}`eq-lii-w7-monopsony` to explain why the same binding wage floor can imply different employment responses under different market structures.
2. Why is Equation {eq}`eq-lii-w7-kaitz` often more informative than the raw nominal increase in the minimum wage?
3. In `@cardKrueger1994`, what varies, what unit is observed, what margin is observed, and what key object remains unobserved?
4. In `@dubeLesterReich2010`, why are contiguous-border counties a more credible comparison group than broad state panels in some settings?
5. In `@cengizDubeLindnerZipperer2019`, is the main employment object total jobs, hours, or jobs below a threshold? Why does that distinction matter?
6. How can a paper find little change in headcount employment but meaningful changes in hours, hiring, or worker turnover without contradiction?
7. Use Table {numref}`tbl:global-mw-map` to explain why evidence from Brazil or another high-informality setting cannot be interpreted as a simple clone of the U.S. case.
8. Why does Equation {eq}`eq-lii-w7-compliance` matter for both minimum wages and broader wage-law literatures?
9. Compare evidence on minimum wages with evidence on pay transparency or equal-pay rules. Which labor-market margin is each policy trying to move most directly?
10. Propose one transfer design using a small public or synthetic border panel, grouped wage-bin panel, or cross-region policy panel. Name the observed unit, observed margin, identifying variation, and the key unobserved object.

## Reproducibility or code lab note

The Week 7 code lab is deliberately bounded and local. The reproduction step uses a synthetic grouped wage-bin panel inspired by `@cengizDubeLindnerZipperer2019` so students can measure wage gains, disappearing sub-minimum jobs, and reappearing jobs just above the new floor. The diagnose step compares that object to a synthetic contiguous-border county design in the spirit of `@dubeLesterReich2010`, making students state plainly whether they are observing headcount employment, hours, or jobs below a threshold and what the main identification challenge is in each case. The optional extension asks how the same logic transfers to a national high-bite setting anchored to `@engbomMoser2022`. The bounded path runs locally without confidential microdata; the local handout lives at [labs/07-minimum-wages-and-wage-regulations/lab.md](labs/07-minimum-wages-and-wage-regulations/lab.md).

## Slide companion note

The slide deck at [slides/week7/07-minimum-wages-and-wage-regulations.tex](slides/week7/07-minimum-wages-and-wage-regulations.tex) should stay tighter than the chapter. It should cover the central question and course repositioning, the Week 6 to Week 7 bridge, competitive versus monopsony predictions under a wage floor, what exactly the employment debate is about, modern evidence on wages, jobs, hours, turnover, and reallocation, global evidence across the United States, Europe/Germany, and Latin America or emerging markets, wage law beyond minimum wages, empirical designs and what they identify, a frontier extension on own-wage elasticities, compliance, and new data, and the bridge to Week 8 unions and worker voice.
