# Code Lab 5: Social Norms, Bargaining, And Institutions Shaping Gendered Work

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 5 -- Social norms, bargaining, and institutions shaping gendered work  
**Associated chapter:** `05-social-norms-bargaining-and-institutions-shaping-gendered-work.md`  
**Lab slug:** `05-social-norms-bargaining-and-institutions-shaping-gendered-work`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@bursztynGonzalezYanagizawaDrott2020misperceivedSocialNorms]  
**Secondary / challenge anchor:** [@bertrandKamenicaPan2015genderIdentityRelativeIncome]  
**Optional extension anchor:** [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount] or [@leBarbanchonRathelotRoulet2021commuteWageTradeoff]  

## Why This Lab Exists

Week 5 teaches students to make norms empirically concrete. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a norm-misperception information exercise where beliefs about social approval affect job-search behavior.
2. **Diagnose** whether each output speaks to beliefs, sanctions, bargaining, search, or selection.
3. **Transfer** the same discipline to a relative-income household exercise where a breadwinner norm may affect labor supply and home production.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential survey, household, or job-search microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce grouped summaries for a norm-misperception intervention;
2. distinguish a belief-about-acceptability channel from a wage, law, or selection channel;
3. state the identifying variation and observed labor margin in an information intervention;
4. transfer the same logic to a household relative-income threshold setting;
5. explain what extra data would be needed to separate identity, bargaining, and selection.

## Local Structure

```text
labs/05-social-norms-bargaining-and-institutions-shaping-gendered-work/
  lab.md
  smoke.sh
  src/
    build_week5_synthetic_data.py
    reproduce_norm_misperceptions.py
    transfer_relative_income.py
  original/
    reduced/
  transfer/
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week5_synthetic_data.py

conda run -n research python src/reproduce_norm_misperceptions.py \
  --input original/reduced/bursztyn_norm_misperceptions_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_relative_income.py \
  --input transfer/data/bertrand_relative_income_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/norm_information_balance.csv`
- `output/reproduced/job_search_effects.csv`
- `output/reproduced/mechanism_diagnostics.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the source of identifying variation?
- What is the observed labor margin: beliefs, job-matching sign-up, follow-up search, or employment?
- Does the design identify a wage effect or a legal-rights effect?
- What data would be needed to distinguish private support, perceived community approval, and household bargaining?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** State whether the design measures a norm, price, legal institution, bargaining channel, or selection.
2. **Variation:** State the information comparison and why it is useful.
3. **Margin:** State the outcomes observed and why they are job-search margins.
4. **Limitation:** State why a belief update is not automatically evidence on long-run employment, wages, or household allocation.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/relative_income_distribution.csv`
- `output/transfer/threshold_diagnostics.csv`
- `output/transfer/transfer_note.txt`

Use the synthetic relative-income exercise inspired by [@bertrandKamenicaPan2015genderIdentityRelativeIncome] to explain why a threshold pattern near equal earnings is a different empirical object from an information intervention. State the observed margin, the comparison near the threshold, and what would be needed to distinguish identity, bargaining, and selection.

## Optional Frontier Prompt

Choose one extension:

- Use financial-control evidence [@fieldPandeRigolSchanerTroyerMoore2021onHerOwnAccount] to ask whether formal account design changes labor supply by shifting control over earnings and threat points.
- Use commuting evidence [@leBarbanchonRathelotRoulet2021commuteWageTradeoff] to ask whether gender differences in job search reflect wages, safety, mobility norms, household bargaining, or acceptable-job constraints.

Do not estimate either extension in the bounded path. State the treatment, comparison group, observed labor margin, and main threat to interpretation.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced norm-information summaries
- [ ] one-page design memo
- [ ] relative-income transfer summaries
- [ ] paragraph distinguishing belief interventions from threshold evidence
- [ ] optional financial-control or commuting prompt
