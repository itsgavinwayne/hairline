# Divider · 分隔线

长文里分隔两大段的线，中间一枚「鱼尾」。

`<div class="hao-divider" role="separator"><i></i></div>`。

- 鱼尾是雕版印刷的书页中缝上的记号，本来用来对齐折页。这里用它标出「一章结束」。
- 只用在长文、文章详情、关于页里，一篇文章至多两三处。
- 列表行之间用 `hairline`，分组之间用留白，都不用它。
- 它是文章版式的一部分，不算纹样；但同一处不要和针脚、回纹叠着用。
- 另一种是文武线 `hao-divider--wenwu`：一粗一细两道线，取自宋版书的版框，和表头那道线是同一个形。用在一章、一组内容的开头；鱼尾用在段落之间。

## 标记

### 中文

```html
<div class="hao-stack" style="gap:var(--hao-space-6)"><div class="hao-divider" role="separator"><i></i></div><p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">中间的记号叫「鱼尾」，是雕版书页版心上用来对折的标记。</p></div>

<div class="hao-divider hao-divider--wenwu" role="separator" style="max-width:390px;margin:var(--hao-space-6) 0 var(--hao-space-4)"></div>
<p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">另一种是文武线：一粗一细，取自宋版书的版框，用在一章、一组内容的开头。</p>
```

### English

```html
<div class="hao-stack" style="gap:var(--hao-space-6)"><div class="hao-divider" role="separator"><i></i></div><p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">The mark in the middle is a “fishtail”, the fold guide printed at the center of a woodblock page.</p></div>

<div class="hao-divider hao-divider--wenwu" role="separator" style="max-width:390px;margin:var(--hao-space-6) 0 var(--hao-space-4)"></div>
<p style="margin:0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">The other kind is the double rule, one thick line and one thin, from the page frame of Song printed books. Use it at the head of a chapter or a group.</p>
```
