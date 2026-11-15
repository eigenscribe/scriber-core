# src/frontend/the_scriber_experience/cli/gradients.py
"""
cli_gradient_boilerplate.py / gradients.py

ANSI TrueColor multi-stop linear RGB gradient engine for terminal output.
Provides multi-keyframe color interpolation across six-digit hex codes and RGB
tuples, along with curated Eigenscribe brand gradient presets (electric, sunset,
forest, midnight, aurora, cyberpunk).

Usage
-----
>>> from frontend.the_scriber_experience.cli.gradients import multi_gradient, PRESETS
>>> print(multi_gradient("Electric Gradient", PRESETS["electric"]))  # doctest: +SKIP
>>> print(multi_gradient("Custom Stops", ["#00a6ff", "#a855f7", "#ff00c3"]))  # doctest: +SKIP

Author: Eigenscribe & Scriber Labs
Date: October 2026
Last Updated: November 14, 2026
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Final, TypeAlias

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
        _normalize_color,
        hex_to_rgb,
        multi_gradient,
    )
    from frontend.THE_SCRIBER_EXPERIENCE.style.tse_colors import CLI_COLORS
except ImportError:
    try:
        from src.frontend.gradients import (
            GRADIENT_PRESETS,
            TSE_GRADIENTS,
            Color,
            RGB,
            _normalize_color,
            hex_to_rgb,
            multi_gradient,
        )
        from src.frontend.THE_SCRIBER_EXPERIENCE.style.tse_colors import CLI_COLORS
    except ImportError:
        RGB: TypeAlias = tuple[int, int, int]
        Color: TypeAlias = str | RGB
        CLI_COLORS: Final[dict[str, str]] = {
            "success": "success_emerald",
            "info": "sky_info",
            "error": "error_crimson",
            "warning": "warning_amber",
        }
        GRADIENT_PRESETS: Final[dict[str, tuple[str, ...]]] = {
            "electric": ("#00a6ff", "#a855f7", "#ff00c3"),
            "sunset": ("#ff6b35", "#f7c548", "#ff40a1"),
            "forest": ("#a7c957", "#2a9d8f", "#264653"),
            "midnight": ("#38bdf8", "#818cf8", "#f43f5e"),
            "aurora": ("#06b6d4", "#10b981", "#84cc16"),
            "cyberpunk": ("#00f0ff", "#7000ff", "#ff007b"),
        }
        TSE_GRADIENTS = GRADIENT_PRESETS

        def hex_to_rgb(hex_color: str) -> RGB:
            v = hex_color.removeprefix("#")
            return int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16)

        def _normalize_color(color: Color) -> RGB:
            return hex_to_rgb(color) if isinstance(color, str) else color

        def multi_gradient(
            text: str,
            colors: Sequence[Color] = GRADIENT_PRESETS["electric"],
            *,
            bold: bool = True,
        ) -> str:
            if not text:
                return ""
            rgb_colors = [_normalize_color(c) for c in colors]
            style = "1;" if bold else ""
            segments = len(rgb_colors) - 1
            out = []
            for i, ch in enumerate(text):
                pos = i / (len(text) - 1) if len(text) > 1 else 0.0
                sc = pos * segments
                seg = min(int(sc), segments - 1)
                sp = sc - seg
                st, en = rgb_colors[seg], rgb_colors[seg + 1]
                r = round(st[0] + sp * (en[0] - st[0]))
                g = round(st[1] + sp * (en[1] - st[1]))
                b = round(st[2] + sp * (en[2] - st[2]))
                out.append(f"\033[{style}38;2;{r};{g};{b}m{ch}")
            out.append("\033[0m")
            return "".join(out)

__all__: list[str] = [
    "RGB",
    "Color",
    "CLI_COLORS",
    "PRESETS",
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
    """Sanity checks for gradient engine and presets."""
    print("💨 Running cli_gradient_boilerplate smoke tests...")

    # 1. Hex to RGB conversion
    assert hex_to_rgb("#00a6ff") == (0, 166, 255)
    assert hex_to_rgb("a855f7") == (168, 85, 247)

    # 2. Multi-gradient rendering across presets
    for name, stops in PRESETS.items():
        rendered = multi_gradient(f"Test preset {name}", stops)
        assert len(rendered) > 0
        assert "\033[0m" in rendered

    # 3. Empty string test
    assert multi_gradient("") == ""

    # 4. Custom RGB tuple stops
    custom_rendered = multi_gradient("Custom RGB", [(0, 0, 0), (255, 255, 255)])
    assert "\033[0m" in custom_rendered

    print("✅ cli_gradient_boilerplate smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> int:
    """Print text using one of the built-in gradient presets or run smoke test."""
    parser = argparse.ArgumentParser(
        description="Print text with an ANSI TrueColor gradient."
    )
    parser.add_argument("text", nargs="?", default=None, help="Text to color")
    parser.add_argument(
        "--preset",
        choices=list(PRESETS.keys()),
        default="electric",
        help="Gradient preset to use (default: electric)",
    )
    parser.add_argument(
        "--no-bold",
        action="store_true",
        help="Print without bold styling",
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run smoke test suite",
    )
    args = parser.parse_args()

    if args.smoke or args.text is None:
        _run_smoke_test()
        if args.text is None:
            return 0

    print(multi_gradient(args.text, PRESETS[args.preset], bold=not args.no_bold))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
