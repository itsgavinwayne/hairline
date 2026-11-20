# Segmented · Segmented control

Switch between two and five parallel views.

Inside `.hao-seg`, each segment is a `<label><input type="radio" name="…"><span>text</span></label>`, and the group shares one `name`. You supply each segment’s text and the group’s `aria-label`.

- One short word per segment—ten characters at most in English, one or two in Chinese—and all segments equal in width.
- Use it only to switch views of the same content; to jump to another page, use the tab bar.
- Past five segments, use a list or a menu instead.
- When the window is narrower than 600px, the segments split the width equally, and text that doesn’t fit is truncated.

## Markup

### English

```html
<div class="hao-seg" role="radiogroup" aria-label="Time range">
  <label><input type="radio" name="r-en" checked><span>Day</span></label>
  <label><input type="radio" name="r-en"><span>Week</span></label>
  <label><input type="radio" name="r-en"><span>Month</span></label>
  <label><input type="radio" name="r-en"><span>Year</span></label>
</div>
```

### Chinese

```html
<div class="hao-seg" role="radiogroup" aria-label="时间范围">
  <label><input type="radio" name="r" checked><span>日</span></label>
  <label><input type="radio" name="r"><span>周</span></label>
  <label><input type="radio" name="r"><span>月</span></label>
  <label><input type="radio" name="r"><span>年</span></label>
</div>
```
