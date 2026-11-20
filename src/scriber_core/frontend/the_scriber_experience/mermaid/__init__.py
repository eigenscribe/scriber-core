# src/scriber_core/frontend/the_scriber_experience/mermaid/__init__.py
"""
The Scriber Experience (TSE) Mermaid Subpackage.
Mermaid.js theme generator, custom styling classes, and HTML diagram preview rendering.
"""

from __future__ import annotations

from .theme import (
    EIGENSCRIBE_MERMAID_CLASSES,
    EIGENSCRIBE_MERMAID_THEME_VARIABLES,
    generate_mermaid_flowchart,
    get_mermaid_class_defs,
    get_mermaid_init_directive,
    get_mermaid_theme_variables,
    render_html_preview,
    save_mermaid_diagram,
    wrap_mermaid_diagram,
)

__all__: list[str] = [
    "EIGENSCRIBE_MERMAID_THEME_VARIABLES",
    "EIGENSCRIBE_MERMAID_CLASSES",
    "get_mermaid_theme_variables",
    "get_mermaid_init_directive",
    "get_mermaid_class_defs",
    "wrap_mermaid_diagram",
    "generate_mermaid_flowchart",
    "render_html_preview",
    "save_mermaid_diagram",
]
