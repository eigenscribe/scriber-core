"""
Scriber Core CLI Package.

Provides terminal color table formatters, block swatch generators, and palette inspection tools.
Follows the gold standard module structure: what exists, what you're allowed to call,
how it works, and proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

from typing import Final

from scriber_core.frontend.colors import COLOR_PALETTE, RGB, hex_to_rgb

from . import branding, command_catalog, colors_table, main, messaging, smoke_tests, vt_mode
from .branding import (
    BORDER_FRAME_COLOR,
    CLI_VERSION,
    CMD_NAME_COLOR,
    DESC_TEXT_COLOR,
    EIGENSCRIBE_BLOCK_TEXT,
    HEADER_CATEGORY_COLOR,
    PRIMARY_GRADIENT,
    SECONDARY_GRADIENT,
    SECTION_BULLET_COLOR,
    SYNTAX_FLAG_COLOR,
    ansi_color,
    print_brand_header,
    render_brand_header,
    run_smoke_test as run_branding_smoke_test,
)
from .command_catalog import (
    BADGE_COLORS,
    CommandDescriptor,
    REGISTERED_COMMANDS,
    print_commands_list,
    render_commands_list,
    run_smoke_test as run_catalog_smoke_test,
)
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
    run_smoke_test as run_colors_table_smoke_test,
)
from .main import (
    cli as main_cli,
    cli_group,
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
from .smoke_tests import run_smoke_test as run_cli_smoke_test
from .vt_mode import enable_vt_mode, run_smoke_test as run_vt_mode_smoke_test

__version__: Final[str] = CLI_VERSION

__all__: list[str] = [
    "__version__",
    # Submodules
    "branding",
    "command_catalog",
    "colors_table",
    "main",
    "messaging",
    "smoke_tests",
    "vt_mode",
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
    "print_brand_header",
    "render_brand_header",
    "print_commands_list",
    "render_commands_list",
    "ansi_color",
    "enable_vt_mode",
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
    # Smoke test functions (module-level)
    "run_cli_smoke_test",
    "run_messaging_smoke_test",
    "run_branding_smoke_test",
    "run_catalog_smoke_test",
    "run_colors_table_smoke_test",
    "run_vt_mode_smoke_test",
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
    "EIGENSCRIBE_BLOCK_TEXT",
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
