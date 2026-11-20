# TabBar · 标签栏

屏幕底部的标签栏，在产品的几个顶层区域之间切换。

`<nav class="hao-tabbar">` 里放三到五个 `.hao-tabbar__item`，每个是一个 24px 图标加一个词；当前页加 `aria-current="page"`。你提供图标和文字。

- 三到五项。两项用分段控件，六项以上重新想信息结构。
- 每项一个词，中文两个字，英文不超过八个字母。图标下面总有字。
- 当前项用 `tint`，其余用 `ink-tertiary`；不加底色、圆点或下划线。
- 用 `material` 毛玻璃，固定在底部，底下留出安全区。
- 标签栏只做导航，不放「新建」这类动作。

## 标记

### 中文

```html
<nav class="hao-tabbar" aria-label="主导航" style="max-width:390px;border-radius:var(--hao-radius-md)">
  <a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>我的</a>
</nav>
```

### English

```html
<nav class="hao-tabbar" aria-label="Main" style="max-width:390px;border-radius:var(--hao-radius-md)">
  <a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes</a>
  <a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>Me</a>
</nav>
```
