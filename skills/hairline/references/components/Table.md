# Table · 表格

在宽屏上并排比较多条记录的表格。

`.hao-table-wrap` 包住 `<table class="hao-table">`。表头用 `<th scope="col">`；数字列加 `hao-num`（右对齐、等宽数字）；次要的列加 `hao-muted`。数据由你提供。

- 表格放在 `surface` 的圆角容器里，只有横向的 `hairline`，没有竖线和斑马纹。
- 文字左对齐，数字右对齐，表头和它那一列对齐方式一致。
- 第一列是这条记录的名字，用 `ink`；其余列能淡则淡。
- 状态用 `Tag`，不单靠颜色。
- 窄屏不用表格：同样的数据改用 `ListGroup`，每条记录一行，次要信息放到副标题里。
- 超过二十行时分页或按需加载。
- 表头下面是「文武线」：上面一道粗线，下面一道细线，是书页边栏的画法。表格里只有这一处用它，行与行之间仍是 `hairline`。

**无障碍**

- 保持原生 `<table>`：圆角容器是 `.hao-table-wrap` 的事，行列的对应关系读屏靠表格结构，不要拆成 `<div>` 网格。
- `hao-num` 和 `hao-muted` 只改对齐、颜色和字号，不改单元格的语义。

## 标记

### 中文

```html
<div class="hao-table-wrap" style="max-width:720px">
<table class="hao-table">
  <thead><tr><th scope="col">标题</th><th scope="col">文件夹</th><th scope="col">状态</th><th scope="col" class="hao-num">字数</th><th scope="col">上次编辑</th></tr></thead>
  <tbody>
    <tr><td>晨间札记</td><td class="hao-muted">随笔</td><td><span class="hao-tag hao-tag--jade">已发布</span></td><td class="hao-num">486</td><td class="hao-muted">今天 07:12</td></tr>
    <tr><td>《园冶》读书笔记</td><td class="hao-muted">读书</td><td><span class="hao-tag hao-tag--tint">进行中</span></td><td class="hao-num">2,140</td><td class="hao-muted">昨天</td></tr>
    <tr><td>苏州三日</td><td class="hao-muted">旅行</td><td><span class="hao-tag">草稿</span></td><td class="hao-num">912</td><td class="hao-muted">11 月 12 日</td></tr>
  </tbody>
</table>
</div>
```

### English

```html
<div class="hao-table-wrap" style="max-width:720px">
<table class="hao-table">
  <thead><tr><th scope="col">Title</th><th scope="col">Folder</th><th scope="col">Status</th><th scope="col" class="hao-num">Words</th><th scope="col">Last edited</th></tr></thead>
  <tbody>
    <tr><td>Morning note</td><td class="hao-muted">Essays</td><td><span class="hao-tag hao-tag--jade">Published</span></td><td class="hao-num">486</td><td class="hao-muted">Today, 7:12 AM</td></tr>
    <tr><td>Notes on The Craft of Gardens</td><td class="hao-muted">Reading</td><td><span class="hao-tag hao-tag--tint">In progress</span></td><td class="hao-num">2,140</td><td class="hao-muted">Yesterday</td></tr>
    <tr><td>Three days in Suzhou</td><td class="hao-muted">Travel</td><td><span class="hao-tag">Draft</span></td><td class="hao-num">912</td><td class="hao-muted">Nov 12</td></tr>
  </tbody>
</table>
</div>
```
