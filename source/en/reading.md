# Reading and content

Interfaces are for getting things done: fast and quiet. Content is for reading: it can be slower and more particular. The components in this section belong to the second kind, and traditional elements can appear more freely here.

## The five content components

| Component | What it is | Source |
| --- | --- | --- |
| `Prose` | Layout for long text: type area, paragraphs, signature | The type area of a thread-bound book, with a larger head than foot |
| `Verse` | A poem or short lines set vertically | Poem lines set vertically, without punctuation |
| `Mount` | A mounted image | Hanging scrolls and horizontal scrolls |
| `Handscroll` | A row of content that unrolls sideways | The frontispiece, spacer band (隔水), and tail of a handscroll |
| `Paper` | Letter paper with ruled columns, for writing or reading | The double border and ruled columns of letter paper |

Add the `Quote` (a quotation) and the `Divider` with its fishtail mark (鱼尾), both of which came earlier, and a piece has everything it needs.

## How to put a page together

- The reading page is: a navigation bar, then one `Prose`, nothing else. Sidebars, recommendations, and comments go after the article ends.
- Don’t let the “refinements” add up too much on one page. One `Prose` can hold one `Mount`, one `Quote`, two or three `Divider`s, and one signature—that’s the limit.
- `Verse`, `Mount`, `Handscroll`, and `Paper` each appear at most once per screen.
- These components don’t count as patterns, but they carry enough character already; don’t add stitches, frets, or wave patterns on the same screen.

## Horizontal and vertical

- Body text is always set horizontally. Vertical setting is only for very short texts: poems, title slips, the frontispiece of a handscroll.
- English is always set horizontally; in the corresponding places, switch to a serif typeface or italics.

## The line between interface and content

- Task screens (settings, forms, lists, tables) don’t use the components in this section.
- Content pages (articles, note details, works, letters) don’t use dense controls like tables, pagination, or filters; tuck those into a toolbar or menu.
- One product will have both kinds of pages. Tapping from a list into an article should feel like things “slow down”: margins widen, line height loosens, the title becomes large Song type. Long text takes no size of its own: it is still `body` at 17px, with line height opened from 28px to 32px (24px to 28px in English); headings come in three levels: `title-1`, `title-2`, `title-3`.
