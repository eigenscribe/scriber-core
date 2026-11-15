# src/frontend/__init__.py
"""
frontend

Frontend, design tokens, ANSI TrueColor gradient engine, and styling subsystems
conforming to the Eigenscribe and Scriber Labs design system.

Author: Eigenscribe & Scriber Labs
Date: November 15, 2026
"""

from __future__ import annotations

import sys

from . import colors, gradients, THE_SCRIBER_EXPERIENCE
from .THE_SCRIBER_EXPERIENCE import (
    CLI_COLORS,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    EIGENSCRIBE_PALETTE,
    PRESETS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    ansi_256,
    apply_cosmic_theme,
    apply_theme,
    cli,
    cli_banner,
    cli_echo,
    cli_error,
    cli_highlight,
    cli_info,
    cli_message,
    cli_rule,
    cli_success,
    cli_warning,
    create_eigenscribe_colormap,
    create_plotly_base_figure,
    get_eigenscribe_rcparams,
    mermaid,
    plot_eigenscribe_heatmap,
    plots,
    register_colormaps,
    style,
    supports_256_color,
)
from .colors import (
    COLOR_PALETTE,
    Color,
    RGB,
    hex_to_rgb,
)
from .gradients import (
    GRADIENT_PRESETS,
    TSE_GRADIENTS,
    multi_gradient,
)

# Export backward-compatibility and uppercase alias
THE_SCRIBER_EXPERIENCE = THE_SCRIBER_EXPERIENCE
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE", THE_SCRIBER_EXPERIENCE)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.cli", cli)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.plots", plots)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.style", style)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.mermaid", mermaid)

__all__: list[str] = [
    # Subpackages
    "colors",
    "gradients",
    "THE_SCRIBER_EXPERIENCE",
    "style",
    "cli",
    "plots",
    "mermaid",
    # Types & Core
    "RGB",
    "Color",
    "hex_to_rgb",
    # Palettes & Tokens
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "EIGENSCRIBE_PALETTE",
    # Gradients & Rendering
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "multi_gradient",
    # CLI Messaging
    "cli_message",
    "cli_echo",
    "cli_rule",
    "cli_banner",
    "cli_info",
    "cli_success",
    "cli_warning",
    "cli_error",
    "cli_highlight",
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
