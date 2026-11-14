"""
cli_gradient_boilerplate.py

ANSI TrueColor multi-stop linear RGB gradient engine for terminal output.
Provides multi-keyframe color interpolation across six-digit hex codes and RGB
tuples, along with curated Eigenscribe brand gradient presets (electric, sunset,
forest, midnight, aurora, cyberpunk).

Usage
-----
>>> from cli_gradient_boilerplate import multi_gradient, PRESETS
>>> print(multi_gradient("Electric Gradient", PRESETS["electric"]))
>>> print(multi_gradient("Custom Stops", ["#00a6ff", "#a855f7", "#ff00c3"]))

Author: Eigenscribe
Date: October 2026
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from typing import Final, TypeAlias

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

__all__: list[str] = [
    "RGB",
    "Color",
    "PRESETS",
    "hex_to_rgb",
    "multi_gradient",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

RGB: TypeAlias = tuple[int, int, int]
Color: TypeAlias = str | RGB

PRESETS: Final[dict[str, tuple[str, ...]]] = {
    # 🌟 Signature Eigenscribe: Blue (#00a6ff) -> Purple (#a855f7) -> Magenta (#ff00c3)
    "electric": ("#00a6ff", "#a855f7", "#ff00c3"),
    # 🌅 Solar Sunset: Orange (#ff6b35) -> Amber (#f7c548) -> Crimson (#d7263d)
    "sunset": ("#ff6b35", "#f7c548", "#d7263d"),
    # 🌲 Deep Forest: Olive (#a7c957) -> Teal (#2a9d8f) -> Pine (#264653)
    "forest": ("#a7c957", "#2a9d8f", "#264653"),
    # 🌌 Midnight Cosmic: Sky Cyan (#38bdf8) -> Lavender (#818cf8) -> Rose (#f43f5e)
    "midnight": ("#38bdf8", "#818cf8", "#f43f5e"),
    # 🌿 Quantum Aurora: Aqua (#06b6d4) -> Emerald (#10b981) -> Lime (#84cc16)
    "aurora": ("#06b6d4", "#10b981", "#84cc16"),
    # ⚡ Cyberpunk Neon: Electric Cyan (#00f0ff) -> Deep Violet (#7000ff) -> Hot Pink (#ff007b)
    "cyberpunk": ("#00f0ff", "#7000ff", "#ff007b"),
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API / Gradient Engine
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


def multi_gradient(
    text: str,
    colors: Sequence[Color] = PRESETS["electric"],
    *,
    bold: bool = True,
) -> str:
    """
    Return text formatted with an ANSI TrueColor gradient across multiple color stops.

    Parameters
    ----------
    text : str
        The input text to colorize.
    colors : Sequence[Color], default=PRESETS["electric"]
        A sequence of at least two color stops, specified as six-digit hex strings
        or (R, G, B) tuples.
    bold : bool, default=True
        Whether to apply bold ANSI formatting.

    Returns
    -------
    str
        ANSI TrueColor-escaped string with color resets appended.

    Raises
    ------
    ValueError
        If fewer than two color stops are provided.
    """
    if not text:
        return ""

    if len(colors) < 2:
        raise ValueError("Provide at least two colors for a gradient")

    rgb_colors = [_normalize_color(color) for color in colors]
    style = "1;" if bold else ""
    segments = len(rgb_colors) - 1
    output: list[str] = []

    for index, character in enumerate(text):
        position = index / (len(text) - 1) if len(text) > 1 else 0.0
        scaled_position = position * segments
        segment = min(int(scaled_position), segments - 1)
        segment_position = scaled_position - segment

        start = rgb_colors[segment]
        end = rgb_colors[segment + 1]

        red = round(start[0] + segment_position * (end[0] - start[0]))
        green = round(start[1] + segment_position * (end[1] - start[1]))
        blue = round(start[2] + segment_position * (end[2] - start[2]))

        output.append(f"\033[{style}38;2;{red};{green};{blue}m{character}")

    output.append("\033[0m")
    return "".join(output)


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Internal Logic & Helpers
# -----------------------------------------------------------------------------------------------------------


def _normalize_color(color: Color) -> RGB:
    """
    Convert a hex string or validate and return an RGB tuple.

    Parameters
    ----------
    color : Color
        A six-digit hex string or an (R, G, B) tuple.

    Returns
    -------
    RGB
        Validated (R, G, B) tuple with channels in [0, 255].

    Raises
    ------
    ValueError
        If RGB tuple channels are out of bounds or not integers.
    """
    if isinstance(color, str):
        return hex_to_rgb(color)

    if (
        len(color) != 3
        or any(not isinstance(ch, int) or isinstance(ch, bool) for ch in color)
        or any(not 0 <= ch <= 255 for ch in color)
    ):
        raise ValueError(
            f"RGB colors must contain three integers from 0 to 255: {color!r}"
        )

    return color


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
