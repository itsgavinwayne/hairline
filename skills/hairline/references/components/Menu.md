# Menu · 菜单

点一下「更多」或长按之后弹出的一小组动作，贴着触发它的东西出现。

`<ul class="hao-menu" role="menu">` 里放若干 `.hao-menu__item`（`role="menuitem"`），文字在左、图标在右；用 `.hao-menu__sep` 分组。删除类加 `hao-menu__item--danger`，放最后一组。文字和图标由你提供。

- 二到七项。更多就分层，或改用底部弹层。
- 每项一个动词开头的短语，全组用同样的句式。
- 宽屏上用菜单，窄屏上同样的内容用 `Sheet`。
- 方向键上下移动，回车执行，Esc 关闭并把焦点还给触发按钮。
- 菜单浮在 `shadow-float` 上，不加遮罩。

**行为**（加载了行为脚本时）

- 菜单平时带 `hidden`，触发按钮写 `data-hao-menu="菜单的 id"`。脚本会给按钮补上 `aria-haspopup` 和 `aria-expanded`。
- 点按钮，菜单像一挂帘子从按钮下方放下来（下面放不下就翻到上面），焦点落到第一项。菜单在 `z-popover` 这一层，在弹窗里打开也不会被盖住。
- 上下方向键在各项之间移动并首尾循环，Home 和 End 跳到头尾；回车或点击执行并关闭；Esc 关闭并把焦点还给按钮；点别处或按 Tab 也会关闭。
- 在按钮上按上下方向键也能打开。选中一项时，那一项会发出 `hao-select` 事件。

## 标记

### 中文

```html
<ul class="hao-menu" role="menu" style="width:240px">
  <li role="none"><button class="hao-menu__item" role="menuitem">分享<i class="hao-icon hao-icon--share" aria-hidden="true"></i></button></li>
  <li role="none"><button class="hao-menu__item" role="menuitem">移到文件夹<i class="hao-icon hao-icon--folder" aria-hidden="true"></i></button></li>
  <li role="none"><button class="hao-menu__item" role="menuitem">复制一份<i class="hao-icon hao-icon--copy" aria-hidden="true"></i></button></li>
  <li class="hao-menu__sep" role="separator"></li>
  <li role="none"><button class="hao-menu__item hao-menu__item--danger" role="menuitem">删除<i class="hao-icon hao-icon--trash" aria-hidden="true"></i></button></li>
</ul>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-menu="live-m-zh"><i class="hao-icon hao-icon--more" aria-hidden="true"></i>更多操作</button></div>
<ul class="hao-menu" role="menu" id="live-m-zh" hidden><li role="none"><button class="hao-menu__item" role="menuitem">分享<i class="hao-icon hao-icon--share" aria-hidden="true"></i></button></li><li role="none"><button class="hao-menu__item" role="menuitem">移到文件夹<i class="hao-icon hao-icon--folder" aria-hidden="true"></i></button></li><li role="none"><button class="hao-menu__item" role="menuitem">复制一份<i class="hao-icon hao-icon--copy" aria-hidden="true"></i></button></li><li class="hao-menu__sep" role="separator"></li><li role="none"><button class="hao-menu__item hao-menu__item--danger" role="menuitem">删除<i class="hao-icon hao-icon--trash" aria-hidden="true"></i></button></li></ul>
```

### English

```html
<ul class="hao-menu" role="menu" style="width:240px">
  <li role="none"><button class="hao-menu__item" role="menuitem">Share<i class="hao-icon hao-icon--share" aria-hidden="true"></i></button></li>
  <li role="none"><button class="hao-menu__item" role="menuitem">Move to folder<i class="hao-icon hao-icon--folder" aria-hidden="true"></i></button></li>
  <li role="none"><button class="hao-menu__item" role="menuitem">Duplicate<i class="hao-icon hao-icon--copy" aria-hidden="true"></i></button></li>
  <li class="hao-menu__sep" role="separator"></li>
  <li role="none"><button class="hao-menu__item hao-menu__item--danger" role="menuitem">Delete<i class="hao-icon hao-icon--trash" aria-hidden="true"></i></button></li>
</ul>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-menu="live-m-en"><i class="hao-icon hao-icon--more" aria-hidden="true"></i>More actions</button></div>
<ul class="hao-menu" role="menu" id="live-m-en" hidden><li role="none"><button class="hao-menu__item" role="menuitem">Share<i class="hao-icon hao-icon--share" aria-hidden="true"></i></button></li><li role="none"><button class="hao-menu__item" role="menuitem">Move to folder<i class="hao-icon hao-icon--folder" aria-hidden="true"></i></button></li><li role="none"><button class="hao-menu__item" role="menuitem">Duplicate<i class="hao-icon hao-icon--copy" aria-hidden="true"></i></button></li><li class="hao-menu__sep" role="separator"></li><li role="none"><button class="hao-menu__item hao-menu__item--danger" role="menuitem">Delete<i class="hao-icon hao-icon--trash" aria-hidden="true"></i></button></li></ul>
```
