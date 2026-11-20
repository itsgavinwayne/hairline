Pick one item from a list of six or more. It looks like an iOS pop-up button: a pale wash, azurite text, and a pair of up-and-down chevrons on the right.

`<span class="hao-select">` wraps a native `<select>`. You supply the options.

- Use the native `<select>`: on a phone it calls up the system’s own picker, exactly what iOS users expect. Don’t build a separate dropdown panel with script.
- On the desktop, the list of options that opens is drawn the same way as `Menu`: a `surface` fill, the `shadow-float` shadow, 44px rows, `surface-hover` on hover, and an azurite check to the right of the current option. The panel opens downward first and flips above only when it doesn’t fit; inside a list row (`hao-select--plain`) it aligns to the right. This is done with styles alone, no script.
- In browsers that can’t yet style the select panel, what opens is the system’s own pop-up menu; the system decides how it looks, and nothing stops working.
- The button is as wide as the current option, not the full row. Add `hao-select--block` to fill the row.
- On its own, give it a label and a hint outside it in the `TextField` structure, with the label above.
- Inside a `ListGroup` row, add `hao-select--plain`: no fill, the value right-aligned in `ink-secondary`, as in iOS Settings. Make the row title a `<label>` connected to the `id` of the `<select>`.
- The paired chevrons say “this opens a list of options”; a single downward chevron belongs to the accordion.
- With five options or fewer, use radio buttons; laying everything out beats hiding it.
- Order the options the way the person using them expects (by time, alphabet, or frequency), never arbitrarily.

**Accessibility**

- It’s a native `<select>`, 44px tall: Tab reaches it, Space or the arrow keys open the options, the arrow keys move, Enter selects, Esc closes—all built into the browser. Connect the label to its `id` with `for`.
- On focus, a `focus`-colored ring is drawn.
- The chevrons on the right are drawn by `.hao-select::after`, which a screen reader never sees; what gets read is the text of the `<option>`s.
