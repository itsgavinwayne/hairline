# Bookmark · 书签

收藏的开关，样子是一盏挂着的灯：没收藏时是一盏空灯，收藏了就点亮。

`<button class="hao-lamp" aria-pressed="true|false" aria-label="…">`。放进 `Card` 里会自动挂在右上角，从卡片顶边垂下来。

- 灯只画四样：提绳、灯盖、灯身、穗子，都是细线。没收藏时灯身是一圈灰色的轮廓，收藏后填上 `tint`。
- 状态靠实心和空心区分，不只靠颜色。
- 按钮本身 44px 见方，灯只占中间一条，手指点得准。
- `aria-label` 写点下去会发生什么：没收藏时写「收藏」，已收藏时写「取消收藏」。
- 用它，不用星星和心形。一张卡片上有灯就不再放印章。
- 不用朱砂色，也不画成红灯笼。它是使用者自己的标记，不是节庆的装饰，也不是系统的提醒。
- 一屏里可以有很多盏：它是控件自己的形，算在「形随控件」里，不算景。

**行为**（加载了行为脚本时）

- 加 `data-hao-toggle`，点一下在收藏和未收藏之间切换。再加 `data-label-on` 和 `data-label-off`，无障碍标签会跟着换（「取消收藏」「收藏」）。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="取消收藏" data-label-off="收藏" aria-pressed="true" aria-label="取消收藏"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">晨间札记</h3><p class="hao-card__body">窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p></div>
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="取消收藏" data-label-off="收藏" aria-pressed="false" aria-label="收藏"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">苏州三日</h3><p class="hao-card__body">第一天只看了一座园子。走得慢，才发现每一扇窗框住的都是一幅画。</p></div>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="Remove bookmark" data-label-off="Bookmark" aria-pressed="true" aria-label="Remove bookmark"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">Morning note</h3><p class="hao-card__body">Fog outside the window. Write down the three things that matter today, and let the rest wait.</p></div>
<div class="hao-card" style="width:300px"><button class="hao-lamp" data-hao-toggle data-label-on="Remove bookmark" data-label-off="Bookmark" aria-pressed="false" aria-label="Bookmark"></button><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">Three days in Suzhou</h3><p class="hao-card__body">We saw one garden on the first day. Walking slowly, I noticed that every window frames a painting.</p></div>
</div>
```
