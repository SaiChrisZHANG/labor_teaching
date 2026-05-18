# Identity, Norms, Fairness, and Labor-Market Allocation

## Learning Objectives

By the end of Week 6, students should be able to:

1. define identity, norms, fairness, peer pressure, and firm culture as behavioral labor objects;
2. distinguish micro workplace norms from broader political, legal, and historical institutions;
3. write identity, fairness, peer-pressure, sorting, and culture-transmission objects and map them to labor margins;
4. explain how social comparisons affect effort, morale, quits, cooperation, and pay satisfaction;
5. separate peer learning, peer pressure, social sanctions, team norms, and firm culture;
6. classify evidence as treatment, sorting, transmission, or equilibrium cultural selection;
7. design a bounded empirical diagnosis that names the behavioral object, labor margin, reference group, identifying variation, and interpretation.

## Opening Orientation

Week 6 asks how identity, norms, fairness concerns, peer pressure, and firm culture shape who works where, under what conditions, and with what response. The economic question is not whether social life matters. It is how social meaning enters labor choice, workplace behavior, and worker-firm matching in ways that change effort, satisfaction, quits, promotion, pay comparisons, and sorting.

This week stays at the behavioral-labor and micro-norms level. It is about workers, teams, supervisors, firms, and near-market allocation. Labor law, state capacity, unions as political organizations, historical institutional change, and macro cultural persistence belong mainly in the political and cultural institutions course.

:::{admonition} Core points
:class: important

- Identity and norms are labor objects when they shape job choice, effort, promotion aspirations, compliance, morale, and retention.
- Fairness concerns turn wages and treatment into social-comparison objects, so worker responses can move even when absolute pay is unchanged.
- Peer pressure differs from peer learning: coworkers can transmit information, but they can also enforce group effort norms through social sanctions.
- Firm culture is a labor-market object because firms communicate it, workers sort on it, and it can affect hiring, quits, match quality, and inequality.
- Managers and supervisors can transmit local norms, not only monitor effort or evaluate performance.
- Empirical claims must name the behavioral object, labor margin, reference group, identifying variation, and whether the evidence identifies treatment, sorting, transmission, or equilibrium cultural selection.

:::

## Bridge

Weeks 1 through 4 built the behavioral primitives: nonstandard preferences, beliefs, attention, complexity, and learning. Week 5 moved those objects inside the employment relationship by studying incentives, contracts, reciprocity, monitoring, and evaluation. Week 6 widens the workplace lens. Workers do not encounter jobs only as bundles of wages, tasks, and monitoring. They also encounter jobs as roles, identities, teams, cultures, and comparison environments.

That shift changes the labor margin. A worker may choose a job because it fits an identity, reject a firm because its culture feels hostile, reduce effort after learning a peer earns more, conform to team effort norms, or pursue promotion differently after observing supervisor expectations. The same wage can feel fair or unfair depending on the reference group. The same task can feel dignified or identity-inconsistent depending on local norms. The same manager can change team behavior by transmitting what counts as acceptable effort, loyalty, ambition, or flexibility.

The boundary with the institutions course is deliberate. This week is micro and allocation-focused. The institutions course asks how law, state capacity, political conflict, unions, and historical cultural persistence shape labor-market rules. Week 6 asks how identity, fairness, team norms, firm culture, and supervisors shape worker choices and within-firm or near-market allocation.

## Field Core

### Identity And Self-Image At Work

A labor model can start from wages and effort costs, but workers also care about who they are and what kind of worker they are expected to be. The Akerlof-Kranton contribution is to make identity part of the objective function rather than a residual label for unexplained behavior [@akerlofKranton2005]. In organizations, identity can substitute for incentives, complement incentives, or make incentives backfire when a contract conflicts with role meaning.

One compact identity-in-organization object is:

```{math}
:label: eq:identity-utility-week6
U_i(a,j) = u\!\left(w_j\right) - c_i(a) + I_i\!\left(a, j, N_j, C_j\right)
```

Here {math}`a` is an action such as effort, compliance, application, promotion effort, or staying in a job. The job or team is {math}`j`, {math}`N_j` denotes social norms in job or team {math}`j`, and {math}`C_j` denotes firm culture. The identity term {math}`I_i(\cdot)` captures whether the action and role fit the worker's self-image, group identity, and beliefs about what "people like me" do at work.

This formulation keeps identity tied to labor economics. It predicts movement on job choice, effort provision, willingness to comply with informal expectations, promotion aspirations, sorting into firms, and reactions to respect or disrespect. It also clarifies the empirical demand. A design should say which identity object changes, which labor margin moves, and why the result is not simply standard heterogeneity in tastes or constraints.

Gender norms can be used as one brief allocation example, but they should not dominate the week. [@bertrandKamenicaPan2015] is useful because it shows how identity-linked norms can shape household labor and earnings arrangements. Here it serves as an illustration of identity in allocation, not as a substitute for the micro workplace focus.

### Fairness And Pay Comparisons

Fairness turns pay into a social object. Workers may evaluate their wage, treatment, and status relative to peers, supervisors, or workers in comparable roles. This matters because a policy or firm decision can change utility by changing comparison information, pay dispersion, or perceived procedural fairness.

A simple social-comparison object is:

```{math}
:label: eq:fairness-comparisons-week6
U_i = u\!\left(w_i\right) - c(e_i) - \phi_i \max\{0, w^{ref}_i - w_i\} - \psi_i \max\{0, w_i - w^{ref}_i\}
```

Here {math}`w^{ref}_i` is a peer or manager comparison wage. The parameter {math}`\phi_i` captures the cost of being paid less than the reference wage, and {math}`\psi_i` allows discomfort, guilt, or social cost from being paid more. In many labor settings, the first term is likely stronger, but the second keeps the model open to inequity aversion and relational concerns.

The empirical anchors make the same discipline visible. [@brezaKaurShamdasani2018] studies morale effects of pay inequality, with the behavioral object being fairness over relative pay and the labor margins including effort and attendance. [@cullenPerezTruglia2018] studies salary comparisons and pay information, where the comparison group can include peers and managers and the outcomes include satisfaction, beliefs, and job-search or quit-related behavior.

The key diagnostic is not "workers dislike inequality" in general. It is: whose wage is the reference wage, what information changed, what labor margin moved, and whether the effect is a fairness treatment, an information update about career prospects, a sorting response, or a longer-run equilibrium response to transparency.

### Peer Pressure And Micro Norms

Peer effects can arise through information, productivity complementarities, monitoring, social pressure, or sanctions. Week 6 focuses on the norm channel: coworkers can discipline or encourage behavior when effort is visible and when deviating from local group behavior is socially costly.

A peer-pressure object is:

```{math}
:label: eq:peer-pressure-week6
U_i(e_i) = u\!\left(w_i\right) - c(e_i) - P_i\!\left(e_i,\bar e_{-i},N_g\right)
```

Here {math}`N_g` is the group norm and {math}`P_i` captures social penalties from deviating from coworker behavior. The comparison object is {math}`\bar e_{-i}`, the behavior of other workers in the group. The penalty may be explicit criticism, loss of coworker goodwill, informal exclusion, or pressure to match a team standard.

[@masMoretti2009] is the primary anchor because it makes peers at work measurable. The observed margin is workplace productivity. The relevant reference group is the set of coworkers whose behavior is visible or socially salient. The identification problem is to separate peer pressure from peer learning, common shocks, worker sorting, and mechanical productivity spillovers.

Micro norms are local. They include firm culture, team culture, peer pressure, manager norms, social sanctions, conformity, and belief formation about what "people like me" do at work. A team can develop norms about acceptable effort, flexibility, loyalty, lunch breaks, staying late, helping coworkers, reporting problems, or reacting to pay gaps. These norms need not be society-wide to matter for labor allocation. They can operate inside a shift, crew, office, occupation, or firm.

```{include} assets/tables/06-micro-norms-peer-pressure-and-firm-culture-map.md
```

### Firm Culture And Labor-Market Sorting

Firm culture is often discussed loosely, but labor economists can make it precise. Culture is a bundle of communicated and experienced norms, values, routines, rewards, and expectations that shape worker beliefs about the job. It matters for labor markets if it affects who applies, who accepts, who stays, who performs, who advances, or who exits.

A sorting object makes the allocation margin explicit:

```{math}
:label: eq:sorting-culture-week6
j_i^\star \in \arg\max_{j \in \mathcal{J}} \; \mathbb{E}\!\left[U_i(j; X_i, N_j, C_j)\right]
```

Workers choose jobs or firms {math}`j` from a set {math}`\mathcal{J}`. Expected utility depends on worker characteristics {math}`X_i`, local norms {math}`N_j`, and firm culture {math}`C_j`. Identity and culture therefore shape labor-market allocation: applications, hiring, match quality, quits, retention, and mobility.

[@huangPacelliShiZou2024] is the culture-communication and sorting anchor. Job postings and firm messages can reveal or construct culture. Workers can respond through application and acceptance decisions. The design question is whether culture text changes the applicant pool, reveals existing firm type, changes worker expectations, or selects workers who already prefer the communicated culture.

Culture is therefore not only a treatment. It can be an attribute workers sort on, a message firms choose, a workplace environment incumbents experience, and an equilibrium object. The empirical task is to separate sorting from within-firm treatment and from equilibrium cultural selection.

### Manager And Supervisor Transmission Of Norms

Week 5 treated managers as monitors, evaluators, and supervisors. Week 6 adds a different role: managers can carry and transmit norms. They shape what effort is respected, whose ambition is encouraged, which behavior is rewarded informally, what flexibility is acceptable, and who is perceived as fitting the team.

A simple culture-evolution object is:

```{math}
:label: eq:culture-transmission-week6
C_{f,t+1} = \Gamma\!\left(C_{f,t}, M_{f,t}, H_{f,t}, R_{f,t}\right)
```

Culture in firm {math}`f` evolves with prior culture {math}`C_{f,t}`, managers {math}`M_{f,t}`, hiring {math}`H_{f,t}`, and reward systems {math}`R_{f,t}`. The object is intentionally dynamic. Culture is not fixed background. It is produced, transmitted, and updated inside organizations.

[@minniNguyenSarsonsSrebot2026] provides the frontier anchor on manager-driven norm transmission. The labor margins include promotion, pay gaps, team composition, career advancement, and local culture persistence. The key identification challenge is assignment: do managers transmit norms, or do they simply differ in skill, information, preferences, or the teams they supervise?

Manager-rotation and assignment designs are powerful when they can separate manager traits from worker composition and team shocks. The analysis should name the transmitted norm, the affected group, the labor margin, and whether the evidence identifies transmission rather than sorting or managerial quality.

### Frontier Questions On Micro Culture And Workplace Behavior

The frontier is not "culture matters." The frontier is measurement, identification, and equilibrium. Can researchers measure culture through job postings, worker reviews, internal communications, manager histories, or team assignments? Do culture messages attract different workers or change behavior after entry? Do managers transmit norms across teams? Does pay transparency improve fairness or induce discouragement, quits, and resentment? Do algorithmic teams create new forms of peer pressure and conformity?

```{include} assets/tables/06-identity-norms-fairness-map.md
```

The strongest papers will connect a precise behavioral object to a labor allocation margin. Identity should predict who applies, stays, exerts effort, or seeks promotion. Fairness should predict morale, effort, attendance, quits, cooperation, or pay satisfaction. Peer pressure should predict effort when coworkers are visible and sanctions are plausible. Culture should predict sorting, retention, match quality, and inequality. Manager norms should predict transmission through assignments, promotions, evaluations, and reward systems.

## Research Lab

The Week 6 lab is organized around **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is [@masMoretti2009]. Students use deterministic synthetic data to reproduce a compact peer-at-work factbook. The teaching path compares worker productivity when high-effort peers are visible versus when the same worker is exposed to lower peer effort. The objective is not an official replication. It is to practice separating peer pressure, peer learning, and common shocks in a bounded setting.

**Diagnose.** Students classify each design by five objects: the behavioral object, the labor margin, the social or reference group, the identifying variation, and the interpretation. A valid diagnosis must say whether the evidence speaks to peer pressure, fairness, sorting, or norm transmission. It must also say whether the result is a treatment effect on incumbents, a sorting effect across jobs and firms, a transmission effect through managers, or an equilibrium selection effect.

**Transfer.** The secondary anchor is [@brezaKaurShamdasani2018]. Students adapt the diagnostic logic to fairness and pay comparisons: who is the reference group, what wage information or pay dispersion changes, and which labor margin moves? The optional frontier extension uses [@huangPacelliShiZou2024] or [@minniNguyenSarsonsSrebot2026] to transfer the framework to firm culture communication, algorithmic teams, or manager rotation settings.

The bounded path runs locally without confidential employer data. It trains a habit that should carry into real research: name the norm or identity object, name the comparison group, distinguish peer pressure from fairness and sorting, and specify what identifying variation would be needed for a stronger claim.

## Methods Box

:::{admonition} Methods Box: identifying identity, norms, fairness, and culture
:class: note

**Field experiments on peer effects** vary coworker exposure, visibility, team composition, or scheduling. They are strongest when they can separate peer pressure from peer learning, common shocks, and mechanical productivity complementarities.

**Experiments or quasi-experiments on pay transparency and social comparisons** vary information about peer or manager wages, pay compression, pay dispersion, or visibility of compensation. They must separate fairness from career-belief updating and from sorting into or out of the firm.

**Survey-plus-administrative designs on wage beliefs and morale** combine elicited beliefs, satisfaction, morale, applications, quits, effort, attendance, and payroll records. They are useful when the research question requires both the perceived reference wage and actual labor behavior.

**Firm-postings and text designs for culture communication** measure how firms describe values, flexibility, competition, inclusion, hierarchy, or mission. They must distinguish culture as communication, culture as a latent firm attribute, and culture as a selection device.

**Manager-rotation or assignment designs for norm transmission** use changes in supervisors, managers, or team leaders to study whether local norms move across workers and teams. They require careful separation of manager quality, team composition, and manager-specific cultural transmission.

**Sorting, treatment, and equilibrium cultural selection** are different claims. Sorting changes who enters or stays. Treatment changes behavior after exposure. Transmission moves norms through managers, peers, or teams. Equilibrium cultural selection changes the distribution of workers and firms after both sides respond.

:::

```{include} assets/tables/06-identification-and-frontier-map.md
```

Across all designs, do not present a result without naming the behavioral object, labor margin, social or reference group, identifying variation, and whether the effect is treatment, sorting, transmission, or equilibrium selection.

## Reading Ladder And References

**Core framing.** Start with [@akerlofKranton2005] for identity and organizations. Read it as a labor model of roles, norms, incentives, and self-image, not as a generic sociology add-on.

**Peer pressure and coworker norms.** Use [@masMoretti2009] as the primary anchor for peers at work. Focus on the distinction between productivity spillovers, peer learning, visibility, and social pressure.

**Fairness and relative pay.** Pair [@brezaKaurShamdasani2018] with [@cullenPerezTruglia2018]. The first centers morale effects of pay inequality; the second centers salary comparisons, wage beliefs, and reference groups that include peers and managers.

**Culture communication and sorting.** Use [@huangPacelliShiZou2024] to study how firms communicate culture in labor markets and how workers may sort in response to culture signals.

**Manager transmission frontier.** Read [@minniNguyenSarsonsSrebot2026] for the frontier idea that managers can transmit workplace norms and shape inequality through local organizational channels.

**Brief allocation example.** Use [@bertrandKamenicaPan2015] as a short example of identity-linked labor allocation outside the firm. Keep the lecture centered on micro workplace norms, firm culture, and near-market allocation.

## Exercises And Discussion Prompts

1. In equation {eq}`eq:identity-utility-week6`, give one example where {math}`I_i(a,j,N_j,C_j)` changes effort and one example where it changes job choice.
2. In equation {eq}`eq:fairness-comparisons-week6`, define {math}`w^{ref}_i` for a peer comparison and for a manager comparison. What outcome would you expect to move in each case?
3. In equation {eq}`eq:peer-pressure-week6`, what data would distinguish peer pressure from peer learning?
4. Suppose a firm advertises a collaborative culture. Is the observed applicant response a treatment effect, sorting effect, or culture-communication effect? What design would help separate them?
5. In equation {eq}`eq:culture-transmission-week6`, what variation would identify the effect of {math}`M_{f,t}` separately from hiring {math}`H_{f,t}`?
6. Choose one empirical anchor from the reading ladder. State the behavioral object, labor margin, reference group, identifying variation, and interpretation.
7. Design a study of algorithmic teams. What is the norm, who is the comparison group, and what would count as peer pressure rather than monitoring?

## Reproducibility And Code Lab Note

The Week 6 lab lives at `labs/06-identity-norms-fairness-and-labor-market-allocation/`. It creates deterministic synthetic data for peer pressure at work, fairness and pay-comparison diagnosis, and culture sorting with manager-transmission transfer. The smoke path builds the data, runs the reproduction script, and runs the transfer script. It is a bounded teaching lab, not an official replication package for the cited papers.

## Slide Companion Note

The Week 6 slide deck lives at `slides/week6/06-identity-norms-fairness-and-labor-market-allocation.tex`. The deck defines the central question, bridges from Weeks 1 through 5, sets the boundary with the institutions course, introduces the identity, fairness, peer-pressure, sorting, and culture-transmission objects, and ends with empirical designs, frontier questions, and the bridge to Week 7.

## Bridge Forward

Week 6 completes the application-heavy middle of the course. Weeks 5 and 6 show that behavioral labor is not only about individual mistakes. Contracts, supervisors, peers, identity, fairness, norms, and culture shape labor behavior inside firms and across jobs. Week 7 turns this into a methods problem: how can labor economists identify behavioral wedges without confusing them with constraints, institutions, sorting, or measurement error?
