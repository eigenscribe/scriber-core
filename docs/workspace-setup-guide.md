# 🌐 Workspace Distribution & Cross-Project Integration Guide

This guide defines how to establish `scriber-core` as the single source of truth across all **Eigenscribe Inc.** and **Scriber Labs** repositories using **Option B: Centralized Submodule / Template Repository Architecture**.

---

## 🏛️ Architecture Overview

To eliminate drift across independent projects, all agents, engineers, and repositories link directly back to `scriber-core`:

```text
scriber-core (Canonical Single Source of Truth)
├── house-rules/
│   ├── python-rules.md
│   └── css-rules.md
├── boilerplates/
│   ├── css/
│   │   └── tse-boilerplate.css
│   ├── notebooks/
│   │   └── visuals-boilerplate.ipynb
│   └── python/
│       ├── gold-standard-boilerplate.py
│       └── visualization_boilerplate.py
└── docs/
    └── workspace-setup-guide.md

       │
       ├──► [Workflow 1: Git Submodule]       ──► Existing Projects (.scriber-core/)
       │
       ├──► [Workflow 2: Template Repo]       ──► Green-field Repositories
       │
       └──► [Workflow 3: Installable Package] ──► Python Libraries (src/ layout + uv)
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

### 1️⃣ Step 1: Establish Standard `src/` Layout
Structure the target repository cleanly:

```text
my-project/
├── .scriber-core/              # Linked rules & templates (Submodule)
├── .junie/
│   └── AGENTS.md               # Guidelines bridge
├── src/
│   └── my_package/
│       ├── __init__.py         # Explicit __all__ exports
│       └── core.py             # Math / logic implementation
├── tests/
│   └── test_core.py            # Automated tests
├── pyproject.toml              # Build & dependency configuration
└── README.md                   # Onboarding & architecture overview
```

### 2️⃣ Step 2: Configure `pyproject.toml`
Set up the build backend and uv package flag:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
description = "Deterministic scientific module adhering to Scriber Labs standards."
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=2.0.0",
    "scipy>=1.11.0",
    "matplotlib>=3.8.0",
]

[tool.uv]
managed = true
package = true

[tool.uv.pip]
universal = true
```

### 3️⃣ Step 3: Sync & Install in Editable Mode
Run:

```bash
uv sync
```
or install directly into current environment:
```bash
uv pip install -e .
```

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
3. **No Orphan Artifacts**:
   - Remove temporary scratchpads, stale comments, broken imports, or outdated configurations before ending any session.

---

## 🛠️ Verification & Best Practices

1. **Path Resolution**: Keep paths in consumer projects pointing cleanly to `.scriber-core/house-rules/...`.
2. **Version Pinning**: Submodules allow pinning to specific stable commits or tags for critical releases, preventing accidental breakage from rule changes.
3. **Continuous Enforcement**: Agent sessions run against the linked rules without requiring manual copy-pasting across projects.
