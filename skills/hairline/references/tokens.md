# 令牌

每个令牌都是一个 CSS 变量，写出来是 `var(--hao-名字)`。颜色有昼夜两个值，跟着 `data-theme` 或系统设置切换。不要写散值，没有合适的令牌就先用最接近的。

## 颜色

| 变量 | 昼 | 夜 | 用途 |
| --- | --- | --- | --- |
| `--hao-bg` | `#f2f4f7` | `#0e1218` | 月白。页面底色，相当于 iOS 的分组背景；所有卡片和列表都浮在它上面。 |
| `--hao-surface` | `#ffffff` | `#181d26` | 瓷白。卡片、列表组、弹层的表面，放在 bg 之上。 |
| `--hao-surface-sunken` | `#e8ebf0` | `#222834` | 云灰。输入框填充、分段控件轨道等向内凹的区域。 |
| `--hao-surface-hover` | `#f5f7fa` | `#1e2430` | 鼠标悬停在 surface 上的行、菜单项时的底色。只在有鼠标的设备上出现。 |
| `--hao-surface-raised` | `#ffffff` | `#303847` | 浮起的小块：分段控件的选中块、步进器按钮悬停。昼间和 surface 同色，靠阴影浮起；夜间阴影看不见，所以比 surface-sunken 亮一档。 |
| `--hao-ink` | `#161b24` | `#eef1f6` | 玄青。标题与正文，可用于 bg、surface、surface-sunken。 |
| `--hao-ink-secondary` | `#4a5263` | `#a9b1c0` | 黛。次要文字、列表右侧的值，可用于 bg、surface、surface-sunken。 |
| `--hao-ink-tertiary` | `#5f6778` | `#8892a3` | 烟灰。占位符、脚注、时间戳，可用于 bg、surface、surface-sunken。 |
| `--hao-hairline` | `#d5dae2` | `#2e3542` | 素线。列表行之间的分隔线，只作装饰，不承载含义。 |
| `--hao-border-control` | `#7e8696` | `#6c7687` | 控件描边与开关的关闭态轨道，在 bg、surface、surface-sunken 上都不低于 3:1。 |
| `--hao-tint` | `#1f4fa8` | `#8fb4ff` | 石青。全系统唯一的交互色：主按钮、链接、选中态、开关开启。作文字时可用于 bg、surface、tint-wash。 |
| `--hao-tint-hover` | `#1a4391` | `#a8c5ff` | tint 填充的按钮在鼠标悬停时的底色，上面仍放 on-tint。 |
| `--hao-on-tint` | `#ffffff` | `#0e1218` | tint 填充上的文字与图标。 |
| `--hao-tint-wash` | `#e3ebfa` | `#1c2a47` | 石青淡染。次级按钮底、选中行底、信息提示底，上面放 tint 或 ink 文字。 |
| `--hao-seal` | `#b83224` | `#ff8a75` | 朱砂。作文字和线：报错的字与描边、删除的菜单项、朱文印的边栏和字。一屏之内只出现一处；可用于 bg、surface、seal-wash。大块的填充用 seal-fill。 |
| `--hao-seal-fill` | `#b83224` | `#c8402e` | 作填充的朱砂：白文印的印面、带数字的角标、删除按钮、标志。昼间和 seal 同色；夜间 seal 为了当字用调亮了，大块铺开会又亮又粉，所以填充另用沉一档的朱。 |
| `--hao-seal-hover` | `#9c2a1e` | `#b83224` | seal-fill 填充的按钮在鼠标悬停时的底色，上面仍放 on-seal。 |
| `--hao-on-seal` | `#ffffff` | `#ffffff` | seal-fill 填充上的文字与图标。昼夜都是白的，白文印才是朱底白字。 |
| `--hao-seal-wash` | `#fbe9e6` | `#40201b` | 朱砂淡染。报错提示的底色，上面放 seal 或 ink 文字。 |
| `--hao-jade` | `#24705a` | `#7fd1b0` | 竹青。成功与完成，总是带一个字或图标，不单靠颜色区分。作文字时可用于 bg、surface、jade-wash。 |
| `--hao-on-jade` | `#ffffff` | `#0e1218` | jade 填充上的文字与图标。 |
| `--hao-jade-wash` | `#e2f2ec` | `#16332a` | 竹青淡染。成功提示的底色。 |
| `--hao-amber` | `#f2b632` | `#f5c451` | 藤黄。提醒类的填充色，只作底，不作浅色背景上的文字。 |
| `--hao-on-amber` | `#2a1d00` | `#2a1d00` | amber 填充上的文字与图标。 |
| `--hao-amber-ink` | `#8a5a00` | `#f5c451` | 提醒类的文字与图标，可用于 bg、surface、amber-wash。 |
| `--hao-amber-wash` | `#fbf1d9` | `#3a2e10` | 藤黄淡染。提醒提示的底色。 |
| `--hao-gold` | `#836427` | `#d9b36a` | 泥金。针脚、回纹、题签描边这类金线点缀；也可作落款与节气的小字，可用于 bg、surface、surface-sunken。不用于按钮和状态。 |
| `--hao-pattern` | `#cfdaf0` | `#2a3754` | 纹样色。海水纹等大面积底纹，画在 surface 或 bg 上，纯装饰，上面不压文字。 |
| `--hao-focus` | `{tint}` | `{tint}` | 键盘焦点环：2px 实线，外扩 2px，在所有表面上不低于 3:1。 |
| `--hao-material` | `rgba(255, 255, 255, 0.72)` | `rgba(24, 29, 38, 0.72)` | 毛玻璃材质。导航栏与标签栏的底，配合 20px 背景模糊。 |
| `--hao-scrim` | `rgba(14, 18, 24, 0.45)` | `rgba(0, 0, 0, 0.6)` | 弹层背后的遮罩。 |

## 间距

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-space-1` | `4px` | 图标与文字之间的最小间隙。 |
| `--hao-space-2` | `8px` | 标签内边距、同组控件的间隙。 |
| `--hao-space-3` | `12px` | 列表行的上下内边距。 |
| `--hao-space-4` | `16px` | 页面左右边距、列表行左右内边距。 |
| `--hao-space-5` | `20px` | 卡片内边距、按钮左右内边距。 |
| `--hao-space-6` | `24px` | 相邻分组之间的距离。 |
| `--hao-space-8` | `32px` | 大标题与内容之间的留白。 |
| `--hao-space-12` | `48px` | 页面分区之间的留白，也是封面的模数。 |

## 圆角

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-radius-xs` | `6px` | 勾选框、很小的标记。 |
| `--hao-radius-sm` | `8px` | 小图标、缩略图、焦点环的圆角。印章不用它，印面有自己的切角。 |
| `--hao-radius-md` | `12px` | 按钮、输入框、分段控件。 |
| `--hao-radius-lg` | `20px` | 卡片、列表组、提示条。 |
| `--hao-radius-xl` | `28px` | 底部弹层、整屏容器。 |
| `--hao-radius-full` | `999px` | 标签、开关、小号胶囊按钮；月洞一类的正圆。 |

## 阴影

| 变量 | 昼 | 夜 | 用途 |
| --- | --- | --- | --- |
| `--hao-shadow-card` | `0 1px 2px rgba(22, 27, 36, 0.05), 0 8px 24px rgba(22, 27, 36, 0.06)` | `0 0 0 1px rgba(255, 255, 255, 0.06), 0 1px 2px rgba(0, 0, 0, 0.4), 0 8px 24px rgba(0, 0, 0, 0.3)` | 卡片。很淡，像纸浮在案上。夜间黑影压在深底上看不见，所以多一圈很淡的亮边。 |
| `--hao-shadow-float` | `0 2px 6px rgba(22, 27, 36, 0.08), 0 16px 40px rgba(22, 27, 36, 0.14)` | `0 0 0 1px rgba(255, 255, 255, 0.1), 0 2px 6px rgba(0, 0, 0, 0.5), 0 16px 40px rgba(0, 0, 0, 0.5)` | 弹层、浮起的菜单。夜间同样多一圈亮边，浮层才有边界。 |
| `--hao-shadow-thumb` | `0 1px 3px rgba(22, 27, 36, 0.2)` | `0 1px 3px rgba(0, 0, 0, 0.5)` | 开关滑块、分段控件的选中块。 |

## 断点

窗口宽度分三级。媒体查询里不能用变量，写数值时照这里抄。

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-bp-medium` | `600px` | 从这里起是「中」：平板、窄的浏览器窗口。栅格 8 列。 |
| `--hao-bp-expanded` | `840px` | 从这里起是「宽」：桌面浏览器。栅格 12 列，标签栏换成顶部导航或侧栏。 |
| `--hao-bp-wide` | `1200px` | 内容区不再变宽，两侧留白增加。 |

## 布局

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-margin-compact` | `16px` | 窄屏（小于 600px）的页面左右边距，4 列栅格。 |
| `--hao-margin-medium` | `24px` | 中屏的页面左右边距，8 列栅格。 |
| `--hao-margin-expanded` | `32px` | 宽屏的页面左右边距，12 列栅格。 |
| `--hao-gutter` | `24px` | 栅格列间距；窄屏用 16px（space-4）。 |
| `--hao-content-max` | `1200px` | 内容区最大宽度，超过后居中。 |
| `--hao-measure` | `680px` | 长文正文的最大行宽，约合中文 38 字、英文 70 字符。 |

## 层级

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-z-nav` | `100` | 吸顶的导航栏、吸底的标签栏。 |
| `--hao-z-sheet` | `200` | 遮罩与底部弹层。 |
| `--hao-z-dialog` | `300` | 弹窗。 |
| `--hao-z-popover` | `350` | 菜单与气泡提示。比弹窗高，在弹窗里打开也看得见。 |
| `--hao-z-toast` | `400` | 轻提示，永远在最上面。 |

## 不透明度

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-opacity-disabled` | `0.4` | 禁用的控件整体降到这个不透明度。 |
| `--hao-opacity-pressed` | `0.85` | 按下的瞬间。 |

## 动效

动效只回应操作。离开比进入快三分之一；系统开启「减弱动态效果」时全部关掉。

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `--hao-dur-fast` | `120ms` | 按下、悬停、勾选。 |
| `--hao-dur-base` | `200ms` | 开关、分段滑块、标签切换。 |
| `--hao-dur-slow` | `320ms` | 弹窗、底部弹层、页面转场。 |
| `--hao-ease-out` | `cubic-bezier(.2, .8, .2, 1)` | 进入：快起慢停。 |
| `--hao-ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | 位置移动。 |

## 字体

字体样式是类名，写出来是 `class="hao-名字"`。带 `-en` 的是英文界面用的那一级；在 `<html lang="en">` 下标题会自动换成英文的字号与字距。

| 字体族 | 变量 | 值 |  |
| --- | --- | --- | --- |
| serif | `--hao-font-serif` | `"Newsreader", "Noto Serif SC", "Songti SC", "STSong", "Source Han Serif SC", Georgia, serif` | |
| sans | `--hao-font-sans` | `-apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", "Noto Sans SC", "Source Han Sans SC", "Helvetica Neue", "Microsoft YaHei", sans-serif` | |

| 类名 | 字号 / 行高 | 字重 | 字体族 | 用途 |
| --- | --- | --- | --- | --- |
| `hao-display` | 44px / 52px | 700 | serif | 封面与启动页，一屏至多一处。唯一随窗口变大的一级：中屏 56/64，宽屏 64/72。 |
| `hao-title-1` | 32px / 40px | 700 | serif | 页面大标题，对应 iOS 的 Large Title。长文的题目也用它。 |
| `hao-title-2` | 24px / 32px | 600 | serif | 卡片标题、分区标题、弹窗标题。 |
| `hao-title-3` | 20px / 28px | 600 | serif | 小标题：长文里的第三级、成组内容里每一项的题目。再小就不用宋体，改用 headline。 |
| `hao-display-en` | 48px / 52px | 500 | serif | 英文界面的封面与启动页，对应 display。一屏至多一处。中屏 60/64，宽屏 68/72。 |
| `hao-title-1-en` | 34px / 40px | 600 | serif | 英文界面的页面大标题，对应 title-1。 |
| `hao-title-2-en` | 24px / 28px | 600 | serif | 英文界面的卡片标题、分区标题，对应 title-2。 |
| `hao-title-3-en` | 20px / 24px | 600 | serif | 英文界面的小标题，对应 title-3。 |
| `hao-colophon` | 15px / 24px | 400 | serif | 英文落款与题记，斜体，代替竖排题签。只用于落款，不作正文强调以外的用途。 |
| `hao-headline` | 17px / 24px | 600 | sans | 按钮、导航栏标题、列表行里要强调的文字。 |
| `hao-body` | 17px / 28px | 400 | sans | 正文与列表行标题。 |
| `hao-body-en` | 17px / 24px | 400 | sans | 英文正文，行高比中文的 body 少 4px。其余黑体样式中英文共用。 |
| `hao-callout` | 15px / 24px | 400 | sans | 辅助说明、表单标签、分段控件。 |
| `hao-footnote` | 13px / 20px | 400 | sans | 列表组的页脚说明、时间戳。 |
| `hao-caption` | 12px / 16px | 500 | sans | 标签、标签栏文字、角标。只排单行。 |
