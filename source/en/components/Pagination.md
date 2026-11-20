Move between the pages of a many-page list or table, on wide screens.

Inside `<nav aria-label="Pagination">` goes a `<ul class="hao-pages">`; each item is a `.hao-pages__item`. The current page takes `aria-current="page"`, an arrow that has run out takes `aria-disabled="true"`, and a gap in the numbering uses `.hao-pages__gap`.

- Always show the first page, the last page, the current page, and one page on each side of it; leave out the rest.
- Don’t show it when there is only one page.
- On narrow screens, don’t paginate; auto-load on scrolling to the bottom, or offer a “Load more” button.
- Place it below the table, right-aligned or centered—the same across the product.
- Where a row of page numbers won’t fit, use one line of text, `.hao-pages__text`: “Page 1 of 12”, with the current page number in bold Song typeface (wrapped in `<b>`), flanked by arrows for the previous and next page.
- The whole control is a handscroll laid open: the page numbers sit on a strip of `surface` paper, with a `hairline` above and below and a roller at each end. Add `hao-pages--plain` to drop the scroll and keep only the numbers.
- The current page number is a “page-number seal”: a Song typeface numeral in a thin, clipped-corner frame—the same shape as a seal. Its color is `tint`, not cinnabar, because it says “you are here”; it isn’t an alert.
