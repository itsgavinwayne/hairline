Pick one option from a set.

A `<label class="hao-radio">` wraps an `<input type="radio">` and its text; a group shares one `name`, goes inside `<fieldset class="hao-choices">`, and carries a `<legend>`.

- Use radio buttons for two to five options; for more, use a select. With only two or three very short options switching a view, use a segmented control.
- One option is always selected by default; put the most common or safest one first.
- Stack the options, one per line.

**Accessibility**

- It’s a native `<input type="radio">`: Tab stops once for the whole group, the arrow keys change the choice, Space selects—all built into the browser.
- On focus, a `focus`-colored ring is drawn.
- Selected or not is read from the `input`’s own state; the look of selection is the solid ring, never color alone.
