# Sheet

A sheet that rises from the bottom, holding a set of actions for the content at hand, or a short form.

Inside `.hao-scrim.hao-scrim--bottom` goes `.hao-sheet`: a `.hao-sheet__grabber` at the top, a line of `.hao-sheet__title`, then the content (usually a `ListGroup`), and at the end a full-width cancel button. You supply the title and the content.

- The sheet sits on `bg`, the list group inside it on `surface`—the same layering as an ordinary page.
- The title names what the actions act on (the note’s name), not “More actions”.
- No more than six actions. Destructive ones go last, in their own group.
- It can be closed by dragging down, by tapping the scrim, or with the cancel button—all three ways out must exist.
- Only the two top corners use `radius-xl`. No patterns inside a sheet.
- It enters by unrolling: add `hao-sheet--enter` to the sheet and `hao-scrim--enter` to the scrim. The sheet unfolds from the bottom up; it doesn’t slide in as a block.
- The grabber at the top, `.hao-sheet__grabber`, is drawn as a scroll roller with a knob at each end, echoing the “unroll” entrance.

**Behavior** (when the behavior script is loaded)

- The same setup as a dialog: the outer `<div class="hao-scrim hao-scrim--bottom" data-hao-modal hidden id="…">`, `data-hao-open` on the triggering button, `data-hao-close` on the closing button.
- It enters with the unrolling motion, and focus stays inside the sheet. Esc, the scrim, or Cancel closes it, and on close, focus returns to the triggering button.
- The drag-down-to-close gesture is not implemented; add it yourself if you need it.

**Accessibility**

- Write the semantics in full, as in the preview: `role="dialog"` and `aria-modal="true"` on `.hao-sheet`, with the title’s `id` pointed to by `aria-labelledby`.
- The sheet normally carries `hidden`, so without the script it never enters the Tab order; the grabber at the top, `.hao-sheet__grabber`, takes `aria-hidden="true"` as in the preview.
- To choose where focus lands when it opens, put `data-hao-initial` on a button inside the sheet; the script looks there first.

## Markup

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

### Chinese

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
