This system’s own cover, at the very front of the guide—not a reusable component.

The left side carries the system’s name and a one-line positioning statement; the right side, a moon gate: a full moon cut out of a block of azurite, and beside it a second disc split in two by blue-black and a wash, like the moon and its reflection. At the lower left sits the system’s mark, the only cinnabar in the whole image.

- The image is laid out on a 48px (`space-12`) module, and every color block’s edges land on the grid.
- A product built on this system doesn’t carry the cover over; it builds its own following “Print and graphics”, with its own seal.
- The cover doesn’t follow the theme; it uses the day colors in both themes (the outer element carries `data-theme="light"`).

**Accessibility**

- The graphic on the right is decoration, and its SVG carries `aria-hidden="true"`; the name and the positioning statement are real text, and a screen reader reads them.
