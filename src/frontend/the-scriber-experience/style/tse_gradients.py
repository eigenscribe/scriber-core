# src/frontend/the_scriber_experience/style/tse_gradients.py
"""
tse_gradients.py

The Scriber Experience (TSE) multi-stop gradient sequences, presets,
and ANSI TrueColor gradient engine wrapper.

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
    from frontend.gradients import (
        GRADIENT_PRESETS,
        TSE_GRADIENTS,
        Color,
        RGB,
        hex_to_rgb,
        multi_gradient,
    )
except ImportError:
    try:
        from src.frontend.gradients import (
            GRADIENT_PRESETS,
            TSE_GRADIENTS,
            Color,
            RGB,
            hex_to_rgb,
            multi_gradient,
        )
    except ImportError:
        from ...gradients import (
            GRADIENT_PRESETS,
            TSE_GRADIENTS,
            Color,
            RGB,
            hex_to_rgb,
            multi_gradient,
        )

__all__: list[str] = [
    "RGB",
    "Color",
    "GRADIENT_PRESETS",
    "TSE_GRADIENTS",
    "hex_to_rgb",
    "multi_gradient",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

PRESETS: Final[dict[str, tuple[str, ...]]] = GRADIENT_PRESETS


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Validate TSE gradient presets and rendering."""
    print("💨 Running tse_gradients.py smoke tests...")
    assert len(TSE_GRADIENTS) > 0
    for name, stops in TSE_GRADIENTS.items():
        assert len(stops) >= 2
        for stop in stops:
            rgb = hex_to_rgb(stop)
            assert len(rgb) == 3
        rendered = multi_gradient(f"TSE Gradient {name}", stops)
        assert "\033[0m" in rendered

    print("✅ tse_gradients.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
