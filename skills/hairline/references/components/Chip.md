# Chip · 筛选标签

可以点选的胶囊，用来筛选一个列表。

`<button class="hao-chip" aria-pressed="true|false">`，里面是一个勾（选中时才显示）和文字。一组放进带 `aria-label` 的容器。文字由你提供。

- 和 `Tag` 的分工：标签只是展示状态，不可点；筛选标签是按钮，点了列表就变。两者长得不同，不要混用。
- 选中时底色、描边、字色、勾四样一起变，不只靠颜色。
- 一行放不下就横向滚动，不折成两行。
- 每个一到四个字。
- 形是一枚签牌：四个角是略不相等的小切角，左端一个穿绳的小孔。选中后小孔换成提勾。

**行为**（加载了行为脚本时）

- 给每个筛选标签加 `data-hao-toggle`，点一下在选中和未选中之间切换，并发出 `hao-change` 事件。
- 一组里只能选一个时，给外层容器加 `data-hao-chips="single"`：选中一个，其余自动取消，已选中的那个点不掉。

## 标记

### 中文

```html
<div class="hao-row" role="group" data-hao-chips="single" aria-label="按状态筛选">
  <button class="hao-chip" data-hao-toggle aria-pressed="true">全部</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">草稿</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">进行中</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">已发布</button>
</div>
```

### English

```html
<div class="hao-row" role="group" data-hao-chips="single" aria-label="Filter by status">
  <button class="hao-chip" data-hao-toggle aria-pressed="true">All</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">Draft</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">In progress</button>
  <button class="hao-chip" data-hao-toggle aria-pressed="false">Published</button>
</div>
```
