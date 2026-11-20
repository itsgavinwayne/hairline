# Logo · 标志

Hairline 这套系统自己的标志：一方朱砂印，印面里一轮月、一道水线，旁边是字标。

`<span class="hao-logo">` 里放印的 SVG 和 Hairline 这个词。尺寸有 `hao-logo--sm`、默认、`hao-logo--lg`；`hao-logo--stack` 是上下排；`hao-logo--ink` 是单色，颜色跟随文字。

**它是什么**

- 印，是这套系统的署名方式；月，是系统里用得最多的意象（月洞、月相、水中月）。标志把两者合成一个记号：从印面望出去，看见水上一轮月。
- 印面是系统里印章的形：四个角略不相等。月和水线是镂空的，透出底色。
- 字标是 Newsreader，字重 500，字距略收。

**什么时候用**

- 只在指代这套系统本身时用：文档封面、关于页里那一行「界面基于 Hairline 设计系统」的旁边、介绍这套系统的海报和幻灯片。
- 用这套系统做出来的产品，不用这个标志。产品的标志是它自己的印（见 `Seal`）。

**怎么用**

- 首选横排。空间接近方形时用竖排。很小的地方（小于 20px 高）只用印，不带字。
- 四周留出至少半个印面宽的空白，里面不放别的东西。
- 印的最小尺寸是 16px。再小，月和水线就糊了。
- 朱砂色的标志就是那一屏唯一的朱砂，同屏不再放印章、红色角标或删除按钮。
- 放在有颜色的底上，或者单色印刷时，用单色版，颜色取所在的文字色。
- 夜间主题下印会自动换成亮一些的朱砂色。

**不要这样**

- 不改颜色（除了单色版），不加阴影、渐变、描边。
- 不拉伸，不旋转，不把印和字拆开重新排。
- 不把月换成别的图形，不往印面里加字。
- 不用它当应用图标的底，不拿它当装饰图案平铺。
- 字标不换字体，不改大小写。

资源的 Logos 组里有三个 SVG 文件（朱砂、夜间朱砂、玄青单色），给设计稿和印刷用。

**无障碍**

- 标志是一个整体：照预览在 `.hao-logo` 上写 `role="img"` 和 `aria-label`，里面的 SVG 写 `aria-hidden="true"`，读屏只读一遍名字，不拆成印和字。
- 只用印、不带字标的版本同样写 `aria-label`，读屏才知道这方印是什么。
- 字标是英文词，照预览在标志上写 `lang="en"`，读屏换英文语音来读。
- 标志当链接用（写成 `<a class="hao-logo">`）时，键盘聚焦会描一圈 `focus` 色的边，和其他能点的东西一致。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end">
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">横排，首选</p></div>
  <div><span class="hao-logo " role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">标准</p></div>
  <div><span class="hao-logo hao-logo--sm" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">最小</p></div>
</div>
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end;margin-top:var(--hao-space-8)">
  <div style="text-align:center"><span class="hao-logo hao-logo--stack" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">竖排，用于方形空间</p></div>
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" style=""><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg></span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">只用印</p></div>
  <div><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">单色</p></div>
  <div style="padding:var(--hao-space-4) var(--hao-space-5);border-radius:var(--hao-radius-md);background:var(--hao-tint)"><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en" style="color:var(--hao-on-tint)"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end">
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Horizontal, preferred</p></div>
  <div><span class="hao-logo " role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Default</p></div>
  <div><span class="hao-logo hao-logo--sm" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Smallest</p></div>
</div>
<div class="hao-row" style="gap:var(--hao-space-12);align-items:flex-end;margin-top:var(--hao-space-8)">
  <div style="text-align:center"><span class="hao-logo hao-logo--stack" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Stacked, for square spaces</p></div>
  <div><span class="hao-logo hao-logo--lg" role="img" aria-label="Hairline" style=""><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg></span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">Mark only</p></div>
  <div><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span><p style="margin:var(--hao-space-2) 0 0;font:400 13px/20px var(--hao-font-sans);color:var(--hao-ink-tertiary)">One color</p></div>
  <div style="padding:var(--hao-space-4) var(--hao-space-5);border-radius:var(--hao-radius-md);background:var(--hao-tint)"><span class="hao-logo hao-logo--ink" role="img" aria-label="Hairline" lang="en" style="color:var(--hao-on-tint)"><svg viewBox="0 0 48 48" aria-hidden="true"><path fill-rule="evenodd" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/></svg>Hairline</span></div>
</div>
```
