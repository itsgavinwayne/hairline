# Progress · Progress and loading

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

## Markup

### English

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),340px));gap:var(--hao-space-8) var(--hao-space-12);align-items:start">
  <div><div class="hao-row" style="gap:var(--hao-space-4)"><span class="hao-moon hao-moon--lg" role="progressbar" aria-label="Monthly goal" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" style="--p:.62"></span><div><div style="font:600 24px/32px var(--hao-font-serif)">62%</div><div style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin:0">31 notes this month, goal 50</div></div></div>
    <div class="hao-row" style="gap:var(--hao-space-4);margin-top:var(--hao-space-5)"><span class="hao-moon" style="--p:.1"></span><span class="hao-moon" style="--p:.3"></span><span class="hao-moon" style="--p:.5"></span><span class="hao-moon" style="--p:.7"></span><span class="hao-moon" style="--p:.9"></span><span class="hao-moon hao-moon--done" style="--p:1"></span></div>
    <p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Waxing moon: new to full, turning jade when complete</p></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-6)">
    <div><div class="hao-progress hao-progress--stitch" role="progressbar" aria-label="Exporting" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100"><span style="--v:62%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-3)">Thread: exporting, 62% done</p></div>
    <div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="Storage" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-5)">Ticks: 4 GB of 10 GB used</p></div>
    <div><div class="hao-progress" role="progressbar" aria-label="Uploading" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"><span style="--v:80%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Plain: uploading</p></div>
  </div>
  <div class="hao-row" style="gap:var(--hao-space-6)"><span class="hao-row"><span class="hao-spinner" role="status" aria-label="Syncing"></span><span style="font-size:15px;color:var(--hao-ink-secondary)">Syncing</span></span><span class="hao-row"><span class="hao-ripple" role="status" aria-label="Loading"><i></i></span><span style="font-size:15px;color:var(--hao-ink-secondary)">Loading</span></span><span class="hao-spinner hao-spinner--ring" role="status" aria-label="Loading"></span></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-2)" aria-hidden="true"><span class="hao-skeleton" style="width:45%;height:22px"></span><span class="hao-skeleton"></span><span class="hao-skeleton" style="width:80%"></span><span class="hao-skeleton hao-skeleton--lines" style="margin-top:var(--hao-space-3)"></span></div>
</div>
```

### Chinese

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),340px));gap:var(--hao-space-8) var(--hao-space-12);align-items:start">
  <div><div class="hao-row" style="gap:var(--hao-space-4)"><span class="hao-moon hao-moon--lg" role="progressbar" aria-label="本月目标" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" style="--p:.62"></span><div><div style="font:600 24px/32px var(--hao-font-serif)">六成二</div><div style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin:0">本月写了 31 条，目标 50 条</div></div></div>
    <div class="hao-row" style="gap:var(--hao-space-4);margin-top:var(--hao-space-5)"><span class="hao-moon" style="--p:.1"></span><span class="hao-moon" style="--p:.3"></span><span class="hao-moon" style="--p:.5"></span><span class="hao-moon" style="--p:.7"></span><span class="hao-moon" style="--p:.9"></span><span class="hao-moon hao-moon--done" style="--p:1"></span></div>
    <p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">月盈：从朔到望，满了转为竹青</p></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-6)">
    <div><div class="hao-progress hao-progress--stitch" role="progressbar" aria-label="正在导出" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100"><span style="--v:62%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-3)">针线：正在导出，已完成 62%</p></div>
    <div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="存储空间" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary);margin-top:var(--hao-space-5)">刻度：已用 4 GB，共 10 GB</p></div>
    <div><div class="hao-progress" role="progressbar" aria-label="正在上传" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"><span style="--v:80%"></span></div><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">素线：正在上传</p></div>
  </div>
  <div class="hao-row" style="gap:var(--hao-space-6)"><span class="hao-row"><span class="hao-spinner" role="status" aria-label="正在同步"></span><span style="font-size:15px;color:var(--hao-ink-secondary)">正在同步</span></span><span class="hao-row"><span class="hao-ripple" role="status" aria-label="正在载入"><i></i></span><span style="font-size:15px;color:var(--hao-ink-secondary)">正在载入</span></span><span class="hao-spinner hao-spinner--ring" role="status" aria-label="载入中"></span></div>
  <div style="display:flex;flex-direction:column;gap:var(--hao-space-2)" aria-hidden="true"><span class="hao-skeleton" style="width:45%;height:22px"></span><span class="hao-skeleton"></span><span class="hao-skeleton" style="width:80%"></span><span class="hao-skeleton hao-skeleton--lines" style="margin-top:var(--hao-space-3)"></span></div>
</div>
```
