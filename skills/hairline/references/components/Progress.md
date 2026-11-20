# Progress · 进度与加载

「正在进行」的几种表达。形状借了三个传统意象：月相、针线、漏刻。

**知道进度时**

| 类名 | 意象 | 用在哪里 |
| --- | --- | --- |
| `.hao-moon` | 月盈：一轮月从朔到望，慢慢圆起来 | 目标、习惯、阅读进度这类「积累」的事。满了加 `hao-moon--done`，转为竹青 |
| `.hao-progress.hao-progress--stitch` | 针线：走过的是实线，没走的是一排针脚，线头一个小点 | 导出、上传、安装这类「正在做」的事 |
| `.hao-progress.hao-progress--ke` | 刻度：取自漏刻，轨道下面每一成一道刻线 | 容量、额度、配额这类要对着刻度读数的事 |
| `.hao-progress` | 素线，不带意象 | 密集的界面、表格行内，或同屏已有别的意象时 |

- 月盈用内联的 `--p`（0 到 1）写进度；进度条里放一个 `<span>`，用内联的 `--v`（百分比）写进度。
- 月盈有 28px 和 64px（`hao-moon--lg`）两个尺寸。大的旁边配一句话，小的可以成排放，一天一个。
- 旁边总有一句文字说进行到哪了。数字要精确时写百分比或实数；只是给个印象时可以写「六成」。

**不知道进度时**

- `.hao-spinner`：一弯月牙在转。等几秒的事用它，旁边配一个词。
- `.hao-ripple`：一滴水落进水面，一圈圈荡开（里面放一个 `<i>`）。整页载入、下拉刷新用它。
- `.hao-spinner.hao-spinner--ring`：普通的圆环，按钮里或很小的地方用。
- `.hao-skeleton`：内容还没到时的占位灰块，宽高由你设，不闪动。

**规则**

- 少于一秒的等待什么都不显示。
- 这些意象是控件自己的形状，不算纹样，不占「一屏一种」的名额。但一屏里的进度只用一种意象，不要月、线、刻混着出现。
- 颜色只用 `tint`，完成用 `jade`。不用 `gold` 和 `seal`。
- 进度的多少写在里面那个 `<span>` 的内联变量上：`style="--v:60%"`。旧写法 `style="width:60%"` 仍然能用，但数值变化时没有过渡。
- 进度加 `role="progressbar"` 和 `aria-valuenow`；加载加 `role="status"` 和 `aria-label`。
- 系统开启「减弱动态效果」时，月牙放慢，涟漪静止。
- 长文还没到时，用 `hao-skeleton--lines`：几行细的界栏线，像一张空的笺纸。高度取 32px 的整数倍。

## 标记

### 中文

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),340px));gap:var(--hao-space-8) var(--hao-space-12);align-items:start">
  <div><div class="hao-row" style="gap:var(--hao-space-4)"><span class="hao-moon hao-moon--lg" role="progressbar" aria-label="本月目标" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" style="--p:.62"></span><div><div style="font:600 24px/32px var(--hao-font-serif)">六成二</div><div style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin:0">本月写了 31 条，目标 50 条</div></div></div>
    <div class="hao-row" style="gap:var(--hao-space-4);margin-top:var(--hao-space-5)"><span class="hao-moon" style="--p:.1"></span><span class="hao-moon" style="--p:.3"></span><span class="hao-moon" style="--p:.5"></span><span class="hao-moon" style="--p:.7"></span><span class="hao-moon" style="--p:.9"></span><span class="hao-moon hao-moon--done" style="--p:1"></span></div>
    <p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">月盈：从朔到望，满了转为竹青</p></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-6)">
    <div><div class="hao-progress hao-progress--stitch" role="progressbar" aria-label="正在导出" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100"><span style="--v:62%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-3)">针线：正在导出，已完成 62%</p></div>
    <div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="存储空间" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-5)">刻度：已用 4 GB，共 10 GB</p></div>
    <div><div class="hao-progress" role="progressbar" aria-label="正在上传" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"><span style="--v:80%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">素线：正在上传</p></div>
  </div>
  <div class="hao-row" style="gap:var(--hao-space-6)"><span class="hao-row"><span class="hao-spinner" role="status" aria-label="正在同步"></span><span style="font-size:15px;color:var(--hao-ink-secondary)">正在同步</span></span><span class="hao-row"><span class="hao-ripple" role="status" aria-label="正在载入"><i></i></span><span style="font-size:15px;color:var(--hao-ink-secondary)">正在载入</span></span><span class="hao-spinner hao-spinner--ring" role="status" aria-label="载入中"></span></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-2)" aria-hidden="true"><span class="hao-skeleton" style="width:45%;height:22px"></span><span class="hao-skeleton"></span><span class="hao-skeleton" style="width:80%"></span><span class="hao-skeleton hao-skeleton--lines" style="margin-top:var(--hao-space-3)"></span></div>
</div>
```

### English

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),340px));gap:var(--hao-space-8) var(--hao-space-12);align-items:start">
  <div><div class="hao-row" style="gap:var(--hao-space-4)"><span class="hao-moon hao-moon--lg" role="progressbar" aria-label="Monthly goal" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" style="--p:.62"></span><div><div style="font:600 24px/32px var(--hao-font-serif)">62%</div><div style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin:0">31 notes this month, goal 50</div></div></div>
    <div class="hao-row" style="gap:var(--hao-space-4);margin-top:var(--hao-space-5)"><span class="hao-moon" style="--p:.1"></span><span class="hao-moon" style="--p:.3"></span><span class="hao-moon" style="--p:.5"></span><span class="hao-moon" style="--p:.7"></span><span class="hao-moon" style="--p:.9"></span><span class="hao-moon hao-moon--done" style="--p:1"></span></div>
    <p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Waxing moon: new to full, turning jade when complete</p></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-6)">
    <div><div class="hao-progress hao-progress--stitch" role="progressbar" aria-label="Exporting" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100"><span style="--v:62%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-3)">Thread: exporting, 62% done</p></div>
    <div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="Storage" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-5)">Ticks: 4 GB of 10 GB used</p></div>
    <div><div class="hao-progress" role="progressbar" aria-label="Uploading" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"><span style="--v:80%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Plain: uploading</p></div>
  </div>
  <div class="hao-row" style="gap:var(--hao-space-6)"><span class="hao-row"><span class="hao-spinner" role="status" aria-label="Syncing"></span><span style="font-size:15px;color:var(--hao-ink-secondary)">Syncing</span></span><span class="hao-row"><span class="hao-ripple" role="status" aria-label="Loading"><i></i></span><span style="font-size:15px;color:var(--hao-ink-secondary)">Loading</span></span><span class="hao-spinner hao-spinner--ring" role="status" aria-label="Loading"></span></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-2)" aria-hidden="true"><span class="hao-skeleton" style="width:45%;height:22px"></span><span class="hao-skeleton"></span><span class="hao-skeleton" style="width:80%"></span><span class="hao-skeleton hao-skeleton--lines" style="margin-top:var(--hao-space-3)"></span></div>
</div>
```
