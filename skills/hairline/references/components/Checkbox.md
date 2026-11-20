# Checkbox · 勾选框

从一组选项里勾选任意几项，提交后才生效。

`<label class="hao-check">` 包住一个 `<input type="checkbox">` 和文字；多个放进 `<fieldset class="hao-choices">`，用 `<legend>` 说明这组在选什么。文字由你提供。

- 选了马上生效的用开关，要点保存才生效的用勾选框。
- 文字写成肯定句（「包含已完成的待办」），不写成否定句让人反着想。
- 整行都能点，高度不低于 44px。
- 禁用时在文字里说明原因。
- 选中的勾是一笔提勾的笔形，起笔重、收笔尖，不是几何折线。不要换成别的图标。
- 「全选」只选了一部分时是半选态（脚本里设 `indeterminate = true`）：框里是一道横，像汉字的「一」。

**行为**（加载了行为脚本时）

- 「全选」那个勾选框写 `data-hao-checkall="组名"`，它管的那些勾选框写同样的 `name`。勾全选，全部勾上；只勾了一部分，全选自动变成半选的「一」。

**无障碍**

- 勾选框是原生 `<input type="checkbox">`：Tab 走到，空格勾选或取消，浏览器自带。
- 聚焦时框外描一圈 `focus` 色的边。
- 框里的笔勾、半选的横、禁用的淡都跟着 `input` 自身的状态走，读屏读的是状态，不只认颜色。

## 标记

### 中文

```html
<fieldset class="hao-choices">
  <legend>每周回顾里包含</legend>
  <label class="hao-check"><input type="checkbox" data-hao-checkall="rev-zh"> 全选</label>
  <label class="hao-check"><input type="checkbox" name="rev-zh" checked> 已完成的待办</label>
  <label class="hao-check"><input type="checkbox" name="rev-zh"> 本周写的札记</label>
  <label class="hao-check"><input type="checkbox" disabled> 阅读时长（需要先开启统计）</label>
</fieldset>
```

### English

```html
<fieldset class="hao-choices">
  <legend>Include in the weekly review</legend>
  <label class="hao-check"><input type="checkbox" data-hao-checkall="rev-en"> Select all</label>
  <label class="hao-check"><input type="checkbox" name="rev-en" checked> Completed to-dos</label>
  <label class="hao-check"><input type="checkbox" name="rev-en"> Notes written this week</label>
  <label class="hao-check"><input type="checkbox" disabled> Reading time (turn on tracking first)</label>
</fieldset>
```
