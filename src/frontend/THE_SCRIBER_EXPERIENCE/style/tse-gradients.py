# src/frontend/the_scriber_experience/style/tse-gradients.py
"""
tse-gradients.py (Hyphenated alias forwarding to tse_gradients.py)
"""

from __future__ import annotations

from .tse_gradients import (
    GOLDEN_RATIO,
    GOLDEN_RATIO_INVERSE,
    GRADIENT_PRESETS,
    PHI,
    PRESETS,
    TSE_GRADIENTS,
    Color,
    RGB,
    compute_golden_ratio_stop_positions,
    hex_to_rgb,
    main,
    multi_gradient,
)

__all__: list[str] = [
    "RGB",
    "Color",
    "GOLDEN_RATIO",
    "GOLDEN_RATIO_INVERSE",
    "PHI",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "PRESETS",
    "compute_golden_ratio_stop_positions",
    "hex_to_rgb",
    "multi_gradient",
]

if __name__ == "__main__":
    main()
