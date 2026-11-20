# Mount · Mounting

Mounts a picture worth pausing on: silk borders on all four sides, and, on a vertical piece, a rod along the bottom.

Inside `<figure class="hao-mount">` go one `<img>` (or SVG) and a `<figcaption>`. A horizontal piece adds `hao-mount--wide`. You provide the picture; the painting in the preview is a placeholder line drawing.

- **Hanging scroll** (the default, vertical): the silk above is wider than the silk below, roughly three to two—these are the “heaven” (天头) and “earth” (地头) bands; a slim rod along the top, and along the bottom a rod whose two ends poke out.
- **Horizontal scroll** (`hao-mount--wide`, horizontal): the silk at the sides is wider than at top and bottom, and there is no rod.
- Around the painting runs a very fine line of gold ink, the border strip (局条) of a mounting. The painting itself keeps square corners—no rounding. This is one of the few places in the system without rounded corners, because paintings are square.
- The silk uses `surface-sunken`, plain, with no pattern.
- Give it only to pictures worth stopping for: an article’s lead image, works, covers. Thumbnails in lists, avatars, and screenshots don’t get mounted.
- One per screen. It already carries enough weight; put no pattern beside it.
- The image needs `alt`; the `<figcaption>` is the picture’s name, one to three words (two to six characters in Chinese), centered.
- The hanging scroll defaults to 220px wide and the horizontal scroll to 420px; override the width and the proportions follow.
- Two “startled swallows” (惊燕) hang in the upper margin of the hanging scroll: the pair of silk strips such a scroll has always carried. The horizontal mounting has none.

**Accessibility**

- The painting needs a name: an SVG painting takes `role="img"` and `aria-label` as in the preview, so a screen reader treats it as a named image; an `<img>` gets its name from `alt`.
- The silk borders, the rods, and the border strip are all drawn with pseudo-elements and stay out of the screen reader.
- The `<figure>` and `<figcaption>` pair lets screen readers natively match the painting with its name; no extra attributes needed.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start"><figure class="hao-mount"><svg viewBox="0 0 200 300" role="img" aria-label="Distant hills, a lone boat and the moon"><circle class="wash" cx="142" cy="62" r="18"/><path class="far" d="M0 150l30-42 24 22 30-52 36 58 30-28 50 46M0 176h42M60 172h30M120 176h60"/><path d="M0 206l40-30 28 16 40-36 44 40 48-18"/><path d="M78 246h40l-7 9H85zM89 246q9-14 18 0M98 232v-12"/><path class="far" d="M20 262h40M72 266h56M140 261h40M40 278h36M96 280h60"/></svg><figcaption>On the river</figcaption></figure><figure class="hao-mount hao-mount--wide"><svg viewBox="0 0 340 150" role="img" aria-label="A range of distant hills under the moon"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>Distant hills</figcaption></figure></div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start"><figure class="hao-mount"><svg viewBox="0 0 200 300" role="img" aria-label="远山、孤舟与月"><circle class="wash" cx="142" cy="62" r="18"/><path class="far" d="M0 150l30-42 24 22 30-52 36 58 30-28 50 46M0 176h42M60 172h30M120 176h60"/><path d="M0 206l40-30 28 16 40-36 44 40 48-18"/><path d="M78 246h40l-7 9H85zM89 246q9-14 18 0M98 232v-12"/><path class="far" d="M20 262h40M72 266h56M140 261h40M40 278h36M96 280h60"/></svg><figcaption>江上</figcaption></figure><figure class="hao-mount hao-mount--wide"><svg viewBox="0 0 340 150" role="img" aria-label="连绵的远山与月"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>远山</figcaption></figure></div>
```
