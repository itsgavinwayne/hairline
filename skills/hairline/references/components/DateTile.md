# DateTile · 日历页

一张小小的日历页，把一个日期当成图形摆在日程或事件旁边。

`.hao-date` 里三行：`.hao-date__m` 月份、`.hao-date__d` 日、`.hao-date__w` 星期。当天是节气时，第三行换成节气名并加 `hao-date__w--term`。

- 样子取自一天撕一页的老式日历：上面一条色带写月份，中间大大的日子。
- 月份用汉字（十一月），日子用宋体的阿拉伯数字，星期写「周三」。英文界面写 “Nov” 和 “Wed”。
- 只在日期本身是重点时用：日程列表、活动详情、提醒。普通的时间戳写成文字。
- 加 `role="img"` 和 `aria-label` 把日期完整读出来；旁边已有完整日期文字时改为 `aria-hidden="true"`。
- 一屏里成列出现时，每行一个，左对齐。
- 想带上农历，在最后加一行 `.hao-date__l`（如「十月初十」），用历法数据生成，不要手写。英文界面不加这一行。
- 顶上的色带两端各有一个小孔，是撕页日历的装订孔。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-date" role="img" aria-label="11 月 18 日，星期三"><span class="hao-date__m">十一月</span><span class="hao-date__d">18</span><span class="hao-date__w">周三</span></span><span class="hao-date" role="img" aria-label="11 月 18 日，星期三，农历十月初十"><span class="hao-date__m">十一月</span><span class="hao-date__d">18</span><span class="hao-date__w">周三</span><span class="hao-date__l">十月初十</span></span><span class="hao-date" role="img" aria-label="11 月 22 日，小雪，农历十月十四"><span class="hao-date__m">十一月</span><span class="hao-date__d">22</span><span class="hao-date__w hao-date__w--term">小雪</span><span class="hao-date__l">十月十四</span></span><div><p style="margin:0;font:600 17px/24px var(--hao-font-sans)">读书会：《园冶》</p><p style="margin:0;font:400 15px/24px var(--hao-font-sans);color:var(--hao-ink-secondary)">晚上 7:30，线上</p></div></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-date" role="img" aria-label="Wednesday, November 18"><span class="hao-date__m">Nov</span><span class="hao-date__d">18</span><span class="hao-date__w">Wed</span></span><span class="hao-date" role="img" aria-label="November 22, Minor Snow"><span class="hao-date__m">Nov</span><span class="hao-date__d">22</span><span class="hao-date__w hao-date__w--term">Minor Snow</span></span><div><p style="margin:0;font:600 17px/24px var(--hao-font-sans)">Book club: The Craft of Gardens</p><p style="margin:0;font:400 15px/24px var(--hao-font-sans);color:var(--hao-ink-secondary)">7:30 PM, online</p></div></div>
```
