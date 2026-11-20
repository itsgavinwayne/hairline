The reading layout for long text: how a piece is set, from its title to its signature.

Inside `<article class="hao-prose">`, in order: an `<h1>`, `.hao-prose__meta`, a run of `<p>`s and `<h2>`s, with `Divider`, `Quote`, or `Mount` woven in, and an optional `.hao-prose__sign` (a group of signature items) at the end. You provide the text.

- **Measure**: the line width stays within `measure` (about 38 Chinese characters). Top margin 72px, bottom margin 48px—more above than below, the thread-bound book rule that the head outweighs the foot: the head leaves room for marginal notes and gives the title room to breathe.
- **Chinese paragraphs**: first line indented two characters, justified, with no blank line between paragraphs. Line height 32px, one step looser than interface body text.
- **English paragraphs**: left-aligned, first line indented 1.5 character widths; the first paragraph after a heading takes no indent. Line height 28px.
- **Headings**: `<h1>` uses `title-1`, one per piece; sections use `<h2>`, `title-2`; one level below that uses `<h3>`, `title-3`, and that is the last. Headings take no period and aren’t centered.
- **Dates**: can be written with the sexagenary cycle and the solar term—the Bingwu year, four days before Minor Snow (丙午年 小雪前四日)—one of the few places in this system allowed a touch of grace; working timestamps stay numeric.
- **Chapters** use the `Divider` with the fishtail mark, at most two or three in a piece.
- The **signature** sits right: a vertical date line with a small seal (in English, an italic colophon with the seal). A page with a signature carries no other seal.
- Links in the body use `.hao-link`; emphasize with bold, not color.
- Reading pages carry no patterns; the fishtail and the signature are enough.

**Accessibility**

- The structure is the semantics: the whole piece sits in `<article class="hao-prose">`, and a screen reader jumps through the `<h1>` and `<h2>` levels.
- The fishtail divider between chapters takes `role="separator"` as in the preview.
- The small seal in the signature takes `aria-hidden="true"` as in the preview; the date-line text (`.hao-slip`, or the italic colophon in English) stays in the screen reader.
