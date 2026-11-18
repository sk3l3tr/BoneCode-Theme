"""Validate theme contracts and readable text without external dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            assert key not in result, f'Duplicate JSON key: {key}'
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique)


def luminance(color):
    rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    return sum((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) * w
               for x, w in zip(rgb, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    low, high = sorted((luminance(a), luminance(b)))
    return (high + 0.05) / (low + 0.05)


def composite(top, bottom):
    alpha = int(top[7:9], 16) / 255 if len(top) == 9 else 1
    return '#' + ''.join(f'{round(int(top[i:i+2], 16) * alpha + int(bottom[i:i+2], 16) * (1-alpha)):02X}'
                         for i in (1, 3, 5))


manifest = load(ROOT / 'package.json')
assert manifest['categories'] == ['Themes']
assert not any(key in manifest for key in ('main', 'browser', 'activationEvents', 'dependencies'))
themes = manifest['contributes']['themes']
assert [(t['label'], t['uiTheme']) for t in themes] == [('BoneCode Dark', 'vs-dark'), ('BoneCode Light', 'vs')]
report = {}
for entry in themes:
    path = (ROOT / entry['path']).resolve()
    assert path.is_relative_to(ROOT)
    t = load(path)
    c = t['colors']
    assert t['semanticHighlighting'] is True
    assert t['type'] == ('dark' if entry['uiTheme'] == 'vs-dark' else 'light')
    assert all(re.fullmatch(r'#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?', v) for v in c.values())
    for i in range(1, 7):
        assert f'editorBracketHighlight.foreground{i}' in c
    assert len([k for k in c if k.startswith('terminal.ansi')]) == 16
    assert len({c['editor'+s+'.foreground'] for s in ('Error', 'Warning', 'Info', 'Hint')}) == 4
    ratios = []
    for r in t['tokenColors']:
        value = contrast(r['settings']['foreground'], c['editor.background'])
        assert value >= 4.5, (entry['label'], r['name'], value)
        assert contrast(r['settings']['foreground'], c['editor.selectionBackground']) >= 4.5, (entry['label'], r['name'], 'selection')
        ratios.append(value)
        for key in ('editor.wordHighlightBackground', 'editor.wordHighlightStrongBackground',
                    'editor.wordHighlightTextBackground', 'editor.selectionHighlightBackground',
                    'editor.rangeHighlightBackground', 'editor.linkedEditingBackground'):
            assert contrast(r['settings']['foreground'], composite(c[key], c['editor.background'])) >= 4.5, (entry['label'], r['name'], key)
        for kind in ('inserted', 'removed'):
            base = composite(c[f'diffEditor.{kind}LineBackground'], c['editor.background'])
            effective = composite(c[f'diffEditor.{kind}TextBackground'], base)
            assert contrast(r['settings']['foreground'], effective) >= 4.5, (entry['label'], r['name'], kind)
    for bg, fg in [('editor.findMatchBackground', 'editor.findMatchForeground'),
                   ('editor.findMatchHighlightBackground', 'editor.findMatchHighlightForeground')]:
        assert contrast(c[fg], composite(c[bg], c['editor.background'])) >= 4.5, (entry['label'], bg)
    for key, rule in t['semanticTokenColors'].items():
        color = rule if isinstance(rule, str) else rule.get('foreground')
        if color:
            assert contrast(color, c['editor.background']) >= 4.5, (entry['label'], key)
            assert contrast(color, c['editor.selectionBackground']) >= 4.5, (entry['label'], key, 'selection')
    for fg, bg in [('editor.foreground','editor.background'),
                   ('descriptionForeground','sideBar.background'),
                   ('input.placeholderForeground','input.background'),
                   ('button.foreground','button.background'), ('badge.foreground','badge.background'),
                   ('statusBarItem.remoteForeground','statusBarItem.remoteBackground'),
                   ('editor.foreground','editor.selectionBackground'),
                   ('list.activeSelectionForeground','list.activeSelectionBackground'),
                   ('menu.selectionForeground','menu.selectionBackground')]:
        assert contrast(c[fg], c[bg]) >= 4.5, (entry['label'], fg, bg)
    report[entry['label']] = {'syntax_min_contrast': round(min(ratios), 2),
                             'editor_contrast': round(contrast(c['editor.foreground'], c['editor.background']), 2),
                             'workbench_colors': len(c)}
assert load(ROOT / themes[0]['path'])['colors']['editor.background'] == '#000000'
print(json.dumps({'ok': True, 'themes': report}, indent=2))
