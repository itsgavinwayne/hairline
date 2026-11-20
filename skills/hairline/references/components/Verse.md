# Verse · 竖排的诗

竖排的诗，或一段值得单独摆出来的短句。这是系统里唯一让正文竖着走的地方。

`.hao-verse` 里第一个是 `.hao-verse__title`，然后每一句一个 `<p>`，最后是 `.hao-verse__by`（作者，可带一方小印）。文字由你提供。

- 竖排，自右向左：题目在最右，作者在最左。每句一列，不加标点（标点在竖排里占位，古诗本来也不加）。
- 只用于诗、对句、题词这类短的文字：不超过八列，每列不超过十个字。长文不竖排，横着读更快。
- 英文不竖排。根元素是英文时，它自动变成横排的衬线诗行，题目在上，作者用斜体在下。
- 字用宋体，字距放宽，行距是字高的两倍。
- 放在阅读页的开头、卡片里、启动页上都可以。一屏一处，周围多留白。
- 例子是王维的《鹿柴》；英文是按意思译的，不是通行译本。

**无障碍**

- 题目、每一句、作者都是 `<p>` 里的文字，DOM 顺序就是朗读顺序，竖排只是样子。
- 作者旁的小印照预览写 `aria-hidden="true"`，作者名字照常读。
- 英文界面自动换成横排诗行，文字内容不变。

## 标记

### 中文

```html
<div class="hao-verse" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg)">
<p class="hao-verse__title">鹿柴</p>
<p>空山不见人</p><p>但闻人语响</p><p>返景入深林</p><p>复照青苔上</p>
<p class="hao-verse__by">王维<span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></p>
</div>
```

### English

```html
<div class="hao-verse" style="background:var(--hao-surface);border-radius:var(--hao-radius-lg);padding:var(--hao-space-6)">
<p class="hao-verse__title">Deer Enclosure</p>
<p>Empty hills, no one in sight,</p><p>yet voices can be heard.</p><p>Late sunlight enters the deep wood</p><p>and shines again on the green moss.</p>
<p class="hao-verse__by">Wang Wei</p>
</div>
```
