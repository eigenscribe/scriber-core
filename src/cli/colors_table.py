"""
colors_table.py

CLI utility and formatting engine for rendering tabular views of COLOR_PALETTE.
Displays colored swatch blocks alongside their associated palette names (rendered
in their respective TrueColor ANSI codes), hex codes, RGB channel vectors, and
luminance values.

The conceptual story follows the Eigenscribe architectural standard:
What exists -> What you're allowed to call -> How it works -> Proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 17, 2026
"""

from __future__ import annotations

import math
import re
from typing import Final, Literal, NamedTuple, Sequence, TypeAlias

import click

from frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb
from frontend.gradients import GRADIENT_PRESETS, multi_gradient

try:
    from .vt_mode import enable_vt_mode
except ImportError:
    from cli.vt_mode import enable_vt_mode


__all__: list[str] = [
    "BOX_STYLES",
    "ColorEntry",
    "DEFAULT_BLOCK_CHAR",
    "DEFAULT_BLOCK_WIDTH",
    "DEFAULT_BORDER_STYLE",
    "PRIMARY_GRADIENT",
    "SECONDARY_GRADIENT",
    "SortKey",
    "TableStyle",
    "build_color_entries",
    "cli",
    "format_color_swatch",
    "format_colored_name",
    "main",
    "print_colors_table",
    "render_colors_table",
    "run_smoke_test",
]


# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / constants (define once, use Final)
# -----------------------------------------------------------------------------------------------------------

SortKey: TypeAlias = Literal["original", "name", "hex", "hue", "luminance"]
TableStyle: TypeAlias = Literal["rounded", "heavy", "ascii", "double", "minimal", "markdown"]

DEFAULT_BLOCK_CHAR: Final[str] = "█"
DEFAULT_BLOCK_WIDTH: Final[int] = 8
DEFAULT_BORDER_STYLE: Final[TableStyle] = "rounded"

PRIMARY_GRADIENT: Final[tuple[str, ...]] = GRADIENT_PRESETS["eigenscribe"]
SECONDARY_GRADIENT: Final[tuple[str, ...]] = GRADIENT_PRESETS["tse-gradient-1"]
# Unicode Box-Drawing Glyphs
BOX_STYLES: Final[dict[TableStyle, dict[str, str]]] = {
    "rounded": {
        "top_left": "╭",
        "top_mid": "┬",
        "top_right": "╮",
        "mid_left": "├",
        "mid_mid": "┼",
        "mid_right": "┤",
        "bot_left": "╰",
        "bot_mid": "┴",
        "bot_right": "╯",
        "horiz": "─",
        "vert": "│",
    },
    "heavy": {
        "top_left": "┏",
        "top_mid": "┳",
        "top_right": "┓",
        "mid_left": "┣",
        "mid_mid": "╋",
        "mid_right": "┫",
        "bot_left": "┗",
        "bot_mid": "┻",
        "bot_right": "┛",
        "horiz": "━",
        "vert": "┃",
    },
    "double": {
        "top_left": "╔",
        "top_mid": "╦",
        "top_right": "╗",
        "mid_left": "╠",
        "mid_mid": "╬",
        "mid_right": "╣",
        "bot_left": "╚",
        "bot_mid": "╩",
        "bot_right": "╝",
        "horiz": "═",
        "vert": "║",
    },
    "ascii": {
        "top_left": "+",
        "top_mid": "+",
        "top_right": "+",
        "mid_left": "+",
        "mid_mid": "+",
        "mid_right": "+",
        "bot_left": "+",
        "bot_mid": "+",
        "bot_right": "+",
        "horiz": "-",
        "vert": "|",
    },
    "minimal": {
        "top_left": " ",
        "top_mid": " ",
        "top_right": " ",
        "mid_left": " ",
        "mid_mid": " ",
        "mid_right": " ",
        "bot_left": " ",
        "bot_mid": " ",
        "bot_right": " ",
        "horiz": "─",
        "vert": " ",
    },
    "markdown": {
        "top_left": "|",
        "top_mid": "|",
        "top_right": "|",
        "mid_left": "|",
        "mid_mid": "|",
        "mid_right": "|",
        "bot_left": "|",
        "bot_mid": "|",
        "bot_right": "|",
        "horiz": "-",
        "vert": "|",
    },
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Core definitions (what exists)
# -----------------------------------------------------------------------------------------------------------


class ColorEntry(NamedTuple):
    """
    Structured descriptor for a single color token in the palette.

    Attributes
    ----------
    index : int
        1-based sequential index within the rendered table.
    name : str
        Canonical identifier key in COLOR_PALETTE.
    hex_code : str
        Six-digit hexadecimal color string including leading '#'.
    rgb : RGB
        Standard (R, G, B) integer channels in [0, 255].
    luminance : float
        Calculated relative perceptual luminance in [0.0, 1.0].
    hue : float
        Calculated HSV hue angle in degrees [0.0, 360.0].
    """

    index: int
    name: str
    hex_code: str
    rgb: RGB
    luminance: float
    hue: float


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------


def build_color_entries(
    palette: dict[str, str] | None = None,
    *,
    sort_by: SortKey = "original",
    reverse: bool = False,
) -> list[ColorEntry]:
    """
    Construct a structured sequence of ColorEntry items from a color dictionary.

    Parameters
    ----------
    palette : dict[str, str] | None, default=None
        Dictionary mapping color name identifiers to hex strings. Defaults to COLOR_PALETTE.
    sort_by : SortKey, default="original"
        Ordering strategy: "original", "name", "hex", "hue", or "luminance".
    reverse : bool, default=False
        Whether to invert the resulting sort order.

    Returns
    -------
    list[ColorEntry]
        List of structured color descriptors with computed color metrics.
    """
    target_palette = COLOR_PALETTE if palette is None else palette
    raw_entries: list[tuple[str, str, RGB, float, float]] = []

    for name, hex_val in target_palette.items():
        rgb = hex_to_rgb(hex_val)
        lum = _compute_relative_luminance(rgb)
        hue = _compute_hue(rgb)
        raw_entries.append((name, hex_val, rgb, lum, hue))

    # Apply sorting criteria
    if sort_by == "name":
        raw_entries.sort(key=lambda item: item[0].lower(), reverse=reverse)
    elif sort_by == "hex":
        raw_entries.sort(key=lambda item: item[1].lower(), reverse=reverse)
    elif sort_by == "hue":
        raw_entries.sort(key=lambda item: item[4], reverse=reverse)
    elif sort_by == "luminance":
        raw_entries.sort(key=lambda item: item[3], reverse=reverse)
    elif reverse:
        raw_entries.reverse()

    return [
        ColorEntry(
            index=idx,
            name=item[0],
            hex_code=item[1],
            rgb=item[2],
            luminance=item[3],
            hue=item[4],
        )
        for idx, item in enumerate(raw_entries, start=1)
    ]


def format_color_swatch(
    rgb: RGB,
    width: int = DEFAULT_BLOCK_WIDTH,
    block_char: str = DEFAULT_BLOCK_CHAR,
    *,
    use_bg: bool = False,
) -> str:
    """
    Render a TrueColor ANSI colored block swatch.

    Parameters
    ----------
    rgb : RGB
        (R, G, B) integer channels in range [0, 255].
    width : int, default=8
        Number of block characters to render in the swatch.
    block_char : str, default="█"
        Character glyph utilized for block rendering.
    use_bg : bool, default=False
        Whether to style the block using ANSI 48-bit TrueColor background escaping.

    Returns
    -------
    str
        ANSI TrueColor formatted block string with reset suffix.
    """
    r, g, b = rgb
    glyph_sequence = block_char * max(1, width)
    if use_bg:
        return f"\033[48;2;{r};{g};{b}m{glyph_sequence}\033[0m"
    return f"\033[38;2;{r};{g};{b}m{glyph_sequence}\033[0m"


def format_colored_name(
    name: str,
    rgb: RGB,
    *,
    bold: bool = True,
    width: int | None = None,
) -> str:
    """
    Render a color's associated palette name printed in its corresponding TrueColor.

    Parameters
    ----------
    name : str
        The color name identifier (e.g. "pure_cyan", "deep_pine").
    rgb : RGB
        (R, G, B) integer channels in range [0, 255].
    bold : bool, default=True
        Whether to render the text with ANSI bold emphasis.
    width : int | None, default=None
        Optional field width padding (applied before styling escape sequences).

    Returns
    -------
    str
        ANSI TrueColor escaped text displaying the color name in its own color.
    """
    r, g, b = rgb
    text = name if width is None else name.ljust(width)
    style_code = "1;" if bold else ""
    return f"\033[{style_code}38;2;{r};{g};{b}m{text}\033[0m"


def render_colors_table(
    palette: dict[str, str] | None = None,
    *,
    block_char: str = DEFAULT_BLOCK_CHAR,
    block_width: int = DEFAULT_BLOCK_WIDTH,
    border_style: TableStyle = DEFAULT_BORDER_STYLE,
    sort_by: SortKey = "original",
    reverse: bool = False,
    include_header: bool = True,
    include_summary: bool = True,
    show_luminance: bool = True,
) -> str:
    """
    Render a complete tabular string representation of all colors in the palette.

    For each color in COLOR_PALETTE, the table displays:
      - Sequential index (#)
      - Colored swatch block rendered in TrueColor
      - Associated color name printed in its corresponding TrueColor
      - Hexadecimal code (#RRGGBB)
      - RGB channel tuple (R, G, B)
      - Relative perceptual luminance percentage

    Parameters
    ----------
    palette : dict[str, str] | None, default=None
        Target color mapping. If None, defaults to COLOR_PALETTE.
    block_char : str, default="█"
        Glyph character for swatch blocks.
    block_width : int, default=8
        Width in characters of the colored swatch block.
    border_style : TableStyle, default="rounded"
        Box drawing style ("rounded", "heavy", "double", "ascii", "minimal", "markdown").
    sort_by : SortKey, default="original"
        Ordering key ("original", "name", "hex", "hue", "luminance").
    reverse : bool, default=False
        Whether to invert the sorting order.
    include_header : bool, default=True
        Whether to output table title and column header rows.
    include_summary : bool, default=True
        Whether to output the concluding summary footer.
    show_luminance : bool, default=True
        Whether to display the luminance column.

    Returns
    -------
    str
        Formatted multi-line table ready for printing to terminal stdout.
    """
    entries = build_color_entries(palette, sort_by=sort_by, reverse=reverse)
    if not entries:
        return "No colors available in palette."

    box = BOX_STYLES.get(border_style, BOX_STYLES["rounded"])

    # Determine column widths
    max_name_len = max(len(entry.name) for entry in entries)
    col_idx_w = max(4, len(str(len(entries))) + 2)
    col_swatch_w = max(8, block_width + 2)
    col_name_w = max(18, max_name_len + 2)
    col_hex_w = 10
    col_rgb_w = 17
    col_lum_w = 8

    col_widths = [col_idx_w, col_swatch_w, col_name_w, col_hex_w, col_rgb_w]
    if show_luminance:
        col_widths.append(col_lum_w)

    def _make_divider(left: str, mid: str, right: str) -> str:
        parts = [box["horiz"] * w for w in col_widths]
        return f"{left}{mid.join(parts)}{right}"

    top_border = _make_divider(box["top_left"], box["top_mid"], box["top_right"])
    mid_border = _make_divider(box["mid_left"], box["mid_mid"], box["mid_right"])
    bot_border = _make_divider(box["bot_left"], box["bot_mid"], box["bot_right"])

    lines: list[str] = []

    if include_header:
        # Title Banner (Styled with multi-stop ANSI TrueColor gradients)
        total_table_w = sum(col_widths) + len(col_widths) + 1
        title_text = "🎨 SCRIBER CORE COLOR PALETTE TABLE"
        subtitle_text = f"Total Colors: {len(entries)} | Order: {sort_by} | Swatch: {block_char * block_width}"

        styled_title = multi_gradient(title_text, colors=PRIMARY_GRADIENT, bold=True)
        styled_subtitle = multi_gradient(subtitle_text, colors=SECONDARY_GRADIENT, bold=False)

        left_pad_t = max(0, (total_table_w - len(title_text)) // 2)
        right_pad_t = max(0, total_table_w - len(title_text) - left_pad_t)
        lines.append(" " * left_pad_t + styled_title + " " * right_pad_t)

        left_pad_s = max(0, (total_table_w - len(subtitle_text)) // 2)
        right_pad_s = max(0, total_table_w - len(subtitle_text) - left_pad_s)
        lines.append(" " * left_pad_s + styled_subtitle + " " * right_pad_s)

        lines.append("")
        lines.append(top_border)

        # Header Row
        headers = [" #", " Swatch", " Color Name", " Hex", " RGB (R, G, B)"]
        if show_luminance:
            headers.append(" Lum %")

        header_cells = [
            f"\033[1;38;2;240;246;252m{hdr.ljust(w)}\033[0m"
            for hdr, w in zip(headers, col_widths)
        ]
        lines.append(f"{box['vert']}" + f"{box['vert']}".join(header_cells) + f"{box['vert']}")
        lines.append(mid_border)

    # Data Rows
    for entry in entries:
        idx_str = f" {entry.index:02d}".ljust(col_idx_w)
        
        # 1. Colored swatch block
        swatch_str = " " + format_color_swatch(entry.rgb, width=block_width, block_char=block_char)
        # Pad right with spaces (accounting for ANSI codes not consuming visual space)
        pad_swatch = " " * max(0, col_swatch_w - (block_width + 1))
        cell_swatch = f"{swatch_str}{pad_swatch}"

        # 2. Associated name in corresponding color
        cell_name = " " + format_colored_name(entry.name, entry.rgb, bold=True, width=col_name_w - 1)

        # 3. Hex code
        cell_hex = f" {entry.hex_code}".ljust(col_hex_w)

        # 4. RGB channel values
        r, g, b = entry.rgb
        rgb_text = f" ({r:3d}, {g:3d}, {b:3d})"
        cell_rgb = rgb_text.ljust(col_rgb_w)

        row_cells = [idx_str, cell_swatch, cell_name, cell_hex, cell_rgb]

        if show_luminance:
            lum_pct = f" {entry.luminance * 100:4.1f}%".ljust(col_lum_w)
            row_cells.append(lum_pct)

        lines.append(f"{box['vert']}" + f"{box['vert']}".join(row_cells) + f"{box['vert']}")

    if include_header:
        lines.append(bot_border)

    if include_summary:
        lines.append("")
        lines.append(
            f"\033[38;2;34;247;146m✔ Rendered {len(entries)} colors from COLOR_PALETTE with ANSI TrueColor blocks and names.\033[0m"
        )

    return "\n".join(lines)


def print_colors_table(
    palette: dict[str, str] | None = None,
    *,
    block_char: str = DEFAULT_BLOCK_CHAR,
    block_width: int = DEFAULT_BLOCK_WIDTH,
    border_style: TableStyle = DEFAULT_BORDER_STYLE,
    sort_by: SortKey = "original",
    reverse: bool = False,
    include_header: bool = True,
    include_summary: bool = True,
    show_luminance: bool = True,
    color: bool = True,
) -> None:
    """
    Print the rendered COLOR_PALETTE table directly to standard output.

    Parameters
    ----------
    palette : dict[str, str] | None, default=None
        Target color mapping. If None, defaults to COLOR_PALETTE.
    block_char : str, default="█"
        Glyph character for swatch blocks.
    block_width : int, default=8
        Width in characters of the colored swatch block.
    border_style : TableStyle, default="rounded"
        Box drawing style.
    sort_by : SortKey, default="original"
        Ordering key ("original", "name", "hex", "hue", "luminance").
    reverse : bool, default=False
        Whether to invert the sorting order.
    include_header : bool, default=True
        Whether to output header and borders.
    include_summary : bool, default=True
        Whether to output the concluding summary line.
    show_luminance : bool, default=True
        Whether to display luminance percentages.
    color : bool, default=True
        Whether to preserve ANSI TrueColor escape sequences.
    """
    enable_vt_mode()
    table_output = render_colors_table(
        palette=palette,
        block_char=block_char,
        block_width=block_width,
        border_style=border_style,
        sort_by=sort_by,
        reverse=reverse,
        include_header=include_header,
        include_summary=include_summary,
        show_luminance=show_luminance,
    )
    click.echo(table_output, color=color)


# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Private helpers (how it works)
# -----------------------------------------------------------------------------------------------------------


def _compute_relative_luminance(rgb: RGB) -> float:
    """
    Compute WCAG 2.1 relative perceptual luminance from standard RGB channels.

    Parameters
    ----------
    rgb : RGB
        (R, G, B) integer channels in [0, 255].

    Returns
    -------
    float
        Relative luminance scalar in range [0.0, 1.0].
    """
    r_norm = rgb[0] / 255.0
    g_norm = rgb[1] / 255.0
    b_norm = rgb[2] / 255.0

    r_lin = r_norm / 12.92 if r_norm <= 0.04045 else math.pow((r_norm + 0.055) / 1.055, 2.4)
    g_lin = g_norm / 12.92 if g_norm <= 0.04045 else math.pow((g_norm + 0.055) / 1.055, 2.4)
    b_lin = b_norm / 12.92 if b_norm <= 0.04045 else math.pow((b_norm + 0.055) / 1.055, 2.4)

    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def _compute_hue(rgb: RGB) -> float:
    """
    Compute standard HSV hue angle in degrees from (R, G, B).

    Parameters
    ----------
    rgb : RGB
        (R, G, B) integer channels in [0, 255].

    Returns
    -------
    float
        Hue angle in range [0.0, 360.0).
    """
    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0

    max_c = max(r, g, b)
    min_c = min(r, g, b)
    delta = max_c - min_c

    if delta == 0.0:
        return 0.0
    if max_c == r:
        hue = 60.0 * (((g - b) / delta) % 6.0)
    elif max_c == g:
        hue = 60.0 * (((b - r) / delta) + 2.0)
    else:
        hue = 60.0 * (((r - g) / delta) + 4.0)

    return (hue + 360.0) % 360.0


# -----------------------------------------------------------------------------------------------------------
# 4️⃣ 💨 Smoke tests / example usage (proof it works)
# -----------------------------------------------------------------------------------------------------------


def run_smoke_test() -> bool:
    """
    Execute deterministic validation of the color table generator and print a sample table.

    Returns
    -------
    bool
        True if all assertions and table renderings succeed.
    """
    print("💨 Running src/cli/colors_table.py smoke tests...")

    entries = build_color_entries()
    assert len(entries) == len(COLOR_PALETTE), (
        f"Expected {len(COLOR_PALETTE)} entries, got {len(entries)}"
    )

    # Verify each entry attributes
    for entry in entries:
        assert entry.name in COLOR_PALETTE
        assert entry.hex_code == COLOR_PALETTE[entry.name]
        assert len(entry.rgb) == 3
        assert 0.0 <= entry.luminance <= 1.0
        assert 0.0 <= entry.hue <= 360.0

        # Verify formatting functions produce TrueColor codes
        swatch = format_color_swatch(entry.rgb, width=4)
        assert "\033[38;2;" in swatch
        assert "\033[0m" in swatch

        colored_name = format_colored_name(entry.name, entry.rgb)
        assert "\033[1;38;2;" in colored_name or "\033[38;2;" in colored_name
        assert entry.name in colored_name
        assert "\033[0m" in colored_name

    # Verify rendering table output
    table_str = render_colors_table(block_width=6)
    plain_table = re.sub(r"\x1b\[[0-9;]*m", "", table_str)
    assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_table
    assert "deep_pine" in table_str
    assert "pure_cyan" in table_str
    assert "\033[38;2;" in table_str

    print("✅ src/cli/colors_table.py smoke tests passed successfully.\n")
    return True


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


@click.command(name="colors-table", help="Print a table of colored blocks and names for COLOR_PALETTE.")
@click.option(
    "--sort",
    "-s",
    "sort_by",
    type=click.Choice(["original", "name", "hex", "hue", "luminance"], case_sensitive=False),
    default="original",
    help="Sort order for the color palette table.",
)
@click.option(
    "--reverse",
    "-r",
    is_flag=True,
    default=False,
    help="Invert the selected sort order.",
)
@click.option(
    "--block-char",
    "-b",
    default=DEFAULT_BLOCK_CHAR,
    help="Character glyph used to render color swatch blocks.",
)
@click.option(
    "--block-width",
    "-w",
    type=int,
    default=DEFAULT_BLOCK_WIDTH,
    help="Number of block characters per swatch.",
)
@click.option(
    "--style",
    "border_style",
    type=click.Choice(["rounded", "heavy", "double", "ascii", "minimal", "markdown"], case_sensitive=False),
    default="rounded",
    help="Border box-drawing line style.",
)
@click.option(
    "--no-header",
    is_flag=True,
    default=False,
    help="Suppress table title banner and column headers.",
)
@click.option(
    "--no-summary",
    is_flag=True,
    default=False,
    help="Suppress the concluding summary line.",
)
@click.option(
    "--smoke-test",
    is_flag=True,
    default=False,
    help="Run module smoke tests and assertions.",
)
def cli(
    sort_by: SortKey,
    reverse: bool,
    block_char: str,
    block_width: int,
    border_style: TableStyle,
    no_header: bool,
    no_summary: bool,
    smoke_test: bool,
) -> None:
    """CLI entry point for displaying COLOR_PALETTE table."""
    if smoke_test:
        run_smoke_test()
        return

    print_colors_table(
        block_char=block_char,
        block_width=block_width,
        border_style=border_style,
        sort_by=sort_by,
        reverse=reverse,
        include_header=not no_header,
        include_summary=not no_summary,
    )


def main() -> None:
    """Direct execution entry point."""
    cli()


if __name__ == "__main__":
    main()
