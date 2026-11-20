# Avatar

A round avatar standing in for a person.

`<span class="hao-avatar">` holds an `<img>`, or the first character of the name when there is no photo. Sizes: `hao-avatar--sm` 28px, default 40px, `hao-avatar--lg` 64px. Use `.hao-avatar-group` for several side by side.

- People are round, seals are square. An avatar is always a perfect circle; don’t let it read as a seal, and don’t color an avatar cinnabar.
- With no photo, a Chinese name takes the family name character and an English name takes the initials, on a `tint-wash` ground with `tint` text.
- Add `role="img"` and an `aria-label` with the full name; when the name already sits beside it, use `aria-hidden="true"` instead.
- Show at most three side by side; fold the rest into a “+3”.
- When an English name supplies two initials, the type steps down one size on its own so both letters fit.
- With no photo there is also a more considered look, `hao-avatar--name`: a round family-name seal, the family name in the Song typeface inside a thin azurite circle. Use it where the person is the subject, such as a profile page or an author byline; when avatars run in rows down a list, use the default light-ground style. Round and azurite, it never reads as the square, cinnabar seal. Han characters only.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5)">
  <span class="hao-avatar hao-avatar--lg" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar hao-avatar--sm" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar-group"><span class="hao-avatar" role="img" aria-label="Lin Wan">LW</span><span class="hao-avatar" role="img" aria-label="Zhou Xing">ZX</span><span class="hao-avatar" role="img" aria-label="3 more">+3</span></span>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-5)">
  <span class="hao-avatar hao-avatar--lg" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--sm" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--lg hao-avatar--name" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--name" role="img" aria-label="周行">周</span>
  <span class="hao-avatar-group"><span class="hao-avatar" role="img" aria-label="林晚">林</span><span class="hao-avatar" role="img" aria-label="周行">周</span><span class="hao-avatar" role="img" aria-label="另外三人">+3</span></span>
</div>
```
