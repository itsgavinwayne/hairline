# English interfaces

The English interface and the Chinese interface are one system: colors, spacing, corner radii, components, and patterns all stay; only the type and the words change. Set `lang="en"` on the page’s root element, and title sizes and tracking switch to the English settings on their own.

## Typefaces

- Newsreader leads the serif-title font stack for Western text; Han characters fall through to Noto Serif SC. Its wedge serifs and stroke contrast come close to the Song typeface’s clipped corners and thin-horizontal, thick-vertical strokes, so the two scripts sit comfortably in one line.
- Western text in body copy and controls uses the system’s San Francisco, same as native iOS.
- English titles use `display-en`, `title-1-en`, `title-2-en`, `title-3-en`: one weight lighter than Chinese (500 or 600), with tighter tracking (-0.02em to -0.01em). Chinese titles open up tracking (+0.02em); don’t swap the two. At the two largest levels English runs one size above Chinese (34 against 32, 48 against 44), because Han characters fill more of their box; the 24 and 20 levels share one size.
- English body text uses `body-en` at a 24px line height, 4px less than the 28px of Chinese; `headline`, `callout`, `footnote`, and `caption` are shared by both languages.
- English paragraphs run 60 to 75 characters per line.

## Capitalization and emphasis

- Use sentence case everywhere: “Save changes”, not “Save Changes”, and certainly not “SAVE CHANGES”.
- No all-caps labels or subheadings, and no letterspaced capitals as decoration.
- Emphasize with italics—the Western tradition closest to small signature text; at most one per paragraph. Han characters are never italicized.
- Use curly quotes (“ ”), the apostrophe ’, and en dashes for ranges (7–9 PM).

## Voice and tone

Same character as the Chinese: short, plain, verb first, no showing off.

| Case | Chinese | English |
| --- | --- | --- |
| Primary button | 保存修改 | Save changes |
| Delete | 删除这条札记 | Delete this note |
| Success | 已发布 | Published |
| Error | 没连上网络，稍后再试 | Can’t reach the network. Try again in a moment. |
| Empty state | 还没有札记，写下第一条 | No notes yet. Write the first one. |
| Status labels | 进行中 / 今天到期 / 已完成 | In progress / Due today / Done |

- Say you, never we; contractions (can’t, you’re) are fine.
- No apologies, no exclamation marks, and never “Oops” or “Whoops”.
- English runs about thirty percent longer than Chinese: buttons at most three words, each segment of a segmented control at most ten characters, tags at most two words. If it doesn’t fit, find a shorter wording—never shrink the type.
- No Eastern-themed stock phrases: zen, ancient wisdom, harmony, journey, and words like them never appear in the interface. The East Asian character is carried by the colors, the seal, and the white space, never by adjectives.

## How Chinese words enter English

- When a plain English word exists, translate: 札记 is note, 案头 is desk, 落款 is signature. Never keep pinyin just to sound refined.
- Proper nouns with no plain equivalent (solar terms, the sexagenary cycle) put English first with Han in parentheses on first mention: “Minor Snow (小雪)”; after that, English only. Write sexagenary years as “the Bingwu year”.
- Wrap Han characters inside English text in `<span lang="zh">` so they render in the Song typeface or PingFang SC and never get italicized.
- Leave one space between Chinese and English; punctuation follows the language of its sentence.

## Dates and numbers

| | Chinese | English |
| --- | --- | --- |
| Date | 11 月 18 日 星期三 | Wednesday, November 18 |
| Short date | 11 月 18 日 | Nov 18 |
| Time | 07:12 | 7:12 AM |
| Relative time | 今天 07:12 | Today, 7:12 AM |

## Seals, title slips, and patterns

- **Seals** keep their Han characters; don’t switch to letters. The seal is a graphic mark—in an English interface it stays like a red stamp on letter paper, untranslated; add `lang="zh"` and an English `aria-label`.
- **Title slips** never set Western type vertically. An English signature uses `colophon`, italic and horizontal, beside the small seal.
- **Stitch, fret, and wave pattern** don’t depend on language; the rules hold: one per screen, never inside controls.

## One component, two languages

Every component preview comes in two sections, Chinese and English. Most components only change their text; the ones below look different across the two languages on purpose.

| Component | Chinese | English |
| --- | --- | --- |
| Title | Song typeface, weight 600 to 700, tracking opened up | Newsreader, weight 500 to 600, tracking tightened |
| Paragraph | Justified, 28px line height, punctuation at the start and end of lines handled by Chinese rules | Left-aligned, 24px line height, the last line never left with a single word |
| Quote | A pair of gold ink corner marks, shaped after 「」 | A single gold ink opening quote “ hanging at the upper left |
| Steps | The numbers are 一, 二, 三 | The numbers are 1, 2, 3 |
| Calendar | The solar term sits under the date (立冬) | A small gold ink dot under the date; the list below the month reads “Nov 7, Start of Winter” |
| Date tile | 十一月 / 18 / 周三 | Nov / 18 / Wed |
| Avatar | With no photo, the family name character (林) | With no photo, two initials (LW) |
| Text beside progress | Can read 六成二 | Reads 62% |
| Text beside rating | 四分 | 4 of 5 |
| Number display | A classifier after the number (31 条) | A plural noun after the number (31 notes) |
| Quoted names | 「晨间札记」 | “Morning note” |
| Seal, title slip | Han characters | Still Han characters, as a graphic; the signature instead uses an italic colophon |

- In Chinese paragraphs, the browser adds the gap between Han characters and Western text or digits on its own (on browsers that support it); when you write copy by hand, still follow “leave one space between Chinese and Latin text”. The two don’t conflict.
- Whatever the language, when a title wraps, keep the two lines close to the same length.
- Buttons have a minimum width of 88px so two-character buttons like “取消” (Cancel) and “删除” (Delete) don’t look too narrow; English buttons size to their text.
