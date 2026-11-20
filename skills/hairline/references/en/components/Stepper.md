# Stepper

Adjust a small number step by step with plus and minus buttons.

Inside `.hao-stepper`, in order: the minus button, an `<output>`, and the plus button. Both buttons need an `aria-label`. You supply the value.

- It suits small ranges like 1 to 20; for larger ranges use a text field.
- At either limit, the matching button gets `disabled`.
- Write the unit outside the control (“条”), not inside the number.
- Press and hold to keep stepping.

**Behavior** (when the behavior script is loaded)

- The plus and minus buttons work. Set the range and step with `data-min`, `data-max`, and `data-step`; at either end, the matching button disables itself.
- Press and hold to keep stepping. Each change fires a `hao-change` event.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-4)"><span style="font-size:17px">Weekly goal</span>
<span class="hao-stepper" data-min="1" data-max="20" role="group" aria-label="Weekly goal"><button aria-label="Decrease"><i class="hao-icon hao-icon--minus" aria-hidden="true"></i></button><output>5</output><button aria-label="Increase"><i class="hao-icon hao-icon--plus" aria-hidden="true"></i></button></span><span style="font-size:15px;color:var(--hao-ink-secondary)">notes</span></div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-4)"><span style="font-size:17px">每周目标</span>
<span class="hao-stepper" data-min="1" data-max="20" role="group" aria-label="每周目标"><button aria-label="减少"><i class="hao-icon hao-icon--minus" aria-hidden="true"></i></button><output>5</output><button aria-label="增加"><i class="hao-icon hao-icon--plus" aria-hidden="true"></i></button></span><span style="font-size:15px;color:var(--hao-ink-secondary)">条</span></div>
```
