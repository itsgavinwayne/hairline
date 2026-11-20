# ListGroup · 分组列表

iOS 式的分组列表，设置页和详情页的主体。

`<ul class="hao-list">` 里每个 `<li>` 放一个 `.hao-list__row`（可点的行用 `<a>` 或 `<button>`）。行内依次是 `.hao-list__title`（可带一行 `.hao-list__sub`）、可选的 `.hao-list__value`、可选的右侧控件或箭头。组的上方可放 `.hao-list-header`，下方可放 `.hao-list-footer`。

- 一组放两到七行；更多就拆成几组，组与组之间留 `space-6`。
- 能进入下一级的行才放箭头。
- 分隔线从文字左缘开始，不通到最左边，这是 iOS 的习惯，保留它。
- 列表组直接放在 `bg` 上，不要再包一层卡片。
- 在列表里单选时，选中的那行右侧放一个 `.hao-list__check`，是一笔 `tint` 色的提勾，和勾选框里的勾同一个笔形。

**无障碍**

- 可点的行用 `<a>` 或 `<button>`，高 44px，Tab 逐行走得到；聚焦时描 `focus` 色的边。
- 行尾的箭头图标和行里的印照预览写 `aria-hidden="true"`，读屏读的是行名、副题和值。
- 做单选时照预览的写法：`<ul>` 上写 `role="listbox"` 和 `aria-label`，每个 `<li>` 写 `role="none"`，里面的 `<button>` 写 `role="option"`，选中那行 `aria-selected="true"`，提勾 `.hao-list__check` 写 `aria-hidden="true"`。

**行为**（加载了行为脚本时）

- 写成 `role="listbox"` 的列表由脚本接管：点一行就选中它，提勾跟过去，列表发出 `hao-change` 事件，带上选中的是第几项。
- 整组只占一个 Tab 停靠点。上下方向键在各行之间移动，Home 和 End 跳到头尾；回车或空格选中。方向键只移动焦点，不改选中，因为这类选项多半一选就生效。
- 用 `<button>` 做行时不用再写内联样式去掉边框和底色，样式表已经处理了。

## 标记

### 中文

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div style="width:390px">
  <p class="hao-list-header">通用</p>
  <ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">外观</span><span class="hao-list__value">跟随系统</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">字号</span><span class="hao-list__value">标准</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">落款印章<span class="hao-list__sub">显示在每条札记的右上角</span></span><span class="hao-seal hao-seal--sm hao-seal--outline" aria-hidden="true">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
  </ul>
  <p class="hao-list-footer">外观设置会同步到你的所有设备。</p>
</div>
<div style="width:300px">
  <p class="hao-list-header">外观</p>
  <ul class="hao-list" role="listbox" aria-label="外观">
    <li role="none"><button class="hao-list__row" role="option" aria-selected="true"><span class="hao-list__title">跟随系统</span><span class="hao-list__check" aria-hidden="true"></span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">昼</span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">夜</span></button></li>
  </ul>
</div>
</div>
```

### English

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
<div style="width:390px">
  <p class="hao-list-header">General</p>
  <ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Appearance</span><span class="hao-list__value">Match system</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Text size</span><span class="hao-list__value">Standard</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Signature seal<span class="hao-list__sub">Shown at the top right of every note</span></span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
  </ul>
  <p class="hao-list-footer">Appearance settings sync to all your devices.</p>
</div>
<div style="width:300px">
  <p class="hao-list-header">Appearance</p>
  <ul class="hao-list" role="listbox" aria-label="Appearance">
    <li role="none"><button class="hao-list__row" role="option" aria-selected="true"><span class="hao-list__title">Match system</span><span class="hao-list__check" aria-hidden="true"></span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">Day</span></button></li>
    <li role="none"><button class="hao-list__row" role="option" aria-selected="false"><span class="hao-list__title">Night</span></button></li>
  </ul>
</div>
</div>
```
