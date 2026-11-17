# tests/test_cli_messaging.py
"""
test_cli_messaging.py

Comprehensive unit and integration test suite for Scriber Core messaging modules:
`src/frontend/messaging.py`, `src/cli/__init__.py`,
and `src/frontend/__init__.py`.
"""

from __future__ import annotations

import os
import re
import click
from click.testing import CliRunner
import pytest

from cli.messaging import (
    EIGENSCRIBE_PALETTE,
    PRIMARY_GRADIENT,
    SECONDARY_GRADIENT,
    STYLE_MAP,
    _FALLBACK_16,
    _ansi_256_raw,
    ansi_256,
    cli as messaging_cli,
    cli_banner,
    cli_echo,
    cli_error,
    cli_highlight,
    cli_info,
    cli_message,
    cli_rule,
    cli_success,
    cli_warning,
    main as messaging_main,
    render_banner,
    render_echo,
    render_message,
    render_rule,
    run_smoke_test,
    supports_256_color,
)
from cli import (
    EIGENSCRIBE_PALETTE as CLI_PALETTE,
    STYLE_MAP as CLI_STYLE_MAP,
    ansi_256 as cli_ansi_256,
    cli_banner as cli_pkg_banner,
    cli_echo as cli_pkg_echo,
    cli_error as cli_pkg_error,
    cli_highlight as cli_pkg_highlight,
    cli_info as cli_pkg_info,
    cli_message as cli_pkg_message,
    cli_rule as cli_pkg_rule,
    cli_success as cli_pkg_success,
    cli_warning as cli_pkg_warning,
    render_banner as cli_pkg_render_banner,
    render_echo as cli_pkg_render_echo,
    render_message as cli_pkg_render_message,
    render_rule as cli_pkg_render_rule,
    supports_256_color as cli_pkg_supports_256_color,
    run_messaging_smoke_test,
)
from cli.messaging import (
    EIGENSCRIBE_PALETTE as FRONTEND_PALETTE,
    STYLE_MAP as FRONTEND_STYLE_MAP,
    ansi_256 as fe_ansi_256,
    cli as fe_cli,
    cli_banner as fe_cli_banner,
    cli_echo as fe_cli_echo,
    cli_error as fe_cli_error,
    cli_highlight as fe_cli_highlight,
    cli_info as fe_cli_info,
    cli_message as fe_cli_message,
    cli_rule as fe_cli_rule,
    cli_success as fe_cli_success,
    cli_warning as fe_cli_warning,
    render_banner as fe_render_banner,
    render_echo as fe_render_echo,
    render_message as fe_render_message,
    render_rule as fe_render_rule,
    run_smoke_test as fe_run_smoke_test,
    supports_256_color as fe_supports_256_color,
)
from cli import (
    EIGENSCRIBE_PALETTE as ROOT_FE_PALETTE,
    STYLE_MAP as ROOT_FE_STYLE_MAP,
    ansi_256 as root_fe_ansi_256,
    cli_banner as root_fe_banner,
    cli_echo as root_fe_echo,
    cli_error as root_fe_error,
    cli_highlight as root_fe_highlight,
    cli_info as root_fe_info,
    cli_message as root_fe_message,
    cli_rule as root_fe_rule,
    cli_success as root_fe_success,
    cli_warning as root_fe_warning,
    render_banner as root_fe_render_banner,
    render_echo as root_fe_render_echo,
    render_message as root_fe_render_message,
    render_rule as root_fe_render_rule,
    supports_256_color as root_fe_supports_256_color,
)
from cli.main import cli as main_cli


@pytest.fixture
def runner() -> CliRunner:
    """Create a click CLI test runner."""
    return CliRunner()


# -----------------------------------------------------------------------------------------------------------
# 1. Palette and Constants Integrity Tests
# -----------------------------------------------------------------------------------------------------------


def test_palette_and_style_map_integrity() -> None:
    """Verify EIGENSCRIBE_PALETTE and STYLE_MAP contain all canonical tokens across modules."""
    assert len(EIGENSCRIBE_PALETTE) >= 45
    assert EIGENSCRIBE_PALETTE == CLI_PALETTE == FRONTEND_PALETTE == ROOT_FE_PALETTE
    assert STYLE_MAP == CLI_STYLE_MAP == FRONTEND_STYLE_MAP == ROOT_FE_STYLE_MAP

    # Key check for blues
    assert EIGENSCRIBE_PALETTE["eigen_cyan"] == 51
    assert EIGENSCRIBE_PALETTE["eigen_blue"] == 27
    assert EIGENSCRIBE_PALETTE["eigen_blue_bright"] == 33
    assert EIGENSCRIBE_PALETTE["eigen_luminous_cyan"] == 123
    assert EIGENSCRIBE_PALETTE["eigen_sky"] == 39

    # 10-node spectrum
    for i in range(10):
        key = f"eigen_node_{i}"
        assert key in EIGENSCRIBE_PALETTE
        assert isinstance(EIGENSCRIBE_PALETTE[key], int)

    # Sephirah legacy node aliases
    sephirah_keys = [
        "sephirah_keter",
        "sephirah_chokhmah",
        "sephirah_binah",
        "sephirah_chesed",
        "sephirah_gevurah",
        "sephirah_tiferet",
        "sephirah_netzach",
        "sephirah_hod",
        "sephirah_yesod",
        "sephirah_malkuth",
    ]
    for key in sephirah_keys:
        assert key in EIGENSCRIBE_PALETTE

    # 4-Color Vibrant Accent Set
    assert EIGENSCRIBE_PALETTE["eigen_accent_green"] == 83
    assert EIGENSCRIBE_PALETTE["eigen_accent_blue"] == 33
    assert EIGENSCRIBE_PALETTE["eigen_accent_magenta"] == 206
    assert EIGENSCRIBE_PALETTE["eigen_accent_amber"] == 215

    # Check STYLE_MAP references valid palette keys
    for level, palette_key in STYLE_MAP.items():
        assert palette_key in EIGENSCRIBE_PALETTE

    # Check _FALLBACK_16 mapping
    assert len(_FALLBACK_16) >= 8
    assert "info" in _FALLBACK_16
    assert "success" in _FALLBACK_16
    assert "warning" in _FALLBACK_16
    assert "error" in _FALLBACK_16


def test_gradient_constants() -> None:
    """Verify primary and secondary gradient constant definitions."""
    assert len(PRIMARY_GRADIENT) == 4
    assert len(SECONDARY_GRADIENT) == 4
    assert all(c.startswith("#") for c in PRIMARY_GRADIENT)
    assert all(c.startswith("#") for c in SECONDARY_GRADIENT)


# -----------------------------------------------------------------------------------------------------------
# 2. ANSI 256 & Color Detection Unit Tests
# -----------------------------------------------------------------------------------------------------------


def test_ansi_256_formatting() -> None:
    """Verify ansi_256 constructs correct ANSI escape codes and supports bold weight."""
    out_cyan = ansi_256("eigen_cyan", "Test Message", bold=False)
    assert out_cyan == "\033[38;5;51mTest Message\033[0m"

    out_cyan_bold = ansi_256("eigen_cyan", "Test Message", bold=True)
    assert out_cyan_bold == "\033[1;38;5;51mTest Message\033[0m"

    # Non-existent key should return plain text
    assert ansi_256("invalid_color_key", "Raw Text") == "Raw Text"


def test_ansi_256_raw() -> None:
    """Verify _ansi_256_raw formats arbitrary color index."""
    raw_plain = _ansi_256_raw(42, "Green Index", bold=False)
    assert raw_plain == "\033[38;5;42mGreen Index\033[0m"

    raw_bold = _ansi_256_raw(200, "Pink Index", bold=True)
    assert raw_bold == "\033[1;38;5;200mPink Index\033[0m"


def test_supports_256_color_detection(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify supports_256_color logic across environment variable combinations."""
    # Test TrueColor / 256color via COLORTERM
    monkeypatch.setenv("COLORTERM", "truecolor")
    assert supports_256_color() is True

    monkeypatch.setenv("COLORTERM", "256color")
    assert supports_256_color() is True

    # Test TERM env var
    monkeypatch.delenv("COLORTERM", raising=False)
    monkeypatch.setenv("TERM", "xterm-256color")
    assert supports_256_color() is True


# -----------------------------------------------------------------------------------------------------------
# 3. Message Rendering & Output Helpers
# -----------------------------------------------------------------------------------------------------------


def test_render_message_and_cli_message(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify render_message and cli_message formatting across all semantic levels."""
    levels = ["info", "success", "warning", "error", "highlight", "rule", "banner_title", "banner_sub"]
    for level in levels:
        rendered = render_message(f"Testing {level}", level=level, bold=True)
        assert f"Testing {level}" in rendered
        assert "\033[" in rendered

    # Test direct cli_message printing
    cli_message("Hello Info", level="info")
    captured = capsys.readouterr()
    assert "Hello Info" in captured.out


def test_render_echo_and_cli_echo(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify render_echo and cli_echo with direct palette keys and fallback levels."""
    # Direct color
    styled_color = render_echo("Dragon", color="eigen_purple", bold=True)
    assert "\033[1;38;5;129mDragon\033[0m" == styled_color

    # Level fallback
    styled_level = render_echo("Beast", level="success", bold=False)
    assert "Beast" in styled_level
    assert "38;5;41m" in styled_level

    # Plain fallback
    plain = render_echo("Plain text")
    assert plain == "Plain text"

    # cli_echo execution
    cli_echo("Testing cli_echo direct", color="eigen_pink_bright")
    captured = capsys.readouterr()
    assert "Testing cli_echo direct" in captured.out


def test_render_rule_and_cli_rule(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify render_rule and cli_rule construct valid divider lines."""
    rule_str = render_rule(char="═", width=42, level="rule")
    assert "═" * 42 in rule_str
    assert "38;5;27m" in rule_str

    cli_rule(char="─", width=50)
    captured = capsys.readouterr()
    assert "─" * 50 in captured.out


def test_render_banner_and_cli_banner(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify render_banner and cli_banner format TrueColor multi-stop headers."""
    banner_str = render_banner("MY APPLICATION", "Secondary subtitle line", width=50)
    plain = re.sub(r"\x1b\[[0-9;]*m", "", banner_str)
    assert "MY APPLICATION" in plain
    assert "Secondary subtitle line" in plain
    assert "─" in plain

    cli_banner("DIRECT BANNER", "Direct subtitle")
    captured = capsys.readouterr()
    assert "DIRECT BANNER" in re.sub(r"\x1b\[[0-9;]*m", "", captured.out)
    assert "Direct subtitle" in re.sub(r"\x1b\[[0-9;]*m", "", captured.out)


def test_semantic_helpers(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify cli_info, cli_success, cli_warning, cli_error, and cli_highlight."""
    cli_info("Informational message")
    out = capsys.readouterr().out
    assert "ℹ️" in out
    assert "Informational message" in out

    cli_success("Success notification")
    out = capsys.readouterr().out
    assert "✅" in out
    assert "Success notification" in out

    cli_warning("Warning alert")
    out = capsys.readouterr().out
    assert "⚠️" in out
    assert "Warning alert" in out

    cli_error("Critical error")
    out = capsys.readouterr().out
    assert "❌" in out
    assert "Critical error" in out

    cli_highlight("Special highlight")
    out = capsys.readouterr().out
    assert "✨" in out
    assert "Special highlight" in out


# -----------------------------------------------------------------------------------------------------------
# 4. Smoke Test Function Verification
# -----------------------------------------------------------------------------------------------------------


def test_all_smoke_tests() -> None:
    """Verify smoke test functions execute successfully and return True."""
    assert run_smoke_test() is True
    assert run_messaging_smoke_test() is True
    assert fe_run_smoke_test() is True


# -----------------------------------------------------------------------------------------------------------
# 5. Click CLI Integration Tests
# -----------------------------------------------------------------------------------------------------------


def test_messaging_cli_commands(runner: CliRunner) -> None:
    """Verify Click subcommands in src/cli/messaging.py."""
    # Banner command
    res_banner = runner.invoke(messaging_cli, ["banner", "MESSAGING BANNER", "-s", "Testing Banner"])
    assert res_banner.exit_code == 0
    assert "MESSAGING BANNER" in re.sub(r"\x1b\[[0-9;]*m", "", res_banner.output)

    # Info, success, warning, error, highlight
    assert runner.invoke(messaging_cli, ["info", "Info test"]).exit_code == 0
    assert runner.invoke(messaging_cli, ["success", "Success test"]).exit_code == 0
    assert runner.invoke(messaging_cli, ["warning", "Warning test"]).exit_code == 0
    assert runner.invoke(messaging_cli, ["error", "Error test"]).exit_code == 0
    assert runner.invoke(messaging_cli, ["highlight", "Highlight test"]).exit_code == 0

    # Palette command
    res_pal = runner.invoke(messaging_cli, ["palette"])
    assert res_pal.exit_code == 0
    assert "256-Color Palette Showcase" in res_pal.output

    # Smoke test command
    res_smoke = runner.invoke(messaging_cli, ["smoke-test"])
    assert res_smoke.exit_code == 0
    assert "smoke tests passed" in res_smoke.output


def test_main_cli_messaging_commands(runner: CliRunner) -> None:
    """Verify Click subcommands in src/cli/main.py (info, gradient, colors, message, rule)."""
    # Info command
    res_info = runner.invoke(main_cli, ["info"])
    assert res_info.exit_code == 0
    plain_info = re.sub(r"\x1b\[[0-9;]*m", "", res_info.output)
    assert "SCRIBER CORE ARCHITECTURAL OVERVIEW" in plain_info
    assert "4-Layer Design Token Stack" in plain_info

    # Gradient command
    res_grad = runner.invoke(main_cli, ["gradient", "Cyberpunk Gradient", "-p", "cyberpunk"])
    assert res_grad.exit_code == 0
    assert "Cyberpunk Gradient" in re.sub(r"\x1b\[[0-9;]*m", "", res_grad.output)

    res_list = runner.invoke(main_cli, ["gradient", "--list-presets"])
    assert res_list.exit_code == 0
    assert "AVAILABLE GRADIENT PRESETS" in res_list.output

    # Colors command
    res_colors = runner.invoke(main_cli, ["colors", "--spectrum"])
    assert res_colors.exit_code == 0
    assert "Signature TSE Palette" in res_colors.output
    assert "Vibrant 10-Node EIGEN Spectrum" in res_colors.output

    # Message command
    res_msg = runner.invoke(main_cli, ["message", "Custom Info", "--level", "info"])
    assert res_msg.exit_code == 0
    assert "ℹ️" in res_msg.output
    assert "Custom Info" in res_msg.output

    # Rule command
    res_rule = runner.invoke(main_cli, ["rule", "-c", "═", "-w", "40"])
    assert res_rule.exit_code == 0
    assert "═" * 40 in res_rule.output
