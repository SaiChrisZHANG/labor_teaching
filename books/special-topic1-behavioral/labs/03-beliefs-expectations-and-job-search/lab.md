# Code Lab 3: Beliefs, Expectations, and Job Search

**Course:** Behavioral Labor  
**Module / Week:** Week 3 -- Beliefs, Expectations, and Job Search  
**Associated chapter:** `03-beliefs-expectations-and-job-search.md`  
**Lab slug:** `03-beliefs-expectations-and-job-search`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@muellerSpinnewijnTopa2021]  
**Secondary / challenge anchor:** [@carranzaGarlickOrkinRankin2022]  
**Optional extension anchor:** [@belotKircherMuller2022]  

## Why This Lab Exists

Week 3 turns beliefs and information into applied job-search designs. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact Mueller-Spinnewijn-Topa-style factbook on subjective job-finding beliefs, realized exits, and duration dependence.
2. **Diagnose** whether belief patterns reflect prediction, optimism, weak updating, unobserved heterogeneity, or true duration dependence.
3. **Transfer** the same logic to a two-sided skill-certification design inspired by Carranza-Garlick-Orkin-Rankin.

The lab does not require confidential unemployment, platform, or employer microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small belief-duration factbook from local synthetic data;
2. compare subjective job-finding beliefs with model-predicted and realized exits;
3. explain why beliefs can be predictive but still weakly updated;
4. distinguish worker learning from firm learning in a certification design;
5. transfer the logic to perceived competition in wage-announcement settings.

## Local Structure

```text
labs/03-beliefs-expectations-and-job-search/
  lab.md
  smoke.sh
  src/
    build_week3_synthetic_data.py
    reproduce_beliefs_duration.py
    transfer_certification_search.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week3_synthetic_data.py

conda run -n research python src/reproduce_beliefs_duration.py \
  --input original/reduced/job_search_beliefs_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_certification_search.py \
  --certification-input transfer/data/skill_certification_synthetic.csv \
  --wage-input transfer/data/wage_signal_applications_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/belief_duration_summary.csv`
- `output/reproduced/belief_calibration_by_bin.csv`
- `output/reproduced/job_search_beliefs_duration.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the belief object: a subjective four-week job-finding probability, an expected wage, or a perceived competition measure?
- How does average belief change with unemployment duration?
- Are beliefs predictive of realized exits?
- What evidence would separate weak updating from true duration dependence in opportunities?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Benchmark:** What would a standard search model with correct beliefs predict about beliefs, reservation wages, and effort as duration rises?
2. **Behavioral object:** Is the plausible object optimism, weak updating, pessimism, or perceived returns to effort?
3. **Margin:** Which outcome is moved: applications, reservation wage, unemployment exit, or search-channel choice?
4. **Identification caution:** What unobserved heterogeneity or standard search friction could generate a similar pattern?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/certification_summary.csv`
- `output/transfer/certification_effects.csv`
- `output/transfer/certification_search.png`
- `output/transfer/wage_signal_summary.csv`
- `output/transfer/transfer_note.txt`

Use [@carranzaGarlickOrkinRankin2022] to classify the certification design. State who learns what: the worker, the firm, or both. Then use the wage-signal summary to classify the optional [@belotKircherMuller2022] extension: did applications respond as if the wage were only a payoff, or also as a perceived-competition signal?

## Challenge

Propose a bounded transfer design for one new search setting:

- belief elicitation about remote-work job finding;
- certification for a technical skill in an entry-level hiring market;
- wage or quality signals on an online vacancy platform.

For the chosen setting, state the belief or information object, the search margin, the identifying variation, and the main standard alternative.

## Deliverables Checklist

- [ ] run log
- [ ] belief-duration summary table
- [ ] belief calibration table
- [ ] reproduction figure
- [ ] one-page diagnosis memo
- [ ] certification transfer figure and tables
- [ ] short paragraph on wage signals and perceived competition
