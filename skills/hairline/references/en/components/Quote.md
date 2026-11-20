# Quote

Quote someone else’s words, framed by a pair of corner brackets taken from the shape of Chinese quotation marks.

`<blockquote class="hao-quote">`, with one `<p>` inside and an optional `<cite>`. You provide the text.

- The quotation is set in the Song typeface at the `title-2` size; the source uses `footnote`.
- One to three lines. Longer quotations are indented ordinary body text instead.
- One per screen. It already stands out; leave more white space around it and add no pattern.
- Two cuts, on the same idea as the relief and intaglio seals: the default is the yang cut, dark text on the light ground with only a pair of corner marks; add `hao-quote--yin` for the yin cut, the whole block filled with `ink` and the text reversed out. Use the yang cut in running text and the yin cut where the block has to hold the page (a poster, a cover, the close of an article). One cut per screen.
- The yin cut reverses with the theme: dark ground and light text by day, a bright block with dark text at night, the brightest thing on the screen. That is intended, since its job is to hold the page; if that is too bright at night, use the yang cut.
- Write the source as “作者《书名》” in Chinese, or “Author, Title” in English.
- The line in the example is from The Craft of Gardens (园冶), the Ming-dynasty treatise of Ji Cheng (计成).
- In an English interface, the corner brackets become an opening quote hanging at the upper left, and the text shifts right to match; the quotation itself takes no quotation marks.

**Accessibility**

- Use a real `<blockquote>`, so a screen reader knows the passage is quoted; the source goes in `<cite>` and is read along with it.
- The Chinese corner brackets and the English hanging quote are drawn with pseudo-elements; a screen reader doesn’t speak the graphics, and the quotation reads as written.

## Markup

### English

```html
<blockquote class="hao-quote" style="max-width:460px"><p>Though made by human hands, it seems the work of nature.</p><cite>Ji Cheng, The Craft of Gardens</cite></blockquote>
<blockquote class="hao-quote hao-quote--yin" style="max-width:460px;margin-top:var(--hao-space-6)"><p>The most important part of the paper is the part left unpainted.</p><cite>A morning in fog</cite></blockquote>
```

### Chinese

```html
<blockquote class="hao-quote" style="max-width:460px"><p>虽由人作，宛自天开。</p><cite>计成《园冶》</cite></blockquote>
<blockquote class="hao-quote hao-quote--yin" style="max-width:460px;margin-top:var(--hao-space-6)"><p>纸上最要紧的，是没画的地方。</p><cite>《雾里的早晨》</cite></blockquote>
```
