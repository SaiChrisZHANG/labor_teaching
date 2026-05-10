# Week 6 source pack — Identity, norms, fairness, and labor-market allocation

## Central question

How do identity, norms, fairness concerns, peer pressure, and firm culture shape labor-market allocation, workplace behavior, and worker–firm matching?

## Why this week matters

Behavioral labor should not treat preferences as purely individual and isolated. Workers interpret jobs, wages, effort, promotion, and workplace relations through social identity, reference groups, and local norms. That makes labor-market allocation partly a social process: workers sort into jobs and firms, firms communicate and cultivate culture, and managers can transmit norms within workplaces.

This is also a natural point to distinguish **micro norms** from the broader institutional themes that will belong in the political/cultural institutions special topic. Here the emphasis is narrow and labor-economic:
- identity at work,
- fairness and social comparison,
- peer pressure and team norms,
- firm culture and worker sorting,
- manager-driven transmission of norms.

## Topic boundary

This week should stay clearly distinct from the political/cultural institutions course.

### This week *is* about
- identity and self-image in organizations
- fairness and relative pay concerns inside firms
- coworker comparisons and peer pressure
- team norms and micro culture
- firm culture as a sorting and allocation object
- how managers shape local workplace norms
- how these channels affect effort, satisfaction, quits, promotion, pay, and job choice

### This week is *not* mainly about
- labor law
- state capacity
- unions and collective political organization
- historical institutional persistence
- macro political conflict over labor-market rules
- long-run cultural persistence at the societal level

If a norm is operating through workplace interactions, local labor-market expectations, team behavior, or firm culture, it belongs here. If it is operating through the state, law, historical political institutions, or macro social structure, it belongs mainly in the institutions course.

## Core arc

### A. Identity and self-image at work

Start from the idea that workers care not only about wages and effort costs but also about whether their work role is consistent with who they think they are or who they believe they ought to be. This is the Akerlof–Kranton insight for organizations: identity can substitute for, complement, or reshape the effects of incentives.

A simple representation is:

```{math}
:label: eq:identity-utility-week6
U_i(a,j) = u\!\left(w_j\right) - c_i(a) + I_i\!\left(a, j, N_j, C_j\right)
```

where `{math}`I_i(\cdot)`` captures identity utility, `{math}`N_j`` denotes local norms in job or team `{math}`j``, and `{math}`C_j`` denotes firm culture.

The chapter should make clear that identity matters for:
- occupational or job choice,
- effort provision,
- willingness to comply with informal expectations,
- responsiveness to fairness or disrespect,
- promotion and supervisory aspirations,
- sorting into workplaces with different cultures.

Use `[@akerlofKranton2005]` as the framing anchor.

### B. Fairness and relative pay comparisons

A second key channel is fairness. Workers do not only respond to their own wage; they also compare their pay, treatment, and status to peers and supervisors. That means workplace outcomes can change even when no worker’s absolute contract changes.

A useful reduced-form object is:

```{math}
:label: eq:fairness-comparisons-week6
U_i = u\!\left(w_i\right) - c(e_i) - \phi_i \max\{0, w^{ref}_i - w_i\} - \psi_i \max\{0, w_i - w^{ref}_i\}
```

where `{math}`w^{ref}_i`` is a reference wage.

This block should show students how fairness concerns can affect:
- effort,
- attendance,
- morale,
- quit intentions,
- cooperation,
- openness to performance pay,
- interpretation of pay transparency.

Use `[@brezaKaurShamdasani2018]` and `[@cullenPerezTruglia2018]` as explicit anchors.

### C. Peer pressure and coworker norms

A separate but related object is peer pressure. Coworkers can discipline or encourage one another, especially when actions are visible and the social cost of deviating from group effort is high.

A simple way to write this is:

```{math}
:label: eq:peer-pressure-week6
U_i(e_i) = u\!\left(w_i\right) - c(e_i) - P_i\!\left(e_i,\bar e_{-i},N_g\right)
```

where `{math}`P_i`` captures social penalties or pressure from deviating from coworker behavior and `{math}`N_g`` is the group norm.

This section should make students distinguish:
- peer learning vs peer pressure,
- information spillovers vs social sanctions,
- peer productivity effects vs norm enforcement,
- local team norms vs broad social norms.

Use `[@masMoretti2009]` as the main anchor.

### D. Micro norms inside teams and firms

This subsection is where the week becomes clearly more current. Norms are not just “society-level.” They can be highly local:
- what a team sees as acceptable effort,
- what counts as loyalty or commitment,
- how much flexibility is acceptable,
- how coworkers react to differential pay,
- what behavior is informally rewarded,
- how workers interpret managerial treatment.

This is where **micro norms** should be introduced explicitly. The lecture should make clear that firm culture is not only an abstract management concept; it is a labor-market object that shapes worker sorting, retention, morale, promotion, and performance.

### E. Firm culture as a labor-market object

The chapter should make firm culture legible to labor economists:
- firms communicate culture to attract certain workers,
- workers sort based on culture fit,
- culture may affect who stays, who leaves, who advances, and how workers behave,
- culture can interact with identity and fairness.

A clean sorting object is:

```{math}
:label: eq:sorting-culture-week6
j_i^\star \in \arg\max_{j \in \mathcal{J}} \; \mathbb{E}\!\left[U_i(j; X_i, N_j, C_j)\right]
```

This section should focus on labor-market allocation:
- hiring and applicant composition,
- match quality,
- quits and retention,
- workplace heterogeneity,
- worker–firm sorting by norms and culture.

Use `[@huangPacelliShiZou2024]` as the explicit frontier anchor for culture communication and labor-market sorting.

### F. Managers, supervisors, and transmission of workplace norms

A frontier contribution of recent work is to treat managers not only as monitors or evaluators, but also as **carriers of norms**. Managers shape:
- local promotion standards,
- acceptable work practices,
- pay or performance norms,
- who belongs,
- how gender or status hierarchies are reproduced or weakened.

A useful law of motion is:

```{math}
:label: eq:culture-transmission-week6
C_{f,t+1} = \Gamma\!\left(C_{f,t}, M_{f,t}, H_{f,t}, R_{f,t}\right)
```

where culture evolves with managers `{math}`M_{f,t}``, hiring `{math}`H_{f,t}``, and rewards `{math}`R_{f,t}``.

This section should show students that culture is not fixed. It is produced and transmitted inside organizations.

Use `[@minniNguyenSarsonsSrebot2026]` as the frontier anchor.

### G. Allocation implications

This week should always return to labor allocation. Identity, fairness, and norms matter because they shape:
- which jobs workers choose,
- whether they accept or reject workplaces,
- where they apply,
- whether they remain in a firm,
- how they react to pay comparisons,
- whether they seek promotion,
- how supervisors allocate opportunities,
- how firms attract workers who fit local norms.

This is the key way to keep the lecture connected to labor economics rather than drifting into generic organizational sociology.

### H. One brief allocation example beyond the firm

It is fine to include one brief example of broader labor allocation through norms, such as gender-identity constraints affecting labor supply and earnings arrangements. But this should remain a short illustration, not the main theme.

Use `[@bertrandKamenicaPan2015]` briefly and carefully.

## Methods and identification

The methods section should clearly separate several empirical strategies:

1. **peer-effects / peer-pressure designs**
   - visibility-based productivity spillovers,
   - within-team variation,
   - shift-based or line-based coworker exposure.

2. **fairness and pay-comparison designs**
   - pay compression vs disparity experiments,
   - information provision about peer or manager salaries,
   - survey-plus-administrative measures of morale and behavior.

3. **firm-culture and sorting designs**
   - text-as-data from job postings,
   - worker inflow / applicant composition responses,
   - culture communication and selection.

4. **manager-transmission designs**
   - manager assignment or manager rotation,
   - supervisor norms and downstream worker outcomes,
   - promotion and pay-gap transmission mechanisms.

5. **identity and allocation examples**
   - designs linking social identity norms to labor supply, work, earnings, or career choice.

Students should leave the week able to answer:
- What is the relevant social reference group?
- Is the paper identifying treatment, sorting, transmission, or equilibrium selection?
- Does the behavioral mechanism operate through identity, fairness, peer pressure, or culture?
- What labor-market outcome is moved?

## Reading backbone

The backbone should feel like:
- theory / concept: Akerlof–Kranton
- coworker norms and peer pressure: Mas–Moretti
- fairness / relative pay: Breza–Kaur–Shamdasani; Cullen–Perez-Truglia
- culture communication and sorting: Huang–Pacelli–Shi–Zou
- manager-driven norm transmission: Minni–Nguyen–Sarsons–Srebot
- broader identity-allocation illustration: Bertrand–Kamenica–Pan

## Research frontier

The frontier should be explicit and visible:
- micro culture rather than only macro norms
- how managers shape local workplace norms
- measuring culture through text, reviews, or managerial assignments
- fairness and morale under pay transparency
- coworker comparisons when workers learn more about peers and supervisors
- algorithmic teams and digital micro norms
- interactions between firm culture and worker sorting
- whether culture changes productivity, retention, inequality, or all three
