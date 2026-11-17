# 🌐 Workspace Distribution, Packaging & Cross-Project Integration Guide

This guide defines how to establish `scriber-core` as the canonical source of truth across all **Eigenscribe Inc.** and **Scriber Labs** repositories. It integrates the **Centralized Submodule / Template Repository Architecture** with the **COOP Gold Standard for Python Packages**, adapted for modern PEP 517/518/621 declarative packaging and deterministic `uv` environment tooling.

---

## 🏛️ Architecture Overview

To eliminate drift across independent projects, all agents, engineers, and repositories link directly back to `scriber-core`:

```text
scriber-core (Canonical Single Source of Truth)
├── house-rules/
│   ├── python-rules.md                 # Mathematical typography, typing, RNG, script flow
│   └── css-rules.md                    # The Scriber Experience 4-layer design tokens & glassmorphism
├── boilerplates/
│   ├── css/                            # Reference stylesheets (tse-boilerplate.css)
│   ├── notebooks/                      # Reference visualization notebooks (visuals-boilerplate.ipynb)
│   └── python/                         # Gold standard script & visualization templates
└── docs/
    └── workspace-setup-guide.md        # Comprehensive workspace, packaging & integration guide

       │
       ├──► [Workflow 1: Git Submodule]       ──► Existing Projects (.scriber-core/)
       │
       ├──► [Workflow 2: Template Repo]       ──► Green-field Repositories
       │
       └──► [Workflow 3: Installable Package] ──► Python Libraries (src/ layout + uv)
```

---

## 📁 1. Canonical Repository Structure & Layout Standards

All Python repositories across Eigenscribe Inc. and Scriber Labs must adhere to the standardized `src/` layout for import parity, test isolation, and deterministic packaging:

```text
my-package/
├── LICENSE                             # Mandatory license (MIT)
├── README.md                           # Mandatory onboarding, architecture, usage & badges
├── CHANGELOG.md                        # Mandatory version history (Keep a Changelog standard)
├── pyproject.toml                      # Single source of truth for build, dependencies & tools
├── .gitignore                          # Strict exclusion of build, cache & data artifacts
├── .readthedocs.yaml                   # Read the Docs v2 build configuration
├── Makefile                            # Standard automation targets (docs, test, lint, wheel, publish)
├── Dockerfile                          # Optional containerization for portability / C extensions
├── .scriber-core/                      # Linked canonical rules & templates (Submodule)
├── .junie/
│   └── AGENTS.md                       # Agent workspace guidelines & reference bridge
├── docs/                               # Diátaxis-structured Sphinx documentation
│   ├── source/
│   │   ├── conf.py                     # Sphinx configuration
│   │   ├── index.rst                   # Master table of contents
│   │   ├── readme_link.md              # MyST single-source include of root README.md
│   │   ├── changelog_link.md           # MyST single-source include of root CHANGELOG.md
│   │   ├── api/                        # API reference documentation
│   │   ├── tutorials/                  # Learning-oriented step-by-step guides (*.rst, *.md, *.ipynb)
│   │   ├── howto/                      # Task-oriented problem-solving guides (*.rst, *.md, *.ipynb)
│   │   └── explanations/               # Understanding-oriented conceptual derivations (*.rst, *.md)
│   ├── Makefile                        # Sphinx build automation
│   ├── make.bat                        # Windows Sphinx build script
│   └── _build/                         # Generated HTML output (NEVER committed to git)
├── src/
│   └── my_package/                     # Isolated source root (Import Parity)
│       ├── __init__.py                 # Contains __version__ and explicit __all__ exports
│       ├── cli.py                      # Click fast-start CLI entry point
│       └── core.py                     # Core logic / mathematical implementations
└── tests/
    ├── conftest.py                     # Shared pytest fixtures & deterministic seeds
    ├── unit/
    │   └── test_*.py                   # Fast, isolated unit tests
    └── func/
        └── test_*.py                   # End-to-end and functional integration tests
```

---

## 🔢 2. Versioning, Branching & Changelog Governance

### 1️⃣ Semantic Versioning (SemVer 2.0.0)
All packages adhere strictly to Semantic Versioning (`MAJOR.MINOR.PATCH`, e.g., `1.3.2`):
- **MAJOR**: Incompatible API modifications or breaking mathematical schema changes.
- **MINOR**: Backward-compatible functionality additions or new public API methods.
- **PATCH**: Backward-compatible bug fixes, numerical stability enhancements, or documentation updates.

### 2️⃣ Cactus Branching Model
For research frameworks and packages under 5,000 lines of code, development proceeds on a **single main branch (`main`)** using short-lived topic branches for atomic merges. This eliminates synchronization overhead while preserving history cleanliness.

### 3️⃣ In-Code Version Export
The package version must always be accessible in Python runtime via `package_name.__version__`:
```python
# src/my_package/__init__.py
from typing import Final

__version__: Final[str] = "1.0.0"
__all__: Final[list[str]] = ["__version__"]
```

### 4️⃣ Keep a Changelog Standard
Maintaining `CHANGELOG.md` is mandatory for all repositories following [Keep a Changelog 1.0.0](https://keepachangelog.com/en/1.0.0/):
- Group changes under: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- Track unreleased modifications under `## [Unreleased]`.
- Provide explicit dated release sections (e.g., `## [1.0.0] - 2026-11-17`).

### 5️⃣ Release Tagging
Every version bump must be committed and accompanied by an exact annotated git tag:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin main --tags
```

---

## 📦 3. Declarative Packaging & Modern `uv` Toolchain

Eigenscribe repositories use modern PEP 517/518/621 declarative packaging via `pyproject.toml` with `hatchling` and the ultra-fast `uv` workspace toolchain. Standalone `requirements.txt` files are strictly eliminated; all dependencies reside in `pyproject.toml`.

### 1️⃣ Canonical `pyproject.toml` Specification
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "1.0.0"
description = "Deterministic scientific module adhering to Scriber Labs standards."
readme = "README.md"
license = { text = "MIT" }
authors = [
    { name = "Scriber Labs & Eigenscribe Inc." }
]
requires-python = ">=3.10"
keywords = [
    "visualization",
    "cli",
    "scientific-computing",
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Visualization",
]
dependencies = [
    "numpy>=2.0.0",
    "scipy>=1.11.0",
    "matplotlib>=3.8.0",
    "click>=8.0.0",
]

[project.urls]
Homepage = "https://github.com/eigenscribe/my-package"
Documentation = "https://my-package.readthedocs.io/en/latest/"
"Bug Tracker" = "https://github.com/eigenscribe/my-package/issues"

[project.scripts]
my-cli = "my_package.cli:main"

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.4.0",
]
docs = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=2.0.0",
    "myst-parser>=2.0.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.uv]
managed = true
package = true

[tool.hatch.build.targets.wheel]
packages = ["src/my_package"]

[tool.uv.pip]
universal = true
```

### 2️⃣ Package Management & Sync Commands
- **Synchronize deterministic virtual environment**:
  ```bash
  uv sync --all-extras
  ```
- **Install in editable development mode**:
  ```bash
  uv pip install -e .[dev,docs]
  ```
- **Build distribution wheels and source archives**:
  ```bash
  uv build
  ```

---

## 🧪 4. Testing & Coverage Strategy ("In Medio Stat Virtus")

1. **Framework & Layout**:
   - Use `pytest` for all test execution.
   - Separate test files into `tests/unit/test_*.py` for isolated unit tests and `tests/func/test_*.py` for end-to-end integration workflows.
   - Centralize shared fixtures and deterministic RNG seeds in `tests/conftest.py`.
2. **"In Medio Stat Virtus" Coverage Philosophy**:
   - Target **70%+ test coverage** for all core logic and mathematical simulation modules.
   - Avoid rushing toward brittle 100% coverage with redundant, heavy functional tests that increase refactoring overhead.
   - Establish a solid foundational layer of unit tests first before writing high-level functional tests.
3. **Execution with Coverage**:
   ```bash
   pytest --cov=my_package tests/
   ```

---

## 🔍 5. Linting, Formatting & Code Quality

1. **PEP 8 Compliance & Modern Linters**:
   - Enforce strict PEP 8 compliance using `ruff` (or `pylint` with scores $\ge 9.0/10$).
   - Code formatting is automated using standard 4-space indentation and 100-character line lengths.
2. **Pragmatic Linting Discipline ("In Medio Stat Virtus")**:
   - Maintain API ergonomics and conceptual story flow; never distort public signatures (e.g. creating unwieldy argument wrappers solely to stay below an arbitrary 5-argument linter threshold).
3. **Root Cause Resolution**:
   - Always resolve issues in the source code rather than masking problems by disabling rules in `.pylintrc` or `ruff.toml`.

---

## 📚 6. Documentation Architecture (Sphinx + Read the Docs + Diátaxis)

1. **The Diátaxis Documentation Framework**:
   Organize `docs/source/` into four distinct cognitive quadrants:
   - **`tutorials/`**: Learning-oriented step-by-step onboarding walkthroughs.
   - **`howto/`**: Task-oriented recipes solving concrete operational problems.
   - **`explanations/`**: Understanding-oriented theoretical background, physics derivations, and architectural notes.
   - **`api/`**: Reference-oriented technical descriptions of classes, functions, and interfaces.
2. **Single-Sourced Content Reuse**:
   - Use `myst_parser` to link root files (`README.md`, `CHANGELOG.md`) directly into Sphinx docs via `readme_link.md` and `changelog_link.md` without duplicating files.
3. **External Link & Asset Hygiene**:
   - Do not use private intranet or local relative image links in `README.md` or documentation that will fail when rendered on PyPI, Read the Docs, or GitHub.
4. **Git Housekeeping for Docs**:
   - `docs/_build/` and auto-generated API directories (`docs/source/api/_generated/`) must be listed in `.gitignore` and **never committed**.
5. **Read the Docs Configuration (`.readthedocs.yaml`)**:
   ```yaml
   version: 2

   sphinx:
     configuration: docs/source/conf.py

   build:
     os: ubuntu-22.04
     tools:
       python: "3.11"
     apt_packages:
       - pandoc

   python:
     install:
       - method: pip
         path: .
         extra_requirements:
           - docs
   ```

---

## 💻 7. Command Line Interface (CLI) & Color-Coded Architecture

1. **Fast-Start Click CLI & Self-Discovery**:
   - Implement entry-point command line interfaces using `click` or standalone execution routers (`python -m cli`).
   - Running the base command (e.g., `my-cli`, `python -m cli`, or `my-cli --help`) must immediately present all available subcommands, parameters, and documentation.
2. **ADHD High-Contrast Semantic Color Spectrum**:
   - CLI interfaces must use semantic color-coding to structure cognitive load and eliminate reading fatigue:
     - **`PRIMARY_GRADIENT` (`#00e8ff` → `#008eff` → `#6f78fa` → `#5e17eb`)**: Section headers, category titles, and diagnostic summaries.
     - **`SECONDARY_GRADIENT` (`#00a6ff` → `#7952f5` → `#a855f7` → `#ff28a2`)**: Signature block banners and decorative framing.
     - **Electric Cyan (`#00e8ff`) & Sky Blue (`#14b5ff`)**: Actionable command names and primary interactive focal points.
     - **Pale Lilac (`#d8b4fe`)**: Syntax flags, options, and parameters.
     - **Ice Blue (`#b8f6ff`)**: High-luminance, low-fatigue descriptive text and documentation.
     - **Periwinkle Blue (`#5280ff`)**: Structural frame dividers and table borders.
     - **Semantic Status Badges**: `success_emerald` (`#10b981`), `midwest_indigo` (`#6f78fa`), `vivid_pink` (`#f72585`), and `warning_amber` (`#f7c548`).
3. **Golden Ratio Multi-Stop Gradient Scaling**:
   - Multi-stop TrueColor gradient text computed via `multi_gradient()` scales color segment proportions according to the Golden Ratio ($\phi \approx 1.618$, $w_k = (1/\phi)^k$).
   - Gives greater visual weight to starting blue/cyan hues on the left and smoothly tapers into purple/pink on the right.
4. **Console Script Registration & Smoke Testing**:
   - Bind CLI entry points in `pyproject.toml` under `[project.scripts]`.
   - Every CLI suite must provide a built-in smoke test subcommand (e.g., `python -m cli smoke-test`) verifying terminal ANSI processing and subtool execution.

---

## 🎨 8. Repo-Wide Hex Color Standard & Design Token Architecture

To ensure strict visual fidelity across CLI TrueColor output, Matplotlib/Seaborn plotting themes, dark-mode Mermaid diagrams, and CSS tokens, `scriber-core` enforces a mandatory repo-wide color standard:

1. **Single Source of Truth (`COLOR_PALETTE`)**:
   - `COLOR_PALETTE` in `src/frontend/colors.py` is the canonical dictionary for all named color variables across the workspace.
2. **Repo-Wide Hex Constraint**:
   - **All color variables must be converted to / defined as canonical 6-digit hex format (`#rrggbb`)**, or reference valid key names from `COLOR_PALETTE` in `src/frontend/colors.py`.
   - Never define raw or arbitrary RGB integer triplets across downstream modules without a canonical hex reference.
3. **Deterministic RGB Normalization**:
   - The `hex_to_rgb(hex_code)` utility in `src/frontend/colors.py` provides deterministic conversion from hex strings to `(R, G, B)` integer tuples for ANSI escape sequence generation (`\033[38;2;R;G;Bm`).
4. **Cross-Subsystem Alignment**:
   - Web / CSS design tokens: mapped directly from hex values to CSS custom properties (`--color-primary: #00e8ff`).
   - Scientific visualization: Matplotlib `rcParams` and Seaborn colormaps use hex strings directly (`axes.prop_cycle: ['#14b5ff', '#9b7dff', '#22f792', '#f78166']`).
   - Dark-mode Mermaid themes: hex codes map directly into diagram directives and node styling classes (`primaryColor: #14b5ff`).

---

## 🚀 9. Distribution & PyPI Publishing Protocol

For distributable libraries published to PyPI or internal registries, follow this 6-step release workflow:

1. **Local Verification**:
   - Run all test suites and linters locally:
     ```bash
     pytest --cov=my_package
     ruff check .
     ```
2. **CI Pipeline Pass**:
   - Push commits to the remote repository and verify that all automated CI pipeline stages (Test, Lint, Docs) succeed.
3. **Changelog & Version Tagging**:
   - Update `CHANGELOG.md` with release notes and date.
   - Bump version in `pyproject.toml` and `src/my_package/__init__.py`.
   - Commit and tag: `git tag -a v1.0.0 -m "Release 1.0.0" && git push origin main --tags`.
4. **Build Distribution**:
   - Build clean binary wheel and source distribution artifacts:
     ```bash
     uv build
     ```
5. **Optional TestPyPI Upload**:
   - When introducing major metadata or dependency schema changes, validate on TestPyPI first:
     ```bash
     uv publish --publish-url https://test.pypi.org/legacy/
     ```
6. **PyPI Production Publish**:
   - Upload distribution artifacts to PyPI:
     ```bash
     uv publish
     ```

---

## 🏷️ 10. CI/CD Automation & Status Badges

Repositories must implement automated CI pipelines with three core verification stages:
1. **Testing**: Runs `pytest` across supported Python versions with coverage reporting.
2. **Linting**: Runs `ruff check` / formatting verification.
3. **Documentation**: Verifies Sphinx HTML build (`cd docs && make html`).

Display standard informative badges at the top of `README.md`:
```markdown
[![Pipeline](https://github.com/eigenscribe/my-package/actions/workflows/ci.yml/badge.svg)](https://github.com/eigenscribe/my-package/actions)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](https://github.com/eigenscribe/my-package)
[![Lint](https://img.shields.io/badge/lint-ruff-blue)](https://github.com/astral-sh/ruff)
[![Docs](https://readthedocs.org/projects/my-package/badge/?version=latest)](https://my-package.readthedocs.io/)
```

---

## 🔗 Workflow 1: Git Submodule Integration (Existing Projects)

For existing codebases or multi-repo ecosystems, include `scriber-core` as a git submodule to ensure seamless synchronization.

### 1️⃣ Step 1: Add Submodule to Target Repository
From the root of your target repository, run:
```bash
git submodule add <REPO_URL_TO_SCRIBER_CORE> .scriber-core
```

### 2️⃣ Step 2: Configure Agent Entry Point
Create or update `.junie/AGENTS.md` (and optionally a root `AGENTS.md`) in your target repository with standard reference bridges:

```markdown
# 🔬 Project Agent Guidelines

This project adheres to canonical Eigenscribe Inc. / Scriber Labs development standards.

## 📁 Canonical Workspace References
Agents must consult the linked rules and templates in `.scriber-core`:
- **Python Rules**: `.scriber-core/house-rules/python-rules.md`
- **CSS / UI System**: `.scriber-core/house-rules/css-rules.md`
- **Workspace & Packaging Guide**: `.scriber-core/docs/workspace-setup-guide.md`
- **Python Numeric Template**: `.scriber-core/boilerplates/python/gold-standard-boilerplate.py`
- **Visualization Bootstrap Template**: `.scriber-core/boilerplates/python/visualization_boilerplate.py`
- **CSS Design System Template**: `.scriber-core/boilerplates/css/tse-boilerplate.css`
- **Visuals & Graphs Template**: `.scriber-core/boilerplates/notebooks/visuals-boilerplate.ipynb`

## 🎯 Project-Specific Context & Overrides
- Target domain and operational requirements for this repository.
```

### 3️⃣ Step 3: Clone & Synchronization Commands
- **Cloning a project with the submodule**:
  ```bash
  git clone --recurse-submodules <TARGET_REPO_URL>
  ```
- **Updating to the latest rules across all repos**:
  ```bash
  git submodule update --remote --merge
  ```

---

## 📋 Workflow 2: Template Repository (New Projects)

For greenfield projects:

### 1️⃣ Step 1: Enable Template Repository
In GitHub / GitLab repository settings for `scriber-core`:
- Check **"Template repository"** (GitHub) / mark as template.

### 2️⃣ Step 2: Initialize from Template
1. Create a new repository using `scriber-core` as the template base.
2. Clone locally and verify directory layout.
3. The newly generated project retains the canonical structure (`house-rules/`, `boilerplates/`, `.junie/AGENTS.md`).

---

## 📦 Workflow 3: Setting Up as an Installable Python Package

When creating or transforming a consumer repository into an installable, distributable Python package:

1. **Establish `src/` layout**: Create `src/my_package/__init__.py` with `__version__` and `__all__`.
2. **Configure `pyproject.toml`**: Use `hatchling` build-backend and `[tool.uv]` package management.
3. **Add Click CLI**: Place command line tools in `src/my_package/cli.py` and map in `[project.scripts]`.
4. **Establish Testing & Docs Scaffolding**: Create `tests/unit/`, `tests/func/`, `tests/conftest.py`, and `docs/source/`.
5. **Sync & Install**: Run `uv sync --all-extras` or `uv pip install -e .[dev,docs]`.

---

## 🔄 End-of-Run File Consistency Protocol

Every autonomous agent run or development cycle must conclude with a mandatory consistency audit to ensure source code cleanliness and zero drift:

1. **Relative File Synchronization**:
   - Every file must be updated appropriately relative to new files created during a given run.
   - If a new module or script is created, ensure `README.md`, setup guides, `pyproject.toml` dependencies, and package `__all__` exports reflect it.
2. **Mutual Consistency Verification**:
   - `pyproject.toml` dependencies ⟷ imports in source code.
   - `README.md` examples ⟷ executable public API functions.
   - Tests ⟷ actual implementation behavior.
   - `CHANGELOG.md` ⟷ actual committed changes.
3. **No Orphan Artifacts**:
   - Remove temporary scratchpads, stale comments, broken imports, or outdated configurations before ending any session.
4. **Build Artifact Cleanliness**:
   - Confirm that `dist/`, `build/`, `*.egg-info`, `docs/_build/`, and auto-generated API directories remain strictly excluded from git tracking.

---

## 📚 References & Provenance

The repository layout, testing philosophy, versioning discipline, and packaging governance defined in this workspace synthesize modern PEP 517/518/621 tooling (`uv`, `hatchling`) with the software engineering standards established by the CERFACS COOP team:

- **Original Article**: Dauptain, Antoine. *"Python packages: the COOP gold standard"*, The COOP Blog, CERFACS (Feb 21, 2022).
  - **Web**: [https://cerfacs.fr/coop/coop-standard-on-python-pkges](https://cerfacs.fr/coop/coop-standard-on-python-pkges)
  - **Local Archive**: [`docs/COOP_blog/Python packages_ the COOP gold standard · The COOP Blog.html`](COOP_blog/Python%20packages_%20the%20COOP%20gold%C2%A0standard%20%C2%B7%20The%20COOP%20Blog.html)
- **Related COOP Articles**:
  - *"The COOP Click Command line interfaces"* — [Web](https://cerfacs.fr/coop/the-coop-click-command-line-interfaces) | Local: [`docs/COOP_blog/The COOP Click Command line interfaces · The COOP Blog.html`](COOP_blog/The%20COOP%20Click%20Command%20line%C2%A0interfaces%20%C2%B7%20The%20COOP%20Blog.html)
  - *"The Coop Cactus branching model"* — [Web](https://cerfacs.fr/coop/the-coop-cactus-branching-model) | Local: [`docs/COOP_blog/The Coop Cactus branching model · The COOP Blog.html`](COOP_blog/The%20Coop%20Cactus%20branching%C2%A0model%20%C2%B7%20The%20COOP%20Blog.html)
  - *"Using the json-SCHEMA standard for scientific applications"* — [Web](https://cerfacs.fr/coop/using-the-json-schema-standard-for-scientific-applications) | Local: [`docs/COOP_blog/Using the json-SCHEMA standard for scientific applications_ · The COOP Blog.html`](COOP_blog/Using%20the%20json-SCHEMA%20standard%20for%20scientific%C2%A0applications_%20%C2%B7%20The%20COOP%20Blog.html)
