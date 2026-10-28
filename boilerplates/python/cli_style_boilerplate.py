"""
cli_style_boilerplate.py

Boilerplate CLI styling module for Scriber Core projects.
Provides a ready-to-use Eigenscribe 256-color terminal palette with automatic
fallback to 16-color mode, plus semantic message helpers (info, success, warning,
error, highlight) and decorative elements (banners, rules).

Inspired by the "EigenBeast" game CLI pattern — uses color-coded semantic levels
to make terminal output visually engaging while remaining accessible.

Usage
-----
>>> from cli_style import cli_info, cli_success, cli_banner, ansi_256
>>> cli_banner("MY APP", "A colorful CLI tool")
>>> cli_info("Loading data...")
>>> cli_success("Done!")

Author: Eigenscribe
Date: October 2026
"""

from __future__ import annotations

import os
import sys
from typing import Final

# Force UTF-8 stdout on Windows to support emoji and Unicode chars
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
elif sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# Try to import click; fall back to raw print if not available
try:
    import click
    _HAS_CLICK = True
except ImportError:
    _HAS_CLICK = False

__all__: list[str] = [
    # Core messaging
    "cli_message",
    "cli_echo",
    "cli_rule",
    "cli_banner",
    # Semantic levels
    "cli_info",
    "cli_success",
    "cli_warning",
    "cli_error",
    "cli_highlight",
    # Color palette access
    "EIGENSCRIBE_PALETTE",
    "ansi_256",
    "supports_256_color",
]

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types — Eigenscribe 256-Color Palette
# -----------------------------------------------------------------------------------------------------------

# Eigenscribe brand palette mapped to ANSI 256-color indices
# Blues (primary), Purples (secondary), Pinks (accents), Greens (success), Oranges (warnings)
EIGENSCRIBE_PALETTE: Final[dict[str, int]] = {
    # --- Blues (Primary domain) ---
    "eigen_blue_dark": 25,       # Deep navy blue
    "eigen_blue": 27,            # Core Eigenscribe blue
    "eigen_blue_bright": 33,     # Bright electric blue
    "eigen_cyan": 51,            # Electric cyan for info
    "eigen_cyan_light": 81,      # Light cyan accent

    # --- Purples (Secondary domain) ---
    "eigen_purple_dark": 55,     # Deep violet
    "eigen_purple": 129,         # Core Eigenscribe purple
    "eigen_purple_bright": 141,  # Bright magenta-purple
    "eigen_magenta": 163,        # Magenta for highlights

    # --- Pinks (Accent domain) ---
    "eigen_pink": 212,           # Soft pink accent
    "eigen_pink_bright": 199,    # Bright pink for emphasis

    # --- Greens (Success domain) ---
    "eigen_green_dark": 22,      # Deep forest green
    "eigen_green": 35,           # Core green
    "eigen_green_bright": 41,    # Bright success green
    "eigen_mint": 121,           # Mint green accent

    # --- Oranges/Ambers (Warning domain) ---
    "eigen_amber": 214,          # Amber warning
    "eigen_orange": 208,         # Core orange
    "eigen_orange_bright": 202,  # Bright orange accent

    # --- Reds (Error domain) ---
    "eigen_red": 160,            # Soft red for errors
    "eigen_red_bright": 196,     # Bright red for critical errors

    # --- Neutrals ---
    "eigen_white": 189,          # Soft white
    "eigen_gray": 145,           # Medium gray
    "eigen_gray_dark": 102,      # Dark gray for dimmed text
}

# Semantic style map: maps message levels to palette keys
STYLE_MAP: Final[dict[str, str]] = {
    "info": "eigen_cyan",
    "success": "eigen_green_bright",
    "warning": "eigen_amber",
    "error": "eigen_red_bright",
    "highlight": "eigen_pink_bright",
    "banner_title": "eigen_blue_bright",
    "banner_sub": "eigen_purple",
    "rule": "eigen_blue",
}

# Fallback 16-color map for terminals that don't support 256 colors
_FALLBACK_16: Final[dict[str, str]] = {
    "info": "bright_cyan",
    "success": "bright_green",
    "warning": "bright_yellow",
    "error": "bright_red",
    "highlight": "bright_magenta",
    "banner_title": "bright_blue",
    "banner_sub": "bright_magenta",
    "rule": "bright_blue",
}


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API — Color Detection & ANSI Helpers
# -----------------------------------------------------------------------------------------------------------


def supports_256_color() -> bool:
    """
    Detect whether the current terminal supports 256-color output.

    Returns
    -------
    bool
        True if the terminal appears to support 256 colors.
    """
    colorterm = os.environ.get("COLORTERM", "")
    if "256color" in colorterm:
        return True

    # Windows 10+ with modern terminals (Windows Terminal, Conhost with VT)
    if sys.platform == "win32":
        return True

    # Fallback: check TERM env var
    term = os.environ.get("TERM", "")
    return "256color" in term


def ansi_256(color_name: str, text: str, bold: bool = False) -> str:
    """
    Wrap text with ANSI 256-color escape codes using the Eigenscribe palette.

    Parameters
    ----------
    color_name : str
        Key from EIGENSCRIBE_PALETTE (e.g., "eigen_blue", "eigen_purple").
    text : str
        The text to colorize.
    bold : bool, default=False
        Whether to apply bold weight.

    Returns
    -------
    str
        The ANSI-escaped string ready for terminal output.

    Examples
    --------
    >>> print(ansi_256("eigen_blue", "Hello, world!", bold=True))
    """
    color_index = EIGENSCRIBE_PALETTE.get(color_name)
    if color_index is None:
        return text

    bold_code = "1;" if bold else ""
    return f"\033[{bold_code}38;5;{color_index}m{text}\033[0m"


def _ansi_256_raw(fg_index: int, text: str, bold: bool = False) -> str:
    """
    Apply a raw 256-color index directly (for dynamic color generation).

    Parameters
    ----------
    fg_index : int
        ANSI 256-color index (0-255).
    text : str
        The text to colorize.
    bold : bool, default=False
        Whether to apply bold weight.

    Returns
    -------
    str
        The ANSI-escaped string.
    """
    bold_code = "1;" if bold else ""
    return f"\033[{bold_code}38;5;{fg_index}m{text}\033[0m"


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API — Core Messaging
# -----------------------------------------------------------------------------------------------------------


def _echo(text: str) -> None:
    """Print text using click.echo if available, otherwise fall back to print."""
    if _HAS_CLICK:
        click.echo(text, color=True)
    else:
        print(text)


def _secho(text: str, fg: str | None = None, bold: bool = False) -> None:
    """Print styled text using click.secho if available, otherwise fall back to print."""
    if _HAS_CLICK:
        click.secho(text, fg=fg, bold=bold)
    else:
        print(text)


def cli_message(msg: str, level: str = "info", bold: bool = False) -> None:
    """
    Print a styled message using the Eigenscribe semantic color palette.

    Automatically detects 256-color support and falls back to 16-color mode
    when the terminal does not support extended colors.

    Parameters
    ----------
    msg : str
        Message content to display.
    level : str, default="info"
        Semantic level key from STYLE_MAP.
    bold : bool, default=False
        Whether to format the text in bold weight.
    """
    if supports_256_color():
        color_key = STYLE_MAP.get(level, "eigen_cyan")
        styled = ansi_256(color_key, msg, bold=bold)
        _echo(styled)
    else:
        fg = _FALLBACK_16.get(level, "bright_cyan")
        _secho(msg, fg=fg, bold=bold)


def cli_echo(
    msg: str,
    color: str | None = None,
    bold: bool = False,
    level: str | None = None,
) -> None:
    """
    Print arbitrary text with a specific Eigenscribe palette color.

    Parameters
    ----------
    msg : str
        Message content to display.
    color : str, optional
        Direct palette key (e.g., "eigen_blue", "eigen_pink").
        If provided, takes precedence over `level`.
    bold : bool, default=False
        Whether to apply bold weight.
    level : str, optional
        Fallback semantic level if `color` is not provided.

    Examples
    --------
    >>> cli_echo("My name is ", color="eigen_white")
    >>> cli_echo("EigenBeast", color="eigen_purple", bold=True)
    """
    if color is not None:
        if supports_256_color():
            styled = ansi_256(color, msg, bold=bold)
            _echo(styled)
        else:
            _secho(msg, bold=bold)
    elif level is not None:
        cli_message(msg, level=level, bold=bold)
    else:
        _echo(msg)


def cli_rule(char: str = "─", width: int = 60, level: str = "rule") -> None:
    """
    Print a horizontal rule line with semantic coloring.

    Parameters
    ----------
    char : str, default="─"
        Character to repeat for the rule line.
    width : int, default=60
        Number of characters wide.
    level : str, default="rule"
        Semantic color level.
    """
    line = char * width
    cli_message(line, level=level)


def cli_banner(title: str, subtitle: str | None = None) -> None:
    """
    Print a styled banner header with Eigenscribe brand colors.

    Parameters
    ----------
    title : str
        Main banner title.
    subtitle : str, optional
        Optional secondary subtitle line.

    Examples
    --------
    >>> cli_banner("EIGENBEAST BATTLE", "The Non-Copyright Generic Beast Game")
    """
    _echo("")
    cli_echo(title, color="eigen_blue_bright", bold=True)

    if subtitle:
        cli_echo(subtitle, color="eigen_purple", bold=False)

    cli_rule(level="rule")
    _echo("")


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API — Semantic Message Functions
# -----------------------------------------------------------------------------------------------------------


def cli_info(msg: str) -> None:
    """
    Print an informational prompt (Electric Cyan).

    Parameters
    ----------
    msg : str
        Informational message string.
    """
    cli_message(f"ℹ️  {msg}", level="info")


def cli_success(msg: str) -> None:
    """
    Print a success confirmation (Bright Green).

    Parameters
    ----------
    msg : str
        Success message string.
    """
    cli_message(f"✅ {msg}", level="success", bold=True)


def cli_warning(msg: str) -> None:
    """
    Print a warning notification (Amber).

    Parameters
    ----------
    msg : str
        Warning message string.
    """
    cli_message(f"⚠️  {msg}", level="warning")


def cli_error(msg: str) -> None:
    """
    Print an error alert (Bright Red).

    Parameters
    ----------
    msg : str
        Error message string.
    """
    cli_message(f"❌ {msg}", level="error", bold=True)


def cli_highlight(msg: str) -> None:
    """
    Print an emphasized highlight message (Bright Pink).

    Parameters
    ----------
    msg : str
        Highlight message string.
    """
    cli_message(f"✨ {msg}", level="highlight", bold=True)


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Quick sanity check for CLI style functions and 256-color palette."""
    _echo("")
    cli_banner("SCRIBER CORE CLI STYLE TEST", "256-Color Palette Verification")

    # Semantic messages
    cli_info("Info message — Electric Cyan")
    cli_success("Success message — Bright Green")
    cli_warning("Warning message — Amber")
    cli_error("Error message — Bright Red")
    cli_highlight("Highlight message — Bright Pink")

    # Palette showcase
    cli_rule()
    cli_echo("🎨 Eigenscribe 256-Color Palette Showcase:", color="eigen_white", bold=True)
    cli_rule()

    if supports_256_color():
        groups = {
            "🔵 Blues": ["eigen_blue_dark", "eigen_blue", "eigen_blue_bright",
                         "eigen_cyan", "eigen_cyan_light"],
            "🟣 Purples": ["eigen_purple_dark", "eigen_purple",
                           "eigen_purple_bright", "eigen_magenta"],
            "🩷 Pinks": ["eigen_pink", "eigen_pink_bright"],
            "🟢 Greens": ["eigen_green_dark", "eigen_green",
                          "eigen_green_bright", "eigen_mint"],
            "🟠 Oranges": ["eigen_amber", "eigen_orange", "eigen_orange_bright"],
            "🔴 Reds": ["eigen_red", "eigen_red_bright"],
            "⚪ Neutrals": ["eigen_white", "eigen_gray", "eigen_gray_dark"],
        }
        for label, colors in groups.items():
            parts = [ansi_256(c, c) for c in colors]
            _echo(f"  {label}: {' '.join(parts)}")
    else:
        _echo("  (256-color mode not available — using 16-color fallback)")

    cli_rule()

    # Example: EigenBeast-style colored output
    _echo("")
    cli_echo("🐉 Example — EigenBeast-style output:", color="eigen_purple", bold=True)
    cli_echo("  Your beast is called ", color="eigen_white")
    cli_echo("Thunderfrost", color="eigen_blue", bold=True)
    cli_echo(". It is a ", color="eigen_white")
    cli_echo("Water", color="eigen_cyan", bold=True)
    cli_echo(" beast with a special move of ", color="eigen_white")
    cli_echo("Glacial Surge", color="eigen_pink_bright", bold=True)
    cli_echo(".", color="eigen_white")

    cli_rule()
    cli_success("Style smoke test passed.")
    _echo("")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Entry point for standalone execution."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
