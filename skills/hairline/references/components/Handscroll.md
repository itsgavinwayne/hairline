# Handscroll · 手卷

横向滚动的一卷内容，像展开一幅手卷：最前面是题名，然后一段一段向后看。

`.hao-handscroll` 里依次是 `.hao-handscroll__title`（引首）、若干 `.hao-handscroll__item`、可选的 `.hao-handscroll__end`（拖尾）。每一段是一个链接，里面放日期、标题、三行以内的摘要。内容由你提供。

- **引首**是这一卷的题名：中文竖排宋体，下面一行小字写数量；英文横排，靠左下。底色是 `tint-wash`，一眼能看出这是开头。
- **每一段**等宽等高，段与段之间一道细缝，像手卷上的「隔水」。摘要超过三行自动截断。
- **拖尾**放一方小印，表示到头了。没有更多内容时才显示；还能继续加载时不放。
- 向右滚动，起点对齐到每一段的左边。不显示滚动条，也不放左右箭头；最后一段露出一半，提示还能往后看。
- 用于「同一组里的几条」：一个月的札记、一个专题、一组作品。互不相干的内容用列表。
- 三到八段。更多就给一个「查看全部」进到列表页。
- 整卷可以用键盘左右移动，每一段都能被聚焦。
- 和 `Mount` 一样，它是内容的容器，不算纹样；但一屏只放一卷。

## 标记

### 中文

```html
<div class="hao-handscroll" style="max-width:760px"><div class="hao-handscroll__title"><span>十一月<small>三篇</small></span></div><a class="hao-handscroll__item" href="#"><time>11 月 18 日</time><h3>晨间札记</h3><p>窗外起了薄雾。把今天要做的三件事写下来，其余的先放一放。</p></a><a class="hao-handscroll__item" href="#"><time>11 月 12 日</time><h3>苏州三日</h3><p>第一天只看了一座园子。走得慢，才发现每一扇窗框住的都是一幅画。</p></a><a class="hao-handscroll__item" href="#"><time>11 月 9 日</time><h3>入冬的第一场雨</h3><p>雨下了一夜。早上出门，地上的银杏叶比树上的还多。</p></a><div class="hao-handscroll__end"><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div>
```

### English

```html
<div class="hao-handscroll" style="max-width:760px"><div class="hao-handscroll__title"><span>November<small> 3 notes</small></span></div><a class="hao-handscroll__item" href="#"><time>Nov 18</time><h3>Morning note</h3><p>Fog outside the window. Write down the three things that matter today, and let the rest wait.</p></a><a class="hao-handscroll__item" href="#"><time>Nov 12</time><h3>Three days in Suzhou</h3><p>We saw one garden on the first day. Walking slowly, I noticed that every window frames a painting.</p></a><a class="hao-handscroll__item" href="#"><time>Nov 9</time><h3>First rain of winter</h3><p>It rained all night. In the morning there were more ginkgo leaves on the ground than on the trees.</p></a><div class="hao-handscroll__end"><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></div></div>
```
