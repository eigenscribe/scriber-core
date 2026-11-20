# src/frontend/the_scriber_experience/__init__.py
"""
The Scriber Experience (TSE) - Frontend Design & Styling System.
Unifies style design tokens, terminal CLI utilities, and scientific plot themes.
"""

from __future__ import annotations

from . import mermaid, plots
from .mermaid import (
    EIGENSCRIBE_MERMAID_CLASSES,
    EIGENSCRIBE_MERMAID_THEME_VARIABLES,
    generate_mermaid_flowchart,
    get_mermaid_class_defs,
    get_mermaid_init_directive,
    get_mermaid_theme_variables,
    render_html_preview,
    save_mermaid_diagram,
    wrap_mermaid_diagram,
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
from frontend.colors import (
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
from frontend.gradients import (
    GRADIENT_PRESETS,
    PRESETS,
    TSE_GRADIENTS,
    multi_gradient,
)

__all__: list[str] = [
    # Submodules
    "plots",
    "mermaid",
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
    # Plots
    "apply_theme",
    "apply_cosmic_theme",
    "get_eigenscribe_rcparams",
    "create_eigenscribe_colormap",
    "register_colormaps",
    "plot_eigenscribe_heatmap",
    "create_plotly_base_figure",
]
