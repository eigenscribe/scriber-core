# src/frontend/colors.py
"""
colors.py

Centralized color definitions, eigenscribe palettes, and design tokens for CLI formatting, Matplotlib plotting, mermaid
diagrams, and UI styling.

Author: Eigenscribe
Date: November 14, 2026
Last Updated: November 14, 2026
"""

from __future__ import annotations

import re
from typing import Final, TypeAlias

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

__all__: list[str] = [
    "RGB",
    "Color",
    "COLOR_PALETTE",
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
    "deep_pine": "#071a12",
    "forest_teal": "#064e38",
    "pine": "#059669",
    "success_emerald": "#10b981",  # ⌨️ cli status color: success
    "deep_green": "#038b00",
    "bright_chartreuse": "#70e000",
    "junie-lime": "#a7c957",
    "neon_green": "#31ff40",
    "tropical_teal": "#03e8bd",
    "pale_mint": "#b4ffcf",
    # 🩵💙 Cyans & Light Blues
    "electric_cyan": "#00ffee",  # 🌈 tse-gradient-1
    "pure_cyan": "#00ffff",
    "bright_cyan": "#00f0ff",  # 🐉 tse-cyan
    "vivid_cyan": "#00e8ff",  # 🌈 tse-gradient-2
    "sky_cyan": "#4cc9f0",
    "vivid_sky_blue": "#14b5ff",  # 🌈 tse-gradient-1
    "sky_info": "#38bdf8",  # ⌨️ info
    "ice_blue": "#b8f6ff",
    # 💙💜 Blues
    "midnight_navy": "#06152b",
    "deep_ocean_blue": "#003b73",
    "vivid_blue": "#0070eb",
    "strong_blue": "#0355e8",
    "indigo_blue": "#4361ee",
    "periwinkle_blue": "#5280ff",
    "skyline_blue": "#0a95eb",
    "electric_blue": "#00a6ff",
    "sky_blue": "#3a98ff",
    # 💜🩷 Purples & Violets
    "deep_plum": "#120A24",
    "dark_violet": "#3b176e",
    "deep_indigo": "#3a0ca3",
    "royal_purple": "#7209b7",
    "electric_violet": "#5e17eb",
    "bright_violet": "#7c3aed",
    "bright_purple": "#a855f7",
    "pale_lilac": "#d8b4fe",
    # 🩷❤️ Pink & Berries
    "black_cherry": "#210817",
    "dark_berry": "#7c174f",
    "deep_rose": "#ad1457",
    "vivid_pink": "#f72585",
    "bright_pink": "#ff40a1",
    "rose_pink": "#ff66b3",
    "soft_rose": "#ff76a1",
    "pale_orchid_pink": "#ffb4f6",
    # 🩷❤️🧡 Magentas & Reds
    "bright_magenta": "#ff00c3",
    "hot_pink": "#ff007b",
    "error_crimson": "#d7263d",  # ⌨️ error
    # 🩷🧡💛 Oranges and Corals
    "dusty_peach": "#e7a697",
    "soft_coral": "#f77f64",
    "peach_coral": "#f79764",
    "tangerine": "#ff8855",
    "coral_orange": "#ff783d",
    "apricot": "#ff9d57",
    "golden_amber": "#feb639",
    "warning_amber": "#f7c548",  # ⌨️ warning
    # 🖤🤍 Neutrals
    "charcoal": "#1e293b",
    "granite": "#264653",
    "slate": "#64748b",
    "ghost_white": "#f8fafc",
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API
# -----------------------------------------------------------------------------------------------------------


def hex_to_rgb(hex_color: str) -> RGB:
    """
    Convert a six-digit hex color string, with or without leading '#', to an (R, G, B) tuple.

    Parameters
    ----------
    hex_color : str
        Hex color string (e.g. '#00a6ff' or '00a6ff').

    Returns
    -------
    RGB
        Tuple of three integer color channels (0 to 255).

    Raises
    ------
    ValueError
        If hex_color is not a valid 6-digit hexadecimal color string.
    """
    value = hex_color.removeprefix("#")
    if re.fullmatch(r"[0-9a-fA-F]{6}", value) is None:
        raise ValueError(f"Expected a six-digit hex color, got {hex_color!r}")

    return (
        int(value[0:2], 16),
        int(value[2:4], 16),
        int(value[4:6], 16),
    )


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Verify that all colors in COLOR_PALETTE are valid 6-digit hex codes."""
    print("💨 Running colors.py smoke tests...")
    assert len(COLOR_PALETTE) > 0
    for name, hex_val in COLOR_PALETTE.items():
        rgb = hex_to_rgb(hex_val)
        assert len(rgb) == 3
        assert all(0 <= c <= 255 for c in rgb), f"Channel out of range for {name}: {hex_val}"
    print("✅ colors.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
