# Tooltip · 气泡提示

鼠标悬停或键盘聚焦时出现的一句说明，给只有图标的按钮起名字。

`<span class="hao-tip" role="tooltip">`，触发它的元素用 `aria-describedby` 指向它。文字由你提供。

- 只放补充信息；必须看到的内容不要放进来，因为触屏上没有悬停。
- 一句话，不超过两行，不放链接和按钮。
- 悬停半秒后出现，移开后消失；键盘聚焦时同样出现。
- 颜色是反的：`ink` 作底，`bg` 作字，和轻提示一致。

**行为**（加载了行为脚本时）

- 在任何元素上写 `data-hao-tip="说明文字"`。鼠标停半秒后出现，移开后消失，鼠标可以移到提示上面而不让它收起；用键盘聚焦到它时立刻出现，离开消失；按 Esc 也会收起。
- 提示出现在元素上方正中，上面放不下就到下面。脚本会用 `aria-describedby` 把它和元素连起来。

## 标记

### 中文

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-tip" role="tooltip">导出为 PDF</span><span class="hao-tip" role="tooltip">上次同步在三分钟前，下拉可以立即同步</span></div>
<div class="hao-row" style="margin-top:var(--hao-space-8)"><button class="hao-btn hao-btn--tinted" data-hao-tip="导出为 PDF"><i class="hao-icon hao-icon--download" aria-hidden="true"></i>导出</button><button class="hao-btn hao-btn--tinted" data-hao-tip="上次同步在三分钟前">同步</button></div>
```

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-tip" role="tooltip">Export as PDF</span><span class="hao-tip" role="tooltip">Last synced 3 minutes ago. Pull down to sync now.</span></div>
<div class="hao-row" style="margin-top:var(--hao-space-8)"><button class="hao-btn hao-btn--tinted" data-hao-tip="Export as PDF"><i class="hao-icon hao-icon--download" aria-hidden="true"></i>Export</button><button class="hao-btn hao-btn--tinted" data-hao-tip="Last synced 3 minutes ago">Sync</button></div>
```
