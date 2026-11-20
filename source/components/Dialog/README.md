打断当前操作、必须先回答的弹窗。

`.hao-scrim` 遮住页面，里面放 `.hao-dialog`：`.hao-dialog__title`（宋体）、`.hao-dialog__body`、`.hao-dialog__actions`（放一到两个 `hao-btn`）。你提供标题、说明和按钮文字。确认删除这类用 `role="alertdialog"`，其余用 `role="dialog"`，都加 `aria-modal="true"`。

- 只在不回答就没法继续时用：确认不可撤销的动作、请求一项权限。普通的结果反馈用提示条。
- 标题写这件事本身（「删除这条札记」），不写「确定吗」。说明写后果，一到两句。
- 按钮写动作的名字（「删除」「开启提醒」），不写「确定」「是」。两个短按钮并排，退路在左；文字长时加 `hao-dialog__actions--stack` 竖排，主按钮在上。
- 删除类用 `hao-btn--seal`，它就是这一屏的朱砂；弹窗里不放印章和纹样。
- 打开时焦点落在退路按钮上，按 Esc 等于取消；关闭后焦点回到触发它的地方。
- 弹窗之上不再弹弹窗。
- 进场给弹窗加 `hao-dialog--enter`（原地淡入并放大到位），给遮罩加 `hao-scrim--enter`。

**行为**（加载了行为脚本时）

- 弹窗平时带 `hidden`，放在 `<div class="hao-scrim" data-hao-modal hidden id="…">` 里。触发它的按钮写 `data-hao-open="那个 id"`，弹窗里关闭的按钮写 `data-hao-close`。
- 打开时焦点落到带 `data-hao-initial` 的按钮上（没有就落到第一个能聚焦的），并且被圈在弹窗里；页面其余部分不可操作，也不跟着滚动。
- 按 Esc 关闭；`role="dialog"` 的点遮罩也能关闭，`role="alertdialog"` 的不能，必须明确选一个按钮。
- 关闭后焦点回到触发它的按钮。脚本里也可以调用 `Hairline.dialog.open(元素)` 和 `Hairline.dialog.close()`。
