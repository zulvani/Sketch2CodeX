"""
Wireframe Evaluation — Visualization Suite
==========================================
Reads results_full.csv and produces 5 publication-ready charts:

  1. Heatmap       — level F1 scores across all wireframes
  2. Radar         — average level F1 profile
  3. Scatter       — TED similarity vs Token F1 (EWM score)
  4. Bar           — EWM vs Equal-Weight score per wireframe
  5. Histogram     — F1 score distribution

Usage (Jupyter):
  from visualize_results import plot_all
  plot_all("results_full.csv", output_dir=".")

  # or individual charts:
  from visualize_results import (plot_heatmap, plot_radar,
      plot_scatter, plot_bar_ewm_vs_equal, plot_histogram)
"""

import math
import numpy  as np
import pandas as pd
import matplotlib.pyplot    as plt
import matplotlib.gridspec  as gridspec
import matplotlib.ticker    as ticker
from   matplotlib.patches   import FancyBboxPatch
import seaborn as sns
from   pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────

LEVEL_KEYS = [
    "row_count_f1",
    "cards_per_row_f1",
    "span_offset_f1",
    "grid_shape_f1",
    "objects_f1",
]
LEVEL_LABELS = [
    "Row Count",
    "Cards / Row",
    "Span & Offset",
    "Grid Shape",
    "Objects",
]

# Thesis-friendly palette
PALETTE = {
    "primary":   "#2C5F8A",
    "secondary": "#E07B39",
    "accent":    "#4CAF82",
    "neutral":   "#8E9AAF",
    "bg":        "#F8F9FB",
    "grid":      "#E2E6EA",
    "text":      "#1A1D23",
    "heatmap_lo":"#FFF0E6",
    "heatmap_hi":"#1B4F72",
}

def _style():
    plt.rcParams.update({
        "font.family":        "DejaVu Sans",
        "font.size":          10,
        "axes.titlesize":     13,
        "axes.titleweight":   "bold",
        "axes.labelsize":     10,
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "axes.facecolor":     PALETTE["bg"],
        "figure.facecolor":   "white",
        "grid.color":         PALETTE["grid"],
        "grid.linewidth":     0.6,
        "xtick.labelsize":    8,
        "ytick.labelsize":    8,
        "legend.fontsize":    9,
        "legend.framealpha":  0.9,
    })

def _save(fig, path):
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    print(f"  Saved → {path}")


# ─────────────────────────────────────────────────────────────────────────────
# 1. Heatmap — level F1 × wireframes
# ─────────────────────────────────────────────────────────────────────────────

def plot_heatmap(df: pd.DataFrame, output_path: str = None):
    _style()

    # Sort by overall EWM score descending so best wireframes are at top
    df_s = df.sort_values("ewm_score", ascending=False).reset_index(drop=True)
    matrix = df_s[LEVEL_KEYS].values          # shape (n, 5)
    n      = len(df_s)

    # Dynamic figure height — cap label font at readable size
    row_h  = max(0.22, min(0.38, 14 / n))
    fig_h  = max(6, n * row_h + 2)
    fig, ax = plt.subplots(figsize=(9, fig_h))

    im = ax.imshow(matrix, aspect="auto", cmap="YlOrBr",
                   vmin=0, vmax=1, interpolation="nearest")

    # Axes
    ax.set_xticks(range(5))
    ax.set_xticklabels(LEVEL_LABELS, fontsize=9, fontweight="bold")
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")

    ax.set_yticks(range(n))
    ax.set_yticklabels(df_s["wireframe"], fontsize=max(5, min(8, 120//n)))

    # Cell annotations (only if n ≤ 60, otherwise too crowded)
    if n <= 60:
        for i in range(n):
            for j in range(5):
                val   = matrix[i, j]
                color = "white" if val > 0.65 else PALETTE["text"]
                ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                        fontsize=max(5, min(7, 90//n)), color=color)

    # Colorbar
    cbar = fig.colorbar(im, ax=ax, fraction=0.02, pad=0.01)
    cbar.set_label("F1 Score", fontsize=9)
    cbar.ax.tick_params(labelsize=8)

    ax.set_title("Level F1 Scores Heatmap — All Wireframes\n"
                 "(sorted by EWM score, best → worst)",
                 fontsize=12, fontweight="bold", pad=18)

    fig.tight_layout()
    if output_path:
        _save(fig, output_path)
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# 2. Radar — average level F1 profile
# ─────────────────────────────────────────────────────────────────────────────

def plot_radar(df: pd.DataFrame, output_path: str = None):
    _style()

    avg_vals = [df[k].mean() for k in LEVEL_KEYS]
    std_vals = [df[k].std()  for k in LEVEL_KEYS]

    # Close the polygon
    values   = avg_vals + [avg_vals[0]]
    std_vals = std_vals + [std_vals[0]]
    labels   = LEVEL_LABELS + [LEVEL_LABELS[0]]

    N      = len(LEVEL_KEYS)
    angles = [n / float(N) * 2 * math.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7),
                           subplot_kw=dict(polar=True))
    ax.set_facecolor(PALETTE["bg"])

    # Grid rings
    for r in [0.2, 0.4, 0.6, 0.8, 1.0]:
        ax.plot(angles, [r]*len(angles), color=PALETTE["grid"],
                linewidth=0.7, linestyle="--", zorder=1)
        ax.text(0, r, f"{r:.1f}", ha="center", va="center",
                fontsize=7, color=PALETTE["neutral"])

    # Std dev band
    upper = [min(1.0, v + s) for v, s in zip(values, std_vals)]
    lower = [max(0.0, v - s) for v, s in zip(values, std_vals)]
    ax.fill(angles, upper, alpha=0.08, color=PALETTE["primary"])
    ax.fill(angles, lower, alpha=0.08, color="white")

    # Main polygon
    ax.plot(angles, values, "o-", linewidth=2.5,
            color=PALETTE["primary"], markersize=7, zorder=3)
    ax.fill(angles, values, alpha=0.20, color=PALETTE["primary"], zorder=2)

    # Data point labels
    for angle, val in zip(angles[:-1], avg_vals):
        ax.text(angle, val + 0.08, f"{val:.3f}",
                ha="center", va="center",
                fontsize=8.5, fontweight="bold",
                color=PALETTE["primary"])

    # Spoke labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(LEVEL_LABELS, fontsize=10, fontweight="bold",
                       color=PALETTE["text"])
    ax.set_yticklabels([])
    ax.set_ylim(0, 1)
    ax.spines["polar"].set_visible(False)

    ax.set_title("Average Structural F1 Profile\n(shaded band = ±1 std dev)",
                 fontsize=12, fontweight="bold", pad=25)

    fig.tight_layout()
    if output_path:
        _save(fig, output_path)
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# 3. Scatter — TED similarity vs EWM score
# ─────────────────────────────────────────────────────────────────────────────

def plot_scatter(df: pd.DataFrame, output_path: str = None):
    _style()

    fig, ax = plt.subplots(figsize=(7, 6))

    # Color points by equal_score quartile
    quartiles = pd.qcut(df["eq_score"], q=4,
                        labels=["Q1 (low)", "Q2", "Q3", "Q4 (high)"])
    colors    = [PALETTE["primary"], PALETTE["secondary"],
                 PALETTE["accent"],  PALETTE["neutral"]]

    for i, (label, grp) in enumerate(df.groupby(quartiles, observed=True)):
        ax.scatter(grp["ewm_score"], grp["ted_similarity"],
                   label=f"Equal-W {label}",
                   color=colors[i], alpha=0.75,
                   s=55, edgecolors="white", linewidths=0.5, zorder=3)

    # Trend line
    x   = df["ewm_score"].values
    y   = df["ted_similarity"].values
    z   = np.polyfit(x, y, 1)
    p   = np.poly1d(z)
    xs  = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, p(xs), "--", color=PALETTE["text"],
            linewidth=1.2, alpha=0.5, label="Trend", zorder=2)

    # Pearson r
    r = np.corrcoef(x, y)[0, 1]
    ax.text(0.04, 0.95, f"Pearson r = {r:.3f}",
            transform=ax.transAxes, fontsize=9,
            color=PALETTE["text"], va="top",
            bbox=dict(boxstyle="round,pad=0.3", fc="white",
                      ec=PALETTE["grid"], alpha=0.9))

    ax.set_xlabel("EWM Weighted Score",  fontsize=10)
    ax.set_ylabel("TED Similarity",      fontsize=10)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, zorder=0)
    ax.legend(loc="lower right", fontsize=8)
    ax.set_title("TED Similarity vs EWM Weighted Score\n"
                 "(colored by Equal-Weight quartile)",
                 fontsize=12, fontweight="bold")

    fig.tight_layout()
    if output_path:
        _save(fig, output_path)
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# 4. Bar — EWM vs Equal-Weight (sorted, divergence highlighted)
# ─────────────────────────────────────────────────────────────────────────────

def plot_bar_ewm_vs_equal(df: pd.DataFrame, output_path: str = None):
    _style()

    df_s   = df.sort_values("ewm_score", ascending=False).reset_index(drop=True)
    n      = len(df_s)
    x      = np.arange(n)
    diff   = df_s["ewm_score"] - df_s["eq_score"]

    fig, axes = plt.subplots(2, 1, figsize=(max(12, n * 0.09 + 2), 8),
                              gridspec_kw={"height_ratios": [3, 1]})

    # ── top panel: grouped bars ──────────────────────────────────────────────
    ax = axes[0]
    w  = 0.4
    ax.bar(x - w/2, df_s["eq_score"],  width=w, label="Equal-Weight",
           color=PALETTE["primary"],   alpha=0.85, zorder=3)
    ax.bar(x + w/2, df_s["ewm_score"], width=w, label="EWM-Weighted",
           color=PALETTE["secondary"], alpha=0.85, zorder=3)

    ax.set_xlim(-1, n)
    ax.set_ylim(0, 1.12)
    ax.set_xticks([])
    ax.set_ylabel("Score", fontsize=10)
    ax.set_title("EWM-Weighted vs Equal-Weight Score per Wireframe\n"
                 "(sorted by EWM score, best → worst)",
                 fontsize=12, fontweight="bold")
    ax.axhline(df_s["eq_score"].mean(),  color=PALETTE["primary"],
               linewidth=1, linestyle=":", alpha=0.7,
               label=f"Equal-W avg ({df_s['eq_score'].mean():.3f})")
    ax.axhline(df_s["ewm_score"].mean(), color=PALETTE["secondary"],
               linewidth=1, linestyle=":", alpha=0.7,
               label=f"EWM avg ({df_s['ewm_score'].mean():.3f})")
    ax.grid(True, axis="y", zorder=0)
    ax.legend(loc="upper right", fontsize=8.5)

    # ── bottom panel: divergence bars ────────────────────────────────────────
    ax2 = axes[1]
    colors_div = [PALETTE["secondary"] if d > 0 else PALETTE["primary"]
                  for d in diff]
    ax2.bar(x, diff, color=colors_div, alpha=0.85, zorder=3)
    ax2.axhline(0, color=PALETTE["text"], linewidth=0.8)

    # Highlight large divergences
    threshold = 0.05
    for i, d in enumerate(diff):
        if abs(d) > threshold:
            ax2.bar(i, d,
                    color=PALETTE["secondary"] if d > 0 else PALETTE["primary"],
                    alpha=1.0, zorder=4,
                    edgecolor="black", linewidth=0.5)

    ax2.set_xlim(-1, n)
    ax2.set_ylabel("EWM − Equal-W", fontsize=9)
    ax2.set_xlabel(f"Wireframes (n={n}, sorted by EWM score)", fontsize=9)
    ax2.set_xticks([])
    ax2.grid(True, axis="y", zorder=0)

    large = (abs(diff) > threshold).sum()
    ax2.text(0.01, 0.92,
             f"|Δ| > {threshold}: {large} wireframes  "
             f"(orange=EWM↑, blue=EWM↓)",
             transform=ax2.transAxes, fontsize=8,
             color=PALETTE["text"], va="top")

    fig.tight_layout(h_pad=0.4)
    if output_path:
        _save(fig, output_path)
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# 5. Histogram — F1 score distribution (all levels + overall)
# ─────────────────────────────────────────────────────────────────────────────

def plot_histogram(df: pd.DataFrame, output_path: str = None):
    _style()

    fig, axes = plt.subplots(2, 3, figsize=(13, 7))
    axes      = axes.flatten()

    all_cols = LEVEL_KEYS + ["ewm_score"]
    all_lbls = LEVEL_LABELS + ["Overall (EWM)"]
    palette  = [PALETTE["primary"]] * 5 + [PALETTE["secondary"]]

    for i, (col, lbl, color) in enumerate(zip(all_cols, all_lbls, palette)):
        ax   = axes[i]
        data = df[col].dropna()

        # Histogram
        n_bins = min(25, max(10, len(data) // 6))
        counts, edges, patches = ax.hist(
            data, bins=n_bins, color=color,
            alpha=0.80, edgecolor="white", linewidth=0.5, zorder=3
        )

        # Color bars by zone: red<0.5, yellow 0.5-0.75, green>0.75
        for patch, left in zip(patches, edges[:-1]):
            if   left < 0.50: patch.set_facecolor("#E74C3C")
            elif left < 0.75: patch.set_facecolor("#F39C12")
            else:             patch.set_facecolor("#27AE60")

        # KDE overlay
        try:
            from scipy.stats import gaussian_kde
            kde_x = np.linspace(0, 1, 200)
            kde   = gaussian_kde(data, bw_method=0.25)
            ax2   = ax.twinx()
            ax2.plot(kde_x, kde(kde_x), color=color,
                     linewidth=2, alpha=0.8)
            ax2.set_yticks([])
            ax2.set_ylim(bottom=0)
            ax2.spines["top"].set_visible(False)
            ax2.spines["right"].set_visible(False)
        except ImportError:
            pass

        # Stats annotation
        ax.axvline(data.mean(),   color="black",          linewidth=1.5,
                   linestyle="-",  label=f"Mean {data.mean():.3f}")
        ax.axvline(data.median(), color=PALETTE["neutral"], linewidth=1.5,
                   linestyle="--", label=f"Median {data.median():.3f}")

        ax.set_title(lbl, fontsize=10, fontweight="bold")
        ax.set_xlabel("F1 Score", fontsize=8)
        ax.set_ylabel("Count",    fontsize=8)
        ax.set_xlim(0, 1)
        ax.grid(True, axis="y", zorder=0)
        ax.legend(fontsize=7, loc="upper left")

    # Hide unused subplot (2×3 grid, 6 items exactly — nothing to hide)
    fig.suptitle("F1 Score Distribution per Structural Level\n"
                 "(red < 0.50  ·  orange 0.50-0.75  ·  green > 0.75)",
                 fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()
    if output_path:
        _save(fig, output_path)
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Master runner
# ─────────────────────────────────────────────────────────────────────────────

def plot_all(csv_path: str, output_dir: str = ".") -> dict:
    """
    Load results_full.csv and produce all 5 charts.
    Returns dict of {chart_name: matplotlib Figure}

    Usage:
        figs = plot_all("results_full.csv", output_dir=".")
    """
    df  = pd.read_csv(csv_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    print(f"\nLoaded {len(df)} wireframes from {csv_path}")
    print(f"Output directory: {out.resolve()}\n")

    figs = {}

    print("1/5  Heatmap ...")
    figs["heatmap"]  = plot_heatmap(
        df, str(out / "01_heatmap.png"))

    print("2/5  Radar ...")
    figs["radar"]    = plot_radar(
        df, str(out / "02_radar.png"))

    print("3/5  Scatter ...")
    figs["scatter"]  = plot_scatter(
        df, str(out / "03_scatter_ted_vs_ewm.png"))

    print("4/5  Bar EWM vs Equal-W ...")
    figs["bar"]      = plot_bar_ewm_vs_equal(
        df, str(out / "04_bar_ewm_vs_equal.png"))

    print("5/5  Histogram ...")
    figs["histogram"]= plot_histogram(
        df, str(out / "05_histogram.png"))

    print(f"\nAll charts saved to: {out.resolve()}")
    return figs


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Generate evaluation visualizations from results_full.csv")
    parser.add_argument("csv",            help="Path to results_full.csv")
    parser.add_argument("--output", "-o", help="Output directory", default=".")
    args = parser.parse_args()
    plot_all(args.csv, args.output)
