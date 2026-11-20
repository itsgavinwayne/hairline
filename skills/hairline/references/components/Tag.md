# Tag · 标签

标出一条内容当前的状态，不可点。

用 `<span class="hao-tag">` 加一个色调类：默认（中性）、`hao-tag--tint`、`hao-tag--jade`、`hao-tag--amber`、`hao-tag--seal`。文字由你提供，两到四个字。

- 状态靠文字说清，颜色只是帮忙；不要出现只有圆点没有字的标签。
- 一行里最多两个标签。
- `hao-tag--seal` 只给真的需要处理的问题。

**无障碍**

- 标签就是 `<span>` 里那几个字，前头的圆点是 `::before` 画的，读屏只读文字。
- 五个色调类只改配色，不改结构，也不改读出来的内容。

## 标记

### 中文

```html
<div class="hao-row">
  <span class="hao-tag">草稿</span>
  <span class="hao-tag hao-tag--tint">进行中</span>
  <span class="hao-tag hao-tag--jade">已完成</span>
  <span class="hao-tag hao-tag--amber">今天到期</span>
  <span class="hao-tag hao-tag--seal">已逾期</span>
</div>
```

### English

```html
<div class="hao-row">
  <span class="hao-tag">Draft</span>
  <span class="hao-tag hao-tag--tint">In progress</span>
  <span class="hao-tag hao-tag--jade">Done</span>
  <span class="hao-tag hao-tag--amber">Due today</span>
  <span class="hao-tag hao-tag--seal">Overdue</span>
</div>
```
