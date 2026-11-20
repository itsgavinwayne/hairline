# Switch · 开关

立即生效的开与关。

用 `<label class="hao-switch">` 包住文字和一个 `<input type="checkbox" role="switch">`。文字由你提供，写成名词（「每日提醒」），不写成问句。

- 拨动后马上生效，不需要再点保存。要等提交才生效的选项，用勾选框。
- 开启是 `tint`，关闭是 `border-control`。滑块在关闭时是空心的（中间透出轨道色），开启时是实心的，再加上位置，一共三重表达，不只靠颜色。
- 放进 `ListGroup` 的行里时，开关靠右。
- 暂时不能拨的加 `disabled`：开关降到 `opacity-disabled`，文字换成 `ink-tertiary`，指针变成禁止；在旁边说明原因。
- 关着的滑钮中间是一个小方孔，外圆内方，取铜钱的形；开着的滑钮是实心的。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <label class="hao-switch">每日提醒 <input type="checkbox" role="switch" checked></label>
  <label class="hao-switch">同步到 iCloud <input type="checkbox" role="switch"></label>
  <label class="hao-switch">蜂窝网络下同步 <input type="checkbox" role="switch" disabled></label>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <label class="hao-switch">Daily reminder <input type="checkbox" role="switch" checked></label>
  <label class="hao-switch">Sync to iCloud <input type="checkbox" role="switch"></label>
  <label class="hao-switch">Sync over cellular <input type="checkbox" role="switch" disabled></label>
</div>
```
