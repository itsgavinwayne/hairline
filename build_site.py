#!/usr/bin/env python3
"""从 source/ 生成两样东西，不需要安装任何依赖：

    python3 build_site.py           先核对令牌，再生成 dist/（给人拿去用的文件）和 site/（文档站）
    python3 build_site.py --check   只核对令牌和样式表，不生成

文档站出中文和英文两套页面：中文在 site/，英文在 site/en/，一页对一页。
英文稿放在 source/en/（规范、组件说明、令牌用途），缺哪一份就报错，不会用中文顶上。
脚本里写给读者看的中文都经过 T()，英文在 EN 这张表里；新加一句中文，就要在表里补一句英文。

source/ 里的变量不带前缀（--bg、--ink），因为线上的设计系统页面按令牌名直接生成变量。
dist/ 和 site/ 里的变量统一加 --hao- 前缀，放进别人的页面不会撞名。
"""
import html, json, os, re, shutil, sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'source')
OUT = os.path.join(HERE, 'site')
DIST = os.path.join(HERE, 'dist')
PREFIX = 'hao-'
HTML_NAMES = set()   # build() 里填上：所有令牌名
SITE_NAMES = set()   # 同上，去掉文档站自己定义的同名变量
SAMPLES = set()      # 同上：示例屏的页名（小写），目录按语言筛选时用
TYPE_NAMES = set()   # 字体样式的名字，会变成类名
STATIC = os.path.join(HERE, 'site-static')   # 原样拷进 site/assets 的文件：favicon、分享卡片
REPO_URL = 'https://github.com/itsgavinwayne/hairline'   # 开源仓库，顶栏右侧的 GitHub 图标链到这里
# GitHub 的标志，取自 GitHub 官方的 Octicons（mark-github，16 格）。品牌标志照原样用，不改形、不改比例
GITHUB_MARK = 'M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z'
SITE_URL = 'https://hairline.gavinwayne.com/'   # 网站的完整地址：分享卡片的图、规范链接、404 页的起点、llms.txt 里的地址都从这里来
FONTS = 'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;1,6..72,400&family=Noto+Serif+SC:wght@600;700;900&display=swap'

ZH = {'Accordion': '折叠面板', 'Avatar': '头像', 'Badge': '角标', 'Banner': '提示条', 'Bookmark': '书签', 'Breadcrumb': '面包屑', 'Button': '按钮', 'Calendar': '月历', 'Card': '卡片', 'Checkbox': '勾选框', 'Chip': '筛选标签', 'Cover': '封面', 'DateTile': '日历页', 'Dialog': '弹窗', 'Divider': '分隔线', 'EmptyState': '空状态', 'Fret': '回纹', 'Handscroll': '手卷', 'Icon': '图标', 'Link': '链接', 'ListGroup': '分组列表', 'Logo': '标志', 'Menu': '菜单', 'Motion': '进场动效', 'Mount': '装裱', 'NavBar': '导航栏', 'Pagination': '分页', 'Paper': '笺纸', 'Poster': '海报', 'Progress': '进度与加载', 'Prose': '长文', 'Quote': '引文', 'Radio': '单选', 'Rating': '梅花评分', 'SampleArticle': '文章页', 'SampleDashboard': '数据页', 'SampleForm': '表单页', 'SampleScreen': '首页', 'SampleScreenEN': '首页（英文）', 'SampleArticleEN': '文章页（英文）', 'SampleDashboardEN': '数据页（英文）', 'SampleFormEN': '表单页（英文）', 'SampleSettingsEN': '设置页（英文）', 'SampleSettings': '设置页', 'SampleWeb': '网页', 'SampleWebEN': '网页（英文）', 'Seal': '印章', 'SealGuide': '印面示意', 'SearchField': '搜索框', 'Segmented': '分段控件', 'Select': '下拉选择', 'Sheet': '底部弹层', 'Sidebar': '侧边栏', 'Slider': '滑块', 'Stamp': '盖印', 'Stat': '数字展示', 'Stepper': '步进器', 'Steps': '步骤条', 'Stitch': '针脚', 'Switch': '开关', 'TabBar': '标签栏', 'Table': '表格', 'Tabs': '标签页', 'Tag': '标签', 'TextField': '输入框', 'Timeline': '时间线', 'TitleSlip': '题签', 'Toast': '轻提示', 'Tooltip': '气泡提示', 'Upload': '上传', 'Verse': '竖排的诗', 'Crackle': '冰裂纹', 'Wave': '海水纹'}
GROUP_ORDER = ['图标', '纹样', '动效', '操作', '表单', '导航', '内容', '反馈', '浮层', '状态', '阅读', '平面', '品牌', '示例']
CATS = [('手册', ['开发指南']), ('基础', ['令牌', '图标', '纹样', '动效']), ('界面', ['操作', '表单', '导航', '内容', '反馈', '浮层', '状态']), ('阅读', ['阅读']), ('平面', ['平面']), ('品牌', ['品牌']), ('示例', ['示例'])]
CAT_OF = {g: c for c, gs in CATS for g in gs}
GUIDE_GROUPS = [('开始', ['install', 'quickstart']), ('原则', ['principles', 'aesthetics', 'outputs', 'references']), ('规范', ['foundations', 'behavior', 'english', 'reading', 'print', 'imagery', 'seal', 'naming'])]
SECTION = {'开始': 'guide', '原则': 'guide', '规范': 'guide', '令牌': 'tokens', '示例': 'ex'}
SEARCH = {'guide': '搜索指南', 'tokens': '搜索令牌', 'comp': '搜索组件', 'ex': '搜索示例'}
GUIDES = [('install', '安装', None), ('quickstart', '快速上手', None), ('principles', '设计原则', 'README.md'), ('behavior', '行为与脚本', 'behavior.md'), ('foundations', '网页与大屏', 'foundations.md'), ('english', '英文界面', 'english.md'), ('reading', '阅读与内容', 'reading.md'), ('print', '平面与印刷', 'print.md'), ('aesthetics', '审美标准与出处', 'aesthetics.md'), ('outputs', '产物分类', 'outputs.md'), ('imagery', '图形与素材', 'imagery.md'), ('seal', '印稿规范', 'seal.md'), ('references', '参考与取舍', 'references.md'), ('naming', '命名对照', 'naming.md')]
TOKENS = [('color', '色彩'), ('type', '字体'), ('space', '间距与圆角'), ('shadow', '阴影与层级')]

LANG = 'zh'          # 正在生成哪一种语言的页面，build() 里依次设成 zh、en
LANGS = ('zh', 'en')
# 英文页里组件的叫法。没列的按组件名拆词：DateTile → Date tile
EN_NAMES = {'Crackle': 'Ice crackle', 'Chip': 'Filter chip', 'Motion': 'Entrance motion', 'Mount': 'Mounting', 'NavBar': 'Navigation bar', 'Paper': 'Letter paper', 'Progress': 'Progress and loading', 'Prose': 'Long-form text', 'Rating': 'Plum-blossom rating', 'Segmented': 'Segmented control', 'Verse': 'Vertical verse', 'Wave': 'Wave pattern',
            'SampleScreen': 'Home screen (Chinese)', 'SampleScreenEN': 'Home screen', 'SampleArticle': 'Article page (Chinese)', 'SampleArticleEN': 'Article page', 'SampleDashboard': 'Dashboard (Chinese)', 'SampleDashboardEN': 'Dashboard', 'SampleForm': 'Form page (Chinese)', 'SampleFormEN': 'Form page', 'SampleSettings': 'Settings page (Chinese)', 'SampleSettingsEN': 'Settings page', 'SampleWeb': 'Web page (Chinese)', 'SampleWebEN': 'Web page'}
# 界面上写死的中文 → 英文。句首大写，不用全大写，不用感叹号，弯引号（见 source/english.md）
EN = {
    # 分组
    '手册': 'Guide', '开发指南': 'Guide', '指南': 'Guide', '基础': 'Foundations', '基础件': 'Foundations', '界面': 'Interface', '阅读': 'Reading', '平面': 'Print', '品牌': 'Brand', '示例': 'Examples', '令牌': 'Tokens', '组件': 'Components',
    '图标': 'Icons', '纹样': 'Patterns', '动效': 'Motion', '操作': 'Actions', '表单': 'Forms', '导航': 'Navigation', '内容': 'Content', '反馈': 'Feedback', '浮层': 'Overlays', '状态': 'Status', '其他': 'Other',
    '开始': 'Get started', '原则': 'Principles', '规范': 'Guidelines',
    '搜索指南': 'Find a guide', '搜索令牌': 'Find a token', '搜索组件': 'Find a component', '搜索示例': 'Find an example',
    # 指南与令牌的页名
    '安装': 'Install', '快速上手': 'Quick start', '设计原则': 'Design principles', '行为与脚本': 'Behavior and scripts', '网页与大屏': 'Web and large screens', '英文界面': 'English interfaces', '阅读与内容': 'Reading and content', '平面与印刷': 'Print and graphics', '审美标准与出处': 'Aesthetic standards and sources', '产物分类': 'Kinds of output', '图形与素材': 'Imagery and assets', '印稿规范': 'Seal design', '参考与取舍': 'References and trade-offs', '命名对照': 'Naming reference',
    '色彩': 'Color', '字体': 'Type', '间距与圆角': 'Spacing and radius', '阴影与层级': 'Shadow and layers',
    # 页面外壳
    '打开目录': 'Open contents', 'Hairline 首页': 'Hairline home', '主导航': 'Main', '切换昼夜主题': 'Switch between day and night', 'GitHub 上的源代码': 'Source code on GitHub', '全站目录': 'Site index', '目录': 'Contents', '文档目录': 'Pages',
    '界面基于毫（Hairline）设计系统': 'Built with the Hairline design system', '没有找到，换一个词试试。': 'Nothing matches. Try another word.',
    '本页内容': 'On this page', '上一页与下一页': 'Previous and next page', '上一页': 'Previous', '下一页': 'Next', '跳到正文': 'Skip to content',
    '毫 Hairline 设计系统': 'Hairline design system', ' · 毫 Hairline': ' · Hairline', '毫 Hairline': 'Hairline', '设计系统': 'Design system',
    '毫 Hairline：一套中英双语、昼夜两套主题的设计系统。': 'Hairline: a design system in Chinese and English, with day and night themes.',
    # 演示
    '在新窗口打开整页': 'Open full page', '看中文版': 'See the Chinese version', '看英文版': 'See the English version', '演示语言': 'Demo language', '复制代码': 'Copy code', '显示代码': 'Show code', '演示': 'Demo', '用法': 'Usage',
    # 令牌页
    '<h1>色彩</h1><p class="site-lead">所有颜色都是令牌，写成 <code>var(--名字)</code>。每个令牌有昼、夜两个值，下面色块显示的是当前主题的值，文字里依次是昼和夜。</p>': '<h1>Color</h1><p class="site-lead">Every color is a token, written as <code>var(--name)</code>. Each token has a day value and a night value. The swatch shows the value in the current theme, and the text gives day, then night.</p>',
    '<h1>字体</h1><p class="site-lead">标题用衬线（中文思源宋体，西文 Newsreader），正文和控件用黑体。每个样式都有一个同名的类，直接写在元素上。</p>': '<h1>Type</h1><p class="site-lead">Titles use serif: Noto Serif SC for Chinese, Newsreader for Latin. Text and controls use sans-serif. Each style has a class of the same name that goes straight on the element.</p>',
    '%s / %s，字重 %s': '%s / %s, weight %s',
    '<h1>间距与圆角</h1><p class="site-lead">间距走 4px 的格。圆角按元素大小分档，大容器套小元素时，里面的圆角比外面小一档。</p><h2>间距</h2>': '<h1>Spacing and radius</h1><p class="site-lead">Spacing follows a 4px grid. Radius steps up with the size of the element. When a large container holds a smaller element, the inner radius is one step smaller than the outer one.</p><h2>Spacing</h2>',
    '%s，%s': '%s, %s', '<h2>圆角</h2>': '<h2>Radius</h2>', '断点': 'Breakpoints', '布局': 'Layout', '层级': 'Stacking order', '不透明度': 'Opacity',
    '<th scope="col">令牌</th><th scope="col">值</th><th scope="col">用途</th>': '<th scope="col">Token</th><th scope="col">Value</th><th scope="col">Use</th>',
    '<h1>阴影与层级</h1><p class="site-lead">阴影只有三种，都很淡。能用留白和底色的差别分出层次时，不加阴影。</p>': '<h1>Shadow and layers</h1><p class="site-lead">There are only three shadows, and all of them are faint. When white space and a change of background can separate the layers, don’t add a shadow.</p>',
    # 首页
    '再盖一次印': 'Stamp the seal again', '朱砂一处': 'One touch of cinnabar', '一屏里红色只出现一次：一方印、一个角标、一个删除按钮、一次盖印，四者取一。': 'Red appears once per screen: a seal, a badge, a delete button, or a stamp. Pick one of the four.',
    '一屏一景': 'One scene per screen', '纹样、小品、装裱这类「景」，一屏至多一个。办事的页面一个都不放。': 'Patterns, vignettes, and mountings are scenes. A screen gets one at most. Task screens get none.',
    '月相进度，从朔到望': 'Moon-phase progress, from new moon to full moon', '形随控件': 'Shape follows the control', '进度是一轮渐圆的月，勾是一笔提勾。控件自己的形状可以有意味，但同类只用一种。': 'Progress is a waxing moon. A check is one upward hook stroke. A control’s own shape can carry meaning, but each kind of control gets only one.',
    '%d 个，从按钮到手卷。每个都有中文和英文两种效果。': '%d of them, from buttons to handscrolls. Each one is shown in Chinese and in English.', '浏览组件': 'Browse components', '没有这一页': 'This page isn’t here', '地址可能写错了，或者这一页已经搬走。可以在下面的目录里找。': 'The address may be mistyped, or the page has moved. Try the index below.', '回首页': 'Back to home', '保存修改': 'Save changes', '存为草稿': 'Save draft',
    '%d 个，1.5px 的圆头线。封闭的轮廓都留一个小缺口，叫「留气口」。': '%d icons, drawn with a 1.5px round-capped line. Every closed outline leaves a small opening, called the breathing gap.', '看全部图标': 'See all icons',
    '石青行事，朱砂点睛。每个颜色都有昼、夜两个值。': 'Azurite does the work. Cinnabar marks the point. Every color has a day value and a night value.', '看色彩令牌': 'See the color tokens',
    '标题用宋体，正文用黑体。英文另有一档标题样式。': 'Titles are set in serif, text in sans-serif. English has its own set of title styles.', '看字体样式': 'See the type styles',
    '个组件': 'components', '个图标': 'icons', '个文件': 'files',
    '数据页示例': 'Sample dashboard', '设置页示例，夜间主题': 'Sample settings page, night theme', '首页示例，夜间主题': 'Sample home screen, night theme', '文章页示例，夜间主题': 'Sample article page, night theme', '网页示例，中文': 'Sample web page, Chinese', '网页示例，英文': 'Sample web page, English',
    '页面内容': 'Your content', '令牌和全部组件的样式': 'Tokens and the styles for every component', '弹窗、菜单、月历等组件的行为': 'Behavior for dialogs, menus, the calendar, and more',
}


def T(s):
    """界面上的一句话：生成中文页时原样返回，生成英文页时查 EN。查不到就是漏翻，直接报错。"""
    return s if LANG == 'zh' else EN[s]


def label(c):
    """组件在页面上的叫法。"""
    if LANG == 'zh':
        return c['zh']
    return EN_NAMES.get(c['name']) or re.sub(r'(?<=[a-z])([A-Z])', lambda m: ' ' + m.group(1).lower(), c['name'])


def twin(name):
    """示例屏成对：SampleScreen 是中文的，SampleScreenEN 是英文的。返回另一种语言的那一张；不成对的返回 None。"""
    if not name.startswith('Sample'):
        return None
    return name[:-2] if name.endswith('EN') else name + 'EN'


def offlang(href):
    """这一页是不是另一种语言的示例屏。目录里只列当前语言的那一半，另一半从演示下面的链接过去。"""
    n = href[len('components/'):-len('.html')]
    if n not in SAMPLES:
        return False
    return (n.endswith('en') and n[:-2] in SAMPLES) != (LANG == 'en')   # 不能只看结尾：samplescreen 自己就以 en 结尾


def aroot(root):
    """到 site/ 根目录的相对路径：样式、脚本、预览页两种语言共用一份，英文页要多退一层。"""
    return root + ('../' if LANG == 'en' else '')


def read(*p):
    with open(os.path.join(*p), encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    if LANG == 'en' and rel.endswith('.html') and not rel.startswith('preview/'):
        rel = 'en/' + rel
    if rel.endswith('.html'):
        text = social(rel, prefix_classes(prefixed(text, HTML_NAMES), TYPE_NAMES))
    elif rel == 'assets/site.css':
        text = prefixed(text, SITE_NAMES)
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


# ---------- 给 AI 读的纯文本 ----------
def llms(nav, comps):
    """llms.txt：全站目录，一行一页，给 AI 找路用。llms-full.txt：规范和全部组件说明连成一份纯文本。
    中文的在站点根目录，英文的在 en/。地址在 SITE_URL 填上之前是相对的。"""
    en = LANG == 'en'
    base = (SITE_URL.rstrip('/') + '/' + ('en/' if en else '')) if SITE_URL else ''
    by = {c['name'].lower(): c for c in comps}

    def first(readme):
        t = readme.strip().split('\n\n', 1)[0].strip()
        return '' if t.startswith(('#', '-', '|')) else ' '.join(t.split())
    out = ['# ' + ('Hairline design system' if en else '毫 Hairline 设计系统'), '',
           '> ' + ('The restraint of iOS with a trace of Chinese character. Bilingual, light and dark, plain HTML and CSS; classes start with hao-, variables with --hao-. One stylesheet, one optional script, one token file.'
                   if en else 'iOS 的克制，加一点东方气韵。中英双语，昼夜两套主题，纯 HTML 和 CSS；类名以 hao- 开头，变量以 --hao- 开头。一份样式表、一份可选的脚本、一份令牌。'), '',
           ('Everything on this site as one plain-text file: %sllms-full.txt' if en else '全站内容连成的一份纯文本：%sllms-full.txt') % base, '']
    for sec, items in nav:
        out += ['## ' + (T(sec) if sec in EN or not en else sec), '']
        for href, name, _ in items:
            if offlang(href):
                continue
            c = by.get(href.split('/')[-1][:-5]) if href.startswith('components/') else None
            desc = first(c['readme_en'] if en else c['readme']) if c else ''
            out.append('- [%s](%s%s)%s' % (name, base, href, ': ' + desc if desc else ''))
        out.append('')
    full = []
    src = os.path.join(SRC, 'en') if en else SRC
    for slug, title, f in GUIDES:
        if f:
            full.append(read(src, f).strip())
    for c in comps:
        r = (c['readme_en'] if en else c['readme']).strip()
        if r and not (c['name'].startswith('Sample') and c['name'].endswith('EN')):
            full.append('# %s%s\n\n%s' % (c['name'], '' if label(c) == c['name'] else ' · ' + label(c), r))
    for rel, text in (('llms.txt', '\n'.join(out)), ('llms-full.txt', '\n\n---\n\n'.join(full) + '\n')):
        path = os.path.join(OUT, 'en' if en else '', rel)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)


# ---------- 令牌 → CSS ----------
def tokens_css(t):
    themes = [x['id'] for x in t['color']['themes']]

    def val(v, th):
        v = v if isinstance(v, str) else v.get(th, v[themes[0]])
        m = re.fullmatch(r'\{(.+)\}', v)
        return 'var(--%s)' % m.group(1) if m else v

    out = '/* Hairline — generated from tokens.json */\n'
    themed = t['color']['tokens'] + t.get('shadow', {}).get('tokens', [])
    def block(th):
        # color-scheme 让滚动条、原生下拉这些浏览器自己画的东西也跟着主题走
        scheme = '  color-scheme: %s;\n' % th if th in ('light', 'dark') else ''
        return scheme + ''.join('  --%s: %s;\n' % (x['name'], val(x['value'], th)) for x in themed)

    for i, th in enumerate(themes):
        sel = ':root, [data-theme="%s"]' % th if i == 0 else '[data-theme="%s"]' % th
        out += sel + ' {\n' + block(th) + '}\n'
    if 'dark' in themes[1:]:
        # 没写 data-theme 的页面跟随系统；写了就以写的为准
        out += '@media (prefers-color-scheme: dark) {\n:root:not([data-theme]) {\n' + block('dark') + '}\n}\n'
    out += ':root {\n'
    for key, fam in t.items():
        if isinstance(fam, dict) and 'tokens' in fam and key not in ('color', 'shadow'):
            out += ''.join('  --%s: %s;\n' % (x['name'], x['value']) for x in fam['tokens'])
    out += ''.join('  --font-%s: %s;\n' % (k, v) for k, v in t['type']['families'].items()) + '}\n'
    for g in t['type']['groups']:
        for s in g['styles']:
            css = 'font-family: var(--font-%s); font-size: %s; line-height: %s; font-weight: %s;' % (s.get('family', g['family']), s['fontSize'], s['lineHeight'], s['fontWeight'])
            if 'letterSpacing' in s:
                css += ' letter-spacing: %s;' % s['letterSpacing']
            if 'fontStyle' in s:
                css += ' font-style: %s;' % s['fontStyle']
            out += '.%s { %s }\n' % (s['name'], css)
    # 随窗口分档的样式（目前只有 display）：断点照 breakpoint 令牌的数值抄，媒体查询里不能用变量
    bp = {x['name']: x['value'] for x in t.get('breakpoint', {}).get('tokens', [])}
    for g in t['type']['groups']:
        for s in g['styles']:
            for name, step in s.get('steps', {}).items():
                out += '@media (min-width: %s) { .%s { font-size: %s; line-height: %s; } }\n' % (bp[name], s['name'], step['fontSize'], step['lineHeight'])
    return out


# ---------- 标签页图标与分享卡片 ----------
def social(rel, page):
    """给文档站的页面加上 favicon 和分享到社交平台时用的信息。组件的独立预览页不加。"""
    m = re.search(r'<title>(.*?)</title>\n<meta name="description" content="(.*?)">', page)
    if not m:
        return page
    root = '../' * rel.count('/')
    en = rel.startswith('en/')
    zh_rel = rel[3:] if en else rel
    alt = lambda r: (SITE_URL.rstrip('/') + '/' + ('' if r == 'index.html' else r[:-10] if r.endswith('/index.html') else r)) if SITE_URL else root + r
    tags = ['<link rel="icon" href="%sassets/favicon.svg" type="image/svg+xml">' % root,
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="%s">' % ('Hairline' if en else '毫 Hairline'),
            '<meta property="og:locale" content="%s">' % ('en_US' if en else 'zh_CN'),
            '<link rel="alternate" hreflang="zh-CN" href="%s">' % alt(zh_rel),
            '<link rel="alternate" hreflang="en" href="%s">' % alt('en/' + zh_rel),
            '<link rel="alternate" hreflang="x-default" href="%s">' % alt(zh_rel),
            '<meta property="og:title" content="%s">' % m.group(1),
            '<meta property="og:description" content="%s">' % m.group(2),
            '<meta name="twitter:card" content="summary_large_image">']
    if SITE_URL:
        base = SITE_URL.rstrip('/') + '/'
        url = alt(rel)
        tags += ['<link rel="canonical" href="%s">' % url,
                 '<meta property="og:url" content="%s">' % url,
                 '<meta property="og:image" content="%sassets/og.png">' % base,
                 '<meta property="og:image:width" content="1200">',
                 '<meta property="og:image:height" content="630">']
    return page.replace(m.group(0), m.group(0) + '\n' + '\n'.join(tags), 1)


# ---------- 前缀、版本、核对 ----------
def token_names(t):
    """tokens.json 里所有会变成 CSS 变量的名字。"""
    names = {x['name'] for fam in t.values() if isinstance(fam, dict) and 'tokens' in fam for x in fam['tokens']}
    return names | {'font-%s' % k for k in t['type']['families']}


def type_names(t):
    """字体样式的名字，它们会变成类名（.title-1）。"""
    return {s['name'] for g in t['type']['groups'] for s in g['styles']}


def prefix_classes(markup, names):
    """标记里的 class="title-1" 改成 class="hao-title-1"。"""
    if not names:
        return markup

    def fix(m):
        return m.group(1) + ' '.join(PREFIX + c if c in names else c for c in m.group(2).split(' ')) + m.group(3)
    return re.sub(r'(class=")([^"]*)(")', fix, markup)


def prefix_selectors(css, names):
    """样式表里的 .title-1 改成 .hao-title-1。"""
    alt = '|'.join(sorted((re.escape(n) for n in names), key=len, reverse=True))
    return re.sub(r'(?<![\w-])\.(%s)(?![\w-])' % alt, r'.%s\1' % PREFIX, css)


def prefixed(text, names):
    """把 --bg 改成 --hao-bg。只动令牌名；hao-btn--seal 这种类名和组件自己的局部变量（--p、--s）不动。"""
    if not names:
        return text
    alt = '|'.join(sorted((re.escape(n) for n in names), key=len, reverse=True))
    return re.sub(r'(?<![\w-])--(%s)(?![\w-])' % alt, r'--%s\1' % PREFIX, text)


def version():
    """版本号只写在 bundle.js 一处。"""
    return re.search(r"version:\s*'([^']+)'", read(SRC, 'components', 'bundle.js')).group(1)


# 定义了但样式表不用，是有意的：
UNUSED_OK = {
    'bp-medium': '媒体查询里不能用变量，照数值抄', 'bp-expanded': '同上', 'bp-wide': '同上',
    'z-nav': '导航栏吸不吸顶由产品决定，吸顶时用它',
}
# 字体样式档位之外、有意保留的字号（px）。只有三种情形可以登记：
# 一、装在方框里的单字，字号跟着框走（约为框的一半）；二、标志和装饰符号，它们是图形；三、格子里实在放不下的小字，下限 11px。
FONT_SIZE_OK = {
    11: '格子里的小字：月历和日历页里的农历，格子只放得下这么大。这是全系统最小的字',
    14: '框里的单字：步骤条序号里的汉字数字，装进 28px 的圆',
    16: '框里的单字：页码印里的数字，装进 36px 的印',
    28: '图形：标志的字',
    52: '图形：英文引文开头那枚装饰引号',
}
# 由标记或脚本在运行时设的局部变量
RUNTIME_VARS = {'p', 'v'}


def check(t, css):
    """核对 tokens.json 和 bundle.css 对得上。返回（错误，提醒）。"""
    errors, warns = [], []
    names = token_names(t)
    used = set(re.findall(r'var\(--([\w-]+)', css))
    local = set(re.findall(r'(?<![\w-])--([\w-]+)\s*:', css))
    for n in sorted(used - names - local - RUNTIME_VARS):
        errors.append('样式表用了 --%s，但 tokens.json 里没有，样式表里也没定义' % n)
    for n in sorted(local & names):
        errors.append('样式表自己又定义了一遍令牌 --%s，令牌只在 tokens.json 里定义' % n)
    if re.search(r'--%s' % PREFIX, css):
        errors.append('source 里的样式表不带 --%s 前缀，前缀在生成 dist 时统一加' % PREFIX)
    for i, line in enumerate(css.split('\n'), 1):
        bare = re.sub(r'mask(-image)?:[^;]*;', '', line)   # 遮罩里的 #000 只表示「不透明」
        if re.search(r'#[0-9a-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(', bare):
            errors.append('bundle.css 第 %d 行写死了颜色，改用颜色令牌' % i)
    scale = {int(float(s['fontSize'].replace('px', ''))) for g in t['type']['groups'] for s in g['styles']}
    scale |= {int(float(x['fontSize'].replace('px', ''))) for g in t['type']['groups'] for s in g['styles'] for x in s.get('steps', {}).values()}
    for g in t['type']['groups']:
        for s in g['styles']:
            for x in [s] + list(s.get('steps', {}).values()):
                if int(float(x['lineHeight'].replace('px', ''))) % 4:
                    errors.append('字体样式 %s 的行高 %s 不是 4 的倍数' % (s['name'], x['lineHeight']))
    for i, line in enumerate(css.split('\n'), 1):
        for m in re.finditer(r'font(?:-size)?:\s*(?:[\w.]+\s+)*?(\d+)px', line):
            n = int(m.group(1))
            if n not in scale and n not in FONT_SIZE_OK:
                errors.append('bundle.css 第 %d 行的字号 %dpx 不在字体样式的档位里；确实需要就登记到 FONT_SIZE_OK 并写明原因' % (i, n))
    for n in sorted(names - used - set(UNUSED_OK)):
        warns.append('令牌 %s 没有被样式表用到' % n)
    for n in sorted(set(UNUSED_OK) & used):
        warns.append('令牌 %s 已经用上了，可以从 UNUSED_OK 里去掉' % n)
    return errors, warns


def dist_css(t, bundle):
    """dist/hairline.css：字体引入必须在最前，然后是令牌，再是组件。"""
    imports = ''.join(re.findall(r'^@import .*\n', bundle, re.M))
    rest = re.sub(r'^@import .*\n', '', bundle, flags=re.M).lstrip('\n')
    banner = '/*! 毫 Hairline %s · 令牌与全部组件的样式。由 build_site.py 从 source/ 生成，不要直接改这个文件。 */\n' % version()
    return banner + imports + prefix_selectors(prefixed(tokens_css(t) + '\n' + rest, token_names(t)), type_names(t))


# ---------- 代码高亮与排版 ----------
VOID = {'input', 'br', 'hr', 'img', 'meta', 'link', 'path', 'circle', 'rect'}
INLINE = {'span', 'i', 'b', 'strong', 'small', 'code', 'a', 'em', 'cite', 'time', 'output', 'option', 'label', 'button', 'th', 'td', 'h1', 'h2', 'h3', 'p', 'legend', 'summary', 'li', 'figcaption', 'textarea'}


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = {'tag': None, 'kids': []}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'raw': self.get_starttag_text(), 'kids': []}
        self.stack[-1]['kids'].append(node)
        if tag not in VOID and not node['raw'].endswith('/>'):
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1]['kids'].append({'tag': tag, 'raw': self.get_starttag_text(), 'kids': [], 'void': True})

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if data.strip():
            self.stack[-1]['kids'].append(re.sub(r'\s+', ' ', data))

    def handle_entityref(self, name):
        self.stack[-1]['kids'].append('&%s;' % name)

    def handle_charref(self, name):
        self.stack[-1]['kids'].append('&#%s;' % name)


def flat(node):
    if isinstance(node, str):
        return node
    inner = ''.join(flat(k) for k in node['kids'])
    if node['tag'] in VOID or node.get('void'):
        return node['raw']
    return '%s%s</%s>' % (node['raw'], inner, node['tag'])


def pretty(markup):
    tree = Tree()
    tree.feed(markup)
    lines = []

    def walk(node, depth):
        pad = '  ' * depth
        if isinstance(node, str):
            if node.strip():
                lines.append(pad + node.strip())
            return
        one = flat(node)
        simple = node['tag'] == 'svg' or all(isinstance(k, str) or k['tag'] in INLINE or k['tag'] in VOID for k in node['kids'])
        if node['tag'] in VOID or node.get('void') or (simple and len(one) <= 150) or node['tag'] == 'svg':
            lines.append(pad + one.strip())
            return
        lines.append(pad + node['raw'])
        for k in node['kids']:
            walk(k, depth + 1)
        lines.append('%s</%s>' % (pad, node['tag']))

    for k in tree.root['kids']:
        walk(k, 0)
    return '\n'.join(lines)


TOKEN = re.compile(r'(</?)([A-Za-z][\w-]*)|("[^"]*")|(\s)([\w:-]+)(?==")|([^<"]+|.)', re.S)


def highlight(code):
    code = prefix_classes(code, TYPE_NAMES)
    out = []
    for m in TOKEN.finditer(code):
        if m.group(2):
            out.append('%s<span class="c-t">%s</span>' % (html.escape(m.group(1)), m.group(2)))
        elif m.group(3):
            out.append('<span class="c-s">%s</span>' % html.escape(m.group(3), quote=False))
        elif m.group(5):
            out.append('%s<span class="c-a">%s</span>' % (m.group(4), m.group(5)))
        else:
            out.append(html.escape(m.group(0), quote=False))
    return ''.join(out)


# ---------- Markdown（只支持这套手册用到的写法） ----------
HAN = r'[\u3400-\u9fff][\u3000-\u303f\u3400-\u9fff\uff00-\uffef]*'


def han(markup):
    """英文页里夹着的汉字包一层 <span lang="zh">：这样它用宋体或苹方，读屏软件也按中文读。标签和代码里的不动。"""
    if LANG != 'en':
        return markup
    parts = re.split(r'(<code>.*?</code>|<[^>]+>)', markup)
    return ''.join(p if i % 2 else re.sub(HAN, lambda m: '<span lang="zh">%s</span>' % m.group(0), p) for i, p in enumerate(parts))


def md(text, root, names, skip_h1=True):
    def inline(s):
        s = html.escape(s, quote=False)

        def code(m):
            c = m.group(1)
            if c in names:
                return '<a class="hao-link" href="%scomponents/%s.html"><code>%s</code></a>' % (root, c.lower(), c)
            return '<code>%s</code>' % c
        s = re.sub(r'`([^`]+)`', code, s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a class="hao-link" href="\2">\1</a>', s)
        return han(s)

    lines = text.split('\n')
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append('<pre class="code"><code>%s</code></pre>' % highlight('\n'.join(lines[i + 1:j])))
            i = j + 1
        elif re.match(r'#{1,4} ', ln):
            n = len(ln.split(' ')[0])
            if not (n == 1 and skip_h1):
                title = ln[n + 1:].strip()
                # 英文标题里有空格，不能直接当 id：改成小写连字符。中文页的 id 仍是标题原文
                hid = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-') if LANG == 'en' else html.escape(title)
                out.append('<h%d id="%s">%s</h%d>' % (n, hid or 's', inline(title), n))
            i += 1
        elif ln.startswith('|') and i + 1 < len(lines) and re.match(r'\|[\s:|-]+\|\s*$', lines[i + 1]):
            cells = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
            head = cells(ln)
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].startswith('|'):
                rows.append(cells(lines[j]))
                j += 1
            out.append('<div class="hao-table-wrap"><table class="hao-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                ''.join('<th scope="col">%s</th>' % inline(c) for c in head),
                ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in rows)))
            i = j
        elif re.match(r'(- |\d+\. )', ln):
            tag = 'ul' if ln.startswith('- ') else 'ol'
            items = []
            while i < len(lines) and (re.match(r'(- |\d+\. )', lines[i]) or (lines[i].startswith('  ') and items)):
                if re.match(r'(- |\d+\. )', lines[i]):
                    items.append(re.sub(r'^(- |\d+\. )', '', lines[i]))
                else:
                    items[-1] += ' ' + lines[i].strip()
                i += 1
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag))
        elif ln.strip() == '' or ln.strip() == '---':
            i += 1
        else:
            j = i
            buf = []
            while j < len(lines) and lines[j].strip() and not re.match(r'(#{1,4} |- |\d+\. |\||```)', lines[j]):
                buf.append(lines[j].strip())
                j += 1
            out.append('<p>%s</p>' % inline(' '.join(buf)))
            i = j
    return '\n'.join(out)


# ---------- 读取组件 ----------
def load_components():
    comps = []
    for name in sorted(os.listdir(os.path.join(SRC, 'components'))):
        d = os.path.join(SRC, 'components', name)
        if not os.path.isfile(os.path.join(d, 'preview.html')):
            continue
        prev = read(d, 'preview.html')
        m = re.search(r'@dsCard([^>]*?)-->', prev)
        attrs = dict(re.findall(r'(\w+)="?([^"\s]+)"?', m.group(1))) if m else {}
        readme = read(d, 'README.md') if os.path.isfile(os.path.join(d, 'README.md')) else ''
        en_path = os.path.join(SRC, 'en', 'components', name + '.md')
        if readme and not os.path.isfile(en_path):
            sys.exit('缺英文稿：source/en/components/%s.md' % name)
        readme_en = read(en_path) if readme else ''
        body = prev[prev.index('<body'):]
        body = body[body.index('>') + 1:body.rindex('</body>')]
        scripts = ''.join(re.findall(r'<script>.*?</script>', body, flags=re.S))
        body = re.sub(r'<script>.*?</script>', '', body, flags=re.S)
        panes = {}
        for lang in ('zh-CN', 'en'):
            s = re.search(r'<section lang="%s">(.*?)</section>\s*(?=<section|</div>\s*$)' % lang, body, flags=re.S)
            if s:
                panes[lang] = re.sub(r'<p class="hao-bi__tag">.*?</p>', '', s.group(1)).strip()
        comps.append({'name': name, 'zh': ZH.get(name, name), 'group': attrs.get('group', '示例' if name == 'Cover' else '其他'), 'height': int(attrs.get('height', 300)), 'width': attrs.get('width'),
                      'readme': readme, 'readme_en': readme_en, 'panes': panes, 'whole': body.strip(), 'scripts': scripts, 'preview': prev,
                      'frame': name.startswith('Sample') or name == 'Cover'})
    return comps


# ---------- 页面外壳 ----------
MARK = 'M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z'
THEME_BOOT = "(function(){var t=null;try{t=localStorage.getItem('hao-theme');}catch(e){}var q=/[?&]theme=(dark|light)/.exec(location.search);if(q){t=q[1];}if(!t){t=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}document.documentElement.setAttribute('data-theme',t);document.documentElement.classList.add('js');var en=document.documentElement.lang==='en',l=en?'en':'zh';try{l=localStorage.getItem(en?'hao-demo-lang-en':'hao-demo-lang')||l;}catch(e){}document.documentElement.setAttribute('data-demo-lang',l);})();"


def shell(rel, title, content, nav, active, prev_next=None, wide=False, home=False, desc=None):
    depth = rel.count('/')
    root = '../' * depth
    files = aroot(root)
    en = LANG == 'en'
    # 语言切换：去同一页的另一种语言。写的是对方语言自己的叫法，并标上那种语言
    other = '<a class="site-lang" href="%s" lang="%s" hreflang="%s">%s</a>' % (('../' * (depth + 1) + rel, 'zh-CN', 'zh-CN', '中文') if en else (root + 'en/' + rel, 'en', 'en', 'English'))
    if rel.startswith('guide/'):
        top_active = 'guide'
    elif rel.startswith('tokens/'):
        top_active = 'tokens'
    elif rel.startswith('components/sample') or rel == 'components/cover.html':
        top_active = 'ex'
    elif rel.startswith('components/'):
        top_active = 'comp'
    else:
        top_active = 'home'
    tops = [('guide', 'guide/install.html', T('指南')), ('comp', 'components/button.html', T('组件')), ('tokens', 'tokens/color.html', T('令牌')), ('ex', 'components/samplescreen%s.html' % ('en' if en else ''), T('示例'))]
    toplinks = ''.join('<a href="%s%s"%s>%s</a>' % (root, h, ' aria-current="true"' if k == top_active else '', l) for k, h, l in tops)
    menu = '' if home else '<button class="site-menu hao-nav__action" type="button" aria-label="%s" aria-expanded="false"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i></button>' % T('打开目录')
    top = '''<header class="site-top"><div class="site-top__in container">
  %s<a class="hao-logo hao-logo--sm hao-logo--ink site-top__logo" href="%sindex.html" lang="en" aria-label="%s"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="%s"/></svg><span class="site-top__name">Hairline</span></a>
  <nav class="site-top__links" aria-label="%s">%s</nav>
  %s
  <a class="hao-nav__action site-gh" href="%s" aria-label="%s"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="%s"/></svg></a>
  <button class="hao-nav__action site-theme" type="button" data-site-theme aria-label="%s"><i class="hao-icon hao-icon--moon" aria-hidden="true"></i></button>
</div></header>''' % (menu, root, T('Hairline 首页'), MARK, T('主导航'), toplinks, other, REPO_URL, T('GitHub 上的源代码'), GITHUB_MARK, T('切换昼夜主题'))
    # 落款的年款：中文页写汉字、不用斜体，英文页是斜体的 colophon（见 source/english.md）
    sign = '<span class="hao-colophon" lang="en">Winter, the Bingwu year</span>' if en else '<span class="hao-colophon">丙午年冬</span>'
    if home:
        cols = ''
        for title, key in (('指南', 'guide'), ('令牌', 'tokens')):
            its0 = [i for sec, items in nav if SECTION.get(sec, 'comp') == key for i in items]
            cols += '<div><h2>%s</h2>%s</div>' % (T(title), ''.join('<a href="%s%s">%s</a>' % (root, h, html.escape(l)) for h, l, _ in its0))
        cats = []
        for cat, gs in CATS[1:-1]:
            its = [i for sec, items in nav if sec in gs and sec != '令牌' for i in items]
            if its:
                cats.append('<a href="%s%s">%s<small>%d</small></a>' % (root, its[0][0], T(cat if cat != '基础' else '基础件'), len(its)))
        cols += '<div><h2>%s</h2>%s</div>' % (T('组件'), ''.join(cats))
        cols += ''.join('<div><h2>%s</h2>%s</div>' % (T(sec), ''.join('<a href="%s%s">%s</a>' % (root, h, html.escape(l)) for h, l, _ in items if not offlang(h))) for sec, items in nav if sec == '示例')
        # 全站目录只在 404 页给：那一页的人正在找路。首页顶栏已有四个去处，页脚只留一行落款
        full = rel == '404.html'
        directory = '<nav class="site-dir__cols" aria-label="%s">%s</nav>\n' % (T('全站目录'), cols) if full else ''
        body = '''<main id="main" class="home">%s</main>
<footer class="site-dir%s"><div class="site-dir__in container">%s<p class="site-dir__end"><span>%s</span>%s</p></div></footer>''' % (content, '' if full else ' site-dir--short', directory, T('界面基于毫（Hairline）设计系统'), sign)
    else:
        side = ''
        last = None
        for sec, items in nav:
            if SECTION.get(sec, 'comp') != top_active:
                continue
            cat = CAT_OF.get(sec, sec)
            if cat != last:
                if top_active not in ('tokens', 'ex'):
                    side += '<p class="site-side__cat">%s</p>' % T(cat)
                last = cat
            links = ''.join('<a class="hao-side__item" href="%s%s"%s>%s%s</a>' % (root, href, ' aria-current="page"' if href == active else '', html.escape(label), '<small>%s</small>' % sub if sub else '') for href, label, sub in items if href == active or not offlang(href))
            side += '<div class="site-side__group">%s%s</div>' % ('' if sec == cat or top_active in ('tokens', 'ex') else '<p class="hao-side__label">%s</p>' % T(sec), links)
        heads = []

        def _hid(m):
            attrs, inner = m.group(1), m.group(2)
            if 'data-demo-h' in attrs:
                return m.group(0)
            got = re.search(r'id="([^"]+)"', attrs)
            hid = got.group(1) if got else 's%d' % (len(heads) + 1)
            heads.append((hid, han(re.sub(r'<[^>]+>', '', inner))))
            return m.group(0) if got else '<h2%s id="%s">%s</h2>' % (attrs, hid, inner)
        content = re.sub(r'<h2([^>]*)>(.*?)</h2>', _hid, content, flags=re.S)
        toc = ''
        if len(heads) >= 2 and not wide:
            toc = '<nav class="site-toc" aria-label="%s"><p>%s</p>%%s</nav>' % (T('本页内容'), T('本页内容')) % ''.join('<a href="#%s">%s</a>' % h for h in heads)
        pn = ''
        if prev_next:
            pv, nx = prev_next
            pn = '<nav class="site-pn" aria-label="%s">%s%s</nav>' % (T('上一页与下一页'),
                '<a class="site-pn__a" href="%s%s"><span>%s</span>%s</a>' % (root, pv[0], T('上一页'), html.escape(pv[1])) if pv else '<span></span>',
                '<a class="site-pn__a site-pn__a--next" href="%s%s"><span>%s</span>%s</a>' % (root, nx[0], T('下一页'), html.escape(nx[1])) if nx else '<span></span>')
        body = '''<div class="site-body container">
  <aside class="site-side" aria-label="%s"><div class="site-side__search"><label class="hao-search"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="%s" aria-label="%s" data-site-search></label></div><nav class="hao-side" aria-label="%s">%s</nav><p class="site-side__none" hidden>%s</p></aside>
  <main class="site-main" id="main"><div class="site-cols%s"><article class="site-doc">%s</article>%s</div>%s
    <footer class="site-foot"><span>%s</span>%s</footer>
  </main>
</div>''' % (T('目录'), T(SEARCH[top_active]), T(SEARCH[top_active]), T('文档目录'), side, T('没有找到，换一个词试试。'), '' if toc else ' site-cols--solo', content, toc, pn, T('界面基于毫（Hairline）设计系统'), sign)
        if top_active in ('tokens', 'ex'):
            body = body.replace('<aside class="site-side"', '<aside class="site-side site-side--short"', 1)
    cls = 'site site--home' if home else ('site site--doc site--wide' if wide else 'site site--doc')
    return '''<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<script>%s</script>
<link rel="stylesheet" href="%s">
<link rel="stylesheet" href="%sassets/hairline.css">
<link rel="stylesheet" href="%sassets/site.css">
</head>
<body class="%s">
<a class="site-skip" href="#main">%s</a>
%s
%s
<script src="%sassets/hairline.js"></script>
<script src="%sassets/site.js"></script>
</body>
</html>
''' % ('en' if en else 'zh-CN', T('毫 Hairline 设计系统') if home else html.escape(title) + T(' · 毫 Hairline'), html.escape(desc or T('毫 Hairline：一套中英双语、昼夜两套主题的设计系统。')), THEME_BOOT, FONTS, files, files, cls, T('跳到正文'), top, body, files, files)


def demo(c, root):
    root = aroot(root)
    if c['frame']:
        w = ' style="min-width:%spx"' % c['width'] if c['width'] else ''
        return '<div class="demo demo--frame"><div class="demo__stage demo__stage--frame"><iframe class="demo__frame" data-theme-follow title="%s" src="%spreview/%s.html" height="%d"%s loading="lazy"></iframe></div><div class="demo__bar"><a class="hao-btn hao-btn--sm hao-btn--plain" href="%spreview/%s.html" target="_blank" rel="noopener">%s</a>%s</div></div>' % (label(c), root, c['name'], c['height'], w, root, c['name'], T('在新窗口打开整页'), '<a class="hao-btn hao-btn--sm hao-btn--plain" href="%s.html">%s</a>' % (twin(c['name']).lower(), T('看中文版' if c['name'].endswith('EN') else '看英文版')) if twin(c['name']) else '')
    panes = c['panes'] or {'zh-CN': c['whole']}
    # 演示里的 <h1> 是组件自己的大标题。放进文档页后，它在页面大纲里降到「演示」这个二级标题之下；给人看的代码不变。
    # 演示里的 <h2> 标上 data-demo-h：它是示例的一部分，不进右边的「本页内容」。
    staged = lambda body: re.sub(r'<h2(?=[\s>])', '<h2 data-demo-h', re.sub(r'<h1(?=[\s>])', '<h1 aria-level="3"', body))
    stage = ''.join('<div class="demo__pane" lang="%s">%s</div>' % (lang, staged(body)) for lang, body in panes.items())
    codes = ''.join('<pre class="code demo__src" data-lang="%s" lang="%s"><code>%s</code></pre>' % (lang, lang, highlight(pretty(body))) for lang, body in panes.items())
    seg = ''
    if len(panes) > 1:
        seg = '<span class="hao-seg" role="radiogroup" aria-label="%s"><label><input type="radio" name="dl-%s" value="zh" data-demo-lang><span lang="zh-CN">中文</span></label><label><input type="radio" name="dl-%s" value="en" data-demo-lang><span lang="en">English</span></label></span>' % (T('演示语言'), c['name'], c['name'])
    cls = 'demo' + ('' if len(panes) > 1 else ' demo--single')
    return '<div class="%s"><div class="demo__stage">%s</div><div class="demo__bar">%s<span class="demo__sp"></span><button class="hao-btn hao-btn--sm hao-btn--plain" type="button" data-demo-copy>%s</button><button class="hao-btn hao-btn--sm hao-btn--tinted" type="button" data-demo-code aria-expanded="false">%s</button></div><div class="demo__code" hidden>%s</div></div>%s' % (cls, stage, seg, T('复制代码'), T('显示代码'), codes, c['scripts'])


# ---------- 站点样式与脚本 ----------
SITE_CSS = r'''/* Hallmark · shape: Specimen · genre: editorial · theme: brand · redesign: full
 * paper: oklch(96.6% 0.004 258) · accent: oklch(44.5% 0.146 262) · display: Noto Serif SC with Newsreader · body: PingFang SC, system sans · hero: Stage (/) · nav: edge-aligned, wordmark left and four destinations right · footer: index columns, a docs hub with a real sitemap · signature: the glyph 毫 at poster size over a gold hairline the brush has just drawn
 * axes: light/roman-serif/cool · posture: Restrained · contrast: pass · fold: pass · draw: f56033 · job: sign up · v2.0.0 */
/* Hallmark · pre-emit critique: P4 H4 E4 S5 R4 V4 · weakest: E, the live sample screens are iframes that only scale with script; gave each a fixed aspect box so the layout holds before the script runs */
/* Hallmark · waive 39b · one control, the seal itself, 96px square · pressing the seal stamps it again, so the control is the seal at its own size */
/* Hallmark · waive 77 · one band, a single sentence beside three counts · the counts of components, icons and files are this band's whole content, so a picture would only repeat the hero */
/* Hallmark · waive 37 · one line, the Chinese colophon in the page footer · Noto Serif SC is loaded from weight 600 up, so the four-character year line is set in the system Song regular to stay thin; it falls back to the display face where no system Song exists */
/* Hallmark · waive 8 · the draw dealt Stat-Led but the page has no headline figure · the glyph 毫 leads this page instead and its three counts sit in a supporting row */
:root, [data-theme] {
  --color-paper: var(--bg); --color-paper-2: var(--surface); --color-paper-3: var(--surface-sunken);
  --color-ink: var(--ink); --color-ink-2: var(--ink-secondary); --color-muted: var(--ink-tertiary);
  --color-rule: var(--hairline); --color-accent: var(--tint); --color-accent-ink: var(--on-tint); --color-focus: var(--focus);
}
:root {
  --font-display: var(--font-serif); --font-body: var(--font-sans); --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --space-3xs: 2px; --space-2xs: 4px; --space-xs: 8px; --space-sm: 12px; --space-md: 16px; --space-lg: 24px; --space-xl: 40px; --space-2xl: 64px; --space-3xl: 96px; --space-4xl: 144px;
  --text-xs: 0.8125rem; --text-sm: 0.9375rem; --text-md: 1.0625rem; --text-lg: 1.25rem; --text-xl: 1.5rem; --text-2xl: 2rem; --text-3xl: 2.75rem;
  --text-display-s: clamp(2.75rem, 4vw + 0.75rem, 4rem); --text-section: clamp(2rem, 2.5vw + 1rem, 2.75rem);
  --text-title: clamp(1.25rem, 0.75vw + 0.875rem, 1.5rem); --text-lead: clamp(1.0625rem, 0.35vw + 0.9375rem, 1.25rem);
  --text-glyph: clamp(7.5rem, 10vw + 2rem, 11.5rem);
  --text-doc-h1: clamp(2rem, 1.5vw + 1.5rem, 2.75rem); --text-doc-h2: 1.5rem; --text-doc-h3: 1.25rem; --measure-doc: 45rem; --measure-prose: 40rem; --toc-w: 9.5rem;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1); --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --dur-micro: 120ms; --dur-short: 220ms; --dur-long: 420ms;
  --container: 1328px; --gutter: 64px; --gap-columns: 32px; --section-gap-s: 96px; --section-gap: 112px; --section-gap-l: 128px;
  --nav-h: 64px; --side-w: 240px; --shot-r: 12px;
}
@media (max-width: 60rem) { :root { --gutter: 24px; --section-gap-s: 80px; --section-gap: 96px; --section-gap-l: 120px; } }
@media (max-width: 40rem) { :root { --gutter: 16px; --section-gap-s: 56px; --section-gap: 72px; --section-gap-l: 96px; --gap-columns: 16px; --nav-h: 88px; } }

html, body { overflow-x: clip; }
html { scroll-padding-top: calc(var(--nav-h) + var(--space-md)); scrollbar-color: var(--color-muted) var(--color-paper); }
/* 页面里自己滚动的小块：细滚动条，轨道透明，不在深一档的底色上露出一条浅带 */
.site-side .hao-side, .code, .demo__stage, .site-doc .hao-table-wrap { scrollbar-width: thin; scrollbar-color: var(--color-muted) transparent; }
body.site { margin: 0; background: var(--color-paper); color: var(--color-ink); font: 400 var(--text-md)/1.65 var(--font-body); -webkit-font-smoothing: antialiased; caret-color: var(--color-accent); }
.site ::selection { background: color-mix(in oklab, var(--color-accent) 22%, transparent); color: var(--color-ink); }
/* 焦点环的兜底：权重压到最低，组件自己定的内收或外扩不被它盖掉 */
:where(.site) :focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.container { box-sizing: border-box; width: 100%; max-width: var(--container); margin-inline: auto; padding-inline: var(--gutter); }
.site-skip { position: absolute; left: var(--space-md); top: calc(-1 * var(--space-3xl)); z-index: var(--z-toast, 500); padding: var(--space-xs) var(--space-md); border-radius: var(--radius-md); background: var(--color-ink); color: var(--color-paper); }
.site-skip:focus-visible { top: var(--space-xs); }

/* 顶栏：标志在左，四个去处和昼夜开关在右 */
.site-top { position: sticky; top: 0; z-index: var(--z-nav); height: var(--nav-h); background: var(--color-paper); border-bottom: 1px solid var(--color-rule); }
.site-top__in { display: flex; align-items: center; gap: var(--space-xs); height: 100%; }
.site-top__logo { margin-right: auto; min-height: 44px; font-size: var(--text-lg); }
.site-top__links { display: flex; align-items: center; gap: var(--space-2xs); }
.site-top__links a { display: inline-flex; align-items: center; min-height: 44px; padding: 0 var(--space-sm); border-radius: var(--radius-sm); font: 400 var(--text-sm)/1 var(--font-body); color: var(--color-ink-2); text-decoration: none; white-space: nowrap; transition: color var(--dur-micro) var(--ease-out), background-color var(--dur-micro) var(--ease-out); }
.site-top__links a:hover, .site-top__links a[aria-current] { color: var(--color-ink); background: var(--color-paper-3); }
.site-top__links a:active { opacity: 0.7; }
.site-top__links a:focus-visible { outline-offset: -2px; }
/* 语言切换：和四个去处同一种字，前面一道细线把它和去处分开 */
.site-lang { position: relative; display: inline-flex; align-items: center; min-height: 44px; margin-left: var(--space-xs); padding: 0 var(--space-sm); border-radius: var(--radius-sm); font: 400 var(--text-sm)/1 var(--font-body); color: var(--color-ink-2); text-decoration: none; white-space: nowrap; transition: color var(--dur-micro) var(--ease-out), background-color var(--dur-micro) var(--ease-out); }
.site-lang::before { content: ""; position: absolute; left: calc(-1 * var(--space-2xs) - 1px); top: 50%; width: 1px; height: 1em; margin-top: -0.5em; background: var(--color-rule); }
.site-lang:hover { color: var(--color-ink); background: var(--color-paper-3); }
.site-lang:active { opacity: 0.7; }
.site-lang:focus-visible { outline-offset: -2px; }
.site-top .site-theme { background: none; }
/* GitHub 标志是实心的，比 1.5px 的线性图标显重，画小两号才和旁边的月亮一样重 */
.site-top .site-gh { width: 44px; padding: 0; color: var(--color-ink-2); }
.site-top .site-gh:hover { color: var(--color-ink); }
.site-gh:active { opacity: 0.7; }
.site-gh svg { display: block; width: 18px; height: 18px; fill: currentColor; }
.site-top .hao-nav__action { min-width: 44px; justify-content: center; border-radius: var(--radius-sm); transition: background-color var(--dur-micro) var(--ease-out); }
.site-top .hao-nav__action:hover { background: var(--color-paper-3); text-decoration: none; }
.site-top .hao-nav__action .hao-icon { margin: 0; }
.site-top__logo { min-width: 44px; }
.site-top .site-theme:active, .site-menu:active { opacity: 0.7; }
.site-menu { display: none; }

/* 首页的公共零件 */
.sec { padding-block: var(--section-gap); background: var(--color-paper); color: var(--color-ink); }
.sec--s { padding-block: var(--section-gap-s); }
.sec--2 { background: var(--color-paper-2); }
.sec--3 { background: var(--color-paper-3); }
.g12 { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--gap-columns); }
.sec__h { margin: 0; max-width: 12em; min-width: 0; overflow-wrap: break-word; font: 600 var(--text-section)/1.18 var(--font-display); letter-spacing: 0.01em; text-wrap: balance; }
.sec__h span { display: inline-block; }
.sec__p { margin: var(--space-lg) 0 0; max-width: 30em; font-size: var(--text-lead); line-height: 1.6; color: var(--color-ink-2); text-wrap: pretty; }
.sec__a { margin: var(--space-sm) 0 0; }

/* 产品图：把示例屏整页缩小放进来，是活的页面，不是截图 */
.shot { position: relative; box-sizing: border-box; width: 100%; margin: 0; overflow: hidden; aspect-ratio: var(--w) / var(--h); border-radius: var(--shot-r); background: var(--color-paper); box-shadow: 0 0 0 1px var(--color-rule); }
.shot iframe { position: absolute; left: 0; top: 0; width: calc(var(--w) * 1px); height: calc(var(--h) * 1px); border: 0; transform-origin: 0 0; transform: scale(var(--s, 1)); pointer-events: none; }
.shot--bare { border-radius: 0; background: none; box-shadow: none; }

/* 首屏：左边是名字，右边是系统在干活 */
.hero { background: var(--color-paper); color: var(--color-ink); }
.hero__in { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: var(--space-2xl); align-items: center; min-height: calc(100svh - var(--nav-h)); padding-block: var(--space-2xl); }
.hero h1 { margin: 0; min-width: 0; overflow-wrap: break-word; font: inherit; }
.hero__glyph { display: block; font: 700 var(--text-glyph)/0.96 var(--font-display); }
.hero__rule { position: relative; display: block; height: 1px; margin-top: var(--space-sm); }
.hero__ink { position: absolute; inset: 0; background: var(--gold); transform-origin: 0 50%; }
.hero__pen { position: absolute; inset: 0; pointer-events: none; }
/* 笔：线描，笔尖落在细线的末端。它是「毫」这个名字的本义，只在这一屏出现 */
.hero__brush { position: absolute; right: 0; bottom: 0; height: calc(var(--text-glyph) * 1.25); width: auto; aspect-ratio: 1 / 6; overflow: visible; transform: translateX(50%) rotate(-24deg); transform-origin: 50% 100%; }
.hero__brush path { fill: none; stroke: color-mix(in srgb, var(--pattern), var(--ink) 22%); stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; vector-effect: non-scaling-stroke; }
.hero__brush .tip { stroke: var(--gold); }
.hero__brush .hair { stroke: var(--gold); stroke-width: 1; opacity: 0.7; }
.hero__name { display: block; margin-top: var(--space-md); font: 500 var(--text-lg)/1.2 var(--font-display); letter-spacing: 0.01em; }
.hero__tag { margin: var(--space-md) 0 0; font: 600 var(--text-2xl)/1.35 var(--font-display); letter-spacing: 0.01em; text-wrap: balance; }
.hero__tag span { display: inline-block; }
.hero__a { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-xs); margin-top: var(--space-xl); }
.hero__a .hao-btn { min-height: 48px; white-space: nowrap; }

/* 数字：一句话在左，三个数在右 */
.facts { align-items: center; row-gap: var(--space-xl); }
.facts__p { grid-column: 1 / span 5; margin: 0; max-width: 24em; font-size: var(--text-lead); line-height: 1.6; text-wrap: pretty; }
.facts__n { grid-column: 7 / -1; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); margin: 0; }
.facts__n div { display: flex; flex-direction: column-reverse; padding-inline: var(--space-lg); border-left: 1px solid var(--color-rule); }
.facts__n div:first-child { padding-left: 0; border-left: 0; }
.facts__n dd { margin: 0; font: 600 var(--text-display-s)/1 var(--font-display); font-variant-numeric: tabular-nums lining-nums; }
.facts__n dt { margin-top: var(--space-sm); font-size: var(--text-sm); line-height: 1.4; color: var(--color-ink-2); }

/* 三条规矩：标题在左，三行在右，细线隔开 */
.rules { row-gap: var(--space-2xl); }
.rules__head { grid-column: 1 / span 4; }
.rules__rows { grid-column: 6 / -1; }
.rule3 { display: grid; grid-template-columns: minmax(0, 1fr) 15rem; gap: var(--space-xl); align-items: center; padding-block: var(--space-xl); border-top: 1px solid var(--color-rule); }
.rule3:first-child { padding-top: 0; border-top: 0; }
.rule3:last-child { padding-bottom: 0; }
.rule3 h3 { margin: 0 0 var(--space-xs); font: 600 var(--text-title)/1.3 var(--font-display); letter-spacing: 0.02em; }
.rule3 p { margin: 0; max-width: 26em; color: var(--color-ink-2); text-wrap: pretty; }
.rule3__v { display: flex; align-items: center; justify-content: center; gap: var(--space-sm); min-height: 8rem; }
.rule3__v .hao-scene { margin: 0; }
.rule3__v .hao-row { flex-wrap: nowrap; }
.restamp { padding: 0; border: 0; border-radius: var(--radius-sm); background: none; color: inherit; font: inherit; cursor: pointer; }
.restamp:focus-visible { outline-offset: 6px; }
.restamp:active { opacity: 0.8; }
.hao-seal.is-stamping { animation: site-stamp var(--dur-long) var(--ease-out) both; }
@keyframes site-stamp { from { opacity: 0; transform: scale(1.35); } to { opacity: 1; transform: none; } }

/* 昼夜：左边切换，右边三块屏跟着换 */
.night { transition: background-color var(--dur-long) var(--ease-in-out), color var(--dur-long) var(--ease-in-out); }
.night .g12 { align-items: center; row-gap: var(--space-2xl); }
.night__text { grid-column: 1 / span 4; }
.night__seg { margin-top: var(--space-xl); }
.night__shots { grid-column: 5 / -1; padding-left: var(--gap-columns); display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--gap-columns); align-items: start; }

/* 中英：标题和说明分在两边，下面一大一小两张图 */
.duo { row-gap: var(--space-2xl); align-items: end; }
.duo__h { grid-column: 1 / span 6; }
.duo__side { grid-column: 8 / -1; }
.duo__side .sec__p { margin-top: 0; }
.duo__shots { grid-column: 1 / -1; display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: var(--gap-columns); align-items: end; }
.duo__shots figure { margin: 0; min-width: 0; }
.duo__shots figcaption { margin-top: var(--space-sm); font-size: var(--text-sm); line-height: 1.4; color: var(--color-ink-2); }

/* 四个入口：一行一个，整行可点 */
.index { border-bottom: 1px solid var(--color-rule); }
.cell { position: relative; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--gap-columns); row-gap: var(--space-lg); align-items: center; min-height: 7.5rem; padding-block: var(--space-lg); border-top: 1px solid var(--color-rule); }
.cell h3 { grid-column: 1 / span 3; margin: 0; font: 600 var(--text-2xl)/1.2 var(--font-display); letter-spacing: 0.01em; transition: color var(--dur-short) var(--ease-out); }
.cell__t { grid-column: 4 / span 5; }
.cell__t p { margin: 0; max-width: 26em; color: var(--color-ink-2); text-wrap: pretty; }
.cell__a::before { content: ""; position: absolute; inset: 0; }
.cell h3, .cell__t p, .cell__v { position: relative; z-index: 1; pointer-events: none; }
.cell__a:focus-visible { outline: none; }
.cell:has(.cell__a:focus-visible) { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.cell:has(.cell__a:hover) h3 { color: var(--color-accent); }
.cell:has(.cell__a:active) h3 { opacity: 0.7; }
.cell__v { grid-column: 9 / -1; justify-self: end; display: flex; flex-wrap: wrap; align-items: center; justify-content: flex-end; gap: var(--space-md); }
.cell__icons { display: grid; grid-template-columns: repeat(6, 24px); gap: var(--space-lg); color: var(--color-ink); }
.cell__v:has(.cell__sw) { flex-wrap: nowrap; width: 100%; }
.cell__sw { flex: 0 1 3rem; min-width: 0; aspect-ratio: 1; border-radius: var(--radius-full); box-shadow: inset 0 0 0 1px var(--color-rule); }
.cell__type { display: flex; align-items: baseline; gap: var(--space-lg); font: 700 5rem/1 var(--font-display); }
.cell__type span[lang] { font-weight: 500; letter-spacing: -0.02em; }

/* 结尾：怎么拿到，旁边就是那几行代码 */
.close { position: relative; padding-bottom: calc(var(--section-gap-s) + var(--space-2xl)); }
.close .g12 { align-items: center; row-gap: var(--space-xl); }
.close__text { grid-column: 1 / span 5; }
.close__code { grid-column: 7 / -1; min-width: 0; }
.close__code .code { margin: 0; background: var(--color-paper-2); }
.close__files { margin: var(--space-lg) 0 0; padding: 0; list-style: none; }
.close__files li { display: grid; grid-template-columns: 9rem minmax(0, 1fr) auto; gap: var(--space-md); align-items: baseline; padding-block: var(--space-md); border-top: 1px solid var(--color-rule); font-size: var(--text-sm); color: var(--color-ink-2); }
.close__files li:first-child { border-top: 0; }
.close__files code { font: 400 var(--text-sm)/1.4 var(--font-mono); }
.site-wave { position: absolute; left: 0; right: 0; bottom: 0; height: 60px; }

/* 404：话在左上，舟偏在右下 */
.lost .g12 { min-height: min(52svh, 28rem); row-gap: var(--space-2xl); }
.lost__text { grid-column: 1 / span 7; align-self: start; }
.lost__scene { grid-column: 9 / -1; justify-self: end; align-self: end; margin: 0; }
.site-foot .hao-colophon:lang(zh), /* 思源宋体只载入了 600 以上的字重，落款要细，先用系统自带的宋体常规体 */
.site-dir__end .hao-colophon:lang(zh) { font-style: normal; font-family: "Songti SC", "STSong", "SimSun", var(--font-display); }

/* 页脚目录 */
.site-dir { border-top: 1px solid var(--color-rule); background: var(--color-paper); font: 400 var(--text-sm)/1.4 var(--font-body); color: var(--color-ink-2); }
.site-dir__in { padding-block: var(--space-2xl) var(--space-xl); }
.site-dir--short .site-dir__in { padding-block: var(--space-lg); }
.site-dir--short .site-dir__end { margin-top: 0; padding-top: 0; border-top: 0; }
.site-dir__cols { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: var(--space-xl) var(--gap-columns); }
.site-dir h2 { margin: 0 0 var(--space-xs); font: 600 var(--text-sm)/1.4 var(--font-body); color: var(--color-ink); }
.site-dir a { display: flex; align-items: baseline; gap: var(--space-xs); padding-block: var(--space-2xs); color: inherit; text-decoration: none; }
.site-dir a:hover { color: var(--color-ink); text-decoration: underline; text-underline-offset: 0.2em; }
.site-dir a:active { opacity: 0.7; }
.site-dir a small { font-size: var(--text-xs); color: var(--color-muted); font-variant-numeric: tabular-nums; }
.site-dir__end { display: flex; justify-content: space-between; flex-wrap: wrap; gap: var(--space-xs) var(--space-lg); margin: var(--space-xl) 0 0; padding-top: var(--space-md); border-top: 1px solid var(--color-rule); color: var(--color-muted); }

/* 文档页 */
.site-body { display: flex; align-items: flex-start; }
/* 侧栏分上下两块：搜索框不动，下面的目录自己滚 */
.site-side { position: sticky; top: var(--nav-h); flex: none; display: flex; flex-direction: column; box-sizing: border-box; width: var(--side-w); height: calc(100dvh - var(--nav-h)); margin-left: calc(-1 * var(--space-sm)); border-right: 1px solid var(--color-rule); }
/* 搜索框右边和当前项的底块对齐 */
.site-side__search { flex: none; padding: var(--space-lg) var(--space-sm) var(--space-md); }
/* 英文的占位文字比框里的云头长，两样叠在一起，英文页不画云头 */
.site-side__search .hao-search:lang(en)::after { content: none; }
.site-side__search .hao-search input { min-height: 44px; }
.site-side--short .site-side__search { display: none; }
.site-side .hao-side { flex: 1 1 auto; min-height: 0; overflow-y: auto; flex-wrap: nowrap; width: auto; padding: 0 var(--space-sm) var(--space-2xl) 0; }
.site-side .hao-side > * { flex: none; }
.site-side.site-side--short .hao-side { padding-top: var(--space-lg); }
/* 令牌和示例的侧栏只有十来项，右边的英文名挤得中文名折行，这里不显示 */
.site-side--short .hao-side__item small { display: none; }
.site-side .hao-side__item small { margin-left: auto; font: 400 var(--text-xs)/1.3 var(--font-body); color: var(--color-muted); }
.site-side .hao-side__item[aria-current] small { color: var(--color-accent); }
.site-side__cat { margin: var(--space-lg) 0 var(--space-2xs); padding: var(--space-md) var(--space-sm) 0; border-top: 1px solid var(--color-rule); font: 600 var(--text-md)/1.4 var(--font-display); letter-spacing: 0.02em; color: var(--color-ink); }
.site-side__cat:first-child { margin-top: 0; padding-top: 0; border-top: 0; }
.site-side__group[hidden], .site-side a[hidden], .site-side__cat[hidden] { display: none; }
.site-side__none { margin: 0; padding: var(--space-xs) var(--space-sm); font-size: var(--text-sm); color: var(--color-ink-2); }
.site-side.is-empty .hao-side { display: none; }
.site-main { flex: 1; min-width: 0; padding: var(--space-2xl) 0 var(--space-2xl) var(--space-2xl); }
.site-cols { display: grid; grid-template-columns: minmax(0, var(--measure-doc)) var(--toc-w); justify-content: space-between; column-gap: var(--space-xl); align-items: start; }
.site--wide .site-cols, .site-cols--solo { grid-template-columns: minmax(0, 1fr); }
.site-toc { position: sticky; top: calc(var(--nav-h) + var(--space-2xl)); font: 400 var(--text-xs)/1.5 var(--font-body); }
.site-toc p { margin: 0 0 var(--space-xs); font-weight: 600; color: var(--color-ink); }
.site-toc a { display: block; padding-block: var(--space-2xs); color: var(--color-ink-2); text-decoration: none; }
.site-toc a:hover { color: var(--color-ink); text-decoration: underline; text-underline-offset: 0.2em; }
.site-toc a:active { opacity: 0.7; }
.site-toc a[aria-current] { color: var(--color-ink); font-weight: 600; }
.site-doc { max-width: var(--measure-doc); }
.site--wide .site-doc { max-width: none; }
.site-doc > h1 { margin: 0 0 var(--space-md); min-width: 0; overflow-wrap: break-word; font: 700 var(--text-doc-h1)/1.2 var(--font-display); letter-spacing: 0.02em; text-wrap: balance; }
.site-doc > h1 small { margin-left: var(--space-sm); font: 400 var(--text-md)/1.2 var(--font-body); letter-spacing: 0; color: var(--color-muted); white-space: nowrap; }
.site-lead { margin: 0 0 var(--space-xl); max-width: var(--measure-prose); font-size: var(--text-lg); line-height: 1.6; color: var(--color-ink-2); text-wrap: pretty; }
.site-doc h2 { margin: var(--space-2xl) 0 var(--space-md); font: 600 var(--text-doc-h2)/1.3 var(--font-display); letter-spacing: 0.01em; }
.site-doc h3 { margin: var(--space-xl) 0 var(--space-xs); font: 600 var(--text-doc-h3)/1.4 var(--font-display); letter-spacing: 0.01em; }
.site-doc p { margin: 0 0 var(--space-md); max-width: var(--measure-prose); text-wrap: pretty; }
.site-doc ul, .site-doc ol { margin: 0 0 var(--space-md); padding-left: 1.3em; max-width: var(--measure-prose); }
.site-doc li { margin-bottom: var(--space-xs); }
.site-doc li::marker { color: var(--color-muted); }
.site-doc code { padding: 0 var(--space-2xs); border-radius: var(--radius-xs); background: var(--color-paper-3); font: 400 0.88em/1.4 var(--font-mono); overflow-wrap: anywhere; }
.site-doc a code { color: var(--color-accent); }
.site-doc .hao-table-wrap { margin: 0 0 var(--space-lg); }
.site-doc .hao-table td { vertical-align: top; }
.site-doc .hao-table th { white-space: nowrap; }
.site-doc .hao-table td:first-child { word-break: keep-all; }
.site-doc .hao-table td code { white-space: nowrap; overflow-wrap: normal; }
.code { margin: 0 0 var(--space-lg); padding: var(--space-md) var(--space-lg); border-radius: var(--radius-md); background: var(--color-paper-3); overflow-x: auto; font: 400 var(--text-xs)/1.7 var(--font-mono); color: var(--color-ink); tab-size: 2; }
.code code { padding: 0; background: none; font: inherit; overflow-wrap: normal; white-space: pre; }
.code-box { position: relative; margin: 0 0 var(--space-lg); border-radius: var(--radius-md); overflow: hidden; }
.code-box .code { margin: 0; }
/* 按钮四周多铺一圈同色的底，长代码从它下面滚过去时不会在按钮右边露头 */
.code-copy.hao-btn { position: absolute; top: var(--space-xs); right: var(--space-xs); background: var(--color-paper-3); box-shadow: 0 0 0 var(--space-sm) var(--color-paper-3); white-space: nowrap; }
.c-t { color: var(--color-accent); } .c-a { color: var(--jade); } .c-s { color: var(--amber-ink); }

.demo { margin: 0 0 var(--space-xl); border: 1px solid var(--color-rule); border-radius: var(--radius-xl); background: var(--color-paper); overflow: hidden; }
.demo__stage { padding: var(--space-xl); overflow-x: auto; font: 400 var(--text-md)/1.55 var(--font-body); }
.demo__stage--frame { padding: 0; }
.demo__frame { display: block; width: 100%; border: 0; }
html[data-demo-lang="zh"] .demo:not(.demo--single) .demo__pane[lang="en"], html[data-demo-lang="en"] .demo:not(.demo--single) .demo__pane[lang="zh-CN"] { display: none; }
html[data-demo-lang="zh"] .demo:not(.demo--single) .demo__src[data-lang="en"], html[data-demo-lang="en"] .demo:not(.demo--single) .demo__src[data-lang="zh-CN"] { display: none; }
.demo__bar { display: flex; align-items: center; flex-wrap: wrap; gap: var(--space-xs); padding: var(--space-xs) var(--space-sm); border-top: 1px solid var(--color-rule); background: var(--color-paper-2); }
.demo__sp { flex: 1; }
.demo__bar .hao-seg span { min-width: 3.5rem; padding: var(--space-2xs) var(--space-sm); font-size: var(--text-xs); line-height: 1.55; }
.demo__bar .hao-btn { white-space: nowrap; }
.demo__code { border-top: 1px solid var(--color-rule); }
.demo__code .code { margin: 0; border-radius: 0; max-height: 27.5rem; }

.site-pn { display: flex; justify-content: space-between; gap: var(--space-md); max-width: var(--measure-doc); margin-top: var(--space-2xl); padding-top: var(--space-lg); border-top: 1px solid var(--color-rule); }
.site-pn__a { display: flex; flex-direction: column; justify-content: center; min-width: 44px; min-height: 44px; color: var(--color-accent); font: 600 var(--text-md)/1.4 var(--font-body); text-decoration: none; }
.site-pn__a:hover { text-decoration: underline; text-underline-offset: 0.2em; }
.site-pn__a:active { opacity: 0.7; }
.site-pn__a span { font: 400 var(--text-xs)/1.4 var(--font-body); color: var(--color-muted); }
.site-pn__a--next { text-align: right; }
.site-foot { display: flex; justify-content: space-between; flex-wrap: wrap; gap: var(--space-xs) var(--space-md); max-width: var(--measure-doc); margin-top: var(--space-2xl); font: 400 var(--text-xs)/1.4 var(--font-body); color: var(--color-muted); }

.tk-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(15.5rem, 1fr)); gap: var(--space-md); margin-bottom: var(--space-xl); }
.tk { border-radius: var(--radius-lg); background: var(--color-paper-2); overflow: hidden; box-shadow: 0 0 0 1px var(--color-rule); }
.tk__sw { height: 4.5rem; border-bottom: 1px solid var(--color-rule); }
.tk__b { padding: var(--space-sm) var(--space-md) var(--space-md); }
.tk__n { font: 600 var(--text-sm)/1.45 var(--font-mono); }
.tk__v { font: 400 var(--text-xs)/1.4 var(--font-mono); color: var(--color-muted); }
.tk__u { margin-top: var(--space-xs); font: 400 var(--text-xs)/1.55 var(--font-body); color: var(--color-ink-2); }
.ty { display: grid; grid-template-columns: 11rem minmax(0, 1fr); gap: var(--space-lg); align-items: baseline; padding-block: var(--space-lg); border-top: 1px solid var(--color-rule); }
.ty__m { font: 400 var(--text-xs)/1.55 var(--font-body); color: var(--color-muted); }
.ty__m b { display: block; font: 600 var(--text-sm)/1.45 var(--font-mono); color: var(--color-ink); }
.sp { display: flex; align-items: center; gap: var(--space-md); padding-block: var(--space-xs); }
.sp__bar { height: 12px; border-radius: 2px; background: var(--color-accent); }
.sp__box { width: 4.5rem; height: 3rem; background: var(--tint-wash); box-shadow: inset 0 0 0 1.5px var(--color-accent); }
.sp code { min-width: 9.5rem; }
.sh { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-xl); margin: var(--space-lg) 0 var(--space-xl); }
.sh__c { padding: var(--space-lg); border-radius: var(--radius-lg); background: var(--color-paper-2); }

/* 动效：首屏的线画一次，各段进场一次；没有脚本或减弱动态效果时，内容直接可见 */
.js .hero__ink { animation: site-draw 0.8s var(--ease-out) 0.15s backwards; }
.js .hero__pen { animation: site-pen 0.8s var(--ease-out) 0.15s backwards; }
@keyframes site-draw { from { transform: scaleX(0.6); } }
@keyframes site-pen { from { transform: translateX(-40%); } }
.js [data-reveal] { opacity: 0; transform: translateY(8px); transition: opacity var(--dur-long) var(--ease-out), transform var(--dur-long) var(--ease-out); }
.js [data-reveal].is-in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .js [data-reveal] { opacity: 1; transform: none; transition: none; }
  .js .hero__ink, .js .hero__pen, .hao-seal.is-stamping { animation: none; }
  .site-top__links a::before, .night, .cell h3, .site-top__links a, .site-lang, .site-top .hao-nav__action, .site-side, .js .site-side, .js .site--menu .site-side { transition: none; }
}

/* 触屏：把偏矮的可点区域撑到 44px */
@media (pointer: coarse) {
  .site-side .hao-side__item { min-height: 44px; }
  .site-dir a { min-height: 44px; align-items: center; padding-block: 0; }
  .demo__bar .hao-seg span { padding-block: var(--space-sm); }
  .demo__bar .hao-btn--sm { min-height: 44px; }
  .code-copy.hao-btn { top: var(--space-2xs); right: var(--space-2xs); }
}
@media (max-width: 75rem) {
  .site-cols { grid-template-columns: minmax(0, 1fr); }
  .site-toc { display: none; }
}
@media (max-width: 60rem) {
  .hero__in { grid-template-columns: minmax(0, 1fr); gap: var(--space-xl); min-height: 0; padding-block: var(--space-xl) var(--space-2xl); }
  .facts__p, .facts__n, .rules__head, .rules__rows, .night__text, .night__shots, .duo__h, .duo__side, .close__text, .close__code, .lost__text, .lost__scene { grid-column: 1 / -1; }
  .cell { min-height: 0; }
  .cell h3, .cell__t { grid-column: 1 / -1; }
  .cell__v { grid-column: 1 / -1; justify-self: start; justify-content: flex-start; }
  .sh { grid-template-columns: minmax(0, 1fr); }
  .js .site-menu { display: inline-flex; }
  .site-body { flex-direction: column-reverse; align-items: stretch; }
  .site-side { position: static; width: 100%; height: auto; margin-left: 0; border-right: 0; border-top: 1px solid var(--color-rule); }
  .js .site-side { position: fixed; left: 0; top: var(--nav-h); z-index: var(--z-sheet); width: var(--side-w); height: calc(100dvh - var(--nav-h)); padding-left: var(--space-sm); border-top: 0; background: var(--color-paper); transform: translateX(-100%); visibility: hidden; transition: transform var(--dur-short) var(--ease-out), visibility 0s var(--dur-short); }
  .js .site--menu .site-side { transform: none; visibility: visible; transition-delay: 0s; box-shadow: var(--shadow-float); }
  .site-main { padding: var(--space-xl) 0 var(--space-2xl); }
  .site-cols { grid-template-columns: minmax(0, 1fr); }
  .site-toc { display: none; }
  .ty { grid-template-columns: minmax(0, 1fr); gap: var(--space-xs); }
  .demo__stage { padding: var(--space-lg) var(--space-md); }
  .site-dir__cols { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 40rem) {
  /* 窄屏的顶栏分两行：上一行是标志、语言和昼夜，下一行是四个去处。英文的四个词一行放不下 */
  .site-top__in { flex-wrap: wrap; align-content: center; row-gap: 0; }
  .site-top__links { order: 9; flex: 0 0 100%; gap: 0; margin-inline: calc(-1 * var(--space-xs)); }
  .site-top__links a, .site-lang { padding: 0 var(--space-xs); }
  .site-lang { margin-left: 0; }
  .site-lang::before { content: none; }
  /* 当前去处的底块上下各收 4px，不贴着顶栏的底线；可点的高度仍是 44px */
  .site-top__links a { position: relative; z-index: 0; }
  .site-top__links a:hover, .site-top__links a[aria-current] { background: none; }
  .site-top__links a::before { content: ""; position: absolute; z-index: -1; inset: var(--space-2xs) 0; border-radius: var(--radius-sm); transition: background-color var(--dur-micro) var(--ease-out); }
  .site-top__links a:hover::before, .site-top__links a[aria-current]::before { background: var(--color-paper-3); }
  /* 三栏以上的表格不硬挤：留够宽度，在自己的框里左右滚 */
  .site-doc .hao-table:has(th:nth-child(3)) { min-width: 30rem; }
  .site-doc .hao-table:has(th:nth-child(4)) { min-width: 38rem; }
  /* 演示框的工具条：语言切换一行，两个按钮另起一行 */
  .demo:not(.demo--single) .demo__sp { flex-basis: 100%; height: 0; }
  .facts__n div { padding-inline: var(--space-sm); }
  .rule3 { grid-template-columns: minmax(0, 1fr); gap: var(--space-lg); }
  .rule3__v { justify-content: flex-start; min-height: 0; }
  .night__shots { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .night__shots .shot:last-child { display: none; }
  .duo__shots { grid-template-columns: minmax(0, 1fr); row-gap: var(--space-lg); }
  .cell__icons { gap: var(--space-md); }
  .cell__type { font-size: 4rem; }
  .cell__v { gap: var(--space-sm); }
  .cell__sw { flex-basis: 2.5rem; }
  .close__files li { grid-template-columns: minmax(0, 1fr) auto; }
  .close__files li span:nth-child(2) { grid-column: 1 / -1; grid-row: 2; }
}
@media (max-width: 22.5rem) {
  .site-top__links a { padding: 0 var(--space-2xs); }
  .site-top__links { margin-inline: calc(-1 * var(--space-2xs)); }
}
/* 减弱动态效果：放在最后，盖过上面各个宽度里写的过渡 */
@media (prefers-reduced-motion: reduce) {
  .js .site-side, .js .site--menu .site-side, .site-top__links a::before, .site-top .hao-nav__action { transition: none; }
}
'''

SITE_JS = r'''
(function () {
  var root = document.documentElement;
  function each(sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); }
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  /* 这份脚本两种语言的页面共用：提示文字按页面语言取；演示语言的选择，中文站和英文站各记各的 */
  var EN = root.lang === 'en', LANG_KEY = EN ? 'hao-demo-lang-en' : 'hao-demo-lang';
  var SAY = EN ? { day: 'Switch to day theme', night: 'Switch to night theme', open: 'Open contents', close: 'Close contents', show: 'Show code', hide: 'Hide code', copy: 'Copy', sTable: 'Table, scrolls sideways', sCode: 'Code, scrolls sideways', sDemo: 'Demo, scrolls sideways', copied: 'Code copied', failed: 'Couldn’t copy. Show the code and select it by hand.' }
               : { day: '换成昼间主题', night: '换成夜间主题', open: '打开目录', close: '收起目录', show: '显示代码', hide: '收起代码', copy: '复制', sTable: '表格，可左右滚动', sCode: '代码，可左右滚动', sDemo: '演示，可左右滚动', copied: '已复制代码', failed: '没能复制，展开代码后手动选取' };
  function syncLang() {
    var l = root.getAttribute('data-demo-lang') || (EN ? 'en' : 'zh');
    each('input[data-demo-lang]', function (r) { r.checked = r.value === l; });
  }
  function syncTheme() {
    var dark = root.getAttribute('data-theme') === 'dark';
    each('[data-site-theme]', function (b) {
      var i = b.querySelector('.hao-icon');
      if (i) i.className = 'hao-icon hao-icon--' + (dark ? 'sun' : 'moon');
      b.setAttribute('aria-label', dark ? SAY.day : SAY.night);
    });
    each('iframe[data-theme-follow]', function (f) {
      try { f.contentDocument.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light'); } catch (e) {}
    });
  }
  function closeMenu() {
    var b = document.querySelector('.site-menu');
    if (!document.body.classList.contains('site--menu')) return;
    document.body.classList.remove('site--menu');
    if (b) { b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-label', SAY.open); }
  }
  function copy(text, back) {
    var say = function (ok) { if (window.Hairline) window.Hairline.toast(ok ? SAY.copied : SAY.failed, { ok: ok }); };
    var old = function () {
      var ta = document.createElement('textarea'), ok = false;
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;left:0;top:0;opacity:0';
      document.body.appendChild(ta); ta.select();
      try { ok = document.execCommand('copy'); } catch (err) {}
      document.body.removeChild(ta); back.focus(); say(ok);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(function () { say(true); }, old);
    else old();
  }
  function stamp(seal) {
    seal.classList.remove('is-stamping'); void seal.offsetWidth;
    seal.classList.add('is-stamping');
  }
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (!t.matches) return;
    if (t.matches('input[data-demo-lang]')) { root.setAttribute('data-demo-lang', t.value); store(LANG_KEY, t.value); syncLang(); }
    if (t.matches('input[name="night-theme"]')) {
      var band = t.closest('.night');
      band.setAttribute('data-theme', t.value);
      Array.prototype.forEach.call(band.querySelectorAll('iframe'), function (f) {
        try { f.contentDocument.documentElement.setAttribute('data-theme', t.value); } catch (err) {}
      });
    }
  });
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-site-theme], [data-demo-code], [data-demo-copy], .code-copy, .site-menu, .restamp');
    if (!t) { if (!(e.target.closest && e.target.closest('.site-side'))) closeMenu(); return; }
    if (t.hasAttribute('data-site-theme')) {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next); store('hao-theme', next); syncTheme();
    } else if (t.hasAttribute('data-demo-code')) {
      var code = t.closest('.demo').querySelector('.demo__code');
      code.hidden = !code.hidden;
      t.setAttribute('aria-expanded', code.hidden ? 'false' : 'true');
      t.textContent = code.hidden ? SAY.show : SAY.hide;
    } else if (t.hasAttribute('data-demo-copy')) {
      var demo = t.closest('.demo'), lang = root.getAttribute('data-demo-lang') === 'en' ? 'en' : 'zh-CN';
      var src = demo.querySelector('.demo__src[data-lang="' + lang + '"]') || demo.querySelector('.demo__src');
      copy(src.textContent, t);
    } else if (t.classList.contains('code-copy')) {
      copy(t.parentNode.querySelector('.code').textContent, t);
    } else if (t.classList.contains('site-menu')) {
      var open = document.body.classList.toggle('site--menu');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
      t.setAttribute('aria-label', open ? SAY.close : SAY.open);
    } else if (t.classList.contains('restamp')) {
      stamp(t.querySelector('.hao-seal'));
    }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });

  var search = document.querySelector('[data-site-search]'), side = document.querySelector('.site-side');
  if (search) search.addEventListener('input', function () {
    var q = search.value.trim().toLowerCase(), total = 0;
    each('.site-side__group', function (g) {
      var any = false;
      Array.prototype.forEach.call(g.querySelectorAll('a'), function (a) { var hit = !q || a.textContent.toLowerCase().indexOf(q) >= 0; a.hidden = !hit; any = any || hit; if (hit) total++; });
      g.hidden = !any;
    });
    each('.site-side__cat', function (c) { c.hidden = !!q; });
    var none = document.querySelector('.site-side__none');
    if (none) none.hidden = total > 0;
    side.classList.toggle('is-empty', total === 0);
  });

  /* 产品图：按容器宽度把整页缩小 */
  function fit() {
    each('.shot', function (s) {
      var w = parseFloat(getComputedStyle(s).getPropertyValue('--w'));
      if (w && s.clientWidth) s.style.setProperty('--s', (s.clientWidth / w).toFixed(4));
    });
  }
  each('.shot iframe', function (f) {
    var quiet = function () {
      try {
        var d = f.contentDocument;
        if (!d || !d.head || d.getElementById('shot-quiet')) return;
        var st = d.createElement('style'); st.id = 'shot-quiet';
        st.textContent = '*{scrollbar-width:none}::-webkit-scrollbar{display:none}';
        d.head.appendChild(st);
      } catch (e) {}
    };
    f.addEventListener('load', quiet); quiet();
  });
  fit();
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);

  /* 文档里的代码块：右上角一个复制按钮 */
  each('.site-doc pre.code', function (pre) {
    if (pre.closest('.demo')) return;
    var box = document.createElement('div'), b = document.createElement('button');
    box.className = 'code-box'; pre.parentNode.insertBefore(box, pre); box.appendChild(pre);
    b.type = 'button'; b.className = 'hao-btn hao-btn--sm hao-btn--plain code-copy'; b.textContent = SAY.copy;
    box.appendChild(b);
  });

  /* 自己能左右滚的表格、代码和演示：滚得动的时候才让键盘停得上去 */
  function reach() {
    each('.site-doc .hao-table-wrap, .site-doc pre.code, .demo__stage:not(.demo__stage--frame)', function (el) {
      var on = el.scrollWidth > el.clientWidth + 1;
      if (on === el.hasAttribute('data-reach')) return;
      if (on) {
        el.setAttribute('data-reach', ''); el.tabIndex = 0; el.setAttribute('role', 'region');
        el.setAttribute('aria-label', el.matches('pre') ? SAY.sCode : el.matches('.demo__stage') ? SAY.sDemo : SAY.sTable);
      } else {
        el.removeAttribute('data-reach'); el.removeAttribute('tabindex'); el.removeAttribute('role'); el.removeAttribute('aria-label');
      }
    });
  }
  reach();
  window.addEventListener('resize', reach);
  window.addEventListener('load', reach);

  /* 本页内容：标出读到了哪一节 */
  var tocs = Array.prototype.slice.call(document.querySelectorAll('.site-toc a'));
  if (tocs.length) {
    var heads = tocs.map(function (a) { return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); });
    var tick = false, spy = function () {
      tick = false;
      var line = parseFloat(getComputedStyle(root).scrollPaddingTop) + 8, at = -1;
      heads.forEach(function (h, i) { if (h && h.getBoundingClientRect().top <= line) at = i; });
      if (window.innerHeight + window.scrollY >= root.scrollHeight - 2) at = tocs.length - 1;
      tocs.forEach(function (a, i) { if (i === at) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); });
    };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(spy); } }, { passive: true });
    spy();
  }

  /* 各段进场：只做一次 */
  if (root.classList.contains('js') && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -10% 0px' });
    each('[data-reveal]', function (el) { io.observe(el); });
  } else {
    each('[data-reveal]', function (el) { el.classList.add('is-in'); });
  }

  each('iframe[data-theme-follow]', function (f) { f.addEventListener('load', syncTheme); });
  var cur = document.querySelector('.site-side [aria-current]');
  var list = side && side.querySelector('.hao-side');
  if (cur && list) list.scrollTop = Math.max(0, cur.getBoundingClientRect().top - list.getBoundingClientRect().top - list.clientHeight / 2);
  syncLang(); syncTheme();
}());
'''

COVER_ART = '<svg class="site-hero__art" viewBox="96 0 384 288" role="img" aria-label="月洞与水中月"><rect class="tint" x="96" y="0" width="192" height="288"/><rect class="deep" x="288" y="0" width="192" height="144"/><rect class="wash" x="288" y="144" width="192" height="144"/><circle class="ground" cx="192" cy="144" r="72"/><path class="wash" d="M312 144a72 72 0 0 1 144 0z"/><path class="deep" d="M312 144a72 72 0 0 0 144 0z"/></svg>'

INSTALL = '''
<h1>安装</h1>
<p class="site-lead">Hairline 由两个文件组成：一份样式表，一份行为脚本。不需要构建工具，也不依赖任何框架。</p>
<h2 id="files">拿到文件</h2>
<p>两个文件就在这个站点的 <code>assets</code> 文件夹里，直接复制到你的项目中：</p>
<div class="hao-table-wrap"><table class="hao-table"><thead><tr><th scope="col">文件</th><th scope="col">内容</th><th scope="col">大小</th></tr></thead><tbody>
<tr><td><a class="hao-link" href="%(files)sassets/hairline.css" download><code>hairline.css</code></a></td><td>全部令牌（颜色、字体、间距、圆角、阴影）和所有组件的样式，含昼夜两套主题</td><td>%(css)s</td></tr>
<tr><td><a class="hao-link" href="%(files)sassets/hairline.js" download><code>hairline.js</code></a></td><td>弹窗、菜单、月历等组件的行为。可选：不加载它，组件照样能看</td><td>%(js)s</td></tr>
<tr><td><a class="hao-link" href="%(files)sassets/tokens.json" download><code>tokens.json</code></a></td><td>令牌的原始数据，给设计工具或别的平台用</td><td>%(tk)s</td></tr>
</tbody></table></div>
<p>目前没有发布到 npm，也没有公共的 CDN 地址。请把文件放进自己的项目里引用。</p>
<h2 id="include">引入</h2>
<p>在页面的 <code>&lt;head&gt;</code> 里引入字体和样式表，在 <code>&lt;body&gt;</code> 结尾引入脚本：</p>
<pre class="code"><code>%(snippet)s</code></pre>
<ul>
<li>标题用的两支衬线字体（Newsreader、思源宋体）从 Google Fonts 加载。离线或无法访问时，会回退到系统自带的宋体和 Georgia。</li>
<li>正文在 Apple 设备上用系统的苹方和 San Francisco，其他平台用思源黑体。要在非 Apple 平台保证一致，把思源黑体也加进字体链接。</li>
<li>脚本要放在内容之后，或者加 <code>defer</code>。</li>
</ul>
<h2 id="theme">昼夜主题</h2>
<p>在 <code>&lt;html&gt;</code> 上写 <code>data-theme="light"</code> 或 <code>data-theme="dark"</code>。不写就跟随系统的深浅色设置。想让读者自己切换，用一小段脚本把选择写到这个属性上，这个站点右上角的开关就是这样做的。</p>
<h2 id="vars">用令牌</h2>
<p>所有令牌都是 CSS 变量，名字以 <code>--hao-</code> 开头，放进已有的页面不会和别的变量撞名。文档里说的 <code>tint</code>、<code>space-4</code>，写出来就是 <code>var(--hao-tint)</code>、<code>var(--hao-space-4)</code>。</p>
<h2 id="lang">语言</h2>
<p>在 <code>&lt;html&gt;</code> 上写 <code>lang="zh-CN"</code> 或 <code>lang="en"</code>。标题的字号与字距、段落的对齐、引文的角标、月历的星期与农历，都会跟着语言走。详见<a class="hao-link" href="english.html">英文界面</a>。</p>
<h2 id="support">浏览器</h2>
<p>面向近两年的 Chrome、Safari、Edge、Firefox。纹样、图标、月相用到了 CSS 遮罩；中西文自动间距和标点挤压是较新的特性，旧浏览器上不生效，但不影响使用。</p>
'''

QUICK = '''
<h1>快速上手</h1>
<p class="site-lead">三步搭出第一个页面：引入文件，写标记，按「三条规矩」检查一遍。</p>
<h2 id="page">一个完整的页面</h2>
<p>把下面这段存成一个 HTML 文件，和 <code>hairline.css</code>、<code>hairline.js</code> 放在一起，用浏览器打开：</p>
<pre class="code"><code>%(page)s</code></pre>
<h2 id="how">组件怎么写</h2>
<ul>
<li>所有类名以 <code>hao-</code> 开头。零件用两道下划线（<code>hao-card__title</code>），变体用两道横线（<code>hao-btn--tinted</code>）。</li>
<li>能用原生元素的地方都用原生元素：按钮是 <code>&lt;button&gt;</code>，开关是 <code>&lt;input type="checkbox"&gt;</code>，下拉是 <code>&lt;select&gt;</code>。</li>
<li>行为靠属性声明。上面例子里的 <code>data-hao-open</code>、<code>data-hao-close</code>、<code>data-hao-toast</code> 就是。全部属性见<a class="hao-link" href="behavior.html">行为与脚本</a>。</li>
<li>每个组件的页面都有可以操作的演示，点「显示代码」能看到对应的标记，直接复制。</li>
</ul>
<h2 id="rules">做完检查三件事</h2>
<ol>
<li><strong>朱砂一处。</strong>这一屏里红色是不是只出现了一次（一方印、一个角标、一个删除按钮）。</li>
<li><strong>一屏一景。</strong>纹样、小品、装裱这类「景」是不是至多一个；设置和表单这类办事的页面应该一个都没有。</li>
<li><strong>形随控件。</strong>进度是不是只用了一种意象，月亮是不是只出现了一处。</li>
</ol>
<p>规矩的全文在<a class="hao-link" href="principles.html">设计原则</a>里。</p>
<h2 id="own">换成你自己的</h2>
<p>这套系统不只属于一个产品。拿去用时换三样：印文、产品名、落款的年款。颜色、字体、间距的令牌和三条规矩保持原样。要做一方真正的篆字印，见<a class="hao-link" href="seal.html">印稿规范</a>。</p>
'''

INSTALL_EN = '''
<h1>Install</h1>
<p class="site-lead">Hairline is two files: a stylesheet and a behavior script. It needs no build tools and depends on no framework.</p>
<h2 id="files">Get the files</h2>
<p>Both files are in this site’s <code>assets</code> folder. Copy them into your project:</p>
<div class="hao-table-wrap"><table class="hao-table"><thead><tr><th scope="col">File</th><th scope="col">What’s in it</th><th scope="col">Size</th></tr></thead><tbody>
<tr><td><a class="hao-link" href="%(files)sassets/hairline.css" download><code>hairline.css</code></a></td><td>Every token (color, type, spacing, radius, shadow) and the styles for all components, in both day and night themes</td><td>%(css)s</td></tr>
<tr><td><a class="hao-link" href="%(files)sassets/hairline.js" download><code>hairline.js</code></a></td><td>Behavior for dialogs, menus, the calendar, and other components. Optional: without it, components still display</td><td>%(js)s</td></tr>
<tr><td><a class="hao-link" href="%(files)sassets/tokens.json" download><code>tokens.json</code></a></td><td>The raw token data, for design tools and other platforms. Its descriptions are in Chinese</td><td>%(tk)s</td></tr>
</tbody></table></div>
<p>Hairline isn’t published to npm yet, and there’s no public CDN address. Keep the files in your own project and link to them there.</p>
<h2 id="include">Include</h2>
<p>Link the fonts and the stylesheet in the page’s <code>&lt;head&gt;</code>, and the script at the end of <code>&lt;body&gt;</code>:</p>
<pre class="code"><code>%(snippet)s</code></pre>
<ul>
<li>The two serif faces for titles, Newsreader and Noto Serif SC, load from Google Fonts. Offline, or where Google Fonts can’t be reached, titles fall back to the system’s Songti and Georgia.</li>
<li>Text uses the system’s PingFang and San Francisco on Apple devices, and Noto Sans SC elsewhere. For a consistent look off Apple platforms, add Noto Sans SC to the font link.</li>
<li>Put the script after the content, or add <code>defer</code>.</li>
</ul>
<h2 id="theme">Day and night themes</h2>
<p>Set <code>data-theme="light"</code> or <code>data-theme="dark"</code> on <code>&lt;html&gt;</code>. Leave it out and the page follows the system’s light or dark setting. To let readers switch, write their choice to this attribute with a few lines of script. The switch at the top right of this site works that way.</p>
<h2 id="vars">Use the tokens</h2>
<p>Every token is a CSS variable whose name starts with <code>--hao-</code>, so it won’t collide with variables already on your page. Where the docs say <code>tint</code> or <code>space-4</code>, you write <code>var(--hao-tint)</code> or <code>var(--hao-space-4)</code>.</p>
<h2 id="lang">Language</h2>
<p>Set <code>lang="en"</code> or <code>lang="zh-CN"</code> on <code>&lt;html&gt;</code>. Title size and letter spacing, paragraph alignment, quote marks, and the calendar’s weekdays and lunar dates all follow the language. See <a class="hao-link" href="english.html">English interfaces</a>.</p>
<h2 id="support">Browsers</h2>
<p>Hairline targets the last two years of Chrome, Safari, Edge, and Firefox. Patterns, icons, and moon phases use CSS masks. Automatic spacing between Chinese and Latin text and punctuation trimming are newer features. Older browsers skip them, and everything still works.</p>
'''

QUICK_EN = '''
<h1>Quick start</h1>
<p class="site-lead">Three steps to a first page: include the files, write the markup, and check it against the three rules.</p>
<h2 id="page">A complete page</h2>
<p>Save this as an HTML file next to <code>hairline.css</code> and <code>hairline.js</code>, then open it in a browser:</p>
<pre class="code"><code>%(page)s</code></pre>
<h2 id="how">How components are written</h2>
<ul>
<li>Every class name starts with <code>hao-</code>. Parts use two underscores (<code>hao-card__title</code>), and variants use two hyphens (<code>hao-btn--tinted</code>).</li>
<li>Native elements are used wherever they exist: a button is a <code>&lt;button&gt;</code>, a switch is an <code>&lt;input type="checkbox"&gt;</code>, a dropdown is a <code>&lt;select&gt;</code>.</li>
<li>Behavior is declared with attributes, like <code>data-hao-open</code>, <code>data-hao-close</code>, and <code>data-hao-toast</code> in the example above. See <a class="hao-link" href="behavior.html">Behavior and scripts</a> for all of them.</li>
<li>Every component page has a working demo. Select “Show code” to see its markup, then copy it.</li>
</ul>
<h2 id="rules">Check three things when you’re done</h2>
<ol>
<li><strong>One touch of cinnabar.</strong> Does red appear only once on this screen: one seal, one badge, or one delete button?</li>
<li><strong>One scene per screen.</strong> Is there at most one scene, such as a pattern, a vignette, or a mounting? Task screens like settings and forms should have none.</li>
<li><strong>Shape follows the control.</strong> Does progress use only one motif, and does the moon appear in only one place?</li>
</ol>
<p>The rules are set out in full in <a class="hao-link" href="principles.html">Design principles</a>.</p>
<h2 id="own">Make it your own</h2>
<p>This system doesn’t belong to one product. When you use it, change three things: the seal character, the product name, and the date line of the signature. Keep the color, type, and spacing tokens and the three rules as they are. To make a real seal in seal script, see <a class="hao-link" href="seal.html">Seal design</a>.</p>
'''

SNIPPET = '''<link rel="stylesheet" href="%s">
<link rel="stylesheet" href="hairline.css">

<!-- 页面内容 -->

<script src="hairline.js"></script>''' % FONTS

PAGE = '''<!doctype html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>札记</title>
  <link rel="stylesheet" href="%s">
  <link rel="stylesheet" href="hairline.css">
</head>
<body style="margin:0;background:var(--bg);color:var(--ink);font:400 17px/28px var(--font-sans)">
  <main class="hao-page" style="padding-top:48px">
    <h1 class="title-1" style="margin:0 0 24px">今日</h1>

    <div class="hao-card hao-card--wave" style="max-width:390px">
      <h2 class="hao-card__title">晨间札记</h2>
      <p class="hao-card__body">窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p>
    </div>

    <p style="margin-top:24px">
      <button class="hao-btn" data-hao-toast="已保存" data-hao-toast-ok>保存修改</button>
      <button class="hao-btn hao-btn--plain" data-hao-open="confirm">删除</button>
    </p>
  </main>

  <div class="hao-scrim" id="confirm" data-hao-modal hidden>
    <div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="confirm-title">
      <h2 class="hao-dialog__title" id="confirm-title">删除这条札记</h2>
      <p class="hao-dialog__body">删除后无法恢复。</p>
      <div class="hao-dialog__actions">
        <button class="hao-btn hao-btn--tinted" data-hao-close data-hao-initial>取消</button>
        <button class="hao-btn hao-btn--seal" data-hao-close>删除</button>
      </div>
    </div>
  </div>

  <script src="hairline.js"></script>
</body>
</html>''' % FONTS

SNIPPET_EN = SNIPPET.replace('页面内容', 'Your content')

PAGE_EN = '''<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Notes</title>
  <link rel="stylesheet" href="%s">
  <link rel="stylesheet" href="hairline.css">
</head>
<body style="margin:0;background:var(--bg);color:var(--ink);font:400 17px/24px var(--font-sans)">
  <main class="hao-page" style="padding-top:48px">
    <h1 class="title-1-en" style="margin:0 0 24px">Today</h1>

    <div class="hao-card hao-card--wave" style="max-width:390px">
      <h2 class="hao-card__title">Morning note</h2>
      <p class="hao-card__body">Mist outside the window. Write down the three things to do today, and let the rest wait.</p>
    </div>

    <p style="margin-top:24px">
      <button class="hao-btn" data-hao-toast="Saved" data-hao-toast-ok>Save changes</button>
      <button class="hao-btn hao-btn--plain" data-hao-open="confirm">Delete</button>
    </p>
  </main>

  <div class="hao-scrim" id="confirm" data-hao-modal hidden>
    <div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="confirm-title">
      <h2 class="hao-dialog__title" id="confirm-title">Delete this note</h2>
      <p class="hao-dialog__body">You can’t undo this.</p>
      <div class="hao-dialog__actions">
        <button class="hao-btn hao-btn--tinted" data-hao-close data-hao-initial>Cancel</button>
        <button class="hao-btn hao-btn--seal" data-hao-close>Delete</button>
      </div>
    </div>
  </div>

  <script src="hairline.js"></script>
</body>
</html>''' % FONTS

# 首页上成段的话。键相同，两种语言各一份
HOME = {
    'zh': {
        'tag': '<span>iOS 的克制，</span><span>一点东方的气韵。</span>', 'start': '开始使用', 'browse': '浏览组件',
        'facts': '一套中英双语、昼夜两套主题的设计系统。从应用界面到海报，都有规矩可循。',
        'rules_h': '三条规矩', 'rules_p': '传统的东西加在哪、加多少，只看这三条。拿不准的时候，少放一样。', 'rules_a': '读设计原则',
        'night_h': '<span>入夜，</span><span>换一套墨。</span>', 'night_p': '夜间主题不是把颜色反过来。石青变浅，朱砂压暗，每个颜色都重新调过。', 'night_a': '看昼夜两套色值', 'night_seg': '这三块屏幕的主题', 'day': '昼', 'night': '夜',
        'duo_h': '<span>中文和英文，</span><span>各排各的。</span>', 'duo_p': '英文界面不是把汉字换成字母。标题字、行高、落款都另有一档，印章仍然用汉字。', 'duo_a': '读英文界面的规则',
        'close_h': '<span>两个文件，</span><span>拿去用。</span>', 'close_p': '一份样式表，一份脚本。不需要构建工具，也不依赖任何框架。印文、产品名和落款换成你自己的。', 'close_b': '照着做一个页面', 'code': '引入这两个文件的代码',
    },
    'en': {
        'tag': '<span>The restraint of iOS,</span> <span>with an East Asian sensibility.</span>', 'start': 'Get started', 'browse': 'Browse components',
        'facts': 'A design system in Chinese and English, with day and night themes. It sets out rules for everything from app screens to posters.',
        'rules_h': 'The three rules', 'rules_p': 'Where a traditional element goes, and how much of it, comes down to these three. When you’re not sure, leave one thing out.', 'rules_a': 'Read the design principles',
        'night_h': '<span>At night,</span> <span>a different ink.</span>', 'night_p': 'The night theme isn’t the day theme inverted. Azurite gets lighter, cinnabar gets darker, and every color is mixed again.', 'night_a': 'See both sets of color values', 'night_seg': 'Theme for these three screens', 'day': 'Day', 'night': 'Night',
        'duo_h': '<span>Chinese and English,</span> <span>each set its own way.</span>', 'duo_p': 'An English interface isn’t a Chinese one with the characters swapped for letters. Titles, line height, and the signature each have their own setting. The seal stays in Chinese.', 'duo_a': 'Read the rules for English interfaces',
        'close_h': '<span>Two files,</span> <span>yours to use.</span>', 'close_p': 'One stylesheet and one script. No build tools, no framework. Swap in your own seal character, product name, and signature.', 'close_b': 'Build a page', 'code': 'Code that includes the two files',
    },
}


def localized(tokens, en):
    """把 tokens.json 里写给人看的中文（用途、分组名）换成 source/en/tokens.json 里的英文。色值和名字不动。
    英文那份的键是路径：/color/tokens/bg/usage。缺一条就报错。"""
    def walk(o, p):
        if isinstance(o, list):
            return [walk(v, p) for v in o]
        if not isinstance(o, dict):
            return o
        key = o.get('name') or o.get('id')
        out = {}
        for k, v in o.items():
            if isinstance(v, str) and re.search(r'[\u3400-\u9fff]', v):
                path = '%s/%s:%s' % (p, k, v) if k == 'name' else ('%s/%s/%s' % (p, key, k) if key else '%s/%s' % (p, k))
                if path not in en:
                    sys.exit('缺英文稿：source/en/tokens.json 里没有 %s' % path)
                out[k] = en[path]
            else:
                out[k] = walk(v, p + '/' + k)
        return out
    return walk(tokens, '')


def size(path):
    n = os.path.getsize(path)
    return '%.0f&nbsp;KB' % (n / 1024) if n >= 1024 else '%d B' % n


def build():
    tokens = json.loads(read(SRC, 'tokens.json'))
    bundle = read(SRC, 'components', 'bundle.css')
    errors, warns = check(tokens, bundle)
    for w in warns:
        print('提醒：' + w)
    for e in errors:
        print('错误：' + e)
    if errors:
        sys.exit('核对没通过，没有生成任何文件。')
    print('令牌核对通过：%d 个令牌。' % len(token_names(tokens)))
    if '--check' in sys.argv:
        sys.exit(0)

    os.makedirs(DIST, exist_ok=True)
    for name, text in (('hairline.css', dist_css(tokens, bundle)), ('hairline.js', read(SRC, 'components', 'bundle.js')), ('tokens.json', read(SRC, 'tokens.json'))):
        with open(os.path.join(DIST, name), 'w', encoding='utf-8') as f:
            f.write(text)

    HTML_NAMES.update(token_names(tokens))
    TYPE_NAMES.update(type_names(tokens))
    SITE_NAMES.update(HTML_NAMES - set(re.findall(r'(?<![\w-])--([\w-]+)\s*:', SITE_CSS)))
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'assets'))
    comps = load_components()
    names = {c['name'] for c in comps}

    for name in ('hairline.css', 'hairline.js', 'tokens.json'):
        shutil.copy(os.path.join(DIST, name), os.path.join(OUT, 'assets', name))
    if os.path.isdir(STATIC):
        for name in sorted(os.listdir(STATIC)):
            if not name.startswith('.'):
                shutil.copy(os.path.join(STATIC, name), os.path.join(OUT, 'assets', name))
    write('assets/site.css', SITE_CSS)
    write('assets/site.js', SITE_JS)
    if os.path.isdir(os.path.join(SRC, 'assets')):
        shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(OUT, 'assets', 'files'))

    en_dir = os.path.join(SRC, 'en', 'assets')
    for name in sorted(os.listdir(en_dir)) if os.path.isdir(en_dir) else []:
        if name.endswith('.md') and os.path.isdir(os.path.join(OUT, 'assets', 'files', name[:-3])):
            shutil.copy(os.path.join(en_dir, name), os.path.join(OUT, 'assets', 'files', name[:-3], 'README.en.md'))
    tokens_en = localized(tokens, json.loads(read(SRC, 'en', 'tokens.json')))

    SAMPLES.update(c['name'].lower() for c in comps if c['name'].startswith('Sample'))
    global LANG
    for LANG in LANGS:
        tk = tokens_en if LANG == 'en' else tokens
        A = aroot('')
        H = HOME[LANG]
        groups = {}
        for c in comps:
            groups.setdefault(c['group'], []).append(c)
        order = [g for g in GROUP_ORDER if g in groups] + [g for g in groups if g not in GROUP_ORDER]
        gt = {s_: t for s_, t, _ in GUIDES}
        assert sorted(x for _, xs in GUIDE_GROUPS for x in xs) == sorted(gt)
        nav = [(g, [('guide/%s.html' % x, T(gt[x]), None) for x in xs]) for g, xs in GUIDE_GROUPS] + [
               ('令牌', [('tokens/%s.html' % s, T(t), None) for s, t in TOKENS])]
        for g in order:
            nav.append((g, [('components/%s.html' % c['name'].lower(), label(c), c['name'] if label(c) != c['name'] else None) for c in groups[g]]))

        def pn(href):
            mine = next(SECTION.get(sec, 'comp') for sec, items in nav if any(h == href for h, _, _ in items))
            seq = [(h, l) for sec, items in nav if SECTION.get(sec, 'comp') == mine for h, l, _ in items if h == href or not offlang(h)]
            i = [h for h, _ in seq].index(href)
            return (seq[i - 1] if i > 0 else None, seq[i + 1] if i + 1 < len(seq) else None)

        # 首页
        n_comp = len([c for c in comps if not c['frame']])
        # 图标的个数照图标页实际列出的数，不写死
        n_icon = len(set(re.findall(r'class="hao-icon hao-icon--([a-z-]+)"', next(c for c in comps if c['name'] == 'Icon')['preview'])))
        E = 'EN' if LANG == 'en' else ''   # 英文首页嵌英文的示例屏

        def shot(name, w, h, theme=None, label=''):
            follow = '' if theme else ' data-theme-follow'
            q = '?theme=%s' % theme if theme else ''
            return '<div class="shot" style="--w:%d;--h:%d" role="img" aria-label="%s"><iframe src="%spreview/%s.html%s"%s tabindex="-1" aria-hidden="true" scrolling="no"></iframe></div>' % (w, h, T(label), A, name, q, follow)

        def bare(x):
            return x.replace('class="shot"', 'class="shot shot--bare"')

        moons = ''.join('<span class="hao-moon%s" style="--p:%s"></span>' % (' hao-moon--done' if p == '1' else '', p) for p in ('.1', '.3', '.5', '.7', '.9', '1'))
        scene = '<svg class="hao-scene hao-scene--lg" viewBox="0 0 96 96" aria-hidden="true"><circle class="wash" cx="60" cy="36" r="13"/><path class="far" d="M8 70q7-4 14 0t14 0 14 0 14 0 14 0 14 0M14 79q7-4 14 0t14 0 14 0 14 0 14 0M24 88q7-4 14 0t14 0 14 0 14 0"/></svg>'
        rules = [
            ('<button class="restamp" type="button" aria-label="%s"><span class="hao-seal hao-seal--xl" aria-hidden="true" lang="zh">印</span></button>' % T('再盖一次印'), T('朱砂一处'), T('一屏里红色只出现一次：一方印、一个角标、一个删除按钮、一次盖印，四者取一。')),
            (scene, T('一屏一景'), T('纹样、小品、装裱这类「景」，一屏至多一个。办事的页面一个都不放。')),
            ('<span class="hao-row" style="gap:var(--space-3)" role="img" aria-label="%s">%s</span>' % (T('月相进度，从朔到望'), moons), T('形随控件'), T('进度是一轮渐圆的月，勾是一笔提勾。控件自己的形状可以有意味，但同类只用一种。')),
        ]
        icons = ''.join('<i class="hao-icon hao-icon--%s" style="--n:%d"></i>' % (x, i) for i, x in enumerate(('search', 'calendar', 'bell', 'bookmark', 'edit', 'folder', 'image', 'mail', 'clock', 'share', 'settings', 'send')))
        swatches = ''.join('<span class="cell__sw" style="background:var(--%s);--n:%d"></span>' % (x, i) for i, x in enumerate(('tint', 'tint-wash', 'jade', 'amber', 'gold', 'ink')))
        cells = [
            (T('组件'), T('%d 个，从按钮到手卷。每个都有中文和英文两种效果。') % n_comp, 'components/button.html', T('浏览组件'),
             '<button class="hao-btn" type="button" tabindex="-1">%s</button><button class="hao-btn hao-btn--tinted" type="button" tabindex="-1">%s</button><span class="hao-moon hao-moon--lg" style="--p:.62"></span>' % (T('保存修改'), T('存为草稿'))),
            (T('图标'), T('%d 个，1.5px 的圆头线。封闭的轮廓都留一个小缺口，叫「留气口」。') % n_icon, 'components/icon.html', T('看全部图标'), '<span class="cell__icons">%s</span>' % icons),
            (T('色彩'), T('石青行事，朱砂点睛。每个颜色都有昼、夜两个值。'), 'tokens/color.html', T('看色彩令牌'), swatches),
            (T('字体'), T('标题用宋体，正文用黑体。英文另有一档标题样式。'), 'tokens/type.html', T('看字体样式'), '<span class="cell__type"><span style="--n:0" lang="zh-CN">永</span><span lang="en" style="--n:3">Aa</span></span>'),
        ]
        files = '<dl class="facts__n"><div><dt>%s</dt><dd>%d</dd></div><div><dt>%s</dt><dd>%d</dd></div><div><dt>%s</dt><dd>2</dd></div></dl>' % (T('个组件'), n_comp, T('个图标'), n_icon, T('个文件'))
        home = """<section class="hero"><div class="hero__in container">
<div class="hero__text">
<h1><span class="hero__glyph" lang="zh-CN">毫</span><span class="hero__rule" aria-hidden="true"><span class="hero__ink"></span><span class="hero__pen"><svg class="hero__brush brandmark" viewBox="0 0 120 720" aria-hidden="true"><path class="rod" d="M60 4a9 9 0 1 0 6.400 2.600M60 22v8M53 30h14M53 30V520M67 30V520M53 168h14M53 172h14M53 352h14M53 356h14M50 520h20M50 520l-4 40M70 520l4 40M46 560h28M48 534h24"/><path class="tip" d="M46 560C39 612 50 672 60 714C70 672 81 612 74 560"/><path class="hair" d="M53 562C50 618 55 678 60 710M60 562V706M67 562C70 618 65 678 60 710"/></svg></span></span><span class="hero__name" lang="en">Hairline</span></h1>
<p class="hero__tag">%(tag)s</p>
<div class="hero__a"><a class="hao-btn" href="guide/install.html">%(start)s</a><a class="hao-btn hao-btn--plain" href="components/button.html">%(browse)s</a></div>
</div>
<div class="hero__shot">%(shot)s</div>
</div></section>

<section class="sec sec--2 sec--s"><div class="container g12 facts" data-reveal>
<p class="facts__p">%(facts)s</p>
%(files)s
</div></section>

<section class="sec"><div class="container g12 rules" data-reveal>
<div class="rules__head">
<h2 class="sec__h">%(rules_h)s</h2>
<p class="sec__p">%(rules_p)s</p>
<p class="sec__a"><a class="hao-link hao-link--go" href="guide/principles.html">%(rules_a)s</a></p>
</div>
<div class="rules__rows">%(rules)s</div>
</div></section>

<section class="sec sec--s night" data-theme="dark"><div class="container g12" data-reveal>
<div class="night__text">
<h2 class="sec__h">%(night_h)s</h2>
<p class="sec__p">%(night_p)s</p>
<p class="sec__a"><a class="hao-link hao-link--go" href="tokens/color.html">%(night_a)s</a></p>
<div class="night__seg"><span class="hao-seg" role="radiogroup" aria-label="%(night_seg)s"><label><input type="radio" name="night-theme" value="light"><span>%(day)s</span></label><label><input type="radio" name="night-theme" value="dark" checked><span>%(night)s</span></label></span></div>
</div>
<div class="night__shots">%(shots3)s</div>
</div></section>

<section class="sec sec--2"><div class="container g12 duo" data-reveal>
<h2 class="sec__h duo__h">%(duo_h)s</h2>
<div class="duo__side">
<p class="sec__p">%(duo_p)s</p>
<p class="sec__a"><a class="hao-link hao-link--go" href="guide/english.html">%(duo_a)s</a></p>
</div>
<div class="duo__shots">%(duo)s</div>
</div></section>

<div class="sec sec--s"><div class="container"><div class="index" data-reveal>%(cells)s</div></div></div>

<section class="sec sec--3 sec--s close"><div class="container g12" data-reveal>
<div class="close__text">
<h2 class="sec__h">%(close_h)s</h2>
<p class="sec__p">%(close_p)s</p>
<div class="hero__a"><a class="hao-btn" href="guide/install.html">%(start)s</a><a class="hao-btn hao-btn--plain" href="guide/quickstart.html">%(close_b)s</a></div>
</div>
<div class="close__code"><pre class="code" tabindex="0" aria-label="%(code)s"><code>%(snippet)s</code></pre>%(dl)s</div>
</div>
<div class="hao-wave site-wave" role="presentation"></div>
</section>""" % dict(
            H,
            shot=shot('SampleDashboard' + E, 1200, 860, None, '数据页示例'),
            files=files,
            rules=''.join('<div class="rule3"><div class="rule3__t"><h3>%s</h3><p>%s</p></div><div class="rule3__v">%s</div></div>' % (r[1], r[2], r[0]) for r in rules),
            shots3=bare(shot('SampleSettings' + E, 430, 840, 'dark', '设置页示例，夜间主题')) + bare(shot('SampleScreen' + E, 430, 792, 'dark', '首页示例，夜间主题')) + bare(shot('SampleArticle' + E, 430, 840, 'dark', '文章页示例，夜间主题')),
            # 大的那张是这一页的语言，小的那张是另一种
            duo=''.join('<figure>%s<figcaption lang="%s">%s</figcaption></figure>' % f for f in sorted([
                (shot('SampleWeb', 1200, 820, None, '网页示例，中文'), 'zh-CN', '中文'), (shot('SampleWebEN', 1200, 820, None, '网页示例，英文'), 'en', 'English')], key=lambda f: (f[1] == 'en') != (LANG == 'en'))),
            cells=''.join('<section class="cell"><h3>%s</h3><div class="cell__t"><p>%s</p><a class="hao-link hao-link--go cell__a" href="%s">%s</a></div><div class="cell__v" aria-hidden="true" inert>%s</div></section>' % (c[0], c[1], c[2], c[3], c[4]) for c in cells),
            snippet=highlight('<link rel="stylesheet" href="hairline.css">\n\n<!-- %s -->\n\n<script src="hairline.js"></script>' % T('页面内容')),
            dl='<ul class="close__files">%s</ul>' % ''.join('<li><a class="hao-link" href="%sassets/%s" download><code>%s</code></a><span>%s</span><span class="hao-num">%s</span></li>' % (A, f, f, T(d), size(os.path.join(OUT, 'assets', f))) for f, d in (('hairline.css', '令牌和全部组件的样式'), ('hairline.js', '弹窗、菜单、月历等组件的行为'))))
        write('index.html', shell('index.html', T('设计系统'), home, nav, None, home=True))
        # 404：照「偏」排，话在左上，一叶舟偏在右下；下面接全站目录。舟是「找不到」那幅小品，这一页不再放别的景
        lost = '''<section class="sec lost"><div class="container g12">
<div class="lost__text"><h1 class="sec__h">%s</h1><p class="sec__p">%s</p>
<p class="hero__a"><a class="hao-btn hao-btn--tinted" href="index.html">%s</a><a class="hao-btn hao-btn--plain" href="components/button.html">%s</a></p></div>
<svg class="hao-scene hao-scene--lg lost__scene" viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M4 50l14-10 10 6 14-14 16 16 12-7 22 11"/><path d="M30 62h36l-6 8H36zM40 62q8-13 16 0M48 49V38"/><path class="far" d="M12 78h20M40 80h28M74 77h12M26 87h18M54 88h20"/></svg>
</div></section>''' % (T('没有这一页'), T('地址可能写错了，或者这一页已经搬走。可以在下面的目录里找。'), T('回首页'), T('浏览组件'))
        page404 = shell('404.html', T('没有这一页'), lost, nav, None, home=True).replace('<title>%s</title>' % T('毫 Hairline 设计系统'), '<title>%s</title>' % (T('没有这一页') + T(' · 毫 Hairline')), 1).replace('<script>', '<meta name="robots" content="noindex">\n<script>', 1)
        if SITE_URL:   # 404 页会在任何一层地址上被送出来，相对路径要有个固定的起点
            page404 = page404.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="%s/%s">' % (SITE_URL.rstrip('/'), 'en/' if LANG == 'en' else ''), 1)
        write('404.html', page404)


        # 指南
        for slug, title, src in GUIDES:
            rel = 'guide/%s.html' % slug
            if slug == 'install':
                body = (INSTALL_EN if LANG == 'en' else INSTALL) % {'files': aroot('../'), 'css': size(os.path.join(OUT, 'assets/hairline.css')), 'js': size(os.path.join(OUT, 'assets/hairline.js')), 'tk': size(os.path.join(OUT, 'assets/tokens.json')), 'snippet': highlight(SNIPPET_EN if LANG == 'en' else SNIPPET)}
            elif slug == 'quickstart':
                body = (QUICK_EN % {'page': highlight(PAGE_EN)}) if LANG == 'en' else (QUICK % {'page': highlight(PAGE)})
            else:
                if LANG == 'en' and not os.path.isfile(os.path.join(SRC, 'en', src)):
                    sys.exit('缺英文稿：source/en/%s' % src)
                text = md(read(SRC, 'en', src) if LANG == 'en' else read(SRC, src), '../', names).lstrip()
                if text.startswith('<p>'):
                    text = '<p class="site-lead">' + text[3:]
                body = '<h1>%s</h1>%s' % (T(title), text)
            write(rel, shell(rel, T(title), body, nav, rel, pn(rel)))

        # 令牌
        themes = [x['id'] for x in tk['color']['themes']]

        def tv(v):
            return v if isinstance(v, str) else ' / '.join(v.get(t, '') for t in themes)
        color = T('<h1>色彩</h1><p class="site-lead">所有颜色都是令牌，写成 <code>var(--名字)</code>。每个令牌有昼、夜两个值，下面色块显示的是当前主题的值，文字里依次是昼和夜。</p>') + '<div class="tk-grid">%s</div>' % ''.join(
            '<div class="tk"><div class="tk__sw" style="background:var(--%s)"></div><div class="tk__b"><div class="tk__n">%s</div><div class="tk__v">%s</div><div class="tk__u">%s</div></div></div>' % (x['name'], x['name'], html.escape(tv(x['value'])), han(html.escape(x.get('usage', '')))) for x in tk['color']['tokens'])
        write('tokens/color.html', shell('tokens/color.html', T('色彩'), color, nav, 'tokens/color.html', pn('tokens/color.html'), wide=True))
        ty = T('<h1>字体</h1><p class="site-lead">标题用衬线（中文思源宋体，西文 Newsreader），正文和控件用黑体。每个样式都有一个同名的类，直接写在元素上。</p>')
        if tk['type'].get('note'):
            ty += '<p>%s</p>' % han(html.escape(tk['type']['note']))
        for g in tk['type']['groups']:
            ty += '<h2>%s</h2>' % g['name']
            for s in g['styles']:
                lang = ' lang="en"' if re.match(r'[A-Za-z]', s.get('sample', '')) else (' lang="zh-CN"' if LANG == 'en' else '')
                ty += '<div class="ty"><div class="ty__m"><b>.%s</b>%s<br>%s</div><div class="%s"%s>%s</div></div>' % (s['name'], T('%s / %s，字重 %s') % (s['fontSize'], s['lineHeight'], s['fontWeight']), han(html.escape(s.get('usage', ''))), s['name'], lang, html.escape(s.get('sample', s['name'])))
        write('tokens/type.html', shell('tokens/type.html', T('字体'), ty, nav, 'tokens/type.html', pn('tokens/type.html')))
        sp = T('<h1>间距与圆角</h1><p class="site-lead">间距走 4px 的格。圆角按元素大小分档，大容器套小元素时，里面的圆角比外面小一档。</p><h2>间距</h2>')
        sp += ''.join('<div class="sp"><code>--%s</code><span class="sp__bar" style="width:%s"></span><span class="ty__m">%s</span></div>' % (x['name'], x['value'], T('%s，%s') % (x['value'], html.escape(x['usage']))) for x in tk['spacing']['tokens'])
        sp += T('<h2>圆角</h2>') + ''.join('<div class="sp"><code>--%s</code><span class="sp__box" style="border-radius:var(--%s)"></span><span class="ty__m">%s</span></div>' % (x['name'], x['name'], T('%s，%s') % (x['value'], html.escape(x['usage']))) for x in tk['radius']['tokens'])
        for key, title in (('breakpoint', '断点'), ('layout', '布局')):
            if key in tk:
                sp += '<h2>%s</h2><div class="hao-table-wrap"><table class="hao-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (T(title), T('<th scope="col">令牌</th><th scope="col">值</th><th scope="col">用途</th>'), ''.join('<tr><td><code>--%s</code></td><td class="hao-num">%s</td><td>%s</td></tr>' % (x['name'], x['value'], html.escape(x['usage'])) for x in tk[key]['tokens']))
        write('tokens/space.html', shell('tokens/space.html', T('间距与圆角'), sp, nav, 'tokens/space.html', pn('tokens/space.html')))
        sh = T('<h1>阴影与层级</h1><p class="site-lead">阴影只有三种，都很淡。能用留白和底色的差别分出层次时，不加阴影。</p>') + '<div class="sh">%s</div>' % ''.join('<div class="sh__c" style="box-shadow:var(--%s)"><div class="tk__n">--%s</div><div class="tk__u">%s</div></div>' % (x['name'], x['name'], html.escape(x['usage'])) for x in tk['shadow']['tokens'])
        for key, title in (('zIndex', '层级'), ('opacity', '不透明度'), ('motion', '动效')):
            if key in tk:
                sh += '<h2>%s</h2><div class="hao-table-wrap"><table class="hao-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (T(title), T('<th scope="col">令牌</th><th scope="col">值</th><th scope="col">用途</th>'), ''.join('<tr><td><code>--%s</code></td><td class="hao-num">%s</td><td>%s</td></tr>' % (x['name'], x['value'], html.escape(x['usage'])) for x in tk[key]['tokens']))
        write('tokens/shadow.html', shell('tokens/shadow.html', T('阴影与层级'), sh, nav, 'tokens/shadow.html', pn('tokens/shadow.html')))

        # 组件
        for c in comps:
            rel = 'components/%s.html' % c['name'].lower()
            readme = c['readme_en'] if LANG == 'en' else c['readme']
            parts = readme.strip().split('\n\n', 1)
            lead = parts[0].strip() if parts and parts[0] and not parts[0].startswith(('#', '-', '|')) else ''
            rest = parts[1] if lead and len(parts) > 1 else ('' if lead else readme)
            body = '<h1>%s%s</h1>%s<h2 id="demo">%s</h2>%s%s' % (label(c), '<small lang="en">%s</small>' % c['name'] if label(c) != c['name'] else '', '<p class="site-lead">%s</p>' % md(lead, '../', names).replace('<p>', '').replace('</p>', '') if lead else '', T('演示'), demo(c, '../'), ('<h2 id="usage">%s</h2>' % T('用法') + md(rest, '../', names)) if rest.strip() else '')
            write(rel, shell(rel, '%s %s' % (label(c), c['name']) if label(c) != c['name'] else c['name'], body, nav, rel, pn(rel), wide=bool(c['width'])))
            # 每个组件都出一张独立的预览页：示例屏嵌在文档页里用它，其余的用来单独打开、逐个核对中英文和昼夜
            head = '<script>%s</script><link rel="stylesheet" href="../assets/hairline.css"><script src="../assets/hairline.js" defer></script>' % THEME_BOOT
            if LANG == 'zh':
                write('preview/%s.html' % c['name'], c['preview'].replace('</head>', head + '</head>', 1))
        llms(nav, comps)
    LANG = 'zh'
    return len(comps), sum(len(items) for _, items in nav)


if __name__ == '__main__':
    n, pages = build()
    print('已生成 %d 个组件页，每种语言 %d 页，中文在 %s，英文在 %s' % (n, pages + 2, OUT, os.path.join(OUT, 'en')))
