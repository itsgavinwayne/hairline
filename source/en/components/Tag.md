Marks the current status of a piece of content; not tappable.

Use a `<span class="hao-tag">` plus a tone class: the default (neutral), `hao-tag--tint`, `hao-tag--jade`, `hao-tag--amber`, `hao-tag--seal`. You supply the text—one or two words (two to four characters in Chinese).

- The text carries the status; color only helps. No tags with a dot and no word.
- At most two tags in a row.
- `hao-tag--seal` is only for problems that truly need attention.

**Accessibility**

- A tag is just the words inside the `<span>`; the dot in front is drawn by `::before`, and a screen reader reads the text only.
- The five tone classes change the colors only—not the structure, and not what gets read out.
