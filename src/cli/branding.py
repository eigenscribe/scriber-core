"""
branding.py

Branding and header rendering for the Eigenscribe CLI.
Contains the ASCII art logo, gradient helpers for block text, semantic color
token constants, and functions to render the branded header with gradient
styling.

The conceptual story follows the Eigenscribe architectural standard:
What exists -> What you're allowed to call -> How it works -> Proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

from typing import Final, Sequence

import click

from frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb
from frontend.gradients import GRADIENT_PRESETS, multi_gradient


__all__: list[str] = [
    # Constants
    "CLI_VERSION",
    "PRIMARY_GRADIENT",
    "SECONDARY_GRADIENT",
    "EIGENSCRIBE_BLOCK_TEXT",
    "HEADER_CATEGORY_COLOR",
    "CMD_NAME_COLOR",
    "SYNTAX_FLAG_COLOR",
    "DESC_TEXT_COLOR",
    "BORDER_FRAME_COLOR",
    "SECTION_BULLET_COLOR",
    # Functions
    "ansi_color",
    "interpolate_gradient_color",
    "vertical_gradient_block_text",
    "render_brand_header",
    "print_brand_header",
    "run_smoke_test",
]


# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / constants (define once, use Final)
# -----------------------------------------------------------------------------------------------------------

CLI_VERSION: Final[str] = "1.0.0"

PRIMARY_GRADIENT: Final[tuple[str, ...]] = GRADIENT_PRESETS["eigenscribe"]
SECONDARY_GRADIENT: Final[tuple[str, ...]] = ("#00a6ff", "#7952f5", "#a855f7", "#ff28a2")

# ASCII art rendering "EIGENSCRIBE" (figlet standard font)
EIGENSCRIBE_BLOCK_TEXT: Final[str] = r"""
 _____ ___ ____ _____ _   _ ____   ____ ____  ___ ____  _____ 
| ____|_ _/ ___| ____| \ | / ___| / ___|  _ \|_ _| __ )| ____|
|  _|  | | |  _|  _| |  \| \___ \| |   | |_) || ||  _ \|  _|  
| |___ | | |_| | |___| |\  |___) | |___|  _ < | || |_) | |___ 
|_____|___\____|_____|_| \_|____/ \____|_| \_\___|____/|_____|
"""

# Semantic Color Token Mapping from COLOR_PALETTE
HEADER_CATEGORY_COLOR: Final[str] = COLOR_PALETTE["node-2"]  # #00e8ff - High contrast primary focus
CMD_NAME_COLOR: Final[str] = COLOR_PALETTE["success_emerald"]  # #10b981 - Command names in help output
SYNTAX_FLAG_COLOR: Final[str] = COLOR_PALETTE["pale_lilac"]  # #d8b4fe - Syntax and options
DESC_TEXT_COLOR: Final[str] = COLOR_PALETTE["ice_blue"]  # #b8f6ff - Readable description body
BORDER_FRAME_COLOR: Final[str] = COLOR_PALETTE["periwinkle_blue"]  # #5280ff - Structural frame borders
SECTION_BULLET_COLOR: Final[str] = COLOR_PALETTE["sky_cyan"]  # #4cc9f0 - Bullet markers


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------


def ansi_color(hex_code: str, text: str, *, bold: bool = False) -> str:
    """Format a text string with ANSI 24-bit TrueColor foreground escape sequences.

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


def interpolate_gradient_color(colors: Sequence[str], position: float) -> str:
    """Interpolate a hex color from a gradient at a given position [0.0, 1.0].

    Parameters
    ----------
    colors : Sequence[str]
        Hex color stops for the gradient (at least two).
    position : float
        Normalized position in [0.0, 1.0].

    Returns
    -------
    str
        Interpolated hex color string.
    """
    if len(colors) < 2:
        return colors[0] if colors else "#000000"

    if position <= 0.0:
        return colors[0]
    if position >= 1.0:
        return colors[-1]

    # Find the two surrounding color stops
    segment_length = 1.0 / (len(colors) - 1)
    segment = int(position / segment_length)
    segment = min(segment, len(colors) - 2)

    t = (position - segment * segment_length) / segment_length
    t = max(0.0, min(1.0, t))

    r1, g1, b1 = hex_to_rgb(colors[segment])
    r2, g2, b2 = hex_to_rgb(colors[segment + 1])

    r = round(r1 + t * (r2 - r1))
    g = round(g1 + t * (g2 - g1))
    b = round(b1 + t * (b2 - b1))

    return f"#{r:02x}{g:02x}{b:02x}"


def vertical_gradient_block_text(
    block_text: str,
    colors: Sequence[str],
    *,
    bold: bool = True,
) -> str:
    """Apply a top-to-bottom gradient to multi-line block text (ASCII art).

    Each non-empty row receives a single interpolated color from the gradient,
    based on its vertical position among all non-empty rows.

    Parameters
    ----------
    block_text : str
        Multi-line block text (e.g. ASCII art).
    colors : Sequence[str]
        Hex color stops for the gradient.
    bold : bool, default=True
        Whether to apply bold ANSI formatting.

    Returns
    -------
    str
        ANSI TrueColor-escaped block text with per-row gradient colors.
    """
    rows = block_text.strip("\n").split("\n")
    non_empty_rows = [r for r in rows if r.strip()]
    total = len(non_empty_rows)

    weight = "1;" if bold else ""
    styled_rows: list[str] = []
    non_empty_index = 0

    for row in rows:
        if row.strip():
            position = non_empty_index / (total - 1) if total > 1 else 0.0
            color = interpolate_gradient_color(colors, position)
            r, g, b = hex_to_rgb(color)
            styled_rows.append(f"\033[{weight}38;2;{r};{g};{b}m{row}\033[0m")
            non_empty_index += 1
        else:
            styled_rows.append(row)

    return "\n".join(styled_rows)


def render_brand_header(
    *,
    title: str = "🔱 SCRIBER CORE — DETERMINISTIC WORKSPACE & PALETTE SUITE",
    description: str = "Deterministic workspace baseline, styling tokens, and visualization rules for scientific and development agents.",
    width: int = 88,
) -> str:
    """Render the signature 'EIGENSCRIBE' block text, gradient title, and description.

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

    # 1. Block text reading "EIGENSCRIBE" with top-to-bottom eigenscribe gradient
    block_logo = vertical_gradient_block_text(EIGENSCRIBE_BLOCK_TEXT, colors=PRIMARY_GRADIENT, bold=True)
    lines.append(block_logo)
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
    """Print the signature brand header directly to standard output.

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


# -----------------------------------------------------------------------------------------------------------
# 4️⃣ 💨 Smoke tests / example usage (proof it works)
# -----------------------------------------------------------------------------------------------------------


def run_smoke_test() -> bool:
    """Validate branding constants and header rendering.

    Returns
    -------
    bool
        True if all branding checks pass.
    """
    print("💨 Running src/cli/branding.py smoke tests...")

    # Verify constants
    assert CLI_VERSION == "1.0.0"
    assert len(PRIMARY_GRADIENT) == 4
    assert len(SECONDARY_GRADIENT) == 4
    assert len(EIGENSCRIBE_BLOCK_TEXT.strip()) > 0

    # Verify color tokens reference valid palette keys
    for color_key in (
        HEADER_CATEGORY_COLOR,
        CMD_NAME_COLOR,
        SYNTAX_FLAG_COLOR,
        DESC_TEXT_COLOR,
        BORDER_FRAME_COLOR,
        SECTION_BULLET_COLOR,
    ):
        assert color_key in COLOR_PALETTE.values(), f"Color token {color_key!r} not in COLOR_PALETTE"

    # Verify ansi_color produces valid ANSI codes
    test_str = ansi_color("#00e8ff", "test_cyan", bold=True)
    assert "\033[1;38;2;0;232;255mtest_cyan\033[0m" == test_str

    # Verify header rendering
    header_output = render_brand_header()
    assert "\033[38;2;" in header_output or "\033[1;38;2;" in header_output

    print("✅ src/cli/branding.py smoke tests passed successfully.\n")
    return True


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Orchestrate branding smoke test output."""
    success = run_smoke_test()
    if not success:
        raise ValueError("Branding validation failed during smoke test checks.")


if __name__ == "__main__":
    main()
