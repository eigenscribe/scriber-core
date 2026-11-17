# boilerplates/python/__init__.py
"""
boilerplates.python

Re-exports the full Eigenscribe visualization theme API from the canonical
source (frontend.the_scriber_experience.plots.theme) so that notebooks and
scripts can import via the shorter `boilerplates.python` path.
"""

from __future__ import annotations

from frontend.the_scriber_experience.plots.theme import (
    COLOR_BG,
    COLOR_BG_COSMIC,
    COLOR_BG_COSMIC_CENTER,
    COLOR_BG_COSMIC_VOID,
    COLOR_GRAPH_BG,
    COLOR_LUMINOUS_CYAN,
    COLOR_SURFACE,
    COLOR_SURFACE_ELEVATED,
    COLOR_TEXT,
    COLOR_TEXT_ACCENT,
    COLOR_TEXT_BRIGHT,
    COLOR_TEXT_MUTED,
    COMPARISON_PALETTES,
    EIGEN_BLUE,
    EIGEN_CYAN,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    EIGEN_NODE_NAMES,
    EIGEN_NODES,
    EIGEN_PURPLE,
    EIGENSCRIBE_COLORMAPS,
    EIGENSCRIBE_GRADIENTS,
    EIGEN_SKY,
    FOUR_COLOR_ACCENT,
    HIGH_CONTRAST_CYCLE,
    NETWORKX_GRAPHS_PALETTE,
    RAMP_BLUE,
    RAMP_GREEN,
    RAMP_MAGENTA,
    RAMP_PURPLE,
    SEMANTIC_COLORMAPS,
    THEME_TOKENS,
    apply_cosmic_theme,
    apply_theme,
    create_plotly_base_figure,
    plot_eigenscribe_heatmap,
)

__all__: list[str] = [
    # Color constants
    "COLOR_BG",
    "COLOR_BG_COSMIC",
    "COLOR_BG_COSMIC_CENTER",
    "COLOR_BG_COSMIC_VOID",
    "COLOR_GRAPH_BG",
    "COLOR_LUMINOUS_CYAN",
    "COLOR_SURFACE",
    "COLOR_SURFACE_ELEVATED",
    "COLOR_TEXT",
    "COLOR_TEXT_ACCENT",
    "COLOR_TEXT_BRIGHT",
    "COLOR_TEXT_MUTED",
    # Palettes
    "COMPARISON_PALETTES",
    "EIGEN_COLORS",
    "EIGEN_CYAN",
    "EIGEN_SKY",
    "EIGEN_BLUE",
    "EIGEN_PURPLE",
    "EIGEN_NODES",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "EIGEN_NODE_NAMES",
    "FOUR_COLOR_ACCENT",
    "HIGH_CONTRAST_CYCLE",
    "NETWORKX_GRAPHS_PALETTE",
    "RAMP_GREEN",
    "RAMP_BLUE",
    "RAMP_PURPLE",
    "RAMP_MAGENTA",
    # Colormaps
    "EIGENSCRIBE_COLORMAPS",
    "EIGENSCRIBE_GRADIENTS",
    "SEMANTIC_COLORMAPS",
    # Theme tokens
    "THEME_TOKENS",
    # Functions
    "apply_theme",
    "apply_cosmic_theme",
    "plot_eigenscribe_heatmap",
    "create_plotly_base_figure",
]
