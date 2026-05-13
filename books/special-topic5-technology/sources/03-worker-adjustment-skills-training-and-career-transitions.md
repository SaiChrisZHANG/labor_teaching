---
title: Worker Adjustment, Skills, Training, and Career Transitions
bibliography:
  - references.bib
---

# Week 3. Worker Adjustment, Skills, Training, and Career Transitions

## Opening orientation

Technology shocks do not stop at labor demand. Once tasks are displaced, augmented, or reorganized, workers must decide whether to remain in place, switch tasks, retrain, change occupations, or exit. A labor market can look resilient in aggregate while specific workers bear persistent earnings losses, mobility costs, or welfare declines. This lecture turns the course explicitly to the supply side and asks how skill accumulation, training systems, and career frictions mediate adjustment to technological change.

## Core points

:::{admonition} Core points
- Worker adjustment is central because technology changes the returns to existing skills and the value of acquiring new ones.
- Aggregate reallocation and individual incidence are not the same object: markets can reallocate even when some workers experience long-lasting losses.
- Training, major choice, track choice, and within-firm skill accumulation are all margins of technological adjustment, but they are measured with very different data and designs.
- Frontier empirical work in this area increasingly relies on admissions cutoffs, matched employer–employee panels, worker-level exposure measures, and training-linked administrative data.
- Frictions such as distrust, inertia, information failures, and switching costs can slow adjustment and amplify inequality.
:::

## Bridge

Week 2 studied how automation, AI, and other technologies shift labor demand. This week asks how workers respond after those shocks arrive. The focus is on the supply side: which workers move, retrain, or adapt; which workers remain stuck; and how researchers can distinguish efficient adjustment from unequal incidence.

## Field Core

### 1. A worker-adjustment framework

A useful labor-economics map begins with a technology shock that changes task prices or the composition of vacancies. Workers then face several adjustment margins:
1. **pre-market or early-career choice**, such as major, track, or occupation;
2. **within-job adaptation**, such as training, learning, or task reallocation;
3. **between-job or between-sector mobility**, such as occupational switching, geographic movement, or labor-force exit.

A simple way to discipline the lecture is to write worker value as:
```{math}
:label: eq:worker-value-tech
V_{it} = w_{it} - c(a_{it}) - \kappa(m_{it}) + E_t \sum_{s \ge t+1} \beta^{s-t} \, u_{is},
```
where {math}`a_{it}` denotes costly adjustment effort (training, coursework, search, learning), {math}`m_{it}` denotes mobility or switching, and technology changes both current wages and the future value of different adjustment strategies. The key research question is not only whether workers adjust, but **which margin** they use and **at what cost**.

### 2. Skill specificity, portability, and career transitions

Technology shocks differ in how they interact with existing human capital. Some shocks reward portable analytical or problem-solving skills. Others devalue occupation-specific or firm-specific task bundles. The worker-side literature therefore asks whether adjustment depends on:
- education level,
- field of study,
- occupational specificity,
- age or career stage,
- local training infrastructure,
- employer willingness to retrain.

Deming and Noray emphasize that career trajectories in STEM-intensive occupations involve rapid task obsolescence and repeated adjustment rather than static skill premia [@demingNoray2020]. Their framing is useful because it links technological change to a moving-skill frontier rather than a one-time treatment.

### 3. Training and retraining as adjustment margins

Training is one of the hardest adjustment margins to observe well. Firms may retrain incumbents, hire new workers with updated skills, or respond to shocks through early retirement instead of training. Bertermann’s recent work is especially useful here because it treats training and retirement as explicit adjustment responses to trade and technology shocks in German local labor markets [@bertermann2025]. Muehlemann’s firm-level evidence on AI adoption and workplace training adds a contemporary firm-side dimension: AI adoption may reduce continuing training for incumbents while shifting training toward newly hired workers [@muehlemann2024].

This immediately creates distributional questions:
- who receives training?
- who bears adjustment costs?
- are older or less-educated workers left behind?
- does technology-induced training narrow or widen inequality?

### 4. Early choices: majors, fields, and vocational tracks

A separate but related literature studies how workers prepare for technologically changing labor markets through educational choices. Here the main labor question is not whether a STEM or vocational path “pays,” but how access to these fields shapes long-run adaptation to changing skill demand.

A frontier design family uses centralized admissions or major cutoffs. Kirkebøen, Leuven, and Mogstad use regression discontinuity in secondary-school field assignment to estimate long-run returns to specific fields [@kirkeboenLeuvenMogstad2021]. Silliman uses centralized vocational-track admissions to estimate returns to vocational secondary education [@silliman2022]. Bleemer and Mehta provide a university-major RD example, showing how access to economics changes major choice and later earnings [@bleemerMehta2022]. These studies are not all “technology papers” narrowly defined, but they provide some of the best causal designs for asking how field choice shapes later exposure and resilience to technological change.

### 5. Matched worker–firm evidence on adaptation

Another major literature studies what happens when firms adopt technology and workers are observed before and after adoption. Genz shows that workers at adopting firms may experience greater employment stability and earnings growth if they remain with the firm, but that adaptation is heterogeneous and tied to within-firm reallocation [@genz2021]. Kogan et al. link patent-based labor-displacing technology exposure to worker outcomes using matched employer–employee data and show how worker-level incidence can differ from aggregate patterns [@koganPapanikolaouSchmidtSeegmiller2021].

These papers matter methodologically because they move beyond repeated cross-sections. They let researchers ask:
- who stays with adopting firms?
- who exits?
- which workers gain from within-firm adjustment?
- how much of measured adaptation is selection rather than treatment?

### 6. Frontier methods box: how researchers identify worker adjustment

:::{admonition} Methods box: frontier designs in worker-adjustment research
**Centralized admissions / cutoff RD**
- Field-of-study or track assignment at cutoffs can identify returns to specific educational paths that shape later technological exposure.
- Representative papers: [@kirkeboenLeuvenMogstad2021]; [@silliman2022]; [@bleemerMehta2022].

**Matched employer–employee event studies**
- Observe workers before and after firm adoption of a new technology, often with worker and firm fixed effects.
- Representative papers: [@genz2021]; [@koganPapanikolaouSchmidtSeegmiller2021].

**Local exposure designs linked to adjustment margins**
- Combine local robot/trade/technology exposure with administrative data on training, retirement, or occupational transitions.
- Representative paper: [@bertermann2025].

**Worker-level task or patent exposure measures**
- Build exposure at the worker or occupation level from patents, task content, or digital technology use, then link to administrative earnings or employment.
- Representative papers: [@koganPapanikolaouSchmidtSeegmiller2021]; [@almeidaDixCarneiro2025].

**Training and program evaluations**
- Evaluate retraining or apprenticeship programs as responses to new technology or structural change, usually with administrative linked earnings data or policy variation.
- This remains an underdeveloped but important design space.

**What good designs in this literature usually do**
- isolate the relevant adjustment margin clearly;
- distinguish treatment from sorting/selection;
- measure dynamic outcomes rather than only short-run employment;
- connect worker outcomes to technology exposure using a transparent mechanism.
:::

### 7. Frictions in worker adjustment and inequality

Adjustment is not frictionless. Workers may fail to retrain or switch even when doing so appears privately valuable. A useful way to organize the frontier is around four frictions:

1. **information frictions**: workers may not know which skills are newly rewarded;
2. **behavioral frictions**: inertia, limited memory, or distrust may slow adoption of new tools or training;
3. **financial frictions**: liquidity and time constraints make retraining costly;
4. **mobility/switching frictions**: occupational, geographic, and family constraints slow adjustment.

Recent work by Gertler et al. is helpful as a conceptual bridge because it shows how present bias, limited memory, and distrust can generate inertia in a managerial technology-adoption setting [@gertlerJohnsonVillarreal2025]. Even though the exact context is not “worker retraining after automation,” it illustrates a broader point highly relevant for this week: the uptake of productivity-improving technology or adjustment opportunities can be slowed by behavioral frictions. Once combined with unequal access to information, time, or training, these frictions can amplify inequality.

### 8. Research architecture: from technology shock to worker incidence

A useful research architecture for this literature is:
1. define the technology shock;
2. identify the relevant worker margin (major choice, training, within-firm learning, occupation switch, retirement, migration);
3. measure the technology exposure at the right level (worker, occupation, firm, region);
4. specify what counts as successful adjustment;
5. test whether frictions or unequal access explain differential adjustment.

This is the right place to ask frontier questions:
- when do firms retrain incumbents versus replace them?
- do AI tools lower or raise the private return to training for different workers?
- can distrust of AI or new digital systems slow worker adaptation?
- do policy-supported retraining systems attenuate inequality or mostly help already-advantaged workers?
- how much of “worker resilience” is really selection into good firms or good fields?

## Research Lab

### Primary anchor paper
A strong primary reproduction anchor for this week is **Kogan, Papanikolaou, Schmidt, and Seegmiller (2021)**, which links labor-displacing technology exposure from patents to worker-level outcomes [@koganPapanikolaouSchmidtSeegmiller2021].

### Reproduce
Recreate one reduced-form exposure-to-worker-outcome relationship using a bounded teaching dataset or simplified replication path. The goal is to understand how worker exposure is constructed and how worker incidence differs from occupational averages.

### Diagnose
Ask what the design is actually identifying:
- worker incidence or firm incidence?
- treatment or selection?
- short-run displacement or long-run adaptation?
- individual exposure or local equilibrium response?

### Transfer
Use the same research logic in a different setting:
- training or retirement responses to local technology exposure [@bertermann2025],
- within-firm adjustment after adoption [@genz2021],
- or the effects of AI adoption on incumbent versus new-hire training [@muehlemann2024].

## Reading Ladder And References

### Core framing
- Autor, “Why Are There Still So Many Jobs?” [@autor2015]
- Deming and Noray, “STEM Careers and Technological Change” [@demingNoray2020]

### Worker adjustment and training
- Genz, “How Do Workers Adjust When Firms Adopt New Technologies?” [@genz2021]
- Bertermann, “Training or Retiring? How Labor Markets Adjust to Trade and Technology Shocks” [@bertermann2025]
- Muehlemann, “AI Adoption and Workplace Training” [@muehlemann2024]

### Early choices and field design
- Kirkebøen, Leuven, and Mogstad, “Long-Run Returns to Field of Study in Secondary School” [@kirkeboenLeuvenMogstad2021]
- Silliman, “Labor Market Returns to Vocational Secondary Education” [@silliman2022]
- Bleemer and Mehta, “Will Studying Economics Make You Rich?” [@bleemerMehta2022]

### Exposure measurement and worker-level incidence
- Kogan, Papanikolaou, Schmidt, and Seegmiller, “Labor-displacing Technology Exposure from Patents” [@koganPapanikolaouSchmidtSeegmiller2021]
- Almeida, “Digital Technology and Worker Tasks” [@almeidaDixCarneiro2025]

### Frictions and adoption
- Gertler et al., “Inertia, Limited Memory, and Distrust in Technology Adoption” [@gertlerJohnsonVillarreal2025]

## Exercises And Discussion Prompts

1. Why can aggregate labor-market adjustment coexist with severe worker-level welfare losses?
2. Compare two identification strategies for worker adjustment: admissions cutoffs and matched employer–employee adoption event studies. What does each one identify better?
3. Why is training one of the hardest margins to measure well?
4. Under what conditions can behavioral frictions in adjustment amplify inequality after technology adoption?
5. Design a study that distinguishes worker retraining from worker replacement after AI adoption.

## Reproducibility And Code Lab Note

This week’s code lab should follow the standard **Reproduce → Diagnose → Transfer** structure. A good bounded teaching path would reproduce a worker-level exposure relation inspired by [@koganPapanikolaouSchmidtSeegmiller2021], diagnose what that exposure design identifies, and then transfer the logic to a training or retirement setting inspired by [@bertermann2025] or [@muehlemann2024].

## Slide Companion Note

The slide deck should emphasize:
- the worker-adjustment framework,
- the frontier methods box,
- the distinction between aggregate and individual adjustment,
- and the role of adjustment frictions in inequality.

## Bridge Forward

Week 4 moves inside firms and studies how hiring, management, training systems, and organizational structure respond to new technology. This week focused on worker-side adjustment; the next week asks how firms shape those margins from the inside.
