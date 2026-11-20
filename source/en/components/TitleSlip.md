A vertical title slip, after the name slip pasted at the top left of a thread-bound book cover.

`<span class="hao-slip">` is small Song typeface text set vertically; `hao-slip--boxed` adds a fine gold-ink frame on white. Wrap the slip and a small seal in `.hao-sign`, and you have a signature group. You supply the text—two to six Han characters.

- Han characters only—no Latin letters, no digits. Write the year with the sexagenary cycle (“丙午冬”, winter of the Bingwu year), never as 2026.
- The boxed form titles covers, cards, and features; the unboxed form serves as the date line of a signature.
- The slip is an ornament; the page’s real title is still the horizontal `title-1`. Don’t write the same text both horizontally and vertically.
- One per screen. Not tappable.

In English interfaces:

- Western script doesn’t run vertically. An English signature uses the horizontal `<span class="hao-colophon">` (italic serif), wrapped with the small seal in `.hao-sign.hao-sign--row`.
- Write the English signature as one phrase, sentence case, with no period: “Winter, the Bingwu year”.
- To keep a vertical Han date line as a graphic, use `.hao-slip` as is, with `lang="zh"` and an English `aria-label`; but on any one screen, keep either the vertical date line or the English signature, not both.
