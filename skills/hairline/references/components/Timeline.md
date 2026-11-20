# Timeline · 时间线

按时间先后列出的一串事件，每个节点是一轮月。

`<ol class="hao-timeline">`，每个 `<li>` 里是一个 `.hao-moon`、`.hao-timeline__title`、`.hao-timeline__meta`，和可选的 `.hao-timeline__body`。当前的一项加 `aria-current="step"`。

- 月相就是状态：做完的是满月（`--p:1` 加 `hao-moon--done`，竹青色），进行中的是半月（`--p:.5`），没开始的是空月（`--p:0`）。知道确切进度时可以写真实的值。
- 状态同时写在 `meta` 里（「已完成」「进行中」），不只靠月相和颜色。
- 最新的在上还是在下，全产品统一。记录类（操作历史）新的在上，计划类（项目进度）早的在上。
- 每项的标题是一个名词短语，说明至多两行。
- 横向的、步骤很少的流程用步骤条。
- 日期后面可以跟一个泥金色的小字 `.hao-timeline__lunar`，写农历日或节气（「十月初一」「小雪」）。用历法数据生成，不要手写；英文界面不加。

## 标记

### 中文

```html
<ol class="hao-timeline" style="max-width:420px">
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">写完初稿</p><p class="hao-timeline__meta">11 月 9 日，已完成<span class="hao-timeline__lunar">十月初一</span></p><p class="hao-timeline__body">共 2,140 字，分三节。</p></li>
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">配图</p><p class="hao-timeline__meta">11 月 12 日，已完成<span class="hao-timeline__lunar">十月初四</span></p></li>
  <li aria-current="step"><span class="hao-moon" style="--p:.5" aria-hidden="true"></span><p class="hao-timeline__title">修改</p><p class="hao-timeline__meta">进行中</p><p class="hao-timeline__body">第二节还要补一段引文。</p></li>
  <li><span class="hao-moon" style="--p:0" aria-hidden="true"></span><p class="hao-timeline__title">发布</p><p class="hao-timeline__meta">计划在 11 月 22 日<span class="hao-timeline__lunar">小雪</span></p></li>
</ol>
```

### English

```html
<ol class="hao-timeline" style="max-width:420px">
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">Finish the first draft</p><p class="hao-timeline__meta">Nov 9, done</p><p class="hao-timeline__body">2,140 words in three sections.</p></li>
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">Add images</p><p class="hao-timeline__meta">Nov 12, done</p></li>
  <li aria-current="step"><span class="hao-moon" style="--p:.5" aria-hidden="true"></span><p class="hao-timeline__title">Revise</p><p class="hao-timeline__meta">In progress</p><p class="hao-timeline__body">Section two still needs a quotation.</p></li>
  <li><span class="hao-moon" style="--p:0" aria-hidden="true"></span><p class="hao-timeline__title">Publish</p><p class="hao-timeline__meta">Planned for Nov 22</p></li>
</ol>
```
