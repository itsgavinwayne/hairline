# Seal

A cinnabar seal is the signature of the person or product using this system, cut in the two traditional ways: intaglio (白文) and relief (朱文).

Use `<span class="hao-seal">印</span>`; you supply the seal text—characters from a surname, a given name, or a product name. The “seal (印)”, “user’s seal (使用者印)”, and “notes (札记)” in the preview are placeholders only.

**Two ways of carving**

- Intaglio (白文, the default): white characters left in a cinnabar ground. The strokes are thick, the characters fill the seal face, and only a thin rim of red remains at the edges. Use it where the brand shows: the launch screen, the About page, the navigation bar.
- Relief (`hao-seal--outline`): a fine border and fine strokes, with the bottom edge slightly heavier than the other three, so the seal sits steady. Use it for signatures: the top right corner of a card, the end of an article.

**Three seal faces**

| Class | Seal face | Seal text |
| --- | --- | --- |
| (default) | Square | One character |
| `hao-seal--four` | Square | Four characters, read vertically starting at the top right, set in a pattern like “so-and-so’s seal (某某之印)” |
| `hao-seal--tall` | Tall | Two characters stacked vertically, used as a leisure seal (闲章) or an opening seal (引首章) at the start of a passage |

**Four sizes**: `hao-seal--sm` 24px, the default 40px, `hao-seal--lg` 64px, `hao-seal--xl` 96px. A four-character seal is at least 64px, a tall seal at least 40px; at 24px use a single character only.

- The four corners of the seal face are small and slightly unequal, like a stone seal cut by hand—not the big rounded corners of an app icon. Don’t switch to `radius-sm` or a perfect circle.
- Set the seal text in the heaviest Song typeface (intaglio) or a medium weight (relief). The characters align vertically in the seal face and center themselves; don’t add padding or line height to nudge them.
- The default Song typeface characters are placeholders. For a true seal, follow “Seal design” in the guide to prepare seal-script artwork, then swap the text for `<span class="hao-seal hao-seal--art"><img src="…" alt=""></span>`; the size classes still apply. This system does not supply seal script; for seal-face sizes and character areas, see `SealGuide`.
- One seal per screen. If the screen already has a delete button or an error, no seal. A product uses one seal text; once set, it doesn’t change.
- No rotation, no distressing, no textures, no shadows.
- As a mark, add `role="img"` and an `aria-label` (the product’s or person’s name plus “seal”, as in “Lin’s seal”); as pure decoration, add `aria-hidden="true"`.
- In English interfaces, keep the seal in Han characters; don’t swap it for letters. Add `lang="zh"` and an English `aria-label`.
- The landing animation uses `hao-seal--stamp` and plays once, at the moment of completion; see `Stamp` for how to use it. The rest of the time the seal is still.

## Markup

### English

```html
<div class="hao-stack" style="max-width:none;gap:var(--hao-space-6)"><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl " lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal hao-seal--lg " lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal  " lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal hao-seal--sm " lang="zh" role="img" aria-label="Seal">印</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Intaglio, one character</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--outline" lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal hao-seal--lg hao-seal--outline" lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal  hao-seal--outline" lang="zh" role="img" aria-label="Seal">印</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" role="img" aria-label="Seal">印</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Relief, one character</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--four " lang="zh" role="img" aria-label="Seal">使用者印</span><span class="hao-seal hao-seal--lg hao-seal--four " lang="zh" role="img" aria-label="Seal">使用者印</span><span class="hao-seal hao-seal--xl hao-seal--tall " lang="zh" role="img" aria-label="Seal">札记</span><span class="hao-seal hao-seal--lg hao-seal--tall " lang="zh" role="img" aria-label="Seal">札记</span><span class="hao-seal hao-seal--tall " lang="zh" role="img" aria-label="Seal">札记</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Intaglio: four characters, and tall</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--four hao-seal--outline" lang="zh" role="img" aria-label="Seal">使用者印</span><span class="hao-seal hao-seal--lg hao-seal--four hao-seal--outline" lang="zh" role="img" aria-label="Seal">使用者印</span><span class="hao-seal hao-seal--xl hao-seal--tall hao-seal--outline" lang="zh" role="img" aria-label="Seal">札记</span><span class="hao-seal hao-seal--lg hao-seal--tall hao-seal--outline" lang="zh" role="img" aria-label="Seal">札记</span><span class="hao-seal hao-seal--tall hao-seal--outline" lang="zh" role="img" aria-label="Seal">札记</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Relief: four characters, and tall</span></div></div>
```

### Chinese

```html
<div class="hao-stack" style="max-width:none;gap:var(--hao-space-6)"><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl " role="img" aria-label="印章">印</span><span class="hao-seal hao-seal--lg " role="img" aria-label="印章">印</span><span class="hao-seal  " role="img" aria-label="印章">印</span><span class="hao-seal hao-seal--sm " role="img" aria-label="印章">印</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">白文 单字</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--outline" role="img" aria-label="印章">印</span><span class="hao-seal hao-seal--lg hao-seal--outline" role="img" aria-label="印章">印</span><span class="hao-seal  hao-seal--outline" role="img" aria-label="印章">印</span><span class="hao-seal hao-seal--sm hao-seal--outline" role="img" aria-label="印章">印</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">朱文 单字</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--four " role="img" aria-label="印章">使用者印</span><span class="hao-seal hao-seal--lg hao-seal--four " role="img" aria-label="印章">使用者印</span><span class="hao-seal hao-seal--xl hao-seal--tall " role="img" aria-label="印章">札记</span><span class="hao-seal hao-seal--lg hao-seal--tall " role="img" aria-label="印章">札记</span><span class="hao-seal hao-seal--tall " role="img" aria-label="印章">札记</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">白文 四字、长方</span></div><div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-end"><span class="hao-seal hao-seal--xl hao-seal--four hao-seal--outline" role="img" aria-label="印章">使用者印</span><span class="hao-seal hao-seal--lg hao-seal--four hao-seal--outline" role="img" aria-label="印章">使用者印</span><span class="hao-seal hao-seal--xl hao-seal--tall hao-seal--outline" role="img" aria-label="印章">札记</span><span class="hao-seal hao-seal--lg hao-seal--tall hao-seal--outline" role="img" aria-label="印章">札记</span><span class="hao-seal hao-seal--tall hao-seal--outline" role="img" aria-label="印章">札记</span><span style="font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">朱文 四字、长方</span></div></div>
```
