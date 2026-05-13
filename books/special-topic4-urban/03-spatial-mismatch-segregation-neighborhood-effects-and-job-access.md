# Spatial Mismatch, Segregation, Neighborhood Effects, And Job Access

## Learning Objectives

By the end of Week 3, students should be able to:

1. distinguish aggregate local opportunity from unequal access within the same metropolitan labor market;
2. separate spatial mismatch, transit feasibility, address stigma, residential networks, peers, schools, institutions, and safety as distinct labor-market mechanisms;
3. define the counterfactual and relevant geography for a job-access or neighborhood-exposure claim;
4. evaluate mover, policy-shock, school-boundary, audit, and matched employer-employee designs for this topic;
5. explain why credible evidence must separate residence, workplace, school, and neighborhood channels.

## Opening Orientation

Week 1 defined the city as a system of jobs, residences, commuting costs, rents, amenities, and outside options. Week 2 added housing and moving costs as constraints on labor-market adjustment. Week 3 asks why opportunity is unequal even inside the same city.

The core problem is not that some metropolitan areas have more jobs than others. A metro area can have strong labor demand and still deliver weak opportunity to some residents if jobs move away from segregated neighborhoods, transit makes shifts infeasible, employers read addresses as signals, referral networks are concentrated, schools and public goods differ, or local safety changes the feasible search radius. This is why spatial mismatch and neighborhood effects must be treated as candidate mechanisms, not as labels for every race-place gap in employment or earnings.

:::{admonition} Core points
:class: important

- Unequal labor-market access is produced by multiple mechanisms, not just distance to jobs.
- Proximity to jobs is not the same thing as access to jobs.
- Neighborhood effects and residential sorting must be separated before interpreting labor gaps.
- Good research designs isolate one mechanism at a time and state the relevant counterfactual.
- Geography, data, and institutional context determine whether a result speaks to access, networks, schools, stigma, exposure, or sorting.

:::

## Bridge

The Week 1 access framework treated reachable jobs as a labor-market object. Week 2 showed that housing costs and moving frictions can prevent workers from reaching better opportunity. Week 3 turns that architecture inward: even when workers live in the same broad metropolitan economy, their feasible labor-market sets can differ sharply.

Four distinctions organize the week. First, **aggregate opportunity** is not **equal opportunity**. Total employment growth in a metro area says little about whether a specific residential group can reach the new jobs. Second, **residence-based disadvantage** is not the same as **workplace-based disadvantage**. A neighborhood may have low resident employment because jobs are far away, because residents face discrimination, because information networks are weak, or because childhood exposure shaped skills long before labor-market entry. Third, **descriptive segregation** is not automatically a causal neighborhood effect. Segregated residence patterns can reflect sorting, constraints, discrimination, historical institutions, or equilibrium prices. Fourth, **current access effects** differ from **long-run exposure effects**. A transit shock may change today's job search set; childhood exposure may change adult earnings through schools, peers, safety, expectations, or institutions.

The labor question is therefore narrow and disciplined: how does residential segregation and neighborhood exposure change job search, hiring, networks, commuting feasibility, human-capital formation, earnings, employment, and mobility?

## Field Core

### Block A. From Aggregate Access To Unequal Access

An aggregate access measure tells us how many jobs exist within a travel-cost radius. An unequal-access framework asks who can actually use those jobs. Let worker {math}`i` face job opportunities indexed by {math}`j`:

```{math}
:label: eq:job-access-week3
A_i = \sum_j v_j \exp\{-\kappa \tau_{ij}\}
```

Here {math}`v_j` captures job opportunities and {math}`\tau_{ij}` is generalized travel cost from worker {math}`i` to job {math}`j`. Travel cost includes time, money, reliability, transfers, schedule compatibility, safety, and sometimes information. The parameter {math}`\kappa` converts travel cost into access decay. The same city can therefore provide high {math}`A_i` for one resident and low {math}`A_i` for another even when both live inside the same metropolitan boundary.

Spatial mismatch begins from this logic: residential segregation can separate workers from employment growth, especially when jobs suburbanize or transit links are weak [@kainHousingSegregationNegro1968; @gobillonSelodZenou2007]. But mismatch is not a complete explanation by itself. Residential segregation may also shape networks, schools, local institutions, safety, employer beliefs, and family constraints. The job of the researcher is to say which channel is being studied.

Residential segregation is therefore a candidate source of unequal access, not the estimand. Neighborhood exposure is also a candidate channel, not a residual. A credible labor paper must translate both into a labor object: employment, callback, vacancy reachability, commute, earnings, job quality, occupational mobility, or intergenerational mobility.

### Block B. Mechanisms Of Unequal Labor-Market Access

The central mechanism taxonomy is the first tool students should carry out of the week.

```{include} assets/tables/03-mechanisms-map.md
```

The mechanisms are related but empirically different.

**Distance to jobs and commuting frictions.** The labor-market object is reachable vacancies or feasible job offers. The counterfactual is a worker with the same skills, networks, and employer treatment but lower generalized travel cost to relevant jobs. Designs use travel-time matrices, transit shocks, job suburbanization, or residence-workplace links.

**Transit and schedule feasibility.** Distance alone is too crude. Two workers at the same distance from jobs can face different access if one has a car, one relies on multi-transfer transit, and the job requires night or weekend shifts. The counterfactual is not simply "closer"; it is "reachable under the actual transport and work-schedule constraint."

**Neighborhood or address discrimination.** The labor-market object is employer response: callback, interview, offer, or wage. The counterfactual is the same applicant with a different address, commute distance, or neighborhood reputation. Audit and correspondence designs are natural because they can randomize the residential signal [@phillipsDoLowWageEmployers2020].

**Referral networks and residential labor-market networks.** The labor-market object is information and trust that connect workers to firms. The counterfactual is the same worker embedded in a different neighbor-coworker network. Matched employer-employee data and neighbor-coworker overlap can separate network access from simple distance [@bayerRossTopa2008; @hellersteinMcInerneyNeumark2011].

**Neighborhood peers and local social capital.** The labor object may be search behavior, aspirations, norms, information, or human-capital investment. The counterfactual is not only a different commute map; it is a different local environment conditional on family background and sorting.

**Schools, public goods, and local institutions.** These channels matter for adult labor outcomes through skill formation, credential access, institutional quality, and expectations. School-boundary and school-admission designs help separate school quality from broader neighborhood exposure [@blackDoBetterSchools1999; @monarrezSchoolAttendance2021].

**Local safety and exposure.** Safety shapes work by changing travel routes, work timing, stress, attendance, and willingness to search beyond a neighborhood. It is related to Week 4, but here it enters as one channel inside unequal access.

One reduced-form decomposition makes the problem visible:

```{math}
:label: eq:mechanism-decomp-week3
Y_i = \beta_A A_i + \beta_N N_i + \beta_P P_i + \beta_S S_i + u_i
```

Here {math}`A_i` is access, {math}`N_i` is networks, {math}`P_i` is neighborhood or peer environment, and {math}`S_i` is schools or local institutions. The equation is not a demand to estimate all terms at once. It is a warning: an omnibus "neighborhood effect" coefficient can bundle different mechanisms with different policy implications.

### Block C. Segregation, Networks, And Job Access

Classic spatial mismatch connects three facts: residential segregation, job decentralization, and barriers to commuting or relocation [@kainHousingSegregationNegro1968]. If employment growth moves toward suburban job centers while Black workers remain disproportionately concentrated in central-city neighborhoods, a simple metro employment count overstates the labor-market opportunity available to those workers. The mechanism is not low local demand alone. It is unequal reachability of demand.

Modern work sharpens that intuition. Gobillon, Selod, and Zenou separate multiple mechanisms that can look like mismatch in reduced form: physical distance, information, search intensity, employer discrimination, and neighborhood effects [@gobillonSelodZenou2007]. Miller's evidence on job suburbanization and Black employment gives students a clean way to see why the geography of work can matter for racial employment gaps even when the jobs remain inside the same broad labor market [@millerWhenWorkMoves2023].

Networks must be taught with spatial mismatch but not collapsed into it. Bayer, Ross, and Topa show that neighbors can matter for employment through informal hiring networks [@bayerRossTopa2008]. Hellerstein, McInerney, and Neumark study the importance of residential labor-market networks by linking neighbors and coworkers [@hellersteinMcInerneyNeumark2011]. These papers teach a different mechanism from commute distance: a nearby job is not accessible if the worker lacks information, referral channels, or employer trust. Conversely, a more distant job may be accessible through a strong network tie.

Proximity to jobs is therefore not the same thing as access to jobs. Access combines travel costs, information, employer response, schedule feasibility, and institutional constraints. A policy that moves jobs closer may not close gaps if employers discriminate or if networks remain segregated. A policy that strengthens referrals may not help if transit makes the job infeasible. A transit policy may raise access without changing childhood exposure. The mechanism determines the policy lever.

### Block D. Neighborhood Exposure And Long-Run Labor Outcomes

Current access is about the job set a worker can reach now. Neighborhood exposure is about how place changes future labor-market opportunity. The main labor outcomes are adult earnings, employment, college attendance, occupational mobility, search scope, and intergenerational mobility.

Mover and exposure designs are central because they use timing. A simple exposure specification is:

```{math}
:label: eq:exposure-week3
Y_i = \alpha + \theta \, \text{Exposure}_{ig} + \lambda_g + \varepsilon_i
```

The term {math}`\text{Exposure}_{ig}` measures exposure of individual {math}`i` to neighborhood {math}`g`, while {math}`\lambda_g` captures place or group structure. Age or duration of exposure can identify causal neighborhood effects when moves are plausibly exogenous or differentially timed. The logic is that children who move earlier should experience more of the destination environment than children who move later, holding the family move itself as comparable.

The Moving to Opportunity evidence shows why timing matters. Chetty, Hendren, and Katz find that moving to lower-poverty neighborhoods as young children improved later outcomes, while effects differed for older children [@chettyHendrenKatz2016]. Chetty and Hendren use national variation in childhood exposure to estimate place effects on intergenerational mobility [@chettyHendren2018]. Chyn studies public housing demolition as a policy-induced relocation that changed children's long-run labor outcomes [@chynPublicHousingDemolition2018]. Bergman and coauthors show that reducing barriers to neighborhood choice can change where families move, which is a frontier example of connecting housing-program design to long-run opportunity [@bergmanChettyDeLucaEtAl2024].

The labor interpretation requires restraint. These papers do not license a generic claim that "neighborhoods matter" in every sense. They say that exposure to particular neighborhood environments, at particular ages, through particular programs or moves, can affect later labor-market outcomes. The mechanism may involve schools, peers, safety, public goods, expectations, health, or networks. The empirical design should make clear which channel is measured directly and which remains bundled.

### Block E. What A Good Empirical Design Looks Like

Design choice follows mechanism. The same reduced-form earnings gap can be generated by commute costs, address stigma, weak referrals, school quality, local safety, or sorting. A credible study must therefore map treatment, geography, data, and outcome to one main channel.

```{include} assets/tables/03-empirical-designs-box.md
```

The required design families have different comparative advantages. **Mover and age-at-move designs** are strongest for long-run exposure and developmental timing. **Cohort exposure designs** are useful when duration and age of exposure vary systematically. **Policy shocks** such as MTO, public housing demolition, transit changes, job suburbanization, or boundary redrawing can create variation in access or exposure, but they often activate multiple channels at once. **School-boundary and admission designs** are useful when the research question is whether measured neighborhood effects are actually school effects. **Audit and correspondence designs** are unusually clean for employer beliefs, address stigma, and commute-distance discrimination, but usually identify an initial hiring margin. **Matched employer-employee and network designs** are essential when the mechanism is referral, coworker overlap, or neighborhood-to-workplace linkage.

```{include} assets/tables/03-good-design-checklist.md
```

Good empirical design in this topic does seven things. It maps the treatment to a single mechanism as cleanly as possible. It defines the relevant geographic scale using commuting, schools, institutions, or employer markets rather than convenience alone. It measures actual job access, exposure, or employer response rather than using tract poverty as an all-purpose proxy. It distinguishes residence, workplace, school, and neighborhood channels. It addresses residential sorting and timing. It discusses equilibrium resorting, displacement, and capitalization when the treatment changes place attractiveness. Finally, it states which labor margin moves: employment, wages, callbacks, commute, job quality, mobility, or long-run earnings.

## Research Lab

The Week 3 lab uses a synthetic teaching path rather than confidential microdata. The workflow is **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is Chetty, Hendren, and Katz on Moving to Opportunity [@chettyHendrenKatz2016]. Students reproduce the chapter's exposure logic with a small deterministic dataset of families who move at different child ages. The exercise computes predicted adult outcomes under differential exposure to destination neighborhood opportunity. The output is not an official replication. It is a way to practice the age-at-move logic and to separate long-run exposure from current job access.

**Diagnose.** Students classify mechanism claims. For each synthetic result, they identify whether the object is access, employment, sorting, school channel, network channel, address stigma, or omnibus neighborhood exposure. The diagnostic questions are: What is treated? What is the counterfactual? Which geography matters? Which labor margin moves? What data would be needed to separate schools from neighborhoods?

**Transfer.** The challenge anchor is Miller on job suburbanization [@millerWhenWorkMoves2023]. Students transfer the framework to a synthetic job-location shock. They compare changes in reachable vacancies with changes in employment and explain why access is not the same as realized employment. The optional frontier prompt uses Bergman and coauthors to ask how reducing barriers to neighborhood choice can change the distribution of exposure before any adult labor outcome is observed [@bergmanChettyDeLucaEtAl2024].

The lab trains five distinctions: access versus employment, neighborhood effects versus sorting, school channels versus neighborhood channels, mover designs versus policy shocks, and mechanism-specific evidence versus omnibus neighborhood claims.

## Methods Box

:::{admonition} Methods Box: Data And Measurement Discipline
:class: note

The practical skill this week is knowing what each data source can and cannot identify. Researchers usually need to combine residence, workplace, school, transportation, and administrative-program data.

```{include} assets/tables/03-data-and-measurement-map.md
```

LEHD, LODES, and QWI are natural for residence-workplace flows, workplace geography, job suburbanization, and access measures. Census, ACS, PUMS, and the Decennial Census are useful for segregation, commuting, earnings, demographics, and residential sorting. Opportunity Atlas and tax-linked mobility data are powerful for childhood exposure and adult outcomes, but they do not directly reveal employer mechanisms. School assignment, school attendance boundary, and admission data are needed when the neighborhood channel may run through schools. GTFS feeds and travel-time matrices help measure generalized access rather than Euclidean distance. Audit and correspondence data identify employer response to randomized address or commute-distance signals. Matched employer-employee data are central for referral networks, coworker geography, and workplace segregation. Administrative relocation, voucher, public housing, or demolition data can create policy-induced moves, but they often bundle many channels.

The rule is simple: choose data that observe the mechanism, not just the neighborhood.

:::

## Reading Ladder And References

**Spatial mismatch foundations.** Start with Kain for the classic claim that housing segregation and metropolitan decentralization can reduce Black employment access, then use Gobillon, Selod, and Zenou to see why mismatch can operate through several channels [@kainHousingSegregationNegro1968; @gobillonSelodZenou2007].

**Segregation and network mechanisms.** Use Bayer, Ross, and Topa and Hellerstein, McInerney, and Neumark to study residential labor-market networks and neighbor-coworker links [@bayerRossTopa2008; @hellersteinMcInerneyNeumark2011]. Add Hellerstein, Kutzbach, and Neumark for the spatial dimension of labor-market networks [@hellersteinKutzbachNeumark2014].

**Causal neighborhood exposure.** Use Chetty, Hendren, and Katz, Chetty and Hendren, and Chyn to study age-at-move logic, childhood exposure, and policy-induced relocation [@chettyHendrenKatz2016; @chettyHendren2018; @chynPublicHousingDemolition2018].

**Modern policy-shock and mover designs.** Use Miller for job suburbanization as an access shock and Bergman and coauthors for barriers to neighborhood choice [@millerWhenWorkMoves2023; @bergmanChettyDeLucaEtAl2024].

**Measurement and identification challenges.** Use Graham for the identification problem in neighborhood effects, Phillips for correspondence evidence on commute-distance discrimination, and Black plus Monarrez for school-boundary logic [@graham2016; @phillipsDoLowWageEmployers2020; @blackDoBetterSchools1999; @monarrezSchoolAttendance2021].

## Exercises And Discussion Prompts

1. A city adds 20,000 jobs in a suburban employment center. Name one access mechanism, one network mechanism, and one discrimination mechanism that could determine whether central-city residents benefit.
2. Using Equation {eq}`eq:job-access-week3`, list the data needed to construct {math}`A_i` for transit-dependent workers. Which parts would be missed by Euclidean distance?
3. Choose one row from the mechanisms map. What is the labor-market object, what is the counterfactual, and which empirical design would isolate it most cleanly?
4. A mover design finds that children who move earlier have higher adult earnings. What evidence would help separate school quality, peer exposure, safety, and family sorting?
5. Design a correspondence experiment that varies address or commute distance. What margin does it identify, and what equilibrium margin does it miss?

## Reproducibility And Code Lab Note

The Week 3 code lab lives at `labs/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access/`. It is a bounded synthetic exercise, not an official replication package. The smoke path creates deterministic synthetic data, computes exposure-timing predictions, diagnoses mechanism claims, and transfers the logic to a job-suburbanization access shock. It runs without confidential microdata or external downloads.

## Slide Companion Note

The Week 3 slide deck lives at `slides/week3/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.tex`. The deck is a compact research-design map. It defines unequal access, separates mismatch, networks, stigma, schools, safety, and exposure, reviews the main design families, and bridges to Week 4 on safety, environment, and the feasible set for work.

## Bridge Forward

Week 4 takes one mechanism from this week - local safety and environmental exposure - and studies it directly as a constraint on work timing, commuting, productivity, search radius, and welfare.
