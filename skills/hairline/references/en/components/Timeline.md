# Timeline

A run of events in time order, each node a phase of the moon.

An `<ol class="hao-timeline">`; each `<li>` holds a `.hao-moon`, the `.hao-timeline__title`, the `.hao-timeline__meta`, and an optional `.hao-timeline__body`. The current item takes `aria-current="step"`.

- The moon phase is the state: finished is a full moon (`--p:1` with `hao-moon--done`, in bamboo green), in progress a half moon (`--p:.5`), not started an empty moon (`--p:0`). When you know the exact progress, write the true value.
- The state also appears in the `meta` (“Done”, “In progress”), not just in the moon and the color.
- Newest on top or on bottom—settle on one across the product. Logs (an action history) put the newest on top; plans (project progress) put the earliest on top.
- Each item’s title is a noun phrase, its description at most two lines.
- A horizontal flow with only a few steps uses steps instead.
- After the date can come a small gold-ink line, `.hao-timeline__lunar`, holding the lunar date or the solar term (“十月初一”, “Minor Snow (小雪)”). Generate it from calendar data—never write it by hand. English interfaces leave it out.

## Markup

### English

```html
<ol class="hao-timeline" style="max-width:420px">
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">Finish the first draft</p><p class="hao-timeline__meta">Nov 9, done</p><p class="hao-timeline__body">2,140 words in three sections.</p></li>
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">Add images</p><p class="hao-timeline__meta">Nov 12, done</p></li>
  <li aria-current="step"><span class="hao-moon" style="--p:.5" aria-hidden="true"></span><p class="hao-timeline__title">Revise</p><p class="hao-timeline__meta">In progress</p><p class="hao-timeline__body">Section two still needs a quotation.</p></li>
  <li><span class="hao-moon" style="--p:0" aria-hidden="true"></span><p class="hao-timeline__title">Publish</p><p class="hao-timeline__meta">Planned for Nov 22</p></li>
</ol>
```

### Chinese

```html
<ol class="hao-timeline" style="max-width:420px">
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">写完初稿</p><p class="hao-timeline__meta">11 月 9 日，已完成<span class="hao-timeline__lunar">十月初一</span></p><p class="hao-timeline__body">共 2,140 字，分三节。</p></li>
  <li><span class="hao-moon hao-moon--done" style="--p:1" aria-hidden="true"></span><p class="hao-timeline__title">配图</p><p class="hao-timeline__meta">11 月 12 日，已完成<span class="hao-timeline__lunar">十月初四</span></p></li>
  <li aria-current="step"><span class="hao-moon" style="--p:.5" aria-hidden="true"></span><p class="hao-timeline__title">修改</p><p class="hao-timeline__meta">进行中</p><p class="hao-timeline__body">第二节还要补一段引文。</p></li>
  <li><span class="hao-moon" style="--p:0" aria-hidden="true"></span><p class="hao-timeline__title">发布</p><p class="hao-timeline__meta">计划在 11 月 22 日<span class="hao-timeline__lunar">小雪</span></p></li>
</ol>
```
