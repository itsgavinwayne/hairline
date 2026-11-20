#!/usr/bin/env python3
"""给每个组件的独立预览页截图，用来逐个核对中英文和昼夜效果。需要本机有 Chrome，并且文档站的预览服务开着。

    python3 tools/shots.py 输出目录 [light|dark] [倍率，默认 2] [组件名 ...]

先运行 python3 build_site.py，并启动预览配置 hairline-site（端口 4173）。
每个组件一张图，高度取预览第一行 @dsCard 里写的高度。不写组件名就是全部（示例屏除外，它们各有固定的尺寸）。
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BASE = os.environ.get('HAO_PREVIEW', 'http://localhost:4173/preview/')   # 端口被占时：HAO_PREVIEW=http://localhost:4183/site/preview/


def main():
    out = sys.argv[1]
    theme = sys.argv[2] if len(sys.argv) > 2 else 'light'
    scale = sys.argv[3] if len(sys.argv) > 3 else '2'
    only = sys.argv[4:]
    os.makedirs(out, exist_ok=True)
    comps = os.path.join(HERE, 'source', 'components')
    for name in sorted(os.listdir(comps)):
        prev = os.path.join(comps, name, 'preview.html')
        if not os.path.isfile(prev):
            continue
        if only and name not in only:
            continue
        if not only and (name.startswith('Sample') or name == 'Cover'):
            continue
        with open(prev, encoding='utf-8') as f:
            m = re.search(r'@dsCard[^>]*height=(\d+)', f.readline())
        height = int(m.group(1)) + 48 if m else 600
        target = os.path.join(out, '%s-%s.png' % (name, theme))
        subprocess.run([CHROME, '--headless=new', '--hide-scrollbars', '--force-device-scale-factor=%s' % scale,
                        '--window-size=800,%d' % height, '--virtual-time-budget=6000',
                        '--screenshot=%s' % target, '%s%s.html?theme=%s' % (BASE, name, theme)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(name, height, 'ok' if os.path.isfile(target) else 'FAILED')


if __name__ == '__main__':
    main()
