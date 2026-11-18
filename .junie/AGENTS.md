# 🔬 Scriber Core — Repo-Specific Agent Overlay

> **Two-layer design:** This file supplements the universal Eigenscribe workspace guidelines (provided in the system prompt). It only contains repo-specific overrides, references, and constraints for `scriber-core`. For all general Python engineering, CSS design system, tooling, and COOP standards, consult the system prompt guidelines.

---

## 📌 Repository Identity

**Package:** `scriber-core` (v1.0.0)  
**Purpose:** Canonical workspace baseline for Eigenscribe Inc. and Scriber Labs, providing deterministic CLI styling tools, TrueColor gradient engines, design tokens, visualization themes, and the Scriber Experience (TSE) subsystem. Distributed via Git submodules, template cloning, or installable Python packaging.

**Packages:** Two installable packages under `src/`:
- **`src/frontend`** — Color palette (`COLOR_PALETTE`), gradient engine (`GRADIENT_PRESETS`), TSE styling subsystems (semantic roles, plots, Mermaid themes).
- **`src/cli`** — CLI suite with TrueColor gradient banners, palette table renderer, semantic messaging, and command catalog.

**Key Files:**
| File | Purpose |
| :--- | :--- |
| [`README.md`](README.md) | Master onboarding index, CLI usage, color standards, and cross-project distribution guide. |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history following Keep a Changelog 1.0.0. |
| [`TODO.md`](TODO.md) | Current task backlog, deferred work, and implementation roadmap. |
| [`pyproject.toml`](pyproject.toml) | PEP 621 metadata, `hatchling` build backend, `uv` tooling config, dependencies, and CLI entry points. |

---

## 📁 Workspace Reference Files

All paths are relative to the project root. Agents must consult these before any code generation.

| Directory | File | Purpose & Contents |
| :--- | :--- | :--- |
| `house-rules` | `house-rules/python-rules.md` | Core rules for Python development: mathematical typography, modern RNG, typing, package hygiene, docstrings, and script flow. |
| `house-rules` | `house-rules/css-rules.md` | The Scriber Experience design system: 4-layer token hierarchy, glassmorphism baseline, ADHD semantic color coding, and golden ratio spacing. |
| `docs` | `docs/workspace-setup-guide.md` | Canonical workspace distribution, packaging, Diátaxis Sphinx docs, testing, and PyPI release guide. |
| `docs/COOP_blog` | `docs/COOP_blog/Python packages_ the COOP gold standard · The COOP Blog.html` | Foundational CERFACS COOP software engineering standard on Python packaging, testing, and continuous integration. |
| `docs/COOP_blog` | `docs/COOP_blog/Packaging guide · The COOP Blog.html` | Step-by-step COOP packaging, sdist/wheel distribution, and PyPI release governance guide. |
| `docs/COOP_blog` | `docs/COOP_blog/The COOP Click Command line interfaces · The COOP Blog.html` | Click-based CLI design, thin-wrapper command architecture, context routing, and CliRunner testing. |
| `docs/COOP_blog` | `docs/COOP_blog/The Coop Cactus branching model · The COOP Blog.html` | Single-trunk Cactus branching model, release stabilization branches, hotfixes, and annotated tag governance. |
| `docs/COOP_blog` | `docs/COOP_blog/Using the json-SCHEMA standard for scientific applications_ · The COOP Blog.html` | JSON Schema validation, fail-fast boundary enforcement, and parameter self-documentation for scientific input decks. |
| `src/frontend` | `src/frontend/the_scriber_experience/style/gradient_presets.py` | ANSI TrueColor multi-stop linear RGB gradient engine and color-stop presets. |
| `src/frontend` | `src/frontend/colors.py` | ANSI 256-color terminal palette, semantic level messaging, and CLI styling helpers. |
| `boilerplates` | `boilerplates/python/gold-standard.py` | Gold standard reference script template implementing mathematical simulation, explicit type annotations, shape assertions, deterministic RNG, and smoke testing. |
| `src/frontend` | `src/frontend/the_scriber_experience/plots/theme.py` | Generalizable visualization bootstrapping script for Matplotlib, Pyplot, and Seaborn with high-contrast curves, deep cosmic void palettes, and 6-style heatmaps. |
| `boilerplates` | `boilerplates/css/tse-boilerplate.css` | Gold standard reference stylesheet implementing the full 4-layer taxonomy, CSS tokens, cosmic radial gradients, Sephirah labels, glassmorphism components, and responsive layouts. |
| `boilerplates` | `boilerplates/notebooks/visuals-boilerplate.ipynb` | Gold standard reference notebook template for scientific visualization, NetworkX graph topologies, dashboards, and design token / colormap palettes. |
| `.junie/skills` | `.junie/skills/cosmic-visual-styling/SKILL.md` | Workspace skill for applying the Sephirah / cosmic visual themes, color tokens, and glassmorphic UI components. |

---

## 🔧 Repo-Specific Overrides & Constraints

### Package Structure
- Two packages: `src/frontend` and `src/cli`. Both must maintain explicit `__all__` in their `__init__.py`.
- Runtime version is exported in `src/__init__.py` as `__version__: Final[str] = "1.0.0"`.
- CLI entry point: `eigenscribe = "cli.main:main"` in `pyproject.toml` under `[project.scripts]`.
- CLI is also runnable via `python -m cli` (see `src/cli/__main__.py`).

### Color Palette Constraint
- **Single source of truth:** `COLOR_PALETTE` in `src/frontend/colors.py` is the canonical dictionary for all named color variables across the repository.
- All color variables must reference valid key names from `COLOR_PALETTE` or be defined as canonical 6-digit hex (`#rrggbb`).
- Never hardcode raw or inconsistent RGB values in downstream modules without a canonical hex reference.
- Use `hex_to_rgb()` from `src/frontend/colors.py` for deterministic hex-to-RGB conversion for ANSI escapes.

### Gradient Engine
- Multi-stop gradients in `src/frontend/gradients.py` scale keyframe segments by the Golden Ratio ($\phi \approx 1.618$).
- Presets are defined in `GRADIENT_PRESETS` and should be extended rather than duplicated.

### Test Structure
- Unit tests: `tests/unit/test_*.py` (isolated module tests).
- Functional tests: `tests/func/test_*.py` (CLI end-to-end workflows and integration scenarios).
- Shared fixtures: `tests/conftest.py`.
- Target **70%+ coverage** on `src/frontend` and `src/cli`.

### Documentation (When Applicable)
- Sphinx + Read the Docs + Diátaxis documentation (`docs/source/`, `.readthedocs.yaml`) is **not yet set up** for this repository. When documentation infrastructure is added, follow the universal guidelines in the system prompt (Section 4.5).
- `README.md` and `CHANGELOG.md` serve as the primary documentation until Sphinx is configured.

### Sublime Text Theme
- The `sublime-theme/` directory contains a Sublime Text 4 package (theme, color scheme, PreTeXt syntax & snippets). Keep its color scheme synchronized with `COLOR_PALETTE` in `src/frontend/colors.py`.

---

## 🏛️ Standards & Provenance

Software architecture, packaging governance, testing standards, branching discipline, and scientific parameter validation across this workspace are adapted from the CERFACS COOP engineering standards. Local HTML archives reside in `docs/COOP_blog/`.

---

_🔬 Eigenscribe Inc. & Scriber Labs 2025–2026. Part of the Scriber Labs Research Framework._
