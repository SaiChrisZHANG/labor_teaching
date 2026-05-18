# Social Norms, Bargaining, And Institutions Shaping Gendered Work

Week 5 asks why gendered work patterns can persist when wages change, education rises, and formal legal barriers weaken. The central question is how social norms, bargaining power, and formal and informal institutions shape labor-force participation, hours, specialization, education and career investment, job search, commuting, competition, authority, and job quality.

The discipline of the week is to treat norms as mechanisms, not as residual explanations. A norm can enter as a preference or identity cost, a belief about sanctions, a coordination device, a change in bargaining power, or a rule embedded in a formal institution. Those channels have different empirical signatures. A claim about social acceptability is not the same as a claim about prices, legal constraint, selection, or household bargaining.

:::{admonition} Core points
:class: important

- A **formal institution** is a written or enforceable rule: law, property right, contract, workplace policy, leave rule, mobility restriction, pay rule, or legal protection.
- An **informal institution** is a social rule or expectation: breadwinning, caregiving, acceptable jobs, mobility, self-promotion, authority, competition, or work-family conduct.
- Norms become labor mechanisms when they change participation, hours, search, commuting, specialization, bargaining, promotion, retention, authority, or job quality.
- Bargaining and threat points are channels through which norms matter: social sanctions, control of resources, and legal rights can change the credible outside option.
- The same norm can operate through preferences, beliefs, coordination, bargaining, and formal rules, so empirical work must name both the identifying variation and the labor margin observed.
- Students should separate norms from prices, norms from pure legal constraints, norms from selection, bargaining channels from pure preferences, and formal institutions from informal ones.

:::

## Learning Objectives

By the end of Week 5, students should be able to:

1. distinguish formal institutions from informal institutions and explain how the two interact;
2. classify gender norms as preference or identity shifters, sanction beliefs, coordination devices, institutional rules, or bargaining modifiers;
3. write a compact bargaining object in which a gender norm enters utility, the feasible set, or the threat point;
4. connect norm mechanisms to labor margins including participation, hours, specialization, education, job search, commuting, competition, authority, and career investment;
5. compare migrant or ancestry designs, norm-misperception interventions, household bargaining designs, historical-origin designs, labor-market experiments, commuting revealed-preference designs, and cross-country legal-institution evidence;
6. evaluate papers by naming the identifying variation, the observed labor margin, and the mechanism claim.

## Opening Orientation

This module orients the economic question, the labor-market object, and the empirical design issues before the layered sections begin.

## Bridge

Week 2 put paid work inside household allocation. Care responsibilities, fertility timing, child penalties, and specialization are not only responses to wages and childcare technology. They can also reflect caregiving norms, male-breadwinner expectations, control over resources, and bargaining power within households. Lundberg and Pollak's bargaining framework is a useful reminder that allocation depends on distributional rules and threat points, not only on a unitary household preference [@lundbergPollak1996bargainingDistributionMarriage].

Week 3 studied education, skills, aspirations, and occupational sorting. Anticipated marriage-market penalties, beliefs about what partners or families consider acceptable, and early expectations about work-family conflict can shape investment before workers enter full-time careers. Acting-wife behavior among elite MBA students and newer evidence on beliefs about marriage-market returns to education show that labor-market investments can respond to social incentives before marriage or childbirth occurs [@bursztynFujiwaraPallais2017actingWife; @andrewCattanCostaDiasFarquharsonKraftKrutikova2025revealedBeliefsMarriageMarket].

Week 4 moved inside firms. Norms matter there because organizations reward self-promotion, competition, long hours, mobility, negotiation, social access, and authority. Competitive job-entry experiments, professional-services career evidence, and commuting-choice evidence show that firm and job design can amplify gendered social expectations [@floryLeibbrandtList2015competitiveWorkplaces; @bertrandGoldinKatz2010dynamicsGenderGapProfessionals; @leBarbanchonRathelotRoulet2021commuteWageTradeoff].

Week 6 will turn to gendered policy incidence. Childcare, leave, taxation, quotas, transparency, equal-pay rules, and protection policies do not enter a blank labor market. They interact with the norms, bargaining channels, and institutional constraints developed here.

## Field Core

### Formal And Informal Institutions

An institution is a rule of the game that structures behavior. For this week, use a sharp distinction:

**Formal institutions** are codified rules with legal, contractual, administrative, or organizational enforcement. Examples include property rights, divorce law, inheritance law, access to bank accounts, tax and transfer rules, parental leave, childcare policy, anti-discrimination law, mobility restrictions, workplace pay systems, promotion procedures, and reporting rules.

**Informal institutions** are social rules sustained by expectations, reputation, sanctions, identity, or coordination. Examples include beliefs about whether married women should work, whether mothers should prioritize care, whether women should commute far for jobs, whether some occupations are appropriate, whether women should compete or self-promote, and whether female authority is legitimate.

The interaction is the interesting part. Formal institutions can codify informal norms, as when legal restrictions make male authority over property or mobility enforceable. Formal institutions can also relax informal norms by changing feasibility, information, or bargaining power. A direct-deposit rule, childcare subsidy, pay-transparency requirement, or enforceable right may change the payoff to violating a norm even if private beliefs move slowly.

The empirical problem is to distinguish five claims:

1. a **price** claim: wages, childcare costs, taxes, or commuting costs changed the relative return to work;
2. a **legal constraint** claim: formal rules directly permit or prohibit behavior;
3. a **selection** claim: workers with different preferences or constraints sort into different choices;
4. a **norm** claim: social expectations or beliefs change payoffs, feasibility, or coordination;
5. a **bargaining** claim: resource control, threat points, or distributional rules change the household or workplace outcome.

```{include} assets/tables/05-norms-and-methods-taxonomy.md
```

### A Compact Bargaining Framework

Consider a household choosing the market hours of a woman, {math}`h_w`, the market hours of a man, {math}`h_m`, and home production, {math}`q`. Let wages be {math}`w_w` and {math}`w_m`. A reduced household surplus can be written as:

```{math}
:label: eq-week5-household-surplus
S(h_w,h_m,q)
=
U_w(c,\ell_w,q)
+
U_m(c,\ell_m,q)
-
\kappa N(h_w,h_m,q;g)
-
C(h_w,h_m,q),
```

where consumption is {math}`c=w_w h_w+w_m h_m+y`, leisure is {math}`\ell_j=T-h_j-t_j`, {math}`C(\cdot)` captures time and job costs, and {math}`N(\cdot;g)` is a norm-violation term under gendered rule {math}`g`. The parameter {math}`\kappa` indexes the salience or expected cost of violating the norm.

This expression can represent several mechanisms. If {math}`N` rises when a wife earns more than her husband, the norm acts like an identity or social-approval cost, as in evidence on relative income and household behavior [@bertrandKamenicaPan2015genderIdentityRelativeIncome]. If {math}`N` rises when a mother works long hours, it changes specialization and career continuity. If {math}`N` rises when a woman commutes far or takes a mixed-gender job, it changes the feasible job set even when the wage is attractive.

Now let the household allocation be determined by bargaining:

```{math}
:label: eq-week5-bargaining-object
\max_{h_w,h_m,q}
\left[V_w(h_w,h_m,q)-T_w(g,F)\right]^{\theta_w}
\left[V_m(h_w,h_m,q)-T_m(g,F)\right]^{\theta_m},
```

where {math}`T_j(g,F)` is person {math}`j`'s threat point and {math}`F` is the formal institutional environment. Gender norms can lower {math}`T_w` by making work socially costly, limiting mobility, weakening control over income, or making exit from marriage less credible. Formal institutions can raise {math}`T_w` by strengthening legal rights, access to accounts, ownership, employment protections, or transfers. The bargaining weight {math}`\theta_w` can also depend on earnings, assets, information, and social support.

The key gender margin is that a wage increase for women need not translate one-for-one into more labor supply or career investment. If the norm penalty {math}`\kappa N` is high, if the threat point remains weak, or if earnings are not controlled by the worker, the response can be muted. Conversely, a policy or intervention that changes control of income or beliefs about acceptability can raise work even with little wage change [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount; @bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms].

```{include} assets/tables/05-bargaining-and-institutions-map.md
```

### Norms As Preferences Or Identity Shifters

The first mechanism is internal: violating a gender role changes utility, self-image, or household identity. Bertrand, Kamenica, and Pan study the distribution of relative income within married couples and connect the male-breadwinner norm to labor supply, earnings, marriage stability, and home production [@bertrandKamenicaPan2015genderIdentityRelativeIncome]. The observed labor margins are earnings shares, labor supply, and household specialization. The identification challenge is to separate a norm-driven discontinuity from sorting into marriage, wage opportunities, and unobserved preferences.

Goldin's grand-gender-convergence framework is useful here because it emphasizes job structure and the price of temporal flexibility [@goldin2014grandGenderConvergence]. Overwork norms and nonlinear returns to hours are not only prices. They are also organizational expectations about availability and commitment. When those expectations collide with caregiving norms, a woman may face a labor-market penalty even in a high-wage occupation.

The method lesson is caution. A preference interpretation requires more than observing that women choose fewer hours or avoid some jobs. The researcher must ask whether the same pattern could arise from childcare prices, commuting costs, discrimination, safety, expectations about future family constraints, or selection into households and occupations.

### Norms As Beliefs About Sanctions Or Acceptability

The second mechanism is social belief: people may privately support women's employment but believe others disapprove. Bursztyn, Gonzalez, and Yanagizawa-Drott study misperceived norms about women working outside the home in Saudi Arabia [@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]. The identifying variation comes from an information intervention that reveals local support among peers. The observed labor margin is willingness to sign up for a job-matching service and subsequent work-related behavior. The paper identifies a belief-about-acceptability channel, not a general wage effect.

Bernhardt, Field, Pande, Rigol, Schaner, and Troyer Moore connect male social status to women's work in India [@bernhardtFieldPandeRigolSchanerTroyerMoore2018maleSocialStatus]. The labor margin is women's work and the mechanism is local status and reputational cost. Again, the empirical object is not simply "culture." It is a claim that perceived sanctions and status concerns change whether market work is acceptable.

Jayachandran synthesizes this developing-country evidence by treating social norms as barriers to employment rather than as a vague residual [@jayachandran2021socialNormsBarrierEmployment]. For labor economists, the useful move is to ask where the norm enters: it may raise the fixed cost of work, restrict acceptable job types, increase the reputational cost of mixed-gender workplaces, lower mobility, or weaken bargaining over care.

### Norms As Coordination Devices

The third mechanism is coordination. A gendered equilibrium can persist even when many individuals privately prefer a different arrangement. Marriage markets are central because workers invest before they know which household they will form and which social expectations will bind.

Bursztyn, Fujiwara, and Pallais show that single women in an elite MBA program report lower career ambitions in a public setting when their answers may be observed by classmates, consistent with marriage-market incentives [@bursztynFujiwaraPallais2017actingWife]. The identifying variation is the public versus private elicitation of preferences and expected labor-market behavior. The observed margins are reported desired compensation, travel, hours, and leadership ambition. The paper speaks to labor-market investment and early career positioning, not to realized lifetime wages by itself.

Andrew, Cattan, Costa Dias, Farquharson, Kraftman, and Krutikova study revealed beliefs and marriage-market returns to education [@andrewCattanCostaDiasFarquharsonKraftKrutikova2025revealedBeliefsMarriageMarket]. The mechanism is anticipatory: education choices can reflect beliefs about future household formation and partner-market returns. This bridges Week 3 directly into Week 5. A student's field choice or labor-market ambition can be shaped by expected social equilibrium rather than by current wages alone.

Coordination also matters in local labor markets. If many employers expect women to reject long commutes, if many families expect daughters-in-law to restrict mobility, or if workers expect social sanctions for certain jobs, the market can settle into a low-mobility equilibrium. The result looks like preference heterogeneity in cross-section, but the mechanism may be common beliefs and expectations.

### Norms Embedded In Formal Institutions

Formal institutions and norms are not rival explanations. Hyland, Djankov, and Goldberg show that gendered laws are associated with women's workforce outcomes across countries [@hylandDjankovGoldberg2020genderedLawsWorkforce]. The identifying variation is cross-country legal-institution variation over time. The observed margin is workforce participation and related economic outcomes. The paper is valuable because it makes formal legal rights measurable, while also forcing the question of enforcement and social credibility.

Field, Pande, Rigol, Schaner, and Troyer Moore study a formal change in financial control: strengthening women's control over bank accounts and direct wage payments [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount]. The observed margins include labor supply and gender norms. The identifying variation comes from account and payment design. The mechanism is not only a price change. Formal financial access can shift bargaining, control over earnings, and social perceptions of work.

Legal and organizational rules can also embed norms inside firms. Leave design can reinforce maternal caregiving if fathers face stigma or weak eligibility. Pay-setting can reward negotiation and self-promotion when those behaviors carry different social costs. Promotion systems can reward uninterrupted availability when household norms allocate care unevenly. Formal equality in text is therefore not enough; the rule must be read together with the informal environment.

### Evidence Across Labor-Market Margins

Norms and institutions show up across the labor market, not only in participation. Fernandez and Fogli use second-generation evidence to study beliefs, work, and fertility [@fernandezFogli2009beliefsWorkFertility]. The identifying variation is ancestry-linked variation among women living in a common destination-country environment. The observed margins are work and fertility. Fernandez studies the evolution of female labor-force participation over a century, emphasizing cultural transmission and changing beliefs [@fernandez2013evolutionFemaleLaborForceParticipation]. Alesina, Giuliano, and Nunn use historical plough agriculture as a source of variation in gender-role origins [@alesinaGiulianoNunn2013originsGenderRoles]. These designs are useful for long-run persistence, but they are less direct about short-run sanctions or household bargaining.

Job-entry and competition evidence speaks to workplace norms and market design. Flory, Leibbrandt, and List use a natural field experiment on job-entry decisions to show how competitive compensation affects applicant pools by gender [@floryLeibbrandtList2015competitiveWorkplaces]. The identifying variation is the compensation or competition structure in job advertisements. The observed margin is application behavior, not downstream promotion. Bertrand, Goldin, and Katz study young professionals and show how hours, career interruptions, and job structure generate gender gaps in high-skill careers [@bertrandGoldinKatz2010dynamicsGenderGapProfessionals]. The margin is career dynamics in a professional labor market where norms about hours and availability interact with household timing.

Search and commuting evidence isolates a different margin. Le Barbanchon, Rathelot, and Roulet study gender differences in job search and the wage-commute tradeoff [@leBarbanchonRathelotRoulet2021commuteWageTradeoff]. The identifying variation comes from job-search and commuting-choice data. The observed margin is the revealed tradeoff between commute and wage. This evidence helps students separate a mobility norm or household constraint from a pure wage preference.

```{include} assets/tables/05-margins-and-evidence-map.md
```

## Research Lab

The Week 5 lab is organized as **Reproduce -> Diagnose -> Transfer**. The goal is to teach students how to investigate norms without treating them as unobserved magic.

**Reproduce.** The primary anchor is Bursztyn, Gonzalez, and Yanagizawa-Drott on misperceived social norms and women's work outside the home [@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]. Students use deterministic synthetic data to reproduce an information-intervention exercise. The observed margins are perceived support, willingness to sign up for job matching, and follow-up employment-related behavior. The identifying variation is simulated random exposure to information about peer support.

**Diagnose.** Students classify each output as a belief, sanction, bargaining, search, or selection object. They must state why the design speaks to perceived acceptability and job search rather than to wages or legal rights.

**Transfer.** The challenge anchor is Bertrand, Kamenica, and Pan on gender identity and relative income within households [@bertrandKamenicaPan2015genderIdentityRelativeIncome]. Students transfer the same discipline to a synthetic relative-income threshold exercise. The observed margins are wife-earnings share, labor supply, and home production. The design memo asks whether a discontinuity near the 50 percent earnings-share point is more consistent with identity, selection, bargaining, or measurement.

**Optional extension.** Students can write a design memo for Field et al. on financial control and labor supply [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount] or Le Barbanchon, Rathelot, and Roulet on commuting and wages [@leBarbanchonRathelotRoulet2021commuteWageTradeoff]. The bounded lab does not estimate those extensions; it asks students to name the treatment, comparison group, labor margin, and mechanism.

Open research questions for the lab:

1. When does an information treatment change beliefs, and when does it change perceived sanction costs?
2. What data would separate private support for women's work from beliefs about community approval?
3. How can a researcher distinguish a breadwinner norm from selection into marriages with different earnings potential?
4. What household data are needed to separate bargaining power from pure preferences?
5. Which labor margins would show that a formal institution relaxed an informal norm?

## Methods Box

:::{admonition} Methods Box: Identify The Norm Channel And The Labor Margin
:class: note

**Migrant, second-generation, and ancestry designs.** These designs compare people exposed to a common destination labor market but linked to different origin-country norms. They are strong for cultural transmission and persistence, as in beliefs, work, fertility, and gender-role origins [@fernandezFogli2009beliefsWorkFertility; @alesinaGiulianoNunn2013originsGenderRoles]. They are weaker for identifying the immediate sanction, bargaining, or workplace mechanism unless linked to specific margins.

**Historical-origin designs.** Historical production systems or institutions can explain persistent gender roles [@alesinaGiulianoNunn2013originsGenderRoles]. The identifying variation is historical exposure; the observed modern margin might be labor-force participation, beliefs, or family behavior. The interpretation must address migration, institutional persistence, and correlated development.

**Norm-misperception interventions.** These designs randomize information about others' beliefs or support. They are strong for social-belief and acceptability channels when they observe job search or take-up responses [@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms].

**Household and bargaining designs.** These designs shift control of resources, information, or threat points. They speak to bargaining when they observe who controls income, who changes labor supply, and whether norms move with resource control [@lundbergPollak1996bargainingDistributionMarriage; @fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount].

**Labor-market experiments on competition or job entry.** These designs randomize job attributes, compensation rules, or public/private elicitation. They observe applications, stated ambitions, or entry choices, not necessarily long-run promotion [@floryLeibbrandtList2015competitiveWorkplaces; @bursztynFujiwaraPallais2017actingWife].

**Commuting and job-search revealed-preference designs.** These designs observe tradeoffs over wages, commute, mobility, and job acceptance. They help separate acceptable-job or mobility constraints from wage offers [@leBarbanchonRathelotRoulet2021commuteWageTradeoff].

**Cross-country legal-institution evidence.** These designs measure formal rules and relate them to workforce outcomes [@hylandDjankovGoldberg2020genderedLawsWorkforce]. They are strongest when legal changes, enforcement, and social norms can be separated.

:::

## Reading Ladder And References

**Start with the frame.** Goldin gives the broad convergence and job-structure frame [@goldin2014grandGenderConvergence]. Lundberg and Pollak provide the bargaining foundation [@lundbergPollak1996bargainingDistributionMarriage]. Jayachandran is the gateway review for social norms and women's employment in developing countries [@jayachandran2021socialNormsBarrierEmployment].

**Culture, transmission, and long-run norms.** Fernandez and Fogli use second-generation evidence on beliefs, work, and fertility [@fernandezFogli2009beliefsWorkFertility]. Fernandez studies the evolution of female labor-force participation [@fernandez2013evolutionFemaleLaborForceParticipation]. Alesina, Giuliano, and Nunn anchor historical origins of gender roles [@alesinaGiulianoNunn2013originsGenderRoles].

**Household identity, breadwinning, and specialization.** Bertrand, Kamenica, and Pan are the main relative-income and breadwinner-norm reading [@bertrandKamenicaPan2015genderIdentityRelativeIncome]. Use the paper to ask whether the observed margin is identity, bargaining, specialization, or selection.

**Misperceptions, sanctions, and status.** Bursztyn, Gonzalez, and Yanagizawa-Drott are the primary norm-misperception intervention [@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]. Bernhardt et al. connect male social status to women's work [@bernhardtFieldPandeRigolSchanerTroyerMoore2018maleSocialStatus].

**Marriage markets and anticipatory investment.** Bursztyn, Fujiwara, and Pallais show how marriage-market incentives can affect reported labor-market ambitions [@bursztynFujiwaraPallais2017actingWife]. Andrew et al. are the frontier marriage-market belief reading [@andrewCattanCostaDiasFarquharsonKraftKrutikova2025revealedBeliefsMarriageMarket].

**Workplace competition, hours, and mobility.** Flory, Leibbrandt, and List anchor job-entry response to competitive workplaces [@floryLeibbrandtList2015competitiveWorkplaces]. Bertrand, Goldin, and Katz connect professional career dynamics to hours and interruptions [@bertrandGoldinKatz2010dynamicsGenderGapProfessionals]. Le Barbanchon, Rathelot, and Roulet identify the wage-commute tradeoff in job search [@leBarbanchonRathelotRoulet2021commuteWageTradeoff].

**Formal institutions and resource control.** Hyland, Djankov, and Goldberg measure gendered laws as formal labor-market institutions [@hylandDjankovGoldberg2020genderedLawsWorkforce]. Field et al. show how strengthening women's financial control can change labor supply and norms [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount].

```{include} assets/tables/05-frontier-and-reading-map.md
```

## Exercises And Discussion Prompts

1. Use Equation {eq}`eq-week5-household-surplus` to explain how the same wage increase can produce different female labor-supply responses under high and low norm penalties.
2. In Equation {eq}`eq-week5-bargaining-object`, give one example of a formal institution that raises {math}`T_w` and one informal institution that lowers it.
3. Choose one paper from the reading ladder. State the identifying variation, the observed labor margin, and the norm channel it can support.
4. Compare a second-generation design with a norm-misperception intervention. Which one is better for cultural persistence? Which one is better for immediate belief updating?
5. Explain why a commuting gap can reflect wages, safety, mobility norms, household bargaining, or job availability. What data would separate those mechanisms?
6. Design a Week 6 policy study that explicitly allows a policy to change both a formal rule and an informal norm.

## Reproducibility And Code Lab Note

The Week 5 code lab lives at `labs/05-social-norms-bargaining-and-institutions-shaping-gendered-work/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates local synthetic norm-misperception and relative-income data, reproduces the primary job-search exercise, and transfers the diagnostic logic to household identity and specialization. It runs without confidential microdata.

## Slide Companion Note

The Week 5 slide deck lives at `slides/week5/05-social-norms-bargaining-and-institutions-shaping-gendered-work.tex`. The deck is a conceptual map rather than a duplicate of the chapter. It defines the central question, bridges from Weeks 2 through 4, distinguishes formal and informal institutions, introduces the methodological taxonomy, presents the compact bargaining framework, organizes evidence across labor margins, and bridges forward to Week 6 policy incidence.

## Bridge Forward

Week 6 asks which policies move which gendered labor-market margins and who bears incidence. The Week 5 lesson is that policy effects depend on the social and bargaining environment into which the policy enters. Childcare, leave, taxation, quotas, transparency, equal-pay rules, safety, and protection can change prices and formal rules, but their incidence depends on norms about caregiving, breadwinning, mobility, authority, reporting, and control over resources.
