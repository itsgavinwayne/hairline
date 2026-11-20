# Banner

A notice inside the page that says what happened and what to do next.

`.hao-banner` holds a 20px icon and a run of text, with the title in `<strong>`. Tint classes: default (information), `hao-banner--jade` (success), `hao-banner--amber` (warning), `hao-banner--seal` (error). You provide the icon, the title, and the message.

- Each tint has its fixed icon: `hao-icon--info`, `hao-icon--success`, `hao-icon--warning`, `hao-icon--error`. Icon and title carry the state together, not the background alone.
- The title gives the outcome (“Published”); the message gives the effect or the next step. No apologies, no exclamation marks.
- Use `role="alert"` for errors and `role="status"` for everything else.
- At most one per screen; when several messages arrive, they take their turn.

## Markup

### English

```html
<div class="hao-stack">
  <div class="hao-banner"><i class="hao-icon hao-icon--info" aria-hidden="true"></i><div><strong>Update available</strong>The new version adds the seal to the night theme.</div></div>
  <div class="hao-banner hao-banner--jade" role="status"><i class="hao-icon hao-icon--success" aria-hidden="true"></i><div><strong>Published</strong>Everyone can now see this note.</div></div>
  <div class="hao-banner hao-banner--amber"><i class="hao-icon hao-icon--warning" aria-hidden="true"></i><div><strong>Storage is almost full</strong>There’s room for about 20 more notes with images.</div></div>
  <div class="hao-banner hao-banner--seal" role="alert"><i class="hao-icon hao-icon--error" aria-hidden="true"></i><div><strong>Can’t reach the network</strong>Your changes are saved on this device and will sync when you’re back online.</div></div>
</div>
```

### Chinese

```html
<div class="hao-stack">
  <div class="hao-banner"><i class="hao-icon hao-icon--info" aria-hidden="true"></i><div><strong>新版本可用</strong>更新后可以在夜间主题下使用印章。</div></div>
  <div class="hao-banner hao-banner--jade" role="status"><i class="hao-icon hao-icon--success" aria-hidden="true"></i><div><strong>已发布</strong>这条札记现在所有人可见。</div></div>
  <div class="hao-banner hao-banner--amber"><i class="hao-icon hao-icon--warning" aria-hidden="true"></i><div><strong>存储空间快满了</strong>还能再存大约 20 条带图的札记。</div></div>
  <div class="hao-banner hao-banner--seal" role="alert"><i class="hao-icon hao-icon--error" aria-hidden="true"></i><div><strong>没连上网络</strong>修改已存在本机，连上后会自动同步。</div></div>
</div>
```
