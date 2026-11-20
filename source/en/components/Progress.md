Several ways to say “in progress”. The shapes borrow three traditional motifs: moon phases, stitching, and the water clock.

**When you know how far along it is**

| Class | Motif | Where |
| --- | --- | --- |
| `.hao-moon` | A waxing moon: from new moon to full, filling in little by little | Things that “add up”: goals, habits, reading progress. When it’s full, add `hao-moon--done`; it turns bamboo green |
| `.hao-progress.hao-progress--stitch` | Stitching: the part covered is a solid line, the rest a row of stitches, with a small dot at the thread’s end | Things “being done”: exporting, uploading, installing |
| `.hao-progress.hao-progress--ke` | Graduations, from the water clock (漏刻): a tick under the track for every tenth | Things read against a scale: capacity, quotas, allowances |
| `.hao-progress` | A plain rule, with no motif | Dense interfaces, inside table rows, or when the screen already carries another motif |

- A waxing moon takes its progress from the inline `--p` (0 to 1); inside a progress bar goes a `<span>`, with progress on the inline `--v` (a percentage).
- The moon comes in two sizes, 28px and 64px (`hao-moon--lg`). Pair the large one with a line of text; the small ones can stand in a row, one a day.
- A line of text alongside always says how far along it is. When the number needs to be exact, give a percentage or a count; for a rough impression, “about 60%” will do.

**When you don’t**

- `.hao-spinner`: a crescent turning. For waits of a few seconds, with a word beside it.
- `.hao-ripple`: a drop of water landing, ring after ring spreading out (put an `<i>` inside). For whole-page loads and pull-to-refresh.
- `.hao-spinner.hao-spinner--ring`: a plain ring, for inside buttons or very small spots.
- `.hao-skeleton`: gray placeholder blocks while the content hasn’t arrived; you set the width and height; no flicker.

**Rules**

- For waits under a second, show nothing.
- These motifs are the controls’ own shapes, not patterns, and don’t count against “one per screen”. Still, use only one progress motif per screen; don’t mix moon, line, and graduations.
- Use only `tint`; use `jade` for done. Don’t use `gold` or `seal`.
- Write the amount on the inline variable of the `<span>` inside: `style="--v:60%"`. The older `style="width:60%"` still works, but the value doesn’t transition when it changes.
- Progress takes `role="progressbar"` and `aria-valuenow`; loading takes `role="status"` and `aria-label`.
- When Reduce Motion is on, the crescent slows and the ripple goes still.
- While a long piece of text is on its way, use `hao-skeleton--lines`: a few thin ruled lines, like a blank sheet of letter paper. Keep the height a multiple of 32px.
