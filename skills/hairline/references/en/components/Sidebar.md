# Sidebar

A navigation column on the left of wide screens. Use it in place of the top navigation when there are more than five top-level areas, or a second level underneath (folders).

Inside `<nav class="hao-side">` go any number of `.hao-side__item`s (icon plus text, with an optional count), grouped by `.hao-side__label`; the current page carries `aria-current="page"`.

- It is 240px wide and sits directly on `bg`, with no fill and no shadow; only the content area to its right uses `surface`.
- The current item is `tint` text on a `tint-wash` fill; the rest are `ink`.
- Counts use `hao-badge--quiet`. A cinnabar badge never appears in the sidebar unless something truly needs attention.
- On narrow screens the sidebar folds away: three to five top-level items go into the `TabBar`, the rest into “Me”.
- The product name and its small seal go at the very top of the sidebar, not on every page.

## Markup

### English

```html
<nav class="hao-side" aria-label="Main" style="border-radius:var(--hao-radius-lg);background:var(--hao-bg);border:1px solid var(--hao-hairline)">
  <a class="hao-side__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes<span class="hao-badge hao-badge--quiet">38</span></a>
  <p class="hao-side__label">Folders</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Essays</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Reading</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Travel</a>
  <p class="hao-side__label">Other</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--settings" aria-hidden="true"></i>Settings</a>
</nav>
```

### Chinese

```html
<nav class="hao-side" aria-label="主导航" style="border-radius:var(--hao-radius-lg);background:var(--hao-bg);border:1px solid var(--hao-hairline)">
  <a class="hao-side__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记<span class="hao-badge hao-badge--quiet">38</span></a>
  <p class="hao-side__label">文件夹</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>随笔</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>读书</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>旅行</a>
  <p class="hao-side__label">其他</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--settings" aria-hidden="true"></i>设置</a>
</nav>
```
