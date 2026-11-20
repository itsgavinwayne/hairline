# Kinds of output

Everything made with this system falls into four kinds. The four share one foundation, and the rules for each run looser or tighter. Decide which kind you have in hand before you go looking for its components and rules.

## First, tell which kind it is

Ask one question: is this thing meant to be **used**, **read**, **looked at**, or used to **sign**?

| Kind | What it is | Examples |
| --- | --- | --- |
| Interface | For use: a person gets a task done on it | An app’s screens, admin panels, forms, settings |
| Reading | For reading: a person lingers and reads to the end | Articles, poems, letters, photo essays |
| Print | For looking: no interaction, and the image has to stand on its own | Posters, social images, slides, printed pieces |
| Brand | For signing: it says whose this is | Logos, seals, title slips, signatures |

A product usually has all four. A page belongs to one kind only: an article page is reading, even with a navigation bar on it; a settings page is interface, even with a seal stamped in its lower right corner.

## The shared foundation

All four draw from here; none keeps its own set.

- Tokens: color, type, spacing and corner radius, shadow and elevation.
- The five standards: plain (素), empty (空), pale (淡), fine (细), off-center (偏). See “Aesthetic standards and sources”.
- The three rules: one touch of cinnabar, one scene per screen, shape follows the control.
- The basics: icons (`Icon`), patterns (`Stitch`, `Fret`, `Wave`, `Crackle`), motion (`Motion`).
- The way it writes copy, and the rules for English interfaces.

## The rules for each kind

| | Interface | Reading | Print | Brand |
| --- | --- | --- | --- | --- |
| Number of scenes | Task screens: zero; the home screen and empty states: at most one | One piece can hold one mounted image, one quotation, two or three fishtail marks (鱼尾), and one signature | One scene per piece | No scenes |
| Cinnabar | One touch per screen | One touch per screen | One seal per piece | The seal itself is that touch |
| White space | Separate sections with blank space | Line length no more than `measure` | At least half stays empty | A clear margin the width of the seal face on all four sides |
| Composition | Follow iOS habits; center what should be centered | One column, left-aligned | Off to one side, the large at the top or right | At the lower right, or the end of the text |
| Title type | `title-1`, `title-2` | `title-1` plus the heading levels for long text | Sized by the share of the short edge | Song typeface, with the product name set out plainly |
| Where the details live | “Web and large screens”, “Behavior and scripts” | “Reading and content” | “Print and graphics”, “Imagery and assets” | “Seal design” |

## Which components each kind uses

**Interface**

- Actions: `Button`, `Bookmark`
- Forms: `TextField`, `SearchField`, `Select`, `Checkbox`, `Radio`, `Switch`, `Segmented`, `Slider`, `Stepper`, `Chip`, `Rating`, `Calendar`, `Upload`
- Navigation: `NavBar`, `TabBar`, `Tabs`, `Sidebar`, `Breadcrumb`, `Pagination`, `Steps`, `Link`
- Content: `Card`, `ListGroup`, `Table`, `Stat`, `Timeline`, `Accordion`, `Avatar`, `DateTile`
- Feedback: `Dialog`, `Sheet`, `Toast`, `Progress`, `EmptyState`, `Stamp`
- Overlays: `Menu`, `Tooltip`
- Status: `Badge`, `Banner`, `Tag`

**Reading**

`Prose`, `Verse`, `Mount`, `Handscroll`, `Paper`, plus `Quote` and `Divider`.

**Print**

`Poster`, `Cover`.

**Brand**

`Logo`, `Seal`, `SealGuide`, `TitleSlip`.

## A few things that cross kinds

- `Seal` shows up in all four kinds, but each screen and each piece gets only one.
- `Quote` and `Divider` are ordinary content components in interfaces; only in articles do they carry the fishtail mark and the corner marks.
- In interfaces a pattern counts as a scene, bound by “one scene per screen”; in print it is that scene.

## When adding something new

First decide which kind it belongs to, then follow that kind’s rules. If it fits none of the four, it is probably another system’s business; see “What fits and what doesn’t” in “References and trade-offs”.
