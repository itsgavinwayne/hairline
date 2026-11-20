# Button

A button that triggers an action. One primary button per screen.

Use `<button class="hao-btn">`; you provide the text, and it says clearly what a press does (“Save changes”, not “OK”).

| Class | Where to use it |
| --- | --- |
| `hao-btn` | The primary button, filled with `tint`. One per screen. |
| `hao-btn--tinted` | Secondary actions, on a `tint-wash` ground. |
| `hao-btn--plain` | Escapes like Cancel and Skip, or a second place to go beside the primary button; text only. |
| `hao-btn--seal` | Irreversible actions such as Delete. It counts as the screen’s one touch of cinnabar—no seal on the same screen. |
| `hao-btn--sm` | A small capsule inside a list row, 32px tall; leave a full 44px touch target around it. |
| `hao-btn--block` | Fills the container’s width, at the foot of a form. |

- Never stand two primary buttons side by side.
- Button text stays on one line, no more than three words (six characters in Chinese).
- When a button is disabled, add the `disabled` attribute and say nearby why it can’t be pressed. A disabled button is gray on gray—not a dimmed primary button—so it doesn’t read as the secondary kind.
- When a press means waiting, add `aria-busy="true"`: a small ring appears in front of the button, the text turns to its progressive form (“Saving”), and the button can’t be pressed again while it works. When it’s done, a toast says “Saved”.
- Buttons keep a minimum width of 88px (64px small), so a two-character button still carries enough weight; plain text buttons set no minimum.

## Markup

### English

```html
<div class="hao-stack" style="max-width:none">
  <div class="hao-row">
    <button class="hao-btn">Save changes</button>
    <button class="hao-btn hao-btn--tinted">Save as draft</button>
    <button class="hao-btn hao-btn--plain">Cancel</button>
    <button class="hao-btn hao-btn--seal">Delete this note</button>
  </div>
  <div class="hao-row">
    <button class="hao-btn hao-btn--sm">Follow</button>
    <button class="hao-btn hao-btn--sm hao-btn--tinted">Following</button>
    <button class="hao-btn" disabled>Save changes</button>
    <button class="hao-btn" aria-busy="true">Saving</button>
  </div>
</div>
```

### Chinese

```html
<div class="hao-stack" style="max-width:none">
  <div class="hao-row">
    <button class="hao-btn">保存修改</button>
    <button class="hao-btn hao-btn--tinted">存为草稿</button>
    <button class="hao-btn hao-btn--plain">取消</button>
    <button class="hao-btn hao-btn--seal">删除这条札记</button>
  </div>
  <div class="hao-row">
    <button class="hao-btn hao-btn--sm">关注</button>
    <button class="hao-btn hao-btn--sm hao-btn--tinted">已关注</button>
    <button class="hao-btn" disabled>保存修改</button>
    <button class="hao-btn" aria-busy="true">正在保存</button>
  </div>
</div>
```
