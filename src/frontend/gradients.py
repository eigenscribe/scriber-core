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

from frontend.colors import (
    COLOR_PALETTE,
    Color,
    GOLDEN_RATIO_INVERSE,
    RGB,
    hex_to_rgb,
)

__all__: list[str] = [
    "RGB",
    "Color",
    "GOLDEN_RATIO_INVERSE",
    "GRADIENT_PRESETS",
    "PRESETS",
    "TSE_GRADIENTS",
    "compute_golden_ratio_stop_positions",
    "hex_to_rgb",
    "multi_gradient",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

GRADIENT_PRESETS: Final[dict[str, tuple[str, ...]]] = {
    # 🐉 Signature Eigenscribe Gradient:
    "eigenscribe": (
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["eigen_blue"],
        COLOR_PALETTE["midwest_indigo"],
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
    "electric": (
        COLOR_PALETTE["electric_blue"],
        COLOR_PALETTE["bright_purple"],
        COLOR_PALETTE["bright_magenta"],
    ),
    # 🌅 Solar Sunset: Coral Orange (#ff783d) -> Amber (#f7c548) -> Bright Pink (#ff40a1)
    "sunset": (
        COLOR_PALETTE["coral_orange"],
        COLOR_PALETTE["warning_amber"],
        COLOR_PALETTE["bright_pink"],
    ),
    # 🌲 Deep Forest: Junie Lime (#a7c957) -> Tropical Teal (#03e8bd) -> Granite (#264653)
    "forest": (
        COLOR_PALETTE["junie_lime"],
        COLOR_PALETTE["tropical_teal"],
        COLOR_PALETTE["granite"],
    ),
    # 🌌 Midnight Cosmic: Sky Info (#38bdf8) -> Midwest Indigo (#6f78fa) -> Rose Pink (#ff66b3)
    "midnight": (
        COLOR_PALETTE["sky_info"],
        COLOR_PALETTE["midwest_indigo"],
        COLOR_PALETTE["rose_pink"],
    ),
    # ⚡ Cyberpunk Neon: Bright Cyan (#00f0ff) -> Electric Violet (#5e17eb) -> Hot Pink (#ff007b)
    "cyberpunk": (
        COLOR_PALETTE["bright_cyan"],
        COLOR_PALETTE["electric_violet"],
        COLOR_PALETTE["hot_pink"],
    ),
    # 🩵 Blue Gradient
    "blue_gradient": (
        COLOR_PALETTE["vivid_cyan"],
        COLOR_PALETTE["vivid_sky_blue"],
        COLOR_PALETTE["eigen_blue"],
        COLOR_PALETTE["strong_blue"],
    ),
    # 💚 Green Gradient: Tropical Teal (#01e8bd) -> Success Emerald (#10b981) -> Bright Chartreuse (#70e000)
    "green_gradient": (
        COLOR_PALETTE["tropical_teal"],
        COLOR_PALETTE["success_emerald"],
        COLOR_PALETTE["bright_chartreuse"],
    ),
    # 💜 Purple Gradient: Royal Purple (#7209b7) -> Bright Purple (#a855f7) -> Bright Violet (#7c3aed)
    "purple_gradient": (
        COLOR_PALETTE["royal_purple"],
        COLOR_PALETTE["bright_purple"],
        COLOR_PALETTE["bright_violet"],
    ),
}

# Legacy aliases for backward compatibility — prefer GRADIENT_PRESETS directly.
TSE_GRADIENTS: Final[dict[str, tuple[str, ...]]] = GRADIENT_PRESETS
PRESETS: Final[dict[str, tuple[str, ...]]] = GRADIENT_PRESETS


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API / Gradient Engine
# -----------------------------------------------------------------------------------------------------------


def compute_golden_ratio_stop_positions(num_stops: int) -> list[float]:
    """
    Compute cumulative keyframe positions in [0.0, 1.0] proportioned by the Golden Ratio.

    The segment proportions decrease from left to right according to the Golden Ratio (phi ≈ 1.618),
    giving greater proportion to starting blue/cyan hues on the left-hand side and tapering
    towards purple/pink on the right:
    $$w_k = (1/\\phi)^k \\quad \\text{for } k \\in [0, \\text{num\\_stops} - 2]$$

    Parameters
    ----------
    num_stops : int
        Total number of color stops (must be >= 2).

    Returns
    -------
    list[float]
        Monotonically increasing list of stop positions in [0.0, 1.0].
    """
    if num_stops <= 2:
        return [0.0, 1.0]

    segments = num_stops - 1
    inv_phi = GOLDEN_RATIO_INVERSE  # 1.0 / phi ≈ 0.618033988749895

    weights = [inv_phi ** k for k in range(segments)]
    total_weight = sum(weights)

    positions = [0.0]
    cumulative = 0.0
    for w in weights:
        cumulative += w / total_weight
        positions.append(cumulative)
    positions[-1] = 1.0
    return positions


def multi_gradient(
    text: str,
    colors: Sequence[Color] = GRADIENT_PRESETS["electric"],
    *,
    bold: bool = True,
    golden_ratio_scale: bool = True,
) -> str:
    """
    Return text formatted with an ANSI TrueColor gradient across multiple color stops.

    When `golden_ratio_scale` is True (default), segment lengths decrease from
    left to right according to the Golden Ratio (phi ≈ 1.618), giving greater proportion
    to the starting blue hues on the left and tapering towards purple/pink on the right.

    Parameters
    ----------
    text : str
        The input text to colorize.
    colors : Sequence[Color], default=GRADIENT_PRESETS["electric"]
        A sequence of at least two color stops, specified as six-digit hex strings
        or (R, G, B) tuples.
    bold : bool, default=True
        Whether to apply bold ANSI formatting.
    golden_ratio_scale : bool, default=True
        Whether to scale color segment proportions using the Golden Ratio (phi ≈ 1.618)
        decreasing from left to right.

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
    num_stops = len(rgb_colors)
    segments = num_stops - 1

    if golden_ratio_scale and num_stops > 2:
        stop_positions = compute_golden_ratio_stop_positions(num_stops)
    else:
        stop_positions = [i / segments for i in range(num_stops)]

    output: list[str] = []
    text_len = len(text)

    for index, character in enumerate(text):
        position = index / (text_len - 1) if text_len > 1 else 0.0

        segment = 0
        for s in range(segments):
            if position <= stop_positions[s + 1] or s == segments - 1:
                segment = s
                break

        t_start = stop_positions[segment]
        t_end = stop_positions[segment + 1]
        span = t_end - t_start
        segment_position = (position - t_start) / span if span > 0 else 0.0
        segment_position = max(0.0, min(1.0, segment_position))

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

    # 2. Golden ratio stop position computation
    pos_2 = compute_golden_ratio_stop_positions(2)
    assert pos_2 == [0.0, 1.0]

    pos_3 = compute_golden_ratio_stop_positions(3)
    assert len(pos_3) == 3
    assert abs(pos_3[1] - GOLDEN_RATIO_INVERSE) < 1e-6  # ~0.618034

    pos_4 = compute_golden_ratio_stop_positions(4)
    assert len(pos_4) == 4
    assert abs(pos_4[0] - 0.0) < 1e-6
    assert abs(pos_4[1] - 0.5) < 1e-6
    assert abs(pos_4[2] - (0.5 + (0.5 * GOLDEN_RATIO_INVERSE))) < 1e-6
    assert abs(pos_4[3] - 1.0) < 1e-6

    # 3. Multi-gradient rendering across presets
    for preset_name, stops in GRADIENT_PRESETS.items():
        assert len(stops) >= 2, f"Preset {preset_name} has fewer than 2 stops"
        for stop in stops:
            rgb = hex_to_rgb(stop)
            assert len(rgb) == 3
        rendered = multi_gradient(f"Test preset {preset_name}", stops, golden_ratio_scale=True)
        assert len(rendered) > 0
        assert "\033[0m" in rendered

    # 4. Empty string test
    assert multi_gradient("") == ""

    # 5. Custom RGB tuple stops
    custom_rendered = multi_gradient("Custom RGB", [(0, 0, 0), (255, 255, 255)])
    assert "\033[0m" in custom_rendered

    # 6. Print each gradient preset
    print()
    for preset_name, stops in GRADIENT_PRESETS.items():
        gradient = multi_gradient("████████████████████████████████████████████████████████", stops)
        print(f"  {preset_name}: {gradient}")

    print("\n✅ gradients.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
