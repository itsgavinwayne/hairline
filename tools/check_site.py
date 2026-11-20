#!/usr/bin/env python3
"""核对生成出来的文档站（先运行 python3 build_site.py）。不需要安装任何依赖：

    python3 tools/check_site.py          链接、中英文页面是否一一对应、语言标记
    python3 tools/check_site.py --han    另外列出英文页里的汉字，给人逐条看是不是有意保留

查四件事：
1. 中文页和英文页数量一致，一页对一页。
2. 全站的 href、src 指向的文件都在，#锚点 在目标页里有对应的 id。
3. 每页的 <html lang>、三条 hreflang、语言切换链接都写对了。
4. 英文页里的汉字都包在标了 lang="zh…" 的元素里（演示里的中文栏、印章、括注）；没包的算漏翻。
"""
import os, re, sys
from html.parser import HTMLParser
from urllib.parse import unquote

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(HERE, 'site')
HAN = re.compile(r'[㐀-鿿]')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr', 'path', 'circle', 'rect'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.alts, self.bare = set(), [], {}, []
        self.lang, self.switch = None, None
        self.stack = []      # (标签, 这一层生效的语言)
        self.skip = 0

    def cur(self):
        return self.stack[-1][1] if self.stack else self.lang

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if 'id' in a:
            self.ids.add(a['id'])
        for k in ('href', 'src'):
            if a.get(k):
                self.refs.append(a[k])
        if tag == 'link' and a.get('rel') == 'alternate' and a.get('hreflang'):
            self.alts[a['hreflang']] = a.get('href')
        if tag == 'a' and 'site-lang' in (a.get('class') or ''):
            self.switch = (a.get('href'), a.get('lang'), a.get('hreflang'))
        lang = a.get('lang') or self.cur()
        for k in ('aria-label', 'title', 'placeholder', 'alt', 'content'):
            if a.get(k) and HAN.search(a[k]) and not (lang or '').startswith('zh'):
                self.bare.append('%s="%s"' % (k, a[k]))
        if tag in ('script', 'style'):
            self.skip += 1
        if tag not in VOID:
            self.stack.append((tag, lang))

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.skip or not HAN.search(data):
            return
        if not (self.cur() or '').startswith('zh'):
            # 代码里的汉字（示例文案）不算漏翻，但也列出来
            where = '代码' if any(t in ('code', 'pre') for t, _ in self.stack) else '正文'
            self.bare.append('%s：%s' % (where, data.strip()[:80]))


def main():
    pages = {}
    for dp, _, fs in os.walk(SITE):
        for f in fs:
            if f.endswith('.html'):
                p = os.path.join(dp, f)
                page = Page()
                page.feed(open(p, encoding='utf-8').read())
                pages[os.path.relpath(p, SITE)] = page
    bad = []
    zh = sorted(r for r in pages if not r.startswith(('en/', 'preview/')))
    en = sorted(r[3:] for r in pages if r.startswith('en/'))
    if zh != en:
        bad.append('中英文页面对不上：只有中文 %s；只有英文 %s' % (sorted(set(zh) - set(en)), sorted(set(en) - set(zh))))
    links = 0
    for rel, page in sorted(pages.items()):
        base = os.path.dirname(os.path.join(SITE, rel))
        for ref in page.refs:
            if re.match(r'(https?:|mailto:|data:|javascript:)', ref):
                continue
            path, _, frag = ref.partition('#')
            path = unquote(path.split('?')[0])
            target = os.path.normpath(os.path.join(base, path)) if path else os.path.join(SITE, rel)
            links += 1
            if not os.path.isfile(target):
                bad.append('%s：链接坏了 %s' % (rel, ref))
            elif frag and target.endswith('.html'):
                t = pages.get(os.path.relpath(target, SITE))
                if t and unquote(frag) not in t.ids:
                    bad.append('%s：锚点不存在 %s' % (rel, ref))
        if rel.startswith('preview/'):
            continue
        is_en = rel.startswith('en/')
        twin = rel[3:] if is_en else 'en/' + rel
        if page.lang != ('en' if is_en else 'zh-CN'):
            bad.append('%s：<html lang> 是 %s' % (rel, page.lang))
        res = lambda href: os.path.relpath(os.path.normpath(os.path.join(base, href)), SITE) if href and not href.startswith('http') else href
        want = {'zh-CN': rel[3:] if is_en else rel, 'en': rel if is_en else 'en/' + rel, 'x-default': rel[3:] if is_en else rel}
        for k, v in want.items():
            if res(page.alts.get(k)) != v:
                bad.append('%s：hreflang %s 指向 %s，应为 %s' % (rel, k, page.alts.get(k), v))
        if not page.switch or res(page.switch[0]) != twin or page.switch[1] != ('zh-CN' if is_en else 'en') or page.switch[1] != page.switch[2]:
            bad.append('%s：语言切换链接不对 %s' % (rel, page.switch))
        if is_en:
            leaks = [b for b in page.bare if not b.startswith('代码')]
            for b in leaks:
                bad.append('%s：英文页里有没标语言的汉字 %s' % (rel, b))
            if '--han' in sys.argv:
                for b in page.bare:
                    if b.startswith('代码'):
                        print('%s　%s' % (rel, b))
    for b in bad:
        print('✗ ' + b)
    print('%d 页（中文 %d，英文 %d，预览 %d），%d 个链接，%d 处问题。' % (len(pages), len(zh), len(en), len(pages) - len(zh) - len(en), links, len(bad)))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
