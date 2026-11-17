# 🧿 Scriber Labs: Agent Workspace Index

Welcome to the canonical environment index for autonomous development agents. This workspace enforces strict structural layout layering, deterministic mathematical simulation profiling, uncompromising code verification rules, and automated workspace consistency.

## 🧭 System Onboarding Directory

```text
├── docs/
│   └── workspace-setup-guide.md        # Multi-project distribution & setup guide (Submodules / Templates / Packaging)
├── house-rules/
│   ├── python-rules.md               # Mathematical typography, packaging hygiene & consistency rules
│   ├── python-rules_v1.md            # Reference version 1 rules archive
│   └── css-rules.md                  # Glassmorphic visual layout layering standards
├── boilerplates/
│   ├── css/
│   │   └── tse-boilerplate.css         # Eigenscribe signature high-contrast layout blueprint
│   ├── mermaid/
│   │   └── boilerplate_diagram.mmd     # Dark-mode Mermaid diagram architecture template
│   ├── notebooks/
│   │   └── visuals-boilerplate.ipynb   # Visualizations, NetworkX topologies & color palettes template
│   └── python/
│       ├── gold-standard.py            # Gold standard numeric integration template
│       ├── gold-standard-boilerplate.py # Submodule canonical alias for numeric template
│       └── visualization_boilerplate.py # Matplotlib, Seaborn & Plotly theme bootstrap template
├── src/
│   ├── __init__.py                   # Scriber Core root namespace
│   ├── cli/                          # 💻 Primary Scriber Core CLI suite & TrueColor tools
│   │   ├── __init__.py               # CLI package exports & public API
│   │   ├── __main__.py               # Package execution entry point (`python -m cli`)
│   │   ├── main.py                   # Command router, gradient banners, and command catalog
│   │   ├── colors_table.py           # COLOR_PALETTE table renderer with TrueColor swatches
│   │   └── colors.py                 # Direct CLI wrapper for palette inspection
│   └── frontend/                     # 🎨 Frontend, design tokens & styling subsystem
│       ├── __init__.py
│       ├── colors.py                 # Canonical named color palette (COLOR_PALETTE), RGB, hex_to_rgb
│       ├── gradients.py              # Golden ratio TrueColor multi-stop gradient engine (GRADIENT_PRESETS)
│       └── the_scriber_experience/   # 🔱 The Scriber Experience (TSE) styling subsystems
│           ├── __init__.py
│           ├── style/                # Design tokens, TSE palettes & gradient presets
│           │   ├── __init__.py
│           │   ├── tse_colors.py     # TSE semantic colors, CLI status roles, EIGEN spectrum
│           │   ├── tse_gradients.py  # TSE multi-stop gradient sequences & presets
│           │   ├── tse-colors.py     # Hyphenated alias forwarding to tse_colors.py
│           │   └── tse-gradients.py  # Hyphenated alias forwarding to tse_gradients.py
│           ├── cli/                  # Legacy TSE CLI formatting & messaging tools
│           ├── plots/                # Scientific plotting themes & colormaps
│           │   ├── __init__.py
│           │   └── theme.py          # Theme engine for Matplotlib, Pyplot, Seaborn, Plotly
│           └── mermaid/              # Dark-mode Mermaid.js diagram theme engine & preview
│               ├── __init__.py
│               └── theme.py          # Class definitions, directives & HTML preview renderer
├── sublime-theme/
│   ├── EigenScribe/                  # Sublime Text 4 package (theme, color scheme, PreTeXt syntax & snippets)
│   ├── install.sh                    # Bash installer (macOS / Linux, copy or symlink mode)
│   ├── install.ps1                   # PowerShell installer (Windows)
│   └── README.md                     # Package documentation, installation, and configuration guide
├── .junie/
│   ├── AGENTS.md                     # Canonical agent guidelines & workspace directives
│   └── skills/
│       └── cosmic-visual-styling/    # Workspace skill for EIGEN / cosmic visual themes & styling
├── pyproject.toml                    # PyPI packaging & uv dependency configuration (v1.0.0)
└── README.md                         # Master onboarding index (This file)
```

## 🛠️ Infrastructure & Tooling Lock-ins

- **Package & Environment Manager**: `uv` (Deterministic synchronization via `uv sync`).
- **Target Runtime Engine**: Python 3.11+
- **Primary IDE Workspace**: JetBrains PyCharm Professional / IntelliJ IDEA.

## 💻 Scriber Core CLI Suite (`python -m cli`)

`scriber-core` provides a unified, color-coded CLI suite in `src/cli/` featuring signature TrueColor gradient banners, golden ratio-proportioned gradient text, interactive palette tables, and structured command catalogs:

```bash
# Sync dependencies and development tools
uv sync --extra dev

# Run default CLI entry point (prints SECONDARY_GRADIENT banner & color-coded command catalog)
uv run python -m cli

# Display the high-contrast ADHD-optimized command catalog
uv run python -m cli commands

# Render the signature TrueColor block text banner (or custom text)
uv run python -m cli banner "SCRIBER-CORE"

# Inspect the canonical COLOR_PALETTE with TrueColor swatch blocks, hex, RGB, and ANSI escapes
uv run python -m cli colors-table
uv run python -m cli.colors_table --block-width 6 --sort hue

# Render TrueColor multi-stop gradients with Golden Ratio keyframe scaling
uv run python -m cli gradient "Deterministic Autonomous Agent Baseline" --preset eigenscribe

# Display architecture telemetry, active token counts, and gradient presets
uv run python -m cli info

# Run built-in self-diagnostics and CLI smoke tests
uv run python -m cli smoke-test
```

### 🎯 Cognitive Load & ADHD Semantic Color Coding

The command directory and CLI outputs implement an ergonomic visual hierarchy to eliminate reading fatigue and accelerate command scanning:
- **`PRIMARY_GRADIENT` (`#00e8ff` → `#008eff` → `#6f78fa` → `#5e17eb`)**: Section headers, category titles, and diagnostic headers proportioned with Golden Ratio decay ($\phi \approx 1.618$).
- **`SECONDARY_GRADIENT` (`#00a6ff` → `#7952f5` → `#a855f7` → `#ff28a2`)**: Block text banners, subtitles, and decorative framing.
- **Electric Cyan (`#00e8ff`) & Vivid Sky Blue (`#14b5ff`)**: Primary focal points, actionable command names, and interactive targets.
- **Pale Lilac (`#d8b4fe`)**: Command arguments, flags, and syntax options.
- **High-Luminance Ice Blue (`#b8f6ff`)**: Command descriptions and contextual documentation.
- **Periwinkle Blue (`#5280ff`)**: Structural box-drawing borders and grid dividers.
- **Status Badges**: `success_emerald` (`#10b981`), `midwest_indigo` (`#6f78fa`), `vivid_pink` (`#f72585`), and `warning_amber` (`#f7c548`).

---

## 🎨 Repo-Wide Hex Color Standard & Design Token Architecture

To ensure strict visual fidelity across CLI TrueColor output, Matplotlib/Seaborn plotting themes, dark-mode Mermaid diagrams, and CSS tokens, `scriber-core` enforces a mandatory repo-wide color standard:

1. **Single Source of Truth (`COLOR_PALETTE`)**:
   - `COLOR_PALETTE` in `src/frontend/colors.py` is the canonical dictionary for all named color variables across the repository.
2. **Repo-Wide Hex Constraint**:
   - **All color variables must be converted to / defined as canonical 6-digit hex format (`#rrggbb`)**, or reference valid key names from `COLOR_PALETTE` in `src/frontend/colors.py`.
   - Never hardcode raw or inconsistent RGB values in downstream modules without a canonical hex reference.
3. **Deterministic RGB Normalization**:
   - The `hex_to_rgb(hex_code)` utility in `src/frontend/colors.py` provides deterministic conversion from hex strings to `(R, G, B)` integer tuples for ANSI escape sequence generation (`\033[38;2;R;G;Bm`).
4. **Golden Ratio Multi-Stop Gradient Interpolation**:
   - Multi-stop gradients computed via `multi_gradient()` scale keyframe segment lengths according to the Golden Ratio ($\phi \approx 1.618$, $w_k = (1/\phi)^k$).
   - Segments taper smoothly from dominant blues and cyans on the left to violets, purples, and magentas on the right.

---

## 🔱 Legacy Eigenscribe CLI Tooling (`eigenscribe`)

For backward compatibility with standalone design token inspection, the `eigenscribe` console script remains registered under `[project.scripts]`:

```bash
# Run legacy design system diagnostics & theme exports
uv run eigenscribe doctor
uv run eigenscribe theme --format css
uv run eigenscribe mermaid --sample
```

## 📦 Cross-Project Distribution & Package Setup

`scriber-core` serves as the single source of truth across all **Eigenscribe Inc.** and **Scriber Labs** projects. There are three core ways to utilize and package this workspace:

1. **Git Submodule (Existing Projects)**:
   - Link this workspace into target repositories:
     ```bash
     git submodule add <SCRIBER_CORE_REPO_URL> .scriber-core
     ```
   - Connect guidelines via `.junie/AGENTS.md` bridging to `.scriber-core/house-rules/...`.
   - Update anytime with: `git submodule update --remote --merge`.

2. **Template Repository (Green-field Projects)**:
   - Enable template mode in repository settings and click **"Use this template"**.
   - Cloned projects inherit the canonical directory structure (`house-rules/`, `boilerplates/`, `.junie/AGENTS.md`).

3. **Installable Python Package Configuration (`src/` Layout)**:
   - To configure consumer projects as installable Python libraries using `uv`:
     - Adopt standard layout: `src/<package_name>/__init__.py` and `src/<package_name>/core.py`.
     - Configure `pyproject.toml` with `[build-system]` (`hatchling`) and `[tool.uv]` (`package = true`).
     - Install and sync in editable mode with `uv sync` or `uv pip install -e .`.

For detailed, step-by-step walkthroughs, see [`docs/workspace-setup-guide.md`](docs/workspace-setup-guide.md).

## 🎛️ Agent Execution House Rules & End-of-Run Consistency

Before executing any generation loop, training pass, or asset construction, agents must ingest and strictly conform to the sub-system specifications:

1. **Python Rules (`/house-rules/python-rules.md`)**: Forces explicit LaTeX/text derivations, checks array dimensionality boundaries to eliminate silent broadcasting traps, binds modern `np.random.default_rng()` constraints, and mandates explicit `__all__` exports.
2. **CSS Rules (`/house-rules/css-rules.md`)**: Dictates strict, predictable flex/grid container scaffolds using the Eigenscribe high-contrast token spectrum.
3. **End-of-Run File Consistency & Hygiene**:
   - At the conclusion of every development pass or agent run, **all project files must be audited for mutual consistency**.
   - When new source files, modules, CLI flags, or packages are introduced or modified, corresponding configuration files (`pyproject.toml`, `.gitignore`), documentation (`README.md`, setup guides), docstrings, and tests **must be updated immediately**.
   - No orphan, out-of-sync, or undocumented artifacts may remain at the end of a run.

For each repository, establish:

- What the project actually does.
- What has been implemented and tested.
- What the figures and results genuinely demonstrate.
- What remains speculative or unfinished.
- Where the relevant mathematical reasoning lives.

---
🔬 *Eigenscribe Inc. 2025-2026. Part of the Scriber Labs Research Framework.*
