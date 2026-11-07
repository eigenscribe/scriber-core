# 🏅 Gold Standard CSS House Rules & Design System ("The Scriber Experience")

This document defines the architectural standards, token hierarchy, and aesthetic signature for all web properties, apps, dashboards, and tools across **The Scriber Experience** and **Scriber Labs**.

---

## 🧭 Architectural Philosophy: The Conceptual Story Flow

Following the Eigenscribe architectural standard (*"What exists → what you're allowed to call → how it works → proof it works"*), our CSS stylesheets and systems strictly follow a structured, predictable 4-layer taxonomy:

```
0️⃣ What Exists              -> Layer 1: CSS Custom Properties & Design Tokens (Primitives & Semantics)
1️⃣ What You're Allowed to Call -> Layer 2: Base Element Resets & Normalize
2️⃣ How It Works             -> Layer 3: Layout Scaffolding (Grid, Flexbox, Golden Ratio Spacing)
3️⃣ Proof It Works           -> Layer 4: Core Reusable Component Classes (Cards, Buttons, Inputs, Code-Blocks)
```

>[!important] 👍 Rule of Thumb
> When someone scrolls a stylesheet top-to-bottom, semantic tokens define the universe first, resets establish baseline invariants, layout primitives position the flow, and components provide self-contained visual interactions.

---

## 🗝️ Key Features & ADHD Cognitive Load Architecture

1. **Number-Emoji Sectioning:**
   - Used as strict semantic anchors (`/* 0️⃣ ... */`, `/* 1️⃣ ... */`, `/* 2️⃣ ... */`, `/* 3️⃣ ... */`) across all stylesheets for rapid scannability and mental mapping.
2. **ADHD Cognitive Load Management & Semantic Color Hierarchies:**
   - Visual complexity is mitigated through high-contrast, structured, and predictable color coding.
   - Variable types, hierarchy levels, data states, and terminal/CLI logs must adhere to explicit color roles:
     - **Primary Cyan / Bright Blue (`#00e8ff` / `#14b5ff`):** Interactive focal points, primary controls, standard variables, and active states.
     - **Secondary Purple / Violet (`#7952f5` / `#9b7dff`):** Structural markers, navigation layers, functions, and subsections.
     - **Tertiary Neon Green (`#22f792` / `#38b000`):** Success metrics, verified states, STEM/tech indicators, and math constants.
     - **Quaternary Amber / Coral Orange (`#f78166` / `#ff783d`):** Warnings, dynamic parameters, auxiliary data, and high-attention highlights.
     - **Pernary Vibrant Pink / Magenta (`#ec4899` / `#ff40a1`):** Special modes, accents, and producer overrides.
3. **Golden Ratio Scaling ($\phi \approx 1.618$):**
   - Applied for typography scale steps, component proportions, and transition intervals (e.g., `61.8%` gradient stops, `1.618rem` rhythmic spacing) when it reinforces visual balance without sacrificing readability or mobile responsiveness.
4. **The Scriber Glassmorphism Baseline & Cosmic Void Palette:**
   - Dark mode first (`#0d1117` / `#161b22`), deep cosmic void radial gradients (`radial-gradient(circle at center, #0a0f1f 0%, #050812 60%, #000000 100%)`), layered with `rgba(0, 0, 0, 0.5)` to `rgba(22, 27, 34, 0.75)` frosted glass backdrops (`backdrop-filter: blur(12px)`), crisp light borders (`rgba(255, 255, 255, 0.1)`), and luminous ice-cyan specular highlights (`#c8f8ff`, `rgba(0, 232, 255, 0.30)` glow).
5. **EIGEN Spectrum & Vibrant 10-Node Architecture:**
   - Core EIGEN Palette: Cyan (`#00e8ff`), Sky (`#14b5ff`), Blue (`#3a98ff`), Purple (`#7952f5`).
   - Vibrant 10 Nodes: Node 0 (`#fff9d6`), Node 1 (`#00ffff`), Node 2 (`#00e8ff`), Node 3 (`#14b5ff`), Node 4 (`#0070eb`), Node 5 (`#ffd94a`), Node 6 (`#7952f5`), Node 7 (`#5e17eb`), Node 8 (`#ff66b3`), Node 9 (`#00c853`).

---

## 📐 Token Layers & Taxonomy

### Layer 1: CSS Custom Properties & Tokens
- **Color System:**
  - Dark surface foundations (`--color-bg: #0d1117`, `--color-surface: #161b22`, `--color-surface-elevated: #21262d`).
  - Deep cosmic void radial foundations (`--color-bg-cosmic-center: #0a0f1f`, `--color-bg-cosmic: #050812`, `--color-bg-cosmic-void: #000000`, `--gradient-cosmic-radial`).
  - Text hierarchy (`--color-text: #f0f6fc`, `--color-text-muted: #8b949e`, `--color-text-accent: #c8f8ff`, `--color-luminous-cyan: #c8f8ff`).
  - Luminous cosmic and tooltip tokens (`--color-cosmic-bg: rgba(0, 232, 255, 0.08)`, `--color-cosmic-glow: rgba(0, 232, 255, 0.30)`, `--color-tooltip-bg: rgba(0, 0, 0, 0.75)`).
  - Extended translucent glass tokens (`--color-glass-indigo`, `--color-glass-purple`, `--color-glass-violet`, `--color-glass-cyan`, `--color-glass-blue`).
  - 4-Color Vibrant Accent Markers (`--color-accent-green: #38fe52`, `--color-accent-blue: #3881fe`, `--color-accent-magenta: #fe38e4`, `--color-accent-amber: #feb538`).
  - 5-Stop Sequential Ramps (`--ramp-green-0..4`, `--ramp-blue-0..4`, `--ramp-purple-0..4`, `--ramp-magenta-0..4`).
  - Vibrant signatures & multi-stop gradients (`--gradient-0` through `--gradient-8`, `--gradient-synthwave`, `--gradient-sunset-soft`, `--gradient-eigenscribe`, `--gradient-multi`, `--gradient-cyan-to-blue`, `--gradient-blue-to-purple`, `--gradient-cosmic-radial`).
- **Typography Tokens:**
  - Display/Headings: `'Aclonica', sans-serif`
  - Body/Editorial: `'Merriweather', Georgia, serif`
  - Monospace/Code/Math: `'Fira Code', monospace`
- **Spacing & Golden Ratio Tokens:**
  - `--space-xs: 0.382rem` ($\phi^{-2}$)
  - `--space-sm: 0.618rem` ($\phi^{-1}$)
  - `--space-md: 1.000rem` ($1.0$)
  - `--space-lg: 1.618rem` ($\phi^1$)
  - `--space-xl: 2.618rem` ($\phi^2$)
  - `--space-2xl: 4.236rem` ($\phi^3$)
- **Depth & Shadows:**
  - Layered elevation with translucent colored glows (`--shadow-glow-cyan`, `--shadow-glow-purple`, `--shadow-glow-cosmic`).

### Layer 2: Base Element Resets
- Standard `box-sizing: border-box` across `*`, `*::before`, `*::after`.
- Baseline typography smoothing (`-webkit-font-smoothing: antialiased`).
- Contrast-preserving focus rings (`:focus-visible`).
- Accessible media and responsive text scaling.

### Layer 3: Layout Scaffolding
- Modern Grid & Flexbox utility constructs (`.grid`, `.grid-cols-2`, `.grid-cols-3`, `.flex`, `.flex-col`, `.items-center`, `.justify-center`).
- Fluid containers with max-width bounds (`.container`, `.max-w-5xl`, `.max-w-7xl`).
- Golden ratio layout divisions (`.layout-golden`).

### Layer 4: Core Reusable Components
- **Buttons (`.btn`, `.btn-primary`, `.btn-secondary`, `.btn-eigenscribe`, `.btn-glass`):**
  - Smooth multi-stop gradients with `background-size: 300% 100%`.
  - Specular hover translation (`transform: translateY(-2px)`), radiant box-shadow expansions, and distinct active press feedback.
- **Glassmorphic Cards & Tooltips (`.card`, `.card-glass`, `#tooltip`, `.tooltip-glass`):**
  - Subtle borders, frosted backgrounds, ambient glow borders on hover, and high-z-index informational tooltips.
- **✨ Cosmic Luminous Labels & Shimmer (`.cosmic-label`, `.eigen-label`, `@keyframes shimmer`):**
  - Center-projected coordinate markers with frosted backgrounds (`rgba(0, 232, 255, 0.08)`), multi-layer text shadows, ambient glow box-shadows, and 4s infinite shimmer breathing animations.
- **Text Gradients & Animations (`.gradient-text`, `.gradient-text-animated`, `.gradient-shift`):**
  - Multi-stop color flows clipped with `-webkit-background-clip: text` and animated shifting keyframes.
- **Forms & Inputs (`.input`, `.textarea`, `.select`):**
  - High-contrast inputs with frosted backgrounds and vibrant cyan/purple focus outlines.
- **Code Blocks & Math (`.code-block`, `.code-inline`, `.math-display`):**
  - Custom scrollbars, glassmorphic container headers, monospaced typography, and syntax accent colors.

---

## 🌐 Cross-Context Utility Mapping

The tokens and rules in `tse-boilerplate.css` map directly across diverse application targets:

| Context | Implementation Strategy | Key Tokens / Classes |
| :--- | :--- | :--- |
| **Web Portfolios & Landing Pages** | Direct inclusion of `tse-boilerplate.css`. Glassmorphic navbars, cards, and animated text headers. | `.navbar-glass`, `.hero-title`, `.btn-eigenscribe`, `.card-glass` |
| **Data Apps (Dash / Streamlit)** | Inject custom CSS or map tokens to `config.toml` (Streamlit) or `assets/style.css` (Dash). | `--color-bg`, `--color-surface`, `--color-primary`, `.dash-graph-container` |
| **Mermaid Diagrams** | Configure theme variables in Mermaid initialization (`theme: 'base'`, `themeVariables`). | `primaryColor: #14b5ff`, `primaryTextColor: #ffffff`, `lineColor: #00e8ff` |
| **Python Matplotlib / Pyplot** | Apply the companion Pyplot stylesheet / `rcParam` dictionary reflecting the eigenscribe color cycle. | `axes.facecolor: '#161b22'`, `figure.facecolor: '#0d1117'`, `axes.prop_cycle: ['#14b5ff', '#9b7dff', '#22f792', '#f78166']` |
| **Custom CLI Interfaces** | Rich / ANSI color formatting matching ADHD variable states. | `cyan: #00e8ff`, `blue: #14b5ff`, `magenta: #ec4899`, `green: #22f792`, `yellow: #f78166` |

---

## ⚡ Golden Rules for Maintainers

1. **Keep Definitions Flat and Highly Modular:** Never nest deeply; avoid overly specific monolithic blocks.
2. **Never Break High-Contrast Legibility:** Backgrounds must stay dark and rich (`#0d1117` base); text must remain crisp (`whitesmoke` / `#f0f6fc` or `#c5f8ff`).
3. **Preserve Micro-Interaction Polish:** All interactive state changes should leverage smooth easing (`transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)` or `0.4s ease-in-out`).
