This system’s own icons: 39 of them, line style, monochrome.

In an interface, use `<i class="hao-icon hao-icon--name" aria-hidden="true"></i>`; the color follows the text it sits with, and `hao-icon--sm` is the 20px size. The same drawings also ship as SVG files in the Icons group under resources, for design files and documents.

**How they’re drawn**

- A 24px grid, the drawing filling the middle 18 to 20px, with clear space on every side.
- The stroke is 1.5px, with round caps and round joins. No fills, apart from a few solid dots.
- **Leave a breathing gap.** Every closed outline holds a small opening instead of being drawn shut: the circle breaks at the upper right, the square at the lower left. It reads like the lift of the brush at the end of a stroke, and it lets the icon breathe at small sizes. This is what sets these icons apart most from other line icons.
- Draw only the strokes that are needed. If three strokes tell it, don’t use five.

**A few drawn from objects**

- Seven icons leave the common drawing for the shape of a studio object: edit is a brush (`edit`), the folder is a book case (`folder`), the image is a hanging scroll (`image`), notes are a thread-bound book (`notes`), the bookmark is a lamp (`bookmark`), the signature is a seal (`seal`), and home is a moon gate (`gate`).
- The rest keep the common drawing. Search, close, the chevrons and the four states have to be recognized at a glance, and are not redrawn for character.
- To draw another of this kind, look in the table under “Imagery”: decide what has to be said, then find an object that already means it; drop anything that can’t be read at 24px.

**How to use them**

- Only two sizes: 24px and 20px. Where something larger is called for, use a vignette or the mark, not a scaled-up icon.
- An icon never carries meaning on its own: it sits beside text, or the button carries an `aria-label`. The icon itself always takes `aria-hidden="true"`.
- Color follows the text; an icon is never colored on its own. The color of a status icon is set by the banner it sits in.
- Each of the four states has its fixed icon: `info`, `success`, `warning`, `error`. Don’t trade them around, and don’t use other icons for states.
- The checks inside checkboxes, chips, and toasts are the other brush form (the upward hook stroke)—part of those controls themselves, not part of this set.

**Adding an icon**

First look through the 39 for one that says close to the same thing. If none does, draw to the rules above—the same grid, stroke, and round caps, plus one breathing gap—then add it to the table. Don’t mix in icons from another set.

In native interfaces on Apple platforms, SF Symbols at the Regular weight can stand in; the two run close in weight.
