Templates for posters, social images, and slide covers. One container, three ratios.

`.hao-poster` is the image itself, 2:3 by default (poster); `hao-poster--square` is 1:1 (square social image) and `hao-poster--wide` is 16:9 (slides, web header images); `hao-poster--tint` swaps in an azurite background. The parts inside: `.hao-poster__title` (the large title; add `--v` for vertical setting), `.hao-poster__sub`, `.hao-poster__meta`, `.hao-poster__foot` (the bottom line, information on the left and the seal on the right), and `.hao-poster__moon` (a moon on the azurite background). Set the image width with the inline `--w`; every type size, margin, and seal inside scales with it.

Five templates:

| Template | Image | For |
| --- | --- | --- |
| Event | Moon-white background, vertical large title on the right, information at lower left, a band of wave pattern along the bottom | Events, launches, exhibitions |
| Solar term | Full azurite background, a moon above, the solar term’s name below | Solar terms, holidays, an image a day |
| Poem | Moon-white background, a fret along the top, the poem set vertically in the middle | Poems, dedications, a line a week |
| Quote (square) | Moon-white background, one sentence, gold-ink corner marks | Quote images for social platforms |
| Cover (wide) | Moon-white background, a line of large title at lower left, the mark at lower right | Slide covers, article header images |

The rules are the same as for interfaces, only stricter:

- **It doesn’t follow the theme.** A poster is print material and uses the day colors in both themes: put `data-theme="light"` on `.hao-poster`. Without it, the azurite ground turns pale at night and the moon becomes a black hole.
- **One scene per piece, one seal per piece.** Each image carries one pattern or one moon, and one touch of cinnabar (a seal, or a cinnabar-colored mark). On an azurite background, the mark and the seal go monochrome.
- **Keep more than half empty.** At least half the image stays empty. When the text is short, don’t enlarge it to fill the space.
- **Leave one-twelfth of the image width on all four sides**, and align all content to this edge.
- **Set titles in the Song typeface**, one large title per image. Chinese can be set vertically, on the right; English runs horizontal, in Newsreader.
- **Set information in small sans-serif type**, at lower left; the seal goes at lower right.
- The mark is only for images introducing this system itself; other images put the product’s own seal at lower right.

For the color values, fonts, and bleed used in print, see “Print and graphics” in the guide.

**Accessibility**

- Hide the patterns from screen readers: give `.hao-wave` and `.hao-fret` `role="presentation"` as in the preview.
- Everything the image says is in real text: the title, the description, and the signature are `<h2>`s and `<p>`s, so a screen reader gets the whole poster.
- The graphics in the seal and the mark take `aria-hidden="true"` as in the preview; the text in `.hao-poster__foot` says who stands at the lower right.
