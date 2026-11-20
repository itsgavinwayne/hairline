# Radio · 单选

从一组选项里只选一项。

`<label class="hao-radio">` 包住一个 `<input type="radio">` 和文字，同组共用 `name`，放进 `<fieldset class="hao-choices">` 并写 `<legend>`。

- 二到五项时用单选；更多用下拉选择。只有两三个很短的选项、切换的是视图时，用分段控件。
- 总有一项是默认选中的，把最常用或最安全的放第一个。
- 选项竖排，一行一项。

**无障碍**

- 原生 `<input type="radio">`：Tab 进组只停一处，上下左右方向键换选，空格选中，都是浏览器自带。
- 聚焦时描一圈 `focus` 色的边。
- 选中与否读的是 `input` 自己的状态；选中的样子是那圈实边，不只靠颜色。

## 标记

### 中文

```html
<fieldset class="hao-choices">
  <legend>外观</legend>
  <label class="hao-radio"><input type="radio" name="a" checked> 跟随系统</label>
  <label class="hao-radio"><input type="radio" name="a"> 昼</label>
  <label class="hao-radio"><input type="radio" name="a"> 夜</label>
</fieldset>
```

### English

```html
<fieldset class="hao-choices">
  <legend>Appearance</legend>
  <label class="hao-radio"><input type="radio" name="a-en" checked> Match system</label>
  <label class="hao-radio"><input type="radio" name="a-en"> Day</label>
  <label class="hao-radio"><input type="radio" name="a-en"> Night</label>
</fieldset>
```
