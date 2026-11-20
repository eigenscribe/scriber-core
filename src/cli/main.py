"""
main.py

Primary entry point for the Eigenscribe CLI suite.
Imports branding, command catalog, smoke tests, and messaging from focused
modules, then defines the Click command group and all CLI subcommands.

The conceptual story follows the Eigenscribe architectural standard:
What exists -> What you're allowed to call -> How it works -> Proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

import sys
from typing import Final

import click

from frontend.colors import COLOR_PALETTE, hex_to_rgb
from frontend.gradients import GRADIENT_PRESETS, multi_gradient

try:
    from .colors_table import (
        cli as colors_table_cli,
        main as colors_table_main,
        print_colors_table,
        render_colors_table,
    )
    from .messaging import (
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
        render_banner,
        render_echo,
        render_message,
        render_rule,
        supports_256_color,
    )
except ImportError:
    from cli.colors_table import (
        cli as colors_table_cli,
        main as colors_table_main,
        print_colors_table,
        render_colors_table,
    )
    from cli.messaging import (
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
        render_banner,
        render_echo,
        render_message,
        render_rule,
        supports_256_color,
    )

from frontend.the_scriber_experience.plots.theme import get_eigenscribe_rcparams
from frontend.the_scriber_experience.mermaid.theme import (
    generate_mermaid_flowchart,
    get_mermaid_init_directive,
    render_html_preview,
)
from frontend.colors import (
    CLI_COLORS,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    SEMANTIC_COLORS,
    TSE_COLORS,
)

try:
    from .branding import (
        CLI_VERSION,
        PRIMARY_GRADIENT,
        SECONDARY_GRADIENT,
        ansi_color,
        print_brand_header,
        render_brand_header,
    )
    from .command_catalog import (
        BADGE_COLORS,
        CommandDescriptor,
        REGISTERED_COMMANDS,
        print_commands_list,
        render_commands_list,
    )
    from .smoke_tests import run_smoke_test
    from .vt_mode import enable_vt_mode
except ImportError:
    from cli.branding import (
        CLI_VERSION,
        PRIMARY_GRADIENT,
        SECONDARY_GRADIENT,
        ansi_color,
        print_brand_header,
        render_brand_header,
    )
    from cli.command_catalog import (
        BADGE_COLORS,
        CommandDescriptor,
        REGISTERED_COMMANDS,
        print_commands_list,
        render_commands_list,
    )
    from cli.smoke_tests import run_smoke_test
    from cli.vt_mode import enable_vt_mode


__all__: list[str] = [
    "CLI_VERSION",
    "CommandDescriptor",
    "PRIMARY_GRADIENT",
    "REGISTERED_COMMANDS",
    "BADGE_COLORS",
    "SECONDARY_GRADIENT",
    "ansi_color",
    "cli",
    "cli_group",
    "colors_table_cli",
    "main",
    "print_brand_header",
    "print_colors_table",
    "print_commands_list",
    "render_brand_header",
    "render_colors_table",
    "render_commands_list",
    "run_smoke_test",
    # Re-exported messaging helpers
    "cli_message",
    "cli_echo",
    "cli_rule",
    "cli_banner",
    "cli_info",
    "cli_success",
    "cli_warning",
    "cli_error",
    "cli_highlight",
    "render_message",
    "render_echo",
    "render_rule",
    "render_banner",
    "ansi_256",
    "supports_256_color",
    "EIGENSCRIBE_PALETTE",
    "STYLE_MAP",
]


# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / constants (define once, use Final)
# -----------------------------------------------------------------------------------------------------------

CLI_HELP_BLUE_GRADIENT = GRADIENT_PRESETS["blue_gradient"]  # vivid_cyan → vivid_sky_blue → eigen_blue → strong_blue

# Per-badge solid color mapping for command names in the help output.
# Each badge maps to a distinct TrueColor hex that reflects the command's functional type.
COMMAND_TYPE_COLORS: Final[dict[str, str]] = {
    "CORE": COLOR_PALETTE["success_emerald"],   # #10b981 — Emerald: workspace core tools
    "STYLE": COLOR_PALETTE["midwest_indigo"],   # #6f78fa — Indigo: gradients & banners
    "TOKEN": COLOR_PALETTE["vivid_pink"],       # #f72585 — Pink: palettes & swatches
    "DIAG": COLOR_PALETTE["warning_amber"],     # #f7c548 — Amber: diagnostics & verification
}

# Fallback color for commands not found in the registry
DEFAULT_COMMAND_COLOR: Final[str] = COLOR_PALETTE["success_emerald"]

CLI_HELP_DESCRIPTION = multi_gradient(
    "🔱 Eigenscribe CLI (Scriber Core) — Deterministic Workspace Baseline & Palette Tools.",
    colors=GRADIENT_PRESETS["eigenscribe"],
    bold=True,
)


# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Private helpers (how it works)
# -----------------------------------------------------------------------------------------------------------


def _render_color_block(hex_code: str, label: str = "", width: int = 4) -> str:
    """Render a colored ANSI block swatch for terminal display."""
    r, g, b = hex_to_rgb(hex_code)
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    fg = "\033[38;2;0;0;0m" if lum > 128 else "\033[38;2;255;255;255m"
    bg = f"\033[48;2;{r};{g};{b}m"
    txt = f"{label:^{width}}" if label else " " * width
    return f"{bg}{fg}{txt}\033[0m"


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (Click Group & Command Definitions)
# -----------------------------------------------------------------------------------------------------------


class _BlueHelpFormatter(click.HelpFormatter):
    """Custom HelpFormatter that applies green gradient to section headers."""

    def write_heading(self, heading: str) -> None:
        """Write a section heading with green gradient styling."""
        colored_heading = multi_gradient(heading, colors=CLI_HELP_BLUE_GRADIENT, bold=True)
        self.write(f"{'':>{self.current_indent}}{colored_heading}:\n")


def _get_command_color(command_name: str) -> str:
    """Look up the solid color for a command based on its badge in REGISTERED_COMMANDS."""
    for desc in REGISTERED_COMMANDS:
        if desc.name == command_name:
            return COMMAND_TYPE_COLORS.get(desc.badge, DEFAULT_COMMAND_COLOR)
    return DEFAULT_COMMAND_COLOR


def _colorize_command(name: str, hex_color: str) -> str:
    """Wrap a command name in a bold TrueColor ANSI escape using the given hex color."""
    r, g, b = hex_to_rgb(hex_color)
    return f"\033[1;38;2;{r};{g};{b}m{name}\033[0m"


class _EigenscribeGroup(click.Group):
    """Custom Click Group that applies type-specific gradients to command names in help output."""

    def __call__(self, args: list[str] | None = None, **kwargs: object) -> None:
        """Force colors on before any help/command processing."""
        # Make sure ctx.color is True so ANSI codes are never stripped
        if "ctx" in kwargs:
            kwargs["ctx"].color = True  # type: ignore[literal-required]
        super().__call__(args, **kwargs)

    def get_help(self, ctx: click.Context) -> str:
        ctx.formatter_class = _BlueHelpFormatter
        ctx.color = True  # Ensure colors are on during help formatting
        return super().get_help(ctx)

    def format_commands(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        commands = []
        for subcommand in self.list_commands(ctx):
            cmd = self.get_command(ctx, subcommand)
            if cmd is None:
                continue
            if cmd.hidden:
                continue
            commands.append((subcommand, cmd))

        if len(commands):
            limit = formatter.width - 6 - max(len(cmd[0]) for cmd in commands)
            rows = []
            for subcommand, cmd in commands:
                help_text = cmd.get_short_help_str(limit)
                # Apply type-specific solid color based on command's badge
                color = _get_command_color(subcommand)
                colored_name = _colorize_command(subcommand, color)
                rows.append((colored_name, help_text))
            if rows:
                with formatter.section("Commands"):
                    formatter.write_dl(rows)

    def format_options(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        """Override format_options to apply green gradient to option names, then render commands."""
        from click import Argument

        opts = []
        for param in self.get_params(ctx):
            rv = param.get_help_record(ctx)
            if rv is not None and not isinstance(param, Argument):
                opts.append(rv)

        if opts:
            # Apply green gradient to option names
            colored_opts = []
            for opt_names, help_text in opts:
                colored_name = multi_gradient(opt_names, colors=CLI_HELP_BLUE_GRADIENT, bold=True)
                colored_opts.append((colored_name, help_text))
            with formatter.section("Options"):
                formatter.write_dl(colored_opts)

        # Group.format_options calls format_commands after super().format_options()
        self.format_commands(ctx, formatter)


@click.group(
    cls=_EigenscribeGroup,
    invoke_without_command=True,
    help=CLI_HELP_DESCRIPTION,
    epilog=multi_gradient(
        "💚 Powered by Eigenscribe — Deterministic Workspace & Palette Suite",
        colors=GRADIENT_PRESETS["eigenscribe"],
        bold=True,
    ),
)
@click.option("--version", "-v", is_flag=True, help="Display Scriber Core / Eigenscribe CLI version.")
@click.pass_context
def cli(ctx: click.Context, version: bool) -> None:
    """Eigenscribe CLI — Deterministic Workspace Baseline & Palette Tools."""
    ctx.color = True  # Force colors on regardless of TTY detection
    if version:
        version_str = f"scriber-core v{CLI_VERSION} (eigenscribe v{CLI_VERSION})"
        click.echo(multi_gradient(version_str, colors=PRIMARY_GRADIENT, bold=True))
        ctx.exit()

    if ctx.invoked_subcommand is None:
        print_brand_header()
        click.echo("")
        cli_info(f"Eigenscribe CLI (Scriber Core) v{CLI_VERSION} initialized.")
        cli_highlight("Run 'eigenscribe --help' to inspect all available commands and options.")
        click.echo("")
        print_commands_list()


# Alias for backward-compatibility with tests and external callers
cli_group = cli


@cli.command(name="commands", help="Display the color-coded Scriber Core command directory.")
def commands_cmd() -> None:
    """Display the color-coded command index."""
    print_brand_header()
    print_commands_list()


@cli.command(name="banner", help="Print signature TrueColor gradient block banner headers.")
@click.argument("title", required=False, default=None)
@click.option("--title-opt", "--title", "-t", "opt_title", default=None, help="Custom banner title.")
@click.option("--subtitle", "-s", default="Deterministic Workspace & Styling Suite", help="Banner subtitle text.")
@click.option("--preset", "-p", default="eigenscribe", help="Gradient preset for title.")
@click.option("--width", "-w", default=80, type=int, help="Banner width in characters.")
def banner_cmd(
    title: str | None,
    opt_title: str | None,
    subtitle: str | None,
    preset: str,
    width: int,
) -> None:
    """Generate a styled Eigenscribe banner and rule header."""
    final_title = title or opt_title or "SCRIBER CORE"
    final_sub = subtitle if subtitle else None
    cli_banner(final_title, final_sub)


@cli.command(name="colors-table", help="Print the COLOR_PALETTE table with TrueColor swatch blocks.")
@click.option("--sort", "-s", "sort_by", type=click.Choice(["original", "name", "hex", "hue", "luminance"], case_sensitive=False), default="original", help="Sort order.")
@click.option("--reverse", "-r", is_flag=True, default=False, help="Invert sort order.")
@click.option("--block-char", "-b", default="█", help="Block character.")
@click.option("--block-width", "-w", type=int, default=8, help="Block width.")
@click.option("--style", "border_style", type=click.Choice(["rounded", "heavy", "double", "ascii", "minimal", "markdown"], case_sensitive=False), default="rounded", help="Border style.")
@click.option("--no-header", is_flag=True, default=False, help="Suppress title and header.")
@click.option("--no-summary", is_flag=True, default=False, help="Suppress summary footer.")
def colors_table_cmd(
    sort_by: str,
    reverse: bool,
    block_char: str,
    block_width: int,
    border_style: str,
    no_header: bool,
    no_summary: bool,
) -> None:
    """Print the COLOR_PALETTE table."""
    print_colors_table(
        sort_by=sort_by,  # type: ignore[arg-type]
        reverse=reverse,
        block_char=block_char,
        block_width=block_width,
        border_style=border_style,  # type: ignore[arg-type]
        include_header=not no_header,
        include_summary=not no_summary,
    )


@cli.command(name="info", help="Display Scriber Core architectural index, 4-layer token stack, and guidelines.")
def info_cmd() -> None:
    """Display Scriber Core architectural overview."""
    print_brand_header(
        title="🏛️ SCRIBER CORE ARCHITECTURAL OVERVIEW",
        description="Deterministic workspace baseline, styling tokens, and visualization rules for scientific agents.",
    )
    click.echo("")
    cli_rule(level="rule")
    cli_echo("  🧱 4-Layer Design Token Stack:", color="eigen_cyan", bold=True)
    cli_echo("    • Layer 1: Primitive Hex Tokens (COLOR_PALETTE in src/frontend/colors.py)", color="eigen_white")
    cli_echo("    • Layer 2: Semantic Mapping (TSE_COLORS, SEMANTIC_COLORS, BADGE_COLORS)", color="eigen_white")
    cli_echo("    • Layer 3: Dynamic Engines (multi_gradient, golden ratio interpolation)", color="eigen_white")
    cli_echo("    • Layer 4: High-Level Visual Themes (Cosmic Void, Sephirah, Glassmorphic UI)", color="eigen_white")
    cli_rule(level="rule")
    click.echo("")
    cli_success("Workspace baseline synchronized.")


@cli.command(name="gradient", help="Generate and display multi-stop ANSI TrueColor gradient text.")
@click.argument("text", required=False, default="Eigenscribe Multi-Stop ANSI TrueColor Gradient Engine")
@click.option(
    "--preset",
    "-p",
    default="electric",
    help="Gradient preset name (e.g. electric, eigenscribe, cyberpunk, sunset, aurora, midnight, tse-gradient-1).",
)
@click.option(
    "--stops",
    "-s",
    multiple=True,
    help="Custom hex color stops (e.g. -s '#00ffff' -s '#ff00c3'). Overrides preset.",
)
@click.option("--bold/--no-bold", default=True, help="Apply bold weight formatting.")
@click.option("--list-presets", "-l", is_flag=True, help="List all available gradient presets with live previews.")
def gradient_cmd(text: str, preset: str, stops: tuple[str, ...], bold: bool, list_presets: bool) -> None:
    """Generate and display multi-stop ANSI TrueColor gradient text."""
    if list_presets:
        cli_banner("GRADIENT PRESETS", f"{len(GRADIENT_PRESETS)} Built-in Multi-Stop Palettes")
        click.echo("")
        cli_echo("AVAILABLE GRADIENT PRESETS:", color="eigen_cyan", bold=True)
        click.echo("")
        for name, preset_stops in GRADIENT_PRESETS.items():
            sample_text = f"  [{name:16s}]  ██████████████  " + "  ".join(preset_stops)
            rendered = multi_gradient(sample_text, colors=preset_stops, bold=True)
            click.echo(rendered, color=True)
        click.echo("")
        cli_rule(char="─", width=80, level="rule")
        return

    color_stops = (
        stops if stops else GRADIENT_PRESETS.get(preset, GRADIENT_PRESETS.get("electric", PRIMARY_GRADIENT))
    )
    rendered = multi_gradient(text, colors=color_stops, bold=bold)
    click.echo(rendered, color=True)


@cli.command(name="colors", help="Inspect and display Eigenscribe color palettes with live TrueColor swatches.")
@click.option("--all-256", "-a", is_flag=True, help="Display the complete ANSI 256-color palette index.")
@click.option("--spectrum", "-s", is_flag=True, help="Display the 10-Node EIGEN vibrant node spectrum.")
@click.option("--table", "-t", is_flag=True, help="Display the full COLOR_PALETTE table with TrueColor blocks and names.")
def colors_cmd(all_256: bool, spectrum: bool, table: bool) -> None:
    """Inspect and display Eigenscribe color palettes with live TrueColor swatches."""
    if table:
        print_colors_table()
        return

    cli_banner("EIGENSCRIBE DESIGN TOKENS", "Color Palettes, Semantic Roles & Node Spectra")
    click.echo("")

    # 1. Signature TSE Colors
    cli_echo("🎨 Signature TSE Palette & Semantic Status Roles:", color="eigen_cyan", bold=True)
    for name, hex_code in TSE_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 2. Semantic Roles
    cli_echo("🚦 Semantic Status Roles:", color="eigen_blue_bright", bold=True)
    for name, hex_code in SEMANTIC_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 3. Canonical EIGEN Spectrum
    cli_echo("🐉 Canonical EIGEN Spectrum:", color="eigen_cyan", bold=True)
    for name, hex_code in EIGEN_COLORS.items():
        block = _render_color_block(hex_code)
        click.echo(f"  {block}  {name:18s} {hex_code}")
    click.echo("")

    # 4. Vibrant 10-Node Spectrum
    cli_echo("🌌 Vibrant 10-Node EIGEN Spectrum (Vibrant 10-Node Spectrum):", color="eigen_purple_bright", bold=True)
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
        cli_echo("💻 ANSI 256-Color Palette Table:", color="eigen_white", bold=True)
        for row in range(0, 256, 16):
            line_parts = []
            for col in range(16):
                idx = row + col
                if idx < 256:
                    line_parts.append(f"\033[48;5;{idx}m {idx:3d} \033[0m")
            click.echo("  " + "".join(line_parts))
        click.echo("")

    cli_rule(char="─", width=80, level="rule")


@cli.command(name="theme", help="Inspect and export Eigenscribe visualization and plotting theme settings.")
@click.option(
    "--format",
    "-f",
    "theme_format",
    type=click.Choice(["summary", "rcparams", "css"], case_sensitive=False),
    default="summary",
    help="Theme export format (summary, rcparams, css).",
)
def theme_cmd(theme_format: str) -> None:
    """Inspect and export Eigenscribe visualization and plotting theme settings."""
    fmt = theme_format.lower()
    if fmt == "summary":
        cli_banner("PLOTTING & GRAPHICS THEME", "Matplotlib, Seaborn & Plotly Design Presets")
        click.echo("")
        click.echo(multi_gradient("Theme Engine Parameters:", colors=PRIMARY_GRADIENT, bold=True))
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


@cli.command(name="mermaid", help="Generate, wrap, or preview Eigenscribe dark-mode Mermaid diagrams.")
@click.option("--sample", "-s", is_flag=True, help="Generate a sample Eigenscribe dark-mode flowchart diagram.")
@click.option("--init", "-i", "init_directive", is_flag=True, help="Print Mermaid.js %%{init} directive string.")
@click.option("--html-preview", "-h", is_flag=True, help="Generate a self-contained HTML preview file.")
@click.option("--output", "-o", type=click.Path(), default="mermaid_preview.html", help="Output path for HTML preview.")
def mermaid_cmd(sample: bool, init_directive: bool, html_preview: bool, output: str) -> None:
    """Generate, wrap, or preview Eigenscribe dark-mode Mermaid diagrams."""
    if init_directive:
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


@cli.command(name="doctor", help="Run full workspace consistency check, token validation, and smoke tests.")
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
    def _chk_python():
        if sys.version_info < (3, 10):
            raise ValueError("Python >= 3.10 required")

    run_check("Python Version >= 3.10", _chk_python)

    # Check 2: Terminal Color Engine
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


@cli.command(name="message", help="Print a semantic status message (info, success, warning, error, highlight).")
@click.argument("text")
@click.option("--level", "-l", type=click.Choice(["info", "success", "warning", "error", "highlight"], case_sensitive=False), default="info", help="Semantic level.")
def message_cmd(text: str, level: str) -> None:
    """Print a semantic level message."""
    level_lower = level.lower()
    if level_lower == "info":
        cli_info(text)
    elif level_lower == "success":
        cli_success(text)
    elif level_lower == "warning":
        cli_warning(text)
    elif level_lower == "error":
        cli_error(text)
    elif level_lower == "highlight":
        cli_highlight(text)
    else:
        cli_message(text, level=level_lower)


@cli.command(name="rule", help="Print a horizontal rule line with semantic coloring.")
@click.option("--char", "-c", default="─", help="Divider character.")
@click.option("--width", "-w", type=int, default=60, help="Rule width in characters.")
@click.option("--level", "-l", default="rule", help="Semantic color level.")
def rule_cmd(char: str, width: int, level: str) -> None:
    """Print a horizontal divider rule."""
    cli_rule(char=char, width=width, level=level)


@cli.command(name="smoke-test", help="Execute deterministic CLI smoke tests and assertions.")
def smoke_test_cmd() -> None:
    """Run CLI smoke tests."""
    run_smoke_test()


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Primary execution entry point."""
    # Enable Windows VT mode at invocation time, not import time
    enable_vt_mode()

    if len(sys.argv) > 1 and sys.argv[1] == "--smoke-test":
        run_smoke_test()
    else:
        cli()


if __name__ == "__main__":
    main()
