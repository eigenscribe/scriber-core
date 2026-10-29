# 🧿 Scriber Labs: Agent Workspace Index

Welcome to the canonical environment index for autonomous development agents. This workspace enforces strict structural layout layering, deterministic mathematical simulation profiling, uncompromising code verification rules, and automated workspace consistency.

## 🧭 System Onboarding Directory

```text
├── docs/
│   └── workspace-setup-guide.md # Multi-project distribution & setup guide (Submodules / Templates / Packaging)
├── house-rules/
│   ├── python-rules.md        # Mathematical typography, packaging hygiene & consistency rules
│   └── css-rules.md           # Glassmorphic visual layout layering standards
├── boilerplates/
│   ├── css/
│   │   └── tse-boilerplate.css          # Eigenscribe signature high-contrast layout blueprint
│   ├── notebooks/
│   │   └── visuals-boilerplate.ipynb    # Visualizations, NetworkX topologies & color palettes template
│   └── python/
│       ├── gold-standard-boilerplate.py # Gold standard numeric integration script template
│       └── visualization_boilerplate.py # Generalizable visualization bootstrap for Matplotlib/Pyplot/Seaborn
├── sublime-theme/
│   ├── EigenScribe/           # Sublime Text 4 package (theme, color scheme, PreTeXt syntax & snippets)
│   ├── install.sh             # Bash installer (macOS / Linux, copy or symlink mode)
│   ├── install.ps1            # PowerShell installer (Windows)
│   └── README.md              # Package documentation, installation, and configuration guide
├── .junie/
│   └── AGENTS.md              # Canonical agent guidelines & workspace directives
├── pyproject.toml             # uv environment dependencies and locks
└── README.md                  # Master onboarding index (This file)
```

## 🛠️ Infrastructure & Tooling Lock-ins

- **Package & Environment Manager**: `uv` (Deterministic synchronization via `uv sync`).
- **Target Runtime Engine**: Python 3.11+
- **Primary IDE Workspace**: JetBrains PyCharm Professional / IntelliJ IDEA.

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
