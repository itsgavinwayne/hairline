# EmptyState · Empty state

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

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-4);align-items:flex-start"><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="wash" cx="60" cy="36" r="13"/><path class="far" d="M8 70q7-4 14 0t14 0 14 0 14 0 14 0 14 0M14 79q7-4 14 0t14 0 14 0 14 0 14 0M24 88q7-4 14 0t14 0 14 0 14 0"/></svg><h2 class="hao-empty__title">No notes yet</h2><p class="hao-empty__body">Write your first one and it will show up here.</p><button class="hao-btn">Write a note</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M4 50l14-10 10 6 14-14 16 16 12-7 22 11"/><path d="M30 62h36l-6 8H36zM40 62q8-13 16 0M48 49V38"/><path class="far" d="M12 78h20M40 80h28M74 77h12M26 87h18M54 88h20"/></svg><h2 class="hao-empty__title">No results for “spring”</h2><p class="hao-empty__body">Try another word, or browse all notes.</p><button class="hao-btn hao-btn--tinted">View all notes</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M-2 52l18-20 12 11 16-25 18 27 14-13 22 22"/><path d="M-2 72l22-16 14 9 20-18 22 20 22-9"/><path class="far" d="M10 64h16M34 62h10M66 64h18M18 82h24M52 84h30"/></svg><h2 class="hao-empty__title">Can’t reach the network</h2><p class="hao-empty__body">You can still read your notes. New changes will sync when you’re back online.</p><button class="hao-btn hao-btn--tinted">Try again</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path d="M24 46q14-3 24-18 10 15 24 18M48 28v-6M31 46h34M35 46v24M61 46v24M27 70h42"/><path class="far" d="M8 76h80M20 84h20M52 85h26"/></svg><h2 class="hao-empty__title">All done for today</h2><p class="hao-empty__body">Nothing left to do. Take a break.</p></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="far wash" cx="48" cy="45" r="26" style="stroke:none"/><path d="M48 12v10M41 22h14M41 22q-10 13 0 28h14q10-15 0-28M42 50h12M48 50v13M45 63h6"/><path class="far" d="M48 30v12"/></svg><h2 class="hao-empty__title">Couldn’t load this</h2><p class="hao-empty__body">Something went wrong, and it wasn’t anything you did.</p><button class="hao-btn hao-btn--tinted">Reload</button></div></div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-4);align-items:flex-start"><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="wash" cx="60" cy="36" r="13"/><path class="far" d="M8 70q7-4 14 0t14 0 14 0 14 0 14 0 14 0M14 79q7-4 14 0t14 0 14 0 14 0 14 0M24 88q7-4 14 0t14 0 14 0 14 0"/></svg><h2 class="hao-empty__title">还没有札记</h2><p class="hao-empty__body">写下第一条，它会出现在这里。</p><button class="hao-btn">写一条札记</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M4 50l14-10 10 6 14-14 16 16 12-7 22 11"/><path d="M30 62h36l-6 8H36zM40 62q8-13 16 0M48 49V38"/><path class="far" d="M12 78h20M40 80h28M74 77h12M26 87h18M54 88h20"/></svg><h2 class="hao-empty__title">没有找到「立春」</h2><p class="hao-empty__body">换一个词试试，或者看看全部札记。</p><button class="hao-btn hao-btn--tinted">查看全部札记</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M-2 52l18-20 12 11 16-25 18 27 14-13 22 22"/><path d="M-2 72l22-16 14 9 20-18 22 20 22-9"/><path class="far" d="M10 64h16M34 62h10M66 64h18M18 82h24M52 84h30"/></svg><h2 class="hao-empty__title">没连上网络</h2><p class="hao-empty__body">已有的札记还能看，新的修改会在连上后同步。</p><button class="hao-btn hao-btn--tinted">再试一次</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path d="M24 46q14-3 24-18 10 15 24 18M48 28v-6M31 46h34M35 46v24M61 46v24M27 70h42"/><path class="far" d="M8 76h80M20 84h20M52 85h26"/></svg><h2 class="hao-empty__title">今天的都做完了</h2><p class="hao-empty__body">没有待办了，歇一会儿。</p></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="far wash" cx="48" cy="45" r="26" style="stroke:none"/><path d="M48 12v10M41 22h14M41 22q-10 13 0 28h14q10-15 0-28M42 50h12M48 50v13M45 63h6"/><path class="far" d="M48 30v12"/></svg><h2 class="hao-empty__title">没能载入</h2><p class="hao-empty__body">出了点问题，不是你的操作造成的。</p><button class="hao-btn hao-btn--tinted">重新载入</button></div></div>
```
