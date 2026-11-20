# Verse · Vertical verse

A poem set vertically, or a short passage worth standing on its own—the only place in the system where body text runs vertically.

Inside `.hao-verse`, first comes `.hao-verse__title`, then one `<p>` per line, and last `.hao-verse__by` (the author, with an optional small seal). You supply the text.

- Vertical, right to left: the title at the far right, the author at the far left. Each line takes one column, with no punctuation (punctuation takes space in a vertical setting, and old poems carried none anyway).
- Use it only for short writing—poems, couplets, inscriptions: no more than eight columns, no more than ten characters to a column. Long text doesn’t go vertical; horizontal reads faster.
- English doesn’t go vertical. When the root element is English, it becomes horizontal serif verse lines on its own, the title above and the author in italics below.
- The characters are set in the Song typeface, with loosened spacing and line height at twice the character height.
- It can open a reading page, sit in a card, or stand on a launch screen. One per screen, with plenty of white space around it.
- The example is “Deer Park (鹿柴)” by Wang Wei (王维); the English version translates the meaning and follows no published translation.

**Accessibility**

- Title, lines, and author are all text in `<p>`s; the DOM order is the reading order, and the vertical setting is looks only.
- The small seal beside the author takes `aria-hidden="true"`, as in the preview; the author’s name is read as usual.
- In an English interface, it becomes horizontal verse lines on its own; the text doesn’t change.

## Markup

### English

```html
<div class="hao-verse" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg);padding:var(--hao-space-6)">
<p class="hao-verse__title">Deer Enclosure</p>
<p>Empty hills, no one in sight,</p><p>yet voices can be heard.</p><p>Late sunlight enters the deep wood</p><p>and shines again on the green moss.</p>
<p class="hao-verse__by">Wang Wei</p>
</div>
```

### Chinese

```html
<div class="hao-verse" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<p class="hao-verse__title">鹿柴</p>
<p>空山不见人</p><p>但闻人语响</p><p>返景入深林</p><p>复照青苔上</p>
<p class="hao-verse__by">王维<span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></p>
</div>
```
