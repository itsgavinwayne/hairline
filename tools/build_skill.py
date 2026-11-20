#!/usr/bin/env python3
"""生成给 AI 用的技能包 skills/hairline/。

    python3 tools/build_skill.py

SKILL.md 是手写的，这个脚本不动它；下面两个文件夹每次整个重建，不要手改：
- references/   规范、令牌表、每个组件的说明和可以直接抄的标记（中文在 references/，英文在 references/en/）
- assets/       dist/ 里的三个文件，原样拷一份，AI 可以直接放进使用者的项目

先运行 python3 build_site.py，保证 dist/ 是新的。
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import build_site as B  # noqa: E402

OUT = os.path.join(HERE, 'skills', 'hairline')
GUIDES = ['README', 'aesthetics', 'outputs', 'foundations', 'behavior', 'english', 'reading', 'print', 'imagery', 'seal', 'naming']
GUIDE_FILE = {'README': 'principles'}


def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text.rstrip('\n') + '\n')


def lead(readme):
    first = readme.strip().split('\n\n', 1)[0].strip()
    return '' if first.startswith(('#', '-', '|')) else ' '.join(first.split())


def tokens_md(t, en):
    L = (lambda zh, e: e if en else zh)
    out = ['# ' + L('令牌', 'Tokens'), '',
           L('每个令牌都是一个 CSS 变量，写出来是 `var(--hao-名字)`。颜色有昼夜两个值，跟着 `data-theme` 或系统设置切换。不要写散值，没有合适的令牌就先用最接近的。',
             'Every token is a CSS variable, written `var(--hao-name)`. Colors have a light and a dark value and follow `data-theme` or the system setting. Do not hard-code values; pick the closest token.'), '']
    names = [('color', L('颜色', 'Color')), ('spacing', L('间距', 'Spacing')), ('radius', L('圆角', 'Radius')), ('shadow', L('阴影', 'Shadow')),
             ('breakpoint', L('断点', 'Breakpoints')), ('layout', L('布局', 'Layout')), ('zIndex', L('层级', 'Layers')), ('opacity', L('不透明度', 'Opacity')), ('motion', L('动效', 'Motion'))]
    for key, title in names:
        fam = t.get(key)
        if not fam:
            continue
        out += ['## ' + title, '']
        if fam.get('note'):
            out += [fam['note'], '']
        themed = any(isinstance(x['value'], dict) for x in fam['tokens'])
        if themed:
            out += ['| %s | %s | %s | %s |' % (L('变量', 'Variable'), L('昼', 'Light'), L('夜', 'Dark'), L('用途', 'Use')), '| --- | --- | --- | --- |']
        else:
            out += ['| %s | %s | %s |' % (L('变量', 'Variable'), L('值', 'Value'), L('用途', 'Use')), '| --- | --- | --- |']
        for x in fam['tokens']:
            v, use = x['value'], x.get('usage', '').replace('|', '\\|')
            if themed:
                lt, dk = (v['light'], v['dark']) if isinstance(v, dict) else (v, v)
                out.append('| `--hao-%s` | `%s` | `%s` | %s |' % (x['name'], lt, dk, use))
            else:
                out.append('| `--hao-%s` | `%s` | %s |' % (x['name'], v, use))
        out.append('')
    out += ['## ' + L('字体', 'Type'), '',
            L('字体样式是类名，写出来是 `class="hao-名字"`。带 `-en` 的是英文界面用的那一级；在 `<html lang="en">` 下标题会自动换成英文的字号与字距。',
              'Type styles are classes, written `class="hao-name"`. Names ending in `-en` are the levels for English interfaces; under `<html lang="en">` headings switch to the English sizes and tracking on their own.'), '',
            '| %s | %s | %s | %s |' % (L('字体族', 'Family'), L('变量', 'Variable'), L('值', 'Value'), ''), '| --- | --- | --- | --- |']
    for k, v in t['type']['families'].items():
        out.append('| %s | `--hao-font-%s` | `%s` | |' % (k, k, v))
    out += ['', '| %s | %s | %s | %s | %s |' % (L('类名', 'Class'), L('字号 / 行高', 'Size / line height'), L('字重', 'Weight'), L('字体族', 'Family'), L('用途', 'Use')), '| --- | --- | --- | --- | --- |']
    for g in t['type']['groups']:
        for s in g['styles']:
            out.append('| `hao-%s` | %s / %s | %s | %s | %s |' % (s['name'], s['fontSize'], s['lineHeight'], s['fontWeight'], g['family'], s.get('usage', '').replace('|', '\\|')))
    return '\n'.join(out)


def main():
    tokens = json.loads(B.read(B.SRC, 'tokens.json'))
    tnames, cnames = B.token_names(tokens), B.type_names(tokens)
    fix = lambda s: B.prefix_classes(B.prefixed(s, tnames), cnames)
    comps = B.load_components()
    for d in ('references', 'assets'):
        shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)

    for en in (False, True):
        root = 'references/en/' if en else 'references/'
        B.LANG = 'en' if en else 'zh'
        src = os.path.join(B.SRC, 'en') if en else B.SRC
        for g in GUIDES:
            write(root + GUIDE_FILE.get(g, g) + '.md', B.read(src, g + '.md'))
        write(root + 'tokens.md', tokens_md(B.localized(tokens, json.loads(B.read(B.SRC, 'en', 'tokens.json'))) if en else tokens, en))
        index = ['# ' + ('Components' if en else '组件一览'), '',
                 ('Each row links to a file with the write-up and copy-ready markup. Open only the ones you need.' if en else '每行对应一个文件，里面是说明和可以直接抄的标记。用到哪个再打开哪个。'), '',
                 '| %s | %s | %s | %s |' % (('Group', 'Component', 'File', 'What it is') if en else ('分组', '组件', '文件', '是什么')), '| --- | --- | --- | --- |']
        for c in sorted(comps, key=lambda c: (B.GROUP_ORDER.index(c['group']) if c['group'] in B.GROUP_ORDER else 99, c['name'])):
            if c['name'].endswith('EN') and c['name'].startswith('Sample'):
                continue   # 英文示例屏并进对应的那一份
            readme = c['readme_en'] if en else c['readme']
            title = B.label(c) if en else c['zh']
            body = ['# %s%s' % (c['name'], '' if title == c['name'] else ' · ' + title), '', readme.strip(), '']
            panes = dict(c['panes'])
            twin = next((x for x in comps if x['name'] == c['name'] + 'EN'), None)
            if c['frame']:   # 示例屏和封面是整幅画面，标记就是整个 body
                panes = {'zh-CN': c['whole']}
                if twin:
                    panes['en'] = twin['whole']
            order = [('en', 'English'), ('zh-CN', 'Chinese' if en else '中文')] if en else [('zh-CN', '中文'), ('en', 'English')]
            got = [(n, panes[k]) for k, n in order if panes.get(k)]
            if got:
                body += ['## ' + ('Markup' if en else '标记'), '']
                for n, m in got:
                    body += ['### ' + n, '', '```html', fix(m), '```', '']
            if c['scripts']:
                body += ['## ' + ('Script used by this example' if en else '这个示例自己带的脚本'), '', '```html', fix(c['scripts']), '```', '']
            write(root + 'components/%s.md' % c['name'], '\n'.join(body))
            index.append('| %s | %s%s | `components/%s.md` | %s |' % (B.T(c['group']) if en else c['group'], c['name'], '' if title == c['name'] else ' ' + title, c['name'], lead(readme).replace('|', '\\|')))
        write(root + 'components.md', '\n'.join(index))
    B.LANG = 'zh'

    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    for f in ('hairline.css', 'hairline.js', 'tokens.json'):
        shutil.copyfile(os.path.join(B.DIST, f), os.path.join(OUT, 'assets', f))
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print('技能包已生成：%s，共 %d 个文件。' % (os.path.relpath(OUT, HERE), n))


if __name__ == '__main__':
    main()
