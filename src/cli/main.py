# src/cli/main.py
"""
main.py

Primary entry point for the Scriber Core CLI suite.
Renders signature TrueColor gradient block text ("scriber-core"), branded gradient
headers, color-coded command listings, and palette inspection tools.

The conceptual story follows the Eigenscribe architectural standard:
What exists -> What you're allowed to call -> How it works -> Proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 17, 2026
"""

from __future__ import annotations

import re
import sys
from typing import Final, NamedTuple, Sequence

# Force UTF-8 stdout and enable ANSI TrueColor / Virtual Terminal Processing on Windows
def _enable_windows_vt_mode() -> None:
    """Enable ANSI/VT100 Virtual Terminal Processing on Windows consoles."""
    if sys.platform != "win32":
        return
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    try:
        import os

        os.system("")
    except Exception:
        pass
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass
    try:
        import colorama

        if hasattr(colorama, "just_fix_windows_console"):
            colorama.just_fix_windows_console()
        else:
            colorama.init(wrap=False)
    except Exception:
        pass


_enable_windows_vt_mode()

import click

from frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb
from frontend.gradients import GRADIENT_PRESETS, multi_gradient

try:
    from .colors_table import (
        cli as colors_table_cli,
        main as colors_table_main,
        print_colors_table,
        render_colors_table,
    )
except (ImportError, ValueError):
    from cli.colors_table import (
        cli as colors_table_cli,
        main as colors_table_main,
        print_colors_table,
        render_colors_table,
    )

__all__: list[str] = [
    "BADGE_COLORS",
    "BORDER_FRAME_COLOR",
    "CLI_VERSION",
    "CMD_NAME_COLOR",
    "CommandDescriptor",
    "DESC_TEXT_COLOR",
    "HEADER_CATEGORY_COLOR",
    "PRIMARY_GRADIENT",
    "REGISTERED_COMMANDS",
    "SCRIBER_CORE_BLOCK_TEXT",
    "SECONDARY_GRADIENT",
    "SECTION_BULLET_COLOR",
    "SYNTAX_FLAG_COLOR",
    "ansi_color",
    "cli",
    "colors_table_cli",
    "main",
    "print_brand_header",
    "print_colors_table",
    "print_commands_list",
    "render_brand_header",
    "render_colors_table",
    "render_commands_list",
    "run_smoke_test",
]


# -----------------------------------------------------------------------------------------------------------
# /* 🎭 Typing helpers / protocols / constants (if needed) */
# -----------------------------------------------------------------------------------------------------------

CLI_VERSION: Final[str] = "0.1.0"

PRIMARY_GRADIENT: Final[tuple[str, ...]] = GRADIENT_PRESETS["eigenscribe"]
SECONDARY_GRADIENT: Final[tuple[str, ...]] = ("#00a6ff", "#7952f5", "#a855f7", "#ff28a2")

# Unicode block text rendering "scriber-core"
SCRIBER_CORE_BLOCK_TEXT: Final[str] = r"""
  ███████╗ ██████╗██████╗ ██╗██████╗ ███████╗██████╗        ██████╗ ██████╗ ██████╗ ███████╗
  ██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗      ██╔════╝██╔═══██╗██╔══██╗██╔════╝
  ███████╗██║     ██████╔╝██║██████╔╝█████╗  ██████╔╝█████╗██║     ██║   ██║██████╔╝█████╗  
  ╚════██║██║     ██╔══██╗██║██╔══██╗██╔══╝  ██╔══██╗╚════╝██║     ██║   ██║██╔══██╗██╔══╝  
  ███████║╚██████╗██║  ██║██║██████╔╝███████╗██║  ██║      ╚██████╗╚██████╔╝██║  ██║███████╗
  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""

# Semantic Color Token Mapping from COLOR_PALETTE
HEADER_CATEGORY_COLOR: Final[str] = COLOR_PALETTE["vivid_cyan"]  # #00e8ff - High contrast primary focus
CMD_NAME_COLOR: Final[str] = COLOR_PALETTE["vivid_sky_blue"]  # #14b5ff - Command identifier
SYNTAX_FLAG_COLOR: Final[str] = COLOR_PALETTE["pale_lilac"]  # #d8b4fe - Syntax and options
DESC_TEXT_COLOR: Final[str] = COLOR_PALETTE["ice_blue"]  # #b8f6ff - Readable description body
BORDER_FRAME_COLOR: Final[str] = COLOR_PALETTE["periwinkle_blue"]  # #5280ff - Structural frame borders
SECTION_BULLET_COLOR: Final[str] = COLOR_PALETTE["sky_cyan"]  # #4cc9f0 - Bullet markers

# Semantic Badges mapped to COLOR_PALETTE
BADGE_COLORS: Final[dict[str, str]] = {
    "CORE": COLOR_PALETTE["success_emerald"],  # #10b981 - Verified core tools
    "STYLE": COLOR_PALETTE["midwest_indigo"],  # #6f78fa - Visual styling & gradients
    "TOKEN": COLOR_PALETTE["vivid_pink"],  # #f72585 - Color tokens and palettes
    "DIAG": COLOR_PALETTE["warning_amber"],  # #f7c548 - Verification & diagnostics
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Core definitions
# -----------------------------------------------------------------------------------------------------------


class CommandDescriptor(NamedTuple):
    """
    Descriptor for a CLI command within the Scriber Core workspace suite.

    Attributes
    ----------
    name : str
        Invocation name of the command.
    category : str
        Semantic section grouping.
    badge : str
        Short functional classification badge (e.g. 'CORE', 'STYLE', 'TOKEN', 'DIAG').
    syntax : str
        Command-line invocation syntax and options.
    description : str
        Concise summary of command functionality and outcomes.
    """

    name: str
    category: str
    badge: str
    syntax: str
    description: str


REGISTERED_COMMANDS: Final[tuple[CommandDescriptor, ...]] = (
    CommandDescriptor(
        name="colors-table",
        category="🎨 COLOR PALETTES & SWATCHES",
        badge="CORE",
        syntax="python -m cli.colors_table [--sort <key>] [--style <box>] [--block-char <c>]",
        description="Render COLOR_PALETTE table with TrueColor swatch blocks, hex codes, RGB vectors, and luminance metrics.",
    ),
    CommandDescriptor(
        name="colors",
        category="🎨 COLOR PALETTES & SWATCHES",
        badge="TOKEN",
        syntax="eigenscribe colors [--all-256] [--spectrum] [--table]",
        description="Inspect terminal color palettes, ANSI 256-color index, and 10-node EIGEN spectrum.",
    ),
    CommandDescriptor(
        name="gradient",
        category="🌈 TRUECOLOR GRADIENTS & BANNERS",
        badge="STYLE",
        syntax="eigenscribe gradient <text> [--preset <name>] [--stops <hex>...]",
        description="Interpolate and render text with multi-stop ANSI TrueColor linear gradients.",
    ),
    CommandDescriptor(
        name="banner",
        category="🌈 TRUECOLOR GRADIENTS & BANNERS",
        badge="STYLE",
        syntax="python -m cli banner [--title <text>] [--subtitle <text>]",
        description="Display signature TrueColor ASCII block banner headers and gradient rule dividers.",
    ),
    CommandDescriptor(
        name="info",
        category="🏛️ WORKSPACE ARCHITECTURE & TOKENS",
        badge="CORE",
        syntax="eigenscribe info",
        description="Display Scriber Core architectural index, 4-layer design token stack, and workspace guidelines.",
    ),
    CommandDescriptor(
        name="commands",
        category="🏛️ WORKSPACE ARCHITECTURE & TOKENS",
        badge="CORE",
        syntax="python -m cli [commands]",
        description="Display the complete color-coded command index, syntax references, and tool directory.",
    ),
    CommandDescriptor(
        name="smoke-test",
        category="💨 DIAGNOSTICS & VERIFICATION",
        badge="DIAG",
        syntax="python -m cli.colors_table --smoke-test",
        description="Execute deterministic smoke test suite, color calculations, and verification assertions.",
    ),
)


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------


def ansi_color(hex_code: str, text: str, *, bold: bool = False) -> str:
    """
    Format a text string with ANSI 24-bit TrueColor foreground escape sequences.

    Parameters
    ----------
    hex_code : str
        Hexadecimal color string (e.g. '#00e8ff').
    text : str
        Text string to style.
    bold : bool, default=False
        Whether to apply bold font weight.

    Returns
    -------
    str
        Text string wrapped in TrueColor ANSI sequences.
    """
    r, g, b = hex_to_rgb(hex_code)
    weight = "1;" if bold else ""
    return f"\033[{weight}38;2;{r};{g};{b}m{text}\033[0m"


def render_brand_header(
    *,
    title: str = "🔱 SCRIBER CORE — DETERMINISTIC WORKSPACE & PALETTE SUITE",
    description: str = "Deterministic workspace baseline, styling tokens, and visualization rules for scientific and development agents.",
    width: int = 88,
) -> str:
    """
    Render the signature 'scriber-core' block text, gradient title, and description.

    Parameters
    ----------
    title : str, default="🔱 SCRIBER CORE — DETERMINISTIC WORKSPACE & PALETTE SUITE"
        Main branded title string.
    description : str, default="..."
        Branded subtitle / description string.
    width : int, default=88
        Total horizontal display width.

    Returns
    -------
    str
        Formatted ANSI TrueColor header block string.
    """
    lines: list[str] = []

    # 1. Block text reading "scriber-core" with SECONDARY_GRADIENT
    block_logo = multi_gradient(SCRIBER_CORE_BLOCK_TEXT, colors=SECONDARY_GRADIENT, bold=True)
    lines.append(block_logo.strip("\n"))
    lines.append("")

    # 2. Branded title with PRIMARY_GRADIENT
    styled_title = multi_gradient(f"  {title}", colors=PRIMARY_GRADIENT, bold=True)
    lines.append(styled_title)

    # 3. Branded description with SECONDARY_GRADIENT
    styled_desc = multi_gradient(f"  {description}", colors=SECONDARY_GRADIENT, bold=False)
    lines.append(styled_desc)
    lines.append("")

    # 4. Horizontal rule divider
    divider = "═" * width
    lines.append(ansi_color(BORDER_FRAME_COLOR, f"  {divider}", bold=True))

    return "\n".join(lines)


def print_brand_header(
    *,
    title: str = "🔱 SCRIBER CORE — DETERMINISTIC WORKSPACE & PALETTE SUITE",
    description: str = "Deterministic workspace baseline, styling tokens, and visualization rules for scientific and development agents.",
    width: int = 88,
    color: bool = True,
) -> None:
    """
    Print the signature brand header directly to standard output.

    Parameters
    ----------
    title : str, optional
        Branded title string.
    description : str, optional
        Branded description string.
    width : int, default=88
        Rule divider width.
    color : bool, default=True
        Whether to preserve ANSI TrueColor escape sequences.
    """
    click.echo(render_brand_header(title=title, description=description, width=width), color=color)


def render_commands_list(
    commands: Sequence[CommandDescriptor] = REGISTERED_COMMANDS,
    *,
    width: int = 88,
) -> str:
    """
    Render a color-coded directory of CLI commands formatted with COLOR_PALETTE tokens.

    Parameters
    ----------
    commands : Sequence[CommandDescriptor], default=REGISTERED_COMMANDS
        Sequence of command definitions to format.
    width : int, default=88
        Target box width.

    Returns
    -------
    str
        Formatted ANSI TrueColor command directory block.
    """
    lines: list[str] = []

    # Section Title
    section_banner = "📋 AVAILABLE CLI COMMANDS & WORKSPACE UTILITIES"
    lines.append(multi_gradient(f"  {section_banner}", colors=PRIMARY_GRADIENT, bold=True))
    lines.append(ansi_color(BORDER_FRAME_COLOR, "  " + "─" * width, bold=False))
    lines.append("")

    # Group commands by category
    categories: dict[str, list[CommandDescriptor]] = {}
    for cmd in commands:
        categories.setdefault(cmd.category, []).append(cmd)

    for category, cat_cmds in categories.items():
        # Category header
        cat_styled = ansi_color(HEADER_CATEGORY_COLOR, f"  {category}", bold=True)
        lines.append(cat_styled)

        for cmd in cat_cmds:
            # Bullet, command name, badge, and description
            bullet = ansi_color(SECTION_BULLET_COLOR, "•", bold=True)
            name_str = ansi_color(CMD_NAME_COLOR, f"{cmd.name:<14}", bold=True)
            badge_color = BADGE_COLORS.get(cmd.badge, COLOR_PALETTE["success_emerald"])
            badge_str = ansi_color(badge_color, f"[{cmd.badge}]", bold=True)
            desc_str = ansi_color(DESC_TEXT_COLOR, cmd.description)

            lines.append(f"    {bullet} {name_str}  {badge_str}  {desc_str}")

            # Syntax line
            syntax_label = ansi_color(SECTION_BULLET_COLOR, "Syntax:", bold=False)
            syntax_val = ansi_color(SYNTAX_FLAG_COLOR, cmd.syntax, bold=False)
            lines.append(f"        {syntax_label} {syntax_val}")

        lines.append("")

    # Legend / Summary footer
    lines.append(ansi_color(BORDER_FRAME_COLOR, "  " + "─" * width, bold=False))
    legend_core = ansi_color(BADGE_COLORS["CORE"], "[CORE]", bold=True) + ansi_color(DESC_TEXT_COLOR, " Primary")
    legend_style = ansi_color(BADGE_COLORS["STYLE"], "[STYLE]", bold=True) + ansi_color(DESC_TEXT_COLOR, " Gradients & Banners")
    legend_token = ansi_color(BADGE_COLORS["TOKEN"], "[TOKEN]", bold=True) + ansi_color(DESC_TEXT_COLOR, " Palettes & Swatches")
    legend_diag = ansi_color(BADGE_COLORS["DIAG"], "[DIAG]", bold=True) + ansi_color(DESC_TEXT_COLOR, " Diagnostics")

    lines.append(f"  💡 {ansi_color(HEADER_CATEGORY_COLOR, 'Semantic Legend:', bold=True)} {legend_core}  {legend_style}  {legend_token}  {legend_diag}")
    lines.append("")

    return "\n".join(lines)


def print_commands_list(
    commands: Sequence[CommandDescriptor] = REGISTERED_COMMANDS,
    *,
    width: int = 88,
    color: bool = True,
) -> None:
    """
    Print the color-coded command directory directly to standard output.

    Parameters
    ----------
    commands : Sequence[CommandDescriptor], default=REGISTERED_COMMANDS
        Sequence of command descriptors.
    width : int, default=88
        Formatting width.
    color : bool, default=True
        Whether to preserve ANSI TrueColor escape sequences.
    """
    click.echo(render_commands_list(commands=commands, width=width), color=color)


# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Smoke tests / example usage
# -----------------------------------------------------------------------------------------------------------


def run_smoke_test() -> bool:
    """
    Execute smoke test assertions for CLI main, brand header, and command directory.

    Returns
    -------
    bool
        True if all verification assertions succeed.
    """
    print("💨 Running src/cli/main.py smoke tests...")

    # 1. Block text existence and gradient definition
    assert len(SCRIBER_CORE_BLOCK_TEXT.strip()) > 0
    assert "██" in SCRIBER_CORE_BLOCK_TEXT
    assert len(SECONDARY_GRADIENT) == 4
    assert len(PRIMARY_GRADIENT) == 4

    # 2. Header rendering test
    header_output = render_brand_header()
    assert "\033[38;2;" in header_output or "\033[1;38;2;" in header_output
    plain_header = re.sub(r"\x1b\[[0-9;]*m", "", header_output)
    assert "SCRIBER CORE" in plain_header
    assert "Deterministic workspace baseline" in plain_header

    # 3. Command list rendering test
    commands_output = render_commands_list()
    assert "\033[38;2;" in commands_output
    plain_commands = re.sub(r"\x1b\[[0-9;]*m", "", commands_output)
    assert "AVAILABLE CLI COMMANDS" in plain_commands
    assert "colors-table" in plain_commands
    assert "gradient" in plain_commands
    assert "info" in plain_commands

    # 4. Color formatting helper test
    test_str = ansi_color("#00e8ff", "test_cyan", bold=True)
    assert "\033[1;38;2;0;232;255mtest_cyan\033[0m" == test_str

    print("✅ src/cli/main.py smoke tests passed successfully.\n")
    return True


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point & Click Command Group
# -----------------------------------------------------------------------------------------------------------


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Display Scriber Core CLI version.")
@click.pass_context
def cli(ctx: click.Context, version: bool) -> None:
    """
    🔱 Scriber Core CLI — Deterministic Workspace Baseline & Palette Tools.
    """
    if version:
        version_str = f"scriber-core v{CLI_VERSION}"
        click.echo(multi_gradient(version_str, colors=PRIMARY_GRADIENT, bold=True))
        ctx.exit()

    if ctx.invoked_subcommand is None:
        print_brand_header()
        print_commands_list()


@cli.command(name="commands", help="Display the color-coded Scriber Core command directory.")
def commands_cmd() -> None:
    """Display the color-coded command index."""
    print_brand_header()
    print_commands_list()


@cli.command(name="banner", help="Print the signature 'scriber-core' TrueColor gradient block text.")
@click.option("--title", "-t", default="🔱 SCRIBER CORE — DETERMINISTIC WORKSPACE & PALETTE SUITE", help="Custom banner title.")
@click.option("--subtitle", "-s", default="Deterministic workspace baseline, styling tokens, and visualization rules.", help="Custom banner subtitle.")
def banner_cmd(title: str, subtitle: str) -> None:
    """Display the signature brand banner."""
    print_brand_header(title=title, description=subtitle)


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


@cli.command(name="smoke-test", help="Execute deterministic CLI smoke tests and assertions.")
def smoke_test_cmd() -> None:
    """Run CLI smoke tests."""
    run_smoke_test()


def main() -> None:
    """Direct execution entry point."""
    cli()


if __name__ == "__main__":
    main()
