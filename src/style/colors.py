# ../boilerplates/python/style/colors.py
"""
colors.py

Centralized color definitions, eigenscribe palettes, and design tokens for CLI formatting, Matplotlib plotting, mermaid
diagrams, and UI styling.

Author: Eigenscribe
Date: November 14, 2026
Last Updated: November 14, 2026
"""

from __future__ import annotations

from typing import Final, TypeAlias

__all__: list[str] = [
    "RGB",
    "Color",
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "GRADIENT_PRESETS",
    "hex_to_rgb",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

RGB: TypeAlias = tuple[int, int, int]
Color: TypeAlias = str | RGB

# 🎨 Single Named Color Palette
COLOR_PALETTE: Final[dict[str, str]] = {
    # 💚🩵 Greens & Teals
    "deep_pine":         "#071a12",
    "forest_teal":       "#064e38",
    "pine":              "#059669",
    "success_emerald":   "#10b981",    # ⌨️ cli status color: success
    "deep_green":        "#038b00",
    "bright_chartreuse": "#70e000",
    "junie-lime":        "#a7c957",
    "neon_green":        "#31ff40",
    "tropical_teal":     "#03e8bd",
    "pale_mint":         "#b4ffcf",

    # 🩵💙 Cyans & Light Blues
    "electric_cyan":    "#00ffee",  #    🌈 tse-gradient-1
    "pure_cyan":        "#00ffff",
    "vivid_cyan":       "#00e8ff",  #    🌈 tse-gradient-1
    "bright_cyan":      "#00f0ff",  # 🐉
    "vivid_sky_blue":   "#14b5ff",  #    🌈 tse-gradient-1
    "sky_info":         "#38bdf8",  #    🌈 eigenscribe,  ⌨️ cli status color: info
    "sky_cyan":         "#4cc9f0",  #    🌈 tse-gradient-2
    "ice_blue":         "#b8f6ff",

    # 💙💜 Blues
    "midnight_navy":   "#06152b",
    "deep_ocean_blue": "#003b73",
    "vivid_blue":      "#0070eb",
    "strong_blue":     "#0355e8",
    "indigo_blue":     "#4361ee",  #    🌈 tse-gradient-2
    "periwinkle_blue": "#5280ff",  # 🐉 🌈 eigenscribe
    "skyline_blue":    "#0a95eb",  #    🌈 eigenscribe
    "electric_blue":   "#00a6ff",  # 🐉 🌈 tse-gradient-1
    "sky_blue":        "#3a98ff",  #    🌈 eigenscribe


    # 💜🩷 Purples & Violets
    "deep_plum":       "#120A24",
    "dark_violet":     "#3b176e",
    "deep_indigo":     "#3a0ca3",
    "royal_purple":    "#7209b7",
    "electric_violet": "#5e17eb",  # 🌈 eigenscribe
    "bright_violet":   "#7c3aed",
    "bright_purple":   "#a855f7",  # 🐉
    "pale_lilac":      "#d8b4fe",

    # 🩷❤️ Pink & Berries
    "black_cherry":     "#210817",
    "dark_berry":       "#7c174f",
    "deep_rose":        "#ad1457",
    "vivid_pink":       "#f72585", # 🐉
    "bright_pink":      "#ff40a1",
    "rose_pink":        "#ff66b3",
    "soft_rose":        "#ff76a1",
    "pale_orchid_pink": "#ffb4f6",

    # 🩷❤️🧡 Magenta & Sunsets
    "bright_magenta": "#ff00c3",
    "hot_pink":       "#ff007b",
    "error_crimson":  "#d7263d",  # ⌨️ cli status color: error

    # 🩷🧡💛
    "dusty_peach":   "#e7a697",
    "soft_coral":    "#f77f64",
    "peach_coral":   "#f79764",
    "tangerine":     "#ff8855",
    "coral_orange":  "#ff783d",
    "apricot":       "#ff9d57",
    "golden_amber":  "#feb639",
    "warning_amber": "#f7c548",  # ⌨️ cli status color: warning

    # 🖤🤍 Neutrals
    "charcoal":    "#1e293b",
    "granite":     "#264653",
    "slate":       "#64748b",
    "ghost_white": "#f8fafc",
}

TSE_COLORS: Final[dict[str, str]] = {
    "tse-cyan": COLOR_PALETTE["bright_cyan"],
    "tse-blue": COLOR_PALETTE["electric_blue"],
    "tse-periwinkle": COLOR_PALETTE["periwinkle_blue"],
    "tse-purple": COLOR_PALETTE["bright_purple"],
    "tse-pink": COLOR_PALETTE["vivid_pink"],
}

SEMANTIC_COLORS: Final[dict[str, str]] = {
    "info": COLOR_PALETTE["sky_info"],
    "success": COLOR_PALETTE["green_success"],
    "warning": COLOR_PALETTE["warning_amber"],
    "error": COLOR_PALETTE["error_crimson"],
}

# 🌈 Multi-Stop Gradient Sequences
GRADIENT_PRESETS: Final[dict[str, tuple[str, ...]]] = {
    # 🐉 Signature Eigenscribe Gradient:
    "eigenscribe": (
        COLOR_PALETTE["sky_info"],
        COLOR_PALETTE["skyline_blue"],
        COLOR_PALETTE["periwinkle_blue"],
        COLOR_PALETTE["electric_violet"]
    ),
    # 🔱 Signature TSE Gradients:
    "tse-gradient-1": (
        COLOR_PALETTE["electric_cyan"],
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["vivid_sky_blue"],
    ),
    "tse-gradient-2": (
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["vivid_sky_blue"],
        COLOR_PALETTE["skyline_blue"],
        COLOR_PALETTE["vivid_blue"],
        COLOR_PALETTE["electric_violet"],
    ),
    "tse-gradient-3": (
        COLOR_PALETTE[""],
    ),
    "electric": ("#00a6ff", "#a855f7", "#ff00c3"),
    # 🌅 Solar Sunset: Orange (#ff6b35) -> Amber (#f7c548) -> Crimson (#d7263d)
    "sunset": ("#ff6b35", "#f7c548", "#ff40a1"),
    # 🌲 Deep Forest: Olive (#a7c957) -> Teal (#2a9d8f) -> Pine (#264653)
    "forest": ("#a7c957", "#2a9d8f", "#264653"),
    # 🌌 Midnight Cosmic: Sky Cyan (#38bdf8) -> Lavender (#818cf8) -> Rose (#f43f5e)
    "midnight": ("#38bdf8", "#818cf8", "#f43f5e"),
    # 🌿 Quantum Aurora: Aqua (#06b6d4) -> Emerald (#10b981) -> Lime (#84cc16)
    "aurora": ("#06b6d4", "#10b981", "#84cc16"),
    # ⚡ Cyberpunk Neon: Electric Cyan (#00f0ff) -> Deep Violet (#7000ff) -> Hot Pink (#ff007b)
    "cyberpunk": ("#00f0ff", "#7000ff", "#ff007b"),
    # 💜 Purple Gradient: Purple-2 (#7209b7) -> Warm purple (#a855f7) -> Purple-1 (#7952f5)
    "purple_gradient": ("#7209b7", "#a855f7", "#7952f5"),
}
