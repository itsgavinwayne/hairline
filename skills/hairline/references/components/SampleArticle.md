# SampleArticle · 文章页

文章页的示例，用来检验「内容页可以讲究一点，但加起来不要太多」，不是可复用的组件。

一篇里用了一幅装裱、一处引文、一道鱼尾、一组落款，这是上限。导航栏里的书签丝带是使用者自己的标记；唯一的朱砂是文末的小印。

## 标记

### 中文

```html
<div class="phone">
  <header class="hao-nav bar"><div class="hao-nav__bar"><a class="hao-nav__action" href="#"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i>札记</a><span></span><button class="hao-lamp" aria-pressed="true" aria-label="取消收藏" style="justify-self:end"></button></div></header>
  <div class="scroll" style="padding:88px 0 var(--hao-space-8);gap:0;background:var(--hao-surface)">
  <article class="hao-prose" style="padding-top:var(--hao-space-8)">
    <h1>雾里的早晨</h1>
    <p class="hao-prose__meta">丙午年 小雪前四日</p>
    <p>早上推开窗，对面的楼只剩一个淡淡的轮廓。雾把远处的东西都收走了，只留下眼前这一小块：窗台、一盆文竹、一杯刚倒的水。</p>
    <figure class="hao-mount hao-mount--wide" style="width:100%;padding:14px 22px"><svg viewBox="0 0 340 150" role="img" aria-label="连绵的远山与月"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>远山</figcaption></figure>
    <p>平时总觉得要看得远才算看清楚。今天看不远，反倒把近处的东西看了个仔细。</p>
    <blockquote class="hao-quote"><p>虽由人作，宛自天开。</p><cite>计成《园冶》</cite></blockquote>
    <p>画山水的人说，纸上最要紧的是没画的地方。雾大概就是天地自己留的白。</p>
    <div class="hao-divider" role="separator"><i></i></div>
    <p>等到九点钟，雾散了，楼又回来了。我把杯子里的水喝完，开始做今天的第一件事。</p>
    <div class="hao-prose__sign"><span class="hao-sign"><span class="hao-slip">丙午冬</span><span class="hao-seal hao-seal--sm hao-seal--outline" aria-hidden="true">印</span></span></div>
  </article></div></div>
```

### English

```html
<div class="phone">
  <header class="hao-nav bar"><div class="hao-nav__bar"><a class="hao-nav__action" href="#"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i>Notes</a><span></span><button class="hao-lamp" aria-pressed="true" aria-label="Remove from favorites" style="justify-self:end"></button></div></header>
  <div class="scroll" style="padding:88px 0 var(--hao-space-8);gap:0;background:var(--hao-surface)">
  <article class="hao-prose" style="padding-top:var(--hao-space-8)">
    <h1>A morning in fog</h1>
    <p class="hao-prose__meta">Four days before Minor Snow (<span lang="zh">小雪</span>), the Bingwu year</p>
    <p>I opened the window this morning and the building across the way was only a faint outline. The fog had taken everything far off, leaving just this small patch in front of me: the windowsill, a pot of asparagus fern, a glass of water just poured.</p>
    <figure class="hao-mount hao-mount--wide" style="width:100%;padding:14px 22px"><svg viewBox="0 0 340 150" role="img" aria-label="Distant hills and a moon"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>Distant hills</figcaption></figure>
    <p>Most days I feel that seeing far is what it means to see clearly. Today I couldn’t see far, and so I looked closely at what was near.</p>
    <blockquote class="hao-quote"><p>Though made by human hands, it seems to come from heaven.</p><cite>Ji Cheng, The Craft of Gardens</cite></blockquote>
    <p>Landscape painters say the most important part of the paper is the place left unpainted. Fog is probably the blank the world leaves for itself.</p>
    <div class="hao-divider" role="separator"><i></i></div>
    <p>By nine the fog had lifted and the building came back. I finished the water in my glass and started the first thing of the day.</p>
    <div class="hao-prose__sign"><span class="hao-sign"><span class="hao-colophon">Winter, the Bingwu year</span><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></span></div>
  </article></div></div>
```
