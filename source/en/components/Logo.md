The mark of the Hairline system itself: a cinnabar seal whose face holds a moon and a water line, with the wordmark beside it.

Inside `<span class="hao-logo">` go the seal’s SVG and the word Hairline. Sizes are `hao-logo--sm`, the default, and `hao-logo--lg`; `hao-logo--stack` stacks the two vertically; `hao-logo--ink` is the monochrome version, colored like the text around it.

**What it is**

- The seal is how this system signs its work; the moon is its most-used motif (the moon gate, the moon phases, the moon in the water). The mark fuses the two into one sign: looking out through the seal face, you see a moon over the water.
- The seal face takes the shape of seals in this system: the four corners slightly unequal. The moon and the water line are cut out, letting the background show through.
- The wordmark is Newsreader, weight 500, with slightly tightened letter spacing.

**When to use it**

- Use it only when referring to this system itself: the documentation cover, beside the line “Built on the Hairline design system” on the About page, and posters and slides introducing the system.
- A product built with this system doesn’t use this mark. A product’s mark is its own seal (see `Seal`).

**How to use it**

- Prefer the horizontal version. Use the stacked version where space is nearly square. In very small spots (under 20px tall), use the seal alone, without the word.
- Leave at least half a seal-face width of empty space on all sides, with nothing else inside it.
- The seal’s minimum size is 16px. Any smaller, and the moon and the water line blur.
- A cinnabar mark is the only cinnabar on that screen: no seals, red badges, or delete buttons alongside it.
- On a colored background, or in one-color printing, use the monochrome version, colored like the surrounding text.
- In the night theme, the seal switches to a lighter cinnabar on its own.

**Don’t do this**

- Don’t change the colors (except in the monochrome version), and don’t add shadows, gradients, or outlines.
- Don’t stretch or rotate it, and don’t take the seal and the word apart and rearrange them.
- Don’t swap the moon for another shape, and don’t put text inside the seal face.
- Don’t use it as an app-icon base, and don’t tile it as a decorative pattern.
- Don’t set the wordmark in another typeface, and don’t change its capitalization.

The Logos group under resources has three SVG files (cinnabar, night-theme cinnabar, and blue-black monochrome) for mockups and print.

**Accessibility**

- The mark is one whole: as in the preview, write `role="img"` and `aria-label` on `.hao-logo`, and `aria-hidden="true"` on the SVG inside, so a screen reader says the name once instead of reading seal and word separately.
- The seal-only version, without the wordmark, still takes `aria-label`; otherwise a screen reader can’t tell what the seal is.
- The wordmark is an English word: as in the preview, write `lang="en"` on the mark, so a screen reader switches to an English voice for it.
- When the mark is a link (written as `<a class="hao-logo">`), keyboard focus draws a `focus`-colored ring, the same as anything else tappable.
