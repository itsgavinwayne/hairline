# Link

A text link that carries you to another page. Three forms, by where it sits.

| Where | How to write it | Look |
| --- | --- | --- |
| In a run of text | `hao-link` | `tint` color with a thin underline. Inside a line of text, the underline is what tells you which words can be tapped. |
| On its own line, under a passage | `hao-link hao-link--go` | Bold `tint` text with no underline, and a chevron follows at the end of the line on its own—the same one at the ends of grouped list rows. |
| Beside the primary button | `hao-btn hao-btn--plain` | A text button, as tall as the primary button. See `Button`. |

- The link text says where it leads or what will be seen (“Read the design principles”, “See all the icons”), never “click here” or “Learn more”.
- The chevron on `hao-link--go` is drawn by the style; don’t add an icon yourself. Put only one under a passage.
- `hao-link--go` stands 44px tall, enough for a finger. On hover, a thin underline appears and the chevron shifts 3px to the right; with Reduce Motion on, the chevron doesn’t move.
- Don’t put an underlined `hao-link` beside a button: it stands shorter than the button and won’t line up.
- For a link that leaves the site, say so in the text (“See it on GitHub”) rather than adding an icon.

**Accessibility**

- The link is a native `<a>`: Tab reaches it, Enter opens it.
- On focus, a `focus`-colored ring is drawn around the text, so where the keyboard has stopped is plain to see.
- The chevron on `hao-link--go` is drawn by `::after`; a screen reader reads only the link text, so you write nothing for the chevron.

## Markup

### English

```html
<div class="hao-stack" style="max-width:none">
  <p class="hao-body" style="margin:0;max-width:34em">How red is used is set out in the <a class="hao-link" href="#">design principles</a>; to cut a real seal, read the seal guide next.</p>
  <div><a class="hao-link hao-link--go" href="#">Read the principles</a></div>
  <div class="hao-row">
    <a class="hao-btn" href="#">Get started</a>
    <a class="hao-btn hao-btn--plain" href="#">Browse components</a>
  </div>
</div>
```

### Chinese

```html
<div class="hao-stack" style="max-width:none">
  <p class="hao-body" style="margin:0;max-width:34em">红色怎么用，写在<a class="hao-link" href="#">设计原则</a>里；要做一方真正的印，再看印稿规范。</p>
  <div><a class="hao-link hao-link--go" href="#">读设计原则</a></div>
  <div class="hao-row">
    <a class="hao-btn" href="#">开始使用</a>
    <a class="hao-btn hao-btn--plain" href="#">浏览组件</a>
  </div>
</div>
```
