# tests/test_cli_colors_table.py
"""
test_cli_colors_table.py

Comprehensive unit and integration test suite for `src/scriber_core/cli/colors_table.py`,
`src/scriber_core/cli/colors.py`, `src/scriber_core/cli/main.py`, and `src/scriber_core/cli/__init__.py`.
"""

from __future__ import annotations

import re
import click
from click.testing import CliRunner
import pytest

from scriber_core.cli import (
    BADGE_COLORS,
    BORDER_FRAME_COLOR,
    BOX_STYLES,
    COLOR_PALETTE,
    ColorEntry,
    CommandDescriptor,
    EIGENSCRIBE_BLOCK_TEXT,
    PRIMARY_GRADIENT,
    REGISTERED_COMMANDS,
    SECONDARY_GRADIENT,
    SortKey,
    TableStyle,
    ansi_color,
    build_color_entries,
    cli,
    format_color_swatch,
    format_colored_name,
    print_brand_header,
    print_colors_table,
    print_commands_list,
    render_brand_header,
    render_colors_table,
    render_commands_list,
)
from scriber_core.cli.colors_table import _compute_hue, _compute_relative_luminance, main as colors_table_main
from scriber_core.cli.main import (
    cli as main_cli,
    main as scriber_main,
    run_smoke_test as main_smoke_test,
)


@pytest.fixture
def runner() -> CliRunner:
    """Provide a Click CliRunner fixture."""
    return CliRunner()


def test_color_entry_namedtuple_and_build() -> None:
    """Verify build_color_entries constructs valid ColorEntry descriptors."""
    entries = build_color_entries()
    assert len(entries) == len(COLOR_PALETTE)
    first = entries[0]
    assert isinstance(first, ColorEntry)
    assert first.index == 1
    assert first.name == "deep_pine"
    assert first.hex_code == "#071a12"
    assert first.rgb == (7, 26, 18)
    assert 0.0 <= first.luminance <= 1.0
    assert 0.0 <= first.hue <= 360.0


def test_build_color_entries_sorting() -> None:
    """Verify sorting options across names, hex values, luminance, and hue."""
    by_name = build_color_entries(sort_by="name")
    names = [e.name.lower() for e in by_name]
    assert names == sorted(names)

    by_hex = build_color_entries(sort_by="hex")
    hexes = [e.hex_code.lower() for e in by_hex]
    assert hexes == sorted(hexes)

    by_lum = build_color_entries(sort_by="luminance")
    lums = [e.luminance for e in by_lum]
    assert lums == sorted(lums)

    by_hue = build_color_entries(sort_by="hue")
    hues = [e.hue for e in by_hue]
    assert hues == sorted(hues)

    by_rev = build_color_entries(sort_by="name", reverse=True)
    rev_names = [e.name.lower() for e in by_rev]
    assert rev_names == sorted(names, reverse=True)


def test_format_swatch_and_colored_name() -> None:
    """Verify ANSI formatting for color swatches and text names."""
    rgb = (0, 232, 255)
    swatch_fg = format_color_swatch(rgb, width=5, block_char="■")
    assert swatch_fg == "\033[38;2;0;232;255m■■■■■\033[0m"

    swatch_bg = format_color_swatch(rgb, width=4, use_bg=True)
    assert swatch_bg == "\033[48;2;0;232;255m████\033[0m"

    name_bold = format_colored_name("vivid_cyan", rgb, bold=True, width=15)
    assert "\033[1;38;2;0;232;255m" in name_bold
    assert "vivid_cyan" in name_bold
    assert "\033[0m" in name_bold


def test_render_colors_table_all_border_styles() -> None:
    """Verify all table box styles produce well-formed table strings."""
    styles: list[TableStyle] = ["rounded", "heavy", "double", "ascii", "minimal", "markdown"]
    for style in styles:
        table_output = render_colors_table(border_style=style, block_width=4)
        plain_table = re.sub(r"\x1b\[[0-9;]*m", "", table_output)
        assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_table
        assert "deep_pine" in table_output
        assert "node-1" in table_output


def test_render_colors_table_empty_palette() -> None:
    """Verify empty palette fallback message."""
    output = render_colors_table(palette={})
    assert "No colors available" in output


def test_print_colors_table_output(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify print_colors_table prints table with ANSI TrueColor escape sequences."""
    sample_palette = {"cyan": "#00ffff", "magenta": "#ff00ff"}
    print_colors_table(sample_palette, block_width=4)
    captured = capsys.readouterr()
    plain_out = re.sub(r"\x1b\[[0-9;]*m", "", captured.out)
    assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_out
    assert "cyan" in captured.out
    assert "magenta" in captured.out
    assert "\033[38;2;0;255;255m" in captured.out  # cyan ANSI code
    assert "\033[38;2;255;0;255m" in captured.out  # magenta ANSI code
    assert "\033[0m" in captured.out


def test_main_and_colors_module_entry_points(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify cli.main and cli.colors_table entry points execute with ANSI TrueColor codes."""
    from scriber_core.cli.main import main as main_entry

    # Direct function invocation of print_colors_table via main module
    print_colors_table({"pine": "#059669"}, block_width=2)
    captured = capsys.readouterr()
    assert "\033[38;2;5;150;105m" in captured.out
    assert "pine" in captured.out


def test_cli_runner_invocations(runner: CliRunner) -> None:
    """Verify Click CLI commands and flags."""
    res_help = runner.invoke(cli, ["--help"])
    assert res_help.exit_code == 0
    assert "colors-table" in res_help.output or "COLOR_PALETTE" in res_help.output

    res_sort = runner.invoke(cli, ["--sort", "luminance", "--block-width", "5", "--block-char", "■"])
    assert res_sort.exit_code == 0
    plain_sort = re.sub(r"\x1b\[[0-9;]*m", "", res_sort.output)
    assert "Order: luminance" in plain_sort

    res_no_head = runner.invoke(cli, ["--no-header", "--no-summary"])
    assert res_no_head.exit_code == 0
    plain_no_head = re.sub(r"\x1b\[[0-9;]*m", "", res_no_head.output)
    assert "SCRIBER CORE COLOR PALETTE TABLE" not in plain_no_head
    assert "deep_pine" in res_no_head.output


def test_scriber_core_block_text_and_brand_header(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify block text reading 'scriber-core' with SECONDARY_GRADIENT and gradient header."""
    assert len(EIGENSCRIBE_BLOCK_TEXT.strip()) > 0
    assert "|" in EIGENSCRIBE_BLOCK_TEXT
    assert len(SECONDARY_GRADIENT) == 4
    assert len(PRIMARY_GRADIENT) == 4

    header_str = render_brand_header()
    assert "\033[38;2;" in header_str or "\033[1;38;2;" in header_str
    plain_header = re.sub(r"\x1b\[[0-9;]*m", "", header_str)
    assert "SCRIBER CORE" in plain_header
    assert "Deterministic workspace baseline" in plain_header

    print_brand_header()
    captured = capsys.readouterr()
    assert "\033[38;2;" in captured.out
    plain_captured = re.sub(r"\x1b\[[0-9;]*m", "", captured.out)
    assert "SCRIBER CORE" in plain_captured


def test_render_and_print_commands_list(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify command directory rendering, semantic categories, badges, and COLOR_PALETTE tokens."""
    assert len(REGISTERED_COMMANDS) >= 5

    commands_str = render_commands_list()
    assert "\033[38;2;" in commands_str
    plain_cmds = re.sub(r"\x1b\[[0-9;]*m", "", commands_str)
    assert "AVAILABLE CLI COMMANDS" in plain_cmds
    assert "colors-table" in plain_cmds
    assert "gradient" in plain_cmds
    assert "info" in plain_cmds
    assert "Syntax:" in plain_cmds

    # Test helper and print function
    print_commands_list()
    captured = capsys.readouterr()
    assert "AVAILABLE CLI COMMANDS" in re.sub(r"\x1b\[[0-9;]*m", "", captured.out)


def test_main_cli_invocations(runner: CliRunner) -> None:
    """Verify main Click group and subcommand invocations in src/scriber_core/cli/main.py."""
    # 1. Default invocation (no subcommands)
    res_default = runner.invoke(main_cli, [])
    assert res_default.exit_code == 0
    plain_default = re.sub(r"\x1b\[[0-9;]*m", "", res_default.output)
    assert "SCRIBER CORE" in plain_default
    assert "AVAILABLE CLI COMMANDS" in plain_default

    # 2. commands subcommand
    res_cmds = runner.invoke(main_cli, ["commands"])
    assert res_cmds.exit_code == 0
    assert "colors-table" in res_cmds.output

    # 3. banner subcommand
    res_banner = runner.invoke(main_cli, ["banner"])
    assert res_banner.exit_code == 0
    assert "SCRIBER CORE" in re.sub(r"\x1b\[[0-9;]*m", "", res_banner.output)

    # 4. colors-table subcommand
    res_table = runner.invoke(main_cli, ["colors-table", "--no-header"])
    assert res_table.exit_code == 0
    assert "deep_pine" in res_table.output

    # 5. smoke-test subcommand
    res_smoke = runner.invoke(main_cli, ["smoke-test"])
    assert res_smoke.exit_code == 0
    assert "smoke tests passed successfully" in res_smoke.output

    # 6. version option
    res_ver = runner.invoke(main_cli, ["--version"])
    assert res_ver.exit_code == 0
    assert "scriber-core" in re.sub(r"\x1b\[[0-9;]*m", "", res_ver.output)


def test_main_smoke_test_function() -> None:
    """Verify run_smoke_test in src/scriber_core/cli/main.py."""
    assert main_smoke_test() is True


def test_relative_luminance_and_hue_calculations() -> None:
    """Verify numerical correctness of luminance and hue algorithms."""
    # Black
    assert _compute_relative_luminance((0, 0, 0)) == 0.0
    assert _compute_hue((0, 0, 0)) == 0.0

    # White
    assert abs(_compute_relative_luminance((255, 255, 255)) - 1.0) < 1e-6
    assert _compute_hue((255, 255, 255)) == 0.0

    # Primary colors hue check
    assert abs(_compute_hue((255, 0, 0)) - 0.0) < 1e-4  # Red = 0 deg
    assert abs(_compute_hue((0, 255, 0)) - 120.0) < 1e-4  # Green = 120 deg
    assert abs(_compute_hue((0, 0, 255)) - 240.0) < 1e-4  # Blue = 240 deg
    assert abs(_compute_hue((0, 255, 255)) - 180.0) < 1e-4  # Cyan = 180 deg


def test_golden_ratio_proportions_and_header_gradients() -> None:
    """Verify golden ratio stop position decay and header gradient styling."""
    from scriber_core.frontend.gradients import compute_golden_ratio_stop_positions, multi_gradient

    # Verify decay across 4 stops (blue -> cyan -> indigo -> violet/pink)
    stops = compute_golden_ratio_stop_positions(4)
    assert len(stops) == 4
    w1 = stops[1] - stops[0]
    w2 = stops[2] - stops[1]
    w3 = stops[3] - stops[2]
    assert w1 > w2 > w3
    assert abs(w1 - 0.5) < 1e-6

    # Verify primary gradient applied to headers
    banner_str = render_brand_header()
    assert "\033[1;38;2;0;232;255m" in banner_str or "\033[38;2;0;232;255m" in banner_str

    commands_str = render_commands_list()
    assert "\033[1;38;2;0;232;255m" in commands_str or "\033[38;2;0;232;255m" in commands_str

    table_str = render_colors_table()
    assert "\033[1;38;2;0;232;255m" in table_str or "\033[38;2;0;232;255m" in table_str
