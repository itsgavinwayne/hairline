# SampleSettings · Settings page (Chinese)

A sample settings page, used to check the rule that “task screens carry no decoration”—not a reusable component.

The screen carries no patterns, vignettes, or display pieces. Only four things hold a traditional flavor, all of them shapes of the controls themselves: the large Song typeface title, the surname-seal avatar, the hollow knob of the switch, the graduations of the storage bar. The only cinnabar is the small seal in the “Signature seal” row.

## Markup

### English

```html
<div class="phone"><div class="scroll">
  <h1 style="margin:var(--hao-space-4) 0 0;font:700 32px/40px var(--hao-font-serif);letter-spacing:-.015em;font-size:34px;font-weight:600">Me</h1>
  <ul class="hao-list"><li><a class="hao-list__row" href="#" style="padding:var(--hao-space-4)"><span class="hao-avatar hao-avatar--lg" aria-hidden="true">LW</span><span class="hao-list__title" style="font-weight:600">Lin Wan<span class="hao-list__sub">38 notes written</span></span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul>
  <div><p class="hao-list-header">General</p><ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">Appearance</span><span class="hao-list__value">System</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">Text size</span><span class="hao-list__value">Default</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><label class="hao-list__row hao-switch" style="display:flex"><span class="hao-list__title">Daily reminder</span><input type="checkbox" role="switch" checked></label></li>
    <li><label class="hao-list__row hao-switch" style="display:flex"><span class="hao-list__title">iCloud sync</span><input type="checkbox" role="switch"></label></li>
  </ul></div>
  <div><p class="hao-list-header">Storage</p><ul class="hao-list"><li><div class="hao-list__row" style="display:block;padding:var(--hao-space-4)"><div style="display:flex;justify-content:space-between;margin-bottom:var(--hao-space-3)"><span>4 GB used</span><span class="hao-list__value">10 GB total</span></div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="Storage" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div></div></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">Manage storage</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul></div>
  <div><ul class="hao-list"><li><a class="hao-list__row" href="#"><span class="hao-list__title">Signature seal</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-label="Seal">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">About</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul><p class="hao-list-footer">Interface built on the Hairline design system</p></div>
</div><nav class="hao-tabbar tabs" aria-label="Main"><a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a><a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes</a><a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>Me</a></nav></div>
```

### Chinese

```html
<div class="phone"><div class="scroll">
  <h1 style="margin:var(--hao-space-4) 0 0;font:700 32px/40px var(--hao-font-serif);letter-spacing:.02em">我的</h1>
  <ul class="hao-list"><li><a class="hao-list__row" href="#" style="padding:var(--hao-space-4)"><span class="hao-avatar hao-avatar--lg hao-avatar--name" aria-hidden="true">林</span><span class="hao-list__title" style="font-weight:600">林晚<span class="hao-list__sub">已写 38 条札记</span></span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul>
  <div><p class="hao-list-header">通用</p><ul class="hao-list">
    <li><a class="hao-list__row" href="#"><span class="hao-list__title">外观</span><span class="hao-list__value">跟随系统</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">字号</span><span class="hao-list__value">标准</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
    <li><label class="hao-list__row hao-switch" style="display:flex"><span class="hao-list__title">每日提醒</span><input type="checkbox" role="switch" checked></label></li>
    <li><label class="hao-list__row hao-switch" style="display:flex"><span class="hao-list__title">同步到 iCloud</span><input type="checkbox" role="switch"></label></li>
  </ul></div>
  <div><p class="hao-list-header">存储</p><ul class="hao-list"><li><div class="hao-list__row" style="display:block;padding:var(--hao-space-4)"><div style="display:flex;justify-content:space-between;margin-bottom:var(--hao-space-3)"><span>已用 4 GB</span><span class="hao-list__value">共 10 GB</span></div><div class="hao-progress hao-progress--ke" role="progressbar" aria-label="存储空间" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><span style="--v:40%"></span></div></div></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">管理存储空间</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul></div>
  <div><ul class="hao-list"><li><a class="hao-list__row" href="#"><span class="hao-list__title">落款印章</span><span class="hao-seal hao-seal--sm hao-seal--outline" aria-hidden="true">印</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li><li><a class="hao-list__row" href="#"><span class="hao-list__title">关于</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li></ul><p class="hao-list-footer">界面基于 Hairline 设计系统</p></div>
</div><nav class="hao-tabbar tabs" aria-label="主导航"><a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a><a class="hao-tabbar__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记</a><a class="hao-tabbar__item" href="#" aria-current="page"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>我的</a></nav></div>
```
