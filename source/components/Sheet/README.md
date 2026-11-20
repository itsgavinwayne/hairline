从底部升起的弹层，放一组针对当前内容的动作或一小段表单。

`.hao-scrim.hao-scrim--bottom` 里放 `.hao-sheet`：顶部一个 `.hao-sheet__grabber`，一行 `.hao-sheet__title`，然后是内容（通常是一个 `ListGroup`），最后一个撑满的取消按钮。你提供标题和内容。

- 弹层的底是 `bg`，里面的列表组是 `surface`，和普通页面的层次一样。
- 标题写这些动作针对的对象（札记的名字），不写「更多操作」。
- 动作不超过六项。删除类放在最后，单独成组。
- 可以下拉关闭，点遮罩关闭，取消按钮也能关闭，三种退路都要有。
- 只有顶部两个角用 `radius-xl`。弹层里不放纹样。
- 进场用「展卷」：给弹层加 `hao-sheet--enter`，给遮罩加 `hao-scrim--enter`。弹层由下而上展开，不是整块滑入。
- 顶上的把手 `.hao-sheet__grabber` 画成一根轴，两端各一个轴头，呼应「展卷」的进场。

**行为**（加载了行为脚本时）

- 和弹窗同一套：外层 `<div class="hao-scrim hao-scrim--bottom" data-hao-modal hidden id="…">`，触发按钮写 `data-hao-open`，关闭按钮写 `data-hao-close`。
- 打开时用「展卷」进场，焦点圈在弹层里；按 Esc、点遮罩、点取消都能关，关闭后焦点回到触发它的按钮。
- 下拉关闭的手势没有实现，需要时自己加。

**无障碍**

- 语义照预览写全：`.hao-sheet` 上 `role="dialog"` 和 `aria-modal="true"`，标题的 `id` 用 `aria-labelledby` 指过去。
- 弹层平时带 `hidden`，不加载脚本也占不进 Tab 顺序；顶部的把手 `.hao-sheet__grabber` 照预览写 `aria-hidden="true"`。
- 要指定打开后的焦点落点，在弹层里的按钮上写 `data-hao-initial`，脚本会先找它。
