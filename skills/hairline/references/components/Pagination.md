# Pagination · 分页

在很多页的列表或表格之间翻页，用在宽屏。

`<nav aria-label="分页">` 里放 `<ul class="hao-pages">`，每项是 `.hao-pages__item`；当前页 `aria-current="page"`，到头的箭头 `aria-disabled="true"`，省略处用 `.hao-pages__gap`。

- 始终显示第一页、最后一页、当前页和它左右各一页，其余省略。
- 只有一页时不显示。
- 窄屏不用分页，改成滚到底自动加载或一个「加载更多」按钮。
- 放在表格下方，靠右或居中，全产品统一。
- 放不下一排页码的地方，用一行文字 `.hao-pages__text`：「第 1 页，共 12 页」，当前页码用宋体加粗（包在 `<b>` 里），配上一页、下一页两个箭头。
- 整条分页是一幅横展的手卷：页码排在一条 `surface` 的纸上，上下各一道 `hairline`，两端各一根轴。不想要这层意思时加 `hao-pages--plain`，只留页码。
- 当前页码是一枚「页码印」：宋体数字，外面一圈切角的细框，形状和印章一样。颜色用 `tint` 不用朱砂，因为它表示「你在这里」，不是提醒。

## 标记

### 中文

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
