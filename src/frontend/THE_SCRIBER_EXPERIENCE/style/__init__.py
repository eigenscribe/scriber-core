# src/frontend/the_scriber_experience/style/__init__.py
"""
The Scriber Experience (TSE) Style Subpackage.
Exposes design tokens, semantic palettes, and gradient presets.
"""

from __future__ import annotations

from . import semantic_roles, gradient_presets
from ..plots import (
    apply_cosmic_theme,
    apply_theme,
    create_eigenscribe_colormap,
    create_plotly_base_figure,
    get_eigenscribe_rcparams,
    plot_eigenscribe_heatmap,
    register_colormaps,
)
from .semantic_roles import (
    CLI_COLORS,
    COLOR_PALETTE,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    RGB,
    SEMANTIC_COLORS,
    TSE_COLORS,
    Color,
    hex_to_rgb,
)
from .gradient_presets import (
    GRADIENT_PRESETS,
    PRESETS,
    TSE_GRADIENTS,
    multi_gradient,
)

__all__: list[str] = [
    "CLI_COLORS",
    "COLOR_PALETTE",
    "EIGEN_COLORS",
    "EIGEN_LABEL_COLORS",
    "EIGEN_NODE_COLORS",
    # Gradients & Rendering
    "GRADIENT_PRESETS",
    "PRESETS",
    # Types & Base
    "RGB",
    "SEMANTIC_COLORS",
    # Palettes & Tokens
    "TSE_COLORS",
    "TSE_GRADIENTS",
    "Color",
    "apply_cosmic_theme",
    # Plot Themes & Helpers
    "apply_theme",
    "create_eigenscribe_colormap",
    "create_plotly_base_figure",
    "get_eigenscribe_rcparams",
    "hex_to_rgb",
    "multi_gradient",
    "plot_eigenscribe_heatmap",
    "register_colormaps",
    "semantic_roles",
    "gradient_presets",
]
