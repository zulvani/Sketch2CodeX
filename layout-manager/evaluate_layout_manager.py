"""
Wireframe JSON Evaluator — Token Set Approach
=============================================
Every structural attribute is serialized into a flat token string.
GT tokens vs GEN tokens → single F1 + Jaccard per wireframe.

Token patterns:
  root.total_rows:[int]
  row[i].total_cards:[int]
  row[i].card[j].columnSpan:[int]
  row[i].card[j].columnOffset:[int]
  row[i].card[j].grid_rows:[int]
  row[i].card[j].grid_cols:[int]
  row[i].card[j].object[r][c]:[objClass]

Usage:
  python evaluate_wireframes.py <root_dir>
  python evaluate_wireframes.py <root_dir> --output results.csv
  python evaluate_wireframes.py <root_dir> --debug          # print token sets
"""

import json, csv, argparse
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Tokenizer
# ─────────────────────────────────────────────────────────────────────────────

def tokenize(data: dict) -> list[str]:
    """
    Convert a wireframe JSON into a flat list of structural token strings.
    Duplicate tokens are kept (converted to set later for F1/Jaccard).
    """
    tokens = []
    rows = data.get("rows", [])

    # Level 1 — row count
    tokens.append(f"root.total_rows:{len(rows)}")

    for i, row in enumerate(rows):
        cards = row.get("cards", [])

        # Level 2 — cards per row
        tokens.append(f"row[{i}].total_cards:{len(cards)}")

        for j, card in enumerate(cards):

            # Level 3 — span & offset
            for field in ("columnSpan", "columnOffset"):
                val = card.get(field)
                if val is not None:
                    tokens.append(f"row[{i}].card[{j}].{field}:{val}")

            # Level 4 — grid dimensions
            se = card.get("segmentedElements", [])
            grid_rows = len(se)
            grid_cols = max((len(row_) for row_ in se), default=0)
            tokens.append(f"row[{i}].card[{j}].grid_rows:{grid_rows}")
            tokens.append(f"row[{i}].card[{j}].grid_cols:{grid_cols}")

            # Level 5 — object class at each (r, c) position (order-sensitive)
            for r, row_ in enumerate(se):
                for c, obj in enumerate(row_):
                    obj_class = obj.get("objClass")
                    tokens.append(
                        f"row[{i}].card[{j}].object[{r}][{c}]:{obj_class}"
                    )

    return tokens


# ─────────────────────────────────────────────────────────────────────────────
# F1 + Jaccard
# ─────────────────────────────────────────────────────────────────────────────

def compute_metrics(gt_tokens: list[str], gen_tokens: list[str]) -> dict:
    gt_set  = set(gt_tokens)
    gen_set = set(gen_tokens)

    intersection = gt_set & gen_set
    union        = gt_set | gen_set

    matched    = len(intersection)
    total_gt   = len(gt_set)
    total_gen  = len(gen_set)
    total_union = len(union)

    precision = matched / total_gen  if total_gen   else 0.0
    recall    = matched / total_gt   if total_gt    else 0.0
    f1        = (2 * precision * recall / (precision + recall)
                 if (precision + recall) else 0.0)
    jaccard   = matched / total_union if total_union else 0.0

    return {
        "total_gt":   total_gt,
        "total_gen":  total_gen,
        "matched":    matched,
        "precision":  precision,
        "recall":     recall,
        "f1":         f1,
        "jaccard":    jaccard,
        # keep sets for debug / micro avg
        "_gt_set":    gt_set,
        "_gen_set":   gen_set,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Debug printer
# ─────────────────────────────────────────────────────────────────────────────

def print_debug(name: str, metrics: dict):
    gt_set  = metrics["_gt_set"]
    gen_set = metrics["_gen_set"]
    matched = gt_set & gen_set
    fp      = gen_set - gt_set   # in GEN but not GT
    fn      = gt_set  - gen_set  # in GT  but not GEN

    print(f"\n{'─'*60}")
    print(f"  DEBUG: {name}")
    print(f"{'─'*60}")
    print(f"  ✅ Matched ({len(matched)}):")
    for t in sorted(matched): print(f"      {t}")
    print(f"  ❌ False Positive — extra in GEN ({len(fp)}):")
    for t in sorted(fp):      print(f"      {t}")
    print(f"  ❌ False Negative — missing in GEN ({len(fn)}):")
    for t in sorted(fn):      print(f"      {t}")


# ─────────────────────────────────────────────────────────────────────────────
# Directory loop
# ─────────────────────────────────────────────────────────────────────────────

def evaluate_directory(root: str, debug: bool = False) -> list[dict]:
    root_path   = Path(root)
    all_results = []

    for wireframe_dir in sorted(root_path.iterdir()):
        if not wireframe_dir.is_dir():
            continue

        name     = wireframe_dir.name
        gt_file  = wireframe_dir / f"{name}.json"
        gen_file = wireframe_dir / f"{name}-result.json"

        if not gt_file.exists():
            print(f"[SKIP] {name}: ground truth not found ({gt_file.name})")
            continue
        if not gen_file.exists():
            print(f"[SKIP] {name}: generated file not found ({gen_file.name})")
            continue

        try:
            with open(gt_file,  encoding="utf-8") as f: gt  = json.load(f)
            with open(gen_file, encoding="utf-8") as f: gen = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] {name}: JSON parse error — {e}")
            continue

        gt_tokens  = tokenize(gt)
        gen_tokens = tokenize(gen)
        metrics    = compute_metrics(gt_tokens, gen_tokens)

        if debug:
            print_debug(name, metrics)

        all_results.append({"wireframe": name, **metrics})

        print(
            f"[OK] {name:<45} "
            f"GT={metrics['total_gt']:>3}  GEN={metrics['total_gen']:>3}  "
            f"matched={metrics['matched']:>3}  "
            f"F1={metrics['f1']:.4f}  Jaccard={metrics['jaccard']:.4f}"
        )

    return all_results


# ─────────────────────────────────────────────────────────────────────────────
# Terminal table
# ─────────────────────────────────────────────────────────────────────────────

def print_table(all_results: list[dict]):
    if not all_results:
        return

    col_name = 45
    sep      = " | "
    header   = (
        f"{'Wireframe':<{col_name}}"
        f"{'GT Tokens':>10}"
        f"{'GEN Tokens':>12}"
        f"{'Matched':>9}"
        f"{'Precision':>11}"
        f"{'Recall':>9}"
        f"{'F1':>8}"
        f"{'Jaccard':>10}"
    )
    divider = "─" * len(header)

    print(f"\n{divider}")
    print(header)
    print(divider)

    for r in all_results:
        print(
            f"{r['wireframe']:<{col_name}}"
            f"{r['total_gt']:>10}"
            f"{r['total_gen']:>12}"
            f"{r['matched']:>9}"
            f"{r['precision']:>11.4f}"
            f"{r['recall']:>9.4f}"
            f"{r['f1']:>8.4f}"
            f"{r['jaccard']:>10.4f}"
        )

    print(divider)

    # ── Macro average (per wireframe equal weight) ───────────────────────────
    n = len(all_results)
    macro_p  = sum(r["precision"] for r in all_results) / n
    macro_r  = sum(r["recall"]    for r in all_results) / n
    macro_f1 = sum(r["f1"]        for r in all_results) / n
    macro_j  = sum(r["jaccard"]   for r in all_results) / n
    print(
        f"{'MACRO AVG':<{col_name}}"
        f"{'':>10}{'':>12}{'':>9}"
        f"{macro_p:>11.4f}"
        f"{macro_r:>9.4f}"
        f"{macro_f1:>8.4f}"
        f"{macro_j:>10.4f}"
    )

    # ── Micro average (global token pool) ────────────────────────────────────
    total_matched = sum(r["matched"]   for r in all_results)
    total_gt      = sum(r["total_gt"]  for r in all_results)
    total_gen     = sum(r["total_gen"] for r in all_results)
    total_union   = total_gt + total_gen - total_matched

    micro_p  = total_matched / total_gen  if total_gen   else 0.0
    micro_r  = total_matched / total_gt   if total_gt    else 0.0
    micro_f1 = (2 * micro_p * micro_r / (micro_p + micro_r)
                if (micro_p + micro_r) else 0.0)
    micro_j  = total_matched / total_union if total_union else 0.0
    print(
        f"{'MICRO AVG':<{col_name}}"
        f"{total_gt:>10}"
        f"{total_gen:>12}"
        f"{total_matched:>9}"
        f"{micro_p:>11.4f}"
        f"{micro_r:>9.4f}"
        f"{micro_f1:>8.4f}"
        f"{micro_j:>10.4f}"
    )
    print(divider)
    print(f"\n  Wireframes evaluated: {n}")
    print(f"  Note: Jaccard ≤ F1 always. Max value = 1.0 (perfect match).\n")


# ─────────────────────────────────────────────────────────────────────────────
# CSV export
# ─────────────────────────────────────────────────────────────────────────────

def save_csv(all_results: list[dict], path: str):
    fields = [
        "wireframe", "total_gt", "total_gen", "matched",
        "precision", "recall", "f1", "jaccard"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for r in all_results:
            writer.writerow({
                "wireframe":  r["wireframe"],
                "total_gt":   r["total_gt"],
                "total_gen":  r["total_gen"],
                "matched":    r["matched"],
                "precision":  f"{r['precision']:.4f}",
                "recall":     f"{r['recall']:.4f}",
                "f1":         f"{r['f1']:.4f}",
                "jaccard":    f"{r['jaccard']:.4f}",
            })
    print(f"[CSV] Saved → {path}")


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Wireframe JSON evaluator — token set F1 + Jaccard"
    )
    parser.add_argument("root",             help="Root directory with wireframe subdirs")
    parser.add_argument("--output", "-o",   help="CSV output path", default=None)
    parser.add_argument("--debug",  "-d",   help="Print matched/FP/FN tokens per wireframe",
                        action="store_true")
    args = parser.parse_args()

    print(f"\nEvaluating: {args.root}\n{'='*60}")
    results = evaluate_directory(args.root, debug=args.debug)

    if not results:
        print("[WARN] No valid wireframe pairs found.")
        return

    print_table(results)

    if args.output:
        save_csv(results, args.output)


if __name__ == "__main__":
    main()
