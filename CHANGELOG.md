# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive design tokens and gradient reference document in `docs/colors-and-gradients.md`.
- `theme`, `mermaid`, and `doctor` subcommands in `src/cli/main.py`.
- Re-exported `cli_group` in `src/cli/__init__.py` and `PRESETS` alias in `src/frontend/gradients.py`.

### Changed
- Updated `pyproject.toml` console script entry point to `cli.main:main`.
- Updated `docs/workspace-setup-guide.md` to explicitly state `COLOR_PALETTE` in `src/frontend/colors.py` as the canonical source of truth with the repo-wide hex constraint.

### Removed
- Removed deprecated `src/frontend/THE_SCRIBER_EXPERIENCE/cli/` directory and its contents (`__init__.py`, `gradients.py`, `main.py`, `messaging.py`), consolidating all CLI utilities into `src/cli/` and messaging functions into `src/frontend/messaging.py`.

## [1.0.0] - 2026-11-17

### Added
- Core repository initialization with `src/frontend/` and `src/cli/` packages.
- 4-layer design token system with 67 primitive colors in `COLOR_PALETTE`.
- Multi-stop TrueColor gradient engine with Golden Ratio ($\phi \approx 1.618$) keyframe scaling.
- Comprehensive ANSI 256-color palette index, terminal swatches, and table formatter.
- Automated testing suite covering CLI commands, colors table, and messaging utilities.
