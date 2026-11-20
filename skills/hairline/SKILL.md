---
name: hairline
description: 用「毫 Hairline」设计系统做界面：iOS 的克制加一点东方气韵，中英双语，昼夜两套主题，纯 HTML 和 CSS，类名以 hao- 开头。用户提到 Hairline、毫、hao- 类名，或要一个带中国气韵、宋式留白、朱砂印章、石青色的网页、应用界面、文章页、海报时使用。Build interfaces with the Hairline (毫) design system - restrained like iOS with a trace of Chinese character, bilingual, light and dark, plain HTML and CSS with hao- classes. Use when the user mentions Hairline, hao- classes, or wants a web page, app screen, article, or poster with a Chinese, Song-dynasty, ink-and-seal feel.
---

# 毫 Hairline

一套不依赖框架的设计系统：一份样式表、一份可选的行为脚本、一份令牌。结构、密度和交互照 iOS 的规矩，颜色、标题字和留白取自石青、朱砂印与宣纸。

English documentation mirrors everything below under `references/en/`. If the user writes in English, read those files instead; the rules are the same.

## 先把文件放进项目

`assets/` 里有三个文件，原样拷进使用者的项目，不要改它们：

- `assets/hairline.css`：全部令牌和所有组件的样式，含昼夜两套主题。
- `assets/hairline.js`：弹窗、菜单、月历、轻提示等的行为。可选，不加载时组件照样能看。
- `assets/tokens.json`：令牌的原始数据，给设计工具或别的平台用。

页面骨架：

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="hairline.css">
</head>
<body>
  <!-- 页面内容 -->
  <script src="hairline.js" defer></script>
</body>
</html>
```

- 语言写在 `<html lang>` 上：`zh-CN` 或 `en`。标题的字号字距、引文的角标、月历的星期都跟着它走。
- 主题写在 `<html data-theme>` 上：`light` 或 `dark`；不写就跟随系统。
- 用了 React、Vue 之类的框架也一样：引入样式表，照抄标记，把 `class` 换成框架的写法。行为脚本接管的是页面上已有的标记，动态加进来的内容调用一次 `Hairline.init(容器)`。

## 怎么写

1. **先定是哪一类产物**：界面、阅读、平面、品牌，各有各的规矩。见 `references/outputs.md`。
2. **找组件，抄标记**：先看 `references/components.md` 这张总表，再只打开用得到的 `references/components/<名字>.md`。每个文件里有说明和中英文两份可以直接用的标记。不要凭印象编类名，表里没有的类就是不存在。
3. **只用令牌**：颜色、间距、圆角、阴影、动效都写成 `var(--hao-名字)`，字体样式写成 `class="hao-名字"`。全表在 `references/tokens.md`。文档正文里提到令牌时省掉了前缀，写的是 `tint`、`space-4`，落到代码里是 `var(--hao-tint)`、`var(--hao-space-4)`。
4. **能用原生元素就用原生元素**：按钮是 `<button>`，开关是 `<input type="checkbox" role="switch">`，下拉是 `<select>`。
5. **行为靠属性声明**：`data-hao-open`、`data-hao-menu`、`data-hao-toast` 等，全表在 `references/behavior.md`。
6. **需要自己写样式时**：先确认真的没有现成组件。新写的类不要用 `hao-` 前缀，那是系统自己的名字空间。

## 三条规矩，交付前逐条核对

这是这套系统和「套了一层中国风皮肤」的区别，全文在 `references/principles.md`。

1. **朱砂一处。** 一屏里红色（`seal`）只出现一次：一方印、一个角标，或者一个删除按钮。
2. **一屏一景。** 纹样、小品、装裱这类「景」一屏至多一个；设置、表单这类办事的页面一个都不放。
3. **形随控件。** 一种意象只对应一种控件：进度只用一种画法，月亮只出现一处。

再对照五条审美标准（素、空、淡、细、偏，见 `references/aesthetics.md`）：拿不准一样东西该不该加，就不加。先留白，再落笔。

## 常见的错

- 把红色当强调色到处用。主操作用 `tint`（石青），红色只留给印和危险操作。
- 堆传统元素：回纹、海水纹、印章、题签同时出现。一屏一景。
- 用水墨笔触、仿旧纸纹、祥云贴图、大红大金。这套系统「取形不取质感」，图形只用细线和平涂，见 `references/imagery.md`。
- 给汉字用斜体，或者把英文的字号字距套到中文标题上。中英文排法见 `references/english.md`。
- 印章里留着占位的字。印文、产品名、落款的年款要换成使用者自己的；要做真的篆字印见 `references/seal.md`。
- 手写色值、像素间距，或者自己造 `z-index`。

## 按需要再读

| 要做什么 | 读哪个 |
| --- | --- |
| 网页布局、断点、悬停与键盘、各种状态 | `references/foundations.md` |
| 弹窗、菜单、月历等的行为和无障碍 | `references/behavior.md` |
| 英文界面 | `references/english.md` |
| 文章、长文、竖排的诗 | `references/reading.md` |
| 海报、社交图片、印刷 | `references/print.md` |
| 配图、插画、纹样怎么选 | `references/imagery.md` |
| 组件名和类名的对照 | `references/naming.md` |
| 整页的样板（首页、文章、表单、设置、数据、网页） | `references/components/Sample*.md` |

## 做完之后

- 昼和夜都看一遍；有英文内容时中英文都看一遍。
- 用键盘走一遍：能点的都能用 Tab 走到，焦点环看得见。
- 凡是一个字或数字放在框里的控件（序号、印章、头像、角标、页码），放大看有没有居中。
- 告诉使用者换了哪三样（印文、产品名、落款），以及哪些地方为了守规矩没有加装饰。
