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
