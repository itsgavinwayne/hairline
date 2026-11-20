# Card

A card holding one piece of standalone content, with the title in the Song typeface.

`.hao-card` holds `.hao-card__title`, `.hao-card__body`, and an optional `.hao-card__meta`. When the card needs a signature, add a `.hao-seal.hao-seal--sm.hao-seal--outline.hao-card__seal` at the head. You provide the title, the body, and the date.

- Cards sit on `bg`, and no card goes inside a card.
- Only one card per screen takes a seal.
- When the whole card is tappable, make the card one `<a>` and put no button inside.
- Keep the body within four lines; anything longer goes to a detail page.

Two variants carry patterns; use at most one of them per screen:

- `hao-card--wave`: two courses of the wave pattern along the bottom edge, for the screen’s most important card.
- `hao-card--stitched`: a round of gold ink stitching along the inner edge, like the edging stitch on an embroidered piece, for content with the feel of “a made object”—saved things, handwork. A stitched card takes no seal.

**Accessibility**

- Write the title as a real heading element; in the preview it’s `<h3 class="hao-card__title">`. Swap in a `<span>` that only looks like a title, and screen readers lose one path of jumping by heading.
- The signature seal is hidden from screen readers: as in the preview, put `aria-hidden="true"` on `.hao-card__seal`; the date stays in `.hao-card__meta` as usual.
- The wave pattern (`hao-card--wave`) and the stitching (`hao-card--stitched`) are drawn by pseudo-elements; screen readers never see them, and you write nothing for them.

## Markup

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

### Chinese

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
