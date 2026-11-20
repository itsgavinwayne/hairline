# Cover · 封面

这套系统自己的封面，放在手册最前面，不是可复用的组件。

左边是系统的名字和一句定位，右边是一幅月洞：一块石青里挖出一轮满月，旁边一轮被玄青和淡染一分为二，像月和它的倒影。左下角落一方系统的标志，是整幅里唯一的朱砂。

- 画面按 48px（`space-12`）的模数排，所有色块的边都落在格子上。
- 用它做出来的产品不沿用这张封面；产品自己的封面照「平面与印刷」一节做，印换成自己的印。
- 封面不跟主题走，昼夜都用昼间的颜色（外层写了 `data-theme="light"`）。

**无障碍**

- 右边的图形是装饰，SVG 上写了 `aria-hidden="true"`；名字和定位是真的文字，读屏读得到。

## 标记

### 中文

```html
<div class="cover" data-theme="light">
  <div class="art">
    <!--
      blocks: tint 192×288 (space-12 × 4 wide, full height) · ink 192×144 · tint-wash 192×144 · the Hairline mark (seal with moon and waterline) 48×48 (space-12)
      arrangement: one tall 石青 slab bleeding top and bottom, two stacked satellites flush to its right, the seal alone on the ground at lower left
      pattern: literal motif — the moon gate. A full disc of ground cut from the slab, and a second disc split across the ink/wash seam (moon and its reflection); chosen because the README limits ornament to the seal and asks for white space first
      scales: module space-12 (48px); discs r = 72 (space-6 × 3); seal corner space-1, matching the cut corners of the Seal component
    -->
    <svg viewBox="0 0 480 288" aria-hidden="true">
      <rect class="tint" x="96" y="0" width="192" height="288"/>
      <rect class="deep" x="288" y="0" width="192" height="144"/>
      <rect class="wash" x="288" y="144" width="192" height="144"/>
      <circle class="ground" cx="192" cy="144" r="72"/>
      <path class="wash" d="M312 144a72 72 0 0 1 144 0z"/>
      <path class="deep" d="M312 144a72 72 0 0 0 144 0z"/>
      <path class="seal" fill-rule="evenodd" transform="translate(24 216)" d="M9 4H41a3 3 0 0 1 3 3V38a6 6 0 0 1-6 6H8a4 4 0 0 1-4-4V9a5 5 0 0 1 5-5zM13.300 26.500A11.500 11.500 0 1 1 34.700 26.500zM14.500 30h19a1.100 1.100 0 0 1 0 2.200h-19a1.100 1.100 0 0 1 0-2.200zM18.500 35.200h11a1.100 1.100 0 0 1 0 2.200h-11a1.100 1.100 0 0 1 0-2.200z"/>
    </svg>
  </div>
  <div class="text">
    <h1 class="name">Hairline</h1>
    <p class="tag">iOS 的克制，加上一点东方的气韵</p>
  </div>
</div>
```
