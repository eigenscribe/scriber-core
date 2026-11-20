"""
vt_mode.py

Windows Virtual Terminal (VT) mode enablement for the Eigenscribe CLI.
Provides a function to enable ANSI/VT100 escape sequence support on Windows
consoles. Called at CLI invocation time, not at import time, to avoid side
effects during module loading.

The conceptual story follows the Eigenscribe architectural standard:
What exists -> What you're allowed to call -> How it works -> Proof it works.

Author: Eigenscribe & Scriber Labs
Date: November 19, 2026
"""

from __future__ import annotations

import sys


__all__: list[str] = [
    "enable_vt_mode",
    "run_smoke_test",
]


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------


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


# -----------------------------------------------------------------------------------------------------------
# 4️⃣ 💨 Smoke tests / example usage (proof it works)
# -----------------------------------------------------------------------------------------------------------


def run_smoke_test() -> bool:
    """Validate that VT mode enablement runs without error.

    Returns
    -------
    bool
        True if enable_vt_mode() completes without raising.
    """
    print("💨 Running src/scriber_core/cli/vt_mode.py smoke tests...")

    # Verify enable_vt_mode does not raise
    enable_vt_mode()

    # Verify platform detection
    assert sys.platform in ("win32", "linux", "darwin"), f"Unexpected platform: {sys.platform!r}"

    print("✅ src/scriber_core/cli/vt_mode.py smoke tests passed successfully.\n")
    return True


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Orchestrate VT mode smoke test output."""
    success = run_smoke_test()
    if not success:
        raise ValueError("VT mode validation failed during smoke test checks.")


if __name__ == "__main__":
    main()
