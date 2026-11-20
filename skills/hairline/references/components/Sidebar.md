# Sidebar · 侧边栏

宽屏左侧的导航栏，顶层区域多于五个，或者下面还有一层（文件夹）时用它代替顶部导航。

`<nav class="hao-side">` 里放若干 `.hao-side__item`（图标加文字，可带一个计数），用 `.hao-side__label` 分组；当前页 `aria-current="page"`。

- 宽 240px，直接坐在 `bg` 上，不加底色和阴影；右边的内容区才用 `surface`。
- 当前项是 `tint-wash` 底、`tint` 字；其余是 `ink`。
- 计数用 `hao-badge--quiet`。侧栏里不出现朱砂角标，除非真有需要处理的事。
- 窄屏上侧栏收起，顶层的三到五项进 `TabBar`，其余进「我的」。
- 产品名和小印放在侧栏最上方，不放在每一页里。

## 标记

### 中文

```html
<nav class="hao-side" aria-label="主导航" style="border-radius:var(--hao-radius-lg);background:var(--hao-bg);border:1px solid var(--hao-hairline)">
  <a class="hao-side__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>今日</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>札记<span class="hao-badge hao-badge--quiet">38</span></a>
  <p class="hao-side__label">文件夹</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>随笔</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>读书</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>旅行</a>
  <p class="hao-side__label">其他</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--settings" aria-hidden="true"></i>设置</a>
</nav>
```

### English

```html
<nav class="hao-side" aria-label="Main" style="border-radius:var(--hao-radius-lg);background:var(--hao-bg);border:1px solid var(--hao-hairline)">
  <a class="hao-side__item" href="#" aria-current="page"><i class="hao-icon hao-icon--today" aria-hidden="true"></i>Today</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--notes" aria-hidden="true"></i>Notes<span class="hao-badge hao-badge--quiet">38</span></a>
  <p class="hao-side__label">Folders</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Essays</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Reading</a>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--folder" aria-hidden="true"></i>Travel</a>
  <p class="hao-side__label">Other</p>
  <a class="hao-side__item" href="#"><i class="hao-icon hao-icon--settings" aria-hidden="true"></i>Settings</a>
</nav>
```
