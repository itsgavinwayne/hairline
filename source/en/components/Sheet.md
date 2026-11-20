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
