#!/usr/bin/env python3
"""一条命令跑完全部检查。不需要安装任何依赖，浏览器那两步需要本机有 Chrome 或 Chromium。

    python3 tools/check_all.py                 全部
    python3 tools/check_all.py --no-browser    只跑不用浏览器的几步（生成、译稿、站点、版本号）

依次做：
1. python3 build_site.py        核对令牌，生成 site/ 和 dist/
2. dist/ 和 skills/ 是否最新     重新生成技能包；改了 source/ 却忘了把这两处一起提交时报错
3. 版本号                        package.json 的 version 要和 bundle.js 里那一处相同
4. tools/check_en.py             英文稿和中文稿的结构
5. tools/check_site.py           链接、锚点、语言标记、中英文页面对应
6. tests/behavior.html           行为测试，无头浏览器里跑
7. tests/audit.html              溢出、裁切、对比度、单字居中，无头浏览器里跑

有一步没过，退出码就不是 0。Chrome 的位置可以用环境变量 HAO_CHROME 指定。
"""
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 审计页里按设计就该报的情况：这些预览是固定尺寸的整幅画面，不随窗口缩。
# 写法：(组件名的正则, 问题开头的文字, 原因)。只放「本来如此」的，不要拿来压真问题。
AUDIT_OK = [
    (r'^Cover$', '横向溢出', '封面是固定 960 宽的整幅画面'),
    (r'^Sample(Screen|Article|Form|Settings)(EN)?$', '横向溢出', '手机示例屏固定 412 宽，在 375 的窗口里必然超出'),
]

REPORTS = {}
GOT = threading.Event()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def do_POST(self):
        if not self.path.startswith('/__report'):
            self.send_error(404)
            return
        body = self.rfile.read(int(self.headers.get('Content-Length') or 0))
        try:
            REPORTS['data'] = json.loads(body.decode('utf-8'))
        except ValueError:
            REPORTS['data'] = None
        GOT.set()
        self.send_response(204)
        self.end_headers()

    def log_message(self, *a):
        pass


def find_chrome():
    cands = [os.environ.get('HAO_CHROME'),
             '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
             '/Applications/Chromium.app/Contents/MacOS/Chromium']
    cands += [shutil.which(n) for n in ('google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'chrome')]
    for c in cands:
        if c and os.path.isfile(c):
            return c
    return None


def in_browser(chrome, port, page, timeout):
    """打开测试页，等它把结果发回来。页面带 ?report=1 时会在跑完后发到 /__report。"""
    REPORTS.clear()
    GOT.clear()
    profile = tempfile.mkdtemp(prefix='hao-chrome-')
    # 窗口开到 3000 高：行为测试页要整页放得下。页面一滚动，等着出现的气泡提示会被取消（这是脚本本来的行为），
    # 窗口矮了，前一项测试把焦点移到屏幕外引起滚动，气泡提示那一项就会时过时不过。
    proc = subprocess.Popen([chrome, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
                             '--no-sandbox' if os.environ.get('CI') else '--disable-extensions',
                             '--user-data-dir=' + profile, '--window-size=1280,3000',
                             'http://127.0.0.1:%d/tests/%s?report=1' % (port, page)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        GOT.wait(timeout)
    finally:
        proc.terminate()
        try:
            proc.wait(10)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)
    return REPORTS.get('data')


def run(args):
    r = subprocess.run([sys.executable] + args, cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return r.returncode == 0, r.stdout.strip()


def step_build():
    ok, out = run(['build_site.py'])
    return ok, out.splitlines()[-2:] if ok else out.splitlines()[-12:]


def step_dist():
    ok, out = run(['tools/build_skill.py'])
    if not ok:
        return False, out.splitlines()[-12:]
    r = subprocess.run(['git', 'status', '--porcelain', '--', 'dist', 'skills'], cwd=HERE, stdout=subprocess.PIPE, text=True)
    if r.returncode != 0:
        return True, ['不在 git 仓库里，跳过']
    changed = [l[3:] for l in r.stdout.splitlines()]
    if changed:
        return False, ['重新生成后这些文件和仓库里的不一样，改了 source/ 之后要把 dist/ 和 skills/ 一起提交：'] + changed
    return True, ['dist/ 和 skills/ 和仓库里的一致']


def step_version():
    with open(os.path.join(HERE, 'source', 'components', 'bundle.js'), encoding='utf-8') as f:
        m = re.search(r"version:\s*'([^']+)'", f.read())
    with open(os.path.join(HERE, 'package.json'), encoding='utf-8') as f:
        pkg = json.load(f)
    if not m:
        return False, ['bundle.js 里没找到 version']
    if pkg.get('version') != m.group(1):
        return False, ['package.json 写的是 %s，bundle.js 写的是 %s' % (pkg.get('version'), m.group(1))]
    return True, ['版本号 ' + m.group(1)]


def step_en():
    ok, out = run(['tools/check_en.py'])
    return ok, out.splitlines()[-1:] if ok else out.splitlines()[-20:]


def step_site():
    ok, out = run(['tools/check_site.py'])
    return ok, out.splitlines()[-1:] if ok else out.splitlines()[-20:]


def step_behavior(chrome, port):
    d = in_browser(chrome, port, 'behavior.html', 90)
    if not d:
        return False, ['90 秒内没有收到结果']
    bad = [r for r in d['results'] if not r['pass']]
    lines = ['共 %d 项，没过 %d 项' % (d['total'], len(bad))]
    lines += ['没过：%s —— %s' % (r['name'], r.get('error', '')) for r in bad]
    return not bad, lines


def step_audit(chrome, port):
    d = in_browser(chrome, port, 'audit.html', 300)
    if not d:
        return False, ['300 秒内没有收到结果']
    real, waived = [], 0
    for a in d['bad']:
        left = []
        for issue in a['issues']:
            if any(re.search(n, a['name']) and issue.startswith(s) for n, s, _ in AUDIT_OK):
                waived += 1
            else:
                left.append(issue)
        if left:
            real.append('%s（%s，%s）：%s' % (a['name'], '夜' if a['theme'] == 'dark' else '昼', a['width'], '；'.join(left)))
    lines = ['查了 %d 个组件、%d 种情况，有问题 %d 种，按设计放过 %d 条' % (d['components'], d['runs'], len(real), waived)]
    return not real, lines + real


def main():
    browser = '--no-browser' not in sys.argv
    steps = [('生成与令牌核对', step_build), ('dist 与技能包是否最新', step_dist), ('版本号', step_version),
             ('英文稿', step_en), ('站点', step_site)]
    server = None
    if browser:
        chrome = find_chrome()
        if not chrome:
            print('没找到 Chrome 或 Chromium。装一个，或用 HAO_CHROME 指定位置；只想跑其余几步就加 --no-browser。')
            return 2
        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        port = server.server_address[1]
        threading.Thread(target=server.serve_forever, daemon=True).start()
        steps += [('行为测试', lambda: step_behavior(chrome, port)), ('组件审计', lambda: step_audit(chrome, port))]
    failed = []
    for name, fn in steps:
        t = time.time()
        ok, lines = fn()
        print('%s　%s（%.1f 秒）' % ('通过' if ok else '没过', name, time.time() - t))
        for l in lines:
            print('    ' + l)
        if not ok:
            failed.append(name)
    if server:
        server.shutdown()
    if not browser:
        print('没跑：行为测试、组件审计（加了 --no-browser）')
    print('全部通过' if not failed else '没过的：' + '、'.join(failed))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
