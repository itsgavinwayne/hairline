# Tabs

Tabs within a page, for switching among blocks of content at the same level; mostly for medium and wide screens.

`.hao-tabs` takes `role="tablist"`, holding any number of `.hao-tabs__item`s (`role="tab"`), with `aria-selected="true"` on the current one. For navigation between pages, use links with `aria-current="page"` instead. You supply the text.

- The split with the segmented control: a segmented control switches views of the same content (day, week, month); tabs switch to different content (essays, reading).
- The current item is bold `ink`, with one `tint`-colored horizontal stroke (横) beneath: heavy where it starts, light where it ends, like a stroke written with a brush—not a straight line of even weight.
- When they don’t fit, scroll sideways: no wrapping, no tucking them into “More”.
- The arrow keys move between tabs; Tab enters the content below.
- Top-level navigation on narrow screens still uses the tab bar.

**Behavior** (when the behavior script is loaded)

- Each tab points to its panel with `aria-controls` (`<div class="hao-tabs__panel" role="tabpanel">`). Tap a tab, and its panel shows while the others hide.
- A tab group holds a single Tab stop. The left and right arrow keys move between tabs and switch at once, wrapping from end to end; Home and End jump to the first and last; Tab then enters the panel below.
- On each switch, the tabs fire a `hao-change` event. Link-style tabs used for page navigation are not taken over by the script.

## Markup

### English

```html
<div style="max-width:520px"><div class="hao-tabs" role="tablist" aria-label="Category"><button class="hao-tabs__item" role="tab" id="tb0-en" aria-selected="true" aria-controls="tp0-en">All</button><button class="hao-tabs__item" role="tab" id="tb1-en" aria-selected="false" aria-controls="tp1-en">Essays</button><button class="hao-tabs__item" role="tab" id="tb2-en" aria-selected="false" aria-controls="tp2-en">Reading</button><button class="hao-tabs__item" role="tab" id="tb3-en" aria-selected="false" aria-controls="tp3-en">Work</button></div><div class="hao-tabs__panel" role="tabpanel" id="tp0-en" aria-labelledby="tb0-en" tabindex="0">All 38 notes.</div><div class="hao-tabs__panel" role="tabpanel" id="tp1-en" aria-labelledby="tb1-en" tabindex="0" hidden>17 essays.</div><div class="hao-tabs__panel" role="tabpanel" id="tp2-en" aria-labelledby="tb2-en" tabindex="0" hidden>12 reading notes.</div><div class="hao-tabs__panel" role="tabpanel" id="tp3-en" aria-labelledby="tb3-en" tabindex="0" hidden>9 work notes.</div></div>
```

### Chinese

```html
<div style="max-width:520px"><div class="hao-tabs" role="tablist" aria-label="分类"><button class="hao-tabs__item" role="tab" id="tb0-zh" aria-selected="true" aria-controls="tp0-zh">全部</button><button class="hao-tabs__item" role="tab" id="tb1-zh" aria-selected="false" aria-controls="tp1-zh">随笔</button><button class="hao-tabs__item" role="tab" id="tb2-zh" aria-selected="false" aria-controls="tp2-zh">读书</button><button class="hao-tabs__item" role="tab" id="tb3-zh" aria-selected="false" aria-controls="tp3-zh">工作</button></div><div class="hao-tabs__panel" role="tabpanel" id="tp0-zh" aria-labelledby="tb0-zh" tabindex="0">这里是全部札记，共 38 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp1-zh" aria-labelledby="tb1-zh" tabindex="0" hidden>随笔 17 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp2-zh" aria-labelledby="tb2-zh" tabindex="0" hidden>读书笔记 12 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp3-zh" aria-labelledby="tb3-zh" tabindex="0" hidden>工作记录 9 条。</div></div>
```
