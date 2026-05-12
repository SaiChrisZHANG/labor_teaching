# Code Lab 8: Comparative And Global Gender In Labor-Market Development

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 8 -- Comparative and global gender in labor-market development  
**Associated chapter:** `08-comparative-and-global-gender-in-labor-market-development.md`  
**Lab slug:** `08-comparative-and-global-gender-in-labor-market-development`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@olivettiPetrongolo2017]  
**Secondary / challenge anchor:** [@jayachandran2021social]  
**Optional extension anchor:** [@goldbergGottliebLallMehta2025ggdi]

## Why This Lab Exists

Week 8 asks students to use comparative evidence without turning the lecture into a country tour. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** compact comparative family-policy summaries inspired by [@olivettiPetrongolo2017].
2. **Diagnose** which variables are labor-supply mechanisms, labor-demand mechanisms, care infrastructure, legal regime, formality, mobility, norms, outcomes, or transportability conditions.
3. **Transfer** the framework to norms-and-development settings inspired by [@jayachandran2021social].

The lab is a teaching analog. It is not an official replication and does not require restricted cross-country microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce comparative policy and regime summaries from synthetic country-year data;
2. distinguish portable mechanisms from setting-specific institutional detail;
3. separate internal validity, transportability, external validity, and policy transferability;
4. transfer a care-policy mechanism to settings where norms, mobility, informality, and service-sector demand differ;
5. write a short country-specific evidence pitch that leads with the labor mechanism rather than the country label.

## Local Structure

```text
labs/08-comparative-and-global-gender-in-labor-market-development/
  lab.md
  smoke.sh
  src/
    build_week8_synthetic_data.py
    reproduce_comparative_family_policy.py
    transfer_norms_development.py
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
conda run -n research python src/build_week8_synthetic_data.py

conda run -n research python src/reproduce_comparative_family_policy.py \
  --input original/reduced/olivetti_petrongolo_family_policy_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_norms_development.py \
  --input transfer/data/jayachandran_norms_transfer_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/comparative_policy_summary.csv`
- `output/reproduced/regime_type_summary.csv`
- `output/reproduced/mechanism_diagnostics.csv`
- `output/reproduced/transportability_matrix.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which labor margins move across regimes: participation, hours, continuity, or wage gaps?
- Which variables look like care infrastructure, labor demand, legal regime, formality, norms, mobility, or public employment?
- Which mechanism appears portable?
- Which setting details limit policy transfer?

## Part II. Diagnose

Write a one-page diagnostic memo with four labeled paragraphs:

1. **Mechanism:** Identify the labor mechanism you would lead with.
2. **Setting taxonomy:** Locate one regime in a comparative map.
3. **Transportability:** State what should generalize to another setting and what should not.
4. **Policy transfer:** Explain why external validity is not the same as copying a policy package.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/transfer_setting_summary.csv`
- `output/transfer/portable_vs_setting_specific.csv`
- `output/transfer/country_pitch_template.csv`
- `output/transfer/transfer_note.txt`

Use the transfer exercise inspired by [@jayachandran2021social] to explain why a norms result must name the labor margin and the setting-specific enforcement mechanism. State whether the binding constraint in each synthetic setting is care, service demand, norms, mobility, informality, or legal access.

## Optional Frontier Prompt

Use [@goldbergGottliebLallMehta2025ggdi] to write a supply-side versus demand-side distortions memo for a country or region you know well. Do not estimate the optional extension in the bounded path. The memo should state:

- the labor object;
- the likely supply-side wedge;
- the likely demand-side wedge;
- the data needed to distinguish them;
- what should and should not generalize from the setting.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced comparative policy outputs
- [ ] one-page diagnostic memo
- [ ] transfer outputs
- [ ] country-specific evidence pitch
- [ ] optional supply-demand distortions memo
