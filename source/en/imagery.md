# Imagery and assets

When you need a new graphic, or a picture, look into Chinese things first. This is a direction, not a list: the system doesn’t say which few things you may use, only which way to look, how to draw, and how to choose.

Once you’ve found something, run it through the five standards from “Aesthetic standards and sources”: plain (素), empty (空), pale (淡), fine (细), off-center (偏). Use it only if it meets all five; it doesn’t matter which dynasty it comes from.

The direction is open; the quantity is held back. The three rules still govern: one touch of cinnabar, one scene per screen, and no scenes on task screens.

## Where to look first

Decide what you want to say first, then find a thing that already says it.

| What you want to say | What you can draw on |
| --- | --- |
| Writing, creating, editing | The scholar’s study: brush, ink stick, paper, inkstone, paperweight, seal |
| Time, schedules, reminders | Solar terms, moon phases, a sundial, a water clock |
| Entrances, navigation, space | Moon gate, lattice window, pavilion, bridge, covered walkway |
| Collecting, sorting, archiving | Cases, slipcases, bookmarks, scrolls |
| Completion, confirmation, signature | Seal, knot |
| Waiting, empty states, nature | Mountain, water, boat, moon, bamboo, plum, pine |
| Ornament, dividers, backgrounds | Fret, wave pattern, stitch, ice crackle |

Things not in the table can still be used. Before taking up a thing, check whether the system already has it: the moon, the boat, the mountain, the pavilion, the lantern, the seal, and the three patterns are already drawn.

## How to draw graphics for interfaces

Icons, empty-state vignettes, and background line drawings all follow these rules.

- **Take the shape, not the texture.** Draw the outline and the structure, not ink washes, dry-brush streaks, or an aged finish. A brush becomes three sections of line—handle, socket, hair—not one streak of ink.
- **Fine lines, flat fills.** Line weight is 1.5px, with round caps and joins. Leave a small gap in every closed outline (a breathing gap).
- **Color comes only from tokens.** Use `tint` or `ink` for the subject, `pattern` for what recedes into the background, `gold` for the line that marks the point, and `tint-wash` for a faint fill. Red stays with the seal.
- **One graphic, one meaning.** Don’t stack several things into one. If it’s still recognizable at 24px, it’s drawn right.
- **It has to hold up in both themes.** When a drawing is done, look at it once under the day theme and once under the night theme.

The brush on the docs site’s opening screen came about this way: the system is named Hairline (毫)—the hair at a brush tip—so the brush was taken; the drawing is fine line, the hair in `gold`, the handle receding to `pattern`.

## How to choose assets

Photos, illustrations, textures—things you don’t draw yourself—are chosen by these rules.

- **Subject.** Objects, gardens, landscapes, handicrafts, and close-ups of materials: paper, ink, cloth, wood, porcelain.
- **Color.** Stay near the system’s colors: moon white, porcelain white, azurite, ink, plus a touch of cinnabar. Avoid large areas of pure red and bright gold.
- **Composition.** Plenty of white space, a small subject, or a subject set off to one side. One subject per image.
- **Where they go.** Ink paintings, rubbings, and details of old paintings may be used, but only in content areas: article figures, posters, covers, and mounting (`Mount`). Don’t use them as interface backgrounds, and don’t set text on top.
- **Rights.** Check before you use. Most old paintings are past their copyright term, but photos of them taken by the holding institutions may carry their own terms.

A few things to avoid:

- Dragon, phoenix, and auspicious clouds piled together, or festival kits such as lanterns and Chinese knots—unless the content is itself about a festival. A single cloud in a thin line, or one lamp with no red in it, may be used as a control’s own shape (the cloud in the search field, the lamp of the bookmark), under “shape follows the control”.
- Distressed filters that fake age, and yellowed paper-texture overlays.
- Miswritten Chinese characters and shapeless calligraphy in generated images.
- Symbols that only “look East Asian”: English lettering in chopstick fonts, conical hats, folding-fan silhouettes.

For comparison, look at the Song dynasty works listed in “Aesthetic standards and sources”: monochrome-glazed porcelain, landscapes that leave room, and the page layout of Song editions.

## When unsure, ask three questions

1. Does it have something to do with the content here, or is it only there to “look Chinese”? If not, swap in something else, or use nothing.
2. Does the page still stand up without it? If so, it’s a scene, and a screen can hold only one.
3. Does it still stand up when shrunk, moved to the night theme, or placed in an English interface?
