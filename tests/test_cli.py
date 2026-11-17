# tests/test_cli.py
"""
test_cli.py

Automated tests for the Eigenscribe CLI baseline suite (`eigenscribe`).
Verifies command invocation, arguments, styling output, diagnostics, and exit codes.
"""

from __future__ import annotations

import re
import click
from click.testing import CliRunner
import pytest

from cli import (
    COLOR_PALETTE,
    build_color_entries,
    format_color_swatch,
    format_colored_name,
    print_colors_table,
    render_colors_table,
    run_smoke_test,
)
from cli.colors_table import cli as colors_table_cli
from frontend.the_scriber_experience.cli.main import cli_group


@pytest.fixture
def runner() -> CliRunner:
    """Create a click CLI test runner."""
    return CliRunner()


def test_cli_help(runner: CliRunner) -> None:
    """Verify eigenscribe --help prints signature banners and subcommands."""
    result = runner.invoke(cli_group, ["--help"])
    assert result.exit_code == 0
    assert "Eigenscribe CLI" in result.output
    assert "info" in result.output
    assert "gradient" in result.output
    assert "colors" in result.output
    assert "banner" in result.output
    assert "theme" in result.output
    assert "mermaid" in result.output
    assert "doctor" in result.output


def test_cli_version(runner: CliRunner) -> None:
    """Verify eigenscribe --version outputs version badge."""
    result = runner.invoke(cli_group, ["--version"])
    assert result.exit_code == 0
    assert "eigenscribe v" in result.output


def test_cli_no_args_brand_header(runner: CliRunner) -> None:
    """Verify eigenscribe invoked with no args renders banner header."""
    result = runner.invoke(cli_group, [])
    assert result.exit_code == 0
    assert "SCRIBER CORE" in result.output or "Eigenscribe CLI" in result.output


def test_cli_info_command(runner: CliRunner) -> None:
    """Verify eigenscribe info outputs architecture and design token stack."""
    result = runner.invoke(cli_group, ["info"])
    assert result.exit_code == 0
    assert "SCRIBER CORE ARCHITECTURAL OVERVIEW" in result.output
    assert "4-Layer Design Token Stack" in result.output


def test_cli_gradient_command(runner: CliRunner) -> None:
    """Verify eigenscribe gradient generates multi-stop gradient outputs."""
    res_default = runner.invoke(cli_group, ["gradient", "Testing Eigenscribe", "-p", "cyberpunk"])
    assert res_default.exit_code == 0
    assert "Testing Eigenscribe" in res_default.output

    res_stops = runner.invoke(cli_group, ["gradient", "Custom Stops", "-s", "#00ffff", "-s", "#ff00c3"])
    assert res_stops.exit_code == 0
    assert "Custom Stops" in res_stops.output

    res_list = runner.invoke(cli_group, ["gradient", "--list-presets"])
    assert res_list.exit_code == 0
    assert "GRADIENT PRESETS" in res_list.output
    assert "electric" in res_list.output
    assert "eigenscribe" in res_list.output
    assert "#00e8ff" in res_list.output
    assert "#008eff" in res_list.output
    assert "#6f78fa" in res_list.output
    assert "#5e17eb" in res_list.output


def test_cli_colors_command(runner: CliRunner) -> None:
    """Verify eigenscribe colors displays palettes, status roles, and 256 index."""
    result = runner.invoke(cli_group, ["colors", "--all-256", "--spectrum"])
    assert result.exit_code == 0
    assert "Signature TSE Palette" in result.output
    assert "Semantic Status Roles" in result.output
    assert "Vibrant 10-Node Spectrum" in result.output


def test_cli_banner_command(runner: CliRunner) -> None:
    """Verify eigenscribe banner creates formatted rule-bordered banners."""
    result = runner.invoke(cli_group, ["banner", "MY EXPERIMENT", "--subtitle", "Trial Run 01"])
    assert result.exit_code == 0
    assert "MY EXPERIMENT" in result.output
    assert "Trial Run 01" in result.output


def test_cli_theme_command(runner: CliRunner) -> None:
    """Verify eigenscribe theme exports summary, rcParams, and CSS variables."""
    res_summary = runner.invoke(cli_group, ["theme", "-f", "summary"])
    assert res_summary.exit_code == 0
    assert "PLOTTING & GRAPHICS THEME" in res_summary.output

    res_rc = runner.invoke(cli_group, ["theme", "-f", "rcparams"])
    assert res_rc.exit_code == 0
    assert "rcParams" in res_rc.output

    res_css = runner.invoke(cli_group, ["theme", "-f", "css"])
    assert res_css.exit_code == 0
    assert ":root {" in res_css.output
    assert "--color-" in res_css.output


def test_cli_mermaid_command(runner: CliRunner) -> None:
    """Verify eigenscribe mermaid generates diagrams and directives."""
    res_sample = runner.invoke(cli_group, ["mermaid", "--sample"])
    assert res_sample.exit_code == 0
    assert "flowchart TD" in res_sample.output

    res_init = runner.invoke(cli_group, ["mermaid", "--init"])
    assert res_init.exit_code == 0
    assert "%%{init:" in res_init.output


def test_cli_doctor_command(runner: CliRunner) -> None:
    """Verify eigenscribe doctor performs and passes all diagnostics."""
    result = runner.invoke(cli_group, ["doctor"])
    assert result.exit_code == 0
    assert "EIGENSCRIBE DOCTOR" in result.output
    assert "[PASS]" in result.output
    assert "checks passed successfully" in result.output


def test_cli_colors_table_direct_command(runner: CliRunner) -> None:
    """Verify colors_table CLI prints table with colored swatches and names."""
    res = runner.invoke(colors_table_cli, [])
    assert res.exit_code == 0
    plain_output = re.sub(r"\x1b\[[0-9;]*m", "", res.output)
    assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_output
    assert "\033[1;38;2;" in res.output or "\033[38;2;" in res.output
    assert "deep_pine" in res.output
    assert "pure_cyan" in res.output
    assert "#00ffff" in res.output

    # Test sorting and formatting options
    res_sorted = runner.invoke(colors_table_cli, ["--sort", "name", "--reverse"])
    assert res_sorted.exit_code == 0
    assert "warning_amber" in res_sorted.output

    # Test style options
    res_ascii = runner.invoke(colors_table_cli, ["--style", "ascii", "--no-header"])
    assert res_ascii.exit_code == 0
    assert "|" in res_ascii.output

    # Test smoke-test flag
    res_smoke = runner.invoke(colors_table_cli, ["--smoke-test"])
    assert res_smoke.exit_code == 0
    assert "smoke tests passed" in res_smoke.output


def test_cli_colors_table_eigenscribe_integration(runner: CliRunner) -> None:
    """Verify eigenscribe colors --table displays the full COLOR_PALETTE table."""
    result = runner.invoke(cli_group, ["colors", "--table"])
    assert result.exit_code == 0
    plain_output = re.sub(r"\x1b\[[0-9;]*m", "", result.output)
    assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_output
    assert "Rendered" in result.output


def test_colors_table_rendering_helpers() -> None:
    """Verify build_color_entries, swatch formatting, and table render functions."""
    entries = build_color_entries()
    assert len(entries) == len(COLOR_PALETTE)
    assert entries[0].index == 1

    swatch = format_color_swatch((0, 255, 255), width=6)
    assert "\033[38;2;0;255;255m██████\033[0m" == swatch

    colored_name = format_colored_name("pure_cyan", (0, 255, 255))
    assert "\033[1;38;2;0;255;255mpure_cyan\033[0m" == colored_name

    rendered = render_colors_table()
    plain_rendered = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
    assert "SCRIBER CORE COLOR PALETTE TABLE" in plain_rendered
    assert run_smoke_test() is True
