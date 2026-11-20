# Tabs · 标签页

页面内的标签页，在同一层级的几块内容之间切换，主要用在中屏和宽屏。

`.hao-tabs` 加 `role="tablist"`，里面是若干 `.hao-tabs__item`（`role="tab"`），当前项 `aria-selected="true"`。作页面间导航时改用链接和 `aria-current="page"`。文字由你提供。

- 和分段控件的分工：分段控件切换同一份内容的看法（日、周、月），标签页切换不同的内容（随笔、读书）。
- 当前项是 `ink` 加粗，下面一笔 `tint` 色的「横」：起笔重，收笔轻，像毛笔写的一横，不是等粗的直线。
- 放不下时横向滚动，不换行，不收进「更多」。
- 方向键在标签之间移动，Tab 键进入下面的内容。
- 窄屏的顶层导航仍用标签栏。

**行为**（加载了行为脚本时）

- 每个标签用 `aria-controls` 指向它的面板（`<div class="hao-tabs__panel" role="tabpanel">`）。点标签，对应的面板显示，其余隐藏。
- 一组标签只占一个 Tab 停靠点。左右方向键在标签间移动并立即切换，首尾循环；Home 和 End 跳到头尾；再按 Tab 进入下面的面板。
- 切换时标签会发出 `hao-change` 事件。作页面导航用的链接式标签不受脚本接管。

## 标记

### 中文

```html
<div style="max-width:520px"><div class="hao-tabs" role="tablist" aria-label="分类"><button class="hao-tabs__item" role="tab" id="tb0-zh" aria-selected="true" aria-controls="tp0-zh">全部</button><button class="hao-tabs__item" role="tab" id="tb1-zh" aria-selected="false" aria-controls="tp1-zh">随笔</button><button class="hao-tabs__item" role="tab" id="tb2-zh" aria-selected="false" aria-controls="tp2-zh">读书</button><button class="hao-tabs__item" role="tab" id="tb3-zh" aria-selected="false" aria-controls="tp3-zh">工作</button></div><div class="hao-tabs__panel" role="tabpanel" id="tp0-zh" aria-labelledby="tb0-zh" tabindex="0">这里是全部札记，共 38 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp1-zh" aria-labelledby="tb1-zh" tabindex="0" hidden>随笔 17 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp2-zh" aria-labelledby="tb2-zh" tabindex="0" hidden>读书笔记 12 条。</div><div class="hao-tabs__panel" role="tabpanel" id="tp3-zh" aria-labelledby="tb3-zh" tabindex="0" hidden>工作记录 9 条。</div></div>
```

### English

```html
<div style="max-width:520px"><div class="hao-tabs" role="tablist" aria-label="Category"><button class="hao-tabs__item" role="tab" id="tb0-en" aria-selected="true" aria-controls="tp0-en">All</button><button class="hao-tabs__item" role="tab" id="tb1-en" aria-selected="false" aria-controls="tp1-en">Essays</button><button class="hao-tabs__item" role="tab" id="tb2-en" aria-selected="false" aria-controls="tp2-en">Reading</button><button class="hao-tabs__item" role="tab" id="tb3-en" aria-selected="false" aria-controls="tp3-en">Work</button></div><div class="hao-tabs__panel" role="tabpanel" id="tp0-en" aria-labelledby="tb0-en" tabindex="0">All 38 notes.</div><div class="hao-tabs__panel" role="tabpanel" id="tp1-en" aria-labelledby="tb1-en" tabindex="0" hidden>17 essays.</div><div class="hao-tabs__panel" role="tabpanel" id="tp2-en" aria-labelledby="tb2-en" tabindex="0" hidden>12 reading notes.</div><div class="hao-tabs__panel" role="tabpanel" id="tp3-en" aria-labelledby="tb3-en" tabindex="0" hidden>9 work notes.</div></div>
```
