# src/cli/__init__.py
"""
Scriber Core CLI Package.

Provides terminal color table formatters, block swatch generators, and palette inspection tools.
"""

from __future__ import annotations

from frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb

from . import colors, colors_table, main, messaging
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
    cli as main_cli,
    cli_group,
    print_brand_header,
    print_commands_list,
    render_brand_header,
    render_commands_list,
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
    run_smoke_test as run_messaging_smoke_test,
)

__all__: list[str] = [
    # Submodules
    "colors",
    "colors_table",
    "main",
    "messaging",
    # Re-exported Palette Data
    "COLOR_PALETTE",
    "RGB",
    "hex_to_rgb",
    # Functions
    "cli",
    "cli_group",
    "main_cli",
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
    # Messaging Functions
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
    "run_messaging_smoke_test",
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
    "EIGENSCRIBE_PALETTE",
    "STYLE_MAP",
]
