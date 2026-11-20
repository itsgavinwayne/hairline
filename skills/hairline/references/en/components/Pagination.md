# Pagination

Move between the pages of a many-page list or table, on wide screens.

Inside `<nav aria-label="Pagination">` goes a `<ul class="hao-pages">`; each item is a `.hao-pages__item`. The current page takes `aria-current="page"`, an arrow that has run out takes `aria-disabled="true"`, and a gap in the numbering uses `.hao-pages__gap`.

- Always show the first page, the last page, the current page, and one page on each side of it; leave out the rest.
- Don’t show it when there is only one page.
- On narrow screens, don’t paginate; auto-load on scrolling to the bottom, or offer a “Load more” button.
- Place it below the table, right-aligned or centered—the same across the product.
- Where a row of page numbers won’t fit, use one line of text, `.hao-pages__text`: “Page 1 of 12”, with the current page number in bold Song typeface (wrapped in `<b>`), flanked by arrows for the previous and next page.
- The whole control is a handscroll laid open: the page numbers sit on a strip of `surface` paper, with a `hairline` above and below and a roller at each end. Add `hao-pages--plain` to drop the scroll and keep only the numbers.
- The current page number is a “page-number seal”: a Song typeface numeral in a thin, clipped-corner frame—the same shape as a seal. Its color is `tint`, not cinnabar, because it says “you are here”; it isn’t an alert.

## Markup

### English

```html
<nav aria-label="Pagination"><ul class="hao-pages">
  <li><a class="hao-pages__item" href="#" aria-label="Previous page" aria-disabled="true"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i></a></li>
  <li><a class="hao-pages__item" href="#" aria-current="page">1</a></li>
  <li><a class="hao-pages__item" href="#">2</a></li>
  <li><a class="hao-pages__item" href="#">3</a></li>
  <li class="hao-pages__gap" aria-hidden="true">…</li>
  <li><a class="hao-pages__item" href="#">12</a></li>
  <li><a class="hao-pages__item" href="#" aria-label="Next page"><i class="hao-icon hao-icon--chevron-right" aria-hidden="true"></i></a></li>
</ul></nav>
<p class="hao-pages__text" style="margin:var(--hao-space-4) 0 0">Page <b>1</b> of 12</p>
```

### Chinese

```html
<nav aria-label="分页"><ul class="hao-pages">
  <li><a class="hao-pages__item" href="#" aria-label="上一页" aria-disabled="true"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i></a></li>
  <li><a class="hao-pages__item" href="#" aria-current="page">1</a></li>
  <li><a class="hao-pages__item" href="#">2</a></li>
  <li><a class="hao-pages__item" href="#">3</a></li>
  <li class="hao-pages__gap" aria-hidden="true">…</li>
  <li><a class="hao-pages__item" href="#">12</a></li>
  <li><a class="hao-pages__item" href="#" aria-label="下一页"><i class="hao-icon hao-icon--chevron-right" aria-hidden="true"></i></a></li>
</ul></nav>
<p class="hao-pages__text" style="margin:var(--hao-space-4) 0 0">第 <b>1</b> 页，共 12 页</p>
```
