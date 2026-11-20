# Poster

Templates for posters, social images, and slide covers. One container, three ratios.

`.hao-poster` is the image itself, 2:3 by default (poster); `hao-poster--square` is 1:1 (square social image) and `hao-poster--wide` is 16:9 (slides, web header images); `hao-poster--tint` swaps in an azurite background. The parts inside: `.hao-poster__title` (the large title; add `--v` for vertical setting), `.hao-poster__sub`, `.hao-poster__meta`, `.hao-poster__foot` (the bottom line, information on the left and the seal on the right), and `.hao-poster__moon` (a moon on the azurite background). Set the image width with the inline `--w`; every type size, margin, and seal inside scales with it.

Five templates:

| Template | Image | For |
| --- | --- | --- |
| Event | Moon-white background, vertical large title on the right, information at lower left, a band of wave pattern along the bottom | Events, launches, exhibitions |
| Solar term | Full azurite background, a moon above, the solar term’s name below | Solar terms, holidays, an image a day |
| Poem | Moon-white background, a fret along the top, the poem set vertically in the middle | Poems, dedications, a line a week |
| Quote (square) | Moon-white background, one sentence, gold-ink corner marks | Quote images for social platforms |
| Cover (wide) | Moon-white background, a line of large title at lower left, the mark at lower right | Slide covers, article header images |

The rules are the same as for interfaces, only stricter:

- **It doesn’t follow the theme.** A poster is print material and uses the day colors in both themes: put `data-theme="light"` on `.hao-poster`. Without it, the azurite ground turns pale at night and the moon becomes a black hole.
- **One scene per piece, one seal per piece.** Each image carries one pattern or one moon, and one touch of cinnabar (a seal, or a cinnabar-colored mark). On an azurite background, the mark and the seal go monochrome.
- **Keep more than half empty.** At least half the image stays empty. When the text is short, don’t enlarge it to fill the space.
- **Leave one-twelfth of the image width on all four sides**, and align all content to this edge.
- **Set titles in the Song typeface**, one large title per image. Chinese can be set vertically, on the right; English runs horizontal, in Newsreader.
- **Set information in small sans-serif type**, at lower left; the seal goes at lower right.
- The mark is only for images introducing this system itself; other images put the product’s own seal at lower right.

For the color values, fonts, and bleed used in print, see “Print and graphics” in the guide.

**Accessibility**

- Hide the patterns from screen readers: give `.hao-wave` and `.hao-fret` `role="presentation"` as in the preview.
- Everything the image says is in real text: the title, the description, and the signature are `<h2>`s and `<p>`s, so a screen reader gets the whole poster.
- The graphics in the seal and the mark take `aria-hidden="true"` as in the preview; the text in `.hao-poster__foot` says who stands at the lower right.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start"><div class="hao-poster" data-theme="light"><div style="display:flex;justify-content:space-between;flex:1">
  <div><p class="hao-poster__meta">Book club, no. 7</p><p class="hao-poster__sub">Ji Cheng,<br>The Craft of Gardens</p></div>
  </div>
  <h2 class="hao-poster__title" style="margin-bottom:calc(var(--w)*.3)">Made by hand,<br>as if by nature</h2>
  <div class="hao-poster__foot"><p class="hao-poster__meta">Wednesday, November 18<br>7:30 PM, online</p><span class="hao-seal " lang="zh" aria-hidden="true">印</span></div>
  <div class="hao-wave" role="presentation"></div></div><div class="hao-poster hao-poster--tint" data-theme="light"><div class="hao-poster__moon" style="margin:calc(var(--w)*.06) auto 0"></div>
  <h2 class="hao-poster__title" style="margin-top:calc(var(--w)*.1)">Minor Snow</h2>
  <p class="hao-poster__sub" style="font-weight:500">The days turn cold. Sleep early, and keep a pot of tea warm.</p>
  <div class="hao-poster__foot"><p class="hao-poster__meta">November 22<br>the Bingwu year</p><span class="hao-logo hao-logo--ink" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div><div class="hao-poster" data-theme="light"><div class="hao-fret" role="presentation"></div><div style="flex:1;display:grid;place-items:center start"><div class="hao-verse" lang="en"><p class="hao-verse__title">Deer Enclosure</p><p>Empty hills, no one in sight,</p><p>yet voices can be heard.</p><p class="hao-verse__by">Wang Wei</p></div></div><div class="hao-poster__foot"><p class="hao-poster__meta">A poem a week</p><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div></div>
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start;margin-top:var(--hao-space-6)"><div class="hao-poster hao-poster--square" data-theme="light"><blockquote class="hao-quote" style="margin:auto 0"><p>The most important part of the paper is the part left unpainted.</p><cite>A morning in fog</cite></blockquote><div class="hao-poster__foot"><span></span><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div><div class="hao-poster hao-poster--wide" data-theme="light" style="--w:min(480px, 72vw)"><h2 class="hao-poster__title" style="font-size:calc(var(--w)*.085);margin-top:auto">November in review</h2><p class="hao-poster__sub" style="font-size:calc(var(--w)*.034);font-weight:500">31 notes, 48,260 words</p><div class="hao-poster__foot" style="margin-top:calc(var(--w)*.05)"><p class="hao-poster__meta" style="font-size:calc(var(--w)*.026)">Winter, the Bingwu year</p><span class="hao-logo" style="font-size:calc(var(--w)*.036)" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div></div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start"><div class="hao-poster" data-theme="light"><div style="display:flex;justify-content:space-between;flex:1">
  <div><p class="hao-poster__meta">读书会 第七期</p><p class="hao-poster__sub">计成《园冶》</p></div>
  <h2 class="hao-poster__title hao-poster__title--v">虽由人作<br>宛自天开</h2></div>
  
  <div class="hao-poster__foot"><p class="hao-poster__meta">十一月十八日 周三<br>晚上七点半，线上</p><span class="hao-seal " lang="zh" aria-hidden="true">印</span></div>
  <div class="hao-wave" role="presentation"></div></div><div class="hao-poster hao-poster--tint" data-theme="light"><div class="hao-poster__moon" style="margin:calc(var(--w)*.06) auto 0"></div>
  <h2 class="hao-poster__title" style="margin-top:calc(var(--w)*.1)">小雪</h2>
  <p class="hao-poster__sub" style="font-weight:600">天渐寒，宜早睡，宜温一壶茶</p>
  <div class="hao-poster__foot"><p class="hao-poster__meta">丙午年十月十四<br>十一月二十二日</p><span class="hao-logo hao-logo--ink" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div><div class="hao-poster" data-theme="light"><div class="hao-fret" role="presentation"></div><div style="flex:1;display:grid;place-items:center"><div class="hao-verse"><p class="hao-verse__title">鹿柴</p><p>空山不见人</p><p>但闻人语响</p><p>返景入深林</p><p>复照青苔上</p><p class="hao-verse__by">王维</p></div></div><div class="hao-poster__foot"><p class="hao-poster__meta">每周一诗</p><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div></div>
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start;margin-top:var(--hao-space-6)"><div class="hao-poster hao-poster--square" data-theme="light"><blockquote class="hao-quote" style="margin:auto 0"><p>纸上最要紧的，是没画的地方。</p><cite>《雾里的早晨》</cite></blockquote><div class="hao-poster__foot"><span></span><span class="hao-seal hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div><div class="hao-poster hao-poster--wide" data-theme="light" style="--w:min(480px, 72vw)"><h2 class="hao-poster__title" style="font-size:calc(var(--w)*.085);margin-top:auto">十一月回顾</h2><p class="hao-poster__sub" style="font-size:calc(var(--w)*.034);font-weight:600">写了 31 条，共 48,260 字</p><div class="hao-poster__foot" style="margin-top:calc(var(--w)*.05)"><p class="hao-poster__meta" style="font-size:calc(var(--w)*.026)">丙午年 冬</p><span class="hao-logo" style="font-size:calc(var(--w)*.036)" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div></div></div>
```
