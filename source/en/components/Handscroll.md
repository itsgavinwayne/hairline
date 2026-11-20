A sideways-scrolling roll of content, like a handscroll unrolling: the title leads, then one section after another.

`.hao-handscroll` holds, in order, `.hao-handscroll__title` (the opening panel, 引首), a run of `.hao-handscroll__item`s, and an optional `.hao-handscroll__end` (the tail, 拖尾). Each item is a link holding a date, a title, and an abstract of three lines or fewer. You provide the content.

- The **opening panel** names the roll: in Chinese, the title stands vertical in the Song typeface with a small line under it giving the count; in English, it lies horizontal at the lower left. Its ground is `tint-wash`, so the start reads at a glance.
- Each **item** is the same width and height, with a thin gap between items like the spacer bands (隔水) of a handscroll. An abstract past three lines is cut off on its own.
- The **tail** carries a small seal, saying the roll has run out. Show it only when nothing more is coming; while more can still load, leave it off.
- It scrolls rightward, each stop aligned to an item’s left edge. No scrollbar shows, and no left or right arrows; the last item peeks halfway out, hinting there is more behind it.
- It’s for “a few items from one group”: a month of notes, one topic, a set of works. Content with nothing in common belongs in a list.
- Three to eight items. Past that, give a “See all” that leads to the list page.
- The whole roll can be worked with the keyboard’s left and right keys, and every item can take focus.
- Like `Mount`, it is a container for content, not a pattern; still, one roll per screen.
