# Prose · 长文

长文的阅读版式：一篇文章从标题到落款该怎么排。

`<article class="hao-prose">` 里依次放 `<h1>`、`.hao-prose__meta`、若干 `<p>` 和 `<h2>`，中间可以穿插 `Divider`、`Quote`、`Mount`，末尾可放 `.hao-prose__sign`（一组落款）。文字由你提供。

- **版心**：行宽不超过 `measure`（约 38 个汉字）。上边距 72px，下边距 48px，上大于下，这是线装书「天头大于地脚」的规矩：天头留给批注，也让标题有地方呼吸。
- **中文段落**：首行缩进两个字，两端对齐，段与段之间不空行。行高 32px，比界面正文再松一档。
- **英文段落**：左对齐，段首缩进 1.5 个字宽；标题后的第一段不缩进。行高 28px。
- **标题**：`<h1>` 用 `title-1`，一篇只有一个；小节用 `<h2>`，`title-2`；再往下一级用 `<h3>`，`title-3`，到此为止。标题不加句号，不居中。
- **日期**：可以写成干支与节气（「丙午年 小雪前四日」），这是这套系统里少数可以雅一点的地方；功能性的时间戳仍写数字。
- **分章**用带鱼尾的 `Divider`，一篇至多两三处。
- **落款**靠右：竖排年款加一方小印（英文用斜体的 colophon 加印）。有落款的页面不再放别的印。
- 正文里的链接用 `.hao-link`，强调用加粗，不用颜色。
- 阅读页不放纹样；鱼尾和落款已经够了。

**无障碍**

- 结构就是语义：整篇落在 `<article class="hao-prose">` 里，读屏按 `<h1>`、`<h2>` 的层级跳着读。
- 分章的鱼尾分隔线照预览写 `role="separator"`。
- 落款的小印照预览写 `aria-hidden="true"`，年款文字（`.hao-slip` 或英文的斜体落款）留在读屏里。

## 标记

### 中文

```html
<article class="hao-prose" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<h1>雾里的早晨</h1>
<p class="hao-prose__meta">丙午年 小雪前四日</p>
<p>早上推开窗，对面的楼只剩一个淡淡的轮廓。雾把远处的东西都收走了，只留下眼前这一小块：窗台、一盆文竹、一杯刚倒的水。</p>
<p>平时总觉得要看得远才算看清楚。今天看不远，反倒把近处的东西看了个仔细。文竹新抽了一枝，细得像一根线，昨天还没有。</p>
<h2>留白</h2>
<p>画山水的人说，纸上最要紧的是没画的地方。雾大概就是天地自己留的白。它什么也不添，只是把多余的先拿开。</p>
<div class="hao-divider" role="separator"><i></i></div>
<p>等到九点钟，雾散了，楼又回来了，一扇扇窗户都清清楚楚。我把杯子里的水喝完，开始做今天的第一件事。</p>
<div class="hao-prose__sign"><span class="hao-sign"><span class="hao-slip">丙午冬</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></span></div>
</article>
```

### English

```html
<article class="hao-prose" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<h1>A morning in fog</h1>
<p class="hao-prose__meta">Four days before Minor Snow, the Bingwu year</p>
<p>I opened the window this morning and the building across the street was only a faint outline. The fog had taken away everything far off and left one small patch in front of me: the windowsill, a pot of asparagus fern, a glass of water just poured.</p>
<p>I usually think that seeing clearly means seeing far. Today I couldn’t see far, so I looked closely at what was near. The fern had put out a new shoot, thin as a thread, that wasn’t there yesterday.</p>
<h2>Blank space</h2>
<p>Landscape painters say the most important part of the paper is the part left unpainted. Fog may be the blank space the world leaves for itself. It adds nothing. It only sets aside what isn’t needed yet.</p>
<div class="hao-divider" role="separator"><i></i></div>
<p>By nine the fog had lifted and the building was back, every window sharp. I finished the water and started on the first thing of the day.</p>
<div class="hao-prose__sign"><span class="hao-sign hao-sign--row"><span class="hao-colophon">Winter, the Bingwu year</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></span></div>
</article>
```
