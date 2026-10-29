#!/usr/bin/env bash
# EigenScribe — Sublime Text Package Installer (Bash)
# ============================================================
# Installs the EigenScribe theme, color scheme, syntax definitions,
# and PreTeXt snippets into your Sublime Text Packages directory.
#
# Usage:
#   ./install.sh            # Copy install (default)
#   ./install.sh symlink    # Symlink install (recommended for dev)
#   ./install.sh uninstall  # Remove the package
#
# NOTE: If your repo lives inside this project and you want edits to
#       instantly appear in Sublime Text, use "symlink" mode.

set -euo pipefail

# Detect OS and locate Sublime Text Packages directory
if [[ "$OSTYPE" == "darwin"* ]]; then
    PACKAGES_DIR="$HOME/Library/Application Support/Sublime Text/Packages/User"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PACKAGES_DIR="$HOME/.config/sublime-text/Packages/User"
else
    echo "[EigenScribe] Unsupported OS: $OSTYPE" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_SOURCE="$SCRIPT_DIR/EigenScribe"
TARGET="$PACKAGES_DIR/EigenScribe"

if [[ "${1:-}" == "uninstall" ]]; then
    # Remove symlink or copied directory
    if [[ -L "$TARGET" ]]; then
        rm "$TARGET"
        echo "[EigenScribe] Symlink removed from: $TARGET"
    elif [[ -d "$TARGET" ]]; then
        rm -rf "$TARGET"
        echo "[EigenScribe] Package removed from: $TARGET"
    else
        echo "[EigenScribe] Package not found at: $TARGET"
    fi
    exit 0
fi

# Verify source exists
if [[ ! -d "$PACKAGE_SOURCE" ]]; then
    echo "[EigenScribe] Error: Package source not found at: $PACKAGE_SOURCE" >&2
    exit 1
fi

# Create Packages directory if needed
mkdir -p "$PACKAGES_DIR"

if [[ "${1:-}" == "symlink" ]]; then
    # ─── SYMLINK MODE (recommended for development) ───
    # Edits to the repo instantly appear in Sublime Text
    if [[ -L "$TARGET" || -d "$TARGET" ]]; then
        echo "[EigenScribe] Removing existing installation at: $TARGET"
        rm -rf "$TARGET"
    fi
    ln -s "$PACKAGE_SOURCE" "$TARGET"
    INSTALL_TYPE="Symlinked"
else
    # ─── COPY MODE (default) ───
    if [[ -d "$TARGET" ]]; then
        echo "[EigenScribe] Overwriting existing installation at: $TARGET"
        rm -rf "$TARGET"
    fi
    cp -r "$PACKAGE_SOURCE" "$TARGET"
    INSTALL_TYPE="Copied"
fi

echo ""
echo "============================================"
echo " EigenScribe Package $INSTALL_TYPE!"
echo "============================================"
echo ""
echo "Source:  $PACKAGE_SOURCE"
echo "Target:  $TARGET"
echo ""
echo "Next steps:"
echo "  1. Restart Sublime Text"
echo "  2. Open Preferences -> Settings and add:"
echo '     "theme": "EigenScribe/EigenScribe.sublime-theme",'
echo '     "color_scheme": "Packages/EigenScribe/color-schemes/EigenScribe.sublime-color-scheme"'
echo ""
echo "  3. Install required fonts (if not already):"
echo "     - Aclonica  (https://fonts.google.com/specimen/Aclonica)"
echo "     - Fira Code (https://github.com/tonsky/FiraCode)"
echo ""
