# Banner · 提示条

页面内的一条提示，说明发生了什么、接下来怎么办。

`.hao-banner` 里放一个 20px 的图标和一段文字，标题用 `<strong>`。色调类：默认（信息）、`hao-banner--jade`（成功）、`hao-banner--amber`（提醒）、`hao-banner--seal`（出错）。你提供图标、标题和说明。

- 每种色调配固定的图标：`hao-icon--info`、`hao-icon--success`、`hao-icon--warning`、`hao-icon--error`。图标和标题一起表达状态，不只靠底色。
- 标题说结果（「已发布」），说明说影响或下一步。不道歉，不用感叹号。
- 出错用 `role="alert"`，其余用 `role="status"`。
- 一屏最多一条；多条消息排队出现。

## 标记

### 中文

```html
<div class="hao-stack">
  <div class="hao-banner"><i class="hao-icon hao-icon--info" aria-hidden="true"></i><div><strong>新版本可用</strong>更新后可以在夜间主题下使用印章。</div></div>
  <div class="hao-banner hao-banner--jade" role="status"><i class="hao-icon hao-icon--success" aria-hidden="true"></i><div><strong>已发布</strong>这条札记现在所有人可见。</div></div>
  <div class="hao-banner hao-banner--amber"><i class="hao-icon hao-icon--warning" aria-hidden="true"></i><div><strong>存储空间快满了</strong>还能再存大约 20 条带图的札记。</div></div>
  <div class="hao-banner hao-banner--seal" role="alert"><i class="hao-icon hao-icon--error" aria-hidden="true"></i><div><strong>没连上网络</strong>修改已存在本机，连上后会自动同步。</div></div>
</div>
```

### English

```html
<div class="hao-stack">
  <div class="hao-banner"><i class="hao-icon hao-icon--info" aria-hidden="true"></i><div><strong>Update available</strong>The new version adds the seal to the night theme.</div></div>
  <div class="hao-banner hao-banner--jade" role="status"><i class="hao-icon hao-icon--success" aria-hidden="true"></i><div><strong>Published</strong>Everyone can now see this note.</div></div>
  <div class="hao-banner hao-banner--amber"><i class="hao-icon hao-icon--warning" aria-hidden="true"></i><div><strong>Storage is almost full</strong>There’s room for about 20 more notes with images.</div></div>
  <div class="hao-banner hao-banner--seal" role="alert"><i class="hao-icon hao-icon--error" aria-hidden="true"></i><div><strong>Can’t reach the network</strong>Your changes are saved on this device and will sync when you’re back online.</div></div>
</div>
```
