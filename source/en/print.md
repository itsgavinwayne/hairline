# Print and graphics

Posters, social images, slides, and printed pieces still use the same colors, type, and rules—there’s no interaction, so the image has to stand on its own. See `Poster` for templates.

## Layout

- **Margins**: Leave one-twelfth of the short edge on all four sides. Align all content to this edge; only the wave pattern and a full background fill may bleed.
- **Grid**: Divide the width into twelve columns. A large title takes four to eight columns; a vertical title takes the two or three columns at the far right.
- **White space**: Keep at least half the image empty.
- **Visual weight**: Put large elements at the top or right; put information and the stamp at the bottom. Information goes at the lower left, the seal at the lower right.

## Type

Size type as a share of the image’s short edge, so a phone image and a one-meter-tall poster look the same. The pixel scale used in interfaces (`display` through `caption`) doesn’t apply to print and graphics.

| Use | Font | Size (share of short edge) |
| --- | --- | --- |
| Large title (Chinese) | Song typeface 700 | 13% to 16% |
| Large title (English) | Newsreader 500 | 11% to 14% |
| Subtitle | Song typeface 600 / Newsreader 500 | 5% to 6% |
| Information | Sans-serif 400 | 3.5% to 4% |

- Use only one large title per piece, and make the two type sizes differ by at least a factor of two.
- Chinese large titles can be set vertically, reading right to left, in no more than two columns with no more than six characters each. English titles are not set vertically.
- Titles take no period and no exclamation mark, and are not centered (except vertical titles).

## Where the fonts come from

| Use | Font | License |
| --- | --- | --- |
| Chinese titles | Noto Serif SC | SIL Open Font License; commercial use and printing allowed |
| Western titles | Newsreader | SIL Open Font License; commercial use and printing allowed |
| Body text and information | Noto Sans SC | SIL Open Font License; commercial use and printing allowed |

- In interfaces, body text on Apple devices still uses the built-in PingFang SC and San Francisco; they are licensed only for interfaces on Apple platforms and **must not be used in posters, printed pieces, Android, or Windows**.
- So for printed pieces and interfaces on non-Apple platforms, use Noto Sans SC for body text. In the font stack it comes after PingFang SC, so anywhere PingFang SC is missing it falls back to Noto Sans SC automatically.
- You can get all three fonts from Google Fonts. Before using them for print, check the license terms in effect at that time.

## Color

On screen, use the hex values in the tokens. For print, refer to the CMYK values in the table below.

| Name | Token | Screen | Approximate CMYK values C / M / Y / K |
| --- | --- | --- | --- |
| Moon white | `bg` | #f2f4f7 | 2 / 1 / 0 / 3 |
| Porcelain white | `surface` | #ffffff | 0 / 0 / 0 / 0 |
| Blue-black | `ink` | #161b24 | 39 / 25 / 0 / 86 |
| Slate | `ink-secondary` | #4a5263 | 25 / 17 / 0 / 61 |
| Azurite | `tint` | #1f4fa8 | 82 / 53 / 0 / 34 |
| Azurite wash | `tint-wash` | #e3ebfa | 9 / 6 / 0 / 2 |
| Cinnabar | `seal` | #b83224 | 0 / 73 / 80 / 28 |
| Bamboo green | `jade` | #24705a | 68 / 0 / 20 / 56 |
| Gamboge | `amber` | #f2b632 | 0 / 25 / 79 / 5 |
| Gold ink | `gold` | #836427 | 0 / 24 / 70 / 49 |
| Pattern color | `pattern` | #cfdaf0 | 14 / 9 / 0 / 6 |

- **These CMYK values are approximations converted directly from the screen colors; they have not been color-managed or checked against a proof.** Before final printing, have the printer make a proof on the chosen paper and use that proof as the reference; for the two main colors, cinnabar and azurite, consider separate spot colors.
- Use no more than three colors per piece: one background color, one text color, and one of azurite or cinnabar.
- Use cinnabar only for the seal. For large areas, use only moon white or azurite.
- Use gold ink only for fine lines (fret, corner marks); when you really need to print gold, use a spot gold, not CMYK builds.

## Scene and seal

- One scene per piece: choose one of a wave pattern, a fret, a moon, a mounted image, or a poem set vertically.
- One seal per piece, at the lower right; the seal face width is about one-tenth of the short edge.
- Use vector files for seal artwork in print. Logo files are in the Logos group under resources; a product’s own seal needs its own vector artwork.

## Sizes and output

| Use | Ratio | Common sizes |
| --- | --- | --- |
| Poster | 2:3 | Screen: 1080×1620 px; print: follow the paper and add 3 mm bleed on all four sides |
| Square social image | 1:1 | 1080×1080 px |
| Slides, header images | 16:9 | 1920×1080 px |

- In printed pieces, keep type and the seal at least 5 mm from the trim edge.
- Export images for screen as PNG; export for print as PDF, with fonts converted to outlines or embedded.
