A tappable capsule for filtering a list.

`<button class="hao-chip" aria-pressed="true|false">`, holding a check mark (it shows only when selected) and the text. Put a group of them in a container that carries an `aria-label`. You provide the text.

- The split with `Tag`: a tag only displays a state and can’t be tapped; a chip is a button, and tapping one changes the list. They look different—don’t mix them up.
- Selected changes four things at once—background, border, text color, and check mark—not color alone.
- When a row runs out of room it scrolls sideways; it never folds into two lines.
- One or two words apiece (one to four characters in Chinese).
- Its shape is a tag: four small clipped corners, each slightly different, and a hole for the cord at the left end. When selected, the hole becomes the hook stroke.

**Behavior** (when the behavior script is loaded)

- Give each chip `data-hao-toggle`; a tap switches it between selected and unselected and fires a `hao-change` event.
- When only one in a group can be selected, put `data-hao-chips="single"` on the outer container: picking one clears the others, and the one already selected can’t be tapped off.
