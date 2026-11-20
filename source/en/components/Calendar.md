A month calendar for picking a date. Under each date you can add a line of lunar text, or a moon phase.

Inside `.hao-cal` are `.hao-cal__head` (the month title in the Song typeface and the month-paging buttons), `.hao-cal__grid` (seven columns: a row of weekday names, then the date buttons `.hao-cal__day`), and an optional `.hao-cal__foot`. Today gets `aria-current="date"`, the chosen date gets `aria-pressed="true"`, and dates filling in from the neighboring months get `hao-cal__day--out`.

**What goes under a date: pick one of three**

| Way | Markup | Look |
| --- | --- | --- |
| Lunar text | `<small class="hao-cal__lunar">初十</small>` | A lunar day under every date; on the first of the lunar month, the month’s name (十月) with `hao-cal__lunar--first`; on a solar term, the term’s name instead, in a plain `<small>` with no class, in gold ink |
| Moon phase | `<i class="hao-moon hao-moon--xs" style="--p:.6">` | A small moon under every date; in the second half of the month add `hao-moon--wane`, and the lit side moves to the left |
| Nothing | | The cleanest, for when a date is all you’re choosing |

- Use only one of the three in a calendar; lunar text and a moon phase together won’t fit in the cells.
- For the **moon phase**, `--p` is the share of the face that is lit: 0 is the new moon (the first of the lunar month), 1 the full moon (around the fifteenth). The lit side sits right in the first half of the month and left in the second—the view from the Northern Hemisphere.
- The **footer** (`.hao-cal__foot`) gives today’s sexagenary year and lunar day; with a moon phase, or in English, list the month’s solar terms there too.
- **English interfaces** show no lunar text; use the moon phase, and list the solar terms by English name in the footer.
- The week starts on Monday. An English interface may follow local custom and start on Sunday.
- Today is `tint` in bold; the chosen date is filled `tint`; when the two fall on the same day, it shows as chosen.
- Arrow keys move between dates, Enter selects, and the paging keys change the month.

**Where the data comes from**

- Never hand-write lunar dates, and never work them out yourself; use calendar data. The internationalization interface built into browsers and systems provides it (set the calendar to `chinese`) and gives the month, the day, and the sexagenary year.
- The moon phase converts straight from the lunar day: the first of the month is the new moon, around the fifteenth the full moon. To pin down the exact phase of a given day, use an astronomical ephemeris library.
- Solar terms call for an ephemeris library or an officially published table. The Start of Winter (立冬) and Minor Snow (小雪) dates and the lunar dates in the preview come from system calendar data for November 2026.

**Behavior** (when the behavior script is loaded)

- Add `data-hao-calendar` to the `<div class="hao-cal">` and the script takes over what’s inside and draws a real month calendar. Attributes: `data-mode` (`lunar`, `moon`, or `plain`), `data-value` (the chosen date, written like `2026-11-20`), `data-today` (pins “today” to a given date, for demos; left out, it’s the real today), and `data-terms="off"` (no solar term marks).
- The month-paging buttons work. Tap a day and it’s selected; the calendar fires a `hao-change` event carrying the date and the lunar date.
- Keyboard: the arrow keys move by day or by week, and leaving the month pages to the next on its own; Home and End go to the start and end of the week; Page Up and Page Down change the month; Enter or Space selects. The whole calendar is a single Tab stop.
- The script-drawn calendar is three layers deep—table, row, cell (`.hao-cal__row`, one week per row; `.hao-cal__cell`, wrapping the date button)—so a screen reader can announce the weekday and the week number.
- Every date has a full spoken form (year, month, and day; weekday; lunar date; solar term) for screen readers.
- **Lunar dates and moon phases are computed live**, on the browser’s built-in Chinese calendar data. Where the browser doesn’t support it, the calendar falls back to the look without lunar text.
- **The browser’s lunar data is off by a day on a handful of dates.** When a new moon falls right at midnight, it can land the first of the lunar month on the neighboring day; in testing, for February 6, 2027 it gives the 30th of the twelfth lunar month, a day that should be the first of the first lunar month. It’s good enough for everyday display. For anything that can’t be wrong—fixing holidays, working out birthdays—swap `Hairline.calendar.source` for a function that takes a date and returns the lunar date, backed by authoritative calendar data.
- **Solar terms run on an approximate formula** that can be off by a day in some years, covering only 2001 through 2100. For exactness, swap `Hairline.calendar.terms` for a function returning ephemeris data.
- With no script loaded, the static month written inside the container shows as it is.
