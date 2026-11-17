# src/cli/__init__.py
"""
Scriber Core CLI Package.

Provides terminal color table formatters, block swatch generators, and palette inspection tools.
"""

from __future__ import annotations

from frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb

from . import colors, colors_table, main
from .colors_table import (
    BOX_STYLES,
    DEFAULT_BLOCK_CHAR,
    DEFAULT_BLOCK_WIDTH,
    DEFAULT_BORDER_STYLE,
    ColorEntry,
    SortKey,
    TableStyle,
    build_color_entries,
    cli,
    format_color_swatch,
    format_colored_name,
    print_colors_table,
    render_colors_table,
    run_smoke_test,
)
from .main import (
    BADGE_COLORS,
    BORDER_FRAME_COLOR,
    CLI_VERSION,
    CMD_NAME_COLOR,
    CommandDescriptor,
    DESC_TEXT_COLOR,
    HEADER_CATEGORY_COLOR,
    PRIMARY_GRADIENT,
    REGISTERED_COMMANDS,
    SCRIBER_CORE_BLOCK_TEXT,
    SECONDARY_GRADIENT,
    SECTION_BULLET_COLOR,
    SYNTAX_FLAG_COLOR,
    ansi_color,
    print_brand_header,
    print_commands_list,
    render_brand_header,
    render_commands_list,
)

__all__: list[str] = [
    # Submodules
    "colors",
    "colors_table",
    "main",
    # Re-exported Palette Data
    "COLOR_PALETTE",
    "RGB",
    "hex_to_rgb",
    # Functions
    "cli",
    "print_colors_table",
    "render_colors_table",
    "build_color_entries",
    "format_color_swatch",
    "format_colored_name",
    "run_smoke_test",
    "print_brand_header",
    "render_brand_header",
    "print_commands_list",
    "render_commands_list",
    "ansi_color",
    # Types & Models
    "ColorEntry",
    "CommandDescriptor",
    "SortKey",
    "TableStyle",
    # Constants
    "BOX_STYLES",
    "DEFAULT_BLOCK_CHAR",
    "DEFAULT_BLOCK_WIDTH",
    "DEFAULT_BORDER_STYLE",
    "CLI_VERSION",
    "PRIMARY_GRADIENT",
    "SECONDARY_GRADIENT",
    "SCRIBER_CORE_BLOCK_TEXT",
    "REGISTERED_COMMANDS",
    "HEADER_CATEGORY_COLOR",
    "CMD_NAME_COLOR",
    "SYNTAX_FLAG_COLOR",
    "DESC_TEXT_COLOR",
    "BORDER_FRAME_COLOR",
    "SECTION_BULLET_COLOR",
    "BADGE_COLORS",
]
