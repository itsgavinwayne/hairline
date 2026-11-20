#!/usr/bin/env python3
"""统计样式表里没走令牌的散值（字体属性不算），按种类列出数值、次数和出现的地方。在仓库根目录运行：

    python3 tools/scatter.py
"""
import re,collections,sys
css=open('source/components/bundle.css',encoding='utf-8').read()
css=re.sub(r'url\("data:[^"]*"\)','url(DATA)',css)
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
FONT={'font','font-size','line-height','letter-spacing','font-weight','font-family','font-variant-numeric','font-style'}
cat=collections.defaultdict(lambda: collections.defaultdict(list))
# crude rule parse
for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',css):
    sel=m.group(1).strip().split('\n')[-1].strip()[:60]
    for d in m.group(2).split(';'):
        if ':' not in d: continue
        p,v=d.split(':',1); p=p.strip(); v=v.strip()
        if p in FONT or p.startswith('--i'): continue
        if p in('transition','animation','animation-duration','animation-delay','transition-duration'):
            for x in re.findall(r'(?<![\w-])(\d*\.?\d+m?s)\b',v): cat['时长'][x].append(sel)
            for x in re.findall(r'\b(ease-out|ease-in|ease-in-out|linear|ease)\b(?!\))',re.sub(r'var\([^)]*\)','',v)): cat['曲线'][x].append(sel)
            continue
        if p=='opacity':
            if 'var(' not in v: cat['不透明度'][v].append(sel)
            continue
        if p=='z-index':
            if 'var(' not in v: cat['层级'][v].append(sel)
            continue
        if 'radius' in p:
            vv=re.sub(r'var\([^)]*\)','',v)
            if re.search(r'\d',vv): cat['圆角'][v].append(sel)
            continue
        if p in('border','border-width','border-top','border-bottom','outline','stroke-width','border-top-color') or p.startswith('border-') :
            for x in re.findall(r'(?<![\w.-])(\d*\.?\d+px)',v): cat['描边粗细('+p.split('-')[0]+')'][x].append(sel)
            if p=='stroke-width': cat['描边粗细(stroke)'][v].append(sel)
            continue
        if p=='box-shadow':
            vv=re.sub(r'var\(--shadow[^)]*\)','',v)
            if 'inset' in vv:
                for x in re.findall(r'(\d*\.?\d+px)\s+var',vv): cat['描边粗细(inset 线)'][x].append(sel)
            elif re.search(r'\d',vv): cat['阴影(自写)'][v[:50]].append(sel)
            continue
        if p in('padding','margin','gap','row-gap','column-gap') or p.startswith('padding-') or p.startswith('margin-'):
            vv=re.sub(r'var\([^)]*\)|calc\([^;]*\)','',v)
            for x in re.findall(r'(-?\d*\.?\d+px)',vv): cat['间距('+p.split('-')[0]+')'][x].append(sel)
            continue
        if p in('width','height','min-width','min-height','max-width','max-height'):
            vv=re.sub(r'var\([^)]*\)|calc\([^;]*\)|min\([^;]*\)','',v)
            for x in re.findall(r'(\d*\.?\d+px)',vv): cat['尺寸('+('h' if 'height' in p else 'w')+')'][x].append(sel)
            continue
        if p in('top','left','right','bottom','inset','outline-offset','text-underline-offset','text-decoration-thickness'):
            vv=re.sub(r'var\([^)]*\)|calc\([^;]*\)','',v)
            for x in re.findall(r'(-?\d*\.?\d+px)',vv): cat['偏移('+p+')'][x].append(sel)
            continue
        if re.search(r'#[0-9a-fA-F]{3,8}\b|rgba?\(',v): cat['颜色'][v[:40]].append(sel)
        if 'blur(' in v: cat['模糊'][v].append(sel)
        if 'scale(' in v and p=='transform': cat['缩放'][v].append(sel)
tot=0
for c in sorted(cat):
    n=sum(len(x) for x in cat[c].values()); tot+=n
    print('\n## %s  共 %d 处'%(c,n))
    for v,s in sorted(cat[c].items(), key=lambda kv:-len(kv[1])):
        print('  %-28s ×%-3d %s'%(v,len(s),' | '.join(sorted(set(s))[:4])+(' …' if len(set(s))>4 else '')))
print('\n总计',tot)
