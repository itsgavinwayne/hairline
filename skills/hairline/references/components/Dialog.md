# Dialog · 弹窗

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

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
  <div style="position:relative;width:360px;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
    <div class="hao-scrim" style="position:absolute;inset:0">
      <div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="d1" aria-describedby="d1b">
        <h2 class="hao-dialog__title" id="d1">删除这条札记</h2>
        <p class="hao-dialog__body" id="d1b">删除后无法恢复，其中的两张图片也会一并删除。</p>
        <div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted">取消</button><button class="hao-btn hao-btn--seal">删除</button></div>
      </div>
    </div>
  </div>
  <div style="position:relative;width:360px;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
    <div class="hao-scrim" style="position:absolute;inset:0">
      <div class="hao-dialog" role="dialog" aria-modal="true" aria-labelledby="d2">
        <h2 class="hao-dialog__title" id="d2">开启每日提醒</h2>
        <p class="hao-dialog__body">每天早上八点提醒你写一条札记，随时可以在设置里关掉。</p>
        <div class="hao-dialog__actions hao-dialog__actions--stack"><button class="hao-btn">开启提醒</button><button class="hao-btn hao-btn--plain">暂时不用</button></div>
      </div>
    </div>
  </div>
</div>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-open="live-d-zh">打开确认弹窗</button><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);max-width:420px">试一试：按 Tab 键，焦点只在弹窗里转；按 Esc 关闭，焦点回到这个按钮。</span></div>
<div class="hao-scrim" id="live-d-zh" data-hao-modal hidden><div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="live-d-zh-t" aria-describedby="live-d-zh-b"><h2 class="hao-dialog__title" id="live-d-zh-t">删除这条札记</h2><p class="hao-dialog__body" id="live-d-zh-b">删除后无法恢复，其中的两张图片也会一并删除。</p><div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted" data-hao-close data-hao-initial>取消</button><button class="hao-btn hao-btn--seal" data-hao-close>删除</button></div></div></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
  <div style="position:relative;width:360px;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
    <div class="hao-scrim" style="position:absolute;inset:0">
      <div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="d1-en" aria-describedby="d1b-en">
        <h2 class="hao-dialog__title" id="d1-en">Delete this note</h2>
        <p class="hao-dialog__body" id="d1b-en">This can’t be undone. The two images in it will be deleted too.</p>
        <div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted">Cancel</button><button class="hao-btn hao-btn--seal">Delete</button></div>
      </div>
    </div>
  </div>
  <div style="position:relative;width:360px;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
    <div class="hao-scrim" style="position:absolute;inset:0">
      <div class="hao-dialog" role="dialog" aria-modal="true" aria-labelledby="d2-en">
        <h2 class="hao-dialog__title" id="d2-en">Turn on daily reminders</h2>
        <p class="hao-dialog__body">You’ll get a reminder to write a note at 8 every morning. Turn it off anytime in Settings.</p>
        <div class="hao-dialog__actions hao-dialog__actions--stack"><button class="hao-btn">Turn on reminders</button><button class="hao-btn hao-btn--plain">Not now</button></div>
      </div>
    </div>
  </div>
</div>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-open="live-d-en">Open the dialog</button><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);max-width:420px">Try it: Tab stays inside the dialog. Esc closes it and returns focus to this button.</span></div>
<div class="hao-scrim" id="live-d-en" data-hao-modal hidden><div class="hao-dialog" role="alertdialog" aria-modal="true" aria-labelledby="live-d-en-t" aria-describedby="live-d-en-b"><h2 class="hao-dialog__title" id="live-d-en-t">Delete this note</h2><p class="hao-dialog__body" id="live-d-en-b">This can’t be undone. The two images in it will be deleted too.</p><div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted" data-hao-close data-hao-initial>Cancel</button><button class="hao-btn hao-btn--seal" data-hao-close>Delete</button></div></div></div>
```
