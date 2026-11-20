# Paper · 笺纸

一张笺纸：带界栏的信纸，用来写和读篇幅不长、带点郑重的文字。

`.hao-paper` 可以加在 `<textarea>` 上（写），也可以加在 `<div>` 上（读，里面每段一个 `<p>`，空行用一个空的 `<p>`）。写的时候照 `TextField` 的结构在上面放标签。

- 样子取自旧式的笺纸：四周是「文武边」（外粗内细两道线），纸上一行一道细的界栏，字正好坐在线上。线都是泥金色。
- 每行 32px，比普通输入框松，写的时候不局促。输入框可以向下拖高，界栏跟着文字一起滚。
- 聚焦时外框变成 `tint`，界栏不变。
- 只用在「写一段话」本身就是主角的地方：写信、写札记、留言、题词。搜索、表单里的备注、评论框用普通的多行输入。
- 一屏一张。读和写可以是同一种纸，这样回信的时候像是在同一张桌子上。
- 不竖排。信纸上的界栏本来是竖的，但横着打字更顺，所以界栏改成了横的。
- 不加花笺的底纹和图案。

**无障碍**

- 写的版本是 `<textarea class="hao-paper">`：原生控件，Tab 走到就能写；标签照预览用 `for` 接到它的 `id` 上。
- 读的版本是普通元素里的 `<p>`，读屏逐段读；界栏和文武边是背景画的，不产生文字。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-field" style="width:400px"><label class="hao-field__label" for="pp">写给林晚</label>
<textarea class="hao-paper" id="pp" style="height:224px">见字如面。

这几天起了雾，早上什么都看不清，倒是安静。你上次说的那本书我找到了，读到第三章。</textarea></div>
<div style="width:400px"><p class="hao-field__label" style="margin:0 0 var(--hao-space-2)">收到的信</p>
<div class="hao-paper"><p>见字如面。</p><p></p><p>书读到哪里了？我这边昨天下了第一场雪，不大，落地就化了。</p></div></div>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-field" style="width:400px"><label class="hao-field__label" for="pp-en">To Lin Wan</label>
<textarea class="hao-paper" id="pp-en" style="height:256px">Dear Lin,

It has been foggy for days. The mornings are quiet, and I can’t see past the street. I found the book you mentioned and I’m on chapter three.</textarea></div>
<div style="width:400px"><p class="hao-field__label" style="margin:0 0 var(--hao-space-2)">Letter received</p>
<div class="hao-paper"><p>Dear friend,</p><p></p><p>How far are you into the book? We had the first snow here yesterday. Not much, and it melted as it landed.</p></div></div>
</div>
```
