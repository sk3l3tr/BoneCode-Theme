---
name: BoneCode
description: Two native VS Code themes combining BoneCode branding with the BoneVim palette.
colors:
  dark-editor: "#000000"
  dark-text: "#FFF3C4"
  dark-surface: "#160F1D"
  dark-raised: "#1C1226"
  dark-border: "#483057"
  dark-bone: "#FFE878"
  dark-violet: "#B565F5"
  dark-blue: "#91BDF5"
  dark-mint: "#A3DEC7"
  dark-comment: "#9586A6"
  dark-selection: "#291833"
  light-editor: "#FAF7F0"
  light-text: "#30243F"
  light-surface: "#F0EBF4"
  light-raised: "#FFFCF5"
  light-border: "#CCBED7"
  light-bone: "#815600"
  light-violet: "#7431A8"
  light-blue: "#265C99"
  light-mint: "#256349"
  light-comment: "#74647B"
  light-selection: "#F1E9F3"
---

# BoneCode theme design

## Overview

Mode: Operate. VS Code controls the layout and typography. This package builds on the established BoneCode/BoneVim identity through native theme colors, without rebuilding the interface.

**Key Characteristics:**

- Dark uses pure black, as explicitly requested.
- Light adjusts accent brightness to maintain readability against ivory backgrounds.
- Syntax color roles remain consistent across both variants.

## Colors

Bone yellow identifies functions and activity; violet identifies keywords and focus. Blue marks types, and mint green marks strings. Text retains a warm tone. Errors, warnings, and informational messages use colors distinct from the brand accents. Selections and search results use subtle backgrounds that keep text readable. Values for both variants are defined in the frontmatter and the installable JSON files.

**The Semantic Continuity Rule.** Each color family keeps its role across both variants; Light adjusts brightness to preserve readability.

## Typography

Fonts, text size, and line height are controlled by VS Code and the user's settings. The theme only adds italic comments, Markdown emphasis, and strikethrough for deprecated semantic tokens.

## Layout

The layout, panels, density, and responsive behavior are native to VS Code; the extension does not define a new layout.

## Elevation & Depth

Eggplant surfaces in Dark and lavender surfaces in Light, along with borders and raised surfaces, create separation. `widget.shadow` is the native shadow color; the theme does not add window blur, desktop transparency, or glow effects.

## Components

Primary buttons use a violet background, dark text in Dark, and white text in Light, with a dedicated hover state. Native controls retain their geometry. Focus indicators, active tabs, and active panels use violet; the cursor and functions use the bone accent. Git states, diagnostics, and the ANSI terminal have their own colors.

The tests in `tests/validate.py` check the manifest, color values, tokens, and text contrast against editor, selection, search, occurrence-highlight, and diff backgrounds, including alpha compositing. Minimum syntax contrast against the editor background is 6.14:1 in Dark and 5.10:1 in Light. The final VSIX was installed and listed in an isolated VS Code profile; the regular profile was left untouched.

`BoneCode-preview.html` is an illustrative preview. There is no actual VS Code screenshot: the Playwright check was denied. Grammars and language servers determine which token each word receives; this document does not certify the actual token assignments in every language.

## Do's and Don'ts

### Do

- Keep color roles consistent between Dark and Light.
- Check contrast against composited selection, search, and diff backgrounds.
- Use only native VS Code colors and contributions.

### Don't

- Attribute font size, icons, or interface geometry to the theme.
- Present the HTML preview as a VS Code screenshot.
