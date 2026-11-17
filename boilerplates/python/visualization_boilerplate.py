# boilerplates/python/visualization_boilerplate.py
"""
visualization_boilerplate.py

Gold Standard visualization bootstrapping script for Matplotlib, Pyplot, Seaborn,
and Plotly graphics conforming to the Eigenscribe / Scriber Labs Design System.

Author: Eigenscribe & Scriber Labs
Date: November 2026
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from typing import Any, Final

try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    sns = None
    HAS_SEABORN = False

try:
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    go = None
    HAS_PLOTLY = False

from frontend.the_scriber_experience.plots.theme import (
    apply_cosmic_theme,
    apply_theme,
    create_eigenscribe_colormap,
    create_plotly_base_figure,
    get_eigenscribe_rcparams,
    plot_eigenscribe_heatmap,
    register_colormaps,
)

# -----------------------------------------------------------------------------------------------------------
# 0️⃣ / 🎭 Definitions, Constants & Types
# -----------------------------------------------------------------------------------------------------------

DEFAULT_SEED: Final[int] = 42

# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Public API — Visualization Helpers
# -----------------------------------------------------------------------------------------------------------


def bootstrap_figure(
    nrows: int = 1,
    ncols: int = 1,
    figsize: tuple[float, float] = (10.0, 6.0),
    cosmic: bool = False,
) -> tuple[plt.Figure, Any]:
    """
    Initialize a styled Eigenscribe Matplotlib figure and axis grid.

    Parameters
    ----------
    nrows : int, default=1
        Number of subplot rows.
    ncols : int, default=1
        Number of subplot columns.
    figsize : tuple[float, float], default=(10.0, 6.0)
        Figure dimensions in inches.
    cosmic : bool, default=False
        Whether to apply deep cosmic void background styling.

    Returns
    -------
    tuple[plt.Figure, Any]
        Configured figure and axis (or axes array).
    """
    if cosmic:
        apply_cosmic_theme()
    else:
        apply_theme()

    register_colormaps()
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    return fig, ax


# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke Tests
# -----------------------------------------------------------------------------------------------------------


def _run_smoke_test() -> None:
    """Validate figure bootstrapping and colormap registration."""
    print("💨 Running visualization_boilerplate.py smoke tests...")
    fig, ax = bootstrap_figure(1, 1, figsize=(6.0, 4.0))
    x = np.linspace(0.0, 10.0, 100)
    y = np.sin(x)
    ax.plot(x, y, label="$\sin(x)$", color="#00e8ff", lw=2.0)
    ax.set_title("Eigenscribe Visualization Bootstrap")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.legend()
    plt.close(fig)
    print("✅ visualization_boilerplate.py smoke tests passed.")


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry Point
# -----------------------------------------------------------------------------------------------------------


def main() -> None:
    """Execute module smoke tests."""
    _run_smoke_test()


if __name__ == "__main__":
    main()
