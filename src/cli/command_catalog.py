# src/cli/command_catalog.py
"""
Command registry and catalog rendering for the Eigenscribe CLI.

Contains the CommandDescriptor type, the REGISTERED_COMMANDS tuple, badge
color mappings, and functions to render the color-coded command directory.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

from typing import Final, NamedTuple, Sequence

import click

from frontend.colors import COLOR_PALETTE, hex_to_rgb
from frontend.gradients import GRADIENT_PRESETS, multi_gradient

from .branding import (
    BORDER_FRAME_COLOR,
    CMD_NAME_COLOR,
    DESC_TEXT_COLOR,
    HEADER_CATEGORY_COLOR,
    PRIMARY_GRADIENT,
    SECTION_BULLET_COLOR,
    SYNTAX_FLAG_COLOR,
    ansi_color,
)


# -----------------------------------------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------------------------------------

# Semantic Badges mapped to COLOR_PALETTE
BADGE_COLORS: Final[dict[str, str]] = {
    "CORE": COLOR_PALETTE["success_emerald"],  # #10b981 - Verified core tools
    "STYLE": COLOR_PALETTE["midwest_indigo"],  # #6f78fa - Visual styling & gradients
    "TOKEN": COLOR_PALETTE["vivid_pink"],  # #f72585 - Color tokens and palettes
    "DIAG": COLOR_PALETTE["warning_amber"],  # #f7c548 - Verification & diagnostics
}


__all__: list[str] = [
    # Types
    "CommandDescriptor",
    # Constants
    "BADGE_COLORS",
    "REGISTERED_COMMANDS",
    # Functions
    "render_commands_list",
    "print_commands_list",
]


# -----------------------------------------------------------------------------------------------------------
# Types
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
        name="theme",
        category="🎨 VISUAL THEMES & PLOTS",
        badge="STYLE",
        syntax="eigenscribe theme [--format summary|rcparams|css]",
        description="Inspect and export Eigenscribe visualization and plotting theme settings for Matplotlib, Seaborn, and CSS.",
    ),
    CommandDescriptor(
        name="mermaid",
        category="📊 ARCHITECTURE & DIAGRAMS",
        badge="STYLE",
        syntax="eigenscribe mermaid [--sample] [--init] [--html-preview]",
        description="Generate dark-mode Mermaid diagram directives, node classes, and interactive HTML previews.",
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
        name="doctor",
        category="💨 DIAGNOSTICS & VERIFICATION",
        badge="DIAG",
        syntax="eigenscribe doctor",
        description="Run comprehensive workspace consistency checks, token validation, and environment health tests.",
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
# Public API: Command list rendering
# -----------------------------------------------------------------------------------------------------------


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
        # Category header styled with PRIMARY_GRADIENT
        cat_styled = multi_gradient(f"  {category}", colors=PRIMARY_GRADIENT, bold=True)
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
