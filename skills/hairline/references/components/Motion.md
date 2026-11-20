# Motion · 进场动效

浮层出现时的几种进场方式，各对应一种浮层；另有一个「点灯」，属于书签。点「重播」再看一次。

| 类名 | 名字 | 样子 | 给谁用 |
| --- | --- | --- | --- |
| `hao-sheet--enter` | 展卷 | 从底边向上展开，像一轴画由下而上打开；里面的内容稍后淡入 | 底部弹层 |
| `hao-dialog--enter` | 定 | 原地淡入，从 96% 放大到位 | 弹窗 |
| `hao-menu--enter` | 卷帘 | 像放下一挂竹帘：从贴着按钮的那一边展开，里面的各项稍后淡入。菜单翻到按钮上方时加 `hao-menu--up`，改成向上卷 | 菜单 |
| `hao-lamp--lit` | 点灯 | 灯身亮起，整盏灯轻轻摆两下再停住 | 书签，收藏的那一刻 |
| `hao-toast--enter` | 浮起 | 从下方 12px 处浮上来并淡入 | 轻提示、气泡提示 |
| `hao-scrim--enter` | 淡入 | 遮罩淡入 | 弹层和弹窗背后的遮罩 |

- 展卷是这套系统自己的进场：底部弹层不是整块滑上来，而是原地由下而上展开。时长 320 毫秒，快起慢停。
- 进场把这些类加到浮层上；离场反向播放，时长取进场的三分之二。
- 一次只有一个浮层在动。遮罩和浮层同时开始。
- 「盖印」是另一种动效，只属于完成时刻，见 `Stamp`。
- 系统开启「减弱动态效果」时，所有进场都取消，浮层直接出现。
- 不给页面里的普通内容加进场动效：卡片、列表、标题都是直接在那里的。
- 点灯和盖印一样，只在使用者做了那个动作的一刻播一次；页面打开时已经亮着的灯不动。

**无障碍**

- 进场动效不承载信息：浮层的出现和消失由 `hidden` 属性决定，动效停了内容照样到位。
- 「减弱动态效果」由样式表统一接管，你不用在自己的代码里再判一遍。
- 轻提示要能自己播出来：预览里它带 `role="status"`；加载行为脚本后，真的轻提示进 `aria-live` 礼貌播报区，不抢焦点。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-start">
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">展卷</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div class="hao-scrim hao-scrim--bottom hao-scrim--enter" id="ms1" style="position:absolute;inset:0"><div class="hao-sheet hao-sheet--enter" id="mh1"><div class="hao-sheet__grabber" aria-hidden="true"></div><h2 class="hao-sheet__title">晨间札记</h2><ul class="hao-list"><li><a class="hao-list__row" href="#"><span class="hao-list__title">分享</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">移到文件夹</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul></div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="ms1:hao-scrim--enter,mh1:hao-sheet--enter">重播</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">定</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div class="hao-scrim hao-scrim--enter" id="md1" style="position:absolute;inset:0;padding:var(--hao-space-4)"><div class="hao-dialog hao-dialog--enter" id="mg1"><h2 class="hao-dialog__title">删除这条札记</h2><p class="hao-dialog__body">删除后无法恢复。</p><div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted" style="min-width:0">取消</button><button class="hao-btn hao-btn--seal" style="min-width:0">删除</button></div></div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="md1:hao-scrim--enter,mg1:hao-dialog--enter">重播</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">浮起</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div style="position:absolute;left:0;right:0;bottom:var(--hao-space-5);display:flex;justify-content:center"><div class="hao-toast hao-toast--enter" id="mt1" role="status">已保存</div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="mt1:hao-toast--enter">重播</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">卷帘</p><div style="position:relative;box-sizing:border-box;width:280px;height:300px;padding:var(--hao-space-4);border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><span class="hao-btn hao-btn--sm hao-btn--tinted" aria-hidden="true">更多操作</span><ul class="hao-menu hao-menu--enter" id="mm1" role="menu" style="margin-top:var(--hao-space-2);width:220px"><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">分享</button></li><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">移到文件夹</button></li><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">复制一份</button></li></ul></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="mm1:hao-menu--enter">重播</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">点灯</p><div style="position:relative;box-sizing:border-box;width:280px;height:300px;padding:var(--hao-space-4);border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div class="hao-card" style="margin-top:var(--hao-space-2)"><span class="hao-lamp hao-lamp--lit" id="ml1" aria-pressed="true" role="img" aria-label="已收藏"></span><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">晨间札记</h3><p class="hao-card__body">窗外起了薄雾。</p></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="ml1:hao-lamp--lit">重播</button></div>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5);align-items:flex-start">
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Unroll</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div class="hao-scrim hao-scrim--bottom hao-scrim--enter" id="ms2" style="position:absolute;inset:0"><div class="hao-sheet hao-sheet--enter" id="mh2"><div class="hao-sheet__grabber" aria-hidden="true"></div><h2 class="hao-sheet__title">Morning note</h2><ul class="hao-list"><li><a class="hao-list__row" href="#"><span class="hao-list__title">Share</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">Move to folder</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul></div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="ms2:hao-scrim--enter,mh2:hao-sheet--enter">Replay</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Settle</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div class="hao-scrim hao-scrim--enter" id="md2" style="position:absolute;inset:0;padding:var(--hao-space-4)"><div class="hao-dialog hao-dialog--enter" id="mg2"><h2 class="hao-dialog__title">Delete this note</h2><p class="hao-dialog__body">This can’t be undone.</p><div class="hao-dialog__actions"><button class="hao-btn hao-btn--tinted" style="min-width:0">Cancel</button><button class="hao-btn hao-btn--seal" style="min-width:0">Delete</button></div></div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="md2:hao-scrim--enter,mg2:hao-dialog--enter">Replay</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Rise</p><div style="position:relative;width:280px;height:300px;border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div style="position:absolute;inset:0;padding:var(--hao-space-4);display:flex;flex-direction:column;gap:var(--hao-space-3)" aria-hidden="true"><div style="height:32px;width:100px;border-radius:var(--hao-radius-sm);background:var(--hao-surface-sunken)"></div><div style="flex:1;border-radius:var(--hao-radius-lg);background:var(--hao-surface)"></div></div><div style="position:absolute;left:0;right:0;bottom:var(--hao-space-5);display:flex;justify-content:center"><div class="hao-toast hao-toast--enter" id="mt2" role="status">Saved</div></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="mt2:hao-toast--enter">Replay</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Blind</p><div style="position:relative;box-sizing:border-box;width:280px;height:300px;padding:var(--hao-space-4);border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><span class="hao-btn hao-btn--sm hao-btn--tinted" aria-hidden="true">More actions</span><ul class="hao-menu hao-menu--enter" id="mm2" role="menu" style="margin-top:var(--hao-space-2);width:220px"><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">Share</button></li><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">Move to folder</button></li><li role="none"><button class="hao-menu__item" role="menuitem" tabindex="-1">Duplicate</button></li></ul></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="mm2:hao-menu--enter">Replay</button></div>
  <div><p style="margin:0 0 var(--hao-space-2);font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Lighting</p><div style="position:relative;box-sizing:border-box;width:280px;height:300px;padding:var(--hao-space-4);border-radius:var(--hao-radius-xl);background:var(--hao-bg);overflow:hidden;border:1px solid var(--hao-hairline)"><div class="hao-card" style="margin-top:var(--hao-space-2)"><span class="hao-lamp hao-lamp--lit" id="ml2" aria-pressed="true" role="img" aria-label="Saved"></span><h3 class="hao-card__title" style="padding-right:var(--hao-space-8)">Morning note</h3><p class="hao-card__body">Fog outside the window.</p></div></div>
    <button class="hao-btn hao-btn--sm hao-btn--tinted" style="margin-top:var(--hao-space-3)" data-replay="ml2:hao-lamp--lit">Replay</button></div>
</div>
```

## 这个示例自己带的脚本

```html
<script>document.querySelectorAll("[data-replay]").forEach(function (b) { b.addEventListener("click", function () { b.getAttribute("data-replay").split(",").forEach(function (pair) { var p = pair.split(":"), el = document.getElementById(p[0]); el.classList.remove(p[1]); void el.offsetWidth; el.classList.add(p[1]); }); }); });</script>
```
