What a region shows when it has nothing to display: a vignette inside a round window, one line on the state of things, one line on the next step.

`.hao-empty` holds, in order, a `.hao-scene`, `.hao-empty__title` (Song typeface), `.hao-empty__body`, and an optional button. You provide the words; the vignette comes from the five below.

**Five vignettes, one per situation**

| Vignette | What it shows | Use it for |
| --- | --- | --- |
| Moon | A moon hanging over the water | A first visit—nothing here yet |
| Boat | A lone boat below distant hills | A search or filter with no results |
| Mountains | Two ranges of far hills with mist between | Offline, out of reach |
| Pavilion | An empty pavilion | All done; time to rest |
| Lantern | A carried lantern | Something failed; it didn’t load |

- Each vignette is drawn inside a round window, like looking out through a moon gate. The subject is fine `tint` lines; the far scenery and the water are washes in `pattern`—two colors, no more.
- The vignette is the scene of that screen (see the three rules in the guide): no pattern or display piece elsewhere on the same screen, and no seal.
- One vignette per situation, fixed across the whole product—don’t trade them by mood, and add no new vignettes.
- The default size is 96px; a whole-page empty state uses `hao-scene--lg` (160px). The vignette is decoration: add `aria-hidden="true"`.
- The title states where things stand, the message says the next step, and the button is that step. “All done” needs no button.
- A first run gets the primary button; every other situation gets `hao-btn--tinted`. When a search brings no results, put the words that were searched into the title.
- No playful lines like “Oh dear” or “Nothing here at all”, and no exclamation marks. When something goes wrong, make clear it isn’t the user’s fault.
- When one block fails to load and the rest of the page stands, use a banner; the lantern is only for a page with no content at all.
