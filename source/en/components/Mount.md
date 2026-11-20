Mounts a picture worth pausing on: silk borders on all four sides, and, on a vertical piece, a rod along the bottom.

Inside `<figure class="hao-mount">` go one `<img>` (or SVG) and a `<figcaption>`. A horizontal piece adds `hao-mount--wide`. You provide the picture; the painting in the preview is a placeholder line drawing.

- **Hanging scroll** (the default, vertical): the silk above is wider than the silk below, roughly three to two—these are the “heaven” (天头) and “earth” (地头) bands; a slim rod along the top, and along the bottom a rod whose two ends poke out.
- **Horizontal scroll** (`hao-mount--wide`, horizontal): the silk at the sides is wider than at top and bottom, and there is no rod.
- Around the painting runs a very fine line of gold ink, the border strip (局条) of a mounting. The painting itself keeps square corners—no rounding. This is one of the few places in the system without rounded corners, because paintings are square.
- The silk uses `surface-sunken`, plain, with no pattern.
- Give it only to pictures worth stopping for: an article’s lead image, works, covers. Thumbnails in lists, avatars, and screenshots don’t get mounted.
- One per screen. It already carries enough weight; put no pattern beside it.
- The image needs `alt`; the `<figcaption>` is the picture’s name, one to three words (two to six characters in Chinese), centered.
- The hanging scroll defaults to 220px wide and the horizontal scroll to 420px; override the width and the proportions follow.
- Two “startled swallows” (惊燕) hang in the upper margin of the hanging scroll: the pair of silk strips such a scroll has always carried. The horizontal mounting has none.

**Accessibility**

- The painting needs a name: an SVG painting takes `role="img"` and `aria-label` as in the preview, so a screen reader treats it as a named image; an `<img>` gets its name from `alt`.
- The silk borders, the rods, and the border strip are all drawn with pseudo-elements and stay out of the screen reader.
- The `<figure>` and `<figcaption>` pair lets screen readers natively match the painting with its name; no extra attributes needed.
