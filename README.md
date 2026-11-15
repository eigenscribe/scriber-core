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
│   └── frontend/                     # 🎨 Frontend, design tokens & styling subsystem
│       ├── __init__.py
│       ├── colors.py                 # Primitive named color palette (COLOR_PALETTE), RGB, hex_to_rgb
│       ├── gradients.py              # ANSI TrueColor multi-stop gradient engine (GRADIENT_PRESETS)
│       └── the_scriber_experience/   # 🔱 The Scriber Experience (TSE) styling subsystems
│           ├── __init__.py
│           ├── style/                # Design tokens, TSE palettes & gradient presets
│           │   ├── __init__.py
│           │   ├── tse_colors.py     # TSE semantic colors, CLI status roles, EIGEN spectrum
│           │   ├── tse_gradients.py  # TSE multi-stop gradient sequences & presets
│           │   ├── tse-colors.py     # Hyphenated alias forwarding to tse_colors.py
│           │   └── tse-gradients.py  # Hyphenated alias forwarding to tse_gradients.py
│           ├── cli/                  # Terminal CLI formatting, gradients & banners
│           │   ├── __init__.py
│           │   ├── main.py           # Unified `eigenscribe` CLI entry point & subcommands
│           │   ├── gradients.py      # CLI TrueColor gradient engine & CLI commands
│           │   └── messaging.py      # ANSI 256 formatting, banners, and semantic logs
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

## 🔱 Eigenscribe CLI (`eigenscribe`)

`scriber-core` includes a self-contained baseline CLI executable via `eigenscribe` (or `uv run eigenscribe`):

```bash
# Sync dependencies and install CLI
uv sync --extra dev

# Run CLI root help & signature banner
uv run eigenscribe --help

# Run full workspace health and token consistency diagnostics
uv run eigenscribe doctor

# Display architecture overview and active token statistics
uv run eigenscribe info

# Render multi-stop TrueColor gradient text
uv run eigenscribe gradient "Deterministic Workspace Suite" --preset cyberpunk
uv run eigenscribe gradient --list-presets

# Inspect color palettes, status roles, and 256-color table
uv run eigenscribe colors --all-256 --spectrum

# Render formatted headers and banners
uv run eigenscribe banner "SCRIBER CORE" --subtitle "Design Tokens & Telemetry"

# Export Matplotlib rcParams or CSS variables
uv run eigenscribe theme --format summary
uv run eigenscribe theme --format css

# Generate or preview dark-mode Mermaid diagrams
uv run eigenscribe mermaid --sample
uv run eigenscribe mermaid --html-preview --output diagram.html
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
