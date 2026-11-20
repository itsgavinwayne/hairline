# Logo

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

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end">
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Horizontal, preferred</p></div>
  <div><span class="hao-logo " role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Default</p></div>
  <div><span class="hao-logo hao-logo--sm" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Smallest</p></div>
</div>
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end;margin-top:var(--hao-space-8)">
  <div style="text-align:center"><span class="hao-logo hao-logo--stack" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Stacked, for square spaces</p></div>
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" style=""><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg></span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Mark only</p></div>
  <div><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">One color</p></div>
  <div style="padding:var(--hao-space-4) var(--hao-space-5);border-radius:var(--hao-radius-md);background:var(--hao-tint)"><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en" style="color:var(--hao-on-tint)"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end">
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">横排，首选</p></div>
  <div><span class="hao-logo " role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">标准</p></div>
  <div><span class="hao-logo hao-logo--sm" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">最小</p></div>
</div>
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end;margin-top:var(--hao-space-8)">
  <div style="text-align:center"><span class="hao-logo hao-logo--stack" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">竖排，用于方形空间</p></div>
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" style=""><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg></span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">只用印</p></div>
  <div><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">单色</p></div>
  <div style="padding:var(--hao-space-4) var(--hao-space-5);border-radius:var(--hao-radius-md);background:var(--hao-tint)"><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en" style="color:var(--hao-on-tint)"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div>
</div>
```
