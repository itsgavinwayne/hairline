# Breadcrumb

A one-line path that shows where you are and how to get back up. For wide screens with three or more levels.

Inside `<nav aria-label="Breadcrumb">` goes an `<ol class="hao-crumbs">`: every level up to the last is a link, and the last level is the current page—not a link—marked `aria-current="page"`.

- The current page is `ink`, the levels above are `ink-secondary`, with a small arrow between them.
- Under three levels, skip it; the navigation bar’s back control is enough.
- On narrow screens, no breadcrumbs—use the navigation bar’s back button.
- When the path runs long, drop the middle levels and keep the first level and the last two.

## Markup

### English

```html
<nav aria-label="Location"><ol class="hao-crumbs"><li><a href="#">Notes</a></li><li><a href="#">Reading</a></li><li aria-current="page">Notes on The Craft of Gardens</li></ol></nav>
```

### Chinese

```html
<nav aria-label="位置"><ol class="hao-crumbs"><li><a href="#">札记</a></li><li><a href="#">读书</a></li><li aria-current="page">《园冶》读书笔记</li></ol></nav>
```
