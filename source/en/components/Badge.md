A small number beside an icon or a list item, saying how many things are waiting to be dealt with.

`<span class="hao-badge">3</span>`; when you only want to signal “new” without saying how many, use `hao-badge--dot`; when it’s only a count no one has to act on, use `hao-badge--quiet`.

- The default badge is cinnabar, and it is that screen’s one touch of cinnabar: no seal on the same screen, and never two red badges.
- Above 99, write “99+”. It disappears at zero; don’t show 0.
- Add an `aria-label` that reads the number as a sentence (“3 unread”).
- For neutral counts (how many things a folder holds), use `hao-badge--quiet`, or just the value at the right of the list row.
- A badge that carries a number has the clipped corners of a seal, each slightly different, not a capsule: it is already cinnabar, so its shape follows the seal too. The dot alone stays round.
