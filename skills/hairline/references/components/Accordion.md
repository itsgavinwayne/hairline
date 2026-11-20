# Accordion · 折叠面板

点一下标题展开下面的内容，用来收起次要的、不是每个人都要看的信息。

`.hao-acc` 里放若干原生的 `<details>`，每个有一个 `<summary>` 和一段 `.hao-acc__body`。标题和内容由你提供。

- 用原生 `<details>`，键盘和读屏不用另外处理。
- 标题写成一个完整的问题或一个名词短语，让人不展开也知道里面是什么。
- 适合常见问题、高级设置。主要内容不要藏进来。
- 各项可以同时展开，不强制只开一个。
- 展开后标题加粗，箭头翻转。
- 展开时内容像经折装的册页那样从上边折下来打开，320 毫秒。系统开启「减弱动态效果」时直接出现。

## 标记

### 中文

```html
<div class="hao-acc" style="max-width:460px">
  <details open><summary>札记会同步到哪些设备</summary><p class="hao-acc__body">登录同一个账号的所有设备。同步在连上网络后自动进行，不需要手动操作。</p></details>
  <details><summary>删除的札记能找回吗</summary><p class="hao-acc__body">删除后会在「最近删除」里保留三十天。</p></details>
  <details><summary>怎么导出全部内容</summary><p class="hao-acc__body">在设置里选择「导出」，可以得到一个包含全部札记的压缩包。</p></details>
</div>
```

### English

```html
<div class="hao-acc" style="max-width:460px">
  <details open><summary>Which devices do notes sync to</summary><p class="hao-acc__body">Every device signed in to the same account. Syncing happens on its own once you’re online.</p></details>
  <details><summary>Can I get a deleted note back</summary><p class="hao-acc__body">Deleted notes stay in Recently Deleted for 30 days.</p></details>
  <details><summary>How do I export everything</summary><p class="hao-acc__body">Choose Export in Settings to download an archive of all your notes.</p></details>
</div>
```
