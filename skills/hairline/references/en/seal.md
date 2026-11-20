# Seal design

The seal is this system’s signature. The `Seal` component ships with a placeholder set in a Song typeface—serviceable, but not a real seal. For a proper one, you need separate “seal artwork”: a vector drawing with the characters already drawn in seal script, placed into `Seal` to replace the placeholder.

This system **ships no seal script glyphs**. Seal script forms differ greatly from today’s writing—one wrong stroke and the character is wrong—and most glyphs are copyrighted. So this page covers only the rules and the dimensions; the characters are yours to prepare. See `SealGuide` for diagrams; blank seal faces are in the Seals group under resources.

## Settle four things first

| What to settle | Options | How to choose |
| --- | --- | --- |
| Seal text | One character, two, or four | A surname, a given name, or a product name. One product uses one seal text |
| Carving | Intaglio seal (白文; white characters on a red ground) or relief seal (朱文; red characters with a border) | Intaglio where the brand shows in the open; relief at the signature. You can make one of each, with the same seal text |
| Script | Small seal script, or the squared script of Han seals (缪篆) | Intaglio suits the squared style—level horizontals and upright verticals fill the seal face easily; relief suits the rounder small seal script |
| Seal face | Square, or a tall rectangle (two characters stacked) | Square for one or four characters; a tall rectangle for two, its width six-tenths of its height |

## Where the glyphs come from

- **Take the Shuowen Jiezi (说文解字) as the authority.** Look up each character’s small seal form first; don’t improvise a “seal script” version from the shape of the modern character—what you get that way is usually a wrong character. A simplified character must first be traced to the traditional or original character it maps to: for done (讫), look up its traditional form (訖).
- **You can use a typeface, but read the license closely.** One checkable source is the Chongxi seal script typeface (崇羲篆体) published by Xiaoxuetang (小学堂), the Chinese paleography service of Academia Sinica in Taiwan; it covers the Shuowen Jiezi and the common characters, over eleven thousand in all, at `xiaoxue.iis.sinica.edu.tw/chongxi`. Its license is “Attribution-NoDerivs 3.0 Taiwan” or later: you may use it, commercially included, but you must name the original author and **must not alter the glyphs**. In practice that means setting the type as is—no bolding, no redrawing of strokes. Read the license page yourself before you use it; the terms there govern.
- **Having someone write or carve it is the safest.** A person who knows seal carving will handle the composition (how the characters sit on the seal face) as a matter of course—something a typeface can’t do.
- **Don’t** turn the fonts bundled with Apple’s or Microsoft’s systems into graphics; those licenses don’t allow it.
- Wherever the characters come from, have someone who reads seal script look them over before you finalize.

## Dimensions

The canvas is 48×48 units; the seal face takes the middle 40×40, from (4, 4) to (44, 44). The corner radii are 5 at the upper left, 3 at the upper right, 6 at the lower right, and 4 at the lower left, matching `Seal` in the system.

| | Intaglio | Relief |
| --- | --- | --- |
| Seal face | Solid cinnabar | Border only |
| Border | None | 1.8 wide, 3 at the bottom edge |
| Character area | 34×34, with 3 of red left on all sides | 30×29.5, 3 from the border |
| Stroke weight | One-eighth to one-ninth of the side of the character area | About the same as the border, 1.4 to 1.8 |
| Space between strokes | As wide as the strokes, or slightly less | Two to three times the stroke width |

- **Intaglio should look “full”.** The characters fill the character area, the strokes run thick, and the red left over and the white of the strokes each take about half. The principle is “treat the white as black”: the empty parts need as much tending as the solid ones.
- **Relief should look “open”.** The strokes are thin, and space is left between the characters and the border. An occasional stroke may reach out and touch the border—borrowing the border (借边)—at most one or two places in a seal.
- **Seals with more characters**: leave 1.6 units between characters. A four-character seal is two rows by two columns, read vertically starting at the upper right (upper right, lower right, upper left, lower left); a two-character seal is set vertically, one character above the other. A character with few strokes can take a smaller spot and give the room to one with many.
- **Tall rectangular seals**: seal face 24×40; every other rule is the same.

## How to build the file

- Vector artwork, SVG, canvas `viewBox="0 0 48 48"`; for a tall rectangular seal, `0 0 32 48`.
- Intaglio: one path, the seal face as the outer contour and the characters as holes cut out of it, with `fill-rule="evenodd"`. Relief: one path for the border, one for the characters.
- One color only. Use `#b83224` on a light ground, and prepare a second copy in `#ff8a75` for a dark one. No gradients, shadows, textures, or distressed edges.
- Convert the characters to outlines; leave no live text.
- At 16px it should still read as a seal; at 40px the strokes should be clear. Strokes that run too thin break at small sizes—test relief seals in particular.

## Putting it into the system

```html
<span class="hao-seal hao-seal--art" role="img" aria-label="Lin’s seal">
  <img src="your-seal.svg" alt="">
</span>
```

- The size classes work as they are: `hao-seal--sm`, the default, `hao-seal--lg`, `hao-seal--xl`.
- To let the color follow the day and night themes, write the SVG into the page itself and color the paths with `var(--seal)` instead of using `<img>`.
- The stamp animation works the same way: add `hao-seal--stamp`.
- In `aria-label`, write the product’s or person’s name plus “seal”, not the pronunciation of the seal text.

## Check before you finish

- Every character checked against the Shuowen Jiezi, or reviewed by someone who reads seal script.
- The source and license of the glyphs written down clearly, with credit given where it’s due.
- Intaglio and relief each looked over at 24px, 40px, and 64px.
- Each looked over once on a light ground and once on a dark one.
- The four corners of the seal face and the weight of the border match this spec.
- The same seal text used everywhere in the product.

## About “done” (讫)

The done (讫) character in the `Stamp` component is also a placeholder in a Song typeface. It belongs to the system, not to any product’s signature, so no artwork for it ships with the system. To make the stamp feel more real, make a relief seal of the traditional form 訖 by the rules above and swap it in.
