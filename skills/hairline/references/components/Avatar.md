# Avatar · 头像

代表一个人的圆形头像。

`<span class="hao-avatar">`，里面放一张 `<img>`，或在没有照片时放姓名的第一个字。尺寸：`hao-avatar--sm` 28px、默认 40px、`hao-avatar--lg` 64px。多人并排用 `.hao-avatar-group`。

- 人用圆，印用方。头像永远是正圆，不要和印章混淆，也不要给头像用朱砂色。
- 没有照片时，中文名取姓，英文名取首字母，底色 `tint-wash`、字色 `tint`。
- 加 `role="img"` 和 `aria-label` 写全名；旁边已经有名字时改成 `aria-hidden="true"`。
- 并排最多显示三个，其余合成一个「+3」。
- 英文名取两个首字母时字号会自动缩小一档，两个字母才放得下。
- 没有照片时还有一种更讲究的样子 `hao-avatar--name`：一枚圆形的姓氏章，宋体的姓，细的石青色圆边。用在个人主页、作者栏这类人是主角的地方；列表里成排出现时用默认的浅底样式。它是圆的、石青色的，和方的、朱砂色的印章不会混。只用于汉字。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-5)">
  <span class="hao-avatar hao-avatar--lg" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--sm" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--lg hao-avatar--name" role="img" aria-label="林晚">林</span>
  <span class="hao-avatar hao-avatar--name" role="img" aria-label="周行">周</span>
  <span class="hao-avatar-group"><span class="hao-avatar" role="img" aria-label="林晚">林</span><span class="hao-avatar" role="img" aria-label="周行">周</span><span class="hao-avatar" role="img" aria-label="另外三人">+3</span></span>
</div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5)">
  <span class="hao-avatar hao-avatar--lg" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar hao-avatar--sm" role="img" aria-label="Lin Wan">LW</span>
  <span class="hao-avatar-group"><span class="hao-avatar" role="img" aria-label="Lin Wan">LW</span><span class="hao-avatar" role="img" aria-label="Zhou Xing">ZX</span><span class="hao-avatar" role="img" aria-label="3 more">+3</span></span>
</div>
```
