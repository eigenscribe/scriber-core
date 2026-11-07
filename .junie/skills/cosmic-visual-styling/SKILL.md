---
name: cosmic-visual-styling
description: Guidelines, design tokens, color palettes, and code recipes for applying the Eigenscribe / Sephirah cosmic visual theme, gradients, colormaps, and glassmorphic UI components across Python, CSS, and dashboards.
---

### 🌌 Cosmic Visual Styling & Sephirah Design System

Use this skill whenever designing, styling, or updating figures, scientific plots, data dashboards, CSS stylesheets, or CLI interfaces in the **Eigenscribe / Scriber Labs** workspace.

---

### 🎨 1. Canonical Cosmic & Sephirah Color Tokens

#### Surface & Void Foundations
- **Cosmic Center:** `#0a0f1f` — Deep celestial navy (radial center / primary card face).
- **Cosmic Mid / Void:** `#050812` — Intermediate cosmic gradient stop / dark canvas base.
- **Cosmic Pure Black:** `#000000` — Outer boundary void.
- **Standard Dark Slate:** `#0d1117` — Default Eigenscribe background foundation.
- **Standard Surface Panel:** `#161b22` — Default card / panel foundation.
- **Radial Cosmic Gradient:** `radial-gradient(circle at center, #0a0f1f 0%, #050812 60%, #000000 100%)`.

#### Luminous Sephirah Accents & Tooltips
- **Sephirah Ice-Cyan:** `#c8f8ff` — Ethereal highlight and high-contrast text accent.
- **Sephirah Translucent Glass:** `rgba(0, 232, 255, 0.08)` — Subtle frosted badge background.
- **Sephirah Ambient Glow:** `rgba(0, 232, 255, 0.25)` — Multi-layer box shadow and text glow.
- **Tooltip Backdrop:** `rgba(0, 0, 0, 0.7)` with `1px solid rgba(255, 255, 255, 0.1)` border and `backdrop-filter: blur(4px)`.

#### 🌌 Core EIGEN & 10 Sephirah Tree of Life Tokens
- **EIGEN Spectrum:**
  - `cyan`: `#00e8ff` (0x00e8ff) — Primary Electric Cyan
  - `sky`: `#14b5ff` (0x14b5ff) — Electric Sky Blue
  - `blue`: `#3a98ff` (0x3a98ff) — Vibrant Cobalt Blue
  - `purple`: `#7952f5` (0x7952f5) — Deep Cosmic Purple
- **10 Sephirah Tree of Life Nodes:**
  - `0️⃣ Keter (Crown):` `#fff9d6` — Divine White-Gold
  - `1️⃣ Chokhmah (Wisdom):` `#00ffff` — Pure Cyan
  - `2️⃣ Binah (Understanding):` `#00e8ff` — Electric Cyan
  - `3️⃣ Chesed (Mercy):` `#14b5ff` — Sky Blue
  - `4️⃣ Gevurah (Severity):` `#0070eb` — Deep Royal Blue
  - `5️⃣ Tiferet (Beauty):` `#ffd94a` (label `#4cc9f0`) — Radiant Gold / Solar Center
  - `6️⃣ Netzach (Victory):` `#7952f5` — Electric Purple
  - `7️⃣ Hod (Splendor):` `#5e17eb` — Deep Violet
  - `8️⃣ Yesod (Foundation):` `#ff66b3` — Hot Pink / Astral Magenta
  - `9️⃣ Malkuth (Kingdom):` `#038b00` — Deep Emerald Earth Green

#### ADHD Semantic High-Contrast Spectrum
- **Primary Cyan / Electric Blue (`#00e8ff` / `#14b5ff`):** Interactive focal points, active states, primary variables.
- **Secondary Violet (`#7952f5` / `#9b7dff`):** Structural markers, navigation layers, functions, subsections.
- **Tertiary Neon Green (`#22f792` / `#10b981`):** Success metrics, verified states, STEM/tech indicators, math constants (`#00f5db`).
- **Quaternary Coral / Amber (`#f78166` / `#ff783d`):** Warnings, dynamic parameters, auxiliary data, high-attention flags.
- **Pernary Hot Pink (`#ec4899` / `#ff40a1`):** Special modes, accents, and producer overrides.

---

### 🐍 2. Python (Matplotlib, Pyplot & Seaborn) Recipes

Import and apply the centralized styling utilities from `boilerplates/python/visualization_boilerplate.py`:

```python
import matplotlib.pyplot as plt
import numpy as np
from boilerplates.python.visualization_boilerplate import (
    THEME_TOKENS,
    HIGH_CONTRAST_CYCLE,
    apply_cosmic_theme,
    apply_theme,
    plot_eigenscribe_heatmap,
)

# 1. Activate Cosmic Deep Void Theme
apply_cosmic_theme(seaborn=True)

# 2. Render High-Contrast Trajectories
x = np.linspace(0, 10, 200)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(x, np.sin(x), color=THEME_TOKENS["sephirah_cyan"], linewidth=2.2, label="Sephirah Phase $\\theta(t)$")
ax.plot(x, np.cos(x) * 0.75, color=THEME_TOKENS["primary"], linewidth=2.0, label="Carrier Signal")
ax.set_title("Cosmic Trajectory Dynamics", fontsize=12, fontweight="bold", pad=12)
ax.legend(framealpha=0.85)
plt.tight_layout()
plt.show()

# 3. Render Deep Cosmic Heatmap Matrix
matrix = np.random.default_rng(42).uniform(0, 1, size=(10, 10))
fig_heat, ax_heat = plt.subplots(figsize=(6, 5))
plot_eigenscribe_heatmap(
    matrix,
    style="cosmic_sephirah",
    ax=ax_heat,
    title="Cosmic Sephirah Coherence Matrix",
    cbar_label="Intensity Level",
)
plt.tight_layout()
plt.show()
```

---

### 📊 3. Plotly & Dash Dashboard Recipes

```python
from boilerplates.python.visualization_boilerplate import (
    COLOR_BG_COSMIC,
    COLOR_SEPHIRAH_CYAN,
    COLOR_TEXT_BRIGHT,
    COLOR_TEXT_MUTED,
    create_plotly_base_figure,
)

fig = create_plotly_base_figure("Cosmic Phase Dashboard", height=380)
fig.update_layout(
    plot_bgcolor="rgba(10, 15, 31, 0.85)",
    paper_bgcolor="rgba(0, 0, 0, 0)",
    font=dict(color=COLOR_TEXT_MUTED, family="Aclonica, sans-serif"),
)
```

---

### 🌐 4. CSS Glassmorphism & Sephirah Component Reference

All web layouts and dashboards must follow the 4-layer taxonomy defined in `house-rules/css-rules.md` and `boilerplates/css/tse-boilerplate.css`:

```css
/* Deep Cosmic Radial Canvas */
.cosmic-canvas, body.cosmic-theme {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(
    circle at center,
    #0a0f1f 0%,
    #050812 60%,
    #000000 100%
  );
  font-family: 'Aclonica', sans-serif;
}

/* Glassmorphic Floating Tooltip */
#tooltip, .tooltip-glass {
  position: absolute;
  color: #ffffff;
  background: rgba(0, 0, 0, 0.7);
  padding: 6px 10px;
  border-radius: 6px;
  font-family: 'Aclonica', sans-serif;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease;
  z-index: 1000;
  font-size: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(4px);
}

/* ✨ Sephirah Luminous Labels ✨ */
@keyframes shimmer {
  0% { filter: brightness(1); }
  50% { filter: brightness(1.35); }
  100% { filter: brightness(1); }
}

.sephirah-label {
  position: absolute;
  color: #c8f8ff;
  font-family: "Aclonica", sans-serif;
  font-size: 14px;
  letter-spacing: 1px;
  text-align: center;
  pointer-events: none;
  user-select: none;
  padding: 4px 10px;
  border-radius: 14px;
  backdrop-filter: blur(4px);
  background: rgba(0, 232, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.08);
  text-shadow:
    0 0 5px currentColor,
    0 0 10px currentColor,
    0 0 20px currentColor;
  box-shadow:
    0 0 8px rgba(0, 232, 255, 0.25),
    inset 0 0 8px rgba(255, 255, 255, 0.04);
  transform: translate(-50%, -50%);
  z-index: 10;
  animation: shimmer 4s infinite ease-in-out;
}
```

---

### 💻 5. CLI 256-Color & ANSI Palettes

Use `boilerplates/python/cli_style_boilerplate.py` for terminal color formatting:

- `eigen_cosmic_navy` (ANSI 17)
- `eigen_cosmic_void` (ANSI 16)
- `eigen_sephirah_cyan` (ANSI 123 / `#c8f8ff`)
- `eigen_cyan` (ANSI 51)
- `eigen_purple` (ANSI 129)
- `eigen_green_bright` (ANSI 41)
