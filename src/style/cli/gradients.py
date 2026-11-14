"""
cli_gradient_boilerplate.py

ANSI TrueColor multi-stop linear RGB gradient engine for terminal output.
Provides multi-keyframe color interpolation across six-digit hex codes and RGB
tuples, along with curated Eigenscribe brand gradient presets (electric, sunset,
forest, midnight, aurora, cyberpunk).

Usage
-----
>>> from cli_gradient_boilerplate import multi_gradient, PRESETS
>>> print(multi_gradient("Electric Gradient", PRESETS["electric"]))  # doctest: +SKIP
>>> print(multi_gradient("Custom Stops", ["#00a6ff", "#a855f7", "#ff00c3"]))  # doctest: +SKIP

Author: Eigenscribe
Date: October 2026
Last Updated: November 14 2026
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
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
    "COLORS",
    "CLI_COLORS",
    "PRESETS",
    "hex_to_rgb",
    "multi_gradient",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

RGB: TypeAlias = tuple[int, int, int]
Color: TypeAlias = str | RGB

# 🎨 Single Named Color Palette
COLORS: Final[dict[str, str]] = {
    # 💚🩵 Greens & Teals
    "deep_pine": "#071a12",
    "forest_teal": "#064e38",
    "emerald": "#059669",
    "success_emerald": "#10b981",           # ✨ cli status color: success
    "deep_green": "#038b00",
    "neon_green": "#31ff40",
    "bright_chartreuse": "#70e000",
    "pale_mint": "#b4ffcf",
    "tropical_teal": "#03e8bd",

    # 🩵💙 Cyans & Light Blues
    "pure_cyan": "#00ffff",
    "electric_cyan": "#00ffee",
    "vivid_cyan": "#00e8ff",
    "bright_cerulean": "#03b4e8",
    "bright_azure": "#00b8ff",
    "sky_cyan": "4cc9f0",
    "vivid_sky_blue": "14b5ff",
    "ice_blue": "#b8f6ff",

    # 💙💜 Blues
    "midnight_navy": "#06152b",
    "deep_ocean_blue": "003b73",
    "strong_blue": "#0355e8",
    "vivid_blue": "#0070eb",
    "sky_blue": "#3a98ff",
    "sky_info": "#38bdf8",                     # ✨ cli status color: info
    "periwinkle_blue": "#5280ff",
    "indigo_blue": "#4361ee",

    # 💜🩷 Purples & Violets
    "deep_plum": "#120A24",
    "dark_violet": "#3b176e",
    "deep_indigo": "#3a0ca3",
    "royal_purple": "#7209b7",
    "electric_violet": "#5e17eb",
    "bright_violet": "7c3aed",
    "bright_purple": "#a855f7",
    "pale_lilac": "#d8b4fe",

    # 🩷❤️ Pink & Berries
    "error_crimson": "#d7263d",             # ✨ cli status color: error
    "black_cherry": "#210817",
    "dark_berry": "#7c174f",
    "deep_rose": "#ad1457",
    "vivid_pink": "#f72585",
    "bright_pink": "#ff40a1",
    "rose_pink": "#ff66b3",
    "soft_rose": "#ff76a1",
    "pale_orchid_pink": "#ffb4f6",

    # 🩷🧡💛
    "dusty_peach": "e7a697",
    "coral": "#f78166",
    "soft_coral": "#f77f64",
    "peach_coral": "#f79764",
    "tangerine": "#ff8855",
    "coral_orange": "#ff783d",
    "apricot": "#ff9d57",
    "golden_amber": "#feb639",
    "warning_amber": "#f7c548",           # ✨ cli status color: warning

    # 🖤🤍 Neutrals
    "charcoal": "#1e293b",
    "slate": "#64748b",
    "ghost_white": "#f8fafc",
}

# ⌨️ CLI Status Colors
CLI_COLORS: Final[dict[str, str]] = {
    "success": "success_emerald",
    "info": "sky_info",
    "error": "error_crimson",
    "warning": "warning_amber",
}

PRESETS: Final[dict[str, tuple[str, ...]]] = {
    # 🐉 Signature Eigenscribe (without pink): Blue (#0a95eb) -> Periwinkle (#5280ff) -> Purple (#a855f7)
    "eigenscribe-1": ("#38bdf8", "#0A95EB", "#5280ff", "#5e17eb"),
    # 🌟 Signature Eigenscribe (with pink): Blue (#00a6ff) -> Purple (#a855f7) -> Magenta (#ff00c3)
    "eigenscribe-2": ("#00a6ff", "#a855f7", "#ff00c3"),
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
