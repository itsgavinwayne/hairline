# Stepper · 步进器

用加减按钮一步一步调整一个小数字。

`.hao-stepper` 里依次是减号按钮、`<output>`、加号按钮。两个按钮都要有 `aria-label`。数值由你提供。

- 适合 1 到 20 这样的小范围；更大的范围用输入框。
- 到了上下限，对应的按钮加 `disabled`。
- 单位写在控件外面（「条」），不塞进数字里。
- 长按连续加减。

**行为**（加载了行为脚本时）

- 加减按钮可用。用 `data-min`、`data-max`、`data-step` 定范围和步长；到了头，对应的按钮自动禁用。
- 按住不放会连续加减。每次变化发出 `hao-change` 事件。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-4)"><span style="font-size:17px">每周目标</span>
<span class="hao-stepper" data-min="1" data-max="20" role="group" aria-label="每周目标"><button aria-label="减少"><i class="hao-icon hao-icon--minus" aria-hidden="true"></i></button><output>5</output><button aria-label="增加"><i class="hao-icon hao-icon--plus" aria-hidden="true"></i></button></span><span style="font-size:15px;color:var(--hao-ink-secondary)">条</span></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-4)"><span style="font-size:17px">Weekly goal</span>
<span class="hao-stepper" data-min="1" data-max="20" role="group" aria-label="Weekly goal"><button aria-label="Decrease"><i class="hao-icon hao-icon--minus" aria-hidden="true"></i></button><output>5</output><button aria-label="Increase"><i class="hao-icon hao-icon--plus" aria-hidden="true"></i></button></span><span style="font-size:15px;color:var(--hao-ink-secondary)">notes</span></div>
```
