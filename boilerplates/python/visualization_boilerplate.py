"""
visualization_boilerplate.py

Generalizable visualization bootstrapping script for Matplotlib, Pyplot, and Seaborn
graphics conforming to the Eigenscribe / Scriber Labs Design System.

Author: Scriber Labs
Date: 2026-10-16
"""

from typing import Any, Dict, Final, List, Mapping, Optional, Sequence, TypeAlias

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Colormap, LinearSegmentedColormap
from numpy.typing import NDArray

try:
    import seaborn as sns

    HAS_SEABORN = True
except ImportError:
    sns = None
    HAS_SEABORN = False

try:
    import plotly.graph_objects as go

    HAS_PLOTLY = True
except ImportError:
    go = None
    HAS_PLOTLY = False

ArrayOrFloat: TypeAlias = float | NDArray[np.float64]

# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / protocols / constants (if needed)
# -----------------------------------------------------------------------------------------------------------

DEFAULT_SEED: Final[int] = 42

# --- Foundation Surface & Text Tokens (Layer 1: Design Tokens) ---
COLOR_BG: Final[str] = "#0d1117"
COLOR_SURFACE: Final[str] = "#161b22"
COLOR_SURFACE_ELEVATED: Final[str] = "#21262d"
COLOR_SURFACE_OVERLAY: Final[str] = "rgba(22, 27, 34, 0.75)"
COLOR_GRAPH_BG: Final[str] = "rgba(3, 7, 18, 0.85)"

# Cosmic Deep Radial Foundations
COLOR_BG_COSMIC_CENTER: Final[str] = "#0a0f1f"
COLOR_BG_COSMIC: Final[str] = "#050812"
COLOR_BG_COSMIC_VOID: Final[str] = "#000000"

COLOR_TEXT: Final[str] = "#f0f6fc"
COLOR_TEXT_BRIGHT: Final[str] = "#ffffff"
COLOR_TEXT_MUTED: Final[str] = "#8b949e"
COLOR_TEXT_SUBTLE: Final[str] = "#6e7681"
COLOR_TEXT_ACCENT: Final[str] = "#c8f8ff"
COLOR_TEXT_SEPHIRAH: Final[str] = "#c8f8ff"

# Glassmorphic Overlays & Luminous Accents
COLOR_LUMINOUS_CYAN: Final[str] = "#c8f8ff"
COLOR_COSMIC_BG: Final[str] = "rgba(0, 232, 255, 0.08)"
COLOR_COSMIC_GLOW: Final[str] = "rgba(0, 232, 255, 0.30)"
COLOR_COSMIC_BORDER: Final[str] = "rgba(255, 255, 255, 0.08)"
COLOR_TOOLTIP_BG: Final[str] = "rgba(0, 0, 0, 0.75)"
COLOR_TOOLTIP_BORDER: Final[str] = "rgba(255, 255, 255, 0.12)"

# Extended Glassmorphic & Specular Tokens (from Obsidian design notes)
COLOR_GLASS_INDIGO: Final[str] = "rgba(99, 102, 241, 0.35)"
COLOR_GLASS_PURPLE: Final[str] = "rgba(168, 85, 247, 0.25)"
COLOR_GLASS_VIOLET: Final[str] = "rgba(121, 82, 245, 0.40)"
COLOR_GLASS_CYAN: Final[str] = "rgba(0, 255, 238, 0.15)"
COLOR_GLASS_CYAN_GLOW: Final[str] = "rgba(0, 232, 255, 0.40)"
COLOR_GLASS_BLUE: Final[str] = "rgba(56, 152, 255, 0.50)"
COLOR_GLASS_SKY: Final[str] = "rgba(20, 165, 255, 0.60)"

# Additional Vibrant & Accent Color Primitives
COLOR_CYAN_PURE: Final[str] = "#00ffee"
COLOR_BLUE_VIBRANT: Final[str] = "#0a95eb"
COLOR_BLUE_AZURE: Final[str] = "#0596f0"
COLOR_BLUE_SKY_LIGHT: Final[str] = "#60a5fa"
COLOR_PURPLE_SOFT: Final[str] = "#a78bfa"
COLOR_INDIGO_ACCENT: Final[str] = "#5280ff"
COLOR_VIOLET_DEEP: Final[str] = "#5e17eb"
COLOR_PINK_HOT: Final[str] = "#ff40a1"
COLOR_ORANGE_BRIGHT: Final[str] = "#ff8855"
COLOR_ORANGE_CORAL: Final[str] = "#ff783d"
COLOR_AMBER_WARM: Final[str] = "#ff9d57"
COLOR_ACCENT_GREEN: Final[str] = "#38fe52"
COLOR_ACCENT_BLUE: Final[str] = "#3881fe"
COLOR_ACCENT_MAGENTA: Final[str] = "#fe38e4"
COLOR_ACCENT_AMBER: Final[str] = "#feb538"

# Backwards compatibility aliases
COLOR_SEPHIRAH_CYAN: Final[str] = COLOR_LUMINOUS_CYAN
COLOR_SEPHIRAH_BG: Final[str] = COLOR_COSMIC_BG
COLOR_SEPHIRAH_GLOW: Final[str] = COLOR_COSMIC_GLOW
COLOR_SEPHIRAH_BORDER: Final[str] = COLOR_COSMIC_BORDER

COLOR_BORDER: Final[str] = "#30363d"
COLOR_GRID: Final[str] = "#21262d"
COLOR_MATH: Final[str] = "#00f5db"

# --- Canonical EIGEN Spectrum ---
EIGEN_CYAN: Final[str] = "#00e8ff"  # 0x00e8ff
EIGEN_SKY: Final[str] = "#14b5ff"  # 0x14b5ff
EIGEN_BLUE: Final[str] = "#3a98ff"  # 0x3a98ff
EIGEN_PURPLE: Final[str] = "#7952f5"  # 0x7952f5

EIGEN_COLORS: Final[Dict[str, str]] = {
    "cyan": EIGEN_CYAN,
    "sky": EIGEN_SKY,
    "blue": EIGEN_BLUE,
    "purple": EIGEN_PURPLE,
}

# --- Vibrant 10-Node Spectrum ---
EIGEN_NODES: Final[Dict[str, str]] = {
    "node_0": "#fff9d6",  # 0. Crown / Divine White-Gold (0xFFF9D6)
    "node_1": "#00ffff",  # 1. Electric Pure Cyan (0x00FFFF)
    "node_2": "#00e8ff",  # 2. Vibrant Cyan (0x00E8FF)
    "node_3": "#14b5ff",  # 3. Sky Blue (0x14B5FF)
    "node_4": "#0070eb",  # 4. Royal Cobalt (0x0070EB)
    "node_5": "#ffd94a",  # 5. Radiant Amber Gold (0xFFD94A)
    "node_6": "#7952f5",  # 6. Electric Purple (0x7952F5)
    "node_7": "#5e17eb",  # 7. Deep Violet (0x5E17EB)
    "node_8": "#ff66b3",  # 8. Neon Hot Pink (0xFF66B3)
    "node_9": "#00c853",  # 9. Vivid Emerald Green (0x00C853)
}

EIGEN_NODE_COLORS: Final[List[str]] = [
    "#fff9d6",  # 0. Crown / White-Gold
    "#00ffff",  # 1. Pure Cyan
    "#00e8ff",  # 2. Vibrant Cyan
    "#14b5ff",  # 3. Sky Blue
    "#0070eb",  # 4. Royal Cobalt
    "#ffd94a",  # 5. Radiant Gold
    "#7952f5",  # 6. Electric Purple
    "#5e17eb",  # 7. Deep Violet
    "#ff66b3",  # 8. Neon Pink
    "#00c853",  # 9. Vivid Emerald Green
]

EIGEN_LABEL_COLORS: Final[List[str]] = [
    "#fff9d6",  # 0. Crown
    "#00ffff",  # 1. Pure Cyan
    "#00e8ff",  # 2. Bright Cyan
    "#14b5ff",  # 3. Sky Blue
    "#0070eb",  # 4. Royal Cobalt
    "#4cc9f0",  # 5. Luminous Solar Cyan
    "#7952f5",  # 6. Electric Purple
    "#5e17eb",  # 7. Deep Violet
    "#ff66b3",  # 8. Neon Pink
    "#00c853",  # 9. Vivid Emerald Green
]

EIGEN_NODE_NAMES: Final[List[str]] = [
    "0️⃣ Keter",
    "1️⃣ Chokhmah",
    "2️⃣ Binah",
    "3️⃣ Chesed",
    "4️⃣ Gevurah",
    "5️⃣ Tiferet",
    "6️⃣ Netzach",
    "7️⃣ Hod",
    "8️⃣ Yesod",
    "9️⃣ Malkuth",
]

# Legacy / Alternative aliases
SEPHIRAH_NODES: Final[Dict[str, str]] = {
    "keter": EIGEN_NODES["node_0"],
    "chokhmah": EIGEN_NODES["node_1"],
    "binah": EIGEN_NODES["node_2"],
    "chesed": EIGEN_NODES["node_3"],
    "gevurah": EIGEN_NODES["node_4"],
    "tiferet": EIGEN_NODES["node_5"],
    "netzach": EIGEN_NODES["node_6"],
    "hod": EIGEN_NODES["node_7"],
    "yesod": EIGEN_NODES["node_8"],
    "malkuth": EIGEN_NODES["node_9"],
}
SEPHIRAH_NODE_COLORS: Final[List[str]] = EIGEN_NODE_COLORS
SEPHIRAH_LABEL_COLORS: Final[List[str]] = EIGEN_LABEL_COLORS
SEPHIRAH_NAMES: Final[List[str]] = EIGEN_NODE_NAMES

# --- ADHD High-Contrast Semantic Palette ---
COLOR_PRIMARY_LIGHT: Final[str] = "#00e8ff"
COLOR_PRIMARY: Final[str] = "#14b5ff"
COLOR_PRIMARY_DARK: Final[str] = "#0070eb"

COLOR_SECONDARY_LIGHT: Final[str] = "#c4b5fd"
COLOR_SECONDARY: Final[str] = "#9b7dff"
COLOR_SECONDARY_DARK: Final[str] = "#7952f5"

COLOR_TERTIARY_LIGHT: Final[str] = "#22f792"
COLOR_TERTIARY: Final[str] = "#10b981"
COLOR_TERTIARY_DARK: Final[str] = "#059669"

COLOR_QUATERNARY_LIGHT: Final[str] = "#fef08a"
COLOR_QUATERNARY: Final[str] = "#f78166"
COLOR_QUATERNARY_DARK: Final[str] = "#ea580c"

COLOR_PERNARY_LIGHT: Final[str] = "#f472b6"
COLOR_PERNARY: Final[str] = "#ec4899"
COLOR_PERNARY_DARK: Final[str] = "#be185d"

# Full token map for Scriber Labs projects
THEME_TOKENS: Final[Dict[str, str]] = {
    # Surfaces & Cosmic Foundations
    "bg": COLOR_BG,
    "surface": COLOR_SURFACE,
    "surface_elevated": COLOR_SURFACE_ELEVATED,
    "bg_cosmic_center": COLOR_BG_COSMIC_CENTER,
    "bg_cosmic": COLOR_BG_COSMIC,
    "bg_cosmic_void": COLOR_BG_COSMIC_VOID,
    "border": COLOR_BORDER,
    "grid": COLOR_GRID,
    # Typography & Overlays
    "text": COLOR_TEXT,
    "text_bright": COLOR_TEXT_BRIGHT,
    "text_muted": COLOR_TEXT_MUTED,
    "text_subtle": COLOR_TEXT_SUBTLE,
    "text_accent": COLOR_TEXT_ACCENT,
    "luminous_cyan": COLOR_LUMINOUS_CYAN,
    "cosmic_bg": COLOR_COSMIC_BG,
    "cosmic_glow": COLOR_COSMIC_GLOW,
    "cosmic_border": COLOR_COSMIC_BORDER,
    "text_sephirah": COLOR_TEXT_SEPHIRAH,
    "sephirah_cyan": COLOR_SEPHIRAH_CYAN,
    "sephirah_bg": COLOR_SEPHIRAH_BG,
    "sephirah_glow": COLOR_SEPHIRAH_GLOW,
    "sephirah_border": COLOR_SEPHIRAH_BORDER,
    "tooltip_bg": COLOR_TOOLTIP_BG,
    "tooltip_border": COLOR_TOOLTIP_BORDER,
    "math": COLOR_MATH,
    # Core EIGEN Spectrum
    "eigen_cyan": EIGEN_CYAN,
    "eigen_sky": EIGEN_SKY,
    "eigen_blue": EIGEN_BLUE,
    "eigen_purple": EIGEN_PURPLE,
    # Vibrant 10-Node Spectrum
    "eigen_node_0": EIGEN_NODES["node_0"],
    "eigen_node_1": EIGEN_NODES["node_1"],
    "eigen_node_2": EIGEN_NODES["node_2"],
    "eigen_node_3": EIGEN_NODES["node_3"],
    "eigen_node_4": EIGEN_NODES["node_4"],
    "eigen_node_5": EIGEN_NODES["node_5"],
    "eigen_node_6": EIGEN_NODES["node_6"],
    "eigen_node_7": EIGEN_NODES["node_7"],
    "eigen_node_8": EIGEN_NODES["node_8"],
    "eigen_node_9": EIGEN_NODES["node_9"],
    # Sephirah Aliases
    "sephirah_keter": SEPHIRAH_NODES["keter"],
    "sephirah_chokhmah": SEPHIRAH_NODES["chokhmah"],
    "sephirah_binah": SEPHIRAH_NODES["binah"],
    "sephirah_chesed": SEPHIRAH_NODES["chesed"],
    "sephirah_gevurah": SEPHIRAH_NODES["gevurah"],
    "sephirah_tiferet": SEPHIRAH_NODES["tiferet"],
    "sephirah_netzach": SEPHIRAH_NODES["netzach"],
    "sephirah_hod": SEPHIRAH_NODES["hod"],
    "sephirah_yesod": SEPHIRAH_NODES["yesod"],
    "sephirah_malkuth": SEPHIRAH_NODES["malkuth"],
    # Semantic Spectrum
    "primary_light": COLOR_PRIMARY_LIGHT,
    "primary": COLOR_PRIMARY,
    "primary_dark": COLOR_PRIMARY_DARK,
    "secondary_light": COLOR_SECONDARY_LIGHT,
    "secondary": COLOR_SECONDARY,
    "secondary_dark": COLOR_SECONDARY_DARK,
    "tertiary_light": COLOR_TERTIARY_LIGHT,
    "tertiary": COLOR_TERTIARY,
    "tertiary_dark": COLOR_TERTIARY_DARK,
    "quaternary_light": COLOR_QUATERNARY_LIGHT,
    "quaternary": COLOR_QUATERNARY,
    "quaternary_dark": COLOR_QUATERNARY_DARK,
    "pernary_light": COLOR_PERNARY_LIGHT,
    "pernary": COLOR_PERNARY,
    "pernary_dark": COLOR_PERNARY_DARK,
    # Extended Primitives & Accents (Obsidian Notes)
    "cyan_pure": COLOR_CYAN_PURE,
    "blue_vibrant": COLOR_BLUE_VIBRANT,
    "blue_azure": COLOR_BLUE_AZURE,
    "blue_sky_light": COLOR_BLUE_SKY_LIGHT,
    "purple_soft": COLOR_PURPLE_SOFT,
    "indigo_accent": COLOR_INDIGO_ACCENT,
    "violet_deep": COLOR_VIOLET_DEEP,
    "pink_hot": COLOR_PINK_HOT,
    "orange_bright": COLOR_ORANGE_BRIGHT,
    "orange_coral": COLOR_ORANGE_CORAL,
    "amber_warm": COLOR_AMBER_WARM,
    "accent_green": COLOR_ACCENT_GREEN,
    "accent_blue": COLOR_ACCENT_BLUE,
    "accent_magenta": COLOR_ACCENT_MAGENTA,
    "accent_amber": COLOR_ACCENT_AMBER,
    "glass_indigo": COLOR_GLASS_INDIGO,
    "glass_purple": COLOR_GLASS_PURPLE,
    "glass_violet": COLOR_GLASS_VIOLET,
    "glass_cyan": COLOR_GLASS_CYAN,
    "glass_cyan_glow": COLOR_GLASS_CYAN_GLOW,
    "glass_blue": COLOR_GLASS_BLUE,
    "glass_sky": COLOR_GLASS_SKY,
}

# -----------------------------------------------------------------------------------------------------------
# 🔮 Signature Gradients & Palette Sequences (Obsidian Notebooks Collection)
# -----------------------------------------------------------------------------------------------------------

GRADIENT_0_CYANS: Final[List[str]] = ["#00ffff", "#00e8ff"]
GRADIENT_1_CYAN_SKY: Final[List[str]] = ["#00ffee", "#14b5ff"]
GRADIENT_2_CYAN_BLUE: Final[List[str]] = ["#00e8ff", "#0070eb"]
GRADIENT_3_TEAL_BLUE: Final[List[str]] = ["#03e8bd", "#03b4e8", "#0355e8"]
GRADIENT_4_CYAN_PURPLE: Final[List[str]] = [
    "#00e8ff",
    "#14b5ff",
    "#0a95eb",
    "#0070eb",
    "#5e17eb",
]
GRADIENT_5_CYAN_DEEP_PURPLE: Final[List[str]] = [
    "#00e8ff",
    "#3a98ff",
    "#0a95eb",
    "#7952f5",
    "#5e17eb",
]
GRADIENT_6_CYAN_PINK: Final[List[str]] = [
    "#00e8ff",
    "#14b5ff",
    "#5280ff",
    "#7952f5",
    "#ff66b3",
]
GRADIENT_7_FULL_FLOW: Final[List[str]] = [
    "#00e8ff",
    "#14b5ff",
    "#5280ff",
    "#7952f5",
    "#ff66b3",
    "#f78166",
]
GRADIENT_8_SYNTHWAVE: Final[List[str]] = [
    "#4cc9f0",
    "#4361ee",
    "#3a0ca3",
    "#7209b7",
    "#f72585",
]
GRADIENT_8_SYNTHWAVE_REV: Final[List[str]] = [
    "#f72585",
    "#7209b7",
    "#3a0ca3",
    "#4361ee",
    "#4cc9f0",
]

EIGENSCRIBE_GRADIENTS: Final[Dict[str, List[str]]] = {
    "gradient_0": GRADIENT_0_CYANS,
    "gradient_1": GRADIENT_1_CYAN_SKY,
    "gradient_2": GRADIENT_2_CYAN_BLUE,
    "gradient_3": GRADIENT_3_TEAL_BLUE,
    "gradient_4": GRADIENT_4_CYAN_PURPLE,
    "gradient_5": GRADIENT_5_CYAN_DEEP_PURPLE,
    "gradient_6": GRADIENT_6_CYAN_PINK,
    "gradient_7": GRADIENT_7_FULL_FLOW,
    "gradient_8": GRADIENT_8_SYNTHWAVE,
    "gradient_8_rev": GRADIENT_8_SYNTHWAVE_REV,
}

# 4-Color Vibrant Accent Set
FOUR_COLOR_ACCENT: Final[List[str]] = ["#38fe52", "#3881fe", "#fe38e4", "#feb538"]

# 5-Stop Sequential & Diverging Ramps
RAMP_GREEN: Final[List[str]] = ["#071a12", "#064e3b", "#059669", "#31ff48", "#b7ffcf"]
RAMP_BLUE: Final[List[str]] = ["#06152b", "#003b73", "#0070eb", "#00b8ff", "#b8f6ff"]
RAMP_PURPLE: Final[List[str]] = ["#120a24", "#3b176e", "#7c3aed", "#a855f7", "#d8b4fe"]
RAMP_MAGENTA: Final[List[str]] = ["#210817", "#7c174f", "#ad1457", "#f72585", "#ffb4f6"]

# 5-Stop Obsidian Palette Scales
PALETTE_PINK_AMBER: Final[List[str]] = [
    "#f75594",
    "#f7556b",
    "#f76755",
    "#f78f55",
    "#f7b855",
]
PALETTE_NEON_GREEN: Final[List[str]] = [
    "#81fe38",
    "#50fe38",
    "#38fe52",
    "#38fe84",
    "#38feb5",
]
PALETTE_CYAN_BLUE: Final[List[str]] = [
    "#00ff97",
    "#00ffd6",
    "#00e8ff",
    "#00a8ff",
    "#0068ff",
]
PALETTE_BLUE_VIOLET: Final[List[str]] = [
    "#52d6ff",
    "#52abff",
    "#5280ff",
    "#5255ff",
    "#7a52ff",
]
PALETTE_INDIGO_MAGENTA: Final[List[str]] = [
    "#527cf5",
    "#5254f5",
    "#7952f5",
    "#a252f5",
    "#ca52f5",
]

# Deep Void / Shaded Ramps
RAMP_DEEP_PURPLE: Final[List[str]] = [
    "#462c96",
    "#33216e",
    "#211547",
    "#0f0920",
    "#000000",
]
RAMP_DEEP_VIOLET: Final[List[str]] = [
    "#371f9d",
    "#281673",
    "#190e48",
    "#0a061d",
    "#000000",
]
RAMP_SKY_BLUE: Final[List[str]] = [
    "#66c4ff",
    "#33b1ff",
    "#009dff",
    "#007ecc",
    "#005e99",
]

# High-contrast multi-curve line color cycle (optimized for distinctiveness & readability on dark surfaces)
HIGH_CONTRAST_CYCLE: Final[List[str]] = [
    COLOR_PRIMARY_LIGHT,  # #00e8ff Electric Cyan
    COLOR_PERNARY,  # #ec4899 Hot Magenta / Pink
    COLOR_TERTIARY_LIGHT,  # #22f792 Neon Emerald
    COLOR_QUATERNARY,  # #f78166 Coral Orange
    COLOR_SECONDARY,  # #9b7dff Cosmic Purple / Violet
    COLOR_QUATERNARY_LIGHT,  # #fef08a Radiant Yellow
    COLOR_PRIMARY,  # #14b5ff Electric Blue
    COLOR_MATH,  # #00f5db Turquoise / Math Accent
]

# --- Generalized Multi-Plot Style Palettes (Styles 1, 2, 3, NetworkX Graphs, Metrics) ---
# Style 1: Tri-Tone Contrast Palette (e.g. solvers, differential states, primary multi-series)
STYLE_1_PALETTE: Final[Dict[str, str]] = {
    "primary": COLOR_PRIMARY_LIGHT,
    "secondary": COLOR_SECONDARY,
    "accent": "#f472b6",
}

# Style 2: NetworkX Graphs Palette (for topological structures, graph nodes, and networks)
NETWORKX_GRAPHS_PALETTE: Final[Dict[str, str]] = {
    "complete": COLOR_PRIMARY_LIGHT,
    "ring": COLOR_SECONDARY,
    "small_world": COLOR_PRIMARY,
    "erdos_renyi": COLOR_QUATERNARY,
}

# Style 3: Quantitative Metrics & Analysis Palette (order parameters, invariants, spectra)
STYLE_3_PALETTE: Final[Dict[str, str]] = {
    "metric_primary": COLOR_PRIMARY_LIGHT,
    "metric_secondary": "#00ff7f",
    "metric_tertiary": "#ff9d57",
    "metric_quaternary": "#a855f7",
}

# Style 4: 4-Color Vibrant Accent Palette (high-energy visual markers)
STYLE_4_PALETTE: Final[Dict[str, str]] = {
    "accent_green": COLOR_ACCENT_GREEN,
    "accent_blue": COLOR_ACCENT_BLUE,
    "accent_magenta": COLOR_ACCENT_MAGENTA,
    "accent_amber": COLOR_ACCENT_AMBER,
}

# Obsidian 5-Color Palette Scales
PALETTE_PINK_AMBER_MAP: Final[Dict[str, str]] = {
    f"p_{i}": c for i, c in enumerate(PALETTE_PINK_AMBER)
}
PALETTE_NEON_GREEN_MAP: Final[Dict[str, str]] = {
    f"g_{i}": c for i, c in enumerate(PALETTE_NEON_GREEN)
}
PALETTE_CYAN_BLUE_MAP: Final[Dict[str, str]] = {
    f"c_{i}": c for i, c in enumerate(PALETTE_CYAN_BLUE)
}
PALETTE_BLUE_VIOLET_MAP: Final[Dict[str, str]] = {
    f"b_{i}": c for i, c in enumerate(PALETTE_BLUE_VIOLET)
}
PALETTE_INDIGO_MAGENTA_MAP: Final[Dict[str, str]] = {
    f"m_{i}": c for i, c in enumerate(PALETTE_INDIGO_MAGENTA)
}

# 5-Stop Sequential & Diverging Ramps
RAMP_GREEN_MAP: Final[Dict[str, str]] = {f"g_{i}": c for i, c in enumerate(RAMP_GREEN)}
RAMP_BLUE_MAP: Final[Dict[str, str]] = {f"b_{i}": c for i, c in enumerate(RAMP_BLUE)}
RAMP_PURPLE_MAP: Final[Dict[str, str]] = {
    f"p_{i}": c for i, c in enumerate(RAMP_PURPLE)
}
RAMP_MAGENTA_MAP: Final[Dict[str, str]] = {
    f"m_{i}": c for i, c in enumerate(RAMP_MAGENTA)
}

# Unified registry of generalized comparison palettes
COMPARISON_PALETTES: Final[Dict[str, Dict[str, str]]] = {
    "eigen": EIGEN_COLORS,
    "eigen_nodes": EIGEN_NODES,
    "sephirah_nodes": SEPHIRAH_NODES,
    "style_1": STYLE_1_PALETTE,
    "networkx_graphs": NETWORKX_GRAPHS_PALETTE,
    "style_3": STYLE_3_PALETTE,
    "style_4_accents": STYLE_4_PALETTE,
    "pink_amber": PALETTE_PINK_AMBER_MAP,
    "neon_green": PALETTE_NEON_GREEN_MAP,
    "cyan_blue": PALETTE_CYAN_BLUE_MAP,
    "blue_violet": PALETTE_BLUE_VIOLET_MAP,
    "indigo_magenta": PALETTE_INDIGO_MAGENTA_MAP,
    "ramp_green": RAMP_GREEN_MAP,
    "ramp_blue": RAMP_BLUE_MAP,
    "ramp_purple": RAMP_PURPLE_MAP,
    "ramp_magenta": RAMP_MAGENTA_MAP,
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Core definitions
# -----------------------------------------------------------------------------------------------------------


def create_eigenscribe_colormap(
    name: str, colors: Sequence[str], n_bins: int = 256
) -> LinearSegmentedColormap:
    """Construct a clean, high-contrast LinearSegmentedColormap.

    Parameters
    ----------
    name : str
        Canonical name identifier for the registered colormap.
    colors : Sequence[str]
        List or tuple of valid hex/RGB color strings defining anchor stops.
    n_bins : int, default=256
        The number of discrete quantization levels in the lookup table.

    Returns
    -------
    LinearSegmentedColormap
        The interpolated colormap instance.
    """
    assert len(colors) >= 2, "A colormap must contain at least two color anchor stops."
    return LinearSegmentedColormap.from_list(name, list(colors), N=n_bins)


# Heatmap style 1: Pink-to-Blue Gradient (Vibrant Diverging/Sequential High Contrast)
HEATMAP_PINK_TO_BLUE: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_pink_to_blue",
    [COLOR_PERNARY, COLOR_SECONDARY_LIGHT, COLOR_PRIMARY, COLOR_PRIMARY_LIGHT],
)

# Heatmap style 2: Light Blue-to-Dark Blue Gradient (Sequential High Dynamic Range)
HEATMAP_LIGHT_BLUE_TO_DARK_BLUE: Final[LinearSegmentedColormap] = (
    create_eigenscribe_colormap(
        "eigenscribe_light_blue_to_dark_blue",
        [COLOR_PRIMARY_LIGHT, COLOR_PRIMARY, COLOR_PRIMARY_DARK],
    )
)

# Heatmap style 3: Light Green-to-Dark Green Gradient (Sequential STEM / Coherence Metric)
HEATMAP_LIGHT_GREEN_TO_DARK_GREEN: Final[LinearSegmentedColormap] = (
    create_eigenscribe_colormap(
        "eigenscribe_light_green_to_dark_green",
        [COLOR_TERTIARY_LIGHT, COLOR_TERTIARY, COLOR_TERTIARY_DARK],
    )
)

# Heatmap style 4: High-Contrast Cyclic Phase Colormap (0 to 2π Continuous)
HEATMAP_CYCLIC_PHASE: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_cyclic_phase",
    ["#0070eb", "#0a95eb", "#14b5ff", "#00f0ff", "#a855f7", "#5e17eb", "#0070eb"],
)

# Heatmap style 5: Deep Cosmic Void to Luminous Cyan
HEATMAP_COSMIC_CYAN: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_cosmic_cyan",
    [
        COLOR_BG_COSMIC_VOID,
        COLOR_BG_COSMIC,
        COLOR_PRIMARY_DARK,
        COLOR_PRIMARY,
        COLOR_PRIMARY_LIGHT,
        COLOR_LUMINOUS_CYAN,
    ],
)
HEATMAP_COSMIC_SEPHIRAH: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_cosmic_sephirah",
    [
        COLOR_BG_COSMIC_VOID,
        COLOR_BG_COSMIC,
        COLOR_PRIMARY_DARK,
        COLOR_PRIMARY,
        COLOR_PRIMARY_LIGHT,
        COLOR_LUMINOUS_CYAN,
    ],
)

# Heatmap style 6: Cosmic Void to Electric Cyan
HEATMAP_COSMIC_VOID_TO_CYAN: Final[LinearSegmentedColormap] = (
    create_eigenscribe_colormap(
        "eigenscribe_cosmic_void_to_cyan",
        [COLOR_BG_COSMIC, COLOR_PRIMARY_DARK, COLOR_PRIMARY_LIGHT, COLOR_LUMINOUS_CYAN],
    )
)

# Heatmap style 7: Vibrant 10-Node Cosmic Spectrum
HEATMAP_COSMIC_SPECTRUM: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_cosmic_spectrum",
    [
        EIGEN_NODES["node_9"],
        EIGEN_NODES["node_8"],
        EIGEN_NODES["node_7"],
        EIGEN_NODES["node_6"],
        EIGEN_NODES["node_5"],
        EIGEN_NODES["node_4"],
        EIGEN_NODES["node_3"],
        EIGEN_NODES["node_2"],
        EIGEN_NODES["node_1"],
        EIGEN_NODES["node_0"],
    ],
)
HEATMAP_SEPHIRAH_SPECTRUM: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_sephirah_spectrum",
    [
        EIGEN_NODES["node_9"],
        EIGEN_NODES["node_8"],
        EIGEN_NODES["node_7"],
        EIGEN_NODES["node_6"],
        EIGEN_NODES["node_5"],
        EIGEN_NODES["node_4"],
        EIGEN_NODES["node_3"],
        EIGEN_NODES["node_2"],
        EIGEN_NODES["node_1"],
        EIGEN_NODES["node_0"],
    ],
)

# Signature Obsidian Gradients Colormaps
HEATMAP_GRADIENT_0: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_0", GRADIENT_0_CYANS
)
HEATMAP_GRADIENT_1: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_1", GRADIENT_1_CYAN_SKY
)
HEATMAP_GRADIENT_2: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_2", GRADIENT_2_CYAN_BLUE
)
HEATMAP_GRADIENT_3: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_3", GRADIENT_3_TEAL_BLUE
)
HEATMAP_GRADIENT_4: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_4", GRADIENT_4_CYAN_PURPLE
)
HEATMAP_GRADIENT_5: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_5", GRADIENT_5_CYAN_DEEP_PURPLE
)
HEATMAP_GRADIENT_6: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_6", GRADIENT_6_CYAN_PINK
)
HEATMAP_GRADIENT_7: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_7", GRADIENT_7_FULL_FLOW
)
HEATMAP_GRADIENT_8: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_gradient_8", GRADIENT_8_SYNTHWAVE
)
HEATMAP_SYNTHWAVE: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_synthwave", GRADIENT_8_SYNTHWAVE_REV
)

# 5-Stop Sequential Ramp Colormaps
HEATMAP_RAMP_GREEN: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_ramp_green", RAMP_GREEN
)
HEATMAP_RAMP_BLUE: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_ramp_blue", RAMP_BLUE
)
HEATMAP_RAMP_PURPLE: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_ramp_purple", RAMP_PURPLE
)
HEATMAP_RAMP_MAGENTA: Final[LinearSegmentedColormap] = create_eigenscribe_colormap(
    "eigenscribe_ramp_magenta", RAMP_MAGENTA
)

# Plotly Format Cyclic Phase Colorscale (for Dash / Plotly heatmaps & circle graphs)
PLOTLY_CYCLIC_PHASE_COLORSCALE: Final[List[List[Any]]] = [
    [0.0, "#0070eb"],
    [0.2, "#0A95EB"],
    [0.35, "#14B5FF"],
    [0.5, "#00f0ff"],
    [0.65, "#A855F7"],
    [0.8, "#5E17EB"],
    [1.0, "#0070eb"],
]

# Semantic Colormaps (exported for generalized continuous gradient visualizations)
SEMANTIC_COLORMAPS: Final[Dict[str, LinearSegmentedColormap]] = {
    "Phase [0, 2π)": create_eigenscribe_colormap(
        "eigenscribe_phase",
        [COLOR_PRIMARY_LIGHT, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_TERTIARY],
    ),
    "Cyclic Phase": HEATMAP_CYCLIC_PHASE,
    "Cosmic Cyan": HEATMAP_COSMIC_CYAN,
    "Cosmic Sephirah": HEATMAP_COSMIC_SEPHIRAH,
    "Cosmic Void to Cyan": HEATMAP_COSMIC_VOID_TO_CYAN,
    "Cosmic Spectrum": HEATMAP_COSMIC_SPECTRUM,
    "Order Parameter [0, 1]": create_eigenscribe_colormap(
        "eigenscribe_order_param",
        [COLOR_SURFACE, COLOR_PRIMARY, COLOR_PRIMARY_LIGHT],
    ),
    "Spectral Density": create_eigenscribe_colormap(
        "eigenscribe_spectral",
        [COLOR_BG, COLOR_SECONDARY_DARK, COLOR_PERNARY, COLOR_QUATERNARY_LIGHT],
    ),
    "Hamiltonian Energy": create_eigenscribe_colormap(
        "eigenscribe_energy",
        [COLOR_PRIMARY, COLOR_SURFACE, "#ff9d57"],
    ),
    "Temporal Flow": create_eigenscribe_colormap(
        "eigenscribe_temporal",
        [COLOR_BG, "#5280ff", "#00e8ff", COLOR_TERTIARY_LIGHT],
    ),
    "Gradient 4 (Cyan-Purple)": HEATMAP_GRADIENT_4,
    "Gradient 6 (Cyan-Pink)": HEATMAP_GRADIENT_6,
    "Gradient 7 (Full Flow)": HEATMAP_GRADIENT_7,
    "Gradient 8 (Synthwave)": HEATMAP_GRADIENT_8,
    "Ramp Green": HEATMAP_RAMP_GREEN,
    "Ramp Blue": HEATMAP_RAMP_BLUE,
    "Ramp Purple": HEATMAP_RAMP_PURPLE,
    "Ramp Magenta": HEATMAP_RAMP_MAGENTA,
}

# Canonical Colormap Registry
EIGENSCRIBE_COLORMAPS: Final[Dict[str, LinearSegmentedColormap]] = {
    "pink_to_blue": HEATMAP_PINK_TO_BLUE,
    "light_blue_to_dark_blue": HEATMAP_LIGHT_BLUE_TO_DARK_BLUE,
    "light_green_to_dark_green": HEATMAP_LIGHT_GREEN_TO_DARK_GREEN,
    "cyclic_phase": HEATMAP_CYCLIC_PHASE,
    "cosmic_cyan": HEATMAP_COSMIC_CYAN,
    "cosmic_sephirah": HEATMAP_COSMIC_SEPHIRAH,
    "cosmic_void_to_cyan": HEATMAP_COSMIC_VOID_TO_CYAN,
    "cosmic_spectrum": HEATMAP_COSMIC_SPECTRUM,
    "sephirah_spectrum": HEATMAP_SEPHIRAH_SPECTRUM,
    "gradient_0": HEATMAP_GRADIENT_0,
    "gradient_1": HEATMAP_GRADIENT_1,
    "gradient_2": HEATMAP_GRADIENT_2,
    "gradient_3": HEATMAP_GRADIENT_3,
    "gradient_4": HEATMAP_GRADIENT_4,
    "gradient_5": HEATMAP_GRADIENT_5,
    "gradient_6": HEATMAP_GRADIENT_6,
    "gradient_7": HEATMAP_GRADIENT_7,
    "gradient_8": HEATMAP_GRADIENT_8,
    "synthwave": HEATMAP_SYNTHWAVE,
    "ramp_green": HEATMAP_RAMP_GREEN,
    "ramp_blue": HEATMAP_RAMP_BLUE,
    "ramp_purple": HEATMAP_RAMP_PURPLE,
    "ramp_magenta": HEATMAP_RAMP_MAGENTA,
    **{k.lower().split()[0]: v for k, v in SEMANTIC_COLORMAPS.items()},
}


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------


def register_colormaps() -> None:
    """Register all Eigenscribe signature colormaps into matplotlib's global colormap registry."""
    for cmap_name, cmap_obj in EIGENSCRIBE_COLORMAPS.items():
        if cmap_obj.name not in mpl.colormaps:
            mpl.colormaps.register(cmap_obj, name=cmap_obj.name, force=False)
        alias_name = f"scriber_{cmap_name}"
        if alias_name not in mpl.colormaps:
            mpl.colormaps.register(cmap_obj, name=alias_name, force=False)


def get_eigenscribe_rcparams(cosmic: bool = False) -> Dict[str, Any]:
    """Generate the canonical matplotlib rcParams dictionary for The Scriber Experience.

    Parameters
    ----------
    cosmic : bool, default=False
        If True, applies deep cosmic void foundations (#050812 / #0a0f1f) instead
        of standard dark slate (#0d1117 / #161b22).

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams properties configuring figure, axes, grid, fonts, and colors.
    """
    fig_bg = COLOR_BG_COSMIC if cosmic else COLOR_BG
    axes_bg = COLOR_BG_COSMIC_CENTER if cosmic else COLOR_SURFACE

    return {
        # Style & Foundations
        "figure.facecolor": fig_bg,
        "figure.edgecolor": fig_bg,
        "figure.dpi": 100,
        "savefig.facecolor": fig_bg,
        "savefig.edgecolor": fig_bg,
        # Axes & Frames
        "axes.facecolor": axes_bg,
        "axes.edgecolor": COLOR_BORDER,
        "axes.linewidth": 1.0,
        "axes.labelcolor": COLOR_TEXT,
        "axes.labelsize": 10.5,
        "axes.labelweight": "normal",
        "axes.titlesize": 12.0,
        "axes.titleweight": "bold",
        "axes.titlecolor": COLOR_TEXT_BRIGHT,
        "axes.titlepad": 10.0,
        "axes.prop_cycle": mpl.cycler(color=HIGH_CONTRAST_CYCLE),
        # Grid System
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": COLOR_GRID,
        "grid.alpha": 0.7,
        "grid.linestyle": "--",
        "grid.linewidth": 0.8,
        # Ticks & Markers
        "xtick.color": COLOR_TEXT_MUTED,
        "ytick.color": COLOR_TEXT_MUTED,
        "xtick.labelsize": 9.0,
        "ytick.labelsize": 9.0,
        "xtick.direction": "out",
        "ytick.direction": "out",
        # Text & Fonts
        "text.color": COLOR_TEXT,
        "font.family": "sans-serif",
        "font.sans-serif": [
            "Segoe UI",
            "SF Pro Display",
            "Inter",
            "DejaVu Sans",
            "Arial",
            "sans-serif",
        ],
        "mathtext.fontset": "cm",
        # Legends
        "legend.facecolor": axes_bg,
        "legend.edgecolor": COLOR_BORDER,
        "legend.labelcolor": COLOR_TEXT,
        "legend.fontsize": 9.0,
        "legend.framealpha": 0.85,
        "legend.fancybox": True,
        # Lines & Scatters
        "lines.linewidth": 2.0,
        "lines.solid_capstyle": "round",
        "patch.edgecolor": COLOR_BORDER,
        "patch.force_edgecolor": True,
    }


def apply_theme(
    seaborn: bool = True,
    custom_rc: Optional[Mapping[str, Any]] = None,
    cosmic: bool = False,
) -> None:
    """Bootstrap and activate the Eigenscribe dark high-contrast visual theme.

    Applies rcParams to Matplotlib/Pyplot and configures Seaborn context and palettes
    when available.

    Parameters
    ----------
    seaborn : bool, default=True
        Whether to configure Seaborn theme settings if Seaborn is installed.
    custom_rc : Optional[Mapping[str, Any]], optional
        Optional dictionary of additional or overriding rcParams.
    cosmic : bool, default=False
        If True, applies deep cosmic void styling with luminous Sephirah accents.
    """
    register_colormaps()
    rc_params = get_eigenscribe_rcparams(cosmic=cosmic)

    if custom_rc:
        rc_params.update(custom_rc)

    plt.style.use("dark_background")
    plt.rcParams.update(rc_params)

    if seaborn and HAS_SEABORN and sns is not None:
        sns.set_theme(style="darkgrid", rc=rc_params, palette=HIGH_CONTRAST_CYCLE)


def apply_cosmic_theme(
    seaborn: bool = True,
    custom_rc: Optional[Mapping[str, Any]] = None,
) -> None:
    """Bootstrap and activate the Eigenscribe deep cosmic visual theme with Sephirah styling.

    Applies deep cosmic void (#050812 / #0a0f1f) background rcParams to Matplotlib/Pyplot
    and configures Seaborn context and palettes with luminous Sephirah accents.

    Parameters
    ----------
    seaborn : bool, default=True
        Whether to configure Seaborn theme settings if Seaborn is installed.
    custom_rc : Optional[Mapping[str, Any]], optional
        Optional dictionary of additional or overriding rcParams.
    """
    apply_theme(seaborn=seaborn, custom_rc=custom_rc, cosmic=True)


def plot_eigenscribe_heatmap(
    data: NDArray[np.float64],
    style: str = "pink_to_blue",
    ax: Optional[plt.Axes] = None,
    title: Optional[str] = None,
    cbar: bool = True,
    cbar_label: Optional[str] = None,
    annot: bool = False,
    fmt: str = ".2f",
    **kwargs: Any,
) -> plt.Axes:
    """Render a generalizable, high-contrast heatmap using Matplotlib or Seaborn.

    Parameters
    ----------
    data : NDArray[np.float64]
        2D numerical array representing the heatmap matrix.
    style : str, default="pink_to_blue"
        Colormap style choice: 'pink_to_blue', 'light_blue_to_dark_blue', or 'light_green_to_dark_green'.
    ax : Optional[plt.Axes], optional
        Matplotlib Axes to render on. If None, uses current axes or creates one.
    title : Optional[str], optional
        Title string for the plot.
    cbar : bool, default=True
        Whether to display the colorbar.
    cbar_label : Optional[str], optional
        Label for the colorbar axis.
    annot : bool, default=False
        If True, annotate matrix cell values.
    fmt : str, default=".2f"
        String formatting for annotations.
    **kwargs : Any
        Additional keyword arguments forwarded to sns.heatmap or ax.imshow.

    Returns
    -------
    plt.Axes
        The Matplotlib Axes containing the generated heatmap.
    """
    assert (
        data.ndim == 2
    ), f"Expected 2D matrix data for heatmap, got shape {data.shape}"

    cmap = _resolve_heatmap_colormap(style)

    if ax is None:
        ax = plt.gca()

    if HAS_SEABORN and sns is not None:
        cbar_kws = kwargs.pop("cbar_kws", {})
        if cbar_label:
            cbar_kws["label"] = cbar_label

        sns.heatmap(
            data,
            ax=ax,
            cmap=cmap,
            cbar=cbar,
            annot=annot,
            fmt=fmt,
            cbar_kws=cbar_kws,
            **kwargs,
        )
    else:
        im = ax.imshow(data, cmap=cmap, aspect=kwargs.get("aspect", "auto"), **kwargs)
        if cbar:
            cb = plt.colorbar(im, ax=ax)
            if cbar_label:
                cb.set_label(cbar_label, color=COLOR_TEXT)
            cb.ax.yaxis.set_tick_params(color=COLOR_TEXT_MUTED)
            plt.setp(cb.ax.yaxis.get_ticklabels(), color=COLOR_TEXT_MUTED)

        if annot:
            nrows, ncols = data.shape
            for i in range(nrows):
                for j in range(ncols):
                    val = data[i, j]
                    ax.text(
                        j,
                        i,
                        format(val, fmt.lstrip(".")),
                        ha="center",
                        va="center",
                        color=COLOR_TEXT_BRIGHT,
                        fontsize=8,
                    )

    if title:
        ax.set_title(
            title, fontsize=12, fontweight="bold", color=COLOR_TEXT_BRIGHT, pad=10
        )

    return ax


def create_plotly_base_figure(title: str = "", height: int = 340) -> Any:
    """Create a Plotly figure pre-configured with the Scriber dark glassmorphic theme.

    Parameters
    ----------
    title : str, default=""
        Plot/dashboard card header title text.
    height : int, default=340
        Default figure pixel height.

    Returns
    -------
    plotly.graph_objects.Figure
        Styled Plotly figure instance.
    """
    if not HAS_PLOTLY or go is None:
        raise ImportError(
            "Plotly is required for create_plotly_base_figure. Install via `pip install plotly`."
        )

    figure = go.Figure()
    figure.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor=COLOR_GRAPH_BG,
        margin=dict(l=48, r=20, t=44, b=40),
        title=dict(
            text=title,
            font=dict(family="Aclonica, sans-serif", size=13, color=COLOR_TEXT_BRIGHT),
            x=0.02,
            y=0.96,
        ),
        font=dict(color=COLOR_TEXT_MUTED, family="Aclonica, sans-serif", size=11),
        height=height,
    )
    figure.update_xaxes(
        gridcolor="rgba(160, 180, 220, 0.12)",
        zerolinecolor="rgba(160, 180, 220, 0.18)",
    )
    figure.update_yaxes(
        gridcolor="rgba(160, 180, 220, 0.12)",
        zerolinecolor="rgba(160, 180, 220, 0.18)",
    )
    return figure


# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Private helpers
# -----------------------------------------------------------------------------------------------------------


def _resolve_heatmap_colormap(style: str) -> Colormap:
    """Resolve a colormap instance from a style name or colormap object.

    Parameters
    ----------
    style : str
        Canonical style name or registered colormap identifier.

    Returns
    -------
    Colormap
        Resolved matplotlib Colormap object.
    """
    style_map = {
        "pink_to_blue": HEATMAP_PINK_TO_BLUE,
        "light_blue_to_dark_blue": HEATMAP_LIGHT_BLUE_TO_DARK_BLUE,
        "light_green_to_dark_green": HEATMAP_LIGHT_GREEN_TO_DARK_GREEN,
        "cyclic_phase": HEATMAP_CYCLIC_PHASE,
        "cosmic_cyan": HEATMAP_COSMIC_CYAN,
        "cosmic_sephirah": HEATMAP_COSMIC_SEPHIRAH,
        "cosmic_void_to_cyan": HEATMAP_COSMIC_VOID_TO_CYAN,
        "cosmic_spectrum": HEATMAP_COSMIC_SPECTRUM,
        "sephirah_spectrum": HEATMAP_SEPHIRAH_SPECTRUM,
    }

    if style in style_map:
        return style_map[style]
    elif style in EIGENSCRIBE_COLORMAPS:
        return EIGENSCRIBE_COLORMAPS[style]
    elif style in mpl.colormaps:
        return mpl.colormaps[style]
    else:
        raise ValueError(
            f"Unknown heatmap style '{style}'. Choose from 'pink_to_blue', "
            f"'light_blue_to_dark_blue', 'light_green_to_dark_green', 'cyclic_phase', 'cosmic_cyan', 'cosmic_void_to_cyan', 'cosmic_spectrum', or registered colormaps."
        )


# -----------------------------------------------------------------------------------------------------------
# 4️⃣ Smoke tests / example usage
# -----------------------------------------------------------------------------------------------------------


def run_smoke_test() -> bool:
    """Run comprehensive verification on theme bootstrapping, colormaps, and plots.

    Returns
    -------
    bool
        True if all invariants, registrations, and plot generation checks pass.
    """
    rng = np.random.default_rng(DEFAULT_SEED)

    # 1. Verification of theme application & registration
    apply_theme()
    assert "eigenscribe_pink_to_blue" in mpl.colormaps, "Colormap registration failed."
    assert (
        "eigenscribe_light_blue_to_dark_blue" in mpl.colormaps
    ), "Colormap registration failed."
    assert (
        "eigenscribe_light_green_to_dark_green" in mpl.colormaps
    ), "Colormap registration failed."
    assert (
        "eigenscribe_cyclic_phase" in mpl.colormaps
    ), "Cyclic phase colormap registration failed."
    assert (
        "eigenscribe_cosmic_cyan" in mpl.colormaps
    ), "Cosmic Cyan colormap registration failed."
    assert (
        "eigenscribe_cosmic_sephirah" in mpl.colormaps
    ), "Cosmic Sephirah colormap registration failed."
    assert (
        "eigenscribe_cosmic_void_to_cyan" in mpl.colormaps
    ), "Cosmic Void to Cyan colormap registration failed."
    assert (
        "eigenscribe_cosmic_spectrum" in mpl.colormaps
    ), "Cosmic Spectrum colormap registration failed."
    assert (
        "eigenscribe_sephirah_spectrum" in mpl.colormaps
    ), "Sephirah Spectrum colormap registration failed."
    assert (
        "eigenscribe_gradient_4" in mpl.colormaps
    ), "Gradient 4 colormap registration failed."
    assert (
        "eigenscribe_gradient_8" in mpl.colormaps
    ), "Gradient 8 colormap registration failed."
    assert (
        "eigenscribe_ramp_green" in mpl.colormaps
    ), "Ramp Green colormap registration failed."
    assert (
        "eigenscribe_ramp_magenta" in mpl.colormaps
    ), "Ramp Magenta colormap registration failed."
    assert len(EIGEN_NODES) == 10, "EIGEN nodes count mismatch."
    assert len(EIGEN_NODE_COLORS) == 10, "EIGEN node colors count mismatch."
    assert len(EIGEN_LABEL_COLORS) == 10, "EIGEN label colors count mismatch."
    assert len(EIGEN_COLORS) == 4, "EIGEN colors count mismatch."
    assert len(EIGENSCRIBE_GRADIENTS) >= 9, "Eigenscribe gradients count mismatch."
    assert len(FOUR_COLOR_ACCENT) == 4, "Four-color accent count mismatch."

    # Verify cosmic theme mode
    apply_cosmic_theme()
    assert (
        plt.rcParams["figure.facecolor"] == COLOR_BG_COSMIC
    ), "Cosmic figure facecolor mismatch."
    assert (
        plt.rcParams["axes.facecolor"] == COLOR_BG_COSMIC_CENTER
    ), "Cosmic axes facecolor mismatch."

    # 2. Multi-curve line plot contrast & array validation
    x = np.linspace(0, 10, 100)
    fig, (ax_line, ax_heat) = plt.subplots(1, 2, figsize=(12, 4.5))

    n_curves = 4
    curves = np.array(
        [np.sin(x + i * 0.5) * np.exp(-0.05 * x) for i in range(n_curves)]
    )
    assert curves.shape == (n_curves, len(x)), "Curves matrix shape mismatch."

    for i in range(n_curves):
        ax_line.plot(x, curves[i], label=f"Signal {i+1}")

    ax_line.set_title("Multi-Curve Contrast Test")
    ax_line.set_xlabel("Time ($t$)")
    ax_line.set_ylabel("Amplitude")
    ax_line.legend()

    # 3. Heatmap verification with core styles
    matrix_data = rng.uniform(0.0, 1.0, size=(8, 8))
    assert matrix_data.ndim == 2, "Heatmap matrix must be 2D."

    plot_eigenscribe_heatmap(
        matrix_data,
        style="pink_to_blue",
        ax=ax_heat,
        title="Pink-to-Blue Heatmap",
        cbar_label="Intensity",
    )

    # Test remaining colormaps without error
    for style_name in [
        "light_blue_to_dark_blue",
        "light_green_to_dark_green",
        "cyclic_phase",
        "cosmic_cyan",
        "cosmic_sephirah",
        "cosmic_void_to_cyan",
        "cosmic_spectrum",
        "sephirah_spectrum",
    ]:
        fig_sub, ax_sub = plt.subplots(figsize=(4, 4))
        plot_eigenscribe_heatmap(
            matrix_data, style=style_name, ax=ax_sub, title=style_name
        )
        plt.close(fig_sub)

    plt.close(fig)

    # 4. Verification of Plotly base figure if Plotly is installed
    if HAS_PLOTLY:
        plotly_fig = create_plotly_base_figure("Test Glassmorphic Chart")
        assert (
            plotly_fig.layout.plot_bgcolor == COLOR_GRAPH_BG
        ), "Plotly plot background mismatch."
        assert (
            len(PLOTLY_CYCLIC_PHASE_COLORSCALE) == 7
        ), "Plotly cyclic colorscale stop count mismatch."

    print(
        "[Verification] Smoke tests passed: Theme applied, colormaps registered, and plots verified."
    )
    return True


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Orchestrate visualization bootstrapping smoke tests and demonstration verification."""
    success = run_smoke_test()
    if not success:
        raise ValueError("Visualization boilerplate verification failed.")


if __name__ == "__main__":
    main()
