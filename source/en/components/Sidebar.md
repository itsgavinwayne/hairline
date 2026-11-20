A navigation column on the left of wide screens. Use it in place of the top navigation when there are more than five top-level areas, or a second level underneath (folders).

Inside `<nav class="hao-side">` go any number of `.hao-side__item`s (icon plus text, with an optional count), grouped by `.hao-side__label`; the current page carries `aria-current="page"`.

- It is 240px wide and sits directly on `bg`, with no fill and no shadow; only the content area to its right uses `surface`.
- The current item is `tint` text on a `tint-wash` fill; the rest are `ink`.
- Counts use `hao-badge--quiet`. A cinnabar badge never appears in the sidebar unless something truly needs attention.
- On narrow screens the sidebar folds away: three to five top-level items go into the `TabBar`, the rest into “Me”.
- The product name and its small seal go at the very top of the sidebar, not on every page.
