Adjust a small number step by step with plus and minus buttons.

Inside `.hao-stepper`, in order: the minus button, an `<output>`, and the plus button. Both buttons need an `aria-label`. You supply the value.

- It suits small ranges like 1 to 20; for larger ranges use a text field.
- At either limit, the matching button gets `disabled`.
- Write the unit outside the control (“条”), not inside the number.
- Press and hold to keep stepping.

**Behavior** (when the behavior script is loaded)

- The plus and minus buttons work. Set the range and step with `data-min`, `data-max`, and `data-step`; at either end, the matching button disables itself.
- Press and hold to keep stepping. Each change fires a `hao-change` event.
