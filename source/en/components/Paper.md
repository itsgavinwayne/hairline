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
