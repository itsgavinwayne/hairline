A divider of embroidery stitches in gold ink, taken from the most basic flat stitch.

Use an `<hr class="hao-stitch">`. It follows the width of its container; the only thing you decide is where it goes.

- Use it between two large blocks of content, or before the signature at the end of an article, in place of a solid rule. Between list rows, keep `hairline`—no stitches.
- It counts as one scene—at most one per screen; see the three rules in the guide.
- The color is `gold` only; don’t change it to `tint` or `seal`.
- The same stitched line appears in three other places, all shapes of the controls themselves, which don’t count as scenes: the stitched edge of a card (`hao-card--stitched`), the border of the upload box, and the stitching of the progress bar.

**Accessibility**

- Use a real `<hr class="hao-stitch">`; a screen reader treats it as a divider. Draw the line with a `<div>` instead, and that meaning is gone.
- The stitches are drawn as a background and hold no text, so a screen reader reads nothing from them.
