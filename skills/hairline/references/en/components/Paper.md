# Paper · Letter paper

A sheet of letter paper: stationery with ruled lines, for writing and reading text that is short and a little formal.

`.hao-paper` can go on a `<textarea>` (writing) or on a `<div>` (reading; one `<p>` per paragraph inside, and an empty `<p>` for a blank line). For writing, put a label above it following the `TextField` structure.

- The look comes from old letter paper: a double rule (文武边) around the edges—one heavy line outside, one fine line inside—and a thin rule under every line, with the characters sitting right on it. All the lines are gold ink.
- Each line is 32px, roomier than an ordinary input, so writing doesn’t feel cramped. The input can be dragged taller, and the rules scroll along with the text.
- On focus, the outer frame turns `tint`; the rules don’t change.
- Use it only where “writing a passage” is itself the point: letters, notes, messages, dedications. Search, remarks in a form, and comment boxes use an ordinary multiline input.
- One per screen. Reading and writing can share the same paper, so a reply feels like it’s written at the same desk.
- No vertical setting. The rules on letter paper ran vertically, but horizontal typing flows better, so the rules were turned sideways.
- Don’t add the patterns or pictures of decorated letter paper.

**Accessibility**

- The writing version is a `<textarea class="hao-paper">`: a native control, ready to write in as soon as Tab lands on it; the label connects to its `id` with `for`, as in the preview.
- The reading version is `<p>`s in an ordinary element, read paragraph by paragraph; the rules and the double rule are painted as backgrounds and produce no text.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-field" style="width:400px"><label class="hao-field__label" for="pp-en">To Lin Wan</label>
<textarea class="hao-paper" id="pp-en" style="height:256px">Dear Lin,

It has been foggy for days. The mornings are quiet, and I can’t see past the street. I found the book you mentioned and I’m on chapter three.</textarea></div>
<div style="width:400px"><p class="hao-field__label" style="margin:0 0 var(--hao-space-2)">Letter received</p>
<div class="hao-paper"><p>Dear friend,</p><p></p><p>How far are you into the book? We had the first snow here yesterday. Not much, and it melted as it landed.</p></div></div>
</div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-6);align-items:flex-start">
<div class="hao-field" style="width:400px"><label class="hao-field__label" for="pp">写给林晚</label>
<textarea class="hao-paper" id="pp" style="height:224px">见字如面。

这几天起了雾，早上什么都看不清，倒是安静。你上次说的那本书我找到了，读到第三章。</textarea></div>
<div style="width:400px"><p class="hao-field__label" style="margin:0 0 var(--hao-space-2)">收到的信</p>
<div class="hao-paper"><p>见字如面。</p><p></p><p>书读到哪里了？我这边昨天下了第一场雪，不大，落地就化了。</p></div></div>
</div>
```
