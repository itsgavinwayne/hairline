A toggle for saving a favorite, shaped like a hanging lamp: an unlit lamp when unsaved, lit once saved.

`<button class="hao-lamp" aria-pressed="true|false" aria-label="…">`. Dropped into a `Card`, it hangs at the top right corner, running down from the card’s top edge.

- The lamp is four things only: the cord, the cap, the body and the tassel, all in thin lines. Unsaved, the body is a gray outline; saved, it fills with `tint`.
- Filled versus outlined tells the two states apart, not color alone.
- The button itself is a 44px square, with the lamp down the middle only, so a finger lands true.
- The `aria-label` says what a tap does: “Save” when unsaved, “Unsave” when saved.
- Use this lamp, not stars or hearts. A card carrying a lamp takes no seal.
- No cinnabar, and never a red festival lantern. The bookmark is the reader’s own mark, not a holiday decoration and not the system’s notice.
- A screen can hold many of them: the lamp is the control’s own shape, covered by “shape follows the control”, not a scene.

**Behavior** (when the behavior script is loaded)

- Add `data-hao-toggle`, and one tap switches between saved and unsaved. Add `data-label-on` and `data-label-off` too, and the accessibility label follows (“Unsave”, “Save”).
