# ListGroup · List group

An iOS-style grouped list, the body of settings and detail screens.

Inside `<ul class="hao-list">`, each `<li>` holds one `.hao-list__row` (a tappable row is an `<a>` or `<button>`). Within the row, in order: `.hao-list__title` (which may carry a line of `.hao-list__sub`), an optional `.hao-list__value`, and an optional control or arrow on the right. A `.hao-list-header` may go above the group, a `.hao-list-footer` below.

- Keep two to seven rows per group; split anything longer into several groups, with `space-6` between groups.
- Give an arrow only to rows that lead a level deeper.
- The separator starts at the left edge of the text and doesn’t run all the way to the left—that’s the iOS habit, and it stays.
- Put list groups directly on `bg`; don’t wrap them in another card.
- For single selection inside a list, the chosen row gets a `.hao-list__check` on the right: one `tint`-colored stroke of the upward hook stroke, the same brushstroke as the check in a checkbox.

**Accessibility**

- Tappable rows are `<a>` or `<button>`, 44px tall, each one reachable by Tab; on focus, a `focus`-colored edge is drawn.
- The arrow icon at the end of a row and the seal within a row take `aria-hidden="true"` as in the preview; a screen reader reads the row name, the subtitle, and the value.
- For single selection, follow the preview’s markup: on the `<ul>` write `role="listbox"` and `aria-label`; on each `<li>` write `role="none"`; on the `<button>` inside write `role="option"`; the chosen row gets `aria-selected="true"`; the check `.hao-list__check` takes `aria-hidden="true"`.

**Behavior** (when the behavior script is loaded)

- A list written as `role="listbox"` is taken over by the script: tap a row and it’s selected, the check moves over, and the list fires a `hao-change` event carrying which item is chosen.
- The whole group is a single Tab stop. The up and down arrow keys move between rows, and Home and End jump to the top and bottom; Enter or Space selects. The arrow keys move focus only, not the selection, because options like these mostly take effect the moment they’re chosen.
- When rows are `<button>`s, you don’t need inline styles to strip the border and the background; the stylesheet already handles it.

## Markup

### English

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div style="width:390px">
  <p class="hao-list-header">General</p>
  <ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Appearance</span><span class="hao-list__value">Match system</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Text size</span><span class="hao-list__value">Standard</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Signature seal<span class="hao-list__sub">Shown at the top right of every note</span></span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
  </ul>
  <p class="hao-list-footer">Appearance settings sync to all your devices.</p>
</div>
<div style="width:300px">
  <p class="hao-list-header">Appearance</p>
  <ul class="hao-list" role="listbox" aria-label="Appearance">
    <li role="none"><button class="hao-list__row" role="option" aria-selected="true"><span class="hao-list__title">Match system</span><span class="hao-list__check" aria-hidden="true"></span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">Day</span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">Night</span></button></li>
  </ul>
</div>
</div>
```

### Chinese

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div style="width:390px">
  <p class="hao-list-header">通用</p>
  <ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">外观</span><span class="hao-list__value">跟随系统</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">字号</span><span class="hao-list__value">标准</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">落款印章<span class="hao-list__sub">显示在每条札记的右上角</span></span><span class="hao-seal hao-seal--sm hao-seal--outline" aria-hidden="true">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
  </ul>
  <p class="hao-list-footer">外观设置会同步到你的所有设备。</p>
</div>
<div style="width:300px">
  <p class="hao-list-header">外观</p>
  <ul class="hao-list" role="listbox" aria-label="外观">
    <li role="none"><button class="hao-list__row" role="option" aria-selected="true"><span class="hao-list__title">跟随系统</span><span class="hao-list__check" aria-hidden="true"></span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">昼</span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">夜</span></button></li>
  </ul>
</div>
</div>
```
