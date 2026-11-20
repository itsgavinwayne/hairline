# Dialog

A dialog that interrupts the task at hand and has to be answered first.

A `.hao-scrim` covers the page, holding a `.hao-dialog`: `.hao-dialog__title` (Song typeface), `.hao-dialog__body`, and `.hao-dialog__actions` (holding one or two `hao-btn` buttons). You provide the title, the message, and the button text. Confirmations like delete take `role="alertdialog"`, everything else takes `role="dialog"`, both with `aria-modal="true"`.

- Reach for it only when nothing can go on without an answer: confirming an irreversible action, asking for a permission. Ordinary outcome feedback belongs in a banner.
- The title names the act itself (“Delete this note”), never “Are you sure?”. The message gives the consequences, in a sentence or two.
- The buttons name the action (“Delete”, “Turn on reminders”), never “OK” or “Yes”. Two short buttons sit side by side, the escape on the left; when the words run long, add `hao-dialog__actions--stack` to set them vertically, the primary button on top.
- Delete actions use `hao-btn--seal`, which is that screen’s one touch of cinnabar; no seal and no pattern inside a dialog.
- On open, focus lands on the escape button, and Esc counts as Cancel; on close, focus returns to what opened it.
- No dialog on top of a dialog.
- For the entrance, give the dialog `hao-dialog--enter` (it fades in and scales up into place) and the scrim `hao-scrim--enter`.

**Behavior** (when the behavior script is loaded)

- The dialog carries `hidden` by default, inside `<div class="hao-scrim" data-hao-modal hidden id="…">`. The button that triggers it writes `data-hao-open="dialog-id"`, and a closing button inside writes `data-hao-close`.
- On open, focus falls on the button with `data-hao-initial` (or the first focusable one, if there is none) and stays inside the dialog; the rest of the page can’t be worked and doesn’t scroll along.
- Esc closes it; a tap on the scrim also closes `role="dialog"`, but not `role="alertdialog"`—there, a button must be chosen outright.
- On close, focus returns to the triggering button. From script you can also call `Hairline.dialog.open(element)` and `Hairline.dialog.close()`.

## Markup

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

### Chinese

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
