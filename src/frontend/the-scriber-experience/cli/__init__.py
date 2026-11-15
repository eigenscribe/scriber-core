# src/frontend/the_scriber_experience/cli/__init__.py
"""
The Scriber Experience (TSE) CLI Subpackage.
Provides ANSI 256-color terminal palettes, semantic logging, banners, and gradient tools.
"""

from __future__ import annotations

from .gradients import (
    CLI_COLORS,
    GRADIENT_PRESETS,
    PRESETS,
    TSE_GRADIENTS,
    Color,
    RGB,
    hex_to_rgb,
    multi_gradient,
)
from .messaging import (
    EIGENSCRIBE_PALETTE,
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

__all__: list[str] = [
    # Semantic Messaging & Elements
    "cli_message",
    "cli_echo",
    "cli_rule",
    "cli_banner",
    "cli_info",
    "cli_success",
    "cli_warning",
    "cli_error",
    "cli_highlight",
    # Palettes & Tokens
    "EIGENSCRIBE_PALETTE",
    "CLI_COLORS",
    "PRESETS",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    # Types & Gradients
    "RGB",
    "Color",
    "hex_to_rgb",
    "multi_gradient",
    "ansi_256",
    "supports_256_color",
]
