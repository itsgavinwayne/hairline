# Tokens

Every token is a CSS variable, written `var(--hao-name)`. Colors have a light and a dark value and follow `data-theme` or the system setting. Do not hard-code values; pick the closest token.

## Color

| Variable | Light | Dark | Use |
| --- | --- | --- | --- |
| `--hao-bg` | `#f2f4f7` | `#0e1218` | Moon white. The page background, equivalent to the iOS grouped background; all cards and lists float on it. |
| `--hao-surface` | `#ffffff` | `#181d26` | Porcelain white. The surface for cards, list groups, and sheets, set on top of bg. |
| `--hao-surface-sunken` | `#e8ebf0` | `#222834` | Cloud gray. Recessed areas such as input fills and segmented control tracks. |
| `--hao-surface-hover` | `#f5f7fa` | `#1e2430` | The fill for rows and menu items when hovering over surface. Appears only on devices with a mouse. |
| `--hao-surface-raised` | `#ffffff` | `#303847` | Small raised pieces: the selected block of a segmented control, a stepper button on hover. By day it matches surface and lifts by its shadow; at night the shadow can’t be seen, so it sits one step lighter than surface-sunken. |
| `--hao-ink` | `#161b24` | `#eef1f6` | Blue-black. Titles and body text; usable on bg, surface, and surface-sunken. |
| `--hao-ink-secondary` | `#4a5263` | `#a9b1c0` | Slate. Secondary text and values on the right side of list rows; usable on bg, surface, and surface-sunken. |
| `--hao-ink-tertiary` | `#5f6778` | `#8892a3` | Smoke gray. Placeholders, footnotes, and timestamps; usable on bg, surface, and surface-sunken. |
| `--hao-hairline` | `#d5dae2` | `#2e3542` | Plain rule. The divider between list rows; decorative only and carries no meaning. |
| `--hao-border-control` | `#7e8696` | `#6c7687` | Control borders and the off-state track of switches; at least 3:1 on bg, surface, and surface-sunken. |
| `--hao-tint` | `#1f4fa8` | `#8fb4ff` | Azurite. The only interaction color in the system: primary buttons, links, selected states, and switches in the on state. When used as text, usable on bg, surface, and tint-wash. |
| `--hao-tint-hover` | `#1a4391` | `#a8c5ff` | The fill of tint-filled buttons on hover; on-tint still sits on top. |
| `--hao-on-tint` | `#ffffff` | `#0e1218` | Text and icons on a tint fill. |
| `--hao-tint-wash` | `#e3ebfa` | `#1c2a47` | Azurite wash. The background for secondary buttons, selected rows, and info messages, with tint or ink text on top. |
| `--hao-seal` | `#b83224` | `#ff8a75` | Cinnabar, for text and lines: error text and borders, delete items in a menu, the frame and characters of a relief seal. Use only one per screen; usable on bg, surface, and seal-wash. Large fills use seal-fill. |
| `--hao-seal-fill` | `#b83224` | `#c8402e` | Cinnabar as a fill: the face of an intaglio seal, numbered badges, delete buttons, the logo. By day it matches seal; at night seal is lightened to work as text and would look bright and pink over a large area, so fills use a deeper cinnabar. |
| `--hao-seal-hover` | `#9c2a1e` | `#b83224` | The fill of seal-fill buttons on hover; on-seal still sits on top. |
| `--hao-on-seal` | `#ffffff` | `#ffffff` | Text and icons on a seal-fill ground. White in both themes, so an intaglio seal stays white on cinnabar. |
| `--hao-seal-wash` | `#fbe9e6` | `#40201b` | Cinnabar wash. The background for error messages, with seal or ink text on top. |
| `--hao-jade` | `#24705a` | `#7fd1b0` | Bamboo green. Success and completion; always paired with a word or icon, never distinguished by color alone. When used as text, usable on bg, surface, and jade-wash. |
| `--hao-on-jade` | `#ffffff` | `#0e1218` | Text and icons on a jade fill. |
| `--hao-jade-wash` | `#e2f2ec` | `#16332a` | Bamboo green wash. The background for success messages. |
| `--hao-amber` | `#f2b632` | `#f5c451` | Gamboge. The fill color for warnings; use only as a fill, not as text on light backgrounds. |
| `--hao-on-amber` | `#2a1d00` | `#2a1d00` | Text and icons on an amber fill. |
| `--hao-amber-ink` | `#8a5a00` | `#f5c451` | Warning text and icons; usable on bg, surface, and amber-wash. |
| `--hao-amber-wash` | `#fbf1d9` | `#3a2e10` | Gamboge wash. The background for warning messages. |
| `--hao-gold` | `#836427` | `#d9b36a` | Gold ink. Gold-line accents such as stitches, fret patterns, and title slip borders; also usable for signatures and small text for solar terms, on bg, surface, and surface-sunken. Not for buttons or status. |
| `--hao-pattern` | `#cfdaf0` | `#2a3754` | Pattern color. Large-area background patterns such as the wave pattern, drawn on surface or bg; purely decorative, with no text on top. |
| `--hao-focus` | `{tint}` | `{tint}` | Keyboard focus ring: 2px solid, offset 2px, at least 3:1 on all surfaces. |
| `--hao-material` | `rgba(255, 255, 255, 0.72)` | `rgba(24, 29, 38, 0.72)` | Frosted glass material. The base of navigation bars and tab bars, with a 20px background blur. |
| `--hao-scrim` | `rgba(14, 18, 24, 0.45)` | `rgba(0, 0, 0, 0.6)` | The scrim behind overlays. |

## Spacing

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-space-1` | `4px` | The minimum gap between an icon and text. |
| `--hao-space-2` | `8px` | Tag padding and the gap between controls in the same group. |
| `--hao-space-3` | `12px` | Vertical padding in list rows. |
| `--hao-space-4` | `16px` | Page left and right margins and left and right padding in list rows. |
| `--hao-space-5` | `20px` | Card padding and left and right button padding. |
| `--hao-space-6` | `24px` | The distance between adjacent groups. |
| `--hao-space-8` | `32px` | White space between a large title and content. |
| `--hao-space-12` | `48px` | White space between page sections, also the module for covers. |

## Radius

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-radius-xs` | `6px` | Checkboxes and very small marks. |
| `--hao-radius-sm` | `8px` | Small icons, thumbnails, and the corner radius of focus rings. Seals do not use it; the seal face has its own cut corners. |
| `--hao-radius-md` | `12px` | Buttons, input fields, and segmented controls. |
| `--hao-radius-lg` | `20px` | Cards, list groups, and message bars. |
| `--hao-radius-xl` | `28px` | Bottom sheets and full-screen containers. |
| `--hao-radius-full` | `999px` | Tags, switches, and small pill buttons; perfect circles such as moon gates. |

## Shadow

| Variable | Light | Dark | Use |
| --- | --- | --- | --- |
| `--hao-shadow-card` | `0 1px 2px rgba(22, 27, 36, 0.05), 0 8px 24px rgba(22, 27, 36, 0.06)` | `0 0 0 1px rgba(255, 255, 255, 0.06), 0 1px 2px rgba(0, 0, 0, 0.4), 0 8px 24px rgba(0, 0, 0, 0.3)` | Cards. Very light, like paper floating on a desk. At night a black shadow can’t be seen on a dark ground, so it adds a very faint light edge. |
| `--hao-shadow-float` | `0 2px 6px rgba(22, 27, 36, 0.08), 0 16px 40px rgba(22, 27, 36, 0.14)` | `0 0 0 1px rgba(255, 255, 255, 0.1), 0 2px 6px rgba(0, 0, 0, 0.5), 0 16px 40px rgba(0, 0, 0, 0.5)` | Overlays and raised menus. At night it adds the same light edge, so overlays have a boundary. |
| `--hao-shadow-thumb` | `0 1px 3px rgba(22, 27, 36, 0.2)` | `0 1px 3px rgba(0, 0, 0, 0.5)` | Switch thumbs and the selected block of segmented controls. |

## Breakpoints

Window width has three levels. Variables cannot be used in media queries; copy the values here when writing numeric values.

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-bp-medium` | `600px` | From here up is medium: tablets and narrow browser windows. The grid has 8 columns. |
| `--hao-bp-expanded` | `840px` | From here up is expanded: desktop browsers. The grid has 12 columns, and the tab bar switches to top navigation or a sidebar. |
| `--hao-bp-wide` | `1200px` | The content area no longer grows wider; the white space on both sides increases. |

## Layout

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-margin-compact` | `16px` | Page left and right margins for narrow screens (under 600px), with a 4-column grid. |
| `--hao-margin-medium` | `24px` | Page left and right margins for medium screens, with an 8-column grid. |
| `--hao-margin-expanded` | `32px` | Page left and right margins for wide screens, with a 12-column grid. |
| `--hao-gutter` | `24px` | Grid column gap; narrow screens use 16px (space-4). |
| `--hao-content-max` | `1200px` | The maximum width of the content area; beyond it, content is centered. |
| `--hao-measure` | `680px` | The maximum line width for long-form body text, about 38 Chinese characters or 70 English characters. |

## Layers

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-z-nav` | `100` | Sticky navigation bars and fixed bottom tab bars. |
| `--hao-z-sheet` | `200` | Scrims and bottom sheets. |
| `--hao-z-dialog` | `300` | Dialogs. |
| `--hao-z-popover` | `350` | Menus and popovers. Higher than dialogs, so they remain visible when opened inside a dialog. |
| `--hao-z-toast` | `400` | Toasts; always on top. |

## Opacity

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-opacity-disabled` | `0.4` | Disabled controls drop to this opacity as a whole. |
| `--hao-opacity-pressed` | `0.85` | The moment of pressing. |

## Motion

Motion only responds to actions. Exit is one third faster than enter; when the system turns on Reduce Motion, turn it all off.

| Variable | Value | Use |
| --- | --- | --- |
| `--hao-dur-fast` | `120ms` | Press, hover, and check. |
| `--hao-dur-base` | `200ms` | Switches, segmented sliders, and tab changes. |
| `--hao-dur-slow` | `320ms` | Dialogs, bottom sheets, and page transitions. |
| `--hao-ease-out` | `cubic-bezier(.2, .8, .2, 1)` | Enter: fast start, slow stop. |
| `--hao-ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Position movement. |

## Type

Type styles are classes, written `class="hao-name"`. Names ending in `-en` are the levels for English interfaces; under `<html lang="en">` headings switch to the English sizes and tracking on their own.

| Family | Variable | Value |  |
| --- | --- | --- | --- |
| serif | `--hao-font-serif` | `"Newsreader", "Noto Serif SC", "Songti SC", "STSong", "Source Han Serif SC", Georgia, serif` | |
| sans | `--hao-font-sans` | `-apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", "Noto Sans SC", "Source Han Sans SC", "Helvetica Neue", "Microsoft YaHei", sans-serif` | |

| Class | Size / line height | Weight | Family | Use |
| --- | --- | --- | --- | --- |
| `hao-display` | 44px / 52px | 700 | serif | Covers and launch screens; at most one per screen. The only style that grows with the window: 56/64 on medium, 64/72 on wide. |
| `hao-title-1` | 32px / 40px | 700 | serif | Page large title, corresponding to the iOS Large Title. Also the title of a long text. |
| `hao-title-2` | 24px / 32px | 600 | serif | Card titles, section titles, and dialog titles. |
| `hao-title-3` | 20px / 28px | 600 | serif | Small titles: the third heading level in long text, and the title of each item in a set. Below this size, switch from the Song typeface to headline. |
| `hao-display-en` | 48px / 52px | 500 | serif | Covers and launch screens for English interfaces, corresponding to display. At most one per screen. 60/64 on medium, 68/72 on wide. |
| `hao-title-1-en` | 34px / 40px | 600 | serif | The page large title for English interfaces, corresponding to title-1. |
| `hao-title-2-en` | 24px / 28px | 600 | serif | Card titles and section titles for English interfaces, corresponding to title-2. |
| `hao-title-3-en` | 20px / 24px | 600 | serif | Small titles for English interfaces, corresponding to title-3. |
| `hao-colophon` | 15px / 24px | 400 | serif | English signatures and colophons, italic, replacing the vertical title slip. Use only for signatures, not for emphasis in body text. |
| `hao-headline` | 17px / 24px | 600 | sans | Text to emphasize in buttons, navigation bar titles, and list rows. |
| `hao-body` | 17px / 28px | 400 | sans | Body text and list row titles. |
| `hao-body-en` | 17px / 24px | 400 | sans | English body text, with 4px less line height than the Chinese body. The other sans-serif styles are shared between Chinese and English. |
| `hao-callout` | 15px / 24px | 400 | sans | Supporting text, form labels, and segmented controls. |
| `hao-footnote` | 13px / 20px | 400 | sans | Footer notes for list groups and timestamps. |
| `hao-caption` | 12px / 16px | 500 | sans | Tags, tab bar text, and badges. Single lines only. |
