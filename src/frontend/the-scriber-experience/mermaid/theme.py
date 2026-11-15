# src/frontend/the_scriber_experience/mermaid/theme.py
"""
theme.py

Eigenscribe Mermaid Diagram Theme Generator & Styling Engine.
Provides dark-mode-first Mermaid.js theme configurations, custom class definitions,
diagram wrapping, and HTML preview rendering conforming to The Scriber Experience design system.

Author: Eigenscribe & Scriber Labs
Date: November 15, 2026
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Final, TypeAlias

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    from frontend.colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
except ImportError:
    try:
        from src.frontend.colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
    except ImportError:
        try:
            from ...colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
        except ImportError:
            COLOR_PALETTE = {
                "bright_cyan": "#00f0ff",
                "vivid_cyan": "#00e8ff",
                "electric_blue": "#00a6ff",
                "vivid_sky_blue": "#14b5ff",
                "periwinkle_blue": "#5280ff",
                "bright_purple": "#a855f7",
                "electric_violet": "#5e17eb",
                "bright_violet": "#7c3aed",
                "bright_magenta": "#ff00c3",
                "vivid_pink": "#f72585",
                "success_emerald": "#10b981",
                "warning_amber": "#f7c548",
                "error_crimson": "#d7263d",
                "sky_info": "#38bdf8",
                "charcoal": "#1e293b",
                "ghost_white": "#f8fafc",
            }

            def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
                v = hex_color.removeprefix("#")
                return int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16)

__all__: list[str] = [
    "EIGENSCRIBE_MERMAID_THEME_VARIABLES",
    "EIGENSCRIBE_MERMAID_CLASSES",
    "get_mermaid_theme_variables",
    "get_mermaid_init_directive",
    "get_mermaid_class_defs",
    "wrap_mermaid_diagram",
    "generate_mermaid_flowchart",
    "render_html_preview",
    "save_mermaid_diagram",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

ThemeDict: TypeAlias = dict[str, Any]

# Foundation Eigenscribe Dark Surface Tokens
SURFACE_BG: Final[str] = "#0d1117"
SURFACE_CARD: Final[str] = "#161b22"
SURFACE_ELEVATED: Final[str] = "#21262d"
BORDER_DEFAULT: Final[str] = "#30363d"
BORDER_CYAN_GLOW: Final[str] = "#00e8ff"
TEXT_PRIMARY: Final[str] = "#f0f6fc"
TEXT_MUTED: Final[str] = "#8b949e"
TEXT_ACCENT: Final[str] = "#c8f8ff"

# Default Eigenscribe Mermaid Theme Variables
EIGENSCRIBE_MERMAID_THEME_VARIABLES: Final[dict[str, str]] = {
    # Foundation
    "darkMode": "true",
    "background": SURFACE_BG,
    "primaryColor": SURFACE_CARD,
    "primaryTextColor": TEXT_PRIMARY,
    "primaryBorderColor": BORDER_CYAN_GLOW,
    "lineColor": "#00e8ff",
    "secondaryColor": "#1f2937",
    "tertiaryColor": "#111827",
    # Flowchart / Graph Nodes
    "nodeBorder": "#00e8ff",
    "nodeTextColor": TEXT_PRIMARY,
    "mainBkg": SURFACE_CARD,
    "clusterBkg": "#11161d",
    "clusterBorder": "#38414e",
    "defaultLinkColor": "#14b5ff",
    "titleColor": TEXT_ACCENT,
    "edgeLabelBackground": SURFACE_CARD,
    # Sequence / Actors
    "actorBkg": SURFACE_CARD,
    "actorBorder": "#14b5ff",
    "actorTextColor": TEXT_PRIMARY,
    "actorLineColor": "#5280ff",
    "signalColor": "#00e8ff",
    "signalTextColor": TEXT_PRIMARY,
    "labelBoxBkgColor": SURFACE_CARD,
    "labelBoxBorderColor": "#a855f7",
    "labelTextColor": TEXT_PRIMARY,
    "loopTextColor": TEXT_ACCENT,
    "noteBkgColor": "#1a2234",
    "noteBorderColor": "#38bdf8",
    "noteTextColor": TEXT_PRIMARY,
    "activationBorderColor": "#a855f7",
    "activationBkgColor": "#2d1b4e",
    # Class & State
    "classText": TEXT_PRIMARY,
    "stateBkg": SURFACE_CARD,
    "stateBorder": "#7952f5",
    # Git Graph / Branches
    "git0": "#00e8ff",
    "git1": "#a855f7",
    "git2": "#10b981",
    "git3": "#f7c548",
    "git4": "#ff00c3",
    "git5": "#38bdf8",
    "git6": "#ff783d",
    "git7": "#5280ff",
    "gitBranchLabel0": TEXT_PRIMARY,
    "gitBranchLabel1": TEXT_PRIMARY,
    "gitBranchLabel2": TEXT_PRIMARY,
    "gitBranchLabel3": TEXT_PRIMARY,
    # Pie & Sankey
    "pie1": "#00e8ff",
    "pie2": "#14b5ff",
    "pie3": "#7952f5",
    "pie4": "#a855f7",
    "pie5": "#ff00c3",
    "pie6": "#10b981",
    "pie7": "#f7c548",
    "pieTitleText": TEXT_ACCENT,
    "pieSectionText": "#ffffff",
    "pieLegendText": TEXT_PRIMARY,
}

# Standard Eigenscribe Mermaid Class Definitions (CSS-in-Mermaid)
EIGENSCRIBE_MERMAID_CLASSES: Final[dict[str, str]] = {
    "eigenCyan": "fill:#0c2233,stroke:#00e8ff,stroke-width:2px,color:#f0f6fc",
    "eigenSky": "fill:#0a2540,stroke:#14b5ff,stroke-width:2px,color:#f0f6fc",
    "eigenBlue": "fill:#071c36,stroke:#3a98ff,stroke-width:2px,color:#f0f6fc",
    "eigenPurple": "fill:#201138,stroke:#a855f7,stroke-width:2px,color:#f0f6fc",
    "eigenViolet": "fill:#190e30,stroke:#7952f5,stroke-width:2px,color:#f0f6fc",
    "eigenMagenta": "fill:#2d0822,stroke:#ff00c3,stroke-width:2px,color:#f0f6fc",
    "eigenPink": "fill:#330a21,stroke:#f72585,stroke-width:2px,color:#f0f6fc",
    "eigenEmerald": "fill:#06261d,stroke:#10b981,stroke-width:2px,color:#f0f6fc",
    "eigenAmber": "fill:#2b1d07,stroke:#f7c548,stroke-width:2px,color:#f0f6fc",
    "eigenCrimson": "fill:#330a0f,stroke:#d7263d,stroke-width:2px,color:#f0f6fc",
    "eigenGlass": "fill:#161b22,stroke:#30363d,stroke-width:1.5px,color:#f0f6fc",
    "eigenSubtle": "fill:#0d1117,stroke:#21262d,stroke-width:1px,color:#8b949e",
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API
# -----------------------------------------------------------------------------------------------------------


def get_mermaid_theme_variables(
    variant: str = "dark",
    **overrides: Any,
) -> dict[str, str]:
    """
    Generate the dictionary of Mermaid theme variables matching the Eigenscribe aesthetic.

    Parameters
    ----------
    variant : str, default="dark"
        Theme variant ("dark", "cosmic", or "high-contrast").
    **overrides : Any
        Custom key-value overrides for specific Mermaid theme variables.

    Returns
    -------
    dict[str, str]
        Dictionary of themeVariable options for Mermaid.js.
    """
    config = dict(EIGENSCRIBE_MERMAID_THEME_VARIABLES)

    if variant == "cosmic":
        config.update({
            "background": "#050812",
            "primaryColor": "#0a0f1f",
            "lineColor": "#00ffee",
            "nodeBorder": "#00ffee",
            "clusterBkg": "#080c18",
            "clusterBorder": "#1a2542",
        })
    elif variant == "high-contrast":
        config.update({
            "background": "#000000",
            "primaryColor": "#121212",
            "lineColor": "#00ffff",
            "nodeBorder": "#00ffff",
            "primaryTextColor": "#ffffff",
            "clusterBkg": "#0a0a0a",
            "clusterBorder": "#ffffff",
        })

    config.update(overrides)
    return config


def get_mermaid_init_directive(
    variant: str = "dark",
    **overrides: Any,
) -> str:
    """
    Generate the `%%{init: {...}}%%` directive block for Mermaid diagrams.

    Parameters
    ----------
    variant : str, default="dark"
        Theme variant name ("dark", "cosmic", or "high-contrast").
    **overrides : Any
        Custom overrides for Mermaid theme variables.

    Returns
    -------
    str
        Formatted Mermaid initialization directive string.
    """
    theme_vars = get_mermaid_theme_variables(variant=variant, **overrides)
    init_payload = {
        "theme": "base",
        "themeVariables": theme_vars,
    }
    json_str = json.dumps(init_payload, indent=2)
    return f"%%{{init: {json_str}}}%%\n"


def get_mermaid_class_defs() -> str:
    """
    Generate standard Eigenscribe classDef declarations for use in Mermaid diagrams.

    Returns
    -------
    str
        Multi-line string containing `classDef` definitions.
    """
    lines = ["    %% Eigenscribe Standard Class Definitions"]
    for class_name, style_str in EIGENSCRIBE_MERMAID_CLASSES.items():
        lines.append(f"    classDef {class_name} {style_str};")
    return "\n".join(lines) + "\n"


def wrap_mermaid_diagram(
    diagram_code: str,
    variant: str = "dark",
    include_classes: bool = True,
    title: str | None = None,
    **overrides: Any,
) -> str:
    """
    Wrap a raw Mermaid diagram body with Eigenscribe initialization directives and style classes.

    Parameters
    ----------
    diagram_code : str
        The raw Mermaid diagram string (e.g., `flowchart TD ...`).
    variant : str, default="dark"
        Theme variant.
    include_classes : bool, default=True
        Whether to append the standard Eigenscribe `classDef` declarations.
    title : str | None, optional
        Optional title header comment to prepend.
    **overrides : Any
        Theme variable overrides.

    Returns
    -------
    str
        Fully configured Mermaid diagram string ready for rendering.
    """
    clean_diagram = diagram_code.strip()
    init_directive = get_mermaid_init_directive(variant=variant, **overrides)

    title_block = f"--- title: {title} ---\n" if title else ""
    class_block = f"\n{get_mermaid_class_defs()}" if include_classes else ""

    return f"{title_block}{init_directive}\n{clean_diagram}\n{class_block}".strip() + "\n"


def generate_mermaid_flowchart(
    nodes: list[tuple[str, str, str | None]],
    edges: list[tuple[str, str, str | None]],
    direction: str = "TD",
    title: str | None = None,
    variant: str = "dark",
) -> str:
    """
    Programmatically assemble a styled Eigenscribe flowchart diagram.

    Parameters
    ----------
    nodes : list[tuple[str, str, str | None]]
        List of nodes formatted as (node_id, label, class_name_or_None).
        e.g., `[("A", "Data Input", "eigenCyan"), ("B", "Compute ODE", "eigenPurple")]`
    edges : list[tuple[str, str, str | None]]
        List of edges formatted as (source_id, target_id, edge_label_or_None).
    direction : str, default="TD"
        Flowchart direction: "TD", "LR", "BT", "RL".
    title : str | None, optional
        Diagram title.
    variant : str, default="dark"
        Theme variant.

    Returns
    -------
    str
        Complete styled Mermaid flowchart.
    """
    lines = [f"flowchart {direction}"]

    # Nodes
    for node_id, label, _ in nodes:
        clean_label = label.replace('"', '\\"')
        lines.append(f'    {node_id}["{clean_label}"]')

    lines.append("")

    # Edges
    for src, tgt, edge_label in edges:
        if edge_label:
            clean_edge = edge_label.replace('"', '\\"')
            lines.append(f'    {src} -->|"{clean_edge}"| {tgt}')
        else:
            lines.append(f"    {src} --> {tgt}")

    lines.append("")

    # Class assignments
    class_assignments: list[str] = []
    for node_id, _, cls_name in nodes:
        if cls_name:
            class_assignments.append(f"    class {node_id} {cls_name};")

    if class_assignments:
        lines.extend(class_assignments)

    body = "\n".join(lines)
    return wrap_mermaid_diagram(body, variant=variant, title=title)


def render_html_preview(
    mermaid_code: str,
    title: str = "Eigenscribe Mermaid Diagram",
    theme_variant: str = "dark",
) -> str:
    """
    Generate a standalone HTML page with Mermaid.js CDN to view the diagram in a browser.

    Parameters
    ----------
    mermaid_code : str
        The mermaid diagram code.
    title : str, default="Eigenscribe Mermaid Diagram"
        HTML page title.
    theme_variant : str, default="dark"
        Visual styling backdrop.

    Returns
    -------
    str
        HTML page source code.
    """
    escaped_code = mermaid_code.strip()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #0d1117;
      --card: #161b22;
      --border: #30363d;
      --text: #f0f6fc;
      --cyan: #00e8ff;
    }}
    body {{
      background: radial-gradient(circle at center, #0a0f1f 0%, #050812 60%, #000000 100%);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      margin: 0;
      padding: 2rem;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-sizing: border-box;
    }}
    .container {{
      background: rgba(22, 27, 34, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), 0 0 16px rgba(0, 232, 255, 0.15);
      padding: 2.5rem;
      max-width: 90vw;
      overflow-x: auto;
    }}
    h1 {{
      color: #c8f8ff;
      font-size: 1.5rem;
      font-weight: 600;
      margin-top: 0;
      margin-bottom: 1.5rem;
      text-align: center;
      text-shadow: 0 0 12px rgba(0, 232, 255, 0.4);
    }}
    .mermaid {{
      display: flex;
      justify-content: center;
    }}
  </style>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true, securityLevel: 'loose' }});
  </script>
</head>
<body>
  <div class="container">
    <h1>{title}</h1>
    <div class="mermaid">
{escaped_code}
    </div>
  </div>
</body>
</html>
"""


def save_mermaid_diagram(
    mermaid_code: str,
    file_path: str | Path,
    as_html: bool = False,
    title: str = "Diagram",
) -> Path:
    """
    Save a Mermaid diagram to a file (.mmd, .md, or .html).

    Parameters
    ----------
    mermaid_code : str
        Mermaid diagram code.
    file_path : str | Path
        Destination file path.
    as_html : bool, default=False
        If True, renders and saves as a standalone HTML viewer file.
    title : str, default="Diagram"
        Title if rendered as HTML.

    Returns
    -------
    Path
        The written Path object.
    """
    out_path = Path(file_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if as_html:
        content = render_html_preview(mermaid_code, title=title)
    else:
        content = mermaid_code

    out_path.write_text(content, encoding="utf-8")
    return out_path


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Verify theme generation, init directives, and diagram wrapping."""
    print("💨 Running mermaid theme.py smoke tests...")

    # 1. Theme variables verification
    theme_vars = get_mermaid_theme_variables(variant="dark")
    assert theme_vars["darkMode"] == "true"
    assert theme_vars["primaryBorderColor"] == "#00e8ff"
    assert "nodeBorder" in theme_vars

    cosmic_vars = get_mermaid_theme_variables(variant="cosmic")
    assert cosmic_vars["background"] == "#050812"

    # 2. Init directive check
    directive = get_mermaid_init_directive()
    assert "%%{init:" in directive
    assert "themeVariables" in directive

    # 3. Class defs check
    class_defs = get_mermaid_class_defs()
    assert "classDef eigenCyan" in class_defs
    assert "classDef eigenPurple" in class_defs

    # 4. Wrap diagram check
    raw = "flowchart TD\n    A[Start] --> B[Finish]"
    wrapped = wrap_mermaid_diagram(raw, title="Sample Flow")
    assert "flowchart TD" in wrapped
    assert "%%{init:" in wrapped
    assert "classDef eigenCyan" in wrapped

    # 5. Programmatic generator check
    nodes = [
        ("A", "Initiate Simulation", "eigenCyan"),
        ("B", "Integrate Dynamics", "eigenPurple"),
        ("C", "Compute Observables", "eigenEmerald"),
    ]
    edges = [
        ("A", "B", "Initialize"),
        ("B", "C", "Order Parameter"),
    ]
    generated = generate_mermaid_flowchart(nodes, edges, title="Kuramoto Flow")
    assert "flowchart TD" in generated
    assert 'A["Initiate Simulation"]' in generated
    assert "class A eigenCyan;" in generated

    # 6. HTML preview renderer
    html = render_html_preview(generated, title="Preview Test")
    assert "<!DOCTYPE html>" in html
    assert "mermaid.initialize" in html

    print("✅ mermaid theme.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
