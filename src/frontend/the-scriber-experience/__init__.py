# src/frontend/the_scriber_experience/__init__.py
"""
The Scriber Experience (TSE) - Frontend Design & Styling System.
Unifies style design tokens, terminal CLI utilities, and scientific plot themes.
"""

from __future__ import annotations

from . import cli, plots, style
from .cli import (
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
from .plots import (
    apply_cosmic_theme,
    apply_theme,
    create_eigenscribe_colormap,
    create_plotly_base_figure,
    get_eigenscribe_rcparams,
    plot_eigenscribe_heatmap,
    register_colormaps,
)
from .style import (
    CLI_COLORS,
    COLOR_PALETTE,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    GRADIENT_PRESETS,
    PRESETS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    TSE_GRADIENTS,
    Color,
    RGB,
    hex_to_rgb,
    multi_gradient,
)

__all__: list[str] = [
    # Submodules
    "cli",
    "plots",
    "style",
    # Style & Tokens
    "RGB",
    "Color",
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "hex_to_rgb",
    "multi_gradient",
    # CLI
    "cli_message",
    "cli_echo",
    "cli_rule",
    "cli_banner",
    "cli_info",
    "cli_success",
    "cli_warning",
    "cli_error",
    "cli_highlight",
    "EIGENSCRIBE_PALETTE",
    "ansi_256",
    "supports_256_color",
    # Plots
    "apply_theme",
    "apply_cosmic_theme",
    "get_eigenscribe_rcparams",
    "create_eigenscribe_colormap",
    "register_colormaps",
    "plot_eigenscribe_heatmap",
    "create_plotly_base_figure",
]
