# Transfer Exercise

The transfer exercise uses a small synthetic-control setting with one treated city and five donor cities. The treated city adopts a workforce placement policy after the pre-treatment period. Donor cities are untreated.

Students use the transfer workflow to:

- choose convex donor weights using pre-treatment outcomes;
- inspect pre-treatment fit;
- estimate post-treatment gaps;
- compare treated gaps to donor placebo gaps.

Run:

```bash
python src/transfer_synthetic_control.py --input transfer/data/synthetic_control_city.csv --outdir output/transfer
```
