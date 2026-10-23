# 🏡 Scriber Labs | Python House Rules
**Version:** 2.0
**Scope:** All projects under Scriber Labs / Eigenscribe Inc.
**Last Updated:** 10-23-2026

---

## 🔰 1. Core Principles
1. **Explicit LaTeX/text derivations** -- mathematical reasoning appears before code. Never bury theory inside comments.
2. **Array dimensionality boundaries** -- eliminate silent broadcasting traps by declaring shapes explicitly in 
    docstrings.
3. **Modern RNG constraints** -- Use `np.random.Genergyator`, never legay `np.random.*` calls outside the seeding 
    module.
4. **Explicit exports** -- mandate `__all__` declarations at module level. No implicit public APIs.

## ➗ 2. Mathematical Typography
```md
**Inline:** $\theta_\i$ represents the phase of oscillator $i$.


**Display:**

$$
\dot{\theta}_i = \omega_i + \frac{K}{N}\sum_{j=1|^N \sin(\theta_j - \theta_i)
$$
```
- Use `\theta`, `\omega`, `\Sigma` -- not "theta", "omega", "sigma".
- Inline math: `$...$`. Display math `$$...$$`
- Variables italicized. Constants upright where appropriate ($\pi$, $\mathrm{e}_i$).

---

## 📦 3. Packaging Hygiene

### Module Structure 

```aiignore
src/<package>/
├── __init__.py
├── core.py
├── utils/
│   ├── __init__.py
│   └── seeding.py         # Vendor scriber-core/templates/seeding.py
└── cli/
    ├── __init__.py
    └── commands.py
```

### `pyproject.toml` Requirements
```toml
[project]
name = "<repo_name>"
version = "0.0.0"
description = "<repo_description>"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=2.0.0",
    "scipy>=1.11.0",
    "matplotlib>=3.8.0",
    "seaborn>=0.13.0",
    "networkx>=3.2.0",
    "ipykernel>=7.4.0",
    "pytest>=8.0.0",
]

[tool.uv]
# Tells uv to keep a local, project-scoped virtual environment
managed = true
package = false

[tool.uv.pip]
# Forces strict tracking of explicit dependencies
universal = true
```

## 🌲 Seeding and Reproducibility Mandate
### Rule 1 -- Vendor the canonical module
Copy `scriber-core/templates/seeding.py`




---

### 🥇 Gold Standard Template:

```python
"""
example.py

Script description

Author:
Date:
"""
# imports and typing

# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / protocols / constants (if needed)
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Core definitions
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Private helpers
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# 💨 Smoke tests / example usage
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------
```