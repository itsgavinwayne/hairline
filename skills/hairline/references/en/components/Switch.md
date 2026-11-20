# Switch

An on-and-off that takes effect at once.

Wrap the text and an `<input type="checkbox" role="switch">` in a `<label class="hao-switch">`. You supply the text—write it as a noun (“Daily reminders”), not a question.

- Flipping it takes effect immediately; no Save needed. Options that wait for a submit use a checkbox.
- On is `tint`, off is `border-control`. The knob is hollow when off (the track color shows through the middle) and solid when on; with position too, that’s three signals, not color alone.
- Inside a `ListGroup` row, the switch goes to the right.
- For a switch that can’t be flipped for now, add `disabled`: the switch drops to `opacity-disabled`, the text becomes `ink-tertiary`, and the pointer shows not-allowed; say why beside it.
- The thumb of a switch that is off has a small square hole at its center, round outside and square inside, after the shape of a copper coin; when on, the thumb is solid.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <label class="hao-switch">Daily reminder <input type="checkbox" role="switch" checked></label>
  <label class="hao-switch">Sync to iCloud <input type="checkbox" role="switch"></label>
  <label class="hao-switch">Sync over cellular <input type="checkbox" role="switch" disabled></label>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <label class="hao-switch">每日提醒 <input type="checkbox" role="switch" checked></label>
  <label class="hao-switch">同步到 iCloud <input type="checkbox" role="switch"></label>
  <label class="hao-switch">蜂窝网络下同步 <input type="checkbox" role="switch" disabled></label>
</div>
```
