# DateTile · Date tile

A small calendar page that stands a date up as a graphic beside a schedule entry or an event.

`.hao-date` holds three lines: `.hao-date__m` the month, `.hao-date__d` the day, `.hao-date__w` the weekday. When the day carries a solar term, the third line gives the term’s name instead, with `hao-date__w--term` added.

- The look is borrowed from the old page-a-day calendar: a color band up top for the month, the day big in the middle.
- The month is written in Han characters (十一月), the day in Arabic numerals set in the Song typeface, the weekday as “周三”; an English interface writes “Nov” and “Wed”.
- Use it only when the date itself is the point: schedule lists, event details, reminders. An ordinary timestamp is written as text.
- Add `role="img"` and an `aria-label` that reads the date out in full; when the full date already stands beside it, use `aria-hidden="true"` instead.
- When they run in a column, one per row, left-aligned.
- To carry the lunar date too, add a `.hao-date__l` line at the end (“十月初十”), generated from calendar data—never written by hand. English interfaces leave this line out.
- The colored band at the top has a small hole at each end: the binding holes of a tear-off calendar.

## Markup

### English

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-date" role="img" aria-label="Wednesday, November 18"><span class="hao-date__m">Nov</span><span class="hao-date__d">18</span><span class="hao-date__w">Wed</span></span><span class="hao-date" role="img" aria-label="November 22, Minor Snow"><span class="hao-date__m">Nov</span><span class="hao-date__d">22</span><span class="hao-date__w hao-date__w--term">Minor Snow</span></span><div><p style="margin:0;font:600 17px/24px var(--hao-font-sans)">Book club: The Craft of Gardens</p><p style="margin:0;font:400 15px/24px var(--hao-font-sans);color:var(--hao-ink-secondary)">7:30 PM, online</p></div></div>
```

### Chinese

```html
<div class="hao-row" style="gap:var(--hao-space-5)"><span class="hao-date" role="img" aria-label="11 月 18 日，星期三"><span class="hao-date__m">十一月</span><span class="hao-date__d">18</span><span class="hao-date__w">周三</span></span><span class="hao-date" role="img" aria-label="11 月 18 日，星期三，农历十月初十"><span class="hao-date__m">十一月</span><span class="hao-date__d">18</span><span class="hao-date__w">周三</span><span class="hao-date__l">十月初十</span></span><span class="hao-date" role="img" aria-label="11 月 22 日，小雪，农历十月十四"><span class="hao-date__m">十一月</span><span class="hao-date__d">22</span><span class="hao-date__w hao-date__w--term">小雪</span><span class="hao-date__l">十月十四</span></span><div><p style="margin:0;font:600 17px/24px var(--hao-font-sans)">读书会：《园冶》</p><p style="margin:0;font:400 15px/24px var(--hao-font-sans);color:var(--hao-ink-secondary)">晚上 7:30，线上</p></div></div>
```
