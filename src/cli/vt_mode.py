# src/cli/vt_mode.py
"""
Windows Virtual Terminal (VT) mode enablement.

Provides a function to enable ANSI/VT100 escape sequence support on Windows
consoles. Called at CLI invocation time, not at import time, to avoid side
effects during module loading.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

import sys


def enable_vt_mode() -> None:
    """Enable ANSI/VT100 Virtual Terminal Processing on Windows consoles.

    Tries multiple strategies in order of preference:
    1. sys.stdout.reconfigure() (Python 3.7+)
    2. ctypes call to kernel32.SetConsoleMode
    3. colorama.just_fix_windows_console()

    On non-Windows platforms, this is a no-op.
    """
    if sys.platform != "win32":
        return

    # Strategy 1: reconfigure stdout encoding
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    # Strategy 2: ctypes to enable ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004)
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass

    # Strategy 3: colorama fallback
    try:
        import colorama

        if hasattr(colorama, "just_fix_windows_console"):
            colorama.just_fix_windows_console()
        else:
            colorama.init(wrap=False)
    except Exception:
        pass
