# Sheet · 底部弹层

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

## 标记

### 中文

```html
<div style="position:relative;width:360px;max-width:100%;box-sizing:border-box;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline);width:390px;max-width:100%;box-sizing:border-box;height:420px"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
  <div class="hao-scrim hao-scrim--bottom" style="position:absolute;inset:0">
    <div class="hao-sheet" role="dialog" aria-modal="true" aria-labelledby="s1">
      <div class="hao-sheet__grabber" aria-hidden="true"></div>
      <h2 class="hao-sheet__title" id="s1">晨间札记</h2>
      <ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">分享</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">移到文件夹</span><span class="hao-list__value">随笔</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">导出为 PDF</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
      </ul>
      <button class="hao-btn hao-btn--tinted hao-btn--block">取消</button>
    </div>
  </div>
</div>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-open="live-s-zh">打开底部弹层</button></div>
<div class="hao-scrim hao-scrim--bottom" id="live-s-zh" data-hao-modal hidden><div class="hao-sheet" role="dialog" aria-modal="true" aria-labelledby="live-s-zh-t"><div class="hao-sheet__grabber" aria-hidden="true"></div><h2 class="hao-sheet__title" id="live-s-zh-t">晨间札记</h2><ul class="hao-list"><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">分享</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">移到文件夹</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">导出为 PDF</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li></ul><button class="hao-btn hao-btn--tinted hao-btn--block" data-hao-close>取消</button></div></div>
```

### English

```html
<div style="position:relative;width:360px;max-width:100%;box-sizing:border-box;height:380px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline);width:390px;max-width:100%;box-sizing:border-box;height:420px"><div style="position:absolute;inset:0;padding:var(--hao-space-5);display:flex;flex-direction:column;gap:var(--hao-space-4)" aria-hidden="true"><div style="height:40px;width:120px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="height:120px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div>
  <div class="hao-scrim hao-scrim--bottom" style="position:absolute;inset:0">
    <div class="hao-sheet" role="dialog" aria-modal="true" aria-labelledby="s1-en">
      <div class="hao-sheet__grabber" aria-hidden="true"></div>
      <h2 class="hao-sheet__title" id="s1-en">Morning note</h2>
      <ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Share</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Move to folder</span><span class="hao-list__value">Essays</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Export as PDF</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
      </ul>
      <button class="hao-btn hao-btn--tinted hao-btn--block">Cancel</button>
    </div>
  </div>
</div>
<div class="hao-row" style="margin-top:var(--hao-space-5)"><button class="hao-btn hao-btn--tinted" data-hao-open="live-s-en">Open the sheet</button></div>
<div class="hao-scrim hao-scrim--bottom" id="live-s-en" data-hao-modal hidden><div class="hao-sheet" role="dialog" aria-modal="true" aria-labelledby="live-s-en-t"><div class="hao-sheet__grabber" aria-hidden="true"></div><h2 class="hao-sheet__title" id="live-s-en-t">Morning note</h2><ul class="hao-list"><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">Share</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">Move to folder</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li><li><button class="hao-list__row" data-hao-close style="width:100%;border:0;background:none;text-align:left"><span class="hao-list__title">Export as PDF</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></button></li></ul><button class="hao-btn hao-btn--tinted hao-btn--block" data-hao-close>Cancel</button></div></div>
```
