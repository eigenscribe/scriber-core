# src/cli/colors.py
"""
colors.py

CLI tool for rendering the COLOR_PALETTE table with TrueColor blocks and names.
Provides direct command-line execution and integration with the Eigenscribe CLI suite.

Author: Eigenscribe & Scriber Labs
Date: November 17, 2026
"""

from __future__ import annotations

import sys
from typing import Final

# Force UTF-8 stdout and enable ANSI TrueColor / Virtual Terminal Processing on Windows
def _enable_windows_vt_mode() -> None:
    """Enable ANSI/VT100 Virtual Terminal Processing on Windows consoles."""
    if sys.platform != "win32":
        return
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    try:
        import os

        os.system("")
    except Exception:
        pass
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass
    try:
        import colorama

        if hasattr(colorama, "just_fix_windows_console"):
            colorama.just_fix_windows_console()
        else:
            colorama.init(wrap=False)
    except Exception:
        pass


_enable_windows_vt_mode()

try:
    from .colors_table import (
        BOX_STYLES,
        DEFAULT_BLOCK_CHAR,
        DEFAULT_BLOCK_WIDTH,
        DEFAULT_BORDER_STYLE,
        ColorEntry,
        SortKey,
        TableStyle,
        build_color_entries,
        cli,
        format_color_swatch,
        format_colored_name,
        main,
        print_colors_table,
        render_colors_table,
        run_smoke_test,
    )
except (ImportError, ValueError):
    from cli.colors_table import (
        BOX_STYLES,
        DEFAULT_BLOCK_CHAR,
        DEFAULT_BLOCK_WIDTH,
        DEFAULT_BORDER_STYLE,
        ColorEntry,
        SortKey,
        TableStyle,
        build_color_entries,
        cli,
        format_color_swatch,
        format_colored_name,
        main,
        print_colors_table,
        render_colors_table,
        run_smoke_test,
    )

__all__: list[str] = [
    "cli",
    "main",
    "print_colors_table",
    "render_colors_table",
    "build_color_entries",
    "format_color_swatch",
    "format_colored_name",
    "run_smoke_test",
    "ColorEntry",
    "SortKey",
    "TableStyle",
    "BOX_STYLES",
    "DEFAULT_BLOCK_CHAR",
    "DEFAULT_BLOCK_WIDTH",
    "DEFAULT_BORDER_STYLE",
]

if __name__ == "__main__":
    main()
