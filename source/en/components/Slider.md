Drag to pick a value within a continuous range; it suits settings that don’t need an exact number.

Use an `<input class="hao-slider" type="range">`, with a label and a hint outside it in the `TextField` structure. Write the current value as a percentage in the inline `--v`, or the track won’t fill (Firefox needs no help).

- The value takes effect at once; you see the effect as you drag.
- Put the current value and what it means in the hint (“17, standard”).
- When you need an exact number, use a stepper or a text field.
- The thumb is 28px, the track 4px; the left and right arrow keys move one step at a time. On touch screens the draggable area grows to 44px tall.
- When it can’t be adjusted, add `disabled`; the whole control drops to `opacity-disabled`.
- At the center of the thumb sits a small azurite dot, like a jade bi disc (玉璧). It is shape only; it doesn’t stand for the value.

**Behavior** (when the behavior script is loaded)

- As you drag, the track fills along automatically; no need to write `--v` yourself.

**Accessibility**

- A native `<input type="range">` brings its own keyboard support: the arrow keys step the value, and Home and End jump to the ends.
- On focus, a `focus`-colored ring is drawn around the track.
- The track fill is for the eyes only; the real value lives on the `input`, and that is what a screen reader announces. Without the script you write `--v` yourself, and the value is unaffected.
