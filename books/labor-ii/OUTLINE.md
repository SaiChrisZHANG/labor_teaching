# Labor II: Firms, Frictions, and Institutions

## Course role in the portfolio

Labor II is the second semester of the core labor sequence. It takes the worker-side foundations from Labor I and embeds them into firm behavior, market frictions, wage-setting institutions, aggregate adjustment, and major shocks to labor demand.

The course is designed to answer five linked questions:
1. How do firms decide how much labor to hire and how quickly to adjust?
2. How do internal firm incentives and market frictions shape worker outcomes?
3. How are wages determined once search, bargaining, and labor market power matter?
4. How do labor policies and institutions reshape firm behavior and market outcomes?
5. How do aggregate, technological, and trade shocks propagate through labor markets?

## Pedagogical logic

This course begins inside the firm, then moves outward to market interaction, then to policy and institutions, and finally to economy-wide shocks and adjustment. The ordering is deliberate.

Students first learn the firm-side partial-equilibrium logic of labor demand, adjustment costs, and personnel economics. Only after those pieces are in place do they move to search, bargaining, and monopsony, where firm behavior is mediated by market structure. The policy block then asks how minimum wages, unions, regulation, enforcement, and insurance change those mechanisms. The final third of the course asks how labor markets respond when shocks are large, persistent, and economy-wide.

## Audience and prerequisites

Primary audience:
- PhD students who have completed Labor I or equivalent preparation

Secondary audience:
- advanced master's students with strong labor economics and econometrics preparation

Prerequisites:
- Labor I or a solid worker-side labor background
- graduate microeconomic theory
- applied econometrics

## Time budget and weekly rhythm

Default design: **13 teaching weeks**, **3 hours per week**.

Recommended structure for each 3-hour week:
- **75 minutes**: conceptual model or organizing framework
- **60 minutes**: empirical evidence and identification strategies
- **45 minutes**: research extensions, policy applications, or code-based exploration

This outline is built to be compressible to 10 or 12 weeks and expandable to 14 weeks without changing the core identity of the course.

## Learning goals

By the end of the course, students should be able to:
1. explain labor demand, adjustment costs, and internal firm labor allocation;
2. connect search frictions, bargaining, and labor market power to wage-setting and employment outcomes;
3. evaluate labor market institutions and policies from both firm and market perspectives;
4. interpret aggregate labor market adjustment under macro, technology, and trade shocks;
5. distinguish partial-equilibrium from equilibrium reasoning in labor economics;
6. formulate research questions that connect firms, institutions, shocks, and labor market outcomes.

## Shared toolkit dependencies

This course should reuse or link to the following shared modules when they exist:
- `shared/labor-market-facts-and-datasets.md`
- `shared/identification-primer.md`
- `shared/structural-estimation-primer.md`
- `shared/reproducibility-workflow.md`

## Week-by-week outline

### Week 1. Labor demand and production

**Central question:** How do firms decide how much labor to hire in a static production setting?

**Why this week is first:** The semester begins by putting the firm at the center.

**Bridge:**
- labor as an input in production
- substitution across labor, capital, and tasks
- static labor demand intuition

**Field Core:**
- firm optimization and conditional labor demand
- wage changes, output demand, and factor substitution
- short-run vs. long-run demand responses

**Research Lab:**
- what margins of adjustment are observed in real data?
- how do product markets shape estimated labor demand elasticities?

**Reading ladder buckets:**
- canonical labor demand theory [placeholder]
- empirical labor demand estimation [placeholder]
- frontier paper on tasks or firm heterogeneity [placeholder]

**Code lab opportunity:** simulate labor demand under different production elasticities.

---

### Week 2. Dynamic labor demand and adjustment costs

**Central question:** Why do firms adjust employment slowly, and what are the consequences of adjustment frictions?

**Why here:** Dynamic adjustment is the natural extension of static demand and is required before internal labor market design.

**Bridge:**
- hiring, firing, and vacancy creation as costly choices
- dynamic adjustment intuition
- persistence in employment

**Field Core:**
- dynamic labor demand with adjustment costs
- convex and nonconvex costs
- employment persistence and firm response to shocks

**Research Lab:**
- identifying adjustment frictions from firm-level or plant-level data
- connections between adjustment costs and policy incidence

**Reading ladder buckets:**
- canonical dynamic labor demand framework [placeholder]
- empirical evidence on adjustment frictions [placeholder]
- frontier paper on plant or firm dynamics [placeholder]

**Code lab opportunity:** simulate dynamic employment adjustment after demand shocks.

---

### Week 3. Personnel economics and internal labor markets

**Central question:** How do firms structure incentives, promotions, monitoring, and pay inside the organization?

**Why here:** This remains a firm-side partial-equilibrium week and fits naturally after labor demand and adjustment.

**Bridge:**
- performance pay, promotions, tournaments, monitoring
- internal vs. external labor markets
- incentive problems inside firms

**Field Core:**
- incentive contracts and worker-firm relationships
- promotion systems, career ladders, and internal wage structures
- personnel policies as labor allocation devices

**Research Lab:**
- management practices and productivity
- using personnel data to study incentives and sorting

**Reading ladder buckets:**
- canonical personnel economics framework [placeholder]
- empirical paper on promotions, incentives, or management [placeholder]
- frontier paper using personnel or administrative data [placeholder]

**Code lab opportunity:** descriptive exercise on promotions, turnover, or wage trajectories in a synthetic personnel dataset.

---

### Week 4. Search, matching, turnover, and unemployment

**Central question:** How do search frictions shape hiring, separations, unemployment, and turnover?

**Why here:** After the partial-equilibrium firm block, the course moves to market interaction under frictions.

**Bridge:**
- search frictions and matching intuition
- unemployment as a flow equilibrium outcome
- job-finding and separation rates

**Field Core:**
- search and matching framework
- job creation and job destruction
- turnover, vacancies, and unemployment dynamics

**Research Lab:**
- measuring flows and frictions in administrative or survey data
- when does matching structure matter empirically?

**Reading ladder buckets:**
- canonical search/matching theory [placeholder]
- empirical turnover or unemployment flows paper [placeholder]
- frontier paper on matching efficiency or worker-firm matching [placeholder]

**Code lab opportunity:** calculate flow-based unemployment statistics or plot a Beveridge-style relationship.

---

### Week 5. Wage posting, bargaining, and wage-setting

**Central question:** How are wages set when search and bargaining replace the competitive benchmark?

**Why here:** Once matching exists, wage determination needs a new framework.

**Bridge:**
- wage posting vs. bargaining intuition
- outside options and bargaining power
- why identical workers may earn different wages

**Field Core:**
- bargaining models and surplus division
- wage posting models
- implications for wage dispersion and mobility

**Research Lab:**
- how can bargaining power be identified?
- empirical signatures of different wage-setting regimes

**Reading ladder buckets:**
- canonical wage-setting framework [placeholder]
- empirical paper on bargaining or wage-setting [placeholder]
- frontier paper on outside options or rent sharing [placeholder]

**Code lab opportunity:** compare wage outcomes under competitive, bargaining, and posting environments.

---

### Week 6. Monopsony and labor market power

**Central question:** When do firms have labor market power, and what does that imply for wages and employment?

**Why here:** Monopsony is the natural culmination of the market-interaction block.

**Bridge:**
- monopsony intuition beyond the single-employer case
- labor supply to the firm
- markdowns and worker mobility

**Field Core:**
- dynamic and modern monopsony frameworks
- sources of labor market power
- wage markdowns, concentration, and mobility frictions

**Research Lab:**
- measuring labor market power in practice
- links between monopsony, inequality, and policy design

**Reading ladder buckets:**
- canonical monopsony framework [placeholder]
- empirical paper on labor market power [placeholder]
- frontier paper on concentration, mobility, or markdowns [placeholder]

**Code lab opportunity:** simple markdown calculations or concentration-style exercises.

---

### Week 7. Minimum wages and wage-setting policy

**Central question:** How do wage floors affect firms, workers, and labor market equilibrium?

**Why this starts the policy block:** Minimum wages are the cleanest entry point into wage-setting institutions.

**Bridge:**
- wage floors in competitive and imperfectly competitive settings
- margins of adjustment beyond employment
- compliance and enforcement intuition

**Field Core:**
- minimum wages under alternative labor market structures
- employment, wages, hours, prices, composition, and turnover
- identification challenges in policy evaluation

**Research Lab:**
- heterogeneity by firms, workers, and local markets
- how monopsony changes policy interpretation

**Reading ladder buckets:**
- canonical minimum wage framework [placeholder]
- empirical minimum wage paper [placeholder]
- frontier paper on margins beyond employment [placeholder]

**Shared toolkit dependency:** identification primer

**Code lab opportunity:** event-study style replication shell for a wage-floor policy design.

---

### Week 8. Unions, collective bargaining, and worker voice

**Central question:** How do collective institutions affect wages, rents, governance, and workplace outcomes?

**Why here:** This extends the policy block from wage floors to collective wage-setting and representation.

**Bridge:**
- unions as wage-setting and voice institutions
- bargaining units and collective action
- worker voice beyond wages

**Field Core:**
- collective bargaining frameworks
- rents, distribution, governance, and productivity
- institutional variation across settings

**Research Lab:**
- unions and inequality
- historical and modern perspectives on worker voice

**Reading ladder buckets:**
- canonical union or bargaining framework [placeholder]
- empirical union effects paper [placeholder]
- frontier paper on worker voice or workplace governance [placeholder]

**Code lab opportunity:** descriptive comparison of outcomes in high- vs. low-union settings.

---

### Week 9. Labor market regulation, enforcement, and insurance

**Central question:** How do labor regulations and social insurance programs shape labor market outcomes?

**Why here:** This completes the policy block by broadening from wage-setting institutions to rules and protections.

**Bridge:**
- employment protection, workplace regulation, unemployment insurance, enforcement
- regulation as both constraint and insurance

**Field Core:**
- firm and worker responses to regulation
- design and enforcement margins
- incidence and equilibrium adjustment under labor market rules

**Research Lab:**
- interaction of enforcement capacity and policy effectiveness
- comparing regulation-focused and transfer-focused labor policy

**Reading ladder buckets:**
- canonical regulation or insurance framework [placeholder]
- empirical policy evaluation paper [placeholder]
- frontier paper on enforcement or compliance [placeholder]

**Code lab opportunity:** policy comparison memo using a common evaluation template.

---

### Week 10. Aggregate fluctuations and labor market adjustment

**Central question:** How do employment, unemployment, vacancies, wages, and participation adjust when shocks are economy-wide?

**Why here:** After firms, frictions, wage-setting, and policy, students are ready to scale those mechanisms up to aggregate dynamics.

**Bridge:**
- business-cycle intuition in labor markets
- vacancies, separations, and job finding over time
- why aggregate shocks differ from local or partial-equilibrium shocks

**Field Core:**
- unemployment dynamics and vacancy adjustment
- wage cyclicality or rigidity
- heterogeneous worker and firm responses over the cycle

**Research Lab:**
- persistence, scarring, and recovery
- how search frictions and institutions shape aggregate adjustment

**Reading ladder buckets:**
- canonical unemployment-dynamics framework [placeholder]
- empirical business-cycle labor paper [placeholder]
- frontier paper on heterogeneity in aggregate adjustment [placeholder]

**Code lab opportunity:** plot cyclical movements in labor market stocks and flows.

---

### Week 11. Technology, automation, AI, and labor market

**Central question:** How do technological changes reshape tasks, demand for skills, and worker allocation?

**Why here:** Technology is a major labor-demand shock and deserves its own week rather than being folded into trade.

**Bridge:**
- automation, augmentation, task substitution, and complementarity
- skill demand and occupational change

**Field Core:**
- task-based approaches to technological change
- firm adoption and labor demand responses
- distributional and occupational implications

**Research Lab:**
- empirical identification of technology exposure
- AI, task content, and changing job design

**Reading ladder buckets:**
- canonical technology and labor framework [placeholder]
- empirical automation or task-change paper [placeholder]
- frontier paper on AI and work [placeholder]

**Code lab opportunity:** construct a simple exposure index or task-based descriptive exercise.

---

### Week 12. Trade, offshoring, and labor market adjustment

**Central question:** How do trade and offshoring shocks transmit through workers, firms, regions, and institutions?

**Why here:** Trade is distinct from technology and highlights a different class of labor-demand and reallocation shocks.

**Bridge:**
- import competition, export exposure, offshoring, and regional incidence
- adjustment costs and worker reallocation

**Field Core:**
- trade shocks and labor market transmission
- firm heterogeneity, worker sorting, and regional exposure
- short-run dislocation vs. longer-run adjustment

**Research Lab:**
- mobility constraints, place effects, and policy response to trade shocks
- comparing trade and technology as labor market shocks

**Reading ladder buckets:**
- canonical trade-and-labor framework [placeholder]
- empirical trade-shock paper [placeholder]
- frontier paper on adjustment or regional persistence [placeholder]

**Code lab opportunity:** map regional exposure to trade-related labor shocks.

---

### Week 13. Synthesis and student research designs

**Central question:** How do firm behavior, market frictions, institutions, and shocks fit into one labor market framework?

**Why last:** This week converts a field survey into a research agenda.

**Bridge:**
- integrative review of the semester

**Field Core:**
- linking labor demand, wage-setting, market power, policy, and shocks
- choosing between reduced-form, structural, and descriptive approaches

**Research Lab:**
- student research design memos or presentations
- comparative discussion of policy and shock-response literatures
- transition to special topics or dissertation questions

**Reading ladder buckets:**
- no new required readings; synthesis materials only

**Deliverable suggestion:** research proposal, referee-style memo, or comparative policy analysis.

## Compression rules

### 10-week version

Merge the following pairs:
- Weeks 1 and 2: static and dynamic labor demand
- Weeks 4 and 5: search/matching and wage-setting
- Weeks 7 and 8: minimum wages and unions

Then choose either Week 10 or one of Weeks 11–12 as a shorter applications week depending on whether the semester is more institution-focused or shock-focused.

### 12-week version

Keep the full sequence, but condense one of the following:
- Weeks 8 and 9 if the policy block is kept compact
- Weeks 11 and 12 if technology and trade are taught comparatively rather than separately

### 14-week version

Add one or two extension weeks such as:
- labor market concentration and antitrust
- workplace surveillance, algorithmic management, or scheduling technology
- advanced structural search models
- comparative labor institutions across countries

## Assessment ideas

Possible assessment mix:
- weekly reading or idea memos
- one policy-evaluation memo
- one replication or code exercise
- final research design presentation or paper proposal

## Relationship to other courses

This course feeds directly into:
- **Behavioral Labor**, by providing a benchmark of firm behavior and market interaction against which behavioral departures can be studied;
- **Labor Markets and Political/Cultural Institutions**, by grounding later institutional analysis in labor demand, wage-setting, and policy mechanisms;
- **Empirical Methods**, through repeated use of policy evaluation, equilibrium interpretation, and structural reasoning.
