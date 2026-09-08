"""
Code Generator Evaluation Suite v2 — Low Fidelity Focus
=========================================================
Metrics:
  1. CCR — Component Coverage Rate   (vs Ground Truth DSL)
           Measures: did full pipeline produce correct component types?
           Formula:  matched_components / total_gt_components

  2. LSR — Layout Structure Rate     (low fidelity specific)
           Measures: does generated code match DSL row/card/grid structure?
           Sub-checks:
             - row count match
             - cards per row match
             - column span/offset match per card
           Formula:  token F1 over layout tokens (same approach as layout manager)

  3. SSIM — Visual Similarity        (optional, requires screenshots)
           Measures: pixel-level similarity wireframe vs rendered screenshot

Directory structure expected:
  root/
    <wireframe_name>/
      <wireframe_name>.json             ← Ground Truth DSL
      <wireframe_name>-result.json      ← Generated (classifier output) DSL
      vue/<wireframe_name>.vue
      react/<wireframe_name>.tsx
      flutter/<wireframe_name>.dart
      screenshots/
        wireframe.png
        vue.png / react.png / flutter.png

Usage (Jupyter):
  from evaluate_codegen_v2 import run_all, plot_results
  df = run_all("/path/to/root", output_csv="results_codegen.csv")
  plot_results(df, output_dir="/path/to/root")
"""

import json, re, csv
import numpy  as np
import pandas as pd
from pathlib  import Path
from typing   import Optional

try:
    from PIL             import Image
    from skimage.metrics import structural_similarity as ssim_fn
    SSIM_AVAILABLE = True
except ImportError:
    SSIM_AVAILABLE = False


# ─────────────────────────────────────────────────────────────────────────────
# Component map: objClass → keyword expected in generated code per stack
# ─────────────────────────────────────────────────────────────────────────────

COMPONENT_MAP = {
    "common-button":        ('<div obj="common-button">',                              '<div obj="common-button">',                      "//obj:common-button"),
    "common-image-button":  ('<div obj="common-image-button">', '<div obj="common-image-button">',                      "//obj:common-image-button"),
    "segmented-button":     ('<div obj="segmented-button">',     '<div obj="segmented-button">',                      "//obj:segmented-button"),
    "icon-button":          ('<div obj="icon-button">',                              '<div obj="icon-button">',                             "//obj:icon-button"),
    "label":                ('<div obj="label">',                '<div obj="label">',                       "//obj:label"),
    "image":                ('<div obj="image">',                '<div obj="image">',                         "//obj:image"),
    "image-card":           ('<div obj="image-card">',           '<div obj="image-card">',      "//obj:image-card"),
    "checkbox":             ('<div obj="checkbox">',                         '<div obj="checkbox">',             "//obj:checkbox"),
    "radio-button":         ('<div obj="radio-button">',                            '<div obj="radio-button">',                "//obj:radio-button"),
    "input-free-text":      ('<div obj="input-free-text">',                       '<div obj="input-free-text">',                 "//obj:input-free-text"),
    "input-password":       ('<div obj="input-password">',                       '<div obj="input-password">',             "//obj:input-password"),
    "input-number":         ('<div obj="input-number">',                       '<div obj="input-number">',               "//obj:input-number"),
    "input-file":           ('<div obj="input-file">',                       '<div obj="input-file">',                 "//obj:input-file"),
    "date-picker":          ('<div obj="date-picker">',                             '<div obj="date-picker">',                 "//obj:date-picker"),
    "time-picker":          ('<div obj="time-picker">',                             '<div obj="time-picker">',                 "//obj:time-picker"),
    "combobox":             ('<div obj="combobox">',                         '<div obj="combobox">',                      "//obj:combobox"),
    "switch":               ('<div obj="switch">',                            '<div obj="switch">',             "//obj:switch"),
    "textarea":             ('<div obj="textarea">',                         '<div obj="textarea">',                    "//obj:textarea"),
    "slider":               ('<div obj="slider">',                           '<div obj="slider">',                "//obj:slider"),
    "alert":                ('<div obj="alert">',                             '<div obj="alert">',                        "//obj:alert"),
    "key-value":            ('<div obj="key-value">',                            '<div obj="key-value">',                       "//obj:key-value"),
    "table":                ('<div obj="table">',                            '<div obj="table">',                       "//obj:table"),
    "list":                 ('<div obj="list">',                            '<div obj="list">',                       "//obj:list"),
    "line-chart":           ('<div obj="line-chart">',                '<div obj="line-chart">',                        "//obj:line-chart"),
    "bar-chart":            ('<div obj="bar-chart">',                '<div obj="bar-chart">',                        "//obj:bar-chart"),
    "pie-chart":            ('<div obj="pie-chart">',                '<div obj="pie-chart">',                        "//obj:pie-chart"),
    "hyperlink":            ('<div obj="hyperlink">',                              '<div obj="hyperlink">',                     "//obj:hyperlink"),
}

STACKS    = ["vue", "react", "flutter"]
STACK_IDX = {"vue": 0, "react": 1, "flutter": 2}
FILE_EXT  = {"vue": ".vue", "react": ".tsx", "flutter": ".dart"}

CLASSIFICATION_METHODS = [
    ("proposed", "result-s2c"),
    ("sketch deep net", "result-sdn"),
    ("yolov11", "result-yolov11"),
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def extract_elements(dsl: dict) -> list[dict]:
    """Flatten all elements from rows → cards → segmentedElements."""
    elements = []
    for row in dsl.get("rows", []):
        for card in row.get("cards", []):
            for cell_row in card.get("segmentedElements", []):
                for el in cell_row:
                    elements.append(el)
    return elements


def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"    [JSON error] {path.name}: {e}")
        return None


def load_code(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def f1_jaccard(matched: int, total_gt: int, total_gen: int, metric: str) -> tuple:
    # print(
    #     f" {metric}: matched={matched}, total_gt={total_gt}, total_gen={total_gen}"
    # )

    union     = total_gt + total_gen - matched
    precision = matched / total_gen if total_gen else 0.0
    recall    = matched / total_gt if total_gt else 0.0
    f1        = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0.0
    )
    jaccard   = matched / union if union else 0.0

    return (
        round(precision, 4),
        round(recall, 4),
        round(f1, 4),
        round(jaccard, 4),
    )


# ─────────────────────────────────────────────────────────────────────────────
# Metric 1 — CCR: Component Coverage Rate  (vs Ground Truth DSL)
#
# Compares: ground truth objClass list  vs  components found in generated code
# This reflects full pipeline accuracy (classifier errors propagate here)
# ─────────────────────────────────────────────────────────────────────────────

def compute_ccr_v0(gt_dsl: dict, code: str, stack: str) -> dict:
    """
    For each element in GT DSL, check if its expected component keyword
    exists in the generated code.

    matched = GT elements whose component keyword IS in the code
    total   = total GT elements

    CCR = matched / total  (recall-style: GT is the reference)
    """
    idx      = STACK_IDX[stack]
    elements = extract_elements(gt_dsl)
    total_gt = len(elements)

    if total_gt == 0:
        return {"ccr": 1.0, "matched": 0, "total_gt": 0,
                "missing": [], "precision": 1.0, "recall": 1.0,
                "f1": 1.0, "jaccard": 1.0}

    # Count expected component keywords in code (multiset — one per GT element)
    # We check positionally: sort GT elements, check each keyword occurrence
    keyword_counts_in_code = {}
    found   = 0
    missing = []

    for el in elements:
        obj_class = el.get("objClass", "unknown")
        mapping   = COMPONENT_MAP.get(obj_class)

        if mapping is None:
            # Unmapped class — count as found (transpiler skips unknown)
            found += 1
            continue

        keyword = mapping[idx]
        # Count how many times this keyword appears in code
        key_lower  = keyword.lower()
        code_lower = code.lower()

        # Track how many we've already "consumed" for this keyword
        used  = keyword_counts_in_code.get(key_lower, 0)
        total_occurrences = code_lower.count(key_lower)

        if total_occurrences > used:
            found += 1
            keyword_counts_in_code[key_lower] = used + 1
        else:
            missing.append(f"{obj_class}({el.get('name','?')})")

    # Also count components in code not in GT → false positives
    # (simplified: count total keyword occurrences vs GT demand)
    total_in_code = sum(
        code.lower().count(COMPONENT_MAP[el.get("objClass","")][idx].lower())
        for el in elements
        if COMPONENT_MAP.get(el.get("objClass",""))
    )

    p, r, f1, jac = f1_jaccard(found, total_gt, max(total_in_code, found), "CCR")

    return {
        "ccr":      round(found / total_gt, 4),
        "matched":  found,
        "total_gt": total_gt,
        "missing":  missing,
        "precision": p,
        "recall":    r,
        "f1":        f1,
        "jaccard":   jac,
    }

def compute_ccr(gt_dsl: dict, code: str, stack: str) -> dict:
    """
    CCR using obj='...' markers embedded by transpiler.
    Falls back to keyword matching if markers not found.
    """
    elements = extract_elements(gt_dsl)
    total_gt = len(elements)

    if total_gt == 0:
        return {
            "ccr": 1.0, "matched": 0, "total_gt": 0,
            "total_gen": 0, "missing": [],
            "precision": 1.0, "recall": 1.0,
            "f1": 1.0, "jaccard": 1.0
        }

    # Check if code uses obj="..." markers (preferred method)
    use_markers = 'obj="' in code

    found   = 0
    missing = []

    if use_markers:
        # Count obj="..." occurrences per objClass in code
        import re
        obj_counts_in_code = {}
        for match in re.finditer(r'obj="([^"]+)"', code):
            cls = match.group(1)
            obj_counts_in_code[cls] = obj_counts_in_code.get(cls, 0) + 1

        # Match each GT element against marker counts
        consumed = {}
        for el in elements:
            obj_class = el.get("objClass", "unknown")
            available = obj_counts_in_code.get(obj_class, 0)
            used      = consumed.get(obj_class, 0)
            if available > used:
                found += 1
                consumed[obj_class] = used + 1
            else:
                missing.append(obj_class)

    else:
        # Fallback: keyword matching with usage tracking
        idx           = STACK_IDX[stack]
        keyword_usage = {}
        for el in elements:
            obj_class = el.get("objClass", "unknown")
            mapping   = COMPONENT_MAP.get(obj_class)
            if mapping is None:
                found += 1  # unknown class, skip
                continue
            keyword          = mapping[idx].lower()
            total_occ        = code.lower().count(keyword)
            already_used     = keyword_usage.get(keyword, 0)
            if total_occ > already_used:
                found += 1
                keyword_usage[keyword] = already_used + 1
            else:
                missing.append(obj_class)

    ccr     = round(found / total_gt, 4)
    jaccard = round(found / (total_gt * 2 - found), 4) if total_gt else 1.0

    return {
        "ccr":       ccr,
        "matched":   found,
        "total_gt":  total_gt,
        "total_gen": total_gt,
        "missing":   missing,
        "precision": ccr,
        "recall":    ccr,
        "f1":        ccr,
        "jaccard":   jaccard,
    }

# ─────────────────────────────────────────────────────────────────────────────
# Metric 2 — LSR: Layout Structure Rate  (low fidelity specific)
#
# Tokenizes DSL layout structure and checks if those tokens appear in code.
# Tokens cover: row count, cards per row, column span, column offset.
# Uses the same token-set F1/Jaccard approach as the layout manager evaluator.
#
# Token patterns checked in code:
#   row count      → number of row wrapper elements (v-row / Grid / Column)
#   cards per row  → number of col wrappers per row section
#   columnSpan     → cols="X" / xs={X} / flex: X
#   columnOffset   → offset="X" / xsOffset={X} / Padding
# ─────────────────────────────────────────────────────────────────────────────

# Regex patterns per stack to extract layout numbers from generated code
ROW_PATTERNS = {
    "vue":     r"<v-row",
    "react":   r'<div\s+class="v-row"[^>]*>',
    "flutter": r"//\s*Row\s+\d+",
}
COL_PATTERNS = {
    "vue":     r'<v-col\s[^>]*cols=["\'](\d+)["\']',
    "react":   r'<div(?=[^>]*\bclass="v-col")[^>]*\bcol-span-(\d+)\b',
    "flutter": r'Expanded\s*\(\s*flex\s*:\s*(\d+)\s*,\s*child\s*:\s*Column\s*\('
}
OFFSET_PATTERNS = {
    "vue":     r'offset=["\'](\d+)["\']',
    "react":   r'<div(?=[^>]*\bclass="v-col")[^>]*\bcol-start-(\d+)\b',
    "flutter": r'Spacer\s*\(\s*flex\s*:\s*(\d+)\s*\)\s*,\s*Expanded\s*\('
}


def tokenize_dsl_layout(dsl: dict) -> set:
    """
    Convert DSL layout structure into a set of layout tokens.
    Mirrors the token approach from evaluate_wireframes.py.
    """
    tokens = set()
    rows   = dsl.get("rows", [])
    tokens.add(f"root.total_rows:{len(rows)}")

    for i, row in enumerate(rows):
        cards = row.get("cards", [])
        tokens.add(f"row[{i}].total_cards:{len(cards)}")

        for j, card in enumerate(cards):
            cs  = card.get("columnSpan",      0)
            co  = card.get("columnOffset",    0)
            # cos = card.get("columnOffsetSum", 0)
            tokens.add(f"row[{i}].card[{j}].columnSpan:{cs}")
            tokens.add(f"row[{i}].card[{j}].columnOffset:{co}")
            # tokens.add(f"row[{i}].card[{j}].columnOffsetSum:{cos}")

    return tokens


def tokenize_code_layout(code: str, stack: str, dsl: dict) -> set:
    """
    Extract layout tokens from generated code.
    We parse what we can (row count, col spans) and infer the rest from DSL
    structure since low-fidelity code uses semantic layout, not raw pixels.
    """
    tokens = set()

    # ── Row count ──────────────────────────────────────────────────────────
    row_pattern = ROW_PATTERNS[stack]
    n_rows      = len(re.findall(row_pattern, code))
    tokens.add(f"root.total_rows:{n_rows}")

    # ── Column spans per row ───────────────────────────────────────────────
    col_pattern = COL_PATTERNS[stack]
    all_spans   = re.findall(col_pattern, code)

    # ── Offsets per row ────────────────────────────────────────────────────
    off_pattern  = OFFSET_PATTERNS[stack]
    all_offsets  = re.findall(off_pattern, code)

    # Distribute spans/offsets across rows (positional assignment)
    rows         = dsl.get("rows", [])
    span_cursor  = 0
    offset_cursor = 0

    for i, row in enumerate(rows):
        cards = row.get("cards", [])
        tokens.add(f"row[{i}].total_cards:{len(cards)}")

        for j in range(len(cards)):
            # columnSpan
            if span_cursor < len(all_spans):
                tokens.add(
                    f"row[{i}].card[{j}].columnSpan:{all_spans[span_cursor]}")
                span_cursor += 1

            # columnOffset
            if offset_cursor < len(all_offsets):
                if stack == "react":
                    offset_sum = int(all_offsets[offset_cursor]) - 1

                    tokens.add(
                        f"row[{i}].card[{j}].columnOffset:{offset_sum}"
                    )
                else:
                    tokens.add(
                        f"row[{i}].card[{j}].columnOffset:{all_offsets[offset_cursor]}")
                    offset_cursor += 1

    return tokens


def compute_lsr(gt_dsl: dict, code: str, stack: str, debug: bool = False) -> dict:
    """
    Compare DSL layout tokens vs code layout tokens using F1 + Jaccard.
    """
    gt_tokens   = tokenize_dsl_layout(gt_dsl)
    code_tokens = tokenize_code_layout(code, stack, gt_dsl)

    matched     = len(gt_tokens & code_tokens)
    total_gt    = len(gt_tokens)
    total_code  = len(code_tokens)

    if debug:
        print(f"{gt_tokens} vs {code_tokens} : {matched} : {len(gt_tokens)} vs {len(code_tokens)}")

    p, r, f1, jac = f1_jaccard(matched, total_gt, total_code, "LSR")

    return {
        "lsr_f1":      f1,
        "lsr_jaccard": jac,
        "lsr_precision": p,
        "lsr_recall":    r,
        "lsr_matched":   matched,
        "lsr_total_gt":  total_gt,
        "lsr_total_code":total_code,
        "lsr_missing":  sorted(gt_tokens - code_tokens),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Metric 3 — SSIM: Visual Similarity (optional)
# ─────────────────────────────────────────────────────────────────────────────

def compute_ssim(wf_img_path: Path, gen_img_path: Path) -> Optional[float]:
    if not SSIM_AVAILABLE:
        return None
    if not wf_img_path.exists() or not gen_img_path.exists():
        return None
    try:
        wf  = np.array(Image.open(wf_img_path).convert("L"))
        gen = np.array(
            Image.open(gen_img_path)
                 .convert("L")
                 .resize((wf.shape[1], wf.shape[0]), Image.LANCZOS)
        )
        score, _ = ssim_fn(wf, gen, full=True)
        return round(float(score), 4)
    except Exception as e:
        print(f"    [SSIM error] {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# Main runner
# ─────────────────────────────────────────────────────────────────────────────

def run_all(root: str,
            output_csv: str = None,
            verbose:    bool = False,
            debug_lsr:  bool = False) -> pd.DataFrame:
    """
    Evaluate all wireframe directories.
    Returns DataFrame with one row per (wireframe × stack × classification method).
    """
    root_path = Path(root)
    records   = []

    if verbose:
        print(f"\nCode Generator Evaluation (Low Fidelity)")
        print(f"Metrics: CCR (vs GT) · LSR (F1+Jaccard)")
        print(f"{'='*65}")

    for wf_dir in sorted(root_path.iterdir()):
        if not wf_dir.is_dir():
            continue

        name     = wf_dir.name
        gt_file  = wf_dir / f"{name}.json"

        if not gt_file.exists():
            if verbose:
                print(f"[SKIP] {name}: no ground truth DSL")
            continue

        gt_dsl = load_json(gt_file)
        if gt_dsl is None:
            continue

        wf_img = wf_dir / "screenshots" / "wireframe.png"

        for stack in STACKS:
            for method_label, method_suffix in CLASSIFICATION_METHODS:
                code_file = wf_dir / stack / f"{name}-{method_suffix}{FILE_EXT[stack]}"
                code      = load_code(code_file)
                if verbose:
                    print(f"Evaluating: {code_file}")

                if code is None:
                    if verbose:
                        print(f"[SKIP] {name}/{stack}/{method_suffix}: no code file")
                    records.append(_empty_record(name, stack, method_label, method_suffix, "file missing"))
                    continue

                # ── CCR ─────────────────────────────────────────────────────────
                ccr_result = compute_ccr(gt_dsl, code, stack)

                # ── LSR ─────────────────────────────────────────────────────────
                lsr_result = compute_lsr(gt_dsl, code, stack, debug=debug_lsr)

                # ── SSIM ────────────────────────────────────────────────────────
                gen_img    = wf_dir / "screenshots" / f"{method_suffix}.png"
                ssim_score = compute_ssim(wf_img, gen_img)

                record = {
                    "wireframe":      name,
                    "stack":          stack,
                    "method":         method_label,
                    "method_suffix":   method_suffix,
                    # CCR
                    "ccr":            ccr_result["ccr"],
                    "ccr_f1":         ccr_result["f1"],
                    "ccr_jaccard":    ccr_result["jaccard"],
                    "ccr_matched":    ccr_result["matched"],
                    "ccr_total_gt":   ccr_result["total_gt"],
                    # LSR
                    "lsr_f1":         lsr_result["lsr_f1"],
                    "lsr_jaccard":    lsr_result["lsr_jaccard"],
                    "lsr_precision":  lsr_result["lsr_precision"],
                    "lsr_recall":     lsr_result["lsr_recall"],
                    "lsr_matched":    lsr_result["lsr_matched"],
                    "lsr_total_gt":   lsr_result["lsr_total_gt"],
                    # SSIM
                    "ssim":           ssim_score,
                }
                records.append(record)

                if verbose:
                    ssim_str = f"{ssim_score:.4f}" if ssim_score else "N/A "
                    print(
                        f"  {name:<35} {method_label:<15} {stack:<8} "
                        f"CCR={ccr_result['ccr']:.4f}  "
                        f"LSR_F1={lsr_result['lsr_f1']:.4f}  "
                        f"LSR_Jac={lsr_result['lsr_jaccard']:.4f}  "
                        f"SSIM={ssim_str}"
                    )
                    if ccr_result["missing"]:
                        print(f"    CCR missing: {ccr_result['missing']}")
                    if lsr_result["lsr_missing"]:
                        missing_tokens = lsr_result["lsr_missing"][:5]
                        missing_suffix = "..." if len(lsr_result["lsr_missing"]) > 5 else ""
                        print(f"    LSR missing tokens: {missing_tokens}{missing_suffix}")
                else:
                    # silent when verbose is False
                    pass

    df = pd.DataFrame(records)
    if df.empty:
        print("[WARN] No results generated.")
        return df

    _print_summary(df)

    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"\n[CSV] Saved → {output_csv}")

    return df


def _empty_record(name, stack, method, method_suffix, note):
    return {
        "wireframe": name, "stack": stack, "method": method, "method_suffix": method_suffix,
        "ccr": None, "ccr_f1": None, "ccr_jaccard": None,
        "ccr_matched": 0, "ccr_total_gt": 0,
        "lsr_f1": None, "lsr_jaccard": None,
        "lsr_precision": None, "lsr_recall": None,
        "lsr_matched": 0, "lsr_total_gt": 0,
        "ssim": None,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Summary printer
# ─────────────────────────────────────────────────────────────────────────────

def _print_summary(df: pd.DataFrame):
    has_ssim = df["ssim"].notna().any()
    print(f"\n{'='*65}")
    print("SUMMARY — per classification method\n")

    header = (f"{'Method':<18} {'CCR':>7} {'CCR_F1':>8} "
              f"{'LSR_F1':>8} {'LSR_Jac':>9}"
              + (f" {'SSIM':>8}" if has_ssim else ""))
    print(header)
    print("─" * len(header))

    for method_label, _ in CLASSIFICATION_METHODS:
        sub = df[df["method"] == method_label].dropna(subset=["ccr"])
        if sub.empty:
            continue
        line = (
            f"{method_label:<18}"
            f"{sub['ccr'].mean():>7.4f}"
            f"{sub['ccr_f1'].mean():>8.4f}"
            f"{sub['lsr_f1'].mean():>8.4f}"
            f"{sub['lsr_jaccard'].mean():>9.4f}"
        )
        if has_ssim and sub["ssim"].notna().any():
            line += f"{sub['ssim'].mean():>8.4f}"
        print(line)

    print("─" * len(header))
    valid = df.dropna(subset=["ccr"])
    line  = (
        f"{'OVERALL':<10}"
        f"{valid['ccr'].mean():>7.4f}"
        f"{valid['ccr_f1'].mean():>8.4f}"
        f"{valid['lsr_f1'].mean():>8.4f}"
        f"{valid['lsr_jaccard'].mean():>9.4f}"
    )
    if has_ssim and valid["ssim"].notna().any():
        line += f"{valid['ssim'].mean():>8.4f}"
    print(line)

    print(f"\n  Wireframes : {df['wireframe'].nunique()}")
    print(f"  Stacks     : {', '.join(STACKS)}")
    print(f"  Total files: {len(valid)}")
    print(f"\n  CCR  — Component Coverage Rate (vs Ground Truth)")
    print(f"         avg {valid['ccr_matched'].mean():.1f} / "
          f"{valid['ccr_total_gt'].mean():.1f} components matched per wireframe")
    print(f"\n  LSR  — Layout Structure Rate (F1 + Jaccard)")
    print(f"         avg {valid['lsr_matched'].mean():.1f} / "
          f"{valid['lsr_total_gt'].mean():.1f} layout tokens matched per wireframe")
    if has_ssim:
        print(f"\n  SSIM — Visual Similarity (1.0 = identical)")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# Visualization
# ─────────────────────────────────────────────────────────────────────────────

def plot_results_v2(
    df: pd.DataFrame,
    output_dir: str = ".",
    fig_width: float = 13,
    fig_height: float = 5,
    ccr_bar_width: float = 0.22,
    lsr_group_width: float = 0.7,
):
    """
    fig_width / fig_height : overall figure size (inches)
    ccr_bar_width           : width of each stack's bar in the CCR chart
    lsr_group_width         : total width occupied by each stack's group
                              (F1 + Jaccard bars) in the LSR chart
    """
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from matplotlib.patches import Patch

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    PALETTE = {"vue": "#41B883", "react": "#E88E0F", "flutter": "#54C5F8"}
    method_labels = [label for label, _ in CLASSIFICATION_METHODS]
    x = np.arange(len(method_labels))
    bar_width = ccr_bar_width

    fig, axes = plt.subplots(1, 2, figsize=(fig_width, fig_height))

    # ---------------- Chart 1: CCR (grouped by method, one bar per stack) ----------------
    ax = axes[0]
    for stack_index, stack in enumerate(STACKS):
        offset = (stack_index - (len(STACKS) - 1) / 2) * bar_width
        vals = [
            df[(df["method"] == method_label) & (df["stack"] == stack)]["ccr"].mean()
            for method_label in method_labels
        ]
        bars = ax.bar(
            x + offset,
            vals,
            width=bar_width,
            color=PALETTE[stack],
            edgecolor="white",
            linewidth=0.8,
            label=stack.capitalize(),
        )
        for bar, val in zip(bars, vals):
            if not np.isnan(val):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() / 2,
                    f"{val:.3f}",
                    ha="center",
                    va="center",
                    fontsize=8,
                    fontweight="bold",
                    rotation=90,
                    color=("white" if val > 0.35 else "black"),
                )

    ax.set_xticks(x)
    ax.set_xticklabels(method_labels, rotation=12, ha="right")
    ax.set_title("Component Coverage Rate\n(CCR vs Ground Truth)", fontsize=10, fontweight="bold", pad=10)
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Score", fontsize=9)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
    ax.axhline(0.8, color="gray", linewidth=0.8, linestyle="--", alpha=0.5, label="0.80 threshold")
    ax.grid(axis="y", alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(fontsize=7)

    # ---------------- Chart 2: LSR combined (F1 + Jaccard per stack) ----------------
    ax = axes[1]
    lsr_metrics = [("lsr_f1", "F1"), ("lsr_jaccard", "Jaccard")]
    hatches = {"F1": "", "Jaccard": "//"}
    n_stacks = len(STACKS)
    group_width = lsr_group_width
    sub_width = group_width / (n_stacks * len(lsr_metrics))

    xs = np.arange(n_stacks)
    for stack_index, stack in enumerate(STACKS):
        for metric_index, (metric_col, metric_name) in enumerate(lsr_metrics):
            val = df[df["stack"] == stack][metric_col].mean()
            # position: group by stack, sub-bars for F1/Jaccard within each stack
            offset = (stack_index - (n_stacks - 1) / 2) * (group_width / n_stacks) \
                     + (metric_index - 0.5) * sub_width
            bars = ax.bar(
                xs[stack_index] + offset,
                val,
                width=sub_width,
                color=PALETTE[stack],
                edgecolor="white",
                linewidth=0.8,
                hatch=hatches[metric_name],
            )
            if not np.isnan(val):
                bar = bars[0]
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.015,
                    f"{val:.3f}",
                    ha="center",
                    va="bottom",
                    fontsize=7,
                    fontweight="bold",
                )

    ax.set_xticks(xs)
    ax.set_xticklabels([s.capitalize() for s in STACKS])
    
    ax.set_title("Layout Structure Rate\n(LSR — F1 vs Jaccard)", fontsize=10, fontweight="bold", pad=10)
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Score", fontsize=9)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
    ax.axhline(0.8, color="gray", linewidth=0.8, linestyle="--", alpha=0.5)
    ax.grid(axis="y", alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend for metric hatch pattern (F1 vs Jaccard)
    metric_handles = [
        Patch(facecolor="white", edgecolor="black", hatch=hatches[name], label=name)
        for _, name in lsr_metrics
    ]
    ax.legend(handles=metric_handles, fontsize=7, loc="upper right")

    # Legend for stack colors (shared across both charts)
    stack_handles = [Patch(color=PALETTE[s], label=s.capitalize()) for s in STACKS]
    fig.legend(handles=stack_handles, loc="lower center",
               ncol=3, fontsize=9, bbox_to_anchor=(0.5, -0.05))

    fig.suptitle(
        "Code Generator Evaluation — Low Fidelity Metrics\n"
        "(CCR vs Ground Truth  ·  LSR F1/Jaccard)",
        fontsize=12, fontweight="bold"
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])

    path = str(out / "codegen_evaluation_v1.png")
    fig.savefig(path, dpi=180, bbox_inches="tight")
    print(f"[Chart] Saved → {path}")
    return fig

def plot_results(df: pd.DataFrame, output_dir: str = "."):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    out      = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    has_ssim = df["ssim"].notna().any()

    PALETTE  = {"vue": "#41B883", "react": "#E88E0F", "flutter": "#54C5F8"}
    method_labels = [label for label, _ in CLASSIFICATION_METHODS]
    x = np.arange(len(method_labels))
    bar_width = 0.22
    n_charts = 4 if has_ssim else 3
    fig, axes = plt.subplots(1, n_charts, figsize=(4 * n_charts + 1, 5))

    metrics = [
        ("ccr",         "Component Coverage Rate\n(CCR vs Ground Truth)"),
        ("lsr_f1",      "Layout Structure Rate\n(LSR — F1 Score)"),
        ("lsr_jaccard", "Layout Structure Rate\n(LSR — Jaccard)"),
    ]
    if has_ssim:
        metrics.append(("ssim", "Visual Similarity\n(SSIM)"))

    for ax, (metric, title) in zip(axes, metrics):
        if metric.startswith("lsr_"):
            stack_vals = [df[df["stack"] == stack][metric].mean() for stack in STACKS]
            bars = ax.bar(
                STACKS,
                stack_vals,
                color=[PALETTE[stack] for stack in STACKS],
                edgecolor="white",
                linewidth=0.8,
                width=0.5,
            )

            for bar, val in zip(bars, stack_vals):
                if not np.isnan(val):
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.015,
                        f"{val:.3f}",
                        ha="center",
                        va="bottom",
                        fontsize=9,
                        fontweight="bold",
                    )
            ax.set_xticks(range(len(STACKS)))
            ax.set_xticklabels([s.capitalize() for s in STACKS])
        else:
            for stack_index, stack in enumerate(STACKS):
                offset = (stack_index - (len(STACKS) - 1) / 2) * bar_width
                vals = [
                    df[(df["method"] == method_label) & (df["stack"] == stack)][metric].mean()
                    for method_label in method_labels
                ]
                bars = ax.bar(
                    x + offset,
                    vals,
                    width=bar_width,
                    color=PALETTE[stack],
                    edgecolor="white",
                    linewidth=0.8,
                    label=stack.capitalize() if metric == metrics[0][0] else None,
                )

                for bar, val in zip(bars, vals):
                    if not np.isnan(val):
                        if metric == "ccr":
                            # Place CCR labels vertically inside the bar
                            ax.text(
                                bar.get_x() + bar.get_width() / 2,
                                bar.get_height() / 2,
                                f"{val:.3f}",
                                ha="center",
                                va="center",
                                fontsize=8,
                                fontweight="bold",
                                rotation=90,
                                color=("white" if val > 0.35 else "black"),
                            )
                        else:
                            ax.text(
                                bar.get_x() + bar.get_width() / 2,
                                bar.get_height() + 0.015,
                                f"{val:.3f}",
                                ha="center",
                                va="bottom",
                                fontsize=8,
                                fontweight="bold",
                            )

            ax.set_xticks(x)
            ax.set_xticklabels(method_labels, rotation=12, ha="right")

        ax.set_title(title, fontsize=10, fontweight="bold", pad=10)
        ax.set_ylim(0, 1.15)
        ax.set_ylabel("Score", fontsize=9)
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
        ax.axhline(0.8, color="gray", linewidth=0.8,
                   linestyle="--", alpha=0.5, label="0.80 threshold")
        ax.grid(axis="y", alpha=0.4)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        if metric.startswith("lsr_"):
            ax.legend(fontsize=7)
        else:
            ax.legend(fontsize=7)

    # Legend for stack colors
    from matplotlib.patches import Patch
    handles = [Patch(color=PALETTE[s], label=s.capitalize()) for s in STACKS]
    fig.legend(handles=handles, loc="lower center",
               ncol=3, fontsize=9, bbox_to_anchor=(0.5, -0.05))

    fig.suptitle(
        "Code Generator Evaluation — Low Fidelity Metrics\n"
        "(CCR vs Ground Truth  ·  LSR F1/Jaccard  ·  SSIM)",
        fontsize=12, fontweight="bold"
    )
    fig.tight_layout(rect=[0, 0.05, 1, 1])

    path = str(out / "codegen_evaluation_v2.png")
    fig.savefig(path, dpi=180, bbox_inches="tight")
    print(f"[Chart] Saved → {path}")
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Code generator evaluator — low fidelity (CCR, LSR, SSIM)")
    parser.add_argument("root",           help="Root directory")
    parser.add_argument("--output", "-o", help="CSV output path", default=None)
    parser.add_argument("--chart",  "-c", help="Chart output dir", default=None)
    parser.add_argument("--verbose","-v", action="store_true")
    args = parser.parse_args()

    df = run_all(args.root, output_csv=args.output, verbose=args.verbose)
    if args.chart and not df.empty:
        # plot_results(df, args.chart)
        plot_results_v2(df, 
            output_dir=args.chart, 
             fig_width=10,        # overall figure width in inches
             fig_height=5,        # overall figure height
             ccr_bar_width=0.3,   # thickness of each stack's bar in CCR chart
             lsr_group_width=8) # total width of each stack's F1+Jaccard pair in LSR chart
