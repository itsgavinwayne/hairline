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
