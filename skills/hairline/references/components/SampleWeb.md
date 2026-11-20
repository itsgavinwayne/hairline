# SampleWeb · 网页

宽屏网页的示例，展示这套系统离开手机之后的样子，不是可复用的组件。

它示范了：12 列栅格，主内容占 8 列、侧栏占 4 列；标签栏在宽屏上换成顶部导航，仍用 `material` 毛玻璃；同一份数据在宽屏上用表格；宋体大标题下压一道回纹，是这一屏唯一的纹样；左上角一方小印是唯一的朱砂；主按钮只有一个。

## 标记

### 中文

```html
<header class="top"><div class="hao-page bar">
  <a class="brand" href="#"><span class="hao-seal hao-seal--sm" aria-hidden="true">印</span>产品名</a>
  <nav class="hao-tabs links" aria-label="主导航"><a class="hao-tabs__item" href="#" aria-current="page">札记</a><a class="hao-tabs__item" href="#">今日</a><a class="hao-tabs__item" href="#">文件夹</a></nav>
  <label class="hao-search" style="width:260px"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="搜索札记" aria-label="搜索札记"></label>
</div></header>
<main class="hao-page" style="padding-bottom:var(--hao-space-12)">
  <div class="head"><div><h1>札记</h1><p>共 38 条，本周新增 3 条</p></div><button class="hao-btn">写一条札记</button></div>
  <div class="hao-fret" role="presentation" style="width:120px;margin-bottom:var(--hao-space-8)"></div>
  <div class="hao-grid">
    <section style="grid-column:span 8">
      <div class="hao-tabs" role="tablist" style="margin-bottom:var(--hao-space-5)"><button class="hao-tabs__item" role="tab" aria-selected="true">全部</button><button class="hao-tabs__item" role="tab" aria-selected="false">随笔</button><button class="hao-tabs__item" role="tab" aria-selected="false">读书</button><button class="hao-tabs__item" role="tab" aria-selected="false">旅行</button></div>
      <div class="hao-table-wrap"><table class="hao-table">
        <thead><tr><th scope="col">标题</th><th scope="col">文件夹</th><th scope="col">状态</th><th scope="col" class="hao-num">字数</th><th scope="col">上次编辑</th></tr></thead>
        <tbody>
          <tr><td>晨间札记</td><td class="hao-muted">随笔</td><td><span class="hao-tag hao-tag--jade">已发布</span></td><td class="hao-num">486</td><td class="hao-muted">今天 07:12</td></tr>
          <tr><td>《园冶》读书笔记</td><td class="hao-muted">读书</td><td><span class="hao-tag hao-tag--tint">进行中</span></td><td class="hao-num">2,140</td><td class="hao-muted">昨天</td></tr>
          <tr><td>苏州三日</td><td class="hao-muted">旅行</td><td><span class="hao-tag">草稿</span></td><td class="hao-num">912</td><td class="hao-muted">11 月 12 日</td></tr>
          <tr><td>入冬的第一场雨</td><td class="hao-muted">随笔</td><td><span class="hao-tag hao-tag--jade">已发布</span></td><td class="hao-num">327</td><td class="hao-muted">11 月 9 日</td></tr>
          <tr><td>年度书单</td><td class="hao-muted">读书</td><td><span class="hao-tag hao-tag--amber">今天到期</span></td><td class="hao-num">1,058</td><td class="hao-muted">11 月 3 日</td></tr>
        </tbody></table></div>
    </section>
    <aside style="grid-column:span 4;display:flex;flex-direction:column;gap:var(--hao-gutter)">
      <div class="hao-card"><h2 class="hao-card__title">本周</h2><p class="hao-card__body">写了 3 条，共 1,725 字。</p><div class="hao-progress" role="progressbar" aria-label="本周目标" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="margin-top:var(--hao-space-4)"><span style="--v:60%"></span></div><p class="hao-card__meta" style="margin-top:var(--hao-space-2)">周目标 5 条，已完成 3 条</p></div>
      <div><p class="hao-list-header">文件夹</p><ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">随笔</span><span class="hao-list__value">17</span></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">读书</span><span class="hao-list__value">12</span></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">旅行</span><span class="hao-list__value">9</span></a></li>
      </ul></div>
    </aside>
  </div>
</main>
```

### English

```html
<header class="top"><div class="hao-page bar">
  <a class="brand" href="#"><span class="hao-seal hao-seal--sm" lang="zh" aria-hidden="true">印</span>Product name</a>
  <nav class="hao-tabs links" aria-label="Main"><a class="hao-tabs__item" href="#" aria-current="page">Notes</a><a class="hao-tabs__item" href="#">Today</a><a class="hao-tabs__item" href="#">Folders</a></nav>
  <label class="hao-search" style="width:260px"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="Search notes" aria-label="Search notes"></label>
</div></header>
<main class="hao-page" style="padding-bottom:var(--hao-space-12)">
  <div class="head"><div><h1>Notes</h1><p>38 notes, 3 new this week</p></div><button class="hao-btn">Write a note</button></div>
  <div class="hao-fret" role="presentation" style="width:120px;margin-bottom:var(--hao-space-8)"></div>
  <div class="hao-grid">
    <section style="grid-column:span 8">
      <div class="hao-tabs" role="tablist" style="margin-bottom:var(--hao-space-5)"><button class="hao-tabs__item" role="tab" aria-selected="true">All</button><button class="hao-tabs__item" role="tab" aria-selected="false">Essays</button><button class="hao-tabs__item" role="tab" aria-selected="false">Reading</button><button class="hao-tabs__item" role="tab" aria-selected="false">Travel</button></div>
      <div class="hao-table-wrap"><table class="hao-table">
        <thead><tr><th scope="col">Title</th><th scope="col">Folder</th><th scope="col">Status</th><th scope="col" class="hao-num">Words</th><th scope="col">Last edited</th></tr></thead>
        <tbody>
          <tr><td>Morning note</td><td class="hao-muted">Essays</td><td><span class="hao-tag hao-tag--jade">Published</span></td><td class="hao-num">486</td><td class="hao-muted">Today, 7:12 AM</td></tr>
          <tr><td>Notes on The Craft of Gardens</td><td class="hao-muted">Reading</td><td><span class="hao-tag hao-tag--tint">In progress</span></td><td class="hao-num">2,140</td><td class="hao-muted">Yesterday</td></tr>
          <tr><td>Three days in Suzhou</td><td class="hao-muted">Travel</td><td><span class="hao-tag">Draft</span></td><td class="hao-num">912</td><td class="hao-muted">Nov 12</td></tr>
          <tr><td>First rain of winter</td><td class="hao-muted">Essays</td><td><span class="hao-tag hao-tag--jade">Published</span></td><td class="hao-num">327</td><td class="hao-muted">Nov 9</td></tr>
          <tr><td>Books of the year</td><td class="hao-muted">Reading</td><td><span class="hao-tag hao-tag--amber">Due today</span></td><td class="hao-num">1,058</td><td class="hao-muted">Nov 3</td></tr>
        </tbody></table></div>
    </section>
    <aside style="grid-column:span 4;display:flex;flex-direction:column;gap:var(--hao-gutter)">
      <div class="hao-card"><h2 class="hao-card__title">This week</h2><p class="hao-card__body">3 notes, 1,725 words.</p><div class="hao-progress" role="progressbar" aria-label="Weekly goal" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="margin-top:var(--hao-space-4)"><span style="--v:60%"></span></div><p class="hao-card__meta" style="margin-top:var(--hao-space-2)">3 of 5 notes toward the weekly goal</p></div>
      <div><p class="hao-list-header">Folders</p><ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Essays</span><span class="hao-list__value">17</span></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Reading</span><span class="hao-list__value">12</span></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Travel</span><span class="hao-list__value">9</span></a></li>
      </ul></div>
    </aside>
  </div>
</main>
```
