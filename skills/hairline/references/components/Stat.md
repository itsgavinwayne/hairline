# Stat · 数字展示

把一个重要的数字放大了摆出来。

`.hao-stat` 里依次是 `.hao-stat__l`（这是什么）、`.hao-stat__v`（数字，单位放进 `<small>`）、可选的 `.hao-stat__n`（一句比较或补充）。

- 数字用宋体、等宽数字；单位是跟在后面的小号黑体（条、字、天）。中文里量词是数字的一部分，不要省。
- 一排最多四个，每个只说一件事。
- 补充的那句写成话（「比上月多 6 条」），不用上下箭头加百分比，也不用红绿色表示涨跌。
- 千位用逗号分隔。过万时可以写「4.8 万」，全产品统一一种写法。
- 数字不是重点的地方，用列表行右侧的值就够了。

**无障碍**

- 标签、数字、补充句都是普通文字，DOM 顺序就是朗读顺序：先听到这是什么，再听到多少。
- 单位放在 `<small>` 里，跟着数字连着读；组件里没有可点的东西，不涉及键盘。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-start">
  <div class="hao-stat"><span class="hao-stat__l">本月札记</span><span class="hao-stat__v">31<small>条</small></span><span class="hao-stat__n">比上月多 6 条</span></div>
  <div class="hao-stat"><span class="hao-stat__l">累计字数</span><span class="hao-stat__v">48,260<small>字</small></span></div>
  <div class="hao-stat"><span class="hao-stat__l">连续记录</span><span class="hao-stat__v">12<small>天</small></span><span class="hao-stat__n">最长 27 天</span></div>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-start">
  <div class="hao-stat"><span class="hao-stat__l">Notes this month</span><span class="hao-stat__v">31<small>notes</small></span><span class="hao-stat__n">6 more than last month</span></div>
  <div class="hao-stat"><span class="hao-stat__l">Total words</span><span class="hao-stat__v">48,260<small>words</small></span></div>
  <div class="hao-stat"><span class="hao-stat__l">Current streak</span><span class="hao-stat__v">12<small>days</small></span><span class="hao-stat__n">Longest: 27 days</span></div>
</div>
```
