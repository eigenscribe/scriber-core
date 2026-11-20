# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive design tokens and gradient reference document in `docs/colors-and-gradients.md`.
- `theme`, `mermaid`, and `doctor` subcommands in `src/cli/main.py`.
- Re-exported `cli_group` in `src/cli/__init__.py` and `PRESETS` alias in `src/frontend/gradients.py`.
- New standard in `docs/workspace-setup-guide.md`: mandatory rule prohibiting duplicate file/folder names (case-insensitive and separator-normalized), with exceptions for `__init__.py` and `main.py`.
- AI-Generated Content Disclosure Standard in `docs/workspace-setup-guide.md` (section 4) — requiring disclosure notices, dedicated `docs/` placement, and README cross-references for AI-generated documentation.
- GitHub Actions release workflow (`.github/workflows/publish.yml`) that runs the test suite on Python 3.10–3.12, builds the sdist + wheel with `uv build` (with a wheel-import smoke test), and publishes to PyPI/TestPyPI via `uv publish` using Trusted Publishing (OIDC, no stored tokens); triggered by `vX.Y.Z` SemVer tag pushes or manual `workflow_dispatch`.
- `src/scriber_core/__init__.py` package root that exports `__version__` and re-exports the `frontend` and `cli` subpackages, establishing `scriber_core` as the single public import namespace.

### Changed
- Collapsed multi-path `try/except ImportError` fallback chains across `src/frontend/gradients.py`, `src/frontend/the_scriber_experience/style/gradient_presets.py`, `src/frontend/the_scriber_experience/style/semantic_roles.py`, `src/frontend/the_scriber_experience/mermaid/theme.py`, `src/cli/main.py`, `src/cli/messaging.py`, and `src/cli/__main__.py` into canonical absolute imports (`frontend.*` and `cli.*`).
- Refactored `src/frontend/the_scriber_experience/style/gradient_presets.py` to import and re-export gradient presets directly from `frontend.gradients`.
- Updated CLI package exports and repointed all `cli.colors` consumers to `cli.colors_table`.
- Renamed `src/frontend/THE_SCRIBER_EXPERIENCE/` to `src/frontend/the_scriber_experience/` (PEP 8 compliant package naming).
- Updated all imports across `src/`, `boilerplates/`, and `tests/` to use `the_scriber_experience` instead of `THE_SCRIBER_EXPERIENCE`.
- Removed `sys.modules` aliasing hacks in `src/frontend/__init__.py` that bridged uppercase and lowercase import names.
- Removed try/except import fallback in `src/cli/main.py` that attempted `THE_SCRIBER_EXPERIENCE` before `the_scriber_experience`.
- Updated `pyproject.toml` console script entry point to `cli.main:main`.
- Updated `docs/workspace-setup-guide.md` to explicitly state `COLOR_PALETTE` in `src/frontend/colors.py` as the canonical source of truth with the repo-wide hex constraint.
- Renamed `src/frontend/the_scriber_experience/style/tse_colors.py` to `semantic_roles.py` to eliminate naming collision with `colors.py` in the parent directory.
- Renamed `src/frontend/the_scriber_experience/style/tse_gradients.py` to `gradient_presets.py` to eliminate naming collision with `gradients.py` in the parent directory.
- Moved `src/frontend/messaging.py` to `src/cli/messaging.py` — all CLI-specific terminal styling now lives in `src/cli/`.
- Consolidated the TSE/semantic/CLI/EIGEN color palettes (`TSE_COLORS`, `SEMANTIC_COLORS`, `CLI_COLORS`, `EIGEN_COLORS`, `EIGEN_NODE_COLORS`, `EIGEN_LABEL_COLORS`) into `src/frontend/colors.py`, making `src/frontend/colors.py` and `src/frontend/gradients.py` the sole source of truth for colors and gradients; repointed `src/cli/main.py`, `src/frontend/__init__.py`, and `src/frontend/the_scriber_experience/__init__.py` to them.
- Consolidated the two top-level packages into a single `scriber_core` namespace: moved `src/frontend/` → `src/scriber_core/frontend/` and `src/cli/` → `src/scriber_core/cli/`, repointed every import to `scriber_core.frontend.*` / `scriber_core.cli.*`, updated the console entry point to `scriber_core.cli.main:main`, the wheel packages to `["src/scriber_core"]`, and the CI wheel smoke test to `import scriber_core` — so the distribution no longer installs generic top-level `frontend`/`cli` packages that could collide with consumer projects.

### Removed
- Deleted duplicate `src/cli/colors.py` facade in favor of direct `cli.colors_table` imports, establishing `src/frontend/colors.py` as the single owner of the `colors` module name.
- Deleted stray package marker `src/__init__.py` to eliminate ambiguous `src.`-prefixed imports and maintain `packages = ["src/frontend", "src/cli"]` parity.
- Removed `src/frontend/messaging.py` (moved to `src/cli/messaging.py`) — all CLI-specific terminal styling now lives in `src/cli/`.
- Removed deprecated `src/frontend/the_scriber_experience/cli/` directory and its contents (`__init__.py`, `gradients.py`, `main.py`, `messaging.py`), consolidating all CLI utilities into `src/cli/`.
- Removed hyphenated alias files `src/frontend/the_scriber_experience/style/tse-colors.py` and `tse-gradients.py` (these simply forwarded to `tse_colors.py` and `tse_gradients.py`).
- Removed `THE_SCRIBER_EXPERIENCE` export alias from `src/__init__.py` and `src/frontend/__init__.py`.
- Removed `boilerplates/python/gold-standard-boilerplate.py` (identical duplicate of `gold-standard.py`).
- Removed `house-rules/python-rules_v1.md` (content duplicate of `python-rules.md`).
- Removed `src/frontend/the_scriber_experience/style/plots/` forwarding bridge directory (no external imports; re-exported from `plots/`).
- Removed the `src/frontend/the_scriber_experience/style/` directory and its modules (`__init__.py`, `semantic_roles.py`, `gradient_presets.py`); the `semantic_roles.py` palettes now live in `src/frontend/colors.py` and `gradient_presets.py` was a redundant re-export of `src/frontend/gradients.py`.

### Fixed
- Defined the previously missing `EIGEN_LABEL_COLORS` (referenced in imports and `__all__` but never defined) and corrected `src/cli/branding.py` to use `COLOR_PALETTE["node-2"]` instead of the non-existent `vivid_cyan` key — both defects had made the `frontend` and `cli` packages fail to import.
- Aligned `tests/unit/test_cli.py` and `tests/unit/test_cli_colors_table.py` with the actual public API (`run_cli_smoke_test`, `EIGENSCRIBE_BLOCK_TEXT`, `node-1`) and ANSI-stripped the `--version` assertions; the full suite passes (46 tests).

## [1.0.0] - 2026-11-17

### Added
- Core repository initialization with `src/frontend/` and `src/cli/` packages.
- 4-layer design token system with 67 primitive colors in `COLOR_PALETTE`.
- Multi-stop TrueColor gradient engine with Golden Ratio ($\phi \approx 1.618$) keyframe scaling.
- Comprehensive ANSI 256-color palette index, terminal swatches, and table formatter.
- Automated testing suite covering CLI commands, colors table, and messaging utilities.
