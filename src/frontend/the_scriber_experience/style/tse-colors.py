# src/frontend/the_scriber_experience/style/tse-colors.py
"""
tse-colors.py (Hyphenated alias forwarding to tse_colors.py)
"""

from __future__ import annotations

from .tse_colors import (
    CLI_COLORS,
    COLOR_PALETTE,
    Color,
    EIGEN_COLORS,
    EIGEN_LABEL_COLORS,
    EIGEN_NODE_COLORS,
    RGB,
    SEMANTIC_COLORS,
    TSE_COLORS,
    hex_to_rgb,
    main,
)

__all__: list[str] = [
    "RGB",
    "Color",
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "CLI_COLORS",
    "EIGEN_COLORS",
    "EIGEN_NODE_COLORS",
    "EIGEN_LABEL_COLORS",
    "hex_to_rgb",
]

if __name__ == "__main__":
    main()
