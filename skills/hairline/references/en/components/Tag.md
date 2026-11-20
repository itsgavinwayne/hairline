# Tag

Marks the current status of a piece of content; not tappable.

Use a `<span class="hao-tag">` plus a tone class: the default (neutral), `hao-tag--tint`, `hao-tag--jade`, `hao-tag--amber`, `hao-tag--seal`. You supply the text—one or two words (two to four characters in Chinese).

- The text carries the status; color only helps. No tags with a dot and no word.
- At most two tags in a row.
- `hao-tag--seal` is only for problems that truly need attention.

**Accessibility**

- A tag is just the words inside the `<span>`; the dot in front is drawn by `::before`, and a screen reader reads the text only.
- The five tone classes change the colors only—not the structure, and not what gets read out.

## Markup

### English

```html
<div class="hao-row">
  <span class="hao-tag">Draft</span>
  <span class="hao-tag hao-tag--tint">In progress</span>
  <span class="hao-tag hao-tag--jade">Done</span>
  <span class="hao-tag hao-tag--amber">Due today</span>
  <span class="hao-tag hao-tag--seal">Overdue</span>
</div>
```

### Chinese

```html
<div class="hao-row">
  <span class="hao-tag">草稿</span>
  <span class="hao-tag hao-tag--tint">进行中</span>
  <span class="hao-tag hao-tag--jade">已完成</span>
  <span class="hao-tag hao-tag--amber">今天到期</span>
  <span class="hao-tag hao-tag--seal">已逾期</span>
</div>
```
