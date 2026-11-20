# Segmented · 分段控件

在两到五个并列视图之间切换。

`.hao-seg` 里每一段是 `<label><input type="radio" name="…"><span>文字</span></label>`，同一组共用一个 `name`。你提供每段的文字和整组的 `aria-label`。

- 每段一到两个字，各段等长。
- 只用来切换同一份内容的不同视图；跳到别的页面用标签栏。
- 超过五段改用列表或菜单。
- 窗口窄于 600px 时各段均分宽度，文字放不下会截断。

## 标记

### 中文

```html
<div class="hao-seg" role="radiogroup" aria-label="时间范围">
  <label><input type="radio" name="r" checked><span>日</span></label>
  <label><input type="radio" name="r"><span>周</span></label>
  <label><input type="radio" name="r"><span>月</span></label>
  <label><input type="radio" name="r"><span>年</span></label>
</div>
```

### English

```html
<div class="hao-seg" role="radiogroup" aria-label="Time range">
  <label><input type="radio" name="r-en" checked><span>Day</span></label>
  <label><input type="radio" name="r-en"><span>Week</span></label>
  <label><input type="radio" name="r-en"><span>Month</span></label>
  <label><input type="radio" name="r-en"><span>Year</span></label>
</div>
```
