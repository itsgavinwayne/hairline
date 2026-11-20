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
