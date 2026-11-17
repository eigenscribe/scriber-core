# src/frontend/the_scriber_experience/style/tse_colors.py
"""
tse_colors.py

The Scriber Experience (TSE) design tokens, semantic palette mappings,
and ADHD high-contrast color roles for terminal, plot, and UI styling.

Author: Eigenscribe & Scriber Labs
Date: November 14, 2026
"""

from __future__ import annotations

from typing import Final

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    from frontend.colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
except ImportError:
    try:
        from src.frontend.colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
    except ImportError:
        from ...colors import COLOR_PALETTE, Color, RGB, hex_to_rgb

__all__: list[str] = [
    "RGB",
    "Color",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "hex_to_rgb",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

# 🔱 Signature TSE Colors
TSE_COLORS: Final[dict[str, str]] = {
    "tse-cyan": COLOR_PALETTE["bright_cyan"],
    "tse-blue": COLOR_PALETTE["electric_blue"],
    "tse-periwinkle": COLOR_PALETTE["periwinkle_blue"],
    "tse-purple": COLOR_PALETTE["bright_purple"],
    "tse-pink": COLOR_PALETTE["vivid_pink"],
}

# 🚦 Semantic Attention & Domain Status Roles
SEMANTIC_COLORS: Final[dict[str, str]] = {
    "info": COLOR_PALETTE["sky_info"],
    "success": COLOR_PALETTE["success_emerald"],
    "warning": COLOR_PALETTE["warning_amber"],
    "error": COLOR_PALETTE["error_crimson"],
    "quantum": COLOR_PALETTE["electric_blue"],
    "rotor": COLOR_PALETTE["bright_violet"],
    "network": COLOR_PALETTE["bright_magenta"],
}

# ⌨️ CLI Status Colors
CLI_COLORS: Final[dict[str, str]] = {
    "success": COLOR_PALETTE["success_emerald"],
    "info": COLOR_PALETTE["sky_info"],
    "error": COLOR_PALETTE["error_crimson"],
    "warning": COLOR_PALETTE["warning_amber"],
}

# 🐉 Canonical EIGEN Spectrum
EIGEN_COLORS: Final[dict[str, str]] = {
    "cyan": COLOR_PALETTE["vivid_cyan"],
    "sky": COLOR_PALETTE["vivid_sky_blue"],
    "blue": COLOR_PALETTE["sky_blue"],
    "purple": COLOR_PALETTE.get("purple_secondary", "#7952f5"),
}

# 🌌 Vibrant 10-Node Spectrum
EIGEN_NODE_COLORS: Final[list[str]] = [
    "#fff9d6",  # Node 0: Pale Yellow
    "#00ffff",  # Node 1: Pure Cyan
    "#00e8ff",  # Node 2: Vivid Cyan
    "#14b5ff",  # Node 3: Vivid Sky Blue
    "#0070eb",  # Node 4: Deep Blue
    "#ffd94a",  # Node 5: Amber Gold
    "#7952f5",  # Node 6: Electric Purple
    "#5e17eb",  # Node 7: Deep Violet
    "#ff66b3",  # Node 8: Rose Pink
    "#00c853",  # Node 9: Bright Green
]

EIGEN_LABEL_COLORS: Final[list[str]] = [
    "#000000",
    "#000000",
    "#000000",
    "#000000",
    "#ffffff",
    "#000000",
    "#ffffff",
    "#ffffff",
    "#000000",
    "#000000",
]


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Validate all palette entries parse to valid (R, G, B) integer tuples."""
    print("💨 Running tse_colors.py smoke tests...")
    for group_name, palette in [
        ("TSE_COLORS", TSE_COLORS),
        ("SEMANTIC_COLORS", SEMANTIC_COLORS),
        ("CLI_COLORS", CLI_COLORS),
        ("EIGEN_COLORS", EIGEN_COLORS),
    ]:
        assert len(palette) > 0, f"{group_name} is empty"
        for name, hex_val in palette.items():
            rgb = hex_to_rgb(hex_val)
            assert len(rgb) == 3
            assert all(0 <= ch <= 255 for ch in rgb), f"Channel out of range for {group_name}.{name}"

    assert len(EIGEN_NODE_COLORS) == 10
    assert len(EIGEN_LABEL_COLORS) == 10
    print("✅ tse_colors.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
