# EmptyState · 空状态

一块区域里没有内容可显示时的画面：一幅圆窗里的小品、一句现状、一句下一步。

`.hao-empty` 里依次放一幅 `.hao-scene`、`.hao-empty__title`（宋体）、`.hao-empty__body`、一个可选的按钮。文字由你提供；小品从下面五幅里选。

**五幅小品，各管一种情况**

| 小品 | 画的是 | 用在 |
| --- | --- | --- |
| 月 | 一轮月悬在水上 | 第一次来，这里还什么都没有 |
| 舟 | 远山下一叶孤舟 | 搜索或筛选没有结果 |
| 山 | 两重远山，中间隔着雾 | 断网，够不着 |
| 亭 | 一座空亭 | 都做完了，可以歇了 |
| 灯 | 一盏提灯 | 出错了，没能载入 |

- 每幅都画在一个圆窗里，像从月洞门望出去。主体用 `tint` 细线，远景和水用 `pattern` 淡染，整幅只有这两种颜色。
- 小品就是这一屏的「景」（见手册的「三条规矩」）：同屏不再用纹样和展示件，也不放印章。
- 一种情况固定一幅，全产品统一，不要按心情换。不新增别的小品。
- 默认 96px；整页的空状态用 `hao-scene--lg`（160px）。小品是装饰，加 `aria-hidden="true"`。
- 标题说现状，说明说下一步，按钮就是那一步。「都做完了」不需要按钮。
- 第一次使用给主按钮，其余情况用 `hao-btn--tinted`。搜索无结果时把人搜的词写进标题。
- 不用「哎呀」「空空如也」这类俏皮话，不用感叹号。出错时说清不是使用者的问题。
- 只是某一块加载失败、页面其余部分还在时，用提示条；整页都没有内容时才用「灯」。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-4);align-items:flex-start"><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="wash" cx="60" cy="36" r="13"/><path class="far" d="M8 70q7-4 14 0t14 0 14 0 14 0 14 0 14 0M14 79q7-4 14 0t14 0 14 0 14 0 14 0M24 88q7-4 14 0t14 0 14 0 14 0"/></svg><h2 class="hao-empty__title">还没有札记</h2><p class="hao-empty__body">写下第一条，它会出现在这里。</p><button class="hao-btn">写一条札记</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M4 50l14-10 10 6 14-14 16 16 12-7 22 11"/><path d="M30 62h36l-6 8H36zM40 62q8-13 16 0M48 49V38"/><path class="far" d="M12 78h20M40 80h28M74 77h12M26 87h18M54 88h20"/></svg><h2 class="hao-empty__title">没有找到「立春」</h2><p class="hao-empty__body">换一个词试试，或者看看全部札记。</p><button class="hao-btn hao-btn--tinted">查看全部札记</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M-2 52l18-20 12 11 16-25 18 27 14-13 22 22"/><path d="M-2 72l22-16 14 9 20-18 22 20 22-9"/><path class="far" d="M10 64h16M34 62h10M66 64h18M18 82h24M52 84h30"/></svg><h2 class="hao-empty__title">没连上网络</h2><p class="hao-empty__body">已有的札记还能看，新的修改会在连上后同步。</p><button class="hao-btn hao-btn--tinted">再试一次</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path d="M24 46q14-3 24-18 10 15 24 18M48 28v-6M31 46h34M35 46v24M61 46v24M27 70h42"/><path class="far" d="M8 76h80M20 84h20M52 85h26"/></svg><h2 class="hao-empty__title">今天的都做完了</h2><p class="hao-empty__body">没有待办了，歇一会儿。</p></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="far wash" cx="48" cy="45" r="26" style="stroke:none"/><path d="M48 12v10M41 22h14M41 22q-10 13 0 28h14q10-15 0-28M42 50h12M48 50v13M45 63h6"/><path class="far" d="M48 30v12"/></svg><h2 class="hao-empty__title">没能载入</h2><p class="hao-empty__body">出了点问题，不是你的操作造成的。</p><button class="hao-btn hao-btn--tinted">重新载入</button></div></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-4);align-items:flex-start"><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="wash" cx="60" cy="36" r="13"/><path class="far" d="M8 70q7-4 14 0t14 0 14 0 14 0 14 0 14 0M14 79q7-4 14 0t14 0 14 0 14 0 14 0M24 88q7-4 14 0t14 0 14 0 14 0"/></svg><h2 class="hao-empty__title">No notes yet</h2><p class="hao-empty__body">Write your first one and it will show up here.</p><button class="hao-btn">Write a note</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M4 50l14-10 10 6 14-14 16 16 12-7 22 11"/><path d="M30 62h36l-6 8H36zM40 62q8-13 16 0M48 49V38"/><path class="far" d="M12 78h20M40 80h28M74 77h12M26 87h18M54 88h20"/></svg><h2 class="hao-empty__title">No results for “spring”</h2><p class="hao-empty__body">Try another word, or browse all notes.</p><button class="hao-btn hao-btn--tinted">View all notes</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path class="far" d="M-2 52l18-20 12 11 16-25 18 27 14-13 22 22"/><path d="M-2 72l22-16 14 9 20-18 22 20 22-9"/><path class="far" d="M10 64h16M34 62h10M66 64h18M18 82h24M52 84h30"/></svg><h2 class="hao-empty__title">Can’t reach the network</h2><p class="hao-empty__body">You can still read your notes. New changes will sync when you’re back online.</p><button class="hao-btn hao-btn--tinted">Try again</button></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><path d="M24 46q14-3 24-18 10 15 24 18M48 28v-6M31 46h34M35 46v24M61 46v24M27 70h42"/><path class="far" d="M8 76h80M20 84h20M52 85h26"/></svg><h2 class="hao-empty__title">All done for today</h2><p class="hao-empty__body">Nothing left to do. Take a break.</p></div><div class="hao-empty" style="width:250px;padding:var(--hao-space-6) var(--hao-space-3)"><svg class="hao-scene " viewBox="0 0 96 96" aria-hidden="true"><circle class="far wash" cx="48" cy="45" r="26" style="stroke:none"/><path d="M48 12v10M41 22h14M41 22q-10 13 0 28h14q10-15 0-28M42 50h12M48 50v13M45 63h6"/><path class="far" d="M48 30v12"/></svg><h2 class="hao-empty__title">Couldn’t load this</h2><p class="hao-empty__body">Something went wrong, and it wasn’t anything you did.</p><button class="hao-btn hao-btn--tinted">Reload</button></div></div>
```
