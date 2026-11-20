# Slider · 滑块

在一个连续范围里拖动选值，适合不需要精确数字的设置。

`<input class="hao-slider" type="range">`，外面照 `TextField` 的结构放标签和说明。用内联的 `--v` 写出当前值占的百分比，轨道才会着色（Firefox 不需要）。

- 值立即生效，边拖边看到效果。
- 说明里写出当前的值和它的含义（「17，标准」）。
- 需要精确数字时用步进器或输入框。
- 滑块 28px，轨道 4px；左右方向键每次一步。触屏上可拖的范围撑到 44px 高。
- 不能调时加 `disabled`，整体降到 `opacity-disabled`。
- 滑块中心有一个石青色的小点，像一枚玉璧。它只是形状，不表示数值。

**行为**（加载了行为脚本时）

- 拖动时轨道的着色自动跟着走，不用自己写 `--v`。

**无障碍**

- 原生 `<input type="range">` 自带键盘操作：方向键增减，Home 和 End 跳到两端。
- 聚焦时滑轨外描一圈 `focus` 色的边。
- 轨道着色只是给眼睛的，真值在 `input` 上，读屏播报的就是它；不加载脚本时自己写 `--v`，值也不受影响。

## 标记

### 中文

```html
<div class="hao-field" style="width:320px;max-width:100%">
  <label class="hao-field__label" for="sl">正文字号</label>
  <input class="hao-slider" id="sl" type="range" min="14" max="22" value="17" style="--v:37.5%">
  <span class="hao-field__hint">17，标准</span>
</div>
```

### English

```html
<div class="hao-field" style="width:320px;max-width:100%">
  <label class="hao-field__label" for="sl-en">Body text size</label>
  <input class="hao-slider" id="sl-en" type="range" min="14" max="22" value="17" style="--v:37.5%">
  <span class="hao-field__hint">17, standard</span>
</div>
```
