# Worker Voice, Collective Action, and Bargaining Institutions

## Learning Objectives

By the end of Week 4, students should be able to:

1. distinguish union membership, collective bargaining coverage, enterprise bargaining, sectoral bargaining, works councils, codetermination, and strike capacity;
2. explain worker organization as an equilibrium object shaped by demand for representation, organizing costs, employer opposition, certification law, labor-market tightness, and institutional design;
3. analyze how collective institutions change wages, rents, employment, payroll, turnover, governance, information, inequality, and worker welfare;
4. separate direct effects on organized units from spillovers to uncovered workers and firms;
5. evaluate empirical designs by naming whether the design identifies organization formation, wage-setting, employment, governance, spillovers, or political participation.

## Opening Orientation

Week 4 asks how worker organizations and bargaining institutions emerge, what they do once they exist, and how their effects travel beyond organized workplaces. The topic sits near political economy, but the core object is labor economics: collective institutions change wage-setting, rent-sharing, monitoring, retention, workplace governance, inequality, and the credibility of worker claims.

Weeks 2 and 3 studied law, enforcement, informality, and contract enforceability. Week 4 turns to a different institutional response to fragmented individual bargaining. When workers bargain separately, each worker may have limited information, weak threat power, retaliation risk, and little ability to monitor compliance. Collective institutions aggregate worker claims, alter threat points, create representation channels, and sometimes extend bargaining outcomes to workers who are not union members.

:::{admonition} Core points
:class: important

- Collective institutions are labor-market institutions for overcoming fragmented individual bargaining.
- The key objects are not only union membership. They also include organization, bargaining coverage, representation, voice, and strike capacity.
- Worker organization itself is endogenous: it depends on worker demand, organizing costs, employer opposition, legal thresholds, labor-market tightness, and institutional design.
- Collective bargaining can change wages, rents, wage compression, employment, turnover, retention, payroll, and the distribution of surplus.
- Worker voice can operate through governance and information channels, not only through wage bargaining.
- Spillovers to uncovered workers are central for evaluating inequality and welfare.
- Political spillovers matter, but in this course they are downstream from labor-market organization rather than a substitute for the labor question.

:::

## Bridge

Week 3 ended with incomplete contracts and uneven enforceability. If a worker cannot easily claim unpaid benefits, challenge unsafe conditions, or bargain over a wage alone, individual contract status is only part of the problem. Collective action is one institutional response: workers can pool information, coordinate threats, monitor compliance, and bargain over how surplus is divided.

The classic starting point is Freeman and Medoff's distinction between the monopoly face and the voice face of unions [@freemanMedoff1984]. The monopoly face emphasizes wage premia, rent extraction, and possible employment or product-market effects. The voice face emphasizes information, grievance procedures, turnover reduction, worker participation, and governance inside firms. Week 4 treats both faces as institutional mechanisms.

A compact way to keep wages, rents, and governance in the same frame is:

```{math}
:label: eq:collective-surplus-week4
\Delta S
= \Delta W_{workers}
+ \Delta \Pi_{firms}
+ \Delta G_{voice}
+ \Delta E_{spillovers},
```

where {math}`\Delta S` is the change in the surplus and social incidence of a collective institution; {math}`\Delta W_{workers}` is the wage, benefit, risk, and job-quality effect for covered workers; {math}`\Delta \Pi_{firms}` is the change in firm profits, productivity, payroll, investment, and employment; {math}`\Delta G_{voice}` is the governance, information, retention, and representation channel; and {math}`\Delta E_{spillovers}` captures effects on uncovered workers, wage norms, inequality, and downstream political participation. Equation {eq}`eq:collective-surplus-week4` is a teaching map, not an accounting identity. It forces students to ask which margin a paper actually observes.

## Field Core

### Why Worker Voice Institutions Arise

Collective institutions arise because employment relationships are incomplete and workers often face fragmented bargaining. A worker may know that a grievance is common but not know whether other workers will act. A worker may value a safer schedule or a higher wage but fear retaliation if the claim is made alone. A firm may have information about productivity, vacancies, and profits that individual workers cannot verify. A government may write labor rights into law, but enforcement may depend on workers reporting violations or organizations helping them aggregate claims.

The economic problem is therefore not only whether unions raise wages after they exist. It is why workers organize, why some organizations obtain legal recognition, and why some institutional designs cover many workers while others cover only members in organized establishments. Jager, Naidu, and Schoefer frame collective bargaining as a comparative wage-setting institution whose effects depend on bargaining level, coverage, coordination, and the relationship between membership and coverage [@jagerNaiduSchoefer2024].

Collective institutions can solve several labor problems. They can raise workers' bargaining power by changing the firm's cost of disagreement. They can reduce information problems by giving workers a channel to report local knowledge. They can lower turnover by making grievances less likely to become quits. They can standardize wages across workers or firms, reducing wage dispersion. They can also create costs: higher wages may reduce employment in some settings, rigid rules may reduce flexibility, and bargaining power can shift rents without raising total surplus. A serious lecture must keep these tradeoffs visible.

### What Counts As Collective Institutions?

The first distinction is between membership and coverage. **Union membership** measures whether a worker formally joins a union or worker organization. **Collective bargaining coverage** measures whether the worker's wage or conditions are governed by a collective agreement. In enterprise systems, membership and coverage may be closely linked. In sectoral systems with extension rules, coverage can be much larger than membership. That difference is central for comparing the United States with continental Europe and Nordic systems [@jagerNaiduSchoefer2024].

The second distinction is bargaining level. **Enterprise bargaining** occurs at the firm, establishment, or workplace. It is closest to union certification elections and close-election research designs. **Sectoral bargaining** occurs at industry, occupation, region, or national levels. It can coordinate wages across firms, create wage floors for nonmembers, and generate large spillovers. A country can have high union membership with decentralized bargaining, low membership with high coverage, or dual systems where sectoral agreements coexist with firm-level representation.

The third distinction is between bargaining and voice. **Works councils** are representation bodies that often focus on consultation, information, scheduling, training, layoffs, and workplace rules rather than classic wage bargaining. **Codetermination** gives workers representation at the board level and therefore connects worker voice to corporate governance. **Strike threats and collective-action capacity** are not organizations by themselves, but they are the power resources that make bargaining credible. A union contract without credible collective action is different from a union contract backed by strike capacity.

```{include} assets/tables/04-collective-bargaining-concepts-map.md
```

This taxonomy prevents a common mistake. "Unionization" can mean membership, recognition, contract coverage, bargaining power, strike capacity, works-council representation, or board representation. Empirical designs differ because they move different objects.

### How Organizations Form

Worker organization is an equilibrium outcome. Workers demand representation when the expected benefits of collective voice exceed the expected costs of organizing, dues, conflict, and retaliation risk. Benefits may include higher wages, better benefits, grievance protection, scheduling voice, safety, fairness, dignity, and a more credible channel for claims. Demand can be latent even when observed unionization is low, because workers may want representation but fail to organize under high costs or legal barriers.

Organizing costs include recruiting coworkers, building trust, learning legal procedures, paying dues, sustaining campaigns, and coordinating across occupations, shifts, locations, or contractors. These costs rise when work is fissured, turnover is high, workers are geographically dispersed, or employees fear retaliation. Employer opposition changes the cost-benefit calculation by raising perceived risks, using information campaigns, delaying recognition, changing employment conditions, or contesting bargaining units.

Legal thresholds and certification rules determine when latent demand becomes recognized organization. In the United States, certification-election settings make the vote share a central variable: an establishment just above the majority threshold can obtain bargaining rights, while an otherwise similar establishment just below the threshold does not. This institutional setting motivates close-election regression discontinuity designs in DiNardo and Lee and Frandsen [@dinardoLee2004; @frandsen2021]. The design is powerful because it studies the causal effect of winning recognition near the threshold, but it does not identify the effect of unions on all workplaces. It identifies marginal organizing victories in close elections.

Labor-market tightness changes the organizing environment. When outside options are strong, workers may be less afraid to support organization and employers may face higher replacement costs. Tightness can therefore raise union activity by improving worker bargaining positions. It may also reduce demand for formal organization if tight labor markets already produce wage gains. Pezold, Jager, and Nuss are useful here because they treat union activity as responsive to labor-market conditions rather than as fixed institutional background [@pezoldJagerNuss2023].

Institutional design determines whether organization is a repeated workplace campaign or a broader coverage system. Extension rules can apply sectoral agreements to nonmembers. Works-council thresholds can create representation when firms pass size cutoffs. Public-sector rules can encourage or restrict bargaining. Strike law can make collective threats credible or costly. The organizational margin is therefore jointly produced by worker demand, employer strategy, law, labor-market conditions, and representation technology.

```{include} assets/tables/04-organization-formation-and-coverage-map.md
```

### Bargaining, Wages, Rents, And Coverage

The wage effect of collective bargaining depends on the object. A new union at an enterprise may raise wages for covered workers if the union captures rents, standardizes pay, or increases the firm's cost of worker replacement. A sectoral agreement may compress wages across firms even if membership is low. A works council may have limited direct wage bargaining authority but still affect compensation indirectly through information, retention, or interaction with sectoral contracts.

Rent-sharing is the core labor-economics mechanism. If firms earn rents because of product-market power, search frictions, firm-specific capital, or location advantages, worker organization can shift part of those rents to workers. The incidence depends on labor demand elasticity, product-market competition, firm profitability, capital adjustment, and the credibility of strike or bargaining threats. The wage premium is therefore not a sufficient statistic for welfare. Students should ask whether higher pay reflects rent-sharing, productivity gains through voice, compensating changes in employment, or wage compression across the distribution.

DiNardo and Lee use close union certification elections to estimate the impact of new unionization on private-sector employers [@dinardoLee2004]. Their design is most informative about establishments near the recognition threshold and about employer outcomes such as employment, output, survival, and wages where data allow. Frandsen uses matched employer-employee data to examine worker and establishment impacts, moving the evidence closer to payroll, careers, separations, and within-firm incidence [@frandsen2021]. Together, these papers teach a crucial distinction: close-election designs are not generic union-premium estimates. They identify the effect of barely winning new recognition among organizing campaigns that made it to an election.

Coverage changes the interpretation. When bargaining coverage exceeds membership, wages can be affected even for nonmembers. Sectoral bargaining can create wage floors, coordinate wage growth, and compress dispersion across firms. Jager, Naidu, and Schoefer's comparative perspective is essential because the United States enterprise model is only one institutional regime [@jagerNaiduSchoefer2024]. A labor-economics course should compare enterprise bargaining, sectoral coverage, extension rules, and works-council systems as different technologies of wage-setting.

### Voice, Governance, And Representation

Worker voice is not exhausted by wages. The voice channel changes how information and authority move inside the firm. Workers observe production bottlenecks, safety issues, scheduling problems, managerial abuse, training needs, and morale. Individual workers may not reveal this information if they fear retaliation or if management lacks a credible channel for response. Representation can make information transmission safer and more systematic.

Works councils and codetermination make this governance channel explicit. Works councils can provide consultation over work organization, hours, training, layoffs, and workplace rules. Board representation can give workers access to strategic information and a formal voice in firm governance. These institutions may raise productivity if they improve information, trust, retention, and cooperation. They may reduce productivity if they slow decisions or protect inefficient practices. The empirical object is therefore governance, not simply wages.

Harju, Jager, and Schoefer study worker voice beyond classic union wage bargaining [@harjuJagerSchoefer2021]. Jager, Schoefer, and Heining use the German industrial-relations model to highlight how sectoral bargaining, works councils, and codetermination can interact [@jagerSchoeferHeining2022]. The German case is useful pedagogically because it separates multiple institutions that are often collapsed into "unions": industry bargaining can set wages, works councils can govern workplace issues, and board representation can affect corporate decisions.

The voice face also changes turnover and retention. If workers can resolve grievances internally, quit rates may fall. If firms learn about local problems earlier, match quality can improve. If representation increases procedural fairness, workers may accept changes that would otherwise be resisted. These channels are hard to measure, but they are central to the welfare object in equation {eq}`eq:collective-surplus-week4`.

### Spillovers And Inequality

Collective institutions affect workers outside organized units. A nonunion firm may raise wages to deter organizing. A sectoral agreement may set a norm that uncovered firms follow. A union wage premium may change the outside option for workers in nearby firms. Bargaining can compress wage differences within firms, across occupations, and across firms. It can also produce composition effects if firms adjust hiring, outsource tasks, or shift toward capital.

Spillovers make the evaluation of collective institutions fundamentally different from a treatment-on-the-treated exercise. A close-election RD can estimate the effect of winning recognition at the treated establishment, but it does not capture threat effects on nonunion firms, sectoral wage norms, or distributional compression in the broader market. Fortin, Lemieux, and Lloyd are central because they put spillover effects into the distributional analysis of labor-market institutions [@fortinLemieuxLloyd2021].

The inequality channel has at least four parts. First, bargaining can raise wages at the bottom or middle of the covered distribution. Second, wage standardization can compress within-firm wage dispersion. Third, sectoral coverage can compress between-firm wage differences by limiting low-wage competition. Fourth, spillovers can alter uncovered wages through threat effects and norms. These channels can reduce wage inequality even when membership is limited, but the sign and size depend on coverage, enforcement, firm heterogeneity, and product-market adjustment.

### Political Spillovers And Feedback

Political spillovers matter because labor institutions are organizations as well as wage-setting rules. The direction from unions to politics runs through mobilization, turnout, campaign contact, political information, policy advocacy, and party coalitions. Freeman's study of unions and voting provides the classic labor-to-politics question: worker organization can change civic participation by giving workers repeated organizational contact and political information [@freeman2003].

The direction from politics to unions runs through labor law, bargaining rights, right-to-work laws, public-sector bargaining rules, strike law, enforcement, and court doctrine. Feigenbaum, Hertel-Fernandez, and Williamson study political effects of right-to-work laws, which makes the feedback visible: rules that weaken union security can change both labor-market organization and downstream political outcomes [@feigenbaumHertelFernandezWilliamson2018]. Kaplan and Naidu place unions between government and market, emphasizing that unions are economic organizations with political effects and political determinants [@kaplanNaidu2024].

For this course, the political section stays bounded. The labor object remains worker organization. Political participation is a downstream outcome or feedback channel: collective labor institutions can mobilize workers, and political rules can expand or restrict bargaining capacity. The lecture should not become a general theory of parties or democracy.

```{include} assets/tables/04-spillovers-and-political-linkages-map.md
```

### Comparative Regimes

Country variation is not a detail. It changes what "union effect" means. A low-membership, high-coverage country differs from a high-membership, enterprise-bargaining country. A system with works councils but limited wage bargaining differs from a system where unions bargain at the enterprise. A system with codetermination differs from a system where workers have no formal governance rights. Strike law, extension rules, public-sector bargaining, and enforcement capacity shape the same labor institution from different sides.

The comparative map has four regimes that are useful for teaching. First, enterprise-bargaining systems focus bargaining at the firm or establishment and make certification, recognition, and local employer opposition central. Second, sectoral systems set wages and conditions above the firm, making coverage and extension rules central. Third, dual-channel systems combine collective agreements with works councils or codetermination, separating wage-setting from workplace consultation. Fourth, weak-coverage systems may have worker demand for organization but high organizing costs, legal barriers, employer opposition, or informal work arrangements that limit recognized bargaining.

Comparative analysis should not ask which model is universally best. It should ask which margin the institution moves: membership, coverage, wage floors, rent-sharing, firm governance, strike capacity, worker voice, or political feedback. This is why the international perspective in Jager, Naidu, and Schoefer is the Week 4 frame rather than a reading add-on [@jagerNaiduSchoefer2024].

### Empirical Designs And What They Identify

The methods lesson is to match the design to the institutional object.

**Close certification-election regression discontinuity** compares workplaces where union campaigns barely win with workplaces where campaigns barely lose. It is strongest for the causal effect of recognition near the vote threshold on organized units. It can speak to wages, employment, payroll, survival, and employer response, as in DiNardo and Lee and Frandsen [@dinardoLee2004; @frandsen2021]. It does not directly identify broad spillovers, latent demand for unions, or the effect of sectoral bargaining.

**Matched employer-employee event studies** follow workers and firms around organizing, recognition, contract adoption, or representation changes. They are strongest for careers, payroll, separations, turnover, wage trajectories, and firm response. Their challenge is separating treatment from selection into organizing and from broader labor-demand shocks.

**Bargaining-right and right-to-work reforms** identify how legal changes alter organizing capacity, union security, coverage, wages, employment, and political outcomes. They are useful for the politics-to-labor feedback channel, but they often bundle law, employer response, union resources, and worker mobilization.

**Threshold designs for representation institutions** use firm-size cutoffs or legal thresholds for works councils, consultation rights, or board representation. They can identify governance and representation effects when firms near the threshold are comparable. The observed margins may be productivity, wages, separations, training, investment, or workplace practices.

**Distributional decompositions for spillovers** identify how institutions contribute to wage dispersion, including direct effects on covered workers and indirect effects on uncovered workers. They are central for inequality, but they rely on assumptions about counterfactual wage structures and the mapping between institutions and distributional changes.

**Survey and field evidence on organizing demand** identifies worker demand, beliefs, retaliation fears, perceived benefits, and the role of labor-market tightness. This evidence is crucial for organization formation because observed union density is an equilibrium outcome, not a clean measure of demand [@pezoldJagerNuss2023].

```{include} assets/tables/04-identification-and-frontier-map.md
```

### Bridge To Week 5

Week 4 closes the legal and organizational foundation of the course. Weeks 2 and 3 showed how formal rules, enforcement, informality, and contract status shape labor exchange. Week 4 showed how collective institutions aggregate worker power, alter wage-setting, and create voice. Week 5 turns to culture and norms as informal allocation mechanisms: how beliefs about work, family, status, mobility, and acceptable jobs change labor supply, search, care work, migration, and occupational sorting.

## Research Lab

The Week 4 lab is built around **Reproduce -> Diagnose -> Transfer**. It runs locally with deterministic synthetic data and does not require confidential microdata from union elections, matched employer-employee records, or political files. The goal is to train students to diagnose what a collective-institutions design identifies.

**Reproduce.** The primary anchor is DiNardo and Lee [@dinardoLee2004]. Students build a synthetic close-election dataset with union vote share, recognition, wages, employment, payroll, and establishment survival. They reproduce the logic of a close-election design by comparing outcomes near the majority threshold. The target is the design object: the effect of barely winning recognition among organizing campaigns that reached an election.

**Diagnose.** The secondary challenge anchor is Frandsen [@frandsen2021]. Students use a matched worker-establishment teaching file to separate establishment outcomes from worker outcomes: wages, separations, payroll, incumbent workers, new hires, and employment composition. The diagnostic question is whether the evidence speaks to treatment on organized units, organization formation, worker sorting, or firm response.

**Transfer.** Students then classify three extensions. The spillover extension uses Fortin, Lemieux, and Lloyd to compare direct incidence on organized workers with spillovers to uncovered workers [@fortinLemieuxLloyd2021]. The voice and governance extension uses Harju, Jager, and Schoefer to separate wage bargaining from representation and information channels [@harjuJagerSchoefer2021]. The political spillover extension uses Feigenbaum, Hertel-Fernandez, and Williamson to distinguish labor-market effects of institutional change from downstream voting and participation outcomes [@feigenbaumHertelFernandezWilliamson2018].

The bounded transfer choices are:

1. compare direct and spillover incidence in one wage-distribution exercise;
2. reinterpret a close-election design through organization formation rather than only treatment effects;
3. separate labor-market and political margins of the same institutional shock.

The lab lives at `labs/04-worker-voice-collective-action-and-bargaining-institutions/`. The smoke test builds synthetic data, writes close-election summaries, classifies design objects, and produces small CSV and text outputs for seminar discussion.

## Methods Box

Week 4 uses six method families. The practical rule is to name the object before interpreting the result.

Close certification-election RD identifies the effect of recognition at the threshold for campaigns that make it to an election. It is best for wages, employment, payroll, survival, and direct treatment on organized units. It is not a direct estimate of latent demand or national bargaining systems.

Matched employer-employee event studies identify worker careers, payroll, separations, turnover, and firm response around organization or contract events. They are valuable for distinguishing worker-level and establishment-level incidence.

Bargaining-right and right-to-work reforms identify institutional shocks to organizing capacity, union security, coverage, and sometimes political participation. They require attention to pre-trends, state politics, sector composition, and concurrent reforms.

Threshold designs for representation institutions identify effects of works councils, consultation rights, or board representation when legal cutoffs create sharp changes in representation. They are especially useful for governance, information, training, productivity, and retention.

Distributional decompositions identify the contribution of coverage, wage floors, union density, and spillovers to wage inequality. They help move beyond the organized workplace, but they require explicit counterfactual wage assumptions.

Survey and field evidence on organizing demand identifies worker preferences, beliefs, fear, salience, and tightness-related changes in organizing activity. This evidence is essential because observed unionization is the result of demand, costs, employer opposition, and law.

## Reading Ladder And References

**Comparative frame.** Start with Jager, Naidu, and Schoefer for the international perspective on bargaining institutions, membership, coverage, wage structure, and comparison across regimes [@jagerNaiduSchoefer2024].

**Classic theory of unions.** Read Freeman and Medoff for the monopoly and voice faces of unions [@freemanMedoff1984]. Use the distinction to keep wage-setting and governance in the same chapter.

**New unionization evidence.** Read DiNardo and Lee as the close-election RD benchmark [@dinardoLee2004]. Then read Frandsen for matched employer-employee evidence on the worker and establishment margins [@frandsen2021].

**Organization formation.** Read Pezold, Jager, and Nuss to see union activity as responsive to labor-market tightness and organizing conditions [@pezoldJagerNuss2023].

**Voice and governance.** Read Harju, Jager, and Schoefer with Jager, Schoefer, and Heining to separate wage bargaining, works councils, codetermination, information, and governance [@harjuJagerSchoefer2021; @jagerSchoeferHeining2022].

**Spillovers and inequality.** Read Fortin, Lemieux, and Lloyd to understand why uncovered workers and distributional spillovers are central to the evaluation of labor-market institutions [@fortinLemieuxLloyd2021].

**Political feedback.** Read Freeman on unions and voting, Feigenbaum, Hertel-Fernandez, and Williamson on right-to-work laws, and Kaplan and Naidu for the broader political economics of unions [@freeman2003; @feigenbaumHertelFernandezWilliamson2018; @kaplanNaidu2024].

## Exercises And Discussion Prompts

1. Choose a country or sector. State whether the relevant worker-voice object is membership, bargaining coverage, enterprise bargaining, sectoral bargaining, works councils, codetermination, or strike capacity.
2. In a close certification-election design, what population is being compared? What does the design identify, and what does it not identify?
3. Use equation {eq}`eq:collective-surplus-week4` to compare a pure wage-premium interpretation with a voice-and-governance interpretation.
4. Suppose a sectoral agreement is extended to nonmember firms. Predict effects on covered wages, uncovered wages, wage dispersion, employment, and organizing incentives.
5. Design a bounded empirical exercise that separates labor-market effects of a right-to-work law from political participation effects.

## Reproducibility And Code Lab Note

The Week 4 code lab is a synthetic teaching analog. It does not reproduce confidential NLRB, matched employer-employee, or voter-file microdata. Its purpose is to help students practice the Week 4 diagnostic sequence: identify the organization-formation margin, distinguish direct effects from spillovers, separate wage bargaining from governance, and treat political outcomes as downstream extensions of labor institutions.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-worker-voice-collective-action-and-bargaining-institutions.tex`. The deck defines the central question, bridges from Week 3, maps collective institutions, explains how organizations form, separates wages and rents from governance, introduces spillovers and political feedback, isolates empirical designs, and bridges to Week 5.

## Bridge Forward

Week 5 moves from formal collective organization to culture, norms, and labor-market allocation. The transition is natural. Worker voice institutions show how organization can change bargaining power and claims. Norms show how informal beliefs and expectations can change the perceived feasible set before formal organization or legal enforcement ever begins.
