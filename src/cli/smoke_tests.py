# src/cli/smoke_tests.py
"""
Smoke tests for the Eigenscribe CLI suite.

Executes deterministic assertions to verify core functionality: block text,
header rendering, command list rendering, color formatting, messaging
integration, command registry, and Click end-to-end tests.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

import re

from .branding import (
    EIGENSCRIBE_BLOCK_TEXT,
    PRIMARY_GRADIENT,
    SECONDARY_GRADIENT,
    ansi_color,
    render_brand_header,
)
from .command_catalog import (
    REGISTERED_COMMANDS,
    render_commands_list,
)
from .messaging import (
    EIGENSCRIBE_PALETTE,
    render_message,
    render_rule,
    supports_256_color,
)


__all__: list[str] = [
    "run_smoke_test",
]


def run_smoke_test() -> bool:
    """Execute smoke test assertions for the Scriber Core CLI suite."""
    print("💨 Running src/cli smoke tests...")

    # 1. Block text existence and gradient definition
    assert len(EIGENSCRIBE_BLOCK_TEXT.strip()) > 0
    assert "EIGENSCRIBE" in EIGENSCRIBE_BLOCK_TEXT.replace("_", "E").replace("|", "") or "_____" in EIGENSCRIBE_BLOCK_TEXT
    assert len(SECONDARY_GRADIENT) == 4
    assert len(PRIMARY_GRADIENT) == 4

    # 2. Header rendering test
    header_output = render_brand_header()
    assert "\033[38;2;" in header_output or "\033[1;38;2;" in header_output
    plain_header = re.sub(r"\x1b\[[0-9;]*m", "", header_output)
    assert "SCRIBER CORE" in plain_header
    assert "Deterministic workspace baseline" in plain_header

    # 3. Command list rendering test
    commands_output = render_commands_list()
    assert "\033[38;2;" in commands_output
    plain_commands = re.sub(r"\x1b\[[0-9;]*m", "", commands_output)
    assert "AVAILABLE CLI COMMANDS" in plain_commands
    assert "colors-table" in plain_commands
    assert "gradient" in plain_commands
    assert "info" in plain_commands

    # 4. Color formatting helper test
    test_str = ansi_color("#00e8ff", "test_cyan", bold=True)
    assert "\033[1;38;2;0;232;255mtest_cyan\033[0m" == test_str

    # 5. Messaging integration assertions
    msg_rendered = render_message("Test Status", level="success", bold=True)
    assert "Test Status" in msg_rendered
    rule_rendered = render_rule("─", width=30)
    assert "─" * 30 in rule_rendered
    assert supports_256_color() in (True, False)
    assert len(EIGENSCRIBE_PALETTE) >= 40

    # 6. Verification of command registry
    assert len(REGISTERED_COMMANDS) >= 7
    names = {cmd.name for cmd in REGISTERED_COMMANDS}
    assert "colors-table" in names
    assert "gradient" in names
    assert "colors" in names
    assert "banner" in names
    assert "theme" in names
    assert "mermaid" in names
    assert "doctor" in names
    assert "info" in names

    # 7. Click CLI integration tests
    # Import here to avoid circular imports
    from .main import cli

    assert "info" in cli.commands
    assert "gradient" in cli.commands
    assert "colors" in cli.commands
    assert "banner" in cli.commands
    assert "theme" in cli.commands
    assert "mermaid" in cli.commands
    assert "doctor" in cli.commands
    assert "commands" in cli.commands
    assert "colors-table" in cli.commands

    from click.testing import CliRunner

    runner = CliRunner()
    res_help = runner.invoke(cli, ["--help"])
    assert res_help.exit_code == 0
    assert "Eigenscribe CLI" in res_help.output or "Scriber Core" in res_help.output

    res_info = runner.invoke(cli, ["info"])
    assert res_info.exit_code == 0

    res_grad = runner.invoke(cli, ["gradient", "Hello Eigenscribe", "--preset", "electric"])
    assert res_grad.exit_code == 0

    res_doc = runner.invoke(cli, ["doctor"])
    assert res_doc.exit_code == 0

    print("✅ src/cli smoke tests passed successfully.\n")
    return True
