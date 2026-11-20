# Radio

Pick one option from a set.

A `<label class="hao-radio">` wraps an `<input type="radio">` and its text; a group shares one `name`, goes inside `<fieldset class="hao-choices">`, and carries a `<legend>`.

- Use radio buttons for two to five options; for more, use a select. With only two or three very short options switching a view, use a segmented control.
- One option is always selected by default; put the most common or safest one first.
- Stack the options, one per line.

**Accessibility**

- It’s a native `<input type="radio">`: Tab stops once for the whole group, the arrow keys change the choice, Space selects—all built into the browser.
- On focus, a `focus`-colored ring is drawn.
- Selected or not is read from the `input`’s own state; the look of selection is the solid ring, never color alone.

## Markup

### English

```html
<fieldset class="hao-choices">
  <legend>Appearance</legend>
  <label class="hao-radio"><input type="radio" name="a-en" checked> Match system</label>
  <label class="hao-radio"><input type="radio" name="a-en"> Day</label>
  <label class="hao-radio"><input type="radio" name="a-en"> Night</label>
</fieldset>
```

### Chinese

```html
<fieldset class="hao-choices">
  <legend>外观</legend>
  <label class="hao-radio"><input type="radio" name="a" checked> 跟随系统</label>
  <label class="hao-radio"><input type="radio" name="a"> 昼</label>
  <label class="hao-radio"><input type="radio" name="a"> 夜</label>
</fieldset>
```
