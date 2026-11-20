Three entrance motions for overlays, one for each kind of overlay. Tap “Replay” to watch them again.

| Class | Name | Look | For |
| --- | --- | --- | --- |
| `hao-sheet--enter` | Unrolling | Spreads upward from the bottom edge, like a scroll opening from below; the content inside fades in a moment later | Sheets |
| `hao-dialog--enter` | Settling | Fades in place, scaling up from 96% to full | Dialogs |
| `hao-menu--enter` | Blind | Like a bamboo blind let down: it opens from the edge that touches the button, and the items fade in a moment later. When the menu flips above its button, add `hao-menu--up` and it rolls upward | Menus |
| `hao-lamp--lit` | Lighting | The lamp body lights and the whole lamp sways twice before it rests | The bookmark, at the moment of saving |
| `hao-toast--enter` | Rising | Floats up from 12px below and fades in | Toasts, bubble tips |
| `hao-scrim--enter` | Fade in | The scrim fades in | The scrim behind sheets and dialogs |

- Unrolling is this system’s own entrance: a sheet doesn’t slide up as one block; it spreads upward where it is. It runs 320ms, fast at the start and easing to a stop.
- The entrance adds these classes to the overlay; the exit plays in reverse, at two-thirds of the duration.
- Only one overlay moves at a time. The scrim and the overlay start together.
- The stamp is another motion, reserved for the moment of completion; see `Stamp`.
- When Reduce Motion is on, all entrances are dropped and overlays simply appear.
- Don’t add entrance motion to ordinary page content: cards, lists, and headings are just there.
- Like the stamp, the lighting plays once, at the moment the person acts; a lamp already lit when the page opens stays still.

**Accessibility**

- The entrance motion carries no information: an overlay’s appearing and disappearing are decided by the `hidden` attribute, and with the motion off, the content still lands in place.
- Reduce Motion is handled once, in the stylesheet; you don’t need to check it again in your own code.
- A toast must announce itself: in the preview it carries `role="status"`; with the behavior script loaded, a real toast goes into an `aria-live` polite region and doesn’t steal focus.
