A card holding one piece of standalone content, with the title in the Song typeface.

`.hao-card` holds `.hao-card__title`, `.hao-card__body`, and an optional `.hao-card__meta`. When the card needs a signature, add a `.hao-seal.hao-seal--sm.hao-seal--outline.hao-card__seal` at the head. You provide the title, the body, and the date.

- Cards sit on `bg`, and no card goes inside a card.
- Only one card per screen takes a seal.
- When the whole card is tappable, make the card one `<a>` and put no button inside.
- Keep the body within four lines; anything longer goes to a detail page.

Two variants carry patterns; use at most one of them per screen:

- `hao-card--wave`: two courses of the wave pattern along the bottom edge, for the screen’s most important card.
- `hao-card--stitched`: a round of gold ink stitching along the inner edge, like the edging stitch on an embroidered piece, for content with the feel of “a made object”—saved things, handwork. A stitched card takes no seal.

**Accessibility**

- Write the title as a real heading element; in the preview it’s `<h3 class="hao-card__title">`. Swap in a `<span>` that only looks like a title, and screen readers lose one path of jumping by heading.
- The signature seal is hidden from screen readers: as in the preview, put `aria-hidden="true"` on `.hao-card__seal`; the date stays in `.hao-card__meta` as usual.
- The wave pattern (`hao-card--wave`) and the stitching (`hao-card--stitched`) are drawn by pseudo-elements; screen readers never see them, and you write nothing for them.
