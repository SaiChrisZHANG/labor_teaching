# Firms, Hiring, Management, And Organizational Response To New Technology

## Learning Objectives

By the end of Week 4, students should be able to:

1. explain why technology adoption is a firm-level labor-demand event rather than a simple purchase of capital or software;
2. distinguish acquisition, implementation, usage, and organizational redesign as separate empirical objects;
3. analyze how AI can substitute for tasks, augment worker productivity, and change delegation, supervision, and performance evaluation;
4. connect technology adoption to hiring, screening, training, internal reallocation, promotion ladders, and job design;
5. explain how employee and manager attitudes toward AI can affect adoption, usage, productivity, resistance, and inequality;
6. compare frontier designs for measuring AI-adoption attitudes while separating technology adoption from technology sentiment.

The central firm-side question is this: when a firm adopts a new technology, how does it reorganize labor demand, hiring, supervision, internal labor markets, and job design around that technology, and why do attitudes toward AI shape the realized effect?

## Opening Orientation

Week 4 moves inside the firm. Week 2 studied automation and AI as labor-demand shocks; Week 3 studied worker adjustment after task prices and career risks move. This week asks how those changes are implemented through firms. A technology becomes a labor-market force when managers decide which tasks to automate, which workers to augment, which jobs to redesign, which vacancies to post, which incumbents to train, how closely to monitor workers, and whether to delegate decisions to algorithms.

The week is not a generic management lecture. The labor objects are vacancies, task assignments, hiring standards, skill demand, internal mobility, promotion systems, supervision, worker voice, job quality, and wage incidence. Firm adoption matters because the same technology can produce different labor outcomes depending on organizational complements, workforce composition, management beliefs, worker acceptance, and principal-agent conflicts.

AI makes the firm interior especially important. It can act as a labor-demand shock by reducing demand for some tasks, as an augmentation technology by raising worker productivity in other tasks, and as an organizational technology by changing who decides, who is monitored, and how performance is evaluated. Its realized effect therefore depends not only on technical capability, but also on adoption costs, complementary investments, trust, delegation, and resistance.

:::{admonition} Core points
:class: important

- Technology adoption is an organizational choice. Firms usually need complementary investments in data, workflow redesign, management practices, worker training, incentives, and monitoring.
- AI can substitute for tasks, augment workers, and reallocate authority between workers, managers, and algorithms.
- Firm adoption changes labor demand through hiring, screening, training, internal reallocation, job redesign, supervision, promotion ladders, and contracting.
- AI creates principal-agent problems because firms, managers, and workers may value speed, control, privacy, fairness, autonomy, job security, and output quality differently.
- Worker and manager attitudes toward AI are not side issues. Acceptance, distrust, perceived fairness, transparency, and algorithm aversion can affect measured adoption, realized usage, productivity gains, and inequality.
- A credible empirical design separates technology availability, adoption, actual use, attitudes, organizational redesign, and worker outcomes.

:::

## Bridge

The course now connects three layers. Week 1 supplied the task-based vocabulary. Week 2 studied how automation and AI shift labor demand across tasks, firms, occupations, and places. Week 3 studied how workers respond through skills, training, mobility, and career transitions. Week 4 adds the implementation layer: firms mediate the relationship between technology and labor outcomes.

This layer is essential because exposure is not adoption, adoption is not usage, and usage is not necessarily successful reorganization. A firm may have technically automatable tasks but choose not to adopt. It may adopt a tool but leave workflows unchanged. It may train new hires while bypassing incumbents. It may use AI for prediction, monitoring, scheduling, hiring, or documentation, each of which changes a different labor object. The empirical challenge is to identify which of those margins the data actually measure.

The week also carries forward the worker-adjustment lesson from Week 3. Whether workers can adjust depends partly on firm choices: access to training, task reassignment, internal job ladders, managerial trust, transparent evaluation, and credible commitments about how AI will be used.

## Field Core

### Firm Adoption As Labor-Demand Implementation

Technology adoption is not a single event. A useful labor-economics sequence separates four margins:

1. **acquisition**, when the firm buys, builds, licenses, or hires for a technology;
2. **implementation**, when the firm changes workflows, data systems, jobs, and incentives;
3. **usage**, when workers or managers actually rely on the technology in production or decision-making;
4. **organizational redesign**, when the technology changes hiring, supervision, delegation, internal mobility, or promotion.

The difference matters empirically. A resume-based AI investment measure, a vacancy asking for machine-learning skills, a survey response about AI adoption, and worker-level software telemetry are not the same treatment. They sit at different points in the adoption chain.

```{include} assets/tables/04-firm-adoption-and-organization-map.md
```

The core adoption problem can be written as a firm comparing expected value with and without reorganization:

```{math}
:label: eq:st5-w4-firm-adoption
Adopt_{ft}=1
\left[
E_t\left(\Pi_{ft}^{AI}(K_{ft}^{O}, H_{ft}, M_{ft}, A_{ft})\right)
- \Pi_{ft}^{0}
- C_{ft}^{adopt}
- C_{ft}^{org}
> 0
\right],
```

where {math}`K_{ft}^{O}` is organizational capital, {math}`H_{ft}` is workforce skill and hierarchy, {math}`M_{ft}` is management practice, {math}`A_{ft}` captures worker and manager acceptance or resistance, {math}`C_{ft}^{adopt}` is the direct adoption cost, and {math}`C_{ft}^{org}` is the cost of redesigning work. Equation {eq}`eq:st5-w4-firm-adoption` is not meant to be estimated literally. It disciplines interpretation: adoption depends on complements, not only on the price of the tool.

This logic is familiar from information technology and workplace organization. IT raised productivity most when paired with worker skills and organizational redesign [@bresnahanBrynjolfssonHitt2002ITWorkplace; @bartelIchniowskiShaw2007ITProductivity]. Cross-country and multinational evidence also shows that management practices shape the productivity returns to IT [@bloomSadunVanReenen2012AmericansIT]. AI should be read in that tradition, with one additional feature: it can enter not only production, but also prediction, evaluation, delegation, and supervision.

### Complementary Investments And Adoption Costs

Complementary investments are the reason AI adoption can be slow, uneven, and firm-specific. Firms need usable data, workflow integration, worker training, legal and compliance routines, cybersecurity, managerial attention, and systems for evaluating output quality. They may also need to rewrite job descriptions, adjust teams, change review protocols, renegotiate implicit contracts, or redesign promotion ladders.

These costs make early adopters selected. Firms that adopt AI earlier may be larger, more productive, more skill-intensive, better managed, or already growing. Babina, Fedyk, He, and Hodson use worker resume and job-posting data to measure firm AI investments and show that AI-investing firms reorganize workforce composition toward more educated, STEM, IT, and junior individual-contributor roles [@babinaFedykHeHodson2023AIWorkforce]. Aghion, Bunel, Jaravel, Mikaelsen, Roulet, and Sogaard use French firm-level AI adoption data to show that adopters are larger, more productive, and more skill-intensive, and that labor-demand effects vary by use case [@aghionBunelJaravelMikaelsenRouletSogaard2025].

For labor economists, the implication is that adoption estimates are rarely pure technology effects. They combine technology with firm capability, management quality, workforce composition, and adoption timing. The object may be "the effect of adopting AI among firms capable of adopting early," not "the effect of AI on a random firm."

### Job Redesign And Task Reassignment

After adoption, the firm has to decide how tasks are rebundled into jobs. Some tasks may be automated away. Other tasks may become more productive because AI reduces search, drafting, prediction, coding, classification, or documentation costs. Still others may become more important because workers must validate outputs, manage exceptions, communicate with customers, maintain systems, or coordinate across teams.

A compact decomposition of firm labor demand is:

```{math}
:label: eq:st5-w4-firm-labor-demand
\Delta L_f =
\Delta L_f^{sub}
+ \Delta L_f^{aug}
+ \Delta L_f^{scale}
+ \Delta L_f^{org},
```

where {math}`\Delta L_f^{sub}` is task substitution, {math}`\Delta L_f^{aug}` is productivity augmentation in worker-performed tasks, {math}`\Delta L_f^{scale}` is output expansion, and {math}`\Delta L_f^{org}` is the labor-demand effect of changing hierarchy, monitoring, teams, and job boundaries. This decomposition is useful because firms can automate a task and still increase employment if productivity and scale effects dominate. They can also raise average wages while leaving incumbents worse off if the workforce is recomposed toward higher-skill hires.

AI is especially likely to change job boundaries rather than replacing whole occupations one for one. Evidence from generative-AI field and online experiments shows that AI can raise productivity in some tasks and change the distribution of performance within teams [@brynjolfssonLiRaymond2025GenerativeAI; @dellAcquaEtAl2026JaggedFrontier]. The firm-level question is what happens after the experiment: which tasks become routine expectations, which workers are trusted with the tool, which tasks require verification, and which jobs are redesigned.

### Hiring And Screening For New Tasks

Hiring is often the first visible labor response to adoption. Firms may post vacancies for AI engineers, data scientists, product managers, compliance specialists, prompt and workflow designers, or domain experts who can use AI tools. They may also raise screening standards for ordinary roles if the redesigned job requires more autonomy, digital fluency, problem-solving, or ability to audit machine output.

Vacancies and resumes are therefore useful but incomplete measures. A vacancy reveals desired skill demand, not realized employment or incumbent welfare. A resume-based measure can capture firm AI investment and workforce composition, but it may miss software purchased without AI-specialized hiring. A firm survey can capture adoption directly, but it may not observe intensity of use or job redesign.

The main labor distinction is whether firms **train incumbents** or **hire around them**. If adoption leads firms to fill new tasks through external hiring, average firm skill intensity can rise while exposed incumbent workers lose task share, promotion prospects, or bargaining power. If adoption is paired with incumbent retraining and internal mobility, the same technology can support adjustment inside the firm. Evidence on AI adoption and workplace training shows why incumbent training, new-hire training, and firm reorganization must be separated [@muehlemann2024].

### Training, Internal Reallocation, And Promotion

Internal labor markets turn technology adoption into a dynamic career problem. Firms decide which workers receive training, which workers are reassigned, which workers become AI-augmented specialists, and which workers are screened out of new internal ladders. A tool that looks productivity-enhancing at the task level may still reduce promotion prospects for workers whose old monitoring, coordination, or routine analytical tasks become less valuable.

Three margins are especially important:

1. **training allocation**, because firms may train high-potential workers and leave the most exposed workers behind;
2. **internal reallocation**, because workers may move across teams before separations appear in administrative data;
3. **promotion redesign**, because AI can flatten hierarchy, expand span of control, or shift authority toward individual contributors.

Babina, Fedyk, He, and Hodson's evidence on workforce composition and hierarchy is useful here because it treats AI investment as associated with organizational change, not merely a new input [@babinaFedykHeHodson2023AIWorkforce]. The key teaching point is that "upskilling" is not automatically an incumbent benefit. It can mean retraining current workers, hiring a different workforce, or changing promotion criteria so that old firm-specific experience carries less value.

### Supervision, Monitoring, And Algorithmic Management

Technology also changes supervision. Digital systems can lower the cost of observing effort, output, location, response time, customer ratings, coding activity, or adherence to protocols. Better monitoring can reduce moral hazard and improve firm performance, but it can also shift risk to workers, reduce autonomy, intensify work, and create incentives to game measured outcomes.

The principal-agent logic is straightforward. Let output depend on worker effort {math}`e_i`, task assignment {math}`q_i`, and monitoring precision {math}`m_f`. A monitoring technology can raise {math}`m_f`, letting the firm write contracts closer to observed performance. But if the measure is noisy, incomplete, or contested, workers may bear more risk or focus on measured tasks at the expense of unmeasured quality.

Kelley, Lane, and Schonholzer provide a useful labor-adjacent example: randomized access to monitoring data changes contracts, effort, risk-taking, profitability, and possible firm expansion in Kenyan public transit [@kelleyLaneSchonholzer2024]. The same principal-agent logic appears in algorithmic management: software can allocate shifts, rank workers, route tasks, trigger discipline, or set pay-relevant performance measures.

Platform-style labor markets are the boundary case. Online hiring intermediaries and ride-hailing platforms change matching, information, flexibility, monitoring, and the boundary between employment and contracting [@stantonThomas2016OnlineHiring; @chenChevalierRossiOehlsen2019FlexibleWork]. For Week 4, platforms matter because they show how technology can become a labor-market institution: the algorithm is not only a production input, but a governance system.

### AI As Substitution, Augmentation, And Delegation

AI should be analyzed as three objects at once.

First, AI can **substitute** for tasks or roles. This is the Week 2 displacement logic. Administrative processing, routine classification, first-draft writing, simple customer support, and some coding tasks may require less labor when AI systems perform them cheaply.

Second, AI can **augment** workers. It can reduce search costs, draft text, summarize information, generate code, standardize quality, or support decision-making. Augmentation can raise productivity without lowering employment if output expands or if workers take on more complex tasks.

Third, AI can **reallocate delegation and control**. A firm can ask workers to follow AI recommendations, ask managers to override AI only in exceptional cases, ask algorithms to screen candidates, or ask workers to use AI under managerial review. This changes authority even if headcount does not change.

The delegation margin is where principal-agent problems become sharp. Firms may value speed, standardization, documentation, and monitoring. Managers may value discretion, status, liability protection, or control. Workers may value autonomy, privacy, fair evaluation, and job security. These objectives can diverge, so adoption is partly a conflict over who controls the production process and who bears the risk of mistakes.

### Worker And Manager Attitudes Toward AI Adoption

Attitudes toward AI are a substantive adoption friction, not a soft afterthought. A technically useful tool can fail to raise productivity if workers do not trust it, if managers refuse to delegate to it, or if both sides anticipate unfair evaluation or job loss.

Workers may resist AI because they fear displacement, deskilling, surveillance, biased evaluation, opaque performance metrics, or loss of control. Some resistance can be rational. If workers expect the firm to use AI gains to reduce headcount, intensify monitoring, or weaken promotion prospects, low acceptance is an economic response to expected incidence. Resistance can also reduce beneficial adoption if workers underestimate augmentation benefits or lack credible training.

Managers face a different attitude problem. They may distrust algorithmic recommendations, overestimate their own judgment, fear liability, or resist delegation because it reduces discretion and status. Dargnies, Hakimov, and Kubler study algorithm aversion in hiring with worker and manager roles; their design is useful because it shows that both sides of the labor market can have preferences over human versus algorithmic decision-making, and that transparency or performance feedback may change acceptance differently [@dargniesEtAl2026].

Fairness, transparency, and control are central. Bansak and Paulson use a large conjoint experiment to study preferences over algorithmic and human decision-makers in high-stakes contexts, showing how performance and fairness attributes can shape attitudes toward decision authority [@bansakEtAl2024]. In firms, these attitudes affect hiring, evaluation, promotion, scheduling, monitoring, and grievance processes.

Attitudes also affect measurement. A survey response that a worker "uses AI" may reflect access, informal experimentation, managerial pressure, or genuine belief that the tool helps. A manager's report of AI adoption may reflect aspiration, compliance language, or real workflow redesign. Worker-level usage logs can show intensity of use but not whether usage is voluntary, trusted, resented, or productivity-enhancing.

Finally, attitudes can contribute to inequality within and across firms. Better-managed firms may pair AI with training, transparency, and credible protections, producing higher usage and larger productivity gains. Lower-trust firms may adopt superficially or use AI mainly for monitoring. High-skill workers may receive augmentation while lower-skill workers face surveillance or substitution. Worker sentiment, manager beliefs, and organizational trust can therefore amplify differences in firm productivity, wages, retention, and internal mobility [@bickBlandinDeming2024; @mcelheranYangKroffBrynjolfsson2025].

```{include} assets/tables/04-ai-attitudes-and-principal-agent-map.md
```

### Research Architecture For Firm Adoption

A disciplined Week 4 paper should name six objects:

1. **technology margin**, such as robots, software, generative AI, predictive AI, monitoring technology, or algorithmic hiring;
2. **adoption measure**, such as survey adoption, AI-skilled hiring, vendor records, internal rollout, vacancies, usage logs, or worker reports;
3. **organizational margin**, such as job redesign, hiring, training, monitoring, delegation, promotion, or internal mobility;
4. **attitude measure**, such as trust, fairness perceptions, transparency, control, algorithm aversion, or manager willingness to delegate;
5. **worker outcome**, such as wages, employment, separations, productivity, promotion, autonomy, schedule quality, or job satisfaction;
6. **counterfactual**, such as nonadopting firms, later-treated teams, nonexposed workers inside the same firm, or pre-adoption worker trajectories.

This architecture keeps the lecture labor-focused. The goal is not to say whether AI is good management. The goal is to identify how firms reorganize labor demand and how workers experience the changed allocation of tasks, authority, risk, and reward.

## Research Lab

The Week 4 research lab follows **Reproduce -> Diagnose -> Transfer**.

The primary anchor is Babina, Fedyk, He, and Hodson's firm-level AI investment and workforce-composition design [@babinaFedykHeHodson2023AIWorkforce]. It is the best anchor for this week because it ties AI adoption to labor composition, hierarchy, job postings, and organizational response. The challenge paper is Dargnies, Hakimov, and Kubler on algorithm aversion in hiring [@dargniesEtAl2026]. A useful empirical extension is Aghion, Bunel, Jaravel, Mikaelsen, Roulet, and Sogaard's firm-level AI adoption evidence from France, especially because it separates labor-demand responses by AI use case [@aghionBunelJaravelMikaelsenRouletSogaard2025].

The lab should not claim to replicate official estimates unless the needed data and code are locally available. No official Babina et al. resume or job-posting microdata, no confidential firm administrative data, and no Dargnies et al. experimental files are bundled in this repository. The teaching path should use deterministic synthetic data to practice the design logic.

**Reproduce.** Students build a synthetic firm panel with pre-adoption skill intensity, AI-skilled hiring, job postings, hierarchy shares, employment, and adoption timing. They reproduce the structure of a firm-adoption result: adopters are selected on baseline skill and size, and post-adoption workforce composition shifts toward AI-complementary roles. The goal is to reproduce the design logic, not published magnitudes.

**Diagnose.** Students diagnose what the adoption coefficient means. They test for pre-trends, compare acquisition with usage, separate hiring from incumbent training, and ask whether composition changes imply worker gains or worker replacement. They classify mechanisms into substitution, augmentation, scale, and organizational redesign.

**Transfer.** Students add a worker and manager attitude module inspired by the algorithm-aversion evidence. They design a vignette or randomized encouragement that varies transparency, human override, replacement risk, performance feedback, and monitoring intensity. The transfer exercise asks whether attitudes predict actual usage and whether usage predicts productivity after conditioning on baseline productivity and job task mix.

## Methods Box

```{include} assets/tables/04-frontier-methods-box.md
```

:::{admonition} Methods Box: Measuring Adoption Attitudes Without Confusing Sentiment With Technology
:class: note

**Worker surveys linked to outcomes.** These designs measure trust, fear of replacement, perceived fairness, transparency, control, willingness to use AI, and actual self-reported use, then link responses to productivity, retention, training, mobility, or wages. They identify associations between attitudes and outcomes, or causal effects only if attitude variation is experimentally induced or plausibly exogenous. They cannot by themselves separate low trust from low tool quality because workers may dislike AI after observing that it performs poorly in their job.

**Management surveys linked to firm administrative data.** These designs measure manager beliefs about AI productivity, delegation, hiring needs, adoption barriers, monitoring value, and worker resistance, then link responses to sales, employment, vacancies, training, turnover, or productivity. They are strong for measuring expectations and implementation strategy. They are weak for causal inference if optimistic managers are also better managers or if high-productivity firms can afford more experimentation.

**Randomized pilots and staggered rollouts inside firms.** These designs compare workers, teams, sites, or managers that receive access earlier versus later. They can identify the short-run effect of access or encouragement on usage, productivity, quality, and attitudes. They usually cannot identify long-run equilibrium redesign unless the rollout changes hiring, promotion, and team structure over a longer horizon.

**Survey experiments, vignette experiments, and conjoint designs.** These designs vary transparency, fairness information, human override, monitoring intensity, replacement risk, data use, or performance metrics. They identify which features change acceptance of AI-mediated hiring, evaluation, scheduling, or supervision. They cannot show whether stated preferences translate into workplace behavior unless linked to actual choices.

**Lab or online experiments eliciting delegation to algorithms.** These designs ask workers or managers to choose between human and algorithmic decision-makers, or to decide whether to delegate a hiring, screening, prediction, or evaluation task. They identify algorithm aversion, algorithm appreciation, overconfidence, and response to feedback. Their limitation is external validity: stakes, employment relationships, and institutional protections may differ from real firms.

**Matched employer-employee panels around adoption timing.** These designs observe workers before and after firm adoption and can estimate changes in wages, separations, promotions, training, or internal moves. If linked to attitude surveys, they can study heterogeneity by trust or perceived fairness. The main threat is adopter selection and differential pre-trends: attitudes may proxy for firm quality or for workers already on different career paths.

**Job-posting and vacancy text linked to adoption.** These designs measure changes in demand for AI skills, oversight tasks, monitoring roles, compliance roles, or human-AI collaboration. They identify intended labor demand, not realized usage or sentiment. They should be paired with employment, training, or worker outcomes before making welfare claims.

**Worker-level usage logs and software telemetry.** These designs measure actual use: prompts, sessions, task categories, acceptance of recommendations, edits, overrides, and timing. They are close to realized implementation. They still cannot identify attitudes unless paired with surveys or experiments, and they can confound productivity with compliance if workers use the tool because managers require it.

A good design separates four objects: technology adoption, technology use, technology sentiment, and productivity effects. Attitudes are confounded with productivity when workers or managers form beliefs after observing tool quality, when high-productivity firms communicate adoption better, or when workers who benefit from AI become more favorable toward it. The strongest designs measure baseline attitudes before adoption, randomize access or information when possible, observe actual usage, and follow worker and firm outcomes long enough to see organizational redesign.

:::

## Reading Ladder And References

```{include} assets/tables/04-reading-and-lab-map.md
```

**Core task and organizational frame.** Start with Autor, Levy, and Murnane for the task framework and Acemoglu-Restrepo for substitution, augmentation, and new tasks [@autorLevyMurnane2003SkillContent; @acemogluRestrepo2019AutomationNewTasks]. Add Bresnahan-Brynjolfsson-Hitt, Bartel-Ichniowski-Shaw, and Bloom-Sadun-Van Reenen to see why technology often requires workplace reorganization and management complements [@bresnahanBrynjolfssonHitt2002ITWorkplace; @bartelIchniowskiShaw2007ITProductivity; @bloomSadunVanReenen2012AmericansIT].

**Firm AI adoption and labor demand.** Read Babina, Fedyk, He, and Hodson as the primary firm-organization anchor [@babinaFedykHeHodson2023AIWorkforce]. Read Aghion, Bunel, Jaravel, Mikaelsen, Roulet, and Sogaard for firm-level AI adoption and heterogeneous labor-demand effects by use case [@aghionBunelJaravelMikaelsenRouletSogaard2025]. Use McElheran, Yang, Kroff, and Brynjolfsson to connect industrial AI adoption to adjustment costs and productivity J-curve dynamics [@mcelheranYangKroffBrynjolfsson2025].

**Worker use, training, and augmentation.** Use Brynjolfsson, Li, and Raymond and Dell'Acqua et al. to understand worker-level productivity and augmentation evidence [@brynjolfssonLiRaymond2025GenerativeAI; @dellAcquaEtAl2026JaggedFrontier]. Use Muehlemann to connect AI adoption to workplace training and the distinction between incumbent adaptation and new-hire skill demand [@muehlemann2024].

**Monitoring, platforms, and algorithmic control.** Read Kelley, Lane, and Schonholzer for a field experiment on monitoring technology and principal-agent problems [@kelleyLaneSchonholzer2024]. Use Stanton-Thomas and Chen-Chevalier-Rossi-Oehlsen to connect digital platforms to matching, contracting, flexibility, and worker-side labor supply [@stantonThomas2016OnlineHiring; @chenChevalierRossiOehlsen2019FlexibleWork].

**Attitudes, delegation, and algorithm aversion.** Read Dargnies, Hakimov, and Kubler for worker and manager aversion to hiring algorithms [@dargniesEtAl2026]. Use Bansak and Paulson for survey-experimental evidence on preferences over algorithmic and human decision-makers [@bansakEtAl2024]. Use Bick, Blandin, and Deming as a worker-use measurement benchmark for generative AI adoption [@bickBlandinDeming2024].

## Exercises And Discussion Prompts

1. Pick a firm adopting generative AI. Separate acquisition, implementation, usage, and organizational redesign. Which labor outcomes would each margin affect?
2. Give an example in which AI substitutes for one task but increases firm employment through augmentation or scale effects.
3. Suppose AI-investing firms become more educated and more junior over time. Give three interpretations, including at least one that is bad for incumbents.
4. Design a study that separates external hiring from incumbent retraining after AI adoption. What data would you need?
5. How can a monitoring technology improve productivity while reducing worker welfare? Name the principal-agent mechanism.
6. Design a vignette or conjoint experiment on AI evaluation at work. Which attributes would you vary to identify fairness, transparency, control, and replacement concerns?
7. Explain how manager overconfidence or algorithm aversion can reduce the measured productivity gains from AI.
8. How could worker and manager attitudes toward AI widen inequality within firms? How could they widen inequality across firms?

## Reproducibility And Code Lab Note

The Week 4 code lab lives at `labs/04-firms-hiring-management-and-organizational-response-to-new-technology/`. It is a bounded synthetic teaching path that implements the Week 4 **Reproduce -> Diagnose -> Transfer** workflow. The smoke test constructs a firm AI-adoption panel, generates workforce-composition and hierarchy outcomes, adds worker and manager attitude measures, and writes compact outputs that separate adoption, usage, sentiment, productivity, and principal-agent tensions. It requires no proprietary resume data, confidential employer-employee records, vendor telemetry, external downloads, or official replication materials.

## Slide Companion Note

The Week 4 slide deck lives at `slides/week4/04-firms-hiring-management-and-organizational-response-to-new-technology.tex`. The deck does not duplicate the chapter. It defines the firm-side question, shows the adoption-implementation-usage-redesign map, isolates substitution versus augmentation versus delegation, includes slides on internal labor markets, principal-agent problems, AI attitudes and algorithm aversion, and frontier methods, and closes with the Reproduce -> Diagnose -> Transfer lab design.

## Bridge Forward

Week 5 moves from the firm interior to equilibrium distribution. Week 4 showed that technology adoption is implemented through jobs, managers, training, monitoring, hiring, and attitudes. Week 5 asks how those firm-level choices aggregate into inequality, rents, market structure, labor-market power, institutions, and worker welfare. The bridge is direct: if better-managed firms adopt AI more effectively and if high-skill workers capture more augmentation while low-skill workers face monitoring or substitution, then firm adoption becomes a mechanism for economy-wide inequality.
