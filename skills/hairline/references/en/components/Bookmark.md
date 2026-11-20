# Bookmark

A toggle for saving a favorite, shaped like a hanging lamp: an unlit lamp when unsaved, lit once saved.

`<button class="hao-lamp" aria-pressed="true|false" aria-label="…">`. Dropped into a `Card`, it hangs at the top right corner, running down from the card’s top edge.

- The lamp is four things only: the cord, the cap, the body and the tassel, all in thin lines. Unsaved, the body is a gray outline; saved, it fills with `tint`.
- Filled versus outlined tells the two states apart, not color alone.
- The button itself is a 44px square, with the lamp down the middle only, so a finger lands true.
- The `aria-label` says what a tap does: “Save” when unsaved, “Unsave” when saved.
- Use this lamp, not stars or hearts. A card carrying a lamp takes no seal.
- No cinnabar, and never a red festival lantern. The bookmark is the reader’s own mark, not a holiday decoration and not the system’s notice.
- A screen can hold many of them: the lamp is the control’s own shape, covered by “shape follows the control”, not a scene.

**Behavior** (when the behavior script is loaded)

- Add `data-hao-toggle`, and one tap switches between saved and unsaved. Add `data-label-on` and `data-label-off` too, and the accessibility label follows (“Unsave”, “Save”).

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="Remove bookmark" data-label-off="Bookmark" aria-pressed="true" aria-label="Remove bookmark"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">Morning note</h3><p class="hao-card__body">Fog outside the window. Write down the three things that matter today, and let the rest wait.</p></div>
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="Remove bookmark" data-label-off="Bookmark" aria-pressed="false" aria-label="Bookmark"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">Three days in Suzhou</h3><p class="hao-card__body">We saw one garden on the first day. Walking slowly, I noticed that every window frames a painting.</p></div>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="取消收藏" data-label-off="收藏" aria-pressed="true" aria-label="取消收藏"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">晨间札记</h3><p class="hao-card__body">窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p></div>
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="取消收藏" data-label-off="收藏" aria-pressed="false" aria-label="收藏"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">苏州三日</h3><p class="hao-card__body">第一天只看了一座园子。走得慢，才发现每一扇窗框住的都是一幅画。</p></div>
</div>
```
