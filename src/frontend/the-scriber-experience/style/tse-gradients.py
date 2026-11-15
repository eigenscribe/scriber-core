# src/frontend/the_scriber_experience/style/tse-gradients.py
"""
tse-gradients.py (Hyphenated alias forwarding to tse_gradients.py)
"""

from __future__ import annotations

from .tse_gradients import (
    GRADIENT_PRESETS,
    PRESETS,
    TSE_GRADIENTS,
    Color,
    RGB,
    hex_to_rgb,
    main,
    multi_gradient,
)

__all__: list[str] = [
    "RGB",
    "Color",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "hex_to_rgb",
    "multi_gradient",
]

if __name__ == "__main__":
    main()
