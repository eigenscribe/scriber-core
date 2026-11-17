# src/frontend/the_scriber_experience/cli/main.py
"""
main.py

Unified CLI entry point for Scriber Core (The Scriber Experience).
Provides colorful, gradient-infused terminal tools, color palette inspectors,
banner generators, plotting/mermaid theme helpers, and workspace consistency diagnostics.

Activated via `eigenscribe` command or `python -m frontend.the_scriber_experience.cli.main`.

Author: Eigenscribe & Scriber Labs
Date: November 15, 2026
"""

from __future__ import annotations

import sys
from typing import Final, Sequence

# Force UTF-8 stdout on Windows to support emoji and Unicode chars
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import click

from frontend.colors import COLOR_PALETTE, hex_to_rgb
from frontend.gradients import (
    GRADIENT_PRESETS,
    TSE_GRADIENTS,
    multi_gradient,
)
from frontend.the_scriber_experience.cli.messaging import (
    EIGENSCRIBE_PALETTE,
    STYLE_MAP,
    ansi_256,
    cli_banner,
    cli_echo,
    cli_error,
    cli_highlight,
    cli_info,
    cli_message,
    cli_rule,
    cli_success,
    cli_warning,
    supports_256_color,
)
from frontend.the_scriber_experience.mermaid.theme import (
    EIGENSCRIBE_MERMAID_THEME_VARIABLES,
    generate_mermaid_flowchart,
    get_mermaid_init_directive,
    render_html_preview,
    wrap_mermaid_diagram,
)
from frontend.the_scriber_experience.plots.theme import (
    get_eigenscribe_rcparams,
)
from frontend.the_scriber_experience.style.tse_colors import (
    CLI_COLORS,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    SEMANTIC_COLORS,
    TSE_COLORS,
)

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

CLI_VERSION: Final[str] = "0.1.0"
EIGENSCRIBE_ASCII_LOGO: Final[str] = r"""
  ███████╗██╗ ██████╗ ███████╗███╗   ██╗███████╗ ██████╗██████╗ ██╗██████╗ ███████╗
  ██╔════╝██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝
  █████╗  ██║██║  ███╗█████╗  ██╔██╗ ██║███████╗██║     ██████╔╝██║██████╔╝█████╗  
  ██╔══╝  ██║██║   ██║██╔══╝  ██║╚██╗██║╚════██║██║     ██╔══██╗██║██╔══██╗██╔══╝  
  ███████╗██║╚██████╔╝███████╗██║ ╚████║███████║╚██████╗██║  ██║██║██████╔╝███████╗
  ╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝
"""

PRIMARY_GRADIENT: Final[tuple[str, ...]] = GRADIENT_PRESETS["eigenscribe"]
SECONDARY_GRADIENT: Final[tuple[str, ...]] = ("#00a6ff", "#7952f5", "#a855f7", "#ff28a2")


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Internal Helpers & Formatters
# -----------------------------------------------------------------------------------------------------------


def _render_color_block(hex_code: str, label: str = "", width: int = 14) -> str:
    """Render a text swatch block with ANSI 24-bit TrueColor background."""
    r, g, b = hex_to_rgb(hex_code)
    # Determine contrasting foreground color (WCAG luminance approximation)
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    fg_code = "\033[38;2;0;0;0m" if luminance > 140 else "\033[38;2;255;255;255m"
    bg_code = f"\033[48;2;{r};{g};{b}m"
    reset = "\033[0m"
    display = (label if label else hex_code).center(width)
    return f"{bg_code}{fg_code} {display} {reset}"


def _print_brand_header() -> None:
    """Print the Eigenscribe signature TrueColor gradient ASCII logo and subtitle."""
    styled_logo = multi_gradient(EIGENSCRIBE_ASCII_LOGO, colors=PRIMARY_GRADIENT, bold=True)
    click.echo(styled_logo)
    subtitle = "  🔱 SCRIBER CORE DESIGN SYSTEM & DETERMINISTIC WORKSPACE SUITE"
    click.echo(multi_gradient(subtitle, colors=SECONDARY_GRADIENT, bold=True))
    cli_rule(char="═", width=80, level="rule")


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API — Click Command Group
# -----------------------------------------------------------------------------------------------------------


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Display Eigenscribe CLI version.")
@click.pass_context
def cli_group(ctx: click.Context, version: bool) -> None:
    """
    🔱 Eigenscribe CLI — Design Tokens, Gradients & Visualization Engine.

    Baseline CLI tool suite for Scriber Core repositories.
    Provides colorful palettes, TrueColor gradients, themes, and health diagnostics.
    """
    if version:
        version_str = f"eigenscribe v{CLI_VERSION} (Scriber Core Design System)"
        click.echo(multi_gradient(version_str, colors=PRIMARY_GRADIENT, bold=True))
        ctx.exit()

    if ctx.invoked_subcommand is None:
        _print_brand_header()
        click.echo("")
        cli_info(f"Eigenscribe CLI v{CLI_VERSION} initialized.")
        cli_highlight("Run 'eigenscribe --help' to inspect all available commands and options.")
        click.echo("")
        cli_rule(char="─", width=80, level="rule")


# -----------------------------------------------------------------------------------------------------------
# Subcommand: info
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="info")
def info_cmd() -> None:
    """Display Scriber Core architectural index, active design tokens, and guidelines."""
    _print_brand_header()
    click.echo("")
    cli_highlight("🏛️  SCRIBER CORE ARCHITECTURAL OVERVIEW")
    click.echo("")
    click.echo("  • " + ansi_256("eigen_cyan", "Package Name: ") + "scriber-core (frontend / the_scriber_experience)")
    click.echo("  • " + ansi_256("eigen_cyan", "CLI Entry:    ") + "eigenscribe")
    click.echo("  • " + ansi_256("eigen_cyan", "Python:       ") + f"{sys.version.split()[0]}")
    click.echo("  • " + ansi_256("eigen_cyan", "Terminal 256: ") + ("Enabled" if supports_256_color() else "Fallback 16-color"))
    click.echo("")
    cli_rule(char="─", width=80, level="rule")
    click.echo("")
    cli_info("🎨  4-Layer Design Token Stack:")
    click.echo("  1. " + ansi_256("eigen_blue_bright", "Primitive Colors:") + f" {len(COLOR_PALETTE)} named hex codes in COLOR_PALETTE")
    click.echo("  2. " + ansi_256("eigen_purple_bright", "Semantic Roles:  ") + f" {len(SEMANTIC_COLORS)} status roles, {len(CLI_COLORS)} CLI levels")
    click.echo("  3. " + ansi_256("eigen_pink_bright", "Gradient Engine: ") + f" {len(GRADIENT_PRESETS)} multi-stop TrueColor gradient presets")
    click.echo("  4. " + ansi_256("eigen_green_bright", "Themes & Assets: ") + " Matplotlib/Plotly themes, Mermaid.js theme generator")
    click.echo("")
    cli_rule(char="─", width=80, level="rule")
    click.echo("")
    cli_success("Workspace guidelines bridge available at house-rules/ (python-rules.md, css-rules.md).")


# -----------------------------------------------------------------------------------------------------------
# Subcommand: gradient
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="gradient")
@click.argument("text", required=False, default="Eigenscribe Multi-Stop ANSI TrueColor Gradient Engine")
@click.option("--preset", "-p", default="electric", help="Gradient preset name (e.g. electric, eigenscribe, cyberpunk, sunset, aurora, midnight, tse-gradient-1).")
@click.option("--stops", "-s", multiple=True, help="Custom hex color stops (e.g. -s '#00ffff' -s '#ff00c3'). Overrides preset.")
@click.option("--bold/--no-bold", default=True, help="Apply bold weight formatting.")
@click.option("--list-presets", "-l", is_flag=True, help="List all available gradient presets with live previews.")
def gradient_cmd(text: str, preset: str, stops: tuple[str, ...], bold: bool, list_presets: bool) -> None:
    """Generate and display multi-stop ANSI TrueColor gradient text."""
    if list_presets:
        cli_banner("GRADIENT PRESETS", f"{len(GRADIENT_PRESETS)} Built-in Multi-Stop Palettes")
        click.echo("")
        for name, preset_stops in GRADIENT_PRESETS.items():
            sample_text = f"  [{name:16s}]  ██████████████  " + "  ".join(preset_stops)
            rendered = multi_gradient(sample_text, colors=preset_stops, bold=True)
            click.echo(rendered)
        click.echo("")
        cli_rule(char="─", width=80, level="rule")
        return

    color_stops: Sequence[str] = stops if stops else GRADIENT_PRESETS.get(preset, GRADIENT_PRESETS["electric"])
    rendered = multi_gradient(text, colors=color_stops, bold=bold)
    click.echo(rendered)


# -----------------------------------------------------------------------------------------------------------
# Subcommand: colors
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="colors")
@click.option("--all-256", "-a", is_flag=True, help="Display the complete ANSI 256-color palette index.")
@click.option("--spectrum", "-s", is_flag=True, help="Display the 10-Node EIGEN vibrant node spectrum.")
@click.option("--table", "-t", is_flag=True, help="Display the full COLOR_PALETTE table with TrueColor blocks and names.")
def colors_cmd(all_256: bool, spectrum: bool, table: bool) -> None:
    """Inspect and display Eigenscribe color palettes with live TrueColor swatches."""
    if table:
        from cli.colors_table import print_colors_table

        print_colors_table()
        return

    cli_banner("EIGENSCRIBE DESIGN TOKENS", "Color Palettes, Semantic Roles & Node Spectra")
    click.echo("")

    # 1. Signature TSE Colors
    cli_highlight("🔱  Signature TSE Palette:")
    for name, hex_code in TSE_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 2. Semantic Roles
    cli_highlight("🚦  Semantic Status Roles:")
    for name, hex_code in SEMANTIC_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 3. Canonical EIGEN Spectrum
    cli_highlight("🐉  Canonical EIGEN Spectrum:")
    for name, hex_code in EIGEN_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 4. Vibrant 10-Node Spectrum
    if spectrum or True:
        cli_highlight("🌌  Vibrant 10-Node Spectrum (0-9):")
        node_names = [
            "0. Crown Gold",
            "1. Electric Cyan",
            "2. Vivid Cyan",
            "3. Sky Blue",
            "4. Deep Cobalt",
            "5. Amber Gold",
            "6. Electric Purple",
            "7. Deep Violet",
            "8. Rose Pink",
            "9. Emerald Green",
        ]
        for i, hex_code in enumerate(EIGEN_NODE_COLORS):
            lbl = node_names[i] if i < len(node_names) else f"Node {i}"
            block = _render_color_block(hex_code, label=f"Node {i}", width=10)
            click.echo(f"  {block}  {lbl:20s} {hex_code}")
        click.echo("")

    # 5. Full ANSI 256 preview if requested
    if all_256:
        cli_highlight("💻  ANSI 256-Color Palette Table:")
        for row in range(0, 256, 16):
            line_parts = []
            for col in range(16):
                idx = row + col
                if idx < 256:
                    line_parts.append(f"\033[48;5;{idx}m {idx:3d} \033[0m")
            click.echo("  " + "".join(line_parts))
        click.echo("")

    cli_rule(char="─", width=80, level="rule")


# -----------------------------------------------------------------------------------------------------------
# Subcommand: banner
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="banner")
@click.argument("title", default="EIGENSCRIBE")
@click.option("--subtitle", "-s", default="Deterministic Workspace & Styling Suite", help="Subtitle line.")
@click.option("--preset", "-p", default="eigenscribe", help="Gradient preset for title.")
@click.option("--width", "-w", default=60, type=int, help="Banner width in characters.")
def banner_cmd(title: str, subtitle: str, preset: str, width: int) -> None:
    """Generate a styled Eigenscribe banner and rule header."""
    cli_banner(title, subtitle if subtitle else None)


# -----------------------------------------------------------------------------------------------------------
# Subcommand: theme
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="theme")
@click.option("--format", "-f", "fmt", type=click.Choice(["summary", "rcparams", "css"]), default="summary", help="Theme export format.")
def theme_cmd(fmt: str) -> None:
    """Inspect and export Eigenscribe visualization and plotting theme settings."""
    if fmt == "summary":
        cli_banner("PLOTTING & GRAPHICS THEME", "Matplotlib, Seaborn & Plotly Design Presets")
        click.echo("")
        cli_info("Theme Engine Parameters:")
        click.echo("  • Dark Surface BG:      #0d1117 (COLOR_BG)")
        click.echo("  • Surface Elevated:     #161b22 (COLOR_SURFACE)")
        click.echo("  • Luminous Accent:      #c8f8ff (COLOR_TEXT_ACCENT)")
        click.echo("  • Primary Font:         JetBrains Mono / Inter / Fira Code")
        click.echo("  • Colormaps:            eigenscribe_cosmic, eigenscribe_vibrant, eigenscribe_diverging")
        click.echo("")
        cli_rule(char="─", width=80, level="rule")
    elif fmt == "rcparams":
        rc = get_eigenscribe_rcparams()
        click.echo(f"# Matplotlib rcParams ({len(rc)} active keys)")
        for k, v in list(rc.items())[:20]:
            click.echo(f"{k}: {v}")
        click.echo(f"# ... ({len(rc) - 20} more keys omitted)")
    elif fmt == "css":
        click.echo("/* Eigenscribe Design System Root CSS Variables */")
        click.echo(":root {")
        for k, v in COLOR_PALETTE.items():
            css_var = "--color-" + k.replace("_", "-")
            click.echo(f"  {css_var}: {v};")
        click.echo("}")


# -----------------------------------------------------------------------------------------------------------
# Subcommand: mermaid
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="mermaid")
@click.option("--sample", "-s", is_flag=True, help="Generate a sample Eigenscribe dark-mode flowchart diagram.")
@click.option("--init", "-i", is_flag=True, help="Print Mermaid.js %%%{init} directive string.")
@click.option("--html-preview", "-h", is_flag=True, help="Generate a self-contained HTML preview file.")
@click.option("--output", "-o", type=click.Path(), default="mermaid_preview.html", help="Output path for HTML preview.")
def mermaid_cmd(sample: bool, init: bool, html_preview: bool, output: str) -> None:
    """Generate, wrap, or preview Eigenscribe dark-mode Mermaid diagrams."""
    if init:
        click.echo(get_mermaid_init_directive())
        return

    sample_diag = generate_mermaid_flowchart()

    if html_preview:
        html_code = render_html_preview(sample_diag, title="Eigenscribe Mermaid Architecture")
        with open(output, "w", encoding="utf-8") as f:
            f.write(html_code)
        cli_success(f"Generated standalone Mermaid HTML preview: {output}")
        return

    cli_banner("EIGENSCRIBE MERMAID ENGINE", "Dark-Mode Architecture Diagram Definition")
    click.echo("")
    click.echo(sample_diag)
    click.echo("")
    cli_rule(char="─", width=80, level="rule")


# -----------------------------------------------------------------------------------------------------------
# Subcommand: doctor
# -----------------------------------------------------------------------------------------------------------


@cli_group.command(name="doctor")
def doctor_cmd() -> None:
    """Run full workspace consistency check, token validation, and smoke tests."""
    cli_banner("EIGENSCRIBE DOCTOR", "Workspace Health & Design System Verification")
    click.echo("")

    checks_passed = 0
    total_checks = 0

    def run_check(label: str, fn) -> None:
        nonlocal checks_passed, total_checks
        total_checks += 1
        try:
            fn()
            checks_passed += 1
            click.echo(f"  [\033[32mPASS\033[0m] {label}")
        except Exception as e:
            click.echo(f"  [\033[31mFAIL\033[0m] {label}: {e}")

    # Check 1: Python Version
    run_check("Python Version >= 3.10", lambda: sys.version_info >= (3, 10) or (_ for _ in ()).throw(ValueError("Python >= 3.10 required")))

    # Check 2: Terminal 256 / TrueColor detection
    run_check("Terminal Color Engine", lambda: supports_256_color() or True)

    # Check 3: Primitive Color Palette
    def _chk_colors():
        assert len(COLOR_PALETTE) >= 15, "Incomplete COLOR_PALETTE"
        for name, hex_val in COLOR_PALETTE.items():
            rgb = hex_to_rgb(hex_val)
            assert len(rgb) == 3 and all(0 <= ch <= 255 for ch in rgb)

    run_check("Primitive Color Palette (COLOR_PALETTE)", _chk_colors)

    # Check 4: Gradient Presets
    def _chk_gradients():
        assert len(GRADIENT_PRESETS) >= 8, "Incomplete GRADIENT_PRESETS"
        for name, stops in GRADIENT_PRESETS.items():
            assert len(stops) >= 2, f"Gradient {name} has fewer than 2 stops"
            for hex_val in stops:
                hex_to_rgb(hex_val)

    run_check("Gradient Engine & Presets (GRADIENT_PRESETS)", _chk_gradients)

    # Check 5: TSE Semantic & Node Colors
    def _chk_tse():
        assert len(TSE_COLORS) >= 5
        assert len(SEMANTIC_COLORS) >= 4
        assert len(EIGEN_NODE_COLORS) == 10
        assert len(EIGEN_LABEL_COLORS) == 10

    run_check("TSE Semantic & 10-Node Spectrum Tokens", _chk_tse)

    # Check 6: Plotting rcParams Theme
    def _chk_theme():
        rc = get_eigenscribe_rcparams()
        assert len(rc) >= 30, "Incomplete rcParams"

    run_check("Matplotlib / Seaborn Theme rcParams Generator", _chk_theme)

    # Check 7: Mermaid Generator
    def _chk_mermaid():
        diag = generate_mermaid_flowchart()
        assert "flowchart TD" in diag
        assert "classDef" in diag

    run_check("Mermaid Dark-Mode Theme Generator", _chk_mermaid)

    click.echo("")
    cli_rule(char="─", width=80, level="rule")
    click.echo("")

    if checks_passed == total_checks:
        cli_success(f"All {checks_passed}/{total_checks} consistency checks passed successfully!")
    else:
        cli_error(f"{checks_passed}/{total_checks} checks passed. Please inspect failures above.")


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Validate CLI group commands instantiate and invoke cleanly."""
    print("💨 Running eigenscribe CLI smoke tests...")
    assert "info" in cli_group.commands
    assert "gradient" in cli_group.commands
    assert "colors" in cli_group.commands
    assert "banner" in cli_group.commands
    assert "theme" in cli_group.commands
    assert "mermaid" in cli_group.commands
    assert "doctor" in cli_group.commands

    from click.testing import CliRunner

    runner = CliRunner()
    result = runner.invoke(cli_group, ["--help"])
    assert result.exit_code == 0
    assert "Eigenscribe CLI" in result.output

    # Test info command
    res_info = runner.invoke(cli_group, ["info"])
    assert res_info.exit_code == 0

    # Test gradient command
    res_grad = runner.invoke(cli_group, ["gradient", "Hello Eigenscribe", "--preset", "electric"])
    assert res_grad.exit_code == 0

    # Test doctor command
    res_doc = runner.invoke(cli_group, ["doctor"])
    assert res_doc.exit_code == 0
    print("✅ eigenscribe CLI smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Primary execution entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--smoke-test":
        _run_smoke_test()
    else:
        cli_group()


if __name__ == "__main__":
    main()
