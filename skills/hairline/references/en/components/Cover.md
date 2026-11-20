# Cover

This system’s own cover, at the very front of the guide—not a reusable component.

The left side carries the system’s name and a one-line positioning statement; the right side, a moon gate: a full moon cut out of a block of azurite, and beside it a second disc split in two by blue-black and a wash, like the moon and its reflection. At the lower left sits the system’s mark, the only cinnabar in the whole image.

- The image is laid out on a 48px (`space-12`) module, and every color block’s edges land on the grid.
- A product built on this system doesn’t carry the cover over; it builds its own following “Print and graphics”, with its own seal.
- The cover doesn’t follow the theme; it uses the day colors in both themes (the outer element carries `data-theme="light"`).

**Accessibility**

- The graphic on the right is decoration, and its SVG carries `aria-hidden="true"`; the name and the positioning statement are real text, and a screen reader reads them.

## Markup

### Chinese

```html
<div class="cover" data-theme="light">
  <div class="art">
    <!--
      blocks: tint 192×288 (space-12 × 4 wide, full height) · ink 192×144 · tint-wash 192×144 · the Hairline mark (seal with moon and waterline) 48×48 (space-12)
      arrangement: one tall 石青 slab bleeding top and bottom, two stacked satellites flush to its right, the seal alone on the ground at lower left
      pattern: literal motif — the moon gate. A full disc of ground cut from the slab, and a second disc split across the ink/wash seam (moon and its reflection); chosen because the README limits ornament to the seal and asks for white space first
      scales: module space-12 (48px); discs r = 72 (space-6 × 3); seal corner space-1, matching the cut corners of the Seal component
    -->
    <svg viewBox="0 0 480 288" aria-hidden="true">
      <rect class="tint" x="96" y="0" width="192" height="288"/>
      <rect class="deep" x="288" y="0" width="192" height="144"/>
      <rect class="wash" x="288" y="144" width="192" height="144"/>
      <circle class="ground" cx="192" cy="144" r="72"/>
      <path class="wash" d="M312 144a72 72 0 0 1 144 0z"/>
      <path class="deep" d="M312 144a72 72 0 0 0 144 0z"/>
      <path class="seal" fill-rule="evenodd" transform="translate(24 216)" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/>
    </svg>
  </div>
  <div class="text">
    <h1 class="name">Hairline</h1>
    <p class="tag">iOS 的克制，加上一点东方的气韵</p>
  </div>
</div>
```
