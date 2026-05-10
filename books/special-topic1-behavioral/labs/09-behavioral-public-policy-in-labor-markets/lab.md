# Code Lab 9: Behavioral Public Policy in Labor Markets

**Course:** Behavioral Labor  
**Module / Week:** Week 9 -- Behavioral Public Policy in Labor Markets  
**Associated chapter:** `09-behavioral-public-policy-in-labor-markets.md`  
**Lab slug:** `09-behavioral-public-policy-in-labor-markets`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@bhargavaManoli2015]  
**Secondary / challenge anchor:** [@chettyFriedmanSaez2013]  
**Optional extension anchor:** [@bernheimFradkinPopov2015] or [@kostolMyhre2021]  

## Why This Lab Exists

Week 9 asks how behavioral frictions change labor-policy design. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact take-up and reminder design inspired by [@bhargavaManoli2015].
2. **Diagnose** whether the policy is correcting a mistake, harnessing a regularity, reducing implementation burden, changing learning, or raising welfare ambiguity.
3. **Transfer** the same policy diagnostic to EITC knowledge, local labor-supply response, and retirement default design.

The lab does not require confidential tax, transfer, employer, UI, disability, or official replication data.

## Learning Objectives

By the end of the lab, students should be able to:

1. estimate treatment-effect summaries for salience, simplification, and assistance interventions;
2. summarize a duration-style take-up hazard;
3. distinguish information, salience, procedural support, trust, and administrative burden;
4. diagnose whether the main margin is claiming, labor-supply response, program enrollment, or welfare;
5. transfer a behavioral policy design to EITC knowledge and work-linked saving defaults;
6. state the welfare benchmark and likely intermediary response for a behavioral labor policy.

## Local Structure

```text
labs/09-behavioral-public-policy-in-labor-markets/
  lab.md
  smoke.sh
  src/
    build_week9_synthetic_data.py
    reproduce_takeup_design.py
    transfer_policy_diagnostics.py
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
conda run -n research python src/build_week9_synthetic_data.py

conda run -n research python src/reproduce_takeup_design.py \
  --worker-input original/reduced/benefit_takeup_synthetic.csv \
  --duration-input original/reduced/benefit_takeup_duration_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_policy_diagnostics.py \
  --eitc-input transfer/data/eitc_local_knowledge_synthetic.csv \
  --default-input transfer/data/retirement_default_welfare_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/takeup_policy_summary.csv`
- `output/reproduced/takeup_treatment_effects.csv`
- `output/reproduced/takeup_hazard_summary.csv`
- `output/reproduced/takeup_reproduction.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the policy tool: salience, simplification, assistance, trust support, or a bundle?
- What friction is the policy targeting?
- Is the policy correcting a mistake, harnessing a regularity, or reducing implementation burden?
- Is the main outcome a response to incentives or a take-up margin?
- What welfare benchmark would make the policy evaluation meaningful?

## Part II. Diagnose

Write a short policy-design memo with five paragraphs:

1. **Friction:** What behavioral friction or implementation barrier is being targeted?
2. **Role:** Is the friction a bias to correct, a lever to harness, an implementation constraint, a learning problem, an intermediary channel, or a welfare complication?
3. **Margin:** Which labor-policy margin moves: claiming, earnings response, search, training, saving, or work incentives?
4. **Method:** Which empirical method fits the design: field experiment, ANCOVA, hazard/timing model, panel/event study, local-knowledge comparison, default comparison, or welfare calibration?
5. **Welfare and equilibrium:** What benchmark action matters, and what intermediary could alter policy incidence?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/eitc_knowledge_summary.csv`
- `output/transfer/eitc_local_response_diagnostic.csv`
- `output/transfer/default_welfare_summary.csv`
- `output/transfer/policy_diagnostic_map.csv`
- `output/transfer/policy_transfer_diagnostics.png`
- `output/transfer/transfer_note.txt`

Use [@chettyFriedmanSaez2013] to interpret the EITC transfer. Does the local response look like a preference elasticity, schedule knowledge, salience, adjustment costs, or a composite?

Then use [@bernheimFradkinPopov2015] for the retirement-default transfer. Does a higher participation rate imply higher welfare? What benchmark contribution rate would you defend?

## Challenge

Propose one bounded transfer design:

- UI job-search support with reminders and reporting deadlines;
- training enrollment after displacement with simplified forms;
- disability work incentives with threshold-information treatments;
- EITC claiming with tax-preparer or neighborhood information;
- retirement saving with employer defaults and active choice.

For the chosen setting, state the targeted friction, policy role, labor margin, identifying variation, empirical method, welfare benchmark, and likely intermediary response.

## Deliverables Checklist

- [ ] run log
- [ ] take-up policy summary table
- [ ] treatment-effect table
- [ ] take-up hazard summary
- [ ] one-page policy-design memo
- [ ] EITC knowledge diagnostic
- [ ] default-welfare diagnostic
- [ ] short transfer paragraph naming the method and welfare limit
