# TextField · 输入框

单行文字输入，带标签和一行说明。

结构是 `.hao-field` 里依次放 `.hao-field__label`、`.hao-field__input`、`.hao-field__hint`。你提供标签文字、占位符和说明；标签用 `for` 连到输入框。

- 标签始终显示在输入框上方，不用占位符代替标签。
- 出错时给 `.hao-field` 加 `hao-field--error`，输入框加 `aria-invalid="true"`，说明文字改成出了什么事、怎么改。描边会加粗到 2px，不只是变色。
- 占位符写一个示例或一句提示，不重复标签。
- 聚焦时描边变成 `tint` 并加粗到 2px，光标也是 `tint`。
- 有字数上限时，把说明和 `.hao-field__count` 一起放进 `.hao-field__foot`，写成「12 / 20」。快到上限不变色，超了才按出错处理。
- 暂时不能改的加 `disabled`：底换成 `surface-sunken`，字和标签换成 `ink-tertiary`，并在说明里写清为什么不能改。只给人看、可以选中复制的加 `readonly`：去掉填充，描边退成 `hairline`，字仍是 `ink`，仍然能聚焦。
- 多行输入用 `<textarea class="hao-field__input">`，至少四行高，可以向下拖大。

**行为**（加载了行为脚本时）

- 输入框有 `maxlength`、旁边有 `.hao-field__count` 时，字数会随输入自动更新成「12 / 20」。

## 标记

### 中文

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
