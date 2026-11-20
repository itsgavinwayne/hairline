A dialog that interrupts the task at hand and has to be answered first.

A `.hao-scrim` covers the page, holding a `.hao-dialog`: `.hao-dialog__title` (Song typeface), `.hao-dialog__body`, and `.hao-dialog__actions` (holding one or two `hao-btn` buttons). You provide the title, the message, and the button text. Confirmations like delete take `role="alertdialog"`, everything else takes `role="dialog"`, both with `aria-modal="true"`.

- Reach for it only when nothing can go on without an answer: confirming an irreversible action, asking for a permission. Ordinary outcome feedback belongs in a banner.
- The title names the act itself (“Delete this note”), never “Are you sure?”. The message gives the consequences, in a sentence or two.
- The buttons name the action (“Delete”, “Turn on reminders”), never “OK” or “Yes”. Two short buttons sit side by side, the escape on the left; when the words run long, add `hao-dialog__actions--stack` to set them vertically, the primary button on top.
- Delete actions use `hao-btn--seal`, which is that screen’s one touch of cinnabar; no seal and no pattern inside a dialog.
- On open, focus lands on the escape button, and Esc counts as Cancel; on close, focus returns to what opened it.
- No dialog on top of a dialog.
- For the entrance, give the dialog `hao-dialog--enter` (it fades in and scales up into place) and the scrim `hao-scrim--enter`.

**Behavior** (when the behavior script is loaded)

- The dialog carries `hidden` by default, inside `<div class="hao-scrim" data-hao-modal hidden id="…">`. The button that triggers it writes `data-hao-open="dialog-id"`, and a closing button inside writes `data-hao-close`.
- On open, focus falls on the button with `data-hao-initial` (or the first focusable one, if there is none) and stays inside the dialog; the rest of the page can’t be worked and doesn’t scroll along.
- Esc closes it; a tap on the scrim also closes `role="dialog"`, but not `role="alertdialog"`—there, a button must be chosen outright.
- On close, focus returns to the triggering button. From script you can also call `Hairline.dialog.open(element)` and `Hairline.dialog.close()`.
