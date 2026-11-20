# Card · 卡片

承载一段独立内容的卡片，标题用宋体。

`.hao-card` 里放 `.hao-card__title`、`.hao-card__body`、可选的 `.hao-card__meta`。需要落款时，在开头加一个 `.hao-seal.hao-seal--sm.hao-seal--outline.hao-card__seal`。你提供标题、正文和时间。

- 卡片放在 `bg` 上，卡片里不再套卡片。
- 一屏里只给一张卡片落印。
- 整张卡片可点时，把它做成一个 `<a>`，不要在里面再放按钮。
- 正文不超过四行，更长的内容进详情页。

两个带纹样的变体，一屏只用其中一张：

- `hao-card--wave`：底边铺两排海水纹，给一屏里最重要的那张卡片。
- `hao-card--stitched`：内缘一圈泥金缝线，像绣片的锁边，给收藏、手作一类有「物件感」的内容。带缝线时不再放印章。

**无障碍**

- 标题用标题元素写，预览里是 `<h3 class="hao-card__title">`。换成 `<span>` 仿标题，读屏就少一条按标题跳转的路。
- 落款的印对读屏隐藏，照预览在 `.hao-card__seal` 上写 `aria-hidden="true"`；时间照常写在 `.hao-card__meta` 里。
- 海水纹（`hao-card--wave`）和缝线（`hao-card--stitched`）都是伪元素画的，读屏读不到，你不用为它们写什么。

## 标记

### 中文

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div class="hao-card" style="width:280px">
  <span class="hao-seal hao-seal--sm hao-seal--outline hao-card__seal" aria-hidden="true">印</span>
  <h3 class="hao-card__title">晨间札记</h3>
  <p class="hao-card__body">窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p>
  <p class="hao-card__meta">今天 07:12</p>
</div>
<div class="hao-card hao-card--wave" style="width:280px">
  <h3 class="hao-card__title">小雪</h3>
  <p class="hao-card__body">十一月二十二日交节。天渐寒，宜早睡，宜温一壶茶。</p>
</div>
<div class="hao-card hao-card--stitched" style="width:280px">
  <h3 class="hao-card__title">手作清单</h3>
  <p class="hao-card__body">三件未完成，最近一件明天到期。</p>
  <p class="hao-card__meta">更新于 09:41</p>
</div>
</div>
```

### English

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div class="hao-card" style="width:280px">
  <span class="hao-seal hao-seal--sm hao-seal--outline hao-card__seal" lang="zh" aria-hidden="true">印</span>
  <h3 class="hao-card__title">Morning note</h3>
  <p class="hao-card__body">Fog outside the window. Write down the three things that matter today, and let the rest wait.</p>
  <p class="hao-card__meta">Today, 7:12 AM</p>
</div>
<div class="hao-card hao-card--wave" style="width:280px">
  <h3 class="hao-card__title">Minor Snow</h3>
  <p class="hao-card__body">Begins November 22. The days turn cold: sleep early, and keep a pot of tea warm.</p>
</div>
<div class="hao-card hao-card--stitched" style="width:280px">
  <h3 class="hao-card__title">Craft list</h3>
  <p class="hao-card__body">Three items open. The next one is due tomorrow.</p>
  <p class="hao-card__meta">Updated 9:41 AM</p>
</div>
</div>
```
