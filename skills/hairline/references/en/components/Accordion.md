# Accordion

Tap a title to expand the content below. Use it to tuck away secondary information that not everyone needs to read.

`.hao-acc` holds a few native `<details>` elements, each with a `<summary>` and a `.hao-acc__body`. You provide the titles and the content.

- Use the native `<details>` element, so keyboard and screen readers need no extra handling.
- Write the title as a complete question or a noun phrase, so a reader knows what’s inside without expanding it.
- Good for frequently asked questions and advanced settings. Don’t hide main content in one.
- Several items can be open at once; don’t force only one.
- The open title turns bold, and the arrow flips.
- When it opens, the content folds down from the top like the leaf of a concertina-bound booklet (经折装), over 320ms; with Reduce Motion on, it simply appears.

## Markup

### English

```html
<div class="hao-acc" style="max-width:460px">
  <details open><summary>Which devices do notes sync to</summary><p class="hao-acc__body">Every device signed in to the same account. Syncing happens on its own once you’re online.</p></details>
  <details><summary>Can I get a deleted note back</summary><p class="hao-acc__body">Deleted notes stay in Recently Deleted for 30 days.</p></details>
  <details><summary>How do I export everything</summary><p class="hao-acc__body">Choose Export in Settings to download an archive of all your notes.</p></details>
</div>
```

### Chinese

```html
<div class="hao-acc" style="max-width:460px">
  <details open><summary>札记会同步到哪些设备</summary><p class="hao-acc__body">登录同一个账号的所有设备。同步在连上网络后自动进行，不需要手动操作。</p></details>
  <details><summary>删除的札记能找回吗</summary><p class="hao-acc__body">删除后会在「最近删除」里保留三十天。</p></details>
  <details><summary>怎么导出全部内容</summary><p class="hao-acc__body">在设置里选择「导出」，可以得到一个包含全部札记的压缩包。</p></details>
</div>
```
