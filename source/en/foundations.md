# Web and large screens

This system grew out of the phone, but it doesn’t end there. As the screen widens, the principles hold: leave room first, one thing per screen, azurite does the work. What changes is the layout, where navigation sits, and the mouse that comes along.

## Three window sizes

| Size | Width | Grid | Margins | Top-level navigation |
| --- | --- | --- | --- | --- |
| Narrow | Under 600px | 4 columns, 16px gutters | `margin-compact` | `TabBar` at the bottom |
| Medium | 600 to 839px | 8 columns, `gutter` spacing | `margin-medium` | `TabBar` at the bottom or top navigation |
| Wide | 840px and up | 12 columns, `gutter` spacing | `margin-expanded` | Top navigation |

- Use `.hao-page` as the page container and `.hao-grid` as the grid; the column count follows the window on its own. The content area stops widening at `content-max`.
- Design the narrow screen first, then add width; never squeeze a wide page down into a narrow one.
- Long-form body text never exceeds `measure` in line length, however wide the screen.
- The same content changes shape, not substance: a narrow screen’s `ListGroup` becomes a `Table` on a wide screen, its `Sheet` becomes a centered `Dialog`, and a full-page detail view becomes a column on the right.

## Mouse and keyboard

- Hover only hints “this is tappable”; it carries no information: filled buttons switch to `tint-hover` or `seal-hover`, rows and menu items to `surface-hover`. Hover styles appear only on devices with a mouse.
- Never hide content behind hover. There is no hover on touch screens, so anything that appears only on hover needs another way in.
- Everything tappable is reachable with Tab, with a focus ring in `focus`, 2px solid. Order follows visual order.
- Tappable targets on touch screens are at least 44px; dense mouse-only areas (small buttons inside table rows) may relax to 32px.

## States

Think through these states for every control; leave any of them out and the control isn’t finished:

| State | Appearance |
| --- | --- |
| Default | The token’s own color |
| Hover | `tint-hover`, `seal-hover`, `surface-hover` |
| Pressed | Buttons scale to 97% at opacity `opacity-pressed`; other small controls only drop in opacity; full rows (list rows, menu items, sidebar items, accordion headers) switch to a `surface-sunken` ground |
| Focused | 2px solid line in `focus`, offset 2px out; controls that sit against a container edge (list rows, menu items, tabs) draw it 2px inside so it isn’t clipped |
| Selected | A `tint` fill, or `ink` bold with a stroke of `tint` |
| Read-only | Text fields lose their fill and the border drops back to `hairline`; the text stays `ink`, and the field still takes focus and selection |
| Disabled | Buttons and text fields switch to a `surface-sunken` ground with `ink-tertiary` text; checkboxes, switches, segmented controls, sliders, chips, steppers, and pagination go entirely `opacity-disabled`, and the text beside them becomes `ink-tertiary`. The cursor signals not-allowed everywhere, and the reason is stated beside it |
| Error | A 2px `seal` outline plus one line of explanation |
| Loading | Nothing under a second; after that, one of the kinds in `Progress` |

## Motion

Motion only answers actions, showing “where this came from and where it goes”; it is never decoration.

| Name | Duration | Where |
| --- | --- | --- |
| `dur-fast` | 120ms | Presses, hover, checking |
| `dur-base` | 200ms | Switches, the segmented slider, tab changes |
| `dur-slow` | 320ms | Dialogs, sheets, page transitions |

- Entrances use `ease-out` (fast start, slow settle); movement uses `ease-in-out`. Exits run one-third faster than entrances.
- An overlay arrives from where it will settle: the sheet enters by “unrolling”, opening bottom to top; the dialog fades in place while scaling from 96%; the toast floats up from below. For the classes and demos, see `Motion`.
- Finishing an important task gets a “stamp”: a seal reading “done” (讫) drops, pauses, and sets. It is the one motion in the system with ceremony to it; see `Stamp`.
- No looping animations, no scroll-triggered fades section by section. The only thing that keeps moving is the spinner.
- With Reduce Motion on, movement and scaling both become fades.

## Layering

From low to high: page content; `z-nav` (sticky nav and tab bars); `z-sheet` (scrim and sheets); `z-dialog` (dialogs); `z-popover` (menus and tooltips); `z-toast` (toasts). Don’t invent numbers of your own.
