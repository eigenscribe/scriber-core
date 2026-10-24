# 🏡 Scriber Labs & Eigenscribe Inc. | Unified Python House Rules

**Version:** 2.1 (Unified Canonical Specification)  
**Scope:** All Python development, research frameworks, and numerical simulations across Scriber Labs / Eigenscribe Inc.  
**Last Updated:** 2026-10-23  

---

## 🔰 1. Core Principles & Architectural Ethos

Every Python codebase must optimize readability, reduce cognitive overhead, and provide immediate verification. Every script and module must flow logically from top to bottom according to the Eigenscribe architectural standard:
> *"What exists → What you're allowed to call → How it works → Proof it works"*

1. **Explicit Mathematical Derivations**: Mathematical reasoning and LaTeX/text derivations must precede implementation. Never bury theoretical equations inside brief, cryptic comments.
2. **Array & Tensor Dimensionality Safety**: Prevent silent broadcasting bugs by declaring explicit shapes in docstrings and adding runtime shape assertions (e.g., `assert phases.shape == np.shape(self.omega)`).
3. **Modern Deterministic RNG Constraints**: Strictly use modern `np.random.Generator` (via `np.random.default_rng(seed)`). Never call legacy `np.random.*` or bare `random.*` routines outside the dedicated seeding module.
4. **Explicit Exports & Package Hygiene**: Mandate explicit `__all__` declarations in every `__init__.py`. Strictly avoid implicit exports and wildcard imports.
5. **Separation of Orchestration and Execution**: `def main() -> None:` orchestrates smoke tests and sanity checks without containing direct math or long training loops.

---

## 🔢 2. Number-Emoji Semantic Sectioning

Use explicit number-emoji section headers as semantic visual anchors across all modules for instant visual scannability:
- `/* imports and typing */`
- `/* 🎭 Typing helpers / protocols / constants (if needed) */`
- `1️⃣ Core definitions`
- `2️⃣ Public API (functions users are meant to call)`
- `3️⃣ Private helpers`
- `4️⃣ Smoke tests / example usage` (or `💨 Smoke tests / example usage`)
- `🔥 Entry point`

---

## 🏅 3. Canonical Gold Standard Python Script Template

```python
"""
example.py

Script description and theoretical summary.

Author: Scriber Labs
Date: 2026-10-23
"""
from __future__ import annotations

from typing import Final, Protocol, TypeAlias
import numpy as np
from numpy.typing import NDArray

# -----------------------------------------------------------------------------------------------------------
# 🎭 Typing helpers / protocols / constants (if needed)
# -----------------------------------------------------------------------------------------------------------

ArrayOrFloat: TypeAlias = float | NDArray[np.float64]
DEFAULT_SEED: Final[int] = 27


class EvolutionSolver(Protocol):
    """Protocol defining a standard execution interface for numerical integrators."""

    def step(self, state: NDArray[np.float64], dt: float) -> NDArray[np.float64]:
        """Advance the system state by a single time increment."""
        ...


# -----------------------------------------------------------------------------------------------------------
# 1️⃣ Core definitions
# -----------------------------------------------------------------------------------------------------------

class DynamicalSystem:
    """Core state representation of a physical or dynamical system.

    Attributes
    ----------
    omega : ArrayOrFloat
        Natural frequencies or stationary inertial frame velocities.
    """

    def __init__(self, omega: ArrayOrFloat) -> None:
        """Initialize the dynamical system.

        Parameters
        ----------
        omega : ArrayOrFloat
            Natural frequency parameters.
        """
        self.omega: Final[ArrayOrFloat] = omega

    def compute_derivative(self, state: NDArray[np.float64]) -> NDArray[np.float64]:
        """Calculate instantaneous state derivative dθ/dt.

        Parameters
        ----------
        state : NDArray[np.float64]
            Active state vector coordinates.

        Returns
        -------
        NDArray[np.float64]
            Instantaneous derivative vector.
        """
        assert state.shape == np.shape(self.omega), "State dimensions must match structural constraints."
        return np.asarray(self.omega, dtype=np.float64)


# -----------------------------------------------------------------------------------------------------------
# 2️⃣ Public API (functions users are meant to call)
# -----------------------------------------------------------------------------------------------------------

def simulate_system(
    system: DynamicalSystem,
    initial_state: NDArray[np.float64],
    steps: int,
    dt: float,
) -> NDArray[np.float64]:
    """Execute deterministic state evolution across a fixed integration interval.

    Parameters
    ----------
    system : DynamicalSystem
        The initialized dynamical system instance.
    initial_state : NDArray[np.float64]
        Initial condition state vector.
    steps : int
        Total evaluation steps to compute.
    dt : float
        Integration time step interval.

    Returns
    -------
    NDArray[np.float64]
        Final state vector after integration.
    """
    current_state = np.copy(initial_state)
    for _ in range(steps):
        derivative = system.compute_derivative(current_state)
        current_state = _euler_step(current_state, derivative, dt)
    return current_state


# -----------------------------------------------------------------------------------------------------------
# 3️⃣ Private helpers
# -----------------------------------------------------------------------------------------------------------

def _euler_step(
    state: NDArray[np.float64],
    derivative: NDArray[np.float64],
    dt: float,
) -> NDArray[np.float64]:
    """Perform a single-step Euler integration update: y_{n+1} = y_n + dt * f(t_n, y_n)."""
    return state + (dt * derivative)


# -----------------------------------------------------------------------------------------------------------
# 4️⃣ Smoke tests / example usage
# -----------------------------------------------------------------------------------------------------------

def run_smoke_test() -> bool:
    """Execute quick sanity checks and deterministic verification.

    Returns
    -------
    bool
        True if all validation assertions pass.
    """
    rng = np.random.default_rng(DEFAULT_SEED)
    omega_mock = rng.uniform(0.5, 1.5, size=(4,))
    initial_state = np.zeros(4, dtype=np.float64)

    sys = DynamicalSystem(omega=omega_mock)
    final_state = simulate_system(sys, initial_state, steps=10, dt=0.1)

    expected_state = initial_state + (10 * 0.1 * omega_mock)
    is_valid: bool = np.allclose(final_state, expected_state)
    assert is_valid, "Smoke test failed: state progression mismatch."
    print("✅ Smoke test passed.")
    return is_valid


# -----------------------------------------------------------------------------------------------------------
# 🔥 Entry point
# -----------------------------------------------------------------------------------------------------------

def main() -> None:
    """Orchestrate demonstration and smoke tests without embedding direct business logic."""
    success = run_smoke_test()
    if not success:
        raise ValueError("System validation failed during deterministic verification.")


if __name__ == "__main__":
    main()
```

---

## ➗ 4. Mathematical Rigor & Typography

1. **Explicit Derivations Before Code**:
   Provide full mathematical context and LaTeX derivations prior to implementation. Mathematical theory must never be hidden inside brief or cryptic comments.
2. **Standard LaTeX Notation**:
   - **Inline Math**: `$\theta_i$` represents the phase of oscillator `$i$`.
   - **Display Math**:
     ```markdown
     $$
     \dot{\theta}_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N} \sin(\theta_j - \theta_i)
     $$
     ```
   - Use standard Greek symbols (`\theta`, `\omega`, `\Sigma`, `\phi`), italicized variables ($x, y, t$), and upright mathematical constants ($\pi$, $\mathrm{e}$, $\mathrm{i}$).

---

## 🛡️ 5. Type System & Dimensionality Safety

1. **Explicit Typing Conventions**:
   - Use `Tensor` (not `torch.Tensor`) directly in type annotations.
   - Annotate physically meaningful scalars explicitly (`float | Tensor` or `ArrayOrFloat: TypeAlias = float | NDArray[np.float64]`).
   - Use `Final` for immutable physical and configuration constants (`OMEGA: Final[float] = 1.0`, `DEFAULT_SEED: Final[int] = 27`).
2. **Array Dimensionality Boundaries**:
   - Prevent broadcasting traps by declaring explicit shapes in docstrings and adding runtime shape assertions (e.g., `assert phases.shape == np.shape(self.omega)`).
3. **NumPy-Style Docstrings**:
   - Mandatory on all public functions, classes, and nontrivial private helpers.
   - Minimal viable structure:
     ```python
     """
     Summary of function behavior.

     Parameters
     ----------
     name : type
         Description of parameter.

     Returns
     -------
     type
         Description of return value.
     """
     ```

---

## 🌲 6. Seeding, RNG & Reproducibility Mandate

To eliminate stochastic errors and ensure absolute reproducibility across all environments:

1. **Modern Generator API Only**:
   - Always use `np.random.default_rng(seed)` or `np.random.Generator`.
   - Strictly prohibit legacy global state mutations (`np.random.seed()` or bare `random.seed()`).
2. **Vendored Canonical Seeding Module**:
   - Vendor canonical seeding helpers into `src/<package>/utils/seeding.py` with the sync header:
     ```python
     # Canonical source: scriber-core/templates/seeding.py
     # Synced: YYYY-MM-DD -- do not edit locally without syncing upstream
     ```
3. **Mandatory Seeding Self-Check**:
   - Verify reproducibility, label separation, and stream independence via `python -m <package>.utils.seeding`:
     ```python
     def _self_check() -> None:
         """💨 Smoke test: reproducibility, label separation, stream independence."""
         import numpy as np
         from .seeding import set_global_seed, derive_seed, spawn_generators

         seed = 27

         # Test 1: global seeding reproducibility
         a = set_global_seed(seed)
         b = set_global_seed(seed)
         assert np.array_equal(a.random(10), b.random(10)), "Global seeds are not reproducible."

         # Test 2: derive_seed stability
         assert derive_seed(seed + 10, "x") == derive_seed(seed + 10, "x"), "derive_seed unstable"
         assert derive_seed(seed + 10, "x") != derive_seed(seed + 10, "y"), "labels collided"

         # Test 3: spawned streams independent
         draws = [g.random(10) for g in spawn_generators(7, 4)]
         for i in range(len(draws)):
             for j in range(i + 1, len(draws)):
                 assert not np.array_equal(draws[i], draws[j]), "streams not independent"

         print("✅ Seeding self-check passed.")

     if __name__ == "__main__":
         _self_check()
     ```
4. **RNG Injection in Numerical Routines**:
   - Numerical solvers must accept an explicit generator parameter:
     ```python
     def solve_system(..., rng: np.random.Generator | None = None) -> ...:
         if rng is None:
             rng = set_global_seed(DEFAULT_SEED)
             warnings.warn("Using default seed -- reproducibility not guaranteed across runs")
     ```
5. **No Bare RNG Calls**:
   - Prohibit bare `np.random.*` and `random.*` calls across the codebase outside the dedicated seeding module.

---

## 🥇 7. Numerical Integration & Verification Protocol

Every numerical pipeline must follow these validation safeguards:
1. **Seeded Entry Point**: Explicitly initialize seed and thread the `Generator` through all stochastic functions.
2. **Pre-Flight Self-Check**: Validate basic invariants and dependencies before initiating expensive compute runs.
3. **Convergence Studies**: Systematically halve `dt` to calculate empirical order and assert against expected theoretical convergence rates.
4. **Invariant Tracking**: Track physical conservation quantities (e.g., energy, symplectic form, probability norm) across time and plot numerical drift.
5. **Bitwise Reproducibility Verification**: Validate that identical seeds produce bitwise-identical trajectories (`np.array_equal()`).

---

## 📦 8. Packaging Hygiene, Imports & Architecture

### Module Structure
```text
src/<package>/
├── __init__.py
├── core.py
├── utils/
│   ├── __init__.py
│   └── seeding.py
└── cli/
    ├── __init__.py
    └── commands.py
```

### Packaging & Import Discipline
1. **Explicit Exports**: Every `__init__.py` must declare an explicit `__all__` list. Avoid empty `__init__.py` files that silently expose nothing.
2. **No Wildcard Imports**: Strictly prohibit `from module import *`. Always import explicitly: `from module import func_a, func_b, ClassC`.
3. **Single Source of Truth**: Centralize shared constants (strings, enums, config keys, solver aliases) in a canonical module. Define once, import everywhere.
4. **Path Hygiene**: Never mutate `sys.path` inside `try/except` blocks or at import time. Use proper relative imports or launcher scripts.
5. **Clean `.gitignore`**: Strictly exclude all generated artifacts and binary data (`*.pyc`, `__pycache__/`, `.idea/`, `.vscode/`, `*.npz`, `*.h5`, `plots/`, `*.log`).

### Environment & Dependency Management (`uv` & `pyproject.toml`)
- Use `uv` as the virtual environment and package manager (`uv sync`).
- Distinguish between application/template repositories (`[tool.uv] package = false`) and installable libraries (`[tool.uv] package = true` with standard `[build-system]` using `hatchling` and `src/<package_name>/` layout).
- Example `pyproject.toml`:
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
  managed = true
  package = false

  [tool.uv.pip]
  universal = true
  ```

---

## 🧪 9. Test Coverage Targets & Git Hooks

1. **Targeted Coverage (70%+)**:
   - Core logic modules must maintain 70%+ test coverage.
   - Every public module must have a corresponding test suite.
   - Bug fixes must always include an automated reproduction test demonstrating failure prior to applying the fix.
2. **Automated Pre-Commit Validation**:
   - Enforce standards via `.git/hooks/pre-commit`:
     ```bash
     #!/usr/bin/env bash
     set -euo pipefail

     # Check for bare np.random usage
     if grep -rn "np\.random\." src/ tests/ | grep -v "utils/seeding.py" | grep -v ".pyc"; then
         echo "❌ Bare np.random calls detected outside seeding module"
         exit 1
     fi

     # Run seeding self-check
     python -m src.<package>.utils.seeding

     echo "✅ Pre-commit checks passed"
     ```

---

## 🔄 10. End-of-Run File Consistency Protocol

At the conclusion of every development session or generation pass, perform a holistic audit to ensure zero entropy across the workspace:
- **`README.md` & Documentation**: Accurately reflect all newly implemented features, mathematical models, CLI flags, and setups.
- **`pyproject.toml`**: Synchronize all new dependencies with correct version constraints.
- **`__init__.py` & `__all__`**: Expose newly added public interfaces and prune deprecated symbols.
- **Test Green State**: Ensure all test suites, smoke tests, and seeding self-checks pass without failure.
- **Delta Transparency**: Explicitly specify what is fully implemented and tested versus what remains theoretical or deferred.

---

_🔬 Eigenscribe Inc. & Scriber Labs 2025–2026. Part of the Scriber Labs Research Framework._
