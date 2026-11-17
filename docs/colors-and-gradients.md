# 🎨 Scriber Core: Color Variables, Design Tokens & Gradient Catalog

This document establishes the canonical reference catalog for all color tokens, palette mappings, and gradient presets across **Eigenscribe Inc.** and **Scriber Labs**. It serves as the single source of truth for UI/CLI development, plotting theme generation, and dark-mode diagram design.

---

## 📋 1. Single Source of Truth (`COLOR_PALETTE`)

All primitive color tokens in `scriber-core` are defined in `src/frontend/colors.py` as 6-digit hex values (`#rrggbb`). Downstream modules, CLI tools, plotting themes, and stylesheets must import and reference these token names rather than introducing raw, uncoordinated RGB/hex literals.

### 🎨 Complete Primitive Palette Table

| # | Token Key Name | Hex Code | RGB Channel Vector | Perceptual Category & Semantic Role |
| :---: | :--- | :---: | :---: | :--- |
| **1** | `deep_pine` | `#071a12` | `(7, 26, 18)` | 💚 Deep background / dark forest baseline |
| **2** | `forest_teal` | `#064e38` | `(6, 78, 56)` | 💚 Deep muted teal / secondary surface |
| **3** | `pine` | `#059669` | `(5, 150, 105)` | 💚 Medium emerald / verified state |
| **4** | `success_emerald` | `#10b981` | `(16, 185, 129)` | 💚 **CLI Status**: Success & STEM verified metric |
| **5** | `ibm-green` | `#309592` | `(48, 149, 146)` | 💚 Muted cyan-green / industrial indicator |
| **6** | `deep_green` | `#038b00` | `(3, 139, 0)` | 💚 Pure deep green / high-saturation accent |
| **7** | `neon_green` | `#31ff40` | `(49, 255, 64)` | 💚 High-luminance neon / attention indicator |
| **8** | `bright_chartreuse` | `#70e000` | `(112, 224, 0)` | 💚 High-contrast lime / mathematical scalar |
| **9** | `junie-lime` | `#a7c957` | `(167, 201, 87)` | 💚 Soft olive-lime / forest gradient stop |
| **10** | `pale_mint` | `#b4ffcf` | `(180, 255, 207)` | 💚 Light mint / luminous accent text |
| **11** | `tropical_teal` | `#03e8bd` | `(3, 232, 189)` | 💚 High-saturation teal / quantum indicator |
| **12** | `electric_cyan` | `#00ffee` | `(0, 255, 238)` | 🩵 High-energy cyan / `tse-gradient-1` start |
| **13** | `pure_cyan` | `#00ffff` | `(0, 255, 255)` | 🩵 Pure cyan / full saturation interactive stop |
| **14** | `bright_cyan` | `#00f0ff` | `(0, 240, 255)` | 🩵 Signature `tse-cyan` / active focus |
| **15** | `vivid_cyan` | `#00e8ff` | `(0, 232, 255)` | 🩵 **Primary Brand**: Eigenscribe core cyan |
| **16** | `sky_cyan` | `#4cc9f0` | `(76, 201, 240)` | 🩵 Soft sky cyan / section bullet marker |
| **17** | `ibm-cyan` | `#2ca9e6` | `(44, 169, 230)` | 🩵 Technical sky blue / documentation accent |
| **18** | `sky_info` | `#38bdf8` | `(56, 189, 248)` | 🩵 **CLI Status**: Informational / interactive badge |
| **19** | `ice_blue` | `#b8f6ff` | `(184, 246, 255)` | 🩵 Luminous low-fatigue body text token |
| **20** | `midnight_navy` | `#06152b` | `(6, 21, 43)` | 💙 Deep cosmic background void |
| **21** | `deep_ocean_blue` | `#003b73` | `(0, 59, 115)` | 💙 Deep structural substrate / frame fill |
| **22** | `vivid_blue` | `#0070eb` | `(0, 112, 235)` | 💙 Saturated primary blue / node 4 spectrum |
| **23** | `eigen_blue` | `#008eff` | `(0, 142, 255)` | 💙 Core eigenscribe intermediate blue stop |
| **24** | `skyline_blue` | `#0a95eb` | `(10, 149, 235)` | 💙 Intermediate gradient bridge blue |
| **25** | `vivid_sky_blue` | `#14b5ff` | `(20, 181, 255)` | 💙 Interactive command name & active control |
| **26** | `electric_blue` | `#00a6ff` | `(0, 166, 255)` | 💙 Quantum status & `electric` gradient start |
| **27** | `sky_blue` | `#3a98ff` | `(58, 152, 255)` | 💙 Clear sky accent / network node identifier |
| **28** | `strong_blue` | `#0355e8` | `(3, 85, 232)` | 💙 High-density blue / border accent |
| **29** | `ibm_indigo` | `#4361ee` | `(67, 97, 238)` | 💙 Crisp periwinkle-indigo / structural link |
| **30** | `periwinkle_blue` | `#5280ff` | `(82, 128, 255)` | 💙 Frame borders & table box drawing |
| **31** | `midwest_indigo` | `#6f78fa` | `(111, 120, 250)` | 💙 Signature mid-tone indigo / `STYLE` badge |
| **32** | `deep_indigo` | `#3a0ca3` | `(58, 12, 163)` | 💙 Deep violet-indigo / shadow highlight |
| **33** | `deep_plum` | `#120A24` | `(18, 10, 36)` | 💜 Cosmic void purple substrate |
| **34** | `dark_violet` | `#3b176e` | `(59, 23, 110)` | 💜 Dark purple structural framing |
| **35** | `electric_violet` | `#5e17eb` | `(94, 23, 235)` | 💜 Core eigenscribe terminal violet stop |
| **36** | `bright_violet` | `#7c3aed` | `(124, 58, 237)` | 💜 Rotor status & function identifier |
| **37** | `ibm_purple` | `#844ccc` | `(132, 76, 204)` | 💜 Technical purple / category marker |
| **38** | `bright_purple` | `#a855f7` | `(168, 85, 247)` | 💜 Signature `tse-purple` / secondary control |
| **39** | `royal_purple` | `#7209b7` | `(114, 9, 183)` | 💜 Deep royal purple / gradient anchor |
| **40** | `pale_lilac` | `#d8b4fe` | `(216, 180, 254)` | 💜 Syntax flags, parameters & options |
| **41** | `black_cherry` | `#210817` | `(33, 8, 23)` | 🩷 Dark magenta shadow background |
| **42** | `dark_berry` | `#7c174f` | `(124, 23, 79)` | 🩷 Deep berry framing / warning shadow |
| **43** | `deep_rose` | `#ad1457` | `(173, 20, 87)` | 🩷 Dense rose accent / critical highlight |
| **44** | `vivid_pink` | `#f72585` | `(247, 37, 133)` | 🩷 Signature `tse-pink` / `TOKEN` badge |
| **45** | `ibm_pink` | `#fe28a2` | `(254, 40, 162)` | 🩷 Technical pink / secondary gradient stop |
| **46** | `bright_pink` | `#ff40a1` | `(255, 64, 161)` | 🩷 High-energy pink / sunset terminal stop |
| **47** | `rose_pink` | `#ff66b3` | `(255, 102, 179)` | 🩷 Soft rose / Node 8 spectrum identifier |
| **48** | `soft_rose` | `#ff76a1` | `(255, 118, 161)` | 🩷 Auxiliary decorative accent |
| **49** | `pale_orchid_pink`| `#ffb4f6` | `(255, 180, 246)` | 🩷 High-luminance pink text accent |
| **50** | `bright_magenta` | `#ff00c3` | `(255, 0, 195)` | 🩷 Pure magenta / network status marker |
| **51** | `hot_pink` | `#ff007b` | `(255, 0, 123)` | 🩷 Neon hot pink / cyberpunk terminal stop |
| **52** | `error_crimson` | `#d7263d` | `(215, 38, 61)` | ❤️ **CLI Status**: Error / critical alert |
| **53** | `dusty_peach` | `#e7a697` | `(231, 166, 151)` | 🧡 Soft neutral coral / low-fatigue indicator |
| **54** | `soft_coral` | `#f77f64` | `(247, 127, 100)` | 🧡 Auxiliary warm indicator |
| **55** | `peach_coral` | `#f79764` | `(247, 151, 100)` | 🧡 Mid-tone warm highlight |
| **56** | `tangerine` | `#ff8855` | `(255, 136, 85)` | 🧡 High-visibility amber-orange |
| **57** | `coral_orange` | `#ff783d` | `(255, 120, 61)` | 🧡 Dynamic parameter & high-attention accent |
| **58** | `apricot` | `#ff9d57` | `(255, 157, 87)` | 🧡 Warm golden apricot / plot cycle stop |
| **59** | `golden_amber` | `#feb639` | `(254, 182, 57)` | 💛 Warm golden accent / Node 5 spectrum |
| **60** | `warning_amber` | `#f7c548` | `(247, 197, 72)` | 💛 **CLI Status**: Warning / `DIAG` badge |
| **61** | `ibm_black` | `#161616` | `(22, 22, 22)` | 🖤 Standard deep dark background |
| **62** | `ibm_gray` | `#262625` | `(38, 38, 37)` | 🖤 Neutral gray dark surface |
| **63** | `charcoal` | `#1e293b` | `(30, 41, 59)` | 🖤 Surface elevated background fill |
| **64** | `granite` | `#264653` | `(38, 70, 83)` | 🖤 Forest baseline dark anchor stop |
| **65** | `slate` | `#64748b` | `(100, 116, 139)` | 🤍 Neutral muted label & gridline token |
| **66** | `ibm_white` | `#f4f4f4` | `(244, 244, 244)` | 🤍 High-contrast light foreground |
| **67** | `ghost_white` | `#f8fafc` | `(248, 250, 252)` | 🤍 Clean white primary text foreground |

---

## 🌈 2. Linear Gradient Engine & Preset Catalog

All multi-stop TrueColor gradients in `src/frontend/gradients.py` support mathematical Golden Ratio stop proportioning ($\phi \approx 1.618$). Segment proportions decrease from left to right according to $w_k = (1/\phi)^k$, providing cognitive grounding with prominent blue/cyan start stops tapering into violet/pink.

### 🌟 Registered Gradient Presets (`GRADIENT_PRESETS`)

| Preset Key | Hex Stop Sequence | Keyframe Color Names | Primary Mathematical / Design Role |
| :--- | :--- | :--- | :--- |
| **`eigenscribe`** | `#00e8ff` → `#008eff` → `#6f78fa` → `#5e17eb` | `vivid_cyan` → `eigen_blue` → `midwest_indigo` → `electric_violet` | **Signature Eigenscribe Gradient**: CLI banners, headers, and major section titles |
| **`tse-gradient-1`** | `#00ffee` → `#00e8ff` → `#14b5ff` | `electric_cyan` → `vivid_cyan` → `vivid_sky_blue` | **Cyan Flow**: High-luminance interactive controls and telemetry monitors |
| **`tse-gradient-2`** | `#00e8ff` → `#14b5ff` → `#0a95eb` → `#0070eb` → `#5e17eb` | `vivid_cyan` → `vivid_sky_blue` → `skyline_blue` → `vivid_blue` → `electric_violet` | **Deep Spectrum**: Extended 5-stop gradient for wide terminal displays and plots |
| **`electric`** | `#00a6ff` → `#a855f7` → `#ff00c3` | `electric_blue` → `bright_purple` → `bright_magenta` | **Signature Electric**: High-contrast cybernetic headings and brand banners |
| **`sunset`** | `#ff6b35` → `#f7c548` → `#ff40a1` | `solar_orange` → `warning_amber` → `bright_pink` | **Solar Sunset**: Dynamic execution telemetry, heat warnings, and benchmarks |
| **`forest`** | `#a7c957` → `#2a9d8f` → `#264653` | `junie-lime` → `tropical_teal` → `granite` | **Deep Forest**: Numerical simulations, environmental metrics, and ecology models |
| **`midnight`** | `#38bdf8` → `#818cf8` → `#f43f5e` | `sky_info` → `midwest_indigo` → `rose_pink` | **Midnight Cosmic**: Astrodynamics, phase topologies, and deep-space metrics |
| **`aurora`** | `#06b6d4` → `#10b981` → `#84cc16` | `aqua` → `success_emerald` → `bright_chartreuse` | **Quantum Aurora**: Energy fields, spectral analysis, and optimal convergence |
| **`cyberpunk`** | `#00f0ff` → `#7000ff` → `#ff007b` | `bright_cyan` → `deep_violet` → `hot_pink` | **Cyberpunk Neon**: High-attention diagnostic flags, overrides, and stress states |
| **`purple_gradient`** | `#7209b7` → `#a855f7` → `#7952f5` | `royal_purple` → `bright_purple` → `bright_violet` | **Royal Violet**: Architectural submodules, structural layers, and mathematics |

---

## 🏛️ 3. Semantic Roles & Subsystem Mappings

### 🔱 Signature TSE Tokens (`TSE_COLORS`)
- `tse-cyan`: `COLOR_PALETTE["bright_cyan"]` (`#00f0ff`)
- `tse-blue`: `COLOR_PALETTE["electric_blue"]` (`#00a6ff`)
- `tse-periwinkle`: `COLOR_PALETTE["periwinkle_blue"]` (`#5280ff`)
- `tse-purple`: `COLOR_PALETTE["bright_purple"]` (`#a855f7`)
- `tse-pink`: `COLOR_PALETTE["vivid_pink"]` (`#f72585`)

### 🚦 Semantic Attention Roles (`SEMANTIC_COLORS`)
- `info`: `COLOR_PALETTE["sky_info"]` (`#38bdf8`) — Informational states and focus
- `success`: `COLOR_PALETTE["success_emerald"]` (`#10b981`) — Verified outcomes and passing assertions
- `warning`: `COLOR_PALETTE["warning_amber"]` (`#f7c548`) — Attention triggers and warnings
- `error`: `COLOR_PALETTE["error_crimson"]` (`#d7263d`) — Exceptions, failures, and critical halts
- `quantum`: `COLOR_PALETTE["electric_blue"]` (`#00a6ff`) — Quantum / harmonic phase markers
- `rotor`: `COLOR_PALETTE["bright_violet"]` (`#7c3aed`) — Rotational kinetics and oscillator markers
- `network`: `COLOR_PALETTE["bright_magenta"]` (`#ff00c3`) — Graph topologies and network edges

### 🏷️ CLI Functional Badges (`BADGE_COLORS`)
- `CORE`: `COLOR_PALETTE["success_emerald"]` (`#10b981`) — Verified core utilities
- `STYLE`: `COLOR_PALETTE["midwest_indigo"]` (`#6f78fa`) — Visual styling & gradient generators
- `TOKEN`: `COLOR_PALETTE["vivid_pink"]` (`#f72585`) — Palette token inspection tools
- `DIAG`: `COLOR_PALETTE["warning_amber"]` (`#f7c548`) — Health diagnostics and smoke tests

---

## 🔍 4. Design & Architecture Review: The Good, the Bad, and the Ugly

A comprehensive utilitarian review of design token architecture and styling subsystems across `scriber-core`:

### 🌟 The Good
1. **Single Source of Truth (`COLOR_PALETTE`)**:
   - Centralizing all 67 named color definitions in `src/frontend/colors.py` guarantees repo-wide color fidelity across terminal CLIs, Matplotlib plots, Seaborn colormaps, dark-mode Mermaid diagrams, and CSS tokens.
2. **Mathematical Golden Ratio ($\phi$) Gradient Proportioning**:
   - Stop positions computed via $w_k = (1/\phi)^k$ eliminate arbitrary gradient banding, anchoring visual attention on high-luminance blue/cyan focal points while smoothly tapering into deep purple/pink accents.
3. **Robust Separation of Concerns**:
   - Clean architectural decoupling between `src/cli/` (terminal user interface, table formatting, click commands) and `src/frontend/` (mathematical color interpolation, design tokens, plotting themes).
4. **Resilient Terminal Compatibility**:
   - Seamless cross-platform support with automatic Windows Virtual Terminal Processing enablement, 24-bit TrueColor rendering, ANSI 256-color fallback, and 16-color degradation.
5. **Deterministic Testing Rigor**:
   - Built-in smoke testing and 100% automated test suite coverage (`pytest`) guaranteeing zero regressions during package refactoring.

### ⚠️ The Bad
1. **Historical Key Naming Inconsistencies**:
   - A minority of keys in `COLOR_PALETTE` use kebab-case (`ibm-green`, `ibm-cyan`, `junie-lime`, `tse-cyan`) while the vast majority follow canonical snake_case (`ibm_indigo`, `ibm_purple`, `vivid_cyan`, `sky_info`). Standardizing all keys to snake_case while preserving alias properties is recommended for future releases.
2. **Residual Hardcoded Hex Literals in Plotting & Mermaid Themes**:
   - While `src/cli/` and `src/frontend/style/` strictly reference `COLOR_PALETTE`, certain theme definitions in `src/frontend/THE_SCRIBER_EXPERIENCE/plots/theme.py` and `mermaid/theme.py` use direct hex literals (`#0d1117`, `#161b22`, `#c8f8ff`) rather than accessing `COLOR_PALETTE["midnight_navy"]` or `COLOR_PALETTE["ice_blue"]`.
3. **Multiple Re-Export Aliases**:
   - The coexistence of `GRADIENT_PRESETS`, `TSE_GRADIENTS`, and `PRESETS` across `gradients.py` increases API redundancy, though it protects legacy callers from breaking changes.

### 🛑 The Ugly
1. **Deprecated Duplicate CLI Folders (Resolved)**:
   - Previously, duplicate CLI implementations existed in both `src/cli/` and `src/frontend/THE_SCRIBER_EXPERIENCE/cli/`, causing import shadowing, partially initialized module errors, and fragile relative imports. Consolidating all CLI commands into `src/cli/` and deleting `src/frontend/THE_SCRIBER_EXPERIENCE/cli/` permanently eliminates this architectural debt.
2. **Module Casing & Path Collisions**:
   - Case-sensitivity variance across Windows NTFS and Linux ext4 with `THE_SCRIBER_EXPERIENCE` vs `the_scriber_experience` required dynamic `sys.modules` aliasing hooks to guarantee consistent cross-platform importability.
