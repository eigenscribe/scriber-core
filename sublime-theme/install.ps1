# EigenScribe — Sublime Text Package Installer (PowerShell)
# ============================================================
# Installs the EigenScribe theme, color scheme, syntax definitions,
# and PreTeXt snippets into your Sublime Text Packages directory.
#
# Usage:
#   .\install.ps1          # Install to default location
#   .\install.ps1 -Uninstall  # Remove the package

param(
    [Switch]$Uninstall
)

$ErrorActionPreference = "Stop"

# Locate Sublime Text Packages directory
$packagesDir = Join-Path $env:APPDATA "Sublime Text\Packages\User"

if (-not (Test-Path $packagesDir)) {
    Write-Host "[EigenScribe] Creating Packages directory: $packagesDir" -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $packagesDir -Force | Out-Null
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$packageSource = Join-Path $scriptDir "EigenScribe"

if ($Uninstall) {
    # Remove the installed package
    $target = Join-Path $packagesDir "EigenScribe"
    if (Test-Path $target) {
        Remove-Item -Path $target -Recurse -Force
        Write-Host "[EigenScribe] Package removed from: $target" -ForegroundColor Yellow
    } else {
        Write-Host "[EigenScribe] Package not found at: $target" -ForegroundColor DarkGray
    }
    return
}

# Verify source exists
if (-not (Test-Path $packageSource)) {
    Write-Error "[EigenScribe] Package source not found at: $packageSource"
    exit 1
}

# Copy the entire EigenScribe package folder
$target = Join-Path $packagesDir "EigenScribe"
if (Test-Path $target) {
    Write-Host "[EigenScribe] Overwriting existing installation at: $target" -ForegroundColor Yellow
    Remove-Item -Path $target -Recurse -Force
}

Copy-Item -Path $packageSource -Destination $packagesDir -Recurse -Force

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " EigenScribe Package Installed!" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Location: $target" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Restart Sublime Text" -ForegroundColor Gray
Write-Host "  2. Open Preferences -> Settings and add:" -ForegroundColor Gray
Write-Host '     "theme": "EigenScribe/EigenScribe.sublime-theme",' -ForegroundColor Gray
Write-Host '     "color_scheme": "Packages/EigenScribe/color-schemes/EigenScribe.sublime-color-scheme"' -ForegroundColor Gray
Write-Host ""
Write-Host "  3. Install required fonts (if not already):" -ForegroundColor Gray
Write-Host "     - Aclonica  (https://fonts.google.com/specimen/Aclonica)" -ForegroundColor Gray
Write-Host "     - Fira Code (https://github.com/tonsky/FiraCode)" -ForegroundColor Gray
Write-Host ""
