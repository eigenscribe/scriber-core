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

from . import THE_SCRIBER_EXPERIENCE, colors, gradients, messaging
from .colors import (
    COLOR_PALETTE,
    GOLDEN_RATIO,
    PHI,
    GOLDEN_RATIO_INVERSE,
    Color,
    RGB,
    generate_golden_ratio_gradient,
    hex_to_rgb,
    interpolate_rgb,
    render_golden_ratio_gradient,
    run_smoke_test as run_colors_smoke_test,
)
from .gradients import (
    GRADIENT_PRESETS,
    TSE_GRADIENTS,
    compute_golden_ratio_stop_positions,
    multi_gradient,
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
from .THE_SCRIBER_EXPERIENCE import (
    CLI_COLORS,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    PRESETS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    apply_cosmic_theme,
    apply_theme,
    cli,
    create_eigenscribe_colormap,
    create_plotly_base_figure,
    get_eigenscribe_rcparams,
    mermaid,
    plot_eigenscribe_heatmap,
    plots,
    register_colormaps,
    style,
)

# Export backward-compatibility and aliases
the_scriber_experience = THE_SCRIBER_EXPERIENCE
sys.modules.setdefault("frontend.the_scriber_experience", the_scriber_experience)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE", the_scriber_experience)
sys.modules.setdefault("frontend.the_scriber_experience.cli", cli)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.cli", cli)
sys.modules.setdefault("frontend.the_scriber_experience.plots", plots)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.plots", plots)
sys.modules.setdefault("frontend.the_scriber_experience.style", style)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.style", style)
sys.modules.setdefault("frontend.the_scriber_experience.mermaid", mermaid)
sys.modules.setdefault("frontend.THE_SCRIBER_EXPERIENCE.mermaid", mermaid)

__all__: list[str] = [
    # Subpackages
    "colors",
    "gradients",
    "messaging",
    "the_scriber_experience",
    "THE_SCRIBER_EXPERIENCE",
    "style",
    "cli",
    "plots",
    "mermaid",
    # Types & Core
    "RGB",
    "Color",
    "GOLDEN_RATIO",
    "PHI",
    "GOLDEN_RATIO_INVERSE",
    "hex_to_rgb",
    "interpolate_rgb",
    "generate_golden_ratio_gradient",
    "render_golden_ratio_gradient",
    "run_colors_smoke_test",
    # Palettes & Tokens
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "EIGENSCRIBE_PALETTE",
    "STYLE_MAP",
    # Gradients & Rendering
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "compute_golden_ratio_stop_positions",
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
    "render_message",
    "render_echo",
    "render_rule",
    "render_banner",
    "ansi_256",
    "supports_256_color",
    "run_messaging_smoke_test",
    # Plots
    "apply_theme",
    "apply_cosmic_theme",
    "get_eigenscribe_rcparams",
    "create_eigenscribe_colormap",
    "register_colormaps",
    "plot_eigenscribe_heatmap",
    "create_plotly_base_figure",
]
