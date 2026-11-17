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

### Changed
- Renamed `src/frontend/THE_SCRIBER_EXPERIENCE/` to `src/frontend/the_scriber_experience/` (PEP 8 compliant package naming).
- Updated all imports across `src/`, `boilerplates/`, and `tests/` to use `the_scriber_experience` instead of `THE_SCRIBER_EXPERIENCE`.
- Removed `sys.modules` aliasing hacks in `src/frontend/__init__.py` that bridged uppercase and lowercase import names.
- Removed try/except import fallback in `src/cli/main.py` that attempted `THE_SCRIBER_EXPERIENCE` before `the_scriber_experience`.
- Updated `pyproject.toml` console script entry point to `cli.main:main`.
- Updated `docs/workspace-setup-guide.md` to explicitly state `COLOR_PALETTE` in `src/frontend/colors.py` as the canonical source of truth with the repo-wide hex constraint.
- Renamed `src/frontend/the_scriber_experience/style/tse_colors.py` to `semantic_roles.py` to eliminate naming collision with `colors.py` in the parent directory.
- Renamed `src/frontend/the_scriber_experience/style/tse_gradients.py` to `gradient_presets.py` to eliminate naming collision with `gradients.py` in the parent directory.
- Moved `src/frontend/messaging.py` to `src/cli/messaging.py` — all CLI-specific terminal styling now lives in `src/cli/`.

### Removed
- Removed `src/frontend/messaging.py` (moved to `src/cli/messaging.py`) — all CLI-specific terminal styling now lives in `src/cli/`.
- Removed deprecated `src/frontend/the_scriber_experience/cli/` directory and its contents (`__init__.py`, `gradients.py`, `main.py`, `messaging.py`), consolidating all CLI utilities into `src/cli/`.
- Removed hyphenated alias files `src/frontend/the_scriber_experience/style/tse-colors.py` and `tse-gradients.py` (these simply forwarded to `tse_colors.py` and `tse_gradients.py`).
- Removed `THE_SCRIBER_EXPERIENCE` export alias from `src/__init__.py` and `src/frontend/__init__.py`.
- Removed `boilerplates/python/gold-standard-boilerplate.py` (identical duplicate of `gold-standard.py`).
- Removed `house-rules/python-rules_v1.md` (content duplicate of `python-rules.md`).
- Removed `src/frontend/the_scriber_experience/style/plots/` forwarding bridge directory (no external imports; re-exported from `plots/`).

## [1.0.0] - 2026-11-17

### Added
- Core repository initialization with `src/frontend/` and `src/cli/` packages.
- 4-layer design token system with 67 primitive colors in `COLOR_PALETTE`.
- Multi-stop TrueColor gradient engine with Golden Ratio ($\phi \approx 1.618$) keyframe scaling.
- Comprehensive ANSI 256-color palette index, terminal swatches, and table formatter.
- Automated testing suite covering CLI commands, colors table, and messaging utilities.
