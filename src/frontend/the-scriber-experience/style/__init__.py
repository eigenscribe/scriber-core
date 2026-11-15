# src/frontend/the_scriber_experience/style/__init__.py
"""
The Scriber Experience (TSE) Style Subpackage.
Exposes design tokens, semantic palettes, and gradient presets.
"""

from __future__ import annotations

from .tse_colors import (
    CLI_COLORS,
    COLOR_PALETTE,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    Color,
    RGB,
    hex_to_rgb,
)
from .tse_gradients import (
    GRADIENT_PRESETS,
    PRESETS,
    TSE_GRADIENTS,
    multi_gradient,
)

__all__: list[str] = [
    # Types & Base
    "RGB",
    "Color",
    "COLOR_PALETTE",
    "hex_to_rgb",
    # Palettes & Tokens
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    # Gradients & Rendering
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "multi_gradient",
]
