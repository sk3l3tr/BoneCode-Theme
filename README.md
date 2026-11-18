# BoneCode

Author: **SK3L3T0R**.

Two original Visual Studio Code themes inspired by the local BoneVim palette.

- **BoneCode Dark**: a pure black editor, eggplant panels, bone-yellow functions, violet keywords, blue types, and mint-green strings.
- **BoneCode Light**: an ivory background and lavender panels, with deeper shades that preserve the same color roles and maintain contrast.

Includes colors for the interface, TextMate syntax, semantic tokens, the ANSI terminal, Git, diffs, diagnostics, search results, and selections. Each language's syntax highlighting depends on its grammar and the tokens provided by its language server.

## Installation

1. Download `bonecode-themes-1.0.1.vsix`.
2. In VS Code, open **Extensions** (`Ctrl+Shift+X`), select **… → Install from VSIX…**, and choose the file.
3. Open **Preferences: Color Theme** (`Ctrl+K`, then `Ctrl+T`) and choose **BoneCode Dark** or **BoneCode Light**.

You can also install it from the terminal using the path where you saved the file:

```sh
code --install-extension ./bonecode-themes-1.0.1.vsix
```

Installation adds both themes. To select one manually in `settings.json`:

```jsonc
{
  "workbench.colorTheme": "BoneCode Dark"
}
```

## Follow the system appearance

These settings are optional. Merge them into your existing configuration:

```jsonc
{
  "window.autoDetectColorScheme": true,
  "workbench.preferredDarkColorTheme": "BoneCode Dark",
  "workbench.preferredLightColorTheme": "BoneCode Light"
}
```

## Customization

The editable theme files are in `themes/`. No JavaScript build is required.

To adjust colors without modifying the extension, use theme-specific overrides:

```jsonc
{
  "workbench.colorCustomizations": {
    "[BoneCode Dark]": {
      "editorCursor.foreground": "#FFE878"
    },
    "[BoneCode Light]": {
      "editorCursor.foreground": "#815600"
    }
  }
}
```

If colors look unexpected, check for existing overrides in `workbench.colorCustomizations`, `editor.tokenColorCustomizations`, and `editor.semanticTokenColorCustomizations`. To inspect a specific token, use **Developer: Inspect Editor Tokens and Scopes**. Icons, fonts, and text size are configured separately.

## Design choices

| Role | Dark | Light |
|---|---|---|
| Editor | `#000000` | `#FAF7F0` |
| Text | `#FFF3C4` | `#30243F` |
| Functions / bone accent | `#FFE878` | `#815600` |
| Keywords / violet | `#B565F5` | `#7431A8` |
| Types / blue | `#91BDF5` | `#265C99` |
| Strings / green | `#A3DEC7` | `#256349` |
| Comments | `#9586A6` | `#74647B` |

BoneVim provides the palette and syntax color roles. Glass UI inspired the clear separation between surfaces; Cyberpunk, the contrast between dark surfaces and accents; and Kaolin, the soft, light backgrounds. These are visual references; no code was copied from those themes. BoneCode is a declarative theme extension with no executable code or runtime dependencies. It does not add window transparency, injected CSS, or glow effects.

The publisher ID `SK3L3T0R` identifies the local package. It does not imply a registered Marketplace account or a published listing.

## Validation and packaging

```sh
python3 tests/validate.py
npx --yes @vscode/vsce package --no-dependencies --allow-missing-repository
```

The VSIX contains only the manifest, both themes, the BoneCode icon, this documentation, and the license. Tests, design notes, and samples are excluded from the installable package.

## References

- [Official VS Code color theme guide](https://code.visualstudio.com/api/extension-guides/color-theme)
- [Theme colors](https://code.visualstudio.com/api/references/theme-color)
- [Semantic tokens](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)
- [Installing from a VSIX](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_install-from-a-vsix)
- [Glass UI](https://github.com/AregGhazaryan/GlassUI-VScode)
- [Cyberpunk](https://github.com/prometheux-ar/cyberpunk)
- [Kaolin](https://github.com/zed-nait/kaolin-vscode-themes)
