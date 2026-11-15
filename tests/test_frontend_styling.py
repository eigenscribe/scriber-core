# tests/test_frontend_styling.py
"""
test_frontend_styling.py

Test suite verifying Scriber Core frontend design tokens, palettes,
and ANSI TrueColor gradient engine.
"""

from __future__ import annotations

from frontend.THE_SCRIBER_EXPERIENCE.cli import cli_banner, cli_info, cli_success
from frontend.THE_SCRIBER_EXPERIENCE.plots import get_eigenscribe_rcparams

from frontend import (
    COLOR_PALETTE,
    GRADIENT_PRESETS,
    SEMANTIC_COLORS,
    TSE_COLORS,
    TSE_GRADIENTS,
    hex_to_rgb,
    multi_gradient,
)


def test_color_palette_validity() -> None:
    """Verify all hex codes in COLOR_PALETTE parse to valid RGB channels."""
    assert len(COLOR_PALETTE) > 0
    for name, hex_val in COLOR_PALETTE.items():
        rgb = hex_to_rgb(hex_val)
        assert len(rgb) == 3
        assert all(0 <= ch <= 255 for ch in rgb)


def test_tse_colors_and_semantics() -> None:
    """Verify TSE semantic color dictionaries."""
    assert len(TSE_COLORS) >= 5
    assert len(SEMANTIC_COLORS) >= 4
    for name, hex_val in TSE_COLORS.items():
        rgb = hex_to_rgb(hex_val)
        assert len(rgb) == 3


def test_gradient_engine() -> None:
    """Verify multi_gradient output formatting and presets."""
    assert len(GRADIENT_PRESETS) >= 6
    assert len(TSE_GRADIENTS) >= 5

    out = multi_gradient("Test Hello", GRADIENT_PRESETS["electric"])
    assert "\033[0m" in out
    assert len(out) > len("Test Hello")

    # Empty string handling
    assert multi_gradient("") == ""


def test_cli_messaging() -> None:
    """Verify CLI messaging helpers run without exception."""
    cli_info("Testing info message")
    cli_success("Testing success message")
    cli_banner("TEST APP", "Test subtitle")


def test_plot_theme_rcparams() -> None:
    """Verify Matplotlib rcParams dictionary generation."""
    rc = get_eigenscribe_rcparams(cosmic=False)
    assert isinstance(rc, dict)
    assert "figure.facecolor" in rc
    assert rc["figure.facecolor"] == "#0d1117"
