# Stamp

When something important is finished, a seal comes down. This is the only moment of ceremony in the whole system.

Inside `.hao-stamp`, in order: a `.hao-seal.hao-seal--lg.hao-seal--outline.hao-seal--stamp`, the `.hao-stamp__title`, and the `.hao-stamp__body`; the title and body take `hao-stamp__text` and fade in after the seal lands. You supply the text.

- The seal text is “done (讫)”. In the old days, when a receipt or a document was settled, it was stamped “received (收讫)” or “verified (验讫)”—this matter is closed. The seal text is fixed; don’t swap in another character, and keep it in English interfaces too.
- The motion is one landing: the seal presses down from slightly above, pauses briefly, and settles with a small bounce, 420ms in all; then the text fades in. It plays once, with no loop.
- Use it only where something is truly finished: publishing, submitting, completing a payment, finishing a book. Small actions like saving or copying take a toast. At most once per flow.
- It is the cinnabar of that screen: no other seal and no red badge alongside it.
- Add `role="status"`; the seal itself takes `aria-hidden="true"`, and the title carries the meaning.
- When Reduce Motion is on, the motion is skipped, and the seal and text simply appear.
- Use relief (the fine border); intaglio is too heavy to sit beside the text.
- The 讫 character is a Song typeface placeholder. To make it seal script, follow “Seal design” in the guide and prepare a relief seal artwork for the traditional character 訖.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <div class="hao-stamp" style="width:300px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)" role="status">
    <span class="hao-seal hao-seal--lg hao-seal--outline hao-seal--stamp" id="st2" lang="zh" aria-hidden="true">讫</span>
    <h2 class="hao-stamp__title hao-stamp__text" id="tt2">Published</h2>
    <p class="hao-stamp__body hao-stamp__text" id="tb2">Everyone can now see this note.</p>
  </div>
  <button class="hao-btn hao-btn--tinted" data-replay="st2:hao-seal--stamp,tt2:hao-stamp__text,tb2:hao-stamp__text">Stamp again</button>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-8)">
  <div class="hao-stamp" style="width:300px;border-radius:var(--hao-radius-lg);background:var(--hao-surface)" role="status">
    <span class="hao-seal hao-seal--lg hao-seal--outline hao-seal--stamp" id="st1" lang="zh" aria-hidden="true">讫</span>
    <h2 class="hao-stamp__title hao-stamp__text" id="tt1">已发布</h2>
    <p class="hao-stamp__body hao-stamp__text" id="tb1">这条札记现在所有人可见。</p>
  </div>
  <button class="hao-btn hao-btn--tinted" data-replay="st1:hao-seal--stamp,tt1:hao-stamp__text,tb1:hao-stamp__text">再盖一次</button>
</div>
```

## Script used by this example

```html
<script>document.querySelectorAll("[data-replay]").forEach(function (b) { b.addEventListener("click", function () { b.getAttribute("data-replay").split(",").forEach(function (pair) { var p = pair.split(":"), el = document.getElementById(p[0]); el.classList.remove(p[1]); void el.offsetWidth; el.classList.add(p[1]); }); }); });</script>
```
