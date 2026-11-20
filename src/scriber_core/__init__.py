# src/scriber_core/__init__.py
"""
scriber_core

Single top-level import namespace for the Scriber Labs & Eigenscribe workspace
baseline. The design-token / gradient frontend and the CLI suite are bundled as
subpackages (``scriber_core.frontend`` and ``scriber_core.cli``) under one package
root, so the distribution no longer installs generic top-level ``frontend`` /
``cli`` packages that could collide with other projects.

Author: Eigenscribe & Scriber Labs
Date: November 20, 2026
"""

from __future__ import annotations

from typing import Final

from . import frontend
from . import cli

__version__: Final[str] = "1.0.0"

__all__: list[str] = [
    "__version__",
    "frontend",
    "cli",
]
