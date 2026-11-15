# src/frontend/gradients.py
"""
gradients.py

ANSI TrueColor multi-stop linear RGB gradient engine and canonical presets.
Provides multi-keyframe color interpolation across six-digit hex codes and RGB
tuples for CLI terminals, dashboards, and visual outputs.

Author: Eigenscribe & Scriber Labs
Date: November 14, 2026
"""

from __future__ import annotations

from collections.abc import Sequence
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
        try:
            from .colors import COLOR_PALETTE, Color, RGB, hex_to_rgb
        except ImportError:
            from colors import COLOR_PALETTE, Color, RGB, hex_to_rgb

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

GRADIENT_PRESETS: Final[dict[str, tuple[str, ...]]] = {
    # 🐉 Signature Eigenscribe Gradient:
    "eigenscribe": (
        COLOR_PALETTE["sky_info"],
        COLOR_PALETTE["skyline_blue"],
        COLOR_PALETTE["periwinkle_blue"],
        COLOR_PALETTE["electric_violet"],
    ),
    # 🔱 Signature TSE Gradients:
    "tse-gradient-1": (
        COLOR_PALETTE["electric_cyan"],
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["vivid_sky_blue"],
    ),
    "tse-gradient-2": (
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["vivid_sky_blue"],
        COLOR_PALETTE["skyline_blue"],
        COLOR_PALETTE["vivid_blue"],
        COLOR_PALETTE["electric_violet"],
    ),
    # 🌟 Eigenscribe signature:
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

TSE_GRADIENTS: Final[dict[str, tuple[str, ...]]] = {
    "tse-gradient-1": GRADIENT_PRESETS["tse-gradient-1"],
    "tse-gradient-2": GRADIENT_PRESETS["tse-gradient-2"],
    "eigenscribe": GRADIENT_PRESETS["eigenscribe"],
    "electric": GRADIENT_PRESETS["electric"],
    "sunset": GRADIENT_PRESETS["sunset"],
    "forest": GRADIENT_PRESETS["forest"],
    "midnight": GRADIENT_PRESETS["midnight"],
    "aurora": GRADIENT_PRESETS["aurora"],
    "cyberpunk": GRADIENT_PRESETS["cyberpunk"],
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API / Gradient Engine
# -----------------------------------------------------------------------------------------------------------


def multi_gradient(
    text: str,
    colors: Sequence[Color] = GRADIENT_PRESETS["electric"],
    *,
    bold: bool = True,
) -> str:
    """
    Return text formatted with an ANSI TrueColor gradient across multiple color stops.

    Parameters
    ----------
    text : str
        The input text to colorize.
    colors : Sequence[Color], default=GRADIENT_PRESETS["electric"]
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
    """Validate all presets and gradient rendering."""
    print("💨 Running gradients.py smoke tests...")
    # 1. Hex to RGB conversion
    assert hex_to_rgb("#00a6ff") == (0, 166, 255)
    assert hex_to_rgb("a855f7") == (168, 85, 247)

    # 2. Multi-gradient rendering across presets
    for preset_name, stops in GRADIENT_PRESETS.items():
        assert len(stops) >= 2, f"Preset {preset_name} has fewer than 2 stops"
        for stop in stops:
            rgb = hex_to_rgb(stop)
            assert len(rgb) == 3
        rendered = multi_gradient(f"Test preset {preset_name}", stops)
        assert len(rendered) > 0
        assert "\033[0m" in rendered

    # 3. Empty string test
    assert multi_gradient("") == ""

    # 4. Custom RGB tuple stops
    custom_rendered = multi_gradient("Custom RGB", [(0, 0, 0), (255, 255, 255)])
    assert "\033[0m" in custom_rendered

    print("✅ gradients.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
