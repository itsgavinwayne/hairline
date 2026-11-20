The restraint of iOS, with an East Asian sensibility: structure, density, and interaction follow iOS conventions, while the colors, the title typeface, and the white space come from azurite, the cinnabar seal, and Xuan paper. The East Asian half comes with five standards you can test against: plain (素), empty (空), pale (淡), fine (细), off-center (偏), drawn mostly from the Song dynasty; see “Aesthetic standards and sources”. The split between the two is fixed—follow the rules below.

## Anyone can use it

This system is called Hairline (毫). 毫 is the tuft at the tip of a brush, and also a measure of the very fine; a hairline is the thinnest line in an interface. It doesn’t belong to one person or one product. Take it and use it: swap in three things of your own and keep the rest as is.

- **Swap in yours:** the seal character (the character inside `Seal`), the product name, and the date line and title slip text of the signature.
- **Don’t change:** the names and roles of the color tokens, the typeface pairing, the spacing and corner-radius steps, or the three rules. Change those and it is no longer the same system.
- **Credit:** the interface never needs to show the name Hairline (毫). To give credit, one `footnote` line on the About page—“Interface built on the Hairline (毫) design system”—is enough.
- **Name and token:** the system shares its name with the divider color token `hairline`. Lowercase `hairline` always means the token; for the system itself, write 毫 or capitalized Hairline.

## Three principles

- **Leave room, then write.** One screen makes one point. When you hesitate over adding an element, don’t. Separate sections with `space-6` to `space-12` of blank space; don’t stack hierarchy with boxes and background fills.
- **Azurite does the work. Cinnabar marks the point.** `tint` is the only interactive color; anything tappable uses it. `seal` appears once per screen at most: one seal, one unread badge, or one delete button.
- **iOS sets the structure. East Asia sets the character.** Lists, navigation, switches, and touch sizes follow iOS habits; the East Asian elements land in four places only: Song typeface titles, the traditional colors, seals, and the scenes and motifs bound by the three rules. Graphics in the interface are all fine lines and flat fills—no ink-brush strokes, no cloud clip art, no distressed textures. For how to choose photos, illustrations, and other assets, see “Imagery and assets”.

## Color

- Pages sit on `bg` (moon white); content sits on `surface` (porcelain white) cards and list groups. Never stack `surface` on `surface`.
- Text comes in three steps: `ink` for titles and body, `ink-secondary` for secondary information, `ink-tertiary` for placeholders and footnotes.
- Primary buttons fill with `tint` and label in `on-tint`; secondary buttons take a `tint-wash` ground with `tint` text. In the night theme `tint` lightens and its label goes dark, so always write `on-tint`—never hard-code white.
- Status colors each carry a word or an icon, never color alone: `jade` for done, `amber-ink` (text) or `amber` (fill) for a nudge, `seal` for errors and deletion.
- `amber` is a fill only, labeled in `on-amber`; any yellow text on a light ground uses `amber-ink`.
- Cinnabar is two tokens: `seal` for text and lines, and `seal-fill` with `on-seal` for large fills (intaglio seals, badges, delete buttons, the logo). By day the two match; at night `seal` is lightened to work as text and `seal-fill` sits one step deeper, so a seal stays white on cinnabar.
- Small raised pieces, such as the selected block of a segmented control, use `surface-raised`.
- Dividers use `hairline`, for decoration only. Control outlines that must read as edges use `border-control`.

## Type

- Titles use the Song typeface (`display`, `title-1`, `title-2`, `title-3`); body text and every control use the system sans-serif (`headline` through `caption`). The Song typeface never enters buttons, input fields, or list rows.
- Sizes come in two runs. Sans-serif text follows the iOS sizes 12, 13, 15, 17, a pixel or two apart, and leans on weight and color for rank. Serif titles start at 17 and multiply by √2 per level, which doubles the area: 17, 24, 34, 48, 68; the only half step in between is 20 (`title-3`).
- Han characters fill more of their box than Latin letters: in Noto Serif SC a character stands about 93% of the font size tall, while a Newsreader capital stands only 72%, so at the same size Chinese looks a notch larger. For the three levels from 34 up, Chinese steps back to the next multiple of 4 below: 32, 44, 64; the 24 and 20 levels share one size in both languages. Digits are Latin glyphs and take the English sizes.
- Line heights are all multiples of 4, on the same grid as spacing: small text 12/16, 13/20, 15/24; body text 17/28 in Chinese and 17/24 in English; a title’s line height is its size plus 8, the same value for English and Chinese at each level, and 4 less where the two share a size.
- Page titles use `title-1`, left-aligned, with `space-8` above. `display` appears at most once per screen and is the only level that grows with the window: 44 on narrow, 56 on medium, 64 on wide. Every other level follows the column it sits in; the column doesn’t widen, so the type doesn’t grow.
- Body text uses `body` at a 28px line height. Chinese paragraphs run at most 37 characters per line. Body text is set solid, with no added tracking; Chinese titles open up slightly (0.02em from `title-1` up, 0.01em below), and English titles tighten.
- Sans-serif text uses only three weights: 400, 500, 600; the Song typeface uses 600 and 700 for Chinese, 500 and 600 for English. Rank comes from size and typeface, not from one more weight.
- Only three kinds of size sit off the scale: a single character in a box (step numbers, the page seal, avatars), sized at about half the box; the logo and the decorative quotation mark, which are graphics; and the 11px lunar dates in calendar cells, the smallest type in the system. Don’t invent sizes beyond these.
- Leave one space between Chinese and Latin text; use Western digits. Punctuation is full-width, and titles take no trailing period.
- Serif titles load two families from Google Fonts: Newsreader for Latin text (500, 600, and italic 400) and Noto Serif SC for Han characters (600, 700; 900 for intaglio seals). Offline on Apple devices they fall back to Songti SC and Georgia.
- Body text on Apple devices uses the system’s PingFang SC and San Francisco; other platforms and all printed pieces use Noto Sans SC. PingFang SC must not be used in print or on non-Apple platforms.
- English interfaces have their own set of title styles (`display-en`, `title-1-en`, `title-2-en`, `title-3-en`, `body-en`, `colophon`); see “English interfaces” for the rules.

## Size and corner radius

- Spacing follows a 4px grid: `space-1` through `space-12`. Page side margins are `space-4`; between groups, `space-6`.
- Anything tappable stands at least 44px tall. Filter chips, small buttons, and page numbers draw shorter under a mouse (32 to 36px) and stretch to 44px on touch screens.
- For breakpoints, grids, hover states, and motion on the web and large screens, see “Web and large screens”; for what this system borrows and what it leaves out, see “References and trade-offs”.
- Content meant for reading—articles, poems, images, letters—has its own layouts and components; see “Reading and content”.
- Posters, social images, slides, and printed pieces—layouts, font licenses, and print color values—are covered in “Print and graphics”.
- How dialogs, menus, and the month calendar move is covered in “Behavior and scripts”. The script is one file with no framework dependencies.
- Corner radius comes in six steps, chosen by element size: checkboxes `radius-xs`; small icons and thumbnails `radius-sm`; buttons and input fields `radius-md`; cards and list groups `radius-lg`; sheets `radius-xl`; tags and switches `radius-full`. When a small element sits inside a larger one, the inner radius steps one size below the outer.
- Shadows come in three kinds—`shadow-card`, `shadow-float`, `shadow-thumb`—all of them faint. When white space and the difference between `surface` and `bg` can carry the hierarchy, add no shadow.

## Seals

- The seal is the user’s own signature, built with the `Seal` component. You supply the seal text: a character from a family name, a given name, or the product name.
- Two cutting styles: the intaglio seal (白文)—white characters on a cinnabar ground, thick strokes filling the seal face—for brand surfaces; the relief seal (朱文)—thin border, thin strokes, bottom edge slightly heavier—for card corners and signatures.
- Three seal faces: the single-character square seal, the four-character square seal (read vertically from the top right), and the two-character rectangular seal—a leisure seal, placed at the head of a passage.
- The four corners of the seal face are slightly unequal small angles, like a stone seal cut by hand. It is the only shape in the system off the `radius` steps—don’t round it.
- Seals don’t rotate, don’t age, take no texture. One seal per screen.
- The character for “seal” (印) in the preview is only a placeholder. A product uses one seal text and keeps it; English interfaces keep the Han seal too—don’t switch to letters.
- The placeholder is set in the Song typeface, not seal script. The system ships no seal-script characters; for a true seal, prepare seal artwork as described in “Seal design”.
- The system has its own mark (a moon inside a seal; see `Logo`), used only when referring to the system itself. Products built with it don’t use this mark: a product’s mark is its own seal, and the product name is simply set in `title-1` or `display`.

## The three rules

Where traditional elements go, and how much of them, is decided by these three rules alone. When unsure, use one less.

**First, one touch of cinnabar.** Red appears once per screen: one seal, one unread badge, one delete button, or one stamp—choose one of the four.

**Second, one scene per screen.** At most one thing that counts as a scene appears per screen. Scenes come in three kinds:

- Patterns: stitch (`Stitch`), fret (`Fret`), wave pattern (`Wave`), ice crackle (`Crackle`)
- Vignettes: the moon, boat, mountain, pavilion, and lantern in empty states (`EmptyState`)
- Display pieces: mounting (`Mount`), the handscroll (`Handscroll`), a poem set vertically (`Verse`), letter paper (`Paper`)

A signature (title slip plus a small seal) is not a scene and may share a screen with one. The article page is the one exception: one piece may hold a mounting, one quotation, two or three fishtail marks (鱼尾), and one signature group; see “Reading and content”.

**Third, shape follows the control.** A control’s own shapes are exempt from the two rules above, because without them the control would not exist: the moon phase, thread, and scale of progress; the crescent and ripple of loading; the upward hook stroke of the checkbox; the underline of the tab; the 一, 二, 三 of the steps; the thick-thin rule pair (文武线) of the table header; the page-number seal and the handscroll of the pagination, the lamp of the bookmark, the single cloud in the search field, the yin and yang cuts of the quotation, the coin hole of the switch, the seal corners of the badge, the tag shape of the filter chip, the binding holes of the date tile, the roller of the sheet’s grabber; the plum-blossom rating; the family-name seal; the lunar dates and solar terms in the calendar. Keep only two limits: one progress motif per screen, and one moon per screen.

What you make falls into four kinds—interface, reading, print, brand; how tightly the rules apply to each is covered in “Kinds of output”.

One more bottom line: **task screens carry no scenes.** Settings, forms, lists, tables—the scene count is zero. Scenes are for home screens, detail-page headers, empty states, launch screens, and About pages.

Remaining details:

- Line patterns use `gold`; background patterns use `pattern`; neither uses `seal`.
- No text sits on a scene, and a scene carries no meaning; mark it `role="presentation"` or `aria-hidden="true"`.
- When you need a new graphic or asset, look to Chinese sources and follow the drawing and choosing guidance in “Imagery and assets”. No registration needed, but the three rules above still cap the count.
- The four sample screens each test one rule: `SampleSettings` and `SampleForm` are task screens, `SampleArticle` is the ceiling for an article page, and `SampleDashboard` puts several motifs on one screen.

## Materials and motion

- Navigation bars and tab bars use `material` with a 20px background blur; content scrolls beneath them. Dialogs and sheets lay `scrim` behind them. Nowhere else uses translucency.
- Motion only answers actions: a press scales to 97%, switches and the segmented slider take a 200ms ease-out. When Reduce Motion is on, all of it turns off.
- Two motions belong to the system itself: the sheet enters by “unrolling”, and finishing an important task gets a “stamp”. Every other motion tries not to be noticed.
- Keyboard focus is one shape everywhere: a 2px solid line in `focus`, offset 2px out.
- Selected text takes a `tint-wash` ground; the text cursor is `tint`; links in body text use `.hao-link` (`tint` with a thin underline). Links standing on their own line use `.hao-link--go`; next to a primary button, use a text button—see the Link component.

## Voice and tone

- Address the reader as you, never with formal honorifics. Short sentences, verb first: “Save changes”, “Delete this record”.
- Buttons say what pressing them does, and one action keeps one name start to finish: the button reads “Publish”, the toast reads “Published”.
- Errors say what went wrong and what to do next—no apology, no exclamation mark: “Can’t reach the network. Try again in a moment.”
- An empty state is an invitation: “No notes yet. Write the first one.”
- No emoji. An occasional refined word (note, desk, signature) is allowed, but don’t turn literary—at most one per screen.

## Icons

- Use the system’s own icons (see `Icon`): 39 of them, on a 24px grid, 1.5px round-cap stroke, monochrome. Written as `<i class="hao-icon hao-icon--name">`; color follows the text.
- One trait is shared across the set: every closed outline leaves a small opening, the “breathing gap”. New icons follow it too.
- Only two sizes: 24px and 20px.
- Icons never carry meaning alone; text sits beside them, or an accessibility label does.
- In native interfaces on Apple platforms, SF Symbols at the Regular weight can stand in.
