# Menu

A small set of actions that pops open after a tap on “More” or a long press, appearing next to the thing that triggered it.

Inside `<ul class="hao-menu" role="menu">` go a number of `.hao-menu__item`s (`role="menuitem"`), text on the left and icon on the right; group them with `.hao-menu__sep`. Destructive items take `hao-menu__item--danger` and go in the last group. You provide the text and the icons.

- Two to seven items. For more, add another level, or switch to a sheet.
- Each item is a short phrase starting with a verb; keep the same sentence pattern across the group.
- Use the menu on wide screens; the same content on a narrow screen goes in a `Sheet`.
- The arrow keys move up and down, Enter runs an item, and Esc closes the menu and returns focus to the trigger button.
- The menu floats on `shadow-float`, with no scrim.

**Behavior** (when the behavior script is loaded)

- The menu carries `hidden` most of the time; on the trigger button write `data-hao-menu="menu-id"`. The script adds `aria-haspopup` and `aria-expanded` to the button.
- Tap the button and the menu appears just below it (flipping above when it won’t fit below), with focus landing on the first item. The menu sits on the `z-popover` layer, so even opened inside a dialog it won’t be covered.
- The up and down arrow keys move through the items and wrap from end to start; Home and End jump to the top and bottom; Enter or a tap runs an item and closes the menu; Esc closes it and returns focus to the button; a tap elsewhere or Tab closes it too.
- The up and down arrow keys on the button open it as well. When an item is chosen, it fires a `hao-select` event.

## Markup

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

### Chinese

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
