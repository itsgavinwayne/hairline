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
