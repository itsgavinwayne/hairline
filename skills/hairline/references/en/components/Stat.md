# Stat

Put one important number up large.

Inside `.hao-stat`, in order: `.hao-stat__l` (what it is), `.hao-stat__v` (the number, with the unit in a `<small>`), and an optional `.hao-stat__n` (a comparison or a remark).

- The number is set in the Song typeface with tabular figures; the unit is a smaller sans-serif word after it (条, 字, 天). In Chinese the measure word is part of the number—don’t drop it.
- At most four in a row, each saying one thing.
- Write the remark as a sentence (“6 more than last month”), not an up or down arrow with a percentage, and not red or green for rise and fall.
- Separate thousands with commas. Past ten thousand you may write “4.8 万”; settle on one style across the product.
- Where the number isn’t the point, the value at the right of a list row is enough.

**Accessibility**

- Label, number, and remark are plain text, and the DOM order is the reading order: first what it is, then how much.
- The unit sits in the `<small>` and reads right after the number; nothing in the component is tappable, so the keyboard isn’t involved.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-start">
  <div class="hao-stat"><span class="hao-stat__l">Notes this month</span><span class="hao-stat__v">31<small>notes</small></span><span class="hao-stat__n">6 more than last month</span></div>
  <div class="hao-stat"><span class="hao-stat__l">Total words</span><span class="hao-stat__v">48,260<small>words</small></span></div>
  <div class="hao-stat"><span class="hao-stat__l">Current streak</span><span class="hao-stat__v">12<small>days</small></span><span class="hao-stat__n">Longest: 27 days</span></div>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-start">
  <div class="hao-stat"><span class="hao-stat__l">本月札记</span><span class="hao-stat__v">31<small>条</small></span><span class="hao-stat__n">比上月多 6 条</span></div>
  <div class="hao-stat"><span class="hao-stat__l">累计字数</span><span class="hao-stat__v">48,260<small>字</small></span></div>
  <div class="hao-stat"><span class="hao-stat__l">连续记录</span><span class="hao-stat__v">12<small>天</small></span><span class="hao-stat__n">最长 27 天</span></div>
</div>
```
