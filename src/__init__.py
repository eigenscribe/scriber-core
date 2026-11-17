# src/__init__.py
"""
Scriber Core root package.
"""

from __future__ import annotations

from typing import Final

from . import cli, frontend
from .frontend import (
    COLOR_PALETTE,
    GRADIENT_PRESETS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    TSE_GRADIENTS,
    colors,
    gradients,
    multi_gradient,
    the_scriber_experience,
)

__version__: Final[str] = "1.0.0"

__all__: list[str] = [
    "__version__",
    "cli",
    "frontend",
    "colors",
    "gradients",
    "the_scriber_experience",
    "COLOR_PALETTE",
    "TSE_COLORS",
    "SEMANTIC_COLORS",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "multi_gradient",
]
