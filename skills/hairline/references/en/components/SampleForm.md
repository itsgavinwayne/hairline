# SampleForm · Form page (Chinese)

A sample form page, used to check the rule that “task screens carry no decoration”—not a reusable component.

The one-two-three of the steps, the check of the checkbox, the stitching of the upload box: all are the controls’ own shapes. The screen has no pattern and no cinnabar, and only one primary button.

## Markup

### English

```html
<div class="phone">
  <header class="hao-nav bar"><div class="hao-nav__bar"><button class="hao-nav__action">Cancel</button><h1 class="hao-nav__title">Export note</h1><span></span></div></header>
  <div class="scroll" style="padding-top:104px">
    <ol class="hao-steps" style="justify-content:center"><li class="hao-steps__item--done"><span class="hao-steps__n" aria-hidden="true">1</span>Content</li><li aria-current="step"><span class="hao-steps__n" aria-hidden="true">2</span>Format</li><li><span class="hao-steps__n" aria-hidden="true">3</span>Export</li></ol>
    <div class="hao-field"><label class="hao-field__label" for="fn">File name</label><input class="hao-field__input" id="fn" value="November note"><span class="hao-field__foot"><span class="hao-field__hint">Don’t add the extension</span><span class="hao-field__count">13 / 20</span></span></div>
    <div class="hao-field"><label class="hao-field__label" for="ff">Format</label><span class="hao-select"><select id="ff"><option>PDF</option><option>Plain text</option><option>Web page</option></select></span></div>
    <fieldset class="hao-choices"><legend>Include</legend><label class="hao-check"><input type="checkbox" checked> Images</label><label class="hao-check"><input type="checkbox" checked> Signature and seal</label><label class="hao-check"><input type="checkbox"> Draft</label></fieldset>
    <div class="hao-upload" style="padding:var(--hao-space-5)"><strong>Cover image</strong><span>Optional, JPG or PNG</span><button class="hao-btn hao-btn--sm hao-btn--tinted">Choose image</button></div>
    <button class="hao-btn hao-btn--block">Next</button>
  </div></div>
```

### Chinese

```html
<div class="phone">
  <header class="hao-nav bar"><div class="hao-nav__bar"><button class="hao-nav__action">取消</button><h1 class="hao-nav__title">导出札记</h1><span></span></div></header>
  <div class="scroll" style="padding-top:104px">
    <ol class="hao-steps" style="justify-content:center"><li class="hao-steps__item--done"><span class="hao-steps__n" aria-hidden="true">一</span>内容</li><li aria-current="step"><span class="hao-steps__n" aria-hidden="true">二</span>格式</li><li><span class="hao-steps__n" aria-hidden="true">三</span>导出</li></ol>
    <div class="hao-field"><label class="hao-field__label" for="fn">文件名</label><input class="hao-field__input" id="fn" value="十一月札记"><span class="hao-field__foot"><span class="hao-field__hint">不用写扩展名</span><span class="hao-field__count">5 / 20</span></span></div>
    <div class="hao-field"><label class="hao-field__label" for="ff">格式</label><span class="hao-select"><select id="ff"><option>PDF</option><option>纯文本</option><option>网页</option></select></span></div>
    <fieldset class="hao-choices"><legend>包含</legend><label class="hao-check"><input type="checkbox" checked> 图片</label><label class="hao-check"><input type="checkbox" checked> 落款与印章</label><label class="hao-check"><input type="checkbox"> 草稿</label></fieldset>
    <div class="hao-upload" style="padding:var(--hao-space-5)"><strong>封面图片</strong><span>可选，JPG 或 PNG</span><button class="hao-btn hao-btn--sm hao-btn--tinted">选择图片</button></div>
    <button class="hao-btn hao-btn--block">下一步</button>
  </div></div>
```
