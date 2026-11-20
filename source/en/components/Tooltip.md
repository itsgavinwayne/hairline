A line of explanation that appears on hover or keyboard focus, naming buttons that hold only an icon.

A `<span class="hao-tip" role="tooltip">`; the element that triggers it points to it with `aria-describedby`. You supply the text.

- Supplementary information only. Nothing people must see belongs here, because there is no hover on a touchscreen.
- One sentence, no more than two lines, with no links or buttons inside.
- It appears half a second after hover and disappears when the pointer leaves; keyboard focus brings it up the same way.
- The colors are inverted—`ink` for the ground, `bg` for the text—matching the toast.

**Behavior** (when the behavior script is loaded)

- Write `data-hao-tip="Tip text"` on any element. It appears after the pointer rests half a second and disappears when the pointer leaves; the pointer can move onto the tip without dismissing it. Keyboard focus shows it at once, and it leaves with the focus; Esc dismisses it too.
- The tip appears centered above the element, or below when there’s no room above. The script links it to the element with `aria-describedby`.
