# tests/test_frontend_styling.py
"""
test_frontend_styling.py

Test suite verifying Scriber Core frontend design tokens, palettes,
and ANSI TrueColor gradient engine.
"""

from __future__ import annotations

from scriber_core.cli.messaging import cli_banner, cli_info, cli_success
from scriber_core.frontend.the_scriber_experience.plots import get_eigenscribe_rcparams

from scriber_core.frontend import (
    COLOR_PALETTE,
    GOLDEN_RATIO,
    GOLDEN_RATIO_INVERSE,
    GRADIENT_PRESETS,
    PHI,
    SEMANTIC_COLORS,
    TSE_COLORS,
    TSE_GRADIENTS,
    compute_golden_ratio_stop_positions,
    generate_golden_ratio_gradient,
    hex_to_rgb,
    interpolate_rgb,
    multi_gradient,
    render_golden_ratio_gradient,
    run_colors_smoke_test,
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
    """Verify multi_gradient output formatting, presets, and golden ratio proportioning."""
    assert len(GRADIENT_PRESETS) >= 6
    assert len(TSE_GRADIENTS) >= 5

    # 1. Test golden ratio stop positions
    stops_4 = compute_golden_ratio_stop_positions(4)
    assert len(stops_4) == 4
    assert stops_4[0] == 0.0
    assert stops_4[-1] == 1.0
    # Verify segment proportions decrease from left to right (blue -> purple -> pink)
    seg1 = stops_4[1] - stops_4[0]
    seg2 = stops_4[2] - stops_4[1]
    seg3 = stops_4[3] - stops_4[2]
    assert seg1 > seg2 > seg3
    assert abs((seg2 / seg1) - GOLDEN_RATIO_INVERSE) < 1e-6
    assert abs((seg3 / seg2) - GOLDEN_RATIO_INVERSE) < 1e-6

    # 2. Test multi_gradient with golden ratio scaling
    out = multi_gradient("Test Hello", GRADIENT_PRESETS["electric"], golden_ratio_scale=True)
    assert "\033[0m" in out
    assert len(out) > len("Test Hello")

    # 3. Test multi_gradient without golden ratio scaling
    out_linear = multi_gradient("Test Hello", GRADIENT_PRESETS["electric"], golden_ratio_scale=False)
    assert "\033[0m" in out_linear

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


def test_golden_ratio_gradient_and_smoke_test() -> None:
    """Verify golden ratio constants, gradient generation, rendering, and smoke tests."""
    assert abs(GOLDEN_RATIO - 1.618033988749895) < 1e-9
    assert abs(PHI - GOLDEN_RATIO) < 1e-9
    assert abs(GOLDEN_RATIO_INVERSE - (1.0 / GOLDEN_RATIO)) < 1e-9

    all_colors = list(COLOR_PALETTE.values())
    expected_len = round(len(all_colors) * GOLDEN_RATIO)
    samples = generate_golden_ratio_gradient(all_colors)
    assert len(samples) == expected_len
    for rgb in samples:
        assert len(rgb) == 3
        assert all(0 <= ch <= 255 for ch in rgb)

    rendered = render_golden_ratio_gradient(all_colors)
    assert "\033[38;2;" in rendered
    assert "\033[0m" in rendered

    # Interpolate RGB helper check
    mid_rgb = interpolate_rgb("#000000", "#ffffff", 0.5)
    assert mid_rgb == (128, 128, 128)

    # Smoke test execution
    assert run_colors_smoke_test() is True
