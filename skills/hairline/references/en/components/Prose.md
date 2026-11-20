# Prose · Long-form text

The reading layout for long text: how a piece is set, from its title to its signature.

Inside `<article class="hao-prose">`, in order: an `<h1>`, `.hao-prose__meta`, a run of `<p>`s and `<h2>`s, with `Divider`, `Quote`, or `Mount` woven in, and an optional `.hao-prose__sign` (a group of signature items) at the end. You provide the text.

- **Measure**: the line width stays within `measure` (about 38 Chinese characters). Top margin 72px, bottom margin 48px—more above than below, the thread-bound book rule that the head outweighs the foot: the head leaves room for marginal notes and gives the title room to breathe.
- **Chinese paragraphs**: first line indented two characters, justified, with no blank line between paragraphs. Line height 32px, one step looser than interface body text.
- **English paragraphs**: left-aligned, first line indented 1.5 character widths; the first paragraph after a heading takes no indent. Line height 28px.
- **Headings**: `<h1>` uses `title-1`, one per piece; sections use `<h2>`, `title-2`; one level below that uses `<h3>`, `title-3`, and that is the last. Headings take no period and aren’t centered.
- **Dates**: can be written with the sexagenary cycle and the solar term—the Bingwu year, four days before Minor Snow (丙午年 小雪前四日)—one of the few places in this system allowed a touch of grace; working timestamps stay numeric.
- **Chapters** use the `Divider` with the fishtail mark, at most two or three in a piece.
- The **signature** sits right: a vertical date line with a small seal (in English, an italic colophon with the seal). A page with a signature carries no other seal.
- Links in the body use `.hao-link`; emphasize with bold, not color.
- Reading pages carry no patterns; the fishtail and the signature are enough.

**Accessibility**

- The structure is the semantics: the whole piece sits in `<article class="hao-prose">`, and a screen reader jumps through the `<h1>` and `<h2>` levels.
- The fishtail divider between chapters takes `role="separator"` as in the preview.
- The small seal in the signature takes `aria-hidden="true"` as in the preview; the date-line text (`.hao-slip`, or the italic colophon in English) stays in the screen reader.

## Markup

### English

```html
<article class="hao-prose" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<h1>A morning in fog</h1>
<p class="hao-prose__meta">Four days before Minor Snow, the Bingwu year</p>
<p>I opened the window this morning and the building across the street was only a faint outline. The fog had taken away everything far off and left one small patch in front of me: the windowsill, a pot of asparagus fern, a glass of water just poured.</p>
<p>I usually think that seeing clearly means seeing far. Today I couldn’t see far, so I looked closely at what was near. The fern had put out a new shoot, thin as a thread, that wasn’t there yesterday.</p>
<h2>Blank space</h2>
<p>Landscape painters say the most important part of the paper is the part left unpainted. Fog may be the blank space the world leaves for itself. It adds nothing. It only sets aside what isn’t needed yet.</p>
<div class="hao-divider" role="separator"><i></i></div>
<p>By nine the fog had lifted and the building was back, every window sharp. I finished the water and started on the first thing of the day.</p>
<div class="hao-prose__sign"><span class="hao-sign hao-sign--row"><span class="hao-colophon">Winter, the Bingwu year</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></span></div>
</article>
```

### Chinese

```html
<article class="hao-prose" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<h1>雾里的早晨</h1>
<p class="hao-prose__meta">丙午年 小雪前四日</p>
<p>早上推开窗，对面的楼只剩一个淡淡的轮廓。雾把远处的东西都收走了，只留下眼前这一小块：窗台、一盆文竹、一杯刚倒的水。</p>
<p>平时总觉得要看得远才算看清楚。今天看不远，反倒把近处的东西看了个仔细。文竹新抽了一枝，细得像一根线，昨天还没有。</p>
<h2>留白</h2>
<p>画山水的人说，纸上最要紧的是没画的地方。雾大概就是天地自己留的白。它什么也不添，只是把多余的先拿开。</p>
<div class="hao-divider" role="separator"><i></i></div>
<p>等到九点钟，雾散了，楼又回来了，一扇扇窗户都清清楚楚。我把杯子里的水喝完，开始做今天的第一件事。</p>
<div class="hao-prose__sign"><span class="hao-sign"><span class="hao-slip">丙午冬</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></span></div>
</article>
```
