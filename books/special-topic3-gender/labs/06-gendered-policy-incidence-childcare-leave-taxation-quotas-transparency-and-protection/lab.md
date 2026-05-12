# Code Lab 6: Gendered Policy Incidence

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 6 -- Gendered policy incidence  
**Associated chapter:** `06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection.md`  
**Lab slug:** `06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@blundellDuchiniSimionTurrell2025]  
**Secondary / challenge anchor:** [@gentilePassaroKojimaPakzadHurson2026]  
**Optional extension anchors:** [@baileyBykerPatelRamnath2025], [@bertrandBlackJensenLlerasMuney2019], [@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025]

## Why This Lab Exists

Week 6 asks students to read gender policy papers by margins and incidence rather than by headline gap closure. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a pay-transparency reporting exercise inspired by [@blundellDuchiniSimionTurrell2025].
2. **Diagnose** whether each output is an average outcome effect, an incidence statement, a firm response, or a welfare-relevant missing margin.
3. **Transfer** the same diagnostic logic to an equal-pay-for-similar-work setting inspired by [@gentilePassaroKojimaPakzadHurson2026].

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential firm-worker microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce threshold-style transparency summaries using synthetic firm-worker data;
2. decompose a firm-level gender pay-gap change into women's pay growth, men's pay growth, bonus changes, and retention;
3. distinguish a gap effect from incidence, firm response, and welfare;
4. transfer the same logic to an equal-pay rule where firms can respond through wage compression and job segregation;
5. write a short policy-as-identification memo that separates policy evaluation from mechanism identification.

## Local Structure

```text
labs/06-gendered-policy-incidence-childcare-leave-taxation-quotas-transparency-and-protection/
  lab.md
  smoke.sh
  src/
    build_week6_synthetic_data.py
    reproduce_pay_transparency.py
    transfer_equal_pay.py
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
conda run -n research python src/build_week6_synthetic_data.py

conda run -n research python src/reproduce_pay_transparency.py \
  --input original/reduced/blundell_uk_pay_transparency_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_equal_pay.py \
  --input transfer/data/gentile_equal_pay_similar_work_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/reporting_threshold_balance.csv`
- `output/reproduced/pay_gap_event_study.csv`
- `output/reproduced/transparency_decomposition.csv`
- `output/reproduced/incidence_diagnostics.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the treatment rule and treated unit?
- Which observed margins move: base pay, bonuses, retention, or total pay?
- Does the gap fall because women's pay rises, men's pay slows, bonuses compress, or composition changes?
- Which welfare margins remain unobserved?

## Part II. Diagnose

Write a one-page diagnostic memo with four labeled paragraphs:

1. **Outcome effect:** State the average pay-gap effect and the comparison group.
2. **Incidence:** State who appears to bear the pay adjustment in the synthetic data.
3. **Firm response:** State which firm margins are observed and which are missing.
4. **Welfare:** State why a smaller gap is not a complete welfare statement.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/equal_pay_gap_by_cell.csv`
- `output/transfer/segregation_response.csv`
- `output/transfer/transfer_diagnostics.csv`
- `output/transfer/transfer_note.txt`

Use the equal-pay exercise inspired by [@gentilePassaroKojimaPakzadHurson2026] to explain why constraining one pay margin can shift another margin. State whether the synthetic rule changes within-cell pay gaps, sorting across job cells, or both.

## Optional Frontier Prompt

Choose one design memo:

- Paid family leave [@baileyBykerPatelRamnath2025]: separate attachment, earnings, childbearing, employer response, and long-run career incidence.
- Board quotas [@bertrandBlackJensenLlerasMuney2019]: separate top-node representation from pipeline spillovers.
- Childcare subsidies [@bjorvatnFerrisGulesciNasgowitzSomvilleVandewalle2025]: separate maternal labor supply from household incidence and child outcomes.

Do not estimate these extensions in the bounded path. For each memo, name the treatment, treated unit, observed margin, likely incidence bearer, and the additional data required for a mechanism claim.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced pay-transparency outputs
- [ ] one-page diagnostic memo
- [ ] equal-pay transfer outputs
- [ ] paragraph on firm response and segregation
- [ ] optional frontier policy-as-identification memo
