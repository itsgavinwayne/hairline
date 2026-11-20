# Divider

A rule dividing two major sections of a long piece, with a fishtail mark (鱼尾) at its center.

`<div class="hao-divider" role="separator"><i></i></div>`.

- The fishtail is a mark from the center seam of woodblock-printed pages, originally for aligning the folded leaves. Here it marks where “a chapter ends”.
- Use it only in long text, article detail pages, and About pages—two or three at most in one piece.
- Between list rows use `hairline`, and between groups use white space; this divider is for neither.
- It belongs to the article’s typography, not to the patterns; still, never layer it with a stitch or a fret in the same place.
- The other kind is the double rule, `hao-divider--wenwu`: one thick line and one thin, from the page frame of Song printed books, the same shape as the rule under a table header. Use it at the head of a chapter or a group; the fishtail goes between passages.

## Markup

### English

```html
<div class="hao-stack" style="gap:var(--hao-space-6)"><div class="hao-divider" role="separator"><i></i></div><p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">The mark in the middle is a “fishtail”, the fold guide printed at the center of a woodblock page.</p></div>

<div class="hao-divider hao-divider--wenwu" role="separator" style="max-width:390px;margin:var(--hao-space-6) 0 var(--hao-space-4)"></div>
<p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">The other kind is the double rule, one thick line and one thin, from the page frame of Song printed books. Use it at the head of a chapter or a group.</p>
```

### Chinese

```html
<div class="hao-stack" style="gap:var(--hao-space-6)"><div class="hao-divider" role="separator"><i></i></div><p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">中间的记号叫「鱼尾」，是雕版书页版心上用来对折的标记。</p></div>

<div class="hao-divider hao-divider--wenwu" role="separator" style="max-width:390px;margin:var(--hao-space-6) 0 var(--hao-space-4)"></div>
<p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">另一种是文武线：一粗一细，取自宋版书的版框，用在一章、一组内容的开头。</p>
```
