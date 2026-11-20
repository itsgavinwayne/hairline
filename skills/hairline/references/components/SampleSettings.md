# SampleSettings · 设置页

设置页的示例，用来检验「功能页不放装饰」这条规则，不是可复用的组件。

整屏没有纹样、小品和内容展示件。带传统意味的只有四处，都是控件本身的形状：宋体大标题、姓氏章头像、开关的空心滑块、存储条的刻度。唯一的朱砂是「落款印章」那一行里的小印。

## 标记

### 中文

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
