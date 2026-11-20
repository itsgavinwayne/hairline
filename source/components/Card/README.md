承载一段独立内容的卡片，标题用宋体。

`.hao-card` 里放 `.hao-card__title`、`.hao-card__body`、可选的 `.hao-card__meta`。需要落款时，在开头加一个 `.hao-seal.hao-seal--sm.hao-seal--outline.hao-card__seal`。你提供标题、正文和时间。

- 卡片放在 `bg` 上，卡片里不再套卡片。
- 一屏里只给一张卡片落印。
- 整张卡片可点时，把它做成一个 `<a>`，不要在里面再放按钮。
- 正文不超过四行，更长的内容进详情页。

两个带纹样的变体，一屏只用其中一张：

- `hao-card--wave`：底边铺两排海水纹，给一屏里最重要的那张卡片。
- `hao-card--stitched`：内缘一圈泥金缝线，像绣片的锁边，给收藏、手作一类有「物件感」的内容。带缝线时不再放印章。

**无障碍**

- 标题用标题元素写，预览里是 `<h3 class="hao-card__title">`。换成 `<span>` 仿标题，读屏就少一条按标题跳转的路。
- 落款的印对读屏隐藏，照预览在 `.hao-card__seal` 上写 `aria-hidden="true"`；时间照常写在 `.hao-card__meta` 里。
- 海水纹（`hao-card--wave`）和缝线（`hao-card--stitched`）都是伪元素画的，读屏读不到，你不用为它们写什么。
