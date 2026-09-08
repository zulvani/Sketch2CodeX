"""
Wireframe Evaluator — Tree Edit Distance + EWM Weighted Similarity
==================================================================

Metrics computed per wireframe:
  1. Token F1 & Jaccard       (from evaluate_wireframes.py)
  2. Tree Edit Distance (TED) — Zhang-Shasha algorithm via `zss`
  3. EWM Weighted Similarity  — Shannon entropy weighting across 5 level F1s

Level F1s used for EWM input:
  L1 row_count_f1
  L2 cards_per_row_f1
  L3 span_offset_f1
  L4 grid_shape_f1
  L5 objects_f1

Usage (Jupyter):
  from ted_ewm import run_all
  results = run_all("/path/to/root", output_csv="/path/to/root/results_full.csv")
"""

import json, csv, math
from pathlib import Path
import zss


# ─────────────────────────────────────────────────────────────────────────────
# 1. JSON → zss.Node tree
# ─────────────────────────────────────────────────────────────────────────────

def build_tree(data: dict) -> zss.Node:
    """
    Convert wireframe JSON into a zss.Node tree.

    Tree shape:
      root
      └── row[i]
          └── card[j]
              ├── span(cS:X,cO:Y,cOS:Z)
              ├── grid(R×C)
              └── obj[r][c]:objClass
    """
    root = zss.Node("root")

    for i, row in enumerate(data.get("rows", [])):
        row_node = zss.Node(f"row[{i}]")
        root.addkid(row_node)

        for j, card in enumerate(row.get("cards", [])):
            card_node = zss.Node(f"card[{j}]")
            row_node.addkid(card_node)

            # Span & offset — one node encodes all three values together
            cs  = card.get("columnSpan",      "?")
            co  = card.get("columnOffset",    "?")
            cos = card.get("columnOffsetSum", "?")
            card_node.addkid(zss.Node(f"span(cS:{cs},cO:{co},cOS:{cos})"))

            # Grid shape — one node
            se        = card.get("segmentedElements", [])
            grid_rows = len(se)
            grid_cols = max((len(r) for r in se), default=0)
            card_node.addkid(zss.Node(f"grid({grid_rows}x{grid_cols})"))

            # Objects — one node per cell, positionally keyed
            for r, row_ in enumerate(se):
                for c, obj in enumerate(row_):
                    obj_class = obj.get("objClass", "unknown")
                    card_node.addkid(zss.Node(f"obj[{r}][{c}]:{obj_class}"))

    return root


def tree_size(node: zss.Node) -> int:
    """Count total nodes in tree."""
    return 1 + sum(tree_size(c) for c in node.children)


def compute_ted(gt_data: dict, gen_data: dict) -> dict:
    """
    Compute Zhang-Shasha Tree Edit Distance and normalize to [0, 1].
    normalized_ted = 1 - (distance / max(size_gt, size_gen))
    similarity     = normalized_ted  (1.0 = perfect match)
    """
    gt_tree  = build_tree(gt_data)
    gen_tree = build_tree(gen_data)

    distance = zss.simple_distance(gt_tree, gen_tree)
    size_gt  = tree_size(gt_tree)
    size_gen = tree_size(gen_tree)
    max_size = max(size_gt, size_gen)

    normalized   = distance / max_size if max_size else 0.0
    similarity   = 1.0 - normalized          # 1.0 = identical, 0.0 = completely different

    return {
        "ted_distance":   distance,
        "ted_size_gt":    size_gt,
        "ted_size_gen":   size_gen,
        "ted_normalized": round(normalized,  4),
        "ted_similarity": round(similarity,  4),
    }


# ─────────────────────────────────────────────────────────────────────────────
# 2. Level F1s  (needed as EWM input)
# ─────────────────────────────────────────────────────────────────────────────

SPAN_FIELDS = ("columnSpan", "columnOffset", "columnOffsetSum")

def _f1_jaccard(matched, total_gt, total_gen):
    union     = total_gt + total_gen - matched
    precision = matched / total_gen  if total_gen  else 0.0
    recall    = matched / total_gt   if total_gt   else 0.0
    f1        = 2*precision*recall / (precision+recall) if (precision+recall) else 0.0
    jaccard   = matched / union      if union      else 0.0
    return precision, recall, f1, jaccard

def level_f1s(gt: dict, gen: dict) -> dict:
    """
    Return per-level F1 scores used as EWM criteria.
    Keys: row_count, cards_per_row, span_offset, grid_shape, objects
    """
    gt_rows  = gt.get("rows",  [])
    gen_rows = gen.get("rows", [])
    n_rows   = max(len(gt_rows), len(gen_rows))

    # L1 — row count (binary)
    _, _, l1_f1, l1_jac = _f1_jaccard(
        1 if len(gt_rows) == len(gen_rows) else 0, 1, 1
    )

    # L2 — cards per row
    l2_matched = sum(
        1 for i in range(n_rows)
        if len((gt_rows[i]["cards"] if i < len(gt_rows) else [])) ==
           len((gen_rows[i]["cards"] if i < len(gen_rows) else []))
    )
    _, _, l2_f1, l2_jac = _f1_jaccard(l2_matched, len(gt_rows), len(gen_rows))

    # L3 — span & offset, L4 — grid shape, L5 — objects (per aligned card)
    l3_gt = l3_gen = l3_matched = 0
    l4_gt = l4_gen = l4_matched = 0
    l5_gt = l5_gen = l5_matched = 0

    for i in range(n_rows):
        gt_cards  = gt_rows[i]["cards"]  if i < len(gt_rows)  else []
        gen_cards = gen_rows[i]["cards"] if i < len(gen_rows) else []
        n_cards   = max(len(gt_cards), len(gen_cards))

        for j in range(n_cards):
            gt_c  = gt_cards[j]  if j < len(gt_cards)  else None
            gen_c = gen_cards[j] if j < len(gen_cards) else None

            # L3
            if gt_c:  l3_gt  += 1
            if gen_c: l3_gen += 1
            if gt_c and gen_c:
                if all(gt_c.get(f) == gen_c.get(f) for f in SPAN_FIELDS):
                    l3_matched += 1

            # L4
            if gt_c:  l4_gt  += 1
            if gen_c: l4_gen += 1
            if gt_c and gen_c:
                gt_se  = gt_c.get("segmentedElements",  [])
                gen_se = gen_c.get("segmentedElements", [])
                gt_shape  = (len(gt_se),  max((len(r) for r in gt_se),  default=0))
                gen_shape = (len(gen_se), max((len(r) for r in gen_se), default=0))
                if gt_shape == gen_shape:
                    l4_matched += 1

            # L5 — per-cell object class
            gt_cells  = {
                (r, c): obj.get("objClass", "unknown")
                for r, row_ in enumerate((gt_c  or {}).get("segmentedElements", []))
                for c, obj  in enumerate(row_)
            }
            gen_cells = {
                (r, c): obj.get("objClass", "unknown")
                for r, row_ in enumerate((gen_c or {}).get("segmentedElements", []))
                for c, obj  in enumerate(row_)
            }
            all_pos = set(gt_cells) | set(gen_cells)
            for pos in all_pos:
                if pos in gt_cells:  l5_gt  += 1
                if pos in gen_cells: l5_gen += 1
                if pos in gt_cells and pos in gen_cells:
                    if gt_cells[pos] == gen_cells[pos]:
                        l5_matched += 1

    _, _, l3_f1, l3_jac = _f1_jaccard(l3_matched, l3_gt, l3_gen)
    _, _, l4_f1, l4_jac = _f1_jaccard(l4_matched, l4_gt, l4_gen)
    _, _, l5_f1, l5_jac = _f1_jaccard(l5_matched, l5_gt, l5_gen)

    return {
        "row_count_f1":         round(l1_f1,  6),
        "cards_per_row_f1":     round(l2_f1,  6),
        "span_offset_f1":       round(l3_f1,  6),
        "grid_shape_f1":        round(l4_f1,  6),
        "objects_f1":           round(l5_f1,  6),
        "row_count_jac":        round(l1_jac, 6),
        "cards_per_row_jac":    round(l2_jac, 6),
        "span_offset_jac":      round(l3_jac, 6),
        "grid_shape_jac":       round(l4_jac, 6),
        "objects_jac":          round(l5_jac, 6),
    }


# ─────────────────────────────────────────────────────────────────────────────
# 3. EWM (Shannon Entropy Weight Method)
# ─────────────────────────────────────────────────────────────────────────────

LEVEL_KEYS = [
    "row_count_f1",
    "cards_per_row_f1",
    "span_offset_f1",
    "grid_shape_f1",
    "objects_f1",
]

def compute_ewm_weights(all_level_f1s: list[dict]) -> dict:
    """
    Apply Shannon Entropy Weight Method across all wireframes.

    Steps:
      1. Normalize each metric column (proportion transform)
      2. Compute entropy E_j for each metric
      3. Compute divergence d_j = 1 - E_j
      4. Normalize divergence to get weights w_j

    Returns dict: {metric_key: weight}
    """
    n = len(all_level_f1s)
    if n == 0:
        return {k: 1/len(LEVEL_KEYS) for k in LEVEL_KEYS}

    # Step 1 — column sums for proportion transform
    col_sums = {
        k: sum(row[k] for row in all_level_f1s) or 1e-10   # avoid div/0
        for k in LEVEL_KEYS
    }

    # Step 2 — entropy per metric
    entropies = {}
    for k in LEVEL_KEYS:
        entropy = 0.0
        for row in all_level_f1s:
            p = row[k] / col_sums[k]
            if p > 0:
                entropy -= p * math.log(p)
        # normalize by ln(n) — standard EWM formula
        entropies[k] = entropy / math.log(n) if n > 1 else 0.0

    # Step 3 — divergence
    divergences = {k: 1.0 - entropies[k] for k in LEVEL_KEYS}

    # Step 4 — weights
    total_div = sum(divergences.values()) or 1e-10
    weights   = {k: divergences[k] / total_div for k in LEVEL_KEYS}

    return weights


def compute_ewm_score(level_f1s_row: dict, weights: dict) -> float:
    """Weighted sum of level F1s using EWM weights."""
    return sum(weights[k] * level_f1s_row[k] for k in LEVEL_KEYS)


def equal_weight_score(level_f1s_row: dict) -> float:
    """Baseline: equal weight for all levels."""
    return sum(level_f1s_row[k] for k in LEVEL_KEYS) / len(LEVEL_KEYS)


# ─────────────────────────────────────────────────────────────────────────────
# 4. Main runner
# ─────────────────────────────────────────────────────────────────────────────

def run_all(root: str, output_csv: str = None, debug: bool = False) -> list[dict]:
    root_path   = Path(root)
    all_results = []

    # ── pass 1: collect per-wireframe metrics ────────────────────────────────
    print(f"\nEvaluating: {root}\n{'='*65}")
    for wireframe_dir in sorted(root_path.iterdir()):
        if not wireframe_dir.is_dir():
            continue

        name     = wireframe_dir.name
        gt_file  = wireframe_dir / f"{name}.json"
        gen_file = wireframe_dir / f"{name}-result.json"

        if not gt_file.exists():
            print(f"[SKIP] {name}: ground truth not found"); continue
        if not gen_file.exists():
            print(f"[SKIP] {name}: generated file not found"); continue

        try:
            with open(gt_file,  encoding="utf-8") as f: gt  = json.load(f)
            with open(gen_file, encoding="utf-8") as f: gen = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] {name}: {e}"); continue

        ted     = compute_ted(gt, gen)
        lf1s    = level_f1s(gt, gen)
        eq_score = equal_weight_score(lf1s)

        all_results.append({
            "wireframe":    name,
            "level_f1s":   lf1s,
            "eq_score":    round(eq_score, 4),
            **ted,
        })
        print(
            f"[OK] {name:<45} "
            f"TED={ted['ted_distance']:>4}  "
            f"TED_sim={ted['ted_similarity']:.4f}  "
            f"eq_score={eq_score:.4f}"
        )

    if not all_results:
        print("[WARN] No valid wireframe pairs found.")
        return []

    # ── pass 2: EWM weights from all wireframes ──────────────────────────────
    all_level_f1s = [r["level_f1s"] for r in all_results]
    weights       = compute_ewm_weights(all_level_f1s)

    for r in all_results:
        r["ewm_score"] = round(compute_ewm_score(r["level_f1s"], weights), 4)

    # ── print results ────────────────────────────────────────────────────────
    _print_table(all_results, weights)

    if output_csv:
        _save_csv(all_results, weights, output_csv)

    return all_results


# ─────────────────────────────────────────────────────────────────────────────
# 5. Output
# ─────────────────────────────────────────────────────────────────────────────

LEVEL_LABELS = {
    "row_count_f1":     "Row Count",
    "cards_per_row_f1": "Cards/Row",
    "span_offset_f1":   "Span & Offset",
    "grid_shape_f1":    "Grid Shape",
    "objects_f1":       "Objects",
}

def _print_table(all_results: list[dict], weights: dict):
    n   = len(all_results)
    sep = " | "

    # ── EWM weights ──────────────────────────────────────────────────────────
    print(f"\n{'─'*65}")
    print("  EWM Weights (Shannon Entropy Method):")
    for k, label in LEVEL_LABELS.items():
        bar = "█" * int(weights[k] * 40)
        print(f"    {label:<18} w={weights[k]:.4f}  {bar}")
    print(f"    {'SUM':<18} w={sum(weights.values()):.4f}")

    # ── per wireframe table ──────────────────────────────────────────────────
    print(f"\n{'─'*65}")
    header = (
        f"{'Wireframe':<40}"
        f"{'TED dist':>9}"
        f"{'TED sim':>9}"
        f"{'Equal W':>9}"
        f"{'EWM W':>9}"
    )
    print(header)
    print("─" * len(header))

    for r in all_results:
        print(
            f"{r['wireframe']:<40}"
            f"{r['ted_distance']:>9}"
            f"{r['ted_similarity']:>9.4f}"
            f"{r['eq_score']:>9.4f}"
            f"{r['ewm_score']:>9.4f}"
        )

    print("─" * len(header))

    # averages
    avg_ted_d   = sum(r["ted_distance"]   for r in all_results) / n
    avg_ted_sim = sum(r["ted_similarity"] for r in all_results) / n
    avg_eq      = sum(r["eq_score"]       for r in all_results) / n
    avg_ewm     = sum(r["ewm_score"]      for r in all_results) / n
    print(
        f"{'AVERAGE':<40}"
        f"{avg_ted_d:>9.2f}"
        f"{avg_ted_sim:>9.4f}"
        f"{avg_eq:>9.4f}"
        f"{avg_ewm:>9.4f}"
    )
    print("─" * len(header))

    # ── level F1 breakdown ───────────────────────────────────────────────────
    print(f"\n  Level F1 breakdown (with EWM weights):\n")
    lheader = f"  {'Wireframe':<40}" + "".join(
        f"{LEVEL_LABELS[k]:>16}" for k in LEVEL_KEYS
    )
    print(lheader)
    print(f"  {'Weight':<40}" + "".join(f"{weights[k]:>16.4f}" for k in LEVEL_KEYS))
    print("  " + "─" * (len(lheader) - 2))
    for r in all_results:
        row = f"  {r['wireframe']:<40}"
        row += "".join(f"{r['level_f1s'][k]:>16.4f}" for k in LEVEL_KEYS)
        print(row)
    print("  " + "─" * (len(lheader) - 2))
    avg_row = f"  {'AVERAGE':<40}"
    avg_row += "".join(
        f"{sum(r['level_f1s'][k] for r in all_results)/n:>16.4f}" for k in LEVEL_KEYS
    )
    print(avg_row)
    print()


JAC_KEYS = [k.replace("_f1", "_jac") for k in LEVEL_KEYS]

def _save_csv(all_results: list[dict], weights: dict, path: str):
    fields = (
        ["wireframe"] +
        list(LEVEL_KEYS) +           # per-level F1
        list(JAC_KEYS)  +            # per-level Jaccard
        ["eq_score", "ewm_score",
         "ted_distance", "ted_size_gt", "ted_size_gen",
         "ted_normalized", "ted_similarity"] +
        [f"ewm_weight_{k}" for k in LEVEL_KEYS]
    )

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in all_results:
            row = {
                "wireframe":      r["wireframe"],
                "eq_score":       r["eq_score"],
                "ewm_score":      r["ewm_score"],
                "ted_distance":   r["ted_distance"],
                "ted_size_gt":    r["ted_size_gt"],
                "ted_size_gen":   r["ted_size_gen"],
                "ted_normalized": r["ted_normalized"],
                "ted_similarity": r["ted_similarity"],
            }
            for k in LEVEL_KEYS:
                row[k]                 = f"{r['level_f1s'][k]:.4f}"
                row[f"ewm_weight_{k}"] = f"{weights[k]:.4f}"
            for jk in JAC_KEYS:
                row[jk] = f"{r['level_f1s'][jk]:.4f}"
            writer.writerow(row)

    print(f"[CSV] Saved → {path}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Wireframe evaluator: TED + EWM weighted similarity"
    )
    parser.add_argument("root",           help="Root directory with wireframe subdirs")
    parser.add_argument("--output", "-o", help="CSV output path", default=None)
    parser.add_argument("--debug",  "-d", action="store_true")
    args = parser.parse_args()
    run_all(args.root, output_csv=args.output, debug=args.debug)
