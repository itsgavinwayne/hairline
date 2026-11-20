A one-line acknowledgment that appears briefly after an action, without interrupting.

A `<div class="hao-toast" role="status">`, holding an optional icon, one line of text, and at most one `.hao-toast__action`. You supply the text.

- The colors are inverted—`ink` for the ground, `bg` for the text—so it stands out in both the day and night themes.
- One line, stating the result, in the same word as the button that triggered it: the button says “Save”, the toast says “Saved”.
- It appears at the bottom of the screen, above the tab bar, and dismisses itself after four seconds; one with “Undo” stays eight.
- Use it for success and neutral messages only. Errors take a banner or a dialog, because people need time to read.
- Show only one at a time.
- Add `hao-toast--enter`, and it floats up from below.
- A success acknowledgment is preceded by an upward hook stroke (提勾), `.hao-toast__ok`—the same stroke as the check in a checkbox. Neutral messages carry no icon.

**Behavior** (when the behavior script is loaded)

- From script, call `Hairline.toast('Saved', { ok: true })`; with an action, `Hairline.toast('Deleted', { action: 'Undo', onAction: fn })`. You can also write `data-hao-toast="text"` right on a button, with the optional `data-hao-toast-ok` and `data-hao-toast-action="Undo"`.
- The toast appears centered at the bottom of the screen, dismisses after four seconds, or eight with an action. The clock pauses while the pointer rests on it or focus is inside it.
- One toast at a time; later ones queue.
- Its region is a polite live region: a screen reader announces it without stealing focus.
