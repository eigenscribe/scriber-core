# src/cli/__main__.py
"""
__main__.py

Package execution launcher for `python -m cli` or `python -m src.cli`.
"""

from __future__ import annotations

try:
    from .main import main
except (ImportError, ValueError):
    from cli.main import main

if __name__ == "__main__":
    main()
