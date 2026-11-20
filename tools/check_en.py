#!/usr/bin/env python3
"""核对 source/en/ 里的英文稿和中文稿对得上。不需要安装任何依赖：

    python3 tools/check_en.py            全部核对
    python3 tools/check_en.py Button seal  只核对名字里含这些词的文件

逐份比较：标题、表格行、列表条数、代码块是否与中文稿一致；反引号里的代码有没有丢；
有没有感叹号、直引号、全大写的词、*斜体*；残留的汉字逐行列出来给人看（括注、印章用字是允许的）。
"""
import os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, 'source')
EN = os.path.join(SRC, 'en')
HAN = re.compile(r'[㐀-鿿]')
BANNED = re.compile(r'\b(zen|harmony|harmonious|journey|ancient wisdom|oriental|mystical|timeless|oops|whoops)\b', re.I)
# 全大写但本来就该大写的词
CAPS_OK = {'OS', 'CSS', 'HTML', 'SVG', 'JSON', 'PNG', 'JPG', 'PDF', 'URL', 'CDN', 'API', 'UI', 'UX', 'AM', 'PM', 'SC', 'TC', 'KB', 'MB', 'ARIA', 'WCAG', 'AA', 'AAA', 'CMYK', 'RGB', 'DPI', 'PPI', 'ID', 'OK', 'EN', 'LW', 'ESC', 'TAB', 'NPM', 'IBM', 'CJK', 'GB', 'ISO', 'RTL', 'LTR', 'DOM', 'JS', 'SF', 'II', 'III', 'IV', 'XL', 'CTA', 'FAQ', 'QR', 'HIG', 'CEO', 'TV', 'PC', 'A4', 'A3', 'HSL', 'P3', 'ICC', 'VS', 'MDN', 'USA', 'UK', 'SAVE', 'CHANGES', 'SIL', 'GOV', 'WAI', 'OFL'}


def pairs():
    out = []
    for n in sorted(os.listdir(SRC)):
        if n.endswith('.md'):
            out.append((os.path.join(SRC, n), os.path.join(EN, n)))
    for n in sorted(os.listdir(os.path.join(SRC, 'components'))):
        p = os.path.join(SRC, 'components', n, 'README.md')
        if os.path.isfile(p):
            out.append((p, os.path.join(EN, 'components', n + '.md')))
    for n in sorted(os.listdir(os.path.join(SRC, 'assets'))):
        p = os.path.join(SRC, 'assets', n, 'README.md')
        if os.path.isfile(p):
            out.append((p, os.path.join(EN, 'assets', n + '.md')))
    return out


def shape(text):
    lines = text.split('\n')
    fence = sum(1 for l in lines if l.startswith('```'))
    return {
        '标题': [len(l.split(' ')[0]) for l in lines if re.match(r'#{1,4} ', l)],
        '表格行': sum(1 for l in lines if l.startswith('|')),
        '列表条': sum(1 for l in lines if re.match(r'(- |\d+\. )', l)),
        '代码块': fence // 2,
        '段落': len([b for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]),
    }


def codes(text):
    """反引号里的代码：令牌名、类名、属性名。并列的写法（、和 , ）算同一种。"""
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    return sorted(c.replace('、', ', ') for c in re.findall(r'`([^`]+)`', text))


def prose(text):
    """去掉代码之后的正文。"""
    return re.sub(r'`[^`]*`', '', re.sub(r'```.*?```', '', text, flags=re.S))


def main():
    want = [w.lower() for w in sys.argv[1:]]
    bad = missing = 0
    for zh, en in pairs():
        rel = os.path.relpath(en, HERE)
        if want and not any(w in rel.lower() for w in want):
            continue
        if not os.path.isfile(en) or not open(en, encoding='utf-8').read().strip():
            print('缺：%s' % rel)
            missing += 1
            continue
        a, b = open(zh, encoding='utf-8').read(), open(en, encoding='utf-8').read()
        notes = []
        sa, sb = shape(a), shape(b)
        for k in sa:
            if sa[k] != sb[k]:
                notes.append('%s对不上：中文 %s，英文 %s' % (k, sa[k], sb[k]))
        ca, cb = codes(a), codes(b)
        # 中文稿里带汉字的代码是占位（data-hao-tip="文字"），英文稿里要译成英文占位，所以只比个数
        slots = len([c for c in ca if HAN.search(c)])
        ca = [c for c in ca if not HAN.search(c)]
        left = [c for c in cb if HAN.search(re.sub(r'>(印|初十)<', '', c))]   # 印章上的字、农历日期本来就是汉字
        if left:
            notes.append('代码里的占位还是中文：%s' % '、'.join('`%s`' % c for c in left))
        lost = [c for c in set(ca) if ca.count(c) > cb.count(c)]
        extra = [c for c in set(cb) if cb.count(c) > ca.count(c) and not HAN.search(c)]
        if len(lost) == 0 and sum(cb.count(c) - ca.count(c) for c in extra) <= slots:
            extra = []
        if lost:
            notes.append('少了代码：%s' % '、'.join('`%s`' % c for c in sorted(lost)))
        if extra:
            notes.append('多了代码：%s' % '、'.join('`%s`' % c for c in sorted(extra)))
        p = prose(b)
        if '!' in p.replace('![', '') or '！' in p:
            notes.append('有感叹号')
        if re.search(r'["\']', re.sub(r'<[^>]+>', '', p)):
            notes.append('有直引号或直撇号：%s' % '；'.join(l.strip()[:60] for l in p.split('\n') if re.search(r'["\']', re.sub(r'<[^>]+>', '', l)))[:300])
        if re.search(r'(?<![\w*])\*[^*\s][^*]*\*(?!\*)', p) or re.search(r'(?<!\w)_[^_\s][^_]*_(?!\w)', p):
            notes.append('有 *斜体* 或 _斜体_，生成脚本不认')
        caps = sorted({w for w in re.findall(r'\b[A-Z]{2,}\b', p) if w not in CAPS_OK})
        if caps:
            notes.append('全大写的词：%s' % '、'.join(caps))
        # english.md 讲的就是哪些词不能用、中文例子怎么写，它引用这些词和中文标点是有意的
        quoting = os.path.basename(en) == 'english.md'
        m = BANNED.search(p)
        if m and not quoting:
            notes.append('不该出现的词：%s' % m.group(0))
        if re.search(r'[，。、；：「」（）]', re.sub(r'[\u3400-\u9fff][^|]*', '', p)) and not quoting:
            notes.append('有中文标点')
        for l in b.split('\n'):
            if l.startswith('#') and re.search(r'#+ .*[a-z] [A-Z][a-z]+ [A-Z][a-z]', l):
                notes.append('标题可能不是句首大写：%s' % l)
        han = [l.strip() for l in b.split('\n') if HAN.search(l)]
        if notes or han:
            print('\n%s' % rel)
            for n in notes:
                print('  ✗ ' + n)
                bad += 1
            for l in han:
                print('  汉字（请人看是否有意保留）：%s' % (l if len(l) < 150 else l[:150] + '…'))
    print('\n%d 处要改，缺 %d 份。' % (bad, missing))
    sys.exit(1 if bad or missing else 0)


if __name__ == '__main__':
    main()
