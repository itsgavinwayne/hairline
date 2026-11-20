# TabBar · Tab bar

The tab bar at the bottom of the screen, for switching among a product’s top-level areas.

Inside `<nav class="hao-tabbar">` go three to five `.hao-tabbar__item`s, each a 24px icon plus one word; the current page carries `aria-current="page"`. You supply the icons and the words.

- Three to five items. With two, use a segmented control; past six, rethink the structure.
- One word per item: two characters in Chinese, no more than eight letters in English. There is always text under the icon.
- The current item is `tint`, the rest `ink-tertiary`; no fill, dot, or underline.
- It uses the `material` frosted glass, is fixed to the bottom, and leaves room for the safe area below.
- The tab bar only navigates; actions like “New” don’t belong in it.

## Markup

### English

```html
<nav class="hao-tabbar" aria-label="Main" style="max-width:390px;border-radius:var(--hao-radius-md)">
  <a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>Me</a>
</nav>
```

### Chinese

```html
<nav class="hao-tabbar" aria-label="主导航" style="max-width:390px;border-radius:var(--hao-radius-md)">
  <a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>我的</a>
</nav>
```
