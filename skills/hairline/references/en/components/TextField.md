# TextField · Text field

A single-line text input with a label and one line of hint text.

The structure is `.hao-field` holding, in order, `.hao-field__label`, `.hao-field__input`, and `.hao-field__hint`. You supply the label text, the placeholder, and the hint; the label connects to the input with `for`.

- The label always shows above the input; never use the placeholder in place of a label.
- On error, add `hao-field--error` to `.hao-field` and `aria-invalid="true"` to the input, and change the hint to say what went wrong and how to fix it. The border thickens to 2px; it doesn’t just change color.
- Let the placeholder hold an example or a short prompt, not a repeat of the label.
- On focus, the border turns `tint` and thickens to 2px, and the caret turns `tint` too.
- With a character limit, put the hint and the `.hao-field__count` together in `.hao-field__foot`, written “12 / 20”. Nothing changes near the limit; only going over is treated as an error.
- For a field that can’t be changed for now, add `disabled`: the fill becomes `surface-sunken`, the text and label become `ink-tertiary`, and the hint says why it can’t be changed. For a value that is only shown and can be selected and copied, add `readonly`: the fill goes away, the border drops back to `hairline`, the text stays `ink`, and the field still takes focus.
- For multiline input, use a `<textarea class="hao-field__input">`, at least four lines tall, draggable taller from the bottom.

**Behavior** (when the behavior script is loaded)

- When the input has a `maxlength` and a `.hao-field__count` beside it, the count updates as you type, in the form “12 / 20”.

## Markup

### English

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="a-en">Title</label>
    <input class="hao-field__input" id="a-en" placeholder="Name this note" maxlength="20">
    <span class="hao-field__foot"><span class="hao-field__hint">Shown in the list</span><span class="hao-field__count">0 / 20</span></span>
  </div>
  <div class="hao-field hao-field--error" style="width:300px">
    <label class="hao-field__label" for="b-en">Email</label>
    <input class="hao-field__input" id="b-en" value="linwan@" aria-invalid="true" aria-describedby="b-hint-en">
    <span class="hao-field__hint" id="b-hint-en">Incomplete address. Add the part after @.</span>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="c-en">Body</label>
    <textarea class="hao-field__input" id="c-en" placeholder="What do you want to remember today"></textarea>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="d-en">Sync account</label>
    <input class="hao-field__input" id="d-en" value="linwan@example.com" disabled aria-describedby="d-hint-en">
    <span class="hao-field__hint" id="d-hint-en">Turn on sync to change this</span>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="e-en">Note number</label>
    <input class="hao-field__input" id="e-en" value="N-2026-1120" readonly aria-describedby="e-hint-en">
    <span class="hao-field__hint" id="e-hint-en">Generated for you. Select to copy.</span>
  </div>
</div>
```

### Chinese

```html
<div class="hao-row" style="align-items:flex-start;gap:var(--hao-space-6)">
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="a">标题</label>
    <input class="hao-field__input" id="a" placeholder="给这条札记起个名字" maxlength="20">
    <span class="hao-field__foot"><span class="hao-field__hint">会显示在列表里</span><span class="hao-field__count">0 / 20</span></span>
  </div>
  <div class="hao-field hao-field--error" style="width:300px">
    <label class="hao-field__label" for="b">邮箱</label>
    <input class="hao-field__input" id="b" value="linwan@" aria-invalid="true" aria-describedby="b-hint">
    <span class="hao-field__hint" id="b-hint">邮箱地址不完整，补上 @ 后面的部分</span>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="c">正文</label>
    <textarea class="hao-field__input" id="c" placeholder="今天想记下什么"></textarea>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="d">同步账号</label>
    <input class="hao-field__input" id="d" value="linwan@example.com" disabled aria-describedby="d-hint">
    <span class="hao-field__hint" id="d-hint">开启同步后才能修改</span>
  </div>
  <div class="hao-field" style="width:300px">
    <label class="hao-field__label" for="e">札记编号</label>
    <input class="hao-field__input" id="e" value="N-2026-1120" readonly aria-describedby="e-hint">
    <span class="hao-field__hint" id="e-hint">自动生成，可以选中复制</span>
  </div>
</div>
```
