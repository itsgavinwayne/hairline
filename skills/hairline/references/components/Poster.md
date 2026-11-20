# Poster · 海报

海报、社交图、幻灯片封面的模板。同一个容器，三种比例。

`.hao-poster` 是画面本身，默认 2:3（海报）；`hao-poster--square` 是 1:1（社交方图），`hao-poster--wide` 是 16:9（幻灯片、网页头图）；`hao-poster--tint` 换成石青底。里面的零件：`.hao-poster__title`（大标题，加 `--v` 竖排）、`.hao-poster__sub`、`.hao-poster__meta`、`.hao-poster__foot`（底部一行，左边信息右边落印）、`.hao-poster__moon`（石青底上的一轮月）。用内联的 `--w` 设画面宽度，里面所有字号、边距、印的大小都跟着缩放。

五个模板：

| 模板 | 画面 | 用在 |
| --- | --- | --- |
| 活动 | 月白底，竖排大标题在右，信息在左下，底边一带海水纹 | 活动、发布、展览 |
| 节气 | 石青满底，上方一轮月，下面是节气名 | 节气、节日、每日一图 |
| 诗 | 月白底，顶上一道回纹，中间竖排的诗 | 诗、题词、每周一句 |
| 引文（方） | 月白底，一句话，泥金角标 | 社交平台的引用图 |
| 封面（宽） | 月白底，左下一行大标题，右下标志 | 幻灯片封面、文章头图 |

规则和界面一样，只是更严：

- **不跟主题走。** 海报是平面物料，昼夜都用昼间的颜色：在 `.hao-poster` 上写 `data-theme="light"`。不写的话，夜间石青底会变浅，月亮成了一个黑洞。
- **一张一景，一张一印。** 每张只有一种纹样或一轮月，只有一处朱砂（一方印，或朱砂色的标志）。石青底上的标志和印用单色。
- **留白过半。** 画面里空着的地方不少于一半。字少的时候不要把字放大去填。
- **四边留出画面宽度的十二分之一**，所有内容对齐到这条边。
- **标题用宋体**，一张里只有一个大标题。中文可以竖排，放在右侧；英文横排，用 Newsreader。
- **信息用黑体小字**，放左下；落印放右下。
- 标志只用于介绍这套系统本身的画面；别的画面右下放产品自己的印。

印刷用的色值、字体和出血，见手册的「平面与印刷」一节。

**无障碍**

- 纹样对读屏隐藏：照预览给 `.hao-wave`、`.hao-fret` 写 `role="presentation"`。
- 画面的信息都在真文字里：标题、说明、落款是 `<h2>` 和 `<p>`，读屏读得到整张海报说了什么。
- 落印和标志里的图形照预览写 `aria-hidden="true"`，右下是谁由 `.hao-poster__foot` 里的文字给出。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start"><div class="hao-poster" data-theme="light"><div style="display:flex;justify-content:space-between;flex:1">
  <div><p class="hao-poster__meta">读书会 第七期</p><p class="hao-poster__sub">计成《园冶》</p></div>
  <h2 class="hao-poster__title hao-poster__title--v">虽由人作<br>宛自天开</h2></div>
  
  <div class="hao-poster__foot"><p class="hao-poster__meta">十一月十八日 周三<br>晚上七点半，线上</p><span class="hao-seal " lang="zh" aria-hidden="true">印</span></div>
  <div class="hao-wave" role="presentation"></div></div><div class="hao-poster hao-poster--tint" data-theme="light"><div class="hao-poster__moon" style="margin:calc(var(--w)*.06) auto 0"></div>
  <h2 class="hao-poster__title" style="margin-top:calc(var(--w)*.1)">小雪</h2>
  <p class="hao-poster__sub" style="font-weight:600">天渐寒，宜早睡，宜温一壶茶</p>
  <div class="hao-poster__foot"><p class="hao-poster__meta">丙午年十月十四<br>十一月二十二日</p><span class="hao-logo hao-logo--ink" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div><div class="hao-poster" data-theme="light"><div class="hao-fret" role="presentation"></div><div style="flex:1;display:grid;place-items:center"><div class="hao-verse"><p class="hao-verse__title">鹿柴</p><p>空山不见人</p><p>但闻人语响</p><p>返景入深林</p><p>复照青苔上</p><p class="hao-verse__by">王维</p></div></div><div class="hao-poster__foot"><p class="hao-poster__meta">每周一诗</p><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div></div>
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start;margin-top:var(--hao-space-6)"><div class="hao-poster hao-poster--square" data-theme="light"><blockquote class="hao-quote" style="margin:auto 0"><p>纸上最要紧的，是没画的地方。</p><cite>《雾里的早晨》</cite></blockquote><div class="hao-poster__foot"><span></span><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div><div class="hao-poster hao-poster--wide" data-theme="light" style="--w:min(480px, 72vw)"><h2 class="hao-poster__title" style="font-size:calc(var(--w)*.085);margin-top:auto">十一月回顾</h2><p class="hao-poster__sub" style="font-size:calc(var(--w)*.034);font-weight:600">写了 31 条，共 48,260 字</p><div class="hao-poster__foot" style="margin-top:calc(var(--w)*.05)"><p class="hao-poster__meta" style="font-size:calc(var(--w)*.026)">丙午年 冬</p><span class="hao-logo" style="font-size:calc(var(--w)*.036)" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start"><div class="hao-poster" data-theme="light"><div style="display:flex;justify-content:space-between;flex:1">
  <div><p class="hao-poster__meta">Book club, no. 7</p><p class="hao-poster__sub">Ji Cheng,<br>The Craft of Gardens</p></div>
  </div>
  <h2 class="hao-poster__title" style="margin-bottom:calc(var(--w)*.3)">Made by hand,<br>as if by nature</h2>
  <div class="hao-poster__foot"><p class="hao-poster__meta">Wednesday, November 18<br>7:30 PM, online</p><span class="hao-seal " lang="zh" aria-hidden="true">印</span></div>
  <div class="hao-wave" role="presentation"></div></div><div class="hao-poster hao-poster--tint" data-theme="light"><div class="hao-poster__moon" style="margin:calc(var(--w)*.06) auto 0"></div>
  <h2 class="hao-poster__title" style="margin-top:calc(var(--w)*.1)">Minor Snow</h2>
  <p class="hao-poster__sub" style="font-weight:500">The days turn cold. Sleep early, and keep a pot of tea warm.</p>
  <div class="hao-poster__foot"><p class="hao-poster__meta">November 22<br>the Bingwu year</p><span class="hao-logo hao-logo--ink" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div><div class="hao-poster" data-theme="light"><div class="hao-fret" role="presentation"></div><div style="flex:1;display:grid;place-items:center start"><div class="hao-verse" lang="en"><p class="hao-verse__title">Deer Enclosure</p><p>Empty hills, no one in sight,</p><p>yet voices can be heard.</p><p class="hao-verse__by">Wang Wei</p></div></div><div class="hao-poster__foot"><p class="hao-poster__meta">A poem a week</p><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div></div>
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start;margin-top:var(--hao-space-6)"><div class="hao-poster hao-poster--square" data-theme="light"><blockquote class="hao-quote" style="margin:auto 0"><p>The most important part of the paper is the part left unpainted.</p><cite>A morning in fog</cite></blockquote><div class="hao-poster__foot"><span></span><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div><div class="hao-poster hao-poster--wide" data-theme="light" style="--w:min(480px, 72vw)"><h2 class="hao-poster__title" style="font-size:calc(var(--w)*.085);margin-top:auto">November in review</h2><p class="hao-poster__sub" style="font-size:calc(var(--w)*.034);font-weight:500">31 notes, 48,260 words</p><div class="hao-poster__foot" style="margin-top:calc(var(--w)*.05)"><p class="hao-poster__meta" style="font-size:calc(var(--w)*.026)">Winter, the Bingwu year</p><span class="hao-logo" style="font-size:calc(var(--w)*.036)" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div></div>
```
