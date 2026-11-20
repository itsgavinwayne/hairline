# Breadcrumb · 面包屑

一行路径，告诉人现在在哪一层、怎么回到上面。用在宽屏、层级三层以上的地方。

`<nav aria-label="位置">` 里放 `<ol class="hao-crumbs">`，前面各级是链接，最后一级是当前页，不是链接，加 `aria-current="page"`。

- 当前页用 `ink`，上级用 `ink-secondary`，中间是小箭头。
- 层级不到三层时不用，导航栏的返回就够了。
- 窄屏不用面包屑，用导航栏的返回按钮。
- 路径太长时省略中间的层级，保留第一级和最后两级。

## 标记

### 中文

```html
<nav aria-label="位置"><ol class="hao-crumbs"><li><a href="#">札记</a></li><li><a href="#">读书</a></li><li aria-current="page">《园冶》读书笔记</li></ol></nav>
```

### English

```html
<nav aria-label="Location"><ol class="hao-crumbs"><li><a href="#">Notes</a></li><li><a href="#">Reading</a></li><li aria-current="page">Notes on The Craft of Gardens</li></ol></nav>
```
