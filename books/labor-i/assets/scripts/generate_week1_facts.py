#!/usr/bin/env python3
"""Generate a simple Week 1 labor-market-status figure from public FRED CSV endpoints.

This script is intended to run locally in the user's environment. It downloads public CSV
series for CIVPART, EMRATIO, and UNRATE, merges them by date, and saves a publication-ready
PNG under `books/labor-i/assets/figures/`.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

SERIES = {
    "CIVPART": "Labor force participation rate",
    "EMRATIO": "Employment-population ratio",
    "UNRATE": "Unemployment rate",
}

BASE_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"


def fetch_series(series_id: str) -> pd.DataFrame:
    df = pd.read_csv(BASE_URL.format(series=series_id))
    df.columns = ["date", series_id]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df[series_id] = pd.to_numeric(df[series_id], errors="coerce")
    return df.dropna().copy()


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    fig_dir = root / "assets" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    merged: pd.DataFrame | None = None
    for sid in SERIES:
        df = fetch_series(sid)
        merged = df if merged is None else merged.merge(df, on="date", how="inner")

    if merged is None or merged.empty:
        raise RuntimeError("No data downloaded from FRED.")

    merged = merged[merged["date"] >= pd.Timestamp("1976-01-01")].copy()

    fig, ax1 = plt.subplots(figsize=(10, 5.8))
    ax2 = ax1.twinx()

    ax1.plot(merged["date"], merged["CIVPART"], label=SERIES["CIVPART"], linewidth=2)
    ax1.plot(merged["date"], merged["EMRATIO"], label=SERIES["EMRATIO"], linewidth=2)
    ax2.plot(merged["date"], merged["UNRATE"], label=SERIES["UNRATE"], linewidth=2, linestyle="--")

    ax1.set_ylabel("Percent")
    ax2.set_ylabel("Percent")
    ax1.set_title("U.S. labor-market status indicators")
    ax1.set_xlabel("")

    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(handles1 + handles2, labels1 + labels2, loc="upper right", frameon=False)

    fig.tight_layout()
    outpath = fig_dir / "01-labor-market-status-dashboard.png"
    fig.savefig(outpath, dpi=180, bbox_inches="tight")
    print(f"Saved {outpath}")


if __name__ == "__main__":
    main()
