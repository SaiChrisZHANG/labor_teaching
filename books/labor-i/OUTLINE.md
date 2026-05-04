# Labor I: Workers, Human Capital, and Inequality

## Course role in the portfolio

Labor I is the first semester of the core labor sequence. It introduces labor economics from the worker side and builds the conceptual foundations students need before moving to firm-side equilibrium, institutions, and aggregate adjustment in Labor II.

The course is designed to answer five linked questions:
1. What are the core labor market outcomes we care about measuring?
2. How do workers allocate time, effort, schooling, and labor supply over the life cycle?
3. How are wages, skill, inequality, and group differences generated?
4. How do households, mobility decisions, and policy environments shape worker outcomes?
5. How do informational and behavioral frictions alter the standard worker-choice benchmark?

## Pedagogical logic

This course begins with measurable labor market objects, then develops worker-side choice models, then embeds those choices in households, distributional outcomes, mobility, and policy. It ends by relaxing the frictionless benchmark through informational and behavioral frictions, which makes Labor I a natural bridge into Behavioral Labor and into the policy evaluation material of the wider teaching platform.

The ordering is deliberately cumulative:
- start with facts and measurement so students know what the field tries to explain;
- build labor supply and human capital foundations before discussing inequality and policy;
- move from individual decisions to households and group outcomes;
- end by showing where standard models fail and where research opportunities begin.

## Audience and prerequisites

Primary audience:
- first- or second-year PhD students in economics

Secondary audience:
- advanced master's students with strong micro and econometrics preparation
- advanced undergraduates using only the Bridge sections

Prerequisites:
- graduate microeconomic theory or equivalent
- introductory econometrics
- willingness to read applied empirical work

## Time budget and weekly rhythm

Default design: **13 teaching weeks**, **3 hours per week**.

Recommended structure for each 3-hour week:
- **75 minutes**: conceptual model or organizing framework
- **60 minutes**: empirical evidence and identification strategies
- **45 minutes**: research extensions, discussion, or code-based exploration

This outline is built to be compressible to 10 or 12 weeks and expandable to 14 weeks without changing the course identity.

## Learning goals

By the end of the course, students should be able to:
1. describe the main worker-side mechanisms used in labor economics;
2. connect labor supply, human capital, household behavior, and wage determination;
3. interpret inequality, discrimination, mobility, and intergenerational outcomes through labor-economic frameworks;
4. evaluate worker-targeted policies using modern empirical designs;
5. identify where informational and behavioral frictions challenge standard models;
6. generate research questions that connect labor theory, data, and policy.

## Shared toolkit dependencies

This course should reuse or link to the following shared modules when they exist:
- `shared/labor-market-facts-and-datasets.md`
- `shared/identification-primer.md`
- `shared/reproducibility-workflow.md`
- `shared/text-and-llm-measurement-primer.md` (optional in later modules)

## Week-by-week outline

### Week 1. Labor market facts, measurement, and canonical questions

**Central question:** What outcomes define labor economics, and how are they measured?

**Why this week is first:** Students need a map of the objects the field studies before seeing models built to explain them.

**Bridge:**
- employment, unemployment, participation, hours, wages, earnings, income
- stock vs. flow measures
- worker, job, establishment, and household as units of analysis

**Field Core:**
- measurement choices and their consequences
- descriptive labor facts as theory discipline
- link between institutional setting and observed statistics

**Research Lab:**
- when stylized facts are stable vs. when they mask heterogeneity
- how administrative, survey, and matched employer-employee data differ

**Reading ladder buckets:**
- canonical labor facts overview [placeholder]
- measurement and datasets [placeholder]
- one frontier descriptive paper [placeholder]

**Shared toolkit dependency:** labor market facts and datasets

**Code lab opportunity:** build a small descriptive dashboard from a public labor dataset.

---

### Week 2. Static labor supply

**Central question:** How do workers choose whether and how much to work in a static setting?

**Why here:** This is the cleanest entry point into worker optimization and policy incidence.

**Bridge:**
- labor-leisure tradeoff
- intensive vs. extensive margins
- budget constraints and nonconvexities

**Field Core:**
- static labor supply under taxes and transfers
- reservation values, participation, and hours choice
- heterogeneity in preferences and constraints

**Research Lab:**
- external validity of labor supply elasticities
- who adjusts on which margin?

**Reading ladder buckets:**
- canonical labor supply theory [placeholder]
- empirical labor supply estimates [placeholder]
- frontier heterogeneity paper [placeholder]

**Code lab opportunity:** simulate participation and hours responses under alternative tax schedules.

---

### Week 3. Dynamic labor supply and lifecycle responses

**Central question:** How do labor supply decisions change over time and over the life cycle?

**Why here:** Dynamic responses are necessary before discussing savings, career timing, fertility, and policy persistence.

**Bridge:**
- intertemporal substitution intuition
- lifecycle framing
- temporary vs. permanent shocks

**Field Core:**
- dynamic labor supply models
- lifecycle labor supply and human capital interaction
- persistence, state dependence, and adjustment frictions

**Research Lab:**
- what can be learned from tax reforms, earnings shocks, and panel variation?
- limits of reduced-form estimates for dynamic policy design

**Reading ladder buckets:**
- canonical lifecycle labor supply [placeholder]
- dynamic response evidence [placeholder]
- frontier paper on persistence or state dependence [placeholder]

**Code lab opportunity:** simple lifecycle simulation with temporary and permanent wage shocks.

---

### Week 4. Human capital and skill formation

**Central question:** How are productive skills built through schooling, training, and experience?

**Why here:** Human capital provides the main bridge from worker choice to wage inequality.

**Bridge:**
- schooling, training, and experience as investments
- private returns vs. social returns
- timing of investment

**Field Core:**
- human capital theory
- general vs. specific training
- dynamic complementarities and skill accumulation

**Research Lab:**
- where do human capital models fit poorly?
- interactions with credit constraints, information, and institutions

**Reading ladder buckets:**
- canonical human capital theory [placeholder]
- empirical returns to education/training [placeholder]
- frontier paper on skill formation or training design [placeholder]

**Code lab opportunity:** estimate and visualize earnings profiles by education or experience group.

---

### Week 5. Wage determination and returns to skill

**Central question:** How are wages linked to productivity, skill, and labor market sorting?

**Why here:** Students have now seen labor supply and human capital; this week connects those primitives to wage outcomes.

**Bridge:**
- wages vs. earnings
- returns to schooling and experience
- sorting and selection intuition

**Field Core:**
- wage equations and interpretation
- compensating vs. productive explanations for wage differences
- selection, sorting, and identification challenges

**Research Lab:**
- how much of wage dispersion is skill, jobs, firms, or institutions?
- what is the right target parameter in returns-to-skill work?

**Reading ladder buckets:**
- canonical wage determination paper [placeholder]
- empirical returns and sorting evidence [placeholder]
- frontier decomposition or sorting paper [placeholder]

**Code lab opportunity:** reproduce a basic wage decomposition or returns-to-schooling graph.

---

### Week 6. Households, family, fertility, and time allocation

**Central question:** How do household structure and family decisions shape labor market behavior?

**Why here:** Worker decisions are often made jointly with partners, children, and care responsibilities.

**Bridge:**
- household production
- joint labor supply
- care constraints and time allocation

**Field Core:**
- collective and unitary household models
- fertility, marriage, and labor supply interactions
- intrahousehold bargaining and policy incidence

**Research Lab:**
- household responses to childcare, leave, and transfer policies
- how household models inform gender and family research

**Reading ladder buckets:**
- canonical family labor supply theory [placeholder]
- empirical work on fertility, care, or household bargaining [placeholder]
- frontier paper on household inequality [placeholder]

**Code lab opportunity:** stylized simulation of joint labor supply with childcare or care-cost shocks.

---

### Week 7. Job amenities and compensating differentials

**Central question:** How do workers value nonwage job attributes and workplace amenities?

**Why here:** This expands worker choice beyond wages and prepares students for job sorting and segmentation.

**Bridge:**
- amenity value and compensating differentials
- risky, flexible, or desirable jobs
- wages as only one component of utility

**Field Core:**
- hedonic intuition in labor markets
- valuation of job amenities and disamenities
- sorting and equilibrium interpretation challenges

**Research Lab:**
- identification of willingness to pay for flexibility, safety, or location
- amenities as a source of inequality

**Reading ladder buckets:**
- canonical compensating differential framework [placeholder]
- empirical amenity valuation paper [placeholder]
- frontier paper on job quality [placeholder]

**Code lab opportunity:** estimate simple wage-amenity correlations and discuss selection bias.

---

### Week 8. Inequality and wage dispersion

**Central question:** Why do labor market outcomes differ so much across workers?

**Why here:** The course now has the ingredients needed to discuss distributional outcomes in a structured way.

**Bridge:**
- inequality measures and decomposition intuition
- between-group vs. within-group inequality
- wages vs. annual earnings vs. household income

**Field Core:**
- decomposition frameworks
- skill-biased, firm-based, and institutional explanations
- composition vs. price effects

**Research Lab:**
- role of firms, tasks, technology, and geography in inequality
- measurement choices in top-income and earnings analysis

**Reading ladder buckets:**
- canonical inequality overview [placeholder]
- empirical decomposition paper [placeholder]
- frontier paper on firms, tasks, or geography [placeholder]

**Code lab opportunity:** compute simple inequality measures and decomposition exercises.

---

### Week 9. Discrimination, identity, and segmentation

**Central question:** How do group identity and market structure generate unequal labor outcomes?

**Why here:** After inequality, students are ready to distinguish discrimination from broader sources of dispersion.

**Bridge:**
- difference between gaps and discrimination
- taste-based, statistical, and identity-based mechanisms
- segmentation and occupational sorting

**Field Core:**
- discrimination frameworks
- employer beliefs, screening, and equilibrium effects
- limits of observational gap comparisons

**Research Lab:**
- experimental and quasi-experimental measurement of discrimination
- how identity, norms, and institutions interact with labor markets

**Reading ladder buckets:**
- canonical discrimination theory [placeholder]
- empirical identification paper [placeholder]
- frontier paper on identity or segmentation [placeholder]

**Code lab opportunity:** compare decomposition-based and experimental approaches conceptually.

---

### Week 10. Mobility, migration, and intergenerational transmission

**Central question:** How do workers move across places, jobs, and generations, and why does that matter for labor outcomes?

**Why here:** Mobility is a natural extension from inequality and discrimination to dynamic reallocation.

**Bridge:**
- migration as investment and sorting
- mobility costs and moving frictions
- intergenerational transmission intuition

**Field Core:**
- spatial and occupational mobility
- migration responses to labor demand and policy
- intergenerational human capital and labor market persistence

**Research Lab:**
- mobility as a mechanism for adjustment vs. mobility as a margin constrained by frictions
- measuring persistence across families and places

**Reading ladder buckets:**
- canonical mobility or migration framework [placeholder]
- empirical migration or intergenerational mobility paper [placeholder]
- frontier paper on place effects or mobility frictions [placeholder]

**Code lab opportunity:** map mobility or migration responses using public regional data.

---

### Week 11. Evaluating public policies targeting workers

**Central question:** How should economists evaluate policies that primarily affect worker constraints, incentives, and choices?

**Why here:** This is the worker-side policy capstone of the semester.

**Bridge:**
- worker-targeted vs. firm-targeted policy
- partial-equilibrium and equilibrium incidence intuition
- why policy evaluation requires both theory and design

**Field Core:**
- taxes, transfers, childcare, training, leave, search assistance, and take-up design
- policy margins: participation, hours, earnings, welfare, distribution
- matching policy question to empirical design

**Research Lab:**
- policy heterogeneity and external validity
- welfare measurement with multiple behavioral margins

**Reading ladder buckets:**
- canonical worker-policy evaluation paper [placeholder]
- quasi-experimental or experimental policy study [placeholder]
- frontier paper on take-up, salience, or heterogeneous effects [placeholder]

**Shared toolkit dependency:** identification primer

**Code lab opportunity:** build a replication-style note for one worker-targeted policy evaluation design.

---

### Week 12. Labor supply under frictions: information, attention, and behavioral responses

**Central question:** What happens to labor supply predictions when workers face information frictions or behavioral frictions?

**Why here:** This week deliberately relaxes the benchmark models developed earlier and connects Labor I to Behavioral Labor.

**Bridge:**
- incomplete information, complexity, inattention, present bias, and reference dependence
- why revealed choices may not map cleanly into standard welfare analysis

**Field Core:**
- labor supply under informational frictions
- behavioral labor supply and take-up behavior
- implications for policy design, elasticities, and welfare interpretation

**Research Lab:**
- salience, administrative burden, and take-up
- when behaviorally informed design changes policy conclusions

**Reading ladder buckets:**
- canonical information-friction or behavioral-friction paper [placeholder]
- empirical paper on take-up, salience, or complexity [placeholder]
- frontier behavioral labor application [placeholder]

**Code lab opportunity:** simulate policy take-up under attention or information frictions.

---

### Week 13. Synthesis and student research designs

**Central question:** How do the worker-side pieces of labor economics fit together, and where are the best open research opportunities?

**Why last:** This week converts the course from topic mastery into research capability.

**Bridge:**
- integrative review of the semester

**Field Core:**
- linking labor supply, human capital, inequality, policy, and frictions
- identifying a clean empirical or theoretical contribution

**Research Lab:**
- student research design memos or presentations
- replication extensions
- how Labor I sets up Labor II and Behavioral Labor

**Reading ladder buckets:**
- no new required readings; synthesis materials only

**Deliverable suggestion:** short research memo or structured proposal.

## Compression rules

### 10-week version

Merge the following pairs:
- Weeks 2 and 3: static and dynamic labor supply
- Weeks 4 and 5: human capital and wage determination
- Weeks 11 and 12: worker policy evaluation and labor supply frictions

Then choose whether Week 7 or Week 10 is partially integrated into another week, depending on instructor emphasis.

### 12-week version

Keep the full sequence, but condense one of the following pairs:
- Weeks 7 and 8 if inequality is the main emphasis
- Weeks 9 and 10 if discrimination and mobility are taught as linked allocation topics

### 14-week version

Add one or two extension weeks such as:
- employer learning and information revelation
- labor supply and social norms
- advanced household bargaining
- frontier workshop using a replication notebook

## Assessment ideas

Possible assessment mix:
- weekly reading or idea memos
- one short empirical design memo
- one replication or code exercise
- final research proposal or presentation

## Relationship to later courses

This course feeds directly into:
- **Labor II**, by providing worker-side foundations before firm-side equilibrium and institutions;
- **Behavioral Labor**, through Week 12 on informational and behavioral frictions;
- **Empirical Methods**, through repeated use of policy evaluation and identification logic.
