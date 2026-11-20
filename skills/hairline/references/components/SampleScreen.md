# SampleScreen · 首页

一张示例屏，展示各组件拼在一起的样子，不是可复用的组件。

它示范了几条规则：宋体大标题左对齐；右上角一组落款（竖排年款加一方小印）是这一屏唯一的朱砂；最重要的卡片底边铺海水纹，是这一屏唯一的纹样；分组列表直接放在 `bg` 上；主按钮只有一个；标签栏用 `material` 毛玻璃。

## 标记

### 中文

```html
<div class="phone">
  <div class="scroll">
    <header class="top">
      <div>
        <p class="date">11 月 18 日 星期三</p>
        <h1 class="big">今日</h1>
      </div>
      <span class="hao-sign"><span class="hao-slip">丙午冬</span><span class="hao-seal hao-seal--sm" role="img" aria-label="印章">印</span></span>
    </header>
    <div class="hao-seg" role="radiogroup" aria-label="范围" style="display:flex">
      <label style="flex:1"><input type="radio" name="s" checked><span>今日</span></label>
      <label style="flex:1"><input type="radio" name="s"><span>本周</span></label>
      <label style="flex:1"><input type="radio" name="s"><span>全部</span></label>
    </div>
    <div class="hao-card hao-card--wave">
      <h2 class="hao-card__title">晨间札记</h2>
      <p class="hao-card__body">窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p>
      <p class="hao-card__meta">今天 07:12</p>
    </div>
    <button class="hao-btn hao-btn--block">写一条札记</button>
    <div>
      <p class="hao-list-header">待办</p>
      <ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">整理设计令牌</span><span class="hao-tag hao-tag--tint">进行中</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">回复出版社邮件</span><span class="hao-tag hao-tag--amber">今天到期</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">晚间散步</span><span class="hao-tag hao-tag--jade">已完成</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
      </ul>
    </div>
  </div>
  <nav class="tabs" aria-label="主导航">
    <a href="#" class="on" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a>
    <a href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记</a>
    <a href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>我的</a>
  </nav>
</div>
```

### English

```html
<div class="phone">
  <div class="scroll">
    <header class="top">
      <div>
        <p class="date">Wednesday, November 18</p>
        <h1 class="big">Today</h1>
      </div>
      <span class="hao-seal" role="img" aria-label="Seal" lang="zh">印</span>
    </header>
    <div class="hao-seg" role="radiogroup" aria-label="Range" style="display:flex">
      <label style="flex:1"><input type="radio" name="s" checked><span>Today</span></label>
      <label style="flex:1"><input type="radio" name="s"><span>This week</span></label>
      <label style="flex:1"><input type="radio" name="s"><span>All</span></label>
    </div>
    <div class="hao-card hao-card--wave">
      <h2 class="hao-card__title">Morning note</h2>
      <p class="hao-card__body">Fog outside the window. Write down the three things that matter today, and let the rest wait.</p>
      <p class="hao-card__meta hao-sign hao-sign--row" style="display:flex;justify-content:space-between"><span>Today, 7:12 AM</span><span class="hao-colophon">Winter, the Bingwu year</span></p>
    </div>
    <button class="hao-btn hao-btn--block">Write a note</button>
    <div>
      <p class="hao-list-header">To do</p>
      <ul class="hao-list">
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Tidy the design tokens</span><span class="hao-tag hao-tag--tint">In progress</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Reply to the publisher</span><span class="hao-tag hao-tag--amber">Due today</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
        <li><a class="hao-list__row" href="#"><span class="hao-list__title">Evening walk</span><span class="hao-tag hao-tag--jade">Done</span><i class="hao-icon hao-icon--chevron-right hao-list__chev" aria-hidden="true"></i></a></li>
      </ul>
    </div>
  </div>
  <nav class="tabs" aria-label="Main">
    <a href="#" class="on" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a>
    <a href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes</a>
    <a href="#"><i class="hao-icon hao-icon--person" aria-hidden="true"></i>Me</a>
  </nav>
</div>
```
