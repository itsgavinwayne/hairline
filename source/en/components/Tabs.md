Tabs within a page, for switching among blocks of content at the same level; mostly for medium and wide screens.

`.hao-tabs` takes `role="tablist"`, holding any number of `.hao-tabs__item`s (`role="tab"`), with `aria-selected="true"` on the current one. For navigation between pages, use links with `aria-current="page"` instead. You supply the text.

- The split with the segmented control: a segmented control switches views of the same content (day, week, month); tabs switch to different content (essays, reading).
- The current item is bold `ink`, with one `tint`-colored horizontal stroke (横) beneath: heavy where it starts, light where it ends, like a stroke written with a brush—not a straight line of even weight.
- When they don’t fit, scroll sideways: no wrapping, no tucking them into “More”.
- The arrow keys move between tabs; Tab enters the content below.
- Top-level navigation on narrow screens still uses the tab bar.

**Behavior** (when the behavior script is loaded)

- Each tab points to its panel with `aria-controls` (`<div class="hao-tabs__panel" role="tabpanel">`). Tap a tab, and its panel shows while the others hide.
- A tab group holds a single Tab stop. The left and right arrow keys move between tabs and switch at once, wrapping from end to end; Home and End jump to the first and last; Tab then enters the panel below.
- On each switch, the tabs fire a `hao-change` event. Link-style tabs used for page navigation are not taken over by the script.
