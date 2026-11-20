# Handscroll

A sideways-scrolling roll of content, like a handscroll unrolling: the title leads, then one section after another.

`.hao-handscroll` holds, in order, `.hao-handscroll__title` (the opening panel, 引首), a run of `.hao-handscroll__item`s, and an optional `.hao-handscroll__end` (the tail, 拖尾). Each item is a link holding a date, a title, and an abstract of three lines or fewer. You provide the content.

- The **opening panel** names the roll: in Chinese, the title stands vertical in the Song typeface with a small line under it giving the count; in English, it lies horizontal at the lower left. Its ground is `tint-wash`, so the start reads at a glance.
- Each **item** is the same width and height, with a thin gap between items like the spacer bands (隔水) of a handscroll. An abstract past three lines is cut off on its own.
- The **tail** carries a small seal, saying the roll has run out. Show it only when nothing more is coming; while more can still load, leave it off.
- It scrolls rightward, each stop aligned to an item’s left edge. No scrollbar shows, and no left or right arrows; the last item peeks halfway out, hinting there is more behind it.
- It’s for “a few items from one group”: a month of notes, one topic, a set of works. Content with nothing in common belongs in a list.
- Three to eight items. Past that, give a “See all” that leads to the list page.
- The whole roll can be worked with the keyboard’s left and right keys, and every item can take focus.
- Like `Mount`, it is a container for content, not a pattern; still, one roll per screen.

## Markup

### English

```html
<div class="hao-handscroll" style="max-width:760px"><div class="hao-handscroll__title"><span>November<small> 3 notes</small></span></div><a class="hao-handscroll__item" href="#"><time>Nov 18</time><h3>Morning note</h3><p>Fog outside the window. Write down the three things that matter today, and let the rest wait.</p></a><a class="hao-handscroll__item" href="#"><time>Nov 12</time><h3>Three days in Suzhou</h3><p>We saw one garden on the first day. Walking slowly, I noticed that every window frames a painting.</p></a><a class="hao-handscroll__item" href="#"><time>Nov 9</time><h3>First rain of winter</h3><p>It rained all night. In the morning there were more ginkgo leaves on the ground than on the trees.</p></a><div class="hao-handscroll__end"><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div>
```

### Chinese

```html
<div class="hao-handscroll" style="max-width:760px"><div class="hao-handscroll__title"><span>十一月<small>三篇</small></span></div><a class="hao-handscroll__item" href="#"><time>11 月 18 日</time><h3>晨间札记</h3><p>窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p></a><a class="hao-handscroll__item" href="#"><time>11 月 12 日</time><h3>苏州三日</h3><p>第一天只看了一座园子。走得慢，才发现每一扇窗框住的都是一幅画。</p></a><a class="hao-handscroll__item" href="#"><time>11 月 9 日</time><h3>入冬的第一场雨</h3><p>雨下了一夜。早上出门，地上的银杏叶比树上的还多。</p></a><div class="hao-handscroll__end"><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div>
```
