# 🔬 Eigenscribe Inc. / Scriber Labs — Agent Workspace Guidelines

Welcome to the canonical workspace baseline for autonomous development agents across **Eigenscribe Inc.** and **Scriber Labs**. Every task, generation pass, and code modification must strictly follow our core ethos: **deterministic rigor, conceptual story flow, and ADHD-structured cognitive load architecture**.

---

## 📁 0. Canonical Workspace Reference Files

Agents must consult and adhere to the source reference specifications and gold standard templates located in `../house-rules` and `../boilerplates`:

| Directory | File | Purpose & Contents |
| :--- | :--- | :--- |
| `../house-rules` | `../house-rules/python-rules_v1.md` | Core rules for Python development: mathematical typography, modern RNG, typing, package hygiene, docstrings, and script flow. |
| `../house-rules` | `../house-rules/css-rules.md` | The Scriber Experience design system: 4-layer token hierarchy, glassmorphism baseline, ADHD semantic color coding, and golden ratio spacing. |
| `../boilerplates` | `../boilerplates/python/gold-standard-boilerplate.py` | Gold standard reference script template implementing mathematical simulation, explicit type annotations, shape assertions, deterministic RNG, and smoke testing. |
| `../boilerplates` | `../boilerplates/python/visualization_boilerplate.py` | Generalizable visualization bootstrapping script for Matplotlib, Pyplot, and Seaborn with high-contrast curves and 3-style heatmaps. |
| `../boilerplates` | `../boilerplates/css` | Gold standard reference stylesheet implementing the full 4-layer taxonomy, CSS tokens, glassmorphism components, gradients, and responsive layouts. |
| `../boilerplates` | `../boilerplates/notebooks/visuals-boilerplate.ipynb` | Gold standard reference notebook template for scientific visualization, NetworkX graph topologies, dashboards, and design token / colormap palettes. |

---

## 🏛️ 1. Core Architectural Ethos & Conceptual Story Flow

All scripts, stylesheets, and documentation must flow logically from top to bottom according to the Eigenscribe architectural standard:
> *"What exists → What you're allowed to call → How it works → Proof it works"*

### 🔢 Number-Emoji Semantic Sectioning
Use explicit number-emoji section headers as semantic anchors (not mere decoration) across all project files for instant visual scannability:

* **In Python scripts / modules:**
  - `/* imports and typing */`
  - `/* 🎭 Typing helpers / protocols / constants (if needed) */`
  - `1️⃣ Core definitions`
  - `2️⃣ Public API (functions users are meant to call)`
  - `3️⃣ Private helpers`
  - `4️⃣ Smoke tests / example usage`
  - `🔥 Entry point`
* **In CSS stylesheets:**
  - `0️⃣ Layer 1: CSS Custom Properties & Design Tokens`
  - `1️⃣ Layer 2: Base Element Resets & Normalization`
  - `2️⃣ Layer 3: Layout Scaffolding & Responsive Grids`
  - `3️⃣ Layer 4: Core Reusable UI Component Classes`

---

## 🐍 2. Python Engineering & Mathematical Rigor

When writing or modifying Python modules, follow the rules defined in `../house-rules/python-rules_v1.md` and reference `../boilerplates/python/gold-standard-boilerplate.py`:

1. **Modern Deterministic RNG**:
   - Always use `np.random.default_rng(seed)`.
   - Never use legacy `np.random.seed()` (which seeds a global `RandomState`).
   - Pass explicit seeds (e.g. `DEFAULT_SEED: Final[int] = 27`) in smoke tests for deterministic reproducibility.
2. **Explicit Type Annotations**:
   - Use `Tensor` (not `torch.Tensor`) in type signatures.
   - Annotate physically meaningful scalars (`float | Tensor` or `ArrayOrFloat: TypeAlias = float | NDArray[np.float64]`).
   - Use `Final` for system constants (e.g. `omega: Final[ArrayOrFloat] = ...`).
3. **Array & Tensor Dimensionality Safety**:
   - Explicitly verify array dimensionality and shapes (e.g., `assert phases.shape == np.shape(self.omega)`) to eliminate silent broadcasting traps.
4. **NumPy-Style Docstrings**:
   - Mandatory on public functions, classes, and nontrivial private helpers (with `Parameters`, `Returns`, and theoretical context).
5. **Clean Entry Point & Script Organization**:
   - `def main() -> None:` must always orchestrate smoke tests / demonstrations and never contain direct math or long loops.
   - `if __name__ == "__main__":` is strictly for smoke tests, sanity checks, or launcher scripts—never for heavy training loops or long sweeps.
6. **Package Hygiene & Imports**:
   - Define an explicit `__all__` in every `__init__.py`.
   - Strictly prohibit wildcard imports (`from module import *`).
   - Centralize shared constants (strings, enums, config keys) in a canonical module.
   - Never mutate `sys.path` inside `try/except` import blocks.

---

## 🎨 3. CSS, Design System & Cognitive Load Architecture

When styling web pages, apps, data dashboards, or CLI outputs, adhere to `../house-rules/css-rules.md` and `../boilerplates/css`:

1. **The Scriber Glassmorphism Baseline**:
   - Dark mode first (`--color-bg: #0d1117`, `--color-surface: #161b22`, `--color-surface-elevated: #21262d`).
   - Translucent frosted glass overlays (`backdrop-filter: blur(12px)`), crisp light borders (`rgba(255, 255, 255, 0.12)`), and colored specular glow highlights.
2. **ADHD High-Contrast Semantic Color Spectrum**:
   - **Primary Cyan / Electric Blue (`#00e8ff` / `#14b5ff`)**: Interactive focal points, primary controls, standard variables, and active states.
   - **Secondary Violet (`#7952f5` / `#9b7dff`)**: Structural markers, navigation layers, functions, and subsections.
   - **Tertiary Neon Green (`#22f792` / `#10b981`)**: Success metrics, verified states, STEM/tech indicators, and math constants (`--color-math: #00f5db`).
   - **Quaternary Amber / Coral Orange (`#f78166` / `#ff783d`)**: Warnings, dynamic parameters, auxiliary data, and high-attention highlights.
   - **Pernary Hot Pink / Magenta (`#ec4899` / `#ff40a1`)**: Special modes, accents, and producer overrides.
3. **Golden Ratio ($\phi \approx 1.618$) Metrics**:
   - Use geometric step tokens: `--space-xs: 0.382rem` ($\phi^{-2}$), `--space-sm: 0.618rem` ($\phi^{-1}$), `--space-md: 1.000rem` ($1.0$), `--space-lg: 1.618rem` ($\phi^1$), `--space-xl: 2.618rem` ($\phi^2$), and split layouts (`.layout-golden`).
4. **Cross-Context Theming**:
   - Align Streamlit/Dash apps, Mermaid diagrams (`primaryColor: #14b5ff`), Matplotlib/Pyplot `rcParams` (`axes.prop_cycle: ['#14b5ff', '#9b7dff', '#22f792', '#f78166']`), and Rich CLI colors to the Eigenscribe token palette.

---

## 🛠️ 4. Tooling, Environment & Repository House Rules

1. **Environment & Dependencies**:
   - Virtual environments and dependencies are managed deterministically via `uv` and `pyproject.toml`.
   - Synchronize environments using `uv sync`.
2. **Project Housekeeping**:
   - Maintain `.gitignore` to strictly exclude generated artifacts (`*.pyc`, `__pycache__/`, `.idea/`, `.vscode/`, `*.npz`, `plots/`, logs).
3. **Proportional Test Coverage**:
   - Target **70%+ coverage** for core logic modules.
   - Bug fixes must always include a reproducer test that fails prior to applying the fix.
   - Every public module should have a dedicated test file or built-in smoke test.
4. **Repository Audit Obligations**:
   For any repository or feature built within this workspace, clearly establish:
   - What the project actually does.
   - What has been implemented and tested.
   - What the figures, derivations, and results genuinely demonstrate.
   - What remains speculative, deferred, or unfinished.
   - Where the underlying mathematical reasoning and derivations live.
5. **End-of-Run File Consistency & Hygiene**:
   - Every file must be updated appropriately relative to files created or modified by the agent during a given run.
   - At the conclusion of any session, perform an explicit consistency audit ensuring that all documentation (`README.md`, setup guides), configuration files (`pyproject.toml`, `.gitignore`), tests, and source codes are completely clean, synchronized, and mutually consistent.
