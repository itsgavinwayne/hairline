# SampleDashboard · Dashboard (Chinese)

A sample data-review screen (wide), used to check whether several motifs together fill the screen too much—not a reusable component.

On this screen the moon appears only once (this week’s seven moon phases); the calendar uses lunar text rather than moon phases, so the two moons don’t clash. The table header is a double rule, the current page number is a page-number seal, and status uses tags. There are no patterns; the only cinnabar is the small seal at the upper left.

## Markup

### English

```html
<header class="top"><div class="hao-page barw">
  <a class="brand" href="#"><span class="hao-seal hao-seal--sm" role="img" aria-label="Seal" lang="zh">印</span>Product name</a>
  <nav class="hao-tabs links" aria-label="Main"><a class="hao-tabs__item" href="#">Notes</a><a class="hao-tabs__item" href="#" aria-current="page">Review</a><a class="hao-tabs__item" href="#">Folders</a></nav>
  <label class="hao-search" style="width:260px"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="Search notes" aria-label="Search notes"></label>
</div></header>
<main class="hao-page" style="padding-bottom:var(--hao-space-12)">
  <div class="head"><h1>November review</h1><p>The tenth month of the Bingwu year, from Start of Winter (<span lang="zh">立冬</span>) to Minor Snow (<span lang="zh">小雪</span>)</p></div>
  <div class="hao-grid">
    <section class="hao-card" style="grid-column:span 8;display:flex;flex-wrap:wrap;gap:var(--hao-space-5) var(--hao-space-12);align-items:flex-start">
      <div class="hao-stat"><span class="hao-stat__l">Notes this month</span><span class="hao-stat__v">31<small>notes</small></span><span class="hao-stat__n">6 more than last month</span></div>
      <div class="hao-stat"><span class="hao-stat__l">Total words</span><span class="hao-stat__v">48,260<small>words</small></span></div>
      <div class="hao-stat"><span class="hao-stat__l">Current streak</span><span class="hao-stat__v">12<small>days</small></span><span class="hao-stat__n">Longest: 27 days</span></div>
    </section>
    <section class="hao-card" style="grid-column:span 4"><h2 class="hao-card__title">This week</h2><div class="hao-row" style="gap:var(--hao-space-2)"><span class="hao-moon hao-moon--done" style="--p:1" role="img" aria-label="Monday, done"></span><span class="hao-moon hao-moon--done" style="--p:1" role="img" aria-label="Tuesday, done"></span><span class="hao-moon" style="--p:0.6" role="img" aria-label="Wednesday, half done"></span><span class="hao-moon" style="--p:0" role="img" aria-label="Thursday"></span><span class="hao-moon" style="--p:0" role="img" aria-label="Friday"></span><span class="hao-moon" style="--p:0" role="img" aria-label="Saturday"></span><span class="hao-moon" style="--p:0" role="img" aria-label="Sunday"></span></div><p class="hao-card__meta">Weekly goal 5 notes, 2 and a half done</p></section>
    <section style="grid-column:span 8">
      <div class="hao-table-wrap"><table class="hao-table">
        <thead><tr><th scope="col">Title</th><th scope="col">Folder</th><th scope="col">Status</th><th scope="col" class="hao-num">Words</th><th scope="col">Last edited</th></tr></thead>
        <tbody>
          <tr><td>Morning note</td><td class="hao-muted">Essays</td><td><span class="hao-tag hao-tag--jade">Published</span></td><td class="hao-num">486</td><td class="hao-muted">Today, 7:12 AM</td></tr>
          <tr><td>Notes on The Craft of Gardens</td><td class="hao-muted">Reading</td><td><span class="hao-tag hao-tag--tint">In progress</span></td><td class="hao-num">2,140</td><td class="hao-muted">Yesterday</td></tr>
          <tr><td>Three days in Suzhou</td><td class="hao-muted">Travel</td><td><span class="hao-tag">Draft</span></td><td class="hao-num">912</td><td class="hao-muted">Nov 12</td></tr>
          <tr><td>First rain of winter</td><td class="hao-muted">Essays</td><td><span class="hao-tag hao-tag--jade">Published</span></td><td class="hao-num">327</td><td class="hao-muted">Nov 9</td></tr>
        </tbody></table></div>
      <nav aria-label="Pagination" style="margin-top:var(--hao-space-4);display:flex;justify-content:flex-end"><ul class="hao-pages"><li><a class="hao-pages__item" href="#" aria-label="Previous page" aria-disabled="true"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i></a></li><li><a class="hao-pages__item" href="#" aria-current="page">1</a></li><li><a class="hao-pages__item" href="#">2</a></li><li><a class="hao-pages__item" href="#">3</a></li><li><a class="hao-pages__item" href="#" aria-label="Next page"><i class="hao-icon hao-icon--chevron-right" aria-hidden="true"></i></a></li></ul></nav>
    </section>
    <aside style="grid-column:span 4"><div class="hao-cal" style="width:100%"><div class="hao-cal__head"><h2 class="hao-cal__title">November</h2></div><div class="hao-cal__grid"><span class="hao-cal__dow">M</span><span class="hao-cal__dow">T</span><span class="hao-cal__dow">W</span><span class="hao-cal__dow">T</span><span class="hao-cal__dow">F</span><span class="hao-cal__dow">S</span><span class="hao-cal__dow">S</span><button class="hao-cal__day hao-cal__day--out">26</button><button class="hao-cal__day hao-cal__day--out">27</button><button class="hao-cal__day hao-cal__day--out">28</button><button class="hao-cal__day hao-cal__day--out">29</button><button class="hao-cal__day hao-cal__day--out">30</button><button class="hao-cal__day hao-cal__day--out">31</button><button class="hao-cal__day">1</button><button class="hao-cal__day">2</button><button class="hao-cal__day">3</button><button class="hao-cal__day">4</button><button class="hao-cal__day">5</button><button class="hao-cal__day">6</button><button class="hao-cal__day">7<small class="hao-cal__dot"></small></button><button class="hao-cal__day">8</button><button class="hao-cal__day">9</button><button class="hao-cal__day">10</button><button class="hao-cal__day">11</button><button class="hao-cal__day">12</button><button class="hao-cal__day">13</button><button class="hao-cal__day">14</button><button class="hao-cal__day">15</button><button class="hao-cal__day">16</button><button class="hao-cal__day">17</button><button class="hao-cal__day" aria-current="date">18</button><button class="hao-cal__day">19</button><button class="hao-cal__day">20</button><button class="hao-cal__day">21</button><button class="hao-cal__day">22<small class="hao-cal__dot"></small></button><button class="hao-cal__day">23</button><button class="hao-cal__day">24</button><button class="hao-cal__day">25</button><button class="hao-cal__day">26</button><button class="hao-cal__day">27</button><button class="hao-cal__day">28</button><button class="hao-cal__day">29</button><button class="hao-cal__day">30</button></div><p class="hao-cal__foot"><span><i></i>Nov 7, Start of Winter</span><span><i></i>Nov 22, Minor Snow</span></p></div></aside>
  </div>
</main>
```

### Chinese

```html
<header class="top"><div class="hao-page barw">
  <a class="brand" href="#"><span class="hao-seal hao-seal--sm" aria-hidden="true">印</span>产品名</a>
  <nav class="hao-tabs links" aria-label="主导航"><a class="hao-tabs__item" href="#">札记</a><a class="hao-tabs__item" href="#" aria-current="page">回顾</a><a class="hao-tabs__item" href="#">文件夹</a></nav>
  <label class="hao-search" style="width:260px"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="搜索札记" aria-label="搜索札记"></label>
</div></header>
<main class="hao-page" style="padding-bottom:var(--hao-space-12)">
  <div class="head"><h1>十一月回顾</h1><p>丙午年十月，立冬到小雪</p></div>
  <div class="hao-grid">
    <section class="hao-card" style="grid-column:span 8;display:flex;flex-wrap:wrap;gap:var(--hao-space-5) var(--hao-space-12);align-items:flex-start">
      <div class="hao-stat"><span class="hao-stat__l">本月札记</span><span class="hao-stat__v">31<small>条</small></span><span class="hao-stat__n">比上月多 6 条</span></div>
      <div class="hao-stat"><span class="hao-stat__l">累计字数</span><span class="hao-stat__v">48,260<small>字</small></span></div>
      <div class="hao-stat"><span class="hao-stat__l">连续记录</span><span class="hao-stat__v">12<small>天</small></span><span class="hao-stat__n">最长 27 天</span></div>
    </section>
    <section class="hao-card" style="grid-column:span 4"><h2 class="hao-card__title">本周</h2><div class="hao-row" style="gap:var(--hao-space-2)"><span class="hao-moon hao-moon--done" style="--p:1" role="img" aria-label="周一，完成"></span><span class="hao-moon hao-moon--done" style="--p:1" role="img" aria-label="周二，完成"></span><span class="hao-moon" style="--p:0.6" role="img" aria-label="周三，过半"></span><span class="hao-moon" style="--p:0" role="img" aria-label="周四"></span><span class="hao-moon" style="--p:0" role="img" aria-label="周五"></span><span class="hao-moon" style="--p:0" role="img" aria-label="周六"></span><span class="hao-moon" style="--p:0" role="img" aria-label="周日"></span></div><p class="hao-card__meta">周目标 5 条，已完成 2 条半</p></section>
    <section style="grid-column:span 8">
      <div class="hao-table-wrap"><table class="hao-table">
        <thead><tr><th scope="col">标题</th><th scope="col">文件夹</th><th scope="col">状态</th><th scope="col" class="hao-num">字数</th><th scope="col">上次编辑</th></tr></thead>
        <tbody>
          <tr><td>晨间札记</td><td class="hao-muted">随笔</td><td><span class="hao-tag hao-tag--jade">已发布</span></td><td class="hao-num">486</td><td class="hao-muted">今天 07:12</td></tr>
          <tr><td>《园冶》读书笔记</td><td class="hao-muted">读书</td><td><span class="hao-tag hao-tag--tint">进行中</span></td><td class="hao-num">2,140</td><td class="hao-muted">昨天</td></tr>
          <tr><td>苏州三日</td><td class="hao-muted">旅行</td><td><span class="hao-tag">草稿</span></td><td class="hao-num">912</td><td class="hao-muted">11 月 12 日</td></tr>
          <tr><td>入冬的第一场雨</td><td class="hao-muted">随笔</td><td><span class="hao-tag hao-tag--jade">已发布</span></td><td class="hao-num">327</td><td class="hao-muted">11 月 9 日</td></tr>
        </tbody></table></div>
      <nav aria-label="分页" style="margin-top:var(--hao-space-4);display:flex;justify-content:flex-end"><ul class="hao-pages"><li><a class="hao-pages__item" href="#" aria-label="上一页" aria-disabled="true"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i></a></li><li><a class="hao-pages__item" href="#" aria-current="page">1</a></li><li><a class="hao-pages__item" href="#">2</a></li><li><a class="hao-pages__item" href="#">3</a></li><li><a class="hao-pages__item" href="#" aria-label="下一页"><i class="hao-icon hao-icon--chevron-right" aria-hidden="true"></i></a></li></ul></nav>
    </section>
    <aside style="grid-column:span 4"><div class="hao-cal" style="width:100%"><div class="hao-cal__head"><h2 class="hao-cal__title">十一月</h2></div><div class="hao-cal__grid"><span class="hao-cal__dow">一</span><span class="hao-cal__dow">二</span><span class="hao-cal__dow">三</span><span class="hao-cal__dow">四</span><span class="hao-cal__dow">五</span><span class="hao-cal__dow">六</span><span class="hao-cal__dow">日</span><button class="hao-cal__day hao-cal__day--out">26<small class="hao-cal__lunar">十七</small></button><button class="hao-cal__day hao-cal__day--out">27<small class="hao-cal__lunar">十八</small></button><button class="hao-cal__day hao-cal__day--out">28<small class="hao-cal__lunar">十九</small></button><button class="hao-cal__day hao-cal__day--out">29<small class="hao-cal__lunar">二十</small></button><button class="hao-cal__day hao-cal__day--out">30<small class="hao-cal__lunar">廿一</small></button><button class="hao-cal__day hao-cal__day--out">31<small class="hao-cal__lunar">廿二</small></button><button class="hao-cal__day">1<small class="hao-cal__lunar">廿三</small></button><button class="hao-cal__day">2<small class="hao-cal__lunar">廿四</small></button><button class="hao-cal__day">3<small class="hao-cal__lunar">廿五</small></button><button class="hao-cal__day">4<small class="hao-cal__lunar">廿六</small></button><button class="hao-cal__day">5<small class="hao-cal__lunar">廿七</small></button><button class="hao-cal__day">6<small class="hao-cal__lunar">廿八</small></button><button class="hao-cal__day">7<small>立冬</small></button><button class="hao-cal__day">8<small class="hao-cal__lunar">三十</small></button><button class="hao-cal__day">9<small class="hao-cal__lunar hao-cal__lunar--first">十月</small></button><button class="hao-cal__day">10<small class="hao-cal__lunar">初二</small></button><button class="hao-cal__day">11<small class="hao-cal__lunar">初三</small></button><button class="hao-cal__day">12<small class="hao-cal__lunar">初四</small></button><button class="hao-cal__day">13<small class="hao-cal__lunar">初五</small></button><button class="hao-cal__day">14<small class="hao-cal__lunar">初六</small></button><button class="hao-cal__day">15<small class="hao-cal__lunar">初七</small></button><button class="hao-cal__day">16<small class="hao-cal__lunar">初八</small></button><button class="hao-cal__day">17<small class="hao-cal__lunar">初九</small></button><button class="hao-cal__day" aria-current="date">18<small class="hao-cal__lunar">初十</small></button><button class="hao-cal__day">19<small class="hao-cal__lunar">十一</small></button><button class="hao-cal__day">20<small class="hao-cal__lunar">十二</small></button><button class="hao-cal__day">21<small class="hao-cal__lunar">十三</small></button><button class="hao-cal__day">22<small>小雪</small></button><button class="hao-cal__day">23<small class="hao-cal__lunar">十五</small></button><button class="hao-cal__day">24<small class="hao-cal__lunar">十六</small></button><button class="hao-cal__day">25<small class="hao-cal__lunar">十七</small></button><button class="hao-cal__day">26<small class="hao-cal__lunar">十八</small></button><button class="hao-cal__day">27<small class="hao-cal__lunar">十九</small></button><button class="hao-cal__day">28<small class="hao-cal__lunar">二十</small></button><button class="hao-cal__day">29<small class="hao-cal__lunar">廿一</small></button><button class="hao-cal__day">30<small class="hao-cal__lunar">廿二</small></button></div></div></aside>
  </div>
</main>
```
