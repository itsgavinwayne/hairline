# 英文稿的术语表与翻译要求

这份文件不会生成到网站上。`source/en/` 里的英文稿都照它翻；改了中文稿，记得来这里改对应的英文稿。
`python3 build_site.py` 在缺英文稿时会报错。

## 翻译要求

1. 译成自然、平实的美式英语技术文档：短句，动词在前，用 you 称呼读者，可以用缩写（can’t、don’t）。不要逐字硬译，也不要加原文没有的内容，不要删内容。
2. 标题和表头一律句首大写（sentence case）：“Day and night themes”，不写 “Day And Night Themes”。不用全大写。
3. 不用感叹号。不用 zen、harmony、journey、ancient wisdom、oriental、mystical、timeless、elegant 这类词。「东方的气韵」译作 “an East Asian sensibility”。
4. 引号用弯引号 “ ”，撇号用 ’，范围用连接号（7–9 PM）。反引号里的代码不动，里面保持直引号。
5. 反引号里的东西原样保留：令牌名（`tint`、`space-4`）、类名（`hao-btn--seal`）、属性名（`data-hao-open`）、组件名（`Button`）、文件名、代码块。代码块（```）整块照抄，只把代码注释和示例文案里的中文译成英文。
6. Markdown 结构原样保留：标题层级、表格的行列数、列表、加粗（`**…**`）、链接。不要用 `*斜体*`、不要用 `_斜体_`，生成脚本不认。不要加一级标题以外的新标题。
7. 中文的「」引用：
   - 引的是界面文案（「保存修改」「已发布」），译成英文界面该有的说法，放进弯引号：“Save changes”、“Published”。
   - 引的是本系统的规矩或章节名，照下面的表译，放进弯引号：“the three rules” 不加引号也可以，章节名加：see “Seal design”。
   - 引的是印章上的字、要人照着写的汉字、或者专门在讲汉字本身（「讫」「印」「永」「一、二、三」），保留汉字，第一次出现时写成 “done (讫)” 这种英文在前、汉字在后的样子。
   - 原文在对比中文和英文两种写法时（比如 english.md 的对照表、组件说明里「中文写…，英文写…」），中文例子保留汉字不译。
8. 没有对应词的专名（节气、干支、朝代、画家、器物）第一次出现英文在前、汉字在后：“Minor Snow (小雪)”、“Ma Yuan (马远)”，之后只写英文。干支年写 “the Bingwu year”。能直译成平常词的就直译，不留拼音。
9. 数字和单位照抄（44px、1.5px、3:1）。日期用美式：November 18、Nov 18、7:12 AM。
10. 每行 Markdown 对应原文的一行，不要自己折行。

## 术语

| 中文 | 英文 |
| --- | --- |
| 毫 | Hairline（第一次出现写 Hairline (毫)） |
| iOS 的克制，一点东方的气韵 | The restraint of iOS, with an East Asian sensibility |
| 三条规矩 | the three rules |
| 朱砂一处 | One touch of cinnabar |
| 一屏一景 | One scene per screen |
| 形随控件 | Shape follows the control |
| 三条原则 | three principles |
| 先留白，再落笔 | Leave room, then write |
| 石青行事，朱砂点睛 | Azurite does the work. Cinnabar marks the point. |
| 结构听 iOS 的，气质听东方的 | iOS sets the structure. East Asia sets the character. |
| 五条审美标准 / 五条标准 | the five standards |
| 素、空、淡、细、偏 | plain (素), empty (空), pale (淡), fine (细), off-center (偏) |
| 景 | scene |
| 意象 | motif |
| 小品 | vignette |
| 纹样 | pattern |
| 留白 | white space（动词：leave room） |
| 印章 / 印 | seal |
| 印文 | seal text（印上的那个字：the seal character） |
| 印面 | seal face |
| 印稿 | seal artwork |
| 白文 / 朱文 | intaglio seal (白文) / relief seal (朱文)；之后写 intaglio / relief |
| 边栏 | border |
| 篆字 / 篆书 | seal script |
| 盖印 | stamp（动词 stamp，名词 the stamp） |
| 落款 | signature |
| 年款 | date line |
| 题签 | title slip |
| 留气口 | breathing gap |
| 提勾 | the upward hook stroke（勾选标记：check） |
| 月相 / 渐圆的月 | moon phase / a waxing moon |
| 朔 / 望 | new moon / full moon |
| 朱砂 | cinnabar（指那种红色；令牌是 `seal`） |
| 石青 | azurite（令牌是 `tint`） |
| 泥金 | gold ink（令牌是 `gold`） |
| 月白 | moon white |
| 瓷白 | porcelain white |
| 云灰 | cloud gray |
| 玄青 | blue-black |
| 黛 | slate |
| 烟灰 | smoke gray |
| 素线 | plain rule |
| 竹青 | bamboo green |
| 藤黄 | gamboge |
| 淡染 | wash（石青淡染：azurite wash） |
| 宣纸 | Xuan paper |
| 宋体 | Song typeface（字体名照写：Noto Serif SC、Songti SC） |
| 黑体 | sans-serif（字体名照写：PingFang SC、Noto Sans SC） |
| 思源宋体 / 思源黑体 / 苹方 | Noto Serif SC / Noto Sans SC / PingFang SC |
| 衬线 | serif |
| 装裱 | mounting |
| 手卷 | handscroll |
| 展卷 | unrolling |
| 笺纸 | letter paper |
| 隔水 | spacer band (隔水) |
| 针脚 | stitch |
| 回纹 | fret |
| 海水纹 | wave pattern |
| 鱼尾 | fishtail mark (鱼尾) |
| 竖排 | vertical setting |
| 札记 | note |
| 案头 | desk |
| 昼 / 夜 | day / night |
| 昼间主题 / 夜间主题 | day theme / night theme |
| 令牌 | token |
| 组件 | component |
| 示例屏 | sample screen |
| 变体 / 零件 | variant / part |
| 主按钮 / 次级按钮 | primary button / secondary button |
| 轻提示 | toast |
| 弹窗 | dialog |
| 底部弹层 | sheet |
| 浮层 | overlay |
| 角标 | badge |
| 空状态 | empty state |
| 分段控件 | segmented control |
| 触控区 | touch target |
| 焦点环 | focus ring |
| 读屏软件 | screen reader |
| 减弱动态效果 | Reduce Motion |
| 办事的页面 / 功能页 | task screens |
| 平面 / 平面物料 | print / printed pieces |
| 产物 | output |
| 节气 | solar term |
| 干支 | sexagenary cycle |
| 农历 | lunar calendar |
| 宋代 | the Song dynasty |

## 章节名（正文里提到别的章节时照这个写）

| 中文 | 英文 |
| --- | --- |
| 安装 | Install |
| 快速上手 | Quick start |
| 设计原则 | Design principles |
| 审美标准与出处 | Aesthetic standards and sources |
| 产物分类 | Kinds of output |
| 参考与取舍 | References and trade-offs |
| 网页与大屏 | Web and large screens |
| 行为与脚本 | Behavior and scripts |
| 英文界面 | English interfaces |
| 阅读与内容 | Reading and content |
| 平面与印刷 | Print and graphics |
| 图形与素材 | Imagery and assets |
| 印稿规范 | Seal design |
| 命名对照 | Naming reference |

## 分组名

| 中文 | 英文 |
| --- | --- |
| 手册 / 开发指南 / 指南 | Guide |
| 基础 | Foundations |
| 界面 | Interface |
| 阅读 | Reading |
| 平面 | Print |
| 品牌 | Brand |
| 示例 | Examples |
| 图标 | Icons |
| 纹样 | Patterns |
| 动效 | Motion |
| 操作 | Actions |
| 表单 | Forms |
| 导航 | Navigation |
| 内容 | Content |
| 反馈 | Feedback |
| 浮层 | Overlays |
| 状态 | Status |
