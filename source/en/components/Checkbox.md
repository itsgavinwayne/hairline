Check any number of items from a set; they take effect when submitted.

A `<label class="hao-check">` wraps an `<input type="checkbox">` and its text; several go in a `<fieldset class="hao-choices">`, with a `<legend>` saying what the group is choosing. You provide the text.

- If the choice takes effect the moment it’s made, use a switch; if it takes effect on Save, use a checkbox.
- Write labels as positive statements (“Include completed to-dos”), not negations that make the reader flip the meaning in their head.
- The whole row is tappable, and no shorter than 44px.
- When disabled, give the reason in the label.
- The check mark is one brushstroke of the upward hook stroke—heavy at the start, tapering at the end—not a geometric zigzag. Don’t swap in a different icon.
- When “Select all” covers only some of the set, it shows the indeterminate state (set `indeterminate = true` in script): a horizontal bar in the box, like the Han character “one” (一).

**Behavior** (when the behavior script is loaded)

- On the “Select all” checkbox write `data-hao-checkall="group"`, and on the checkboxes it governs, the same `name`. Tick “Select all” and every box fills; tick only some, and “Select all” turns into the indeterminate “一” on its own.

**Accessibility**

- The checkbox is a native `<input type="checkbox">`: Tab reaches it, Space ticks or clears it, all straight from the browser.
- On focus, a `focus`-colored ring is drawn around the box.
- The brushstroke check in the box, the indeterminate bar, and the dim of disabled all follow the `input`’s own state; a screen reader reads the state, not just the color.
