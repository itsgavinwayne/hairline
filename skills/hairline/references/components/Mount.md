# Mount · 装裱

把一张重点图片「装裱」起来：四周留出绫边，竖幅的下面有一根轴。

`<figure class="hao-mount">` 里放一张 `<img>`（或 SVG）和一个 `<figcaption>`。横幅加 `hao-mount--wide`。图片由你提供；预览里的画是占位的线稿。

- **立轴**（默认，竖幅）：上边的绫比下边宽，比例大约三比二，这叫「天头」「地头」；顶上一根细的天杆，底下一根两头露出来的地轴。
- **横披**（`hao-mount--wide`，横幅）：左右的绫比上下宽，没有轴。
- 画心四周有一圈很细的泥金线，是装裱里的「局条」。画心本身是直角，不加圆角。这是系统里少数不用圆角的地方，因为画是方的。
- 绫用 `surface-sunken`，素色，不加花纹。
- 只给值得停下来看的图：文章的题图、作品、封面。列表里的缩略图、头像、截图不装裱。
- 一屏一幅。它已经很有分量，旁边不再放纹样。
- 图片要有 `alt`；`<figcaption>` 是图名，两到六个字，居中。
- 立轴默认宽 220px，横披 420px，可以用宽度覆盖，比例会跟着走。
- 立轴的天头垂着两条「惊燕」，是立轴本来就有的两条绫带；横幅没有。

**无障碍**

- 画心要有名字：SVG 的画照预览写 `role="img"` 和 `aria-label`，读屏把它当一张有名字的图；`<img>` 的名字走 `alt`。
- 装裱的绫边、天杆、地轴、局条都是伪元素画的，不进读屏。
- `<figure>` 和 `<figcaption>` 的组合，读屏原生就把画和图名配成一对，不用额外属性。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start"><figure class="hao-mount"><svg viewBox="0 0 200 300" role="img" aria-label="远山、孤舟与月"><circle class="wash" cx="142" cy="62" r="18"/><path class="far" d="M0 150l30-42 24 22 30-52 36 58 30-28 50 46M0 176h42M60 172h30M120 176h60"/><path d="M0 206l40-30 28 16 40-36 44 40 48-18"/><path d="M78 246h40l-7 9H85zM89 246q9-14 18 0M98 232v-12"/><path class="far" d="M20 262h40M72 266h56M140 261h40M40 278h36M96 280h60"/></svg><figcaption>江上</figcaption></figure><figure class="hao-mount hao-mount--wide"><svg viewBox="0 0 340 150" role="img" aria-label="连绵的远山与月"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>远山</figcaption></figure></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start"><figure class="hao-mount"><svg viewBox="0 0 200 300" role="img" aria-label="Distant hills, a lone boat and the moon"><circle class="wash" cx="142" cy="62" r="18"/><path class="far" d="M0 150l30-42 24 22 30-52 36 58 30-28 50 46M0 176h42M60 172h30M120 176h60"/><path d="M0 206l40-30 28 16 40-36 44 40 48-18"/><path d="M78 246h40l-7 9H85zM89 246q9-14 18 0M98 232v-12"/><path class="far" d="M20 262h40M72 266h56M140 261h40M40 278h36M96 280h60"/></svg><figcaption>On the river</figcaption></figure><figure class="hao-mount hao-mount--wide"><svg viewBox="0 0 340 150" role="img" aria-label="A range of distant hills under the moon"><circle class="wash" cx="270" cy="40" r="15"/><path class="far" d="M0 84l40-34 30 20 44-46 50 52 40-26 56 40 80-30M0 104h60M90 100h50M190 104h90"/><path d="M0 120l60-26 40 14 56-30 60 34 60-16 64 20"/><path class="far" d="M30 134h60M120 138h80M230 133h70"/></svg><figcaption>Distant hills</figcaption></figure></div>
```
