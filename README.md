# 毫 Hairline

iOS 的克制，加一点东方气韵。一套中英双语、昼夜两套主题的设计系统：一份样式表、一份行为脚本、一份令牌，不依赖任何框架，也不需要构建工具。

A design system with the restraint of iOS and a trace of East Asian character. Bilingual (Chinese and English), light and dark. One stylesheet, one script, one token file; no framework and no build step. English documentation lives under `site/en/` once the site is built.

## 拿去用

把 `dist/` 里的文件放进自己的项目：

| 文件 | 内容 |
| --- | --- |
| `dist/hairline.css` | 全部令牌和所有组件的样式，含昼夜两套主题 |
| `dist/hairline.js` | 弹窗、菜单、月历等组件的行为。可选，不加载它组件照样能看 |
| `dist/tokens.json` | 令牌的原始数据，给设计工具或别的平台用 |

```html
<link rel="stylesheet" href="hairline.css">
<script src="hairline.js" defer></script>
```

类名以 `hao-` 开头，变量以 `--hao-` 开头。目前还没有发布到 npm，也没有公共的 CDN 地址；`package.json` 已经备好，暂时标着 `private`。

## 让 AI 来用

`skills/hairline/` 是一份给 AI 的技能包：一页怎么用的说明、全部规范、令牌表、每个组件的说明和可以直接抄的标记，外加 `dist/` 的三个文件。

- **Claude Code**：把 `skills/hairline` 整个文件夹拷到 `~/.claude/skills/`（所有项目可用）或项目里的 `.claude/skills/`（只这个项目可用）。之后说「用 Hairline 做一个设置页」，它会自己去读。
- **别的 AI 工具**：让它先读 `skills/hairline/SKILL.md`，里面写明了其余文件各管什么。
- **只能读网页的 AI**：文档站根目录有 `llms.txt`（全站目录）和 `llms-full.txt`（全部内容连成的一份纯文本），英文的在 `/en/` 下。

技能包里除了 `SKILL.md` 都是生成的，改了 `source/` 之后跑 `python3 tools/build_skill.py` 重建（全量检查会替你跑）。

## 看文档

```bash
python3 build_site.py
```

```bash
python3 -m http.server 4173 --directory site
```

然后打开 <http://localhost:4173>。中文在根目录，英文在 `/en/`。

## 目录

| 位置 | 是什么 |
| --- | --- |
| `source/` | 唯一要手改的地方：令牌、组件、图标、规范，英文稿在 `source/en/` |
| `dist/` | 生成出来给人用的三个文件，不要直接改 |
| `site/` | 生成出来的文档站，不入库 |
| `build_site.py` | 核对令牌，生成 `dist/` 和 `site/` |
| `tests/` | 行为测试、组件审计、审阅工作台，都是浏览器里打开的页面 |
| `skills/hairline/` | 给 AI 用的技能包，`SKILL.md` 手写，其余由 `tools/build_skill.py` 生成 |
| `tools/` | 核对脚本和截图工具 |

## 改了东西之后

```bash
python3 tools/check_all.py
```

一条命令跑完全部检查：令牌核对与生成、`dist/` 是否最新、版本号、英文稿、站点链接、行为测试、组件审计。后两步在无头的 Chrome 里跑，本机没有 Chrome 时加 `--no-browser` 只跑其余几步。

- 改 `source/`，不改 `dist/`；改完重新生成，把 `dist/` 和 `skills/` 一起提交。
- 改了中文稿，同步改 `source/en/` 里对应的英文稿。
- 版本号写在 `source/components/bundle.js` 的 `version`，`package.json` 里那一处要跟着改，检查会核对两处是否相同。
- 改动记进 `CHANGELOG.md`。

## 参与

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

- 代码（样式表、脚本、令牌、图标、工具）：[MIT](LICENSE)。
- 规范与文档：[CC BY 4.0](LICENSE-docs.md)，转载和改编请署名。
- 「毫」「Hairline」这个名字和标志保留：可以说你的产品基于这套系统，但改过再发布请换一个名字。

细则见 [LICENSE-docs.md](LICENSE-docs.md)。

Code is MIT; guidelines and documentation are CC BY 4.0; the name and mark are reserved. See [LICENSE-docs.md](LICENSE-docs.md).
