# EigenScribe — Sublime Text Package

A **Sublime Text 4** package derived from the **EigenScribe / Scriber Labs** visual identity — the same cyan-to-purple gradient palette, glassmorphic dark surfaces, and **Aclonica** + **Fira Code** typography used across the project's web output, dashboards, and documentation.

---

## What's Included

| Component | File | Description |
|-----------|------|-------------|
| **Color Scheme** | `EigenScribe.sublime-color-scheme` | Syntax highlighting for 20+ languages |
| **UI Theme** | `EigenScribe.sublime-theme` | Glassmorphic dark UI for sidebar, tabs, panels, status bar |
| **Syntax** | `PreTeXt.sublime-syntax` | PreTeXt XML syntax highlighting with element awareness |
| **Snippets** | 7 PreTeXt snippets | Section, definition, theorem, proof, xref, inline math, display math |

---

## Package Structure

```
EigenScribe/
├── sublime-package.json              # Package manifest
├── color-schemes/
│   └── EigenScribe.sublime-color-scheme
├── themes/
│   └── EigenScribe.sublime-theme
├── syntaxes/
│   └── PreTeXt.sublime-syntax
└── snippets/
    ├── ptx-definition.sublime-snippet
    ├── ptx-math-display.sublime-snippet
    ├── ptx-math-inline.sublime-snippet
    ├── ptx-proof.sublime-snippet
    ├── ptx-section.sublime-snippet
    ├── ptx-theorem.sublime-snippet
    └── ptx-xref.sublime-snippet
```

---

## Color Palette Reference

The theme maps directly to the Eigenscribe CSS design tokens:

| Role | Hex | Token |
|------|-----|-------|
| Background | `#0d1117` | `--color-bg` |
| Surface / Panel | `#161b22` | `--color-surface` |
| Code block bg | `#1a1d24` | — |
| Primary cyan | `#14b5ff` | `--primary-color` |
| Bright cyan (accent) | `#00e8ff` | `--primary-color-light` |
| Primary purple | `#7952f5` | `--primary-purple` |
| Secondary purple | `#9b7dff` | `--secondary-color` |
| Magenta (strings) | `#ff75c3` | — |
| Green (variables) | `#00e000` | — |
| Bright green (decorators) | `#38fe52` | — |
| Yellow (types) | `#feb538` | — |
| Number purple | `#be58f9` | — |
| Pink (constants) | `#fe38e4` | — |
| Indigo (attributes) | `#6f78fa` | — |
| Comment blue | `#4c739c` | — |
| Text | `#C5F8FF` | `--color-text` |
| Muted text | `#8b949e` | `--color-muted` |

---

## Installation

### Quick Install

**Windows (PowerShell):**
```powershell
.\install.ps1
```

**macOS / Linux (copy install):**
```bash
chmod +x install.sh
./install.sh
```

**macOS / Linux (symlink — recommended for development):**
```bash
./install.sh symlink
```
When your repo is cloned on the same device as Sublime Text (e.g., a Raspberry Pi), use **symlink mode** — every edit or `git pull` instantly updates the theme in Sublime Text without re-installing.

Both scripts support uninstalling:
```powershell
.\install.ps1 -Uninstall
```
```bash
./install.sh uninstall
```

### Raspberry Pi Setup

If you're cloning this repo onto a Raspberry Pi and using Sublime Text there:

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USER/YOUR_REPO.git
cd YOUR_REPO/sublime-theme

# 2. Install as symlink (edits update instantly)
./install.sh symlink

# 3. Install required fonts
sudo apt install fonts-firacode
# Aclonica: download from https://fonts.google.com/specimen/Aclonica
#   then sudo cp Aclonica-Regular.ttf /usr/share/fonts/
#   and sudo fc-cache -f

# 4. Activate in Sublime Text Settings (see "Activate the Theme" below)
```

### Manual Install

1. Open Sublime Text → **`Tools → Command Palette`** → type **`Preferences: Browse Packages`**
2. Copy the entire `EigenScribe/` folder into the `Packages/User/` directory

**Default paths by OS:**

| OS | Path |
|----|------|
| Windows | `%APPDATA%\Sublime Text\Packages\User\` |
| macOS | `~/Library/Application Support/Sublime Text/Packages/User/` |
| Linux | `~/.config/sublime-text/Packages/User/` |

### Activate the Theme

Open **`Preferences → Settings`** and add to your user settings:

```json
{
  // EigenScribe Theme
  "theme": "EigenScribe/EigenScribe.sublime-theme",
  "color_scheme": "Packages/EigenScribe/color-schemes/EigenScribe.sublime-color-scheme",

  // Fonts
  "font_face": "Fira Code",
  "font_size": 14,

  // Optional: Enable ligatures for Fira Code
  "font_options": ["subpixel_antialias", "gray_antialias"],

  // UI preferences
  "caret_style": "block",
  "highlight_line": true,
  "highlight_modified_tabs": true,
  "draw_minimap_border": true,
  "indent_guide_options": ["draw_normal", "draw_active"],
  "fold_buttons": true,
  "match_brackets": true,
  "match_brackets_angle": true,
  "match_brackets_square": true,
  "match_brackets_curly": true,

  // Tab behavior
  "tab_size": 2,
  "translate_tabs_to_spaces": true,
  "trim_trailing_white_space_on_save": true,
  "auto_match_enabled": true
}
```

### Install Required Fonts

The theme uses two fonts that must be installed on your system:

1. **Aclonica** — UI elements (tabs, sidebar headers, buttons)
2. **Fira Code** — editor text (supports programming ligatures)

**Download:**
- [Aclonica](https://fonts.google.com/specimen/Aclonica)
- [Fira Code](https://github.com/tonsky/FiraCode)

---

## PreTeXt Syntax Highlighting

The included `PreTeXt.sublime-syntax` extends built-in XML with PreTeXt-specific element awareness. It automatically applies to `.ptx` files.

| PreTeXt Element | Color | Scope |
|-----------------|-------|-------|
| `<section>`, `<p>`, `<title>` | Cyan `#14b5ff` | `entity.name.tag` |
| `xml:id`, `ref` attributes | Indigo `#6f78fa` | `entity.other.attribute-name` |
| Attribute values `"..."` | Magenta `#ff75c3` | `string` |
| `<!-- comments -->` | Muted blue `#4c739c` | `comment` |
| `<?xml ...?>`, `<!DOCTYPE>` | Bright green `#38fe52` | `meta.tag.sgml` |

If `.ptx` files don't auto-detect, go to **`View → Syntax → Open All with Current Extension as... → PreTeXt`**.

---

## PreTeXt Snippets

| Trigger | Snippet | Description |
|---------|---------|-------------|
| `ptxsec` | `<section>` | Section with title, tags, and paragraph |
| `ptxdef` | `<definition>` | Definition with title and body |
| `ptxthm` | `<theorem>` | Theorem with title and statement |
| `ptxpf` | `<proof>` | Proof with body and QED symbol (∎) |
| `ptxxref` | `<xref>` | Cross-reference |
| `ptxm` | `<m>` | Inline math |
| `ptxme` | `<me>` | Display math |

---

## Recommended Keybindings

Add these to **`Preferences → Key Bindings`**:

```json
[
  // PreTeXt: Quick XML tag close
  { "keys": ["ctrl+shift+."], "command": "insert_snippet", "args": { "contents": "></${TM_SELECTED_TEXT:$1}>" } },

  // PreTeXt: Insert xml:id attribute
  { "keys": ["ctrl+alt+i"], "command": "insert_snippet", "args": { "contents": " xml:id=\"sec-${TM_SELECTED_TEXT:$1}\"" } },

  // PreTeXt: Insert xref
  { "keys": ["ctrl+alt+r"], "command": "insert_snippet", "args": { "contents": "<xref ref=\"${TM_SELECTED_TEXT:$1}\"/>" } },

  // PreTeXt: Insert math inline
  { "keys": ["ctrl+shift+m"], "command": "insert_snippet", "args": { "contents": "<m>${1:expression}</m>" } },

  // PreTeXt: Insert math display
  { "keys": ["ctrl+alt+m"], "command": "insert_snippet", "args": { "contents": "<me>\n    ${1:expression}\n</me>" } },

  // Toggle sidebar
  { "keys": ["ctrl+b"], "command": "toggle_side_bar" },

  // Toggle minimap
  { "keys": ["ctrl+shift+m"], "command": "toggle_minimap" }
]
```

---

## Recommended Packages

Install via **Package Control** (`Ctrl+Shift+P` → `Install Package`):

| Package | Purpose |
|---------|---------|
| **XMLTools** | Format and indent `.ptx` XML files |
| **Git** | Git integration in sidebar |
| **GitGutter** | Git change indicators in gutter |
| **SideBarEnhancements** | Extended sidebar context menu |
| **AutoFileName** | Auto-complete file paths |
| **BracketHighlighter** | Enhanced bracket matching |
| **TrailingSpaces** | Highlight trailing whitespace |
| **Color Highlighter** | Inline color previews in CSS |

---

## Glassmorphic Design Notes

The theme faithfully reproduces the glassmorphic aesthetic from the Eigenscribe CSS design system:

- **Background layers**: Deep dark `#0d1117` base with `#161b22` surface panels
- **Accent gradients**: Cyan `#14b5ff` → Purple `#7952f5` transitions on interactive elements
- **Border treatment**: Subtle `rgba(255, 255, 255, 0.08)` borders mimicking glass edges
- **Selection highlight**: Semi-transparent cyan `rgba(20, 181, 255, 0.20)`
- **Scrollbar**: Cyan gradient thumb
- **Font pairing**: Aclonica for UI headings, Fira Code for editor text

---

## Troubleshooting

### Theme not applying
- Ensure the `EigenScribe/` folder is inside `Packages/User/`
- Restart Sublime Text after installation
- Verify the paths in `Preferences → Settings` match exactly

### Fonts not rendering
- Install Aclonica and Fira Code system-wide
- Verify font names match exactly (check via OS font manager)
- On Windows, try `"Fira Code Regular"` if ligatures don't work

### Color scheme looks wrong
- Requires Sublime Text **Build 4000+** (color scheme v2 format)
- Check that no other color scheme plugin is overriding settings

---

## License

This package is provided as-is for personal and project use. The color palette is derived from the Eigenscribe / Scriber Labs CSS design tokens.
