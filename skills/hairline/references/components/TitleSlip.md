# TitleSlip · 题签

竖排的题签，仿线装书封面左上角贴的那张书名签。

`<span class="hao-slip">` 是竖排宋体小字；加 `hao-slip--boxed` 带泥金细框和白底。把题签和一方小印包进 `.hao-sign`，就是一组落款。文字由你提供，二到六个汉字。

- 只放汉字，不放西文和数字；年份用干支（「丙午冬」），不写 2026。
- 带框的用作封面、卡片、专题的题名；不带框的用作落款的年款。
- 题签是点缀，页面真正的标题仍然是横排的 `title-1`。同一段文字不要横竖各写一遍。
- 一屏一处。不可点。

英文界面里：

- 西文不竖排。英文落款用横排的 `<span class="hao-colophon">`（斜体衬线），和小印一起包进 `.hao-sign.hao-sign--row`。
- 英文落款写成一个短语，句首大写，不加句号：“Winter, the Bingwu year”。
- 想保留竖排汉字年款作为图形，可以原样使用 `.hao-slip`，加 `lang="zh"` 和英文 `aria-label`；但同一屏里竖排年款和英文落款只留一个。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start">
  <span class="hao-slip hao-slip--boxed">晨间札记</span>
  <span class="hao-slip">丙午冬</span>
  <span class="hao-sign"><span class="hao-slip">丙午冬</span><span class="hao-seal hao-seal--sm" role="img" aria-label="印章">印</span></span>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8);align-items:flex-start">
  <span class="hao-sign hao-sign--row"><span class="hao-colophon">Winter, the Bingwu year</span><span class="hao-seal hao-seal--sm" lang="zh" role="img" aria-label="Seal">印</span></span>
  <span class="hao-colophon">Morning note</span>
  <span class="hao-slip hao-slip--boxed" lang="zh" role="img" aria-label="Morning note">晨间札记</span>
</div>
```
