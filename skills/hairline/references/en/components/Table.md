# Table

A table for comparing many records side by side on wide screens.

`.hao-table-wrap` wraps the `<table class="hao-table">`. Headers use `<th scope="col">`; number columns take `hao-num` (right-aligned, tabular figures); minor columns take `hao-muted`. You supply the data.

- The table sits in a rounded `surface` container, with horizontal `hairline` rules only—no vertical lines, no zebra stripes.
- Text aligns left, numbers right, and each header matches the alignment of its column.
- The first column is the record’s name, in `ink`; the other columns stay as quiet as they can.
- Show status with a `Tag`, never color alone.
- No tables on narrow screens: the same data becomes a `ListGroup`, one row per record, with minor information moved into the subtitle.
- Past twenty rows, paginate or load as needed.
- Beneath the header runs the thick-and-thin double rule (文武线)—one thick rule above, one thin below—the way book-page borders are drawn. It is the only place in the table that uses it; rows are still separated by `hairline`.

**Accessibility**

- Keep a native `<table>`: the rounded container is `.hao-table-wrap`’s business, and the row-and-column mapping a screen reader relies on comes from the table structure. Don’t break it into a `<div>` grid.
- `hao-num` and `hao-muted` change only alignment, color, and type size—never the semantics of a cell.

## Markup

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

### Chinese

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
