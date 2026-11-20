When a task runs in steps, tell people how many there are and which one they’re on. The step numbers are written in Han numerals.

An `<ol class="hao-steps">`; each `<li>` holds a `.hao-steps__n` (一 二 三) and the step’s name. Finished steps take `hao-steps__item--done`; the current one takes `aria-current="step"`.

- Two to five steps. Past five, split the task into several.
- Number steps only where order truly matters; don’t number parallel items.
- Each number is a Han character in the Song typeface, one character inside a circle. English interfaces use Arabic numerals instead.
- Finished steps are solid `tint`, the current one a `tint` ring, the ones not yet reached gray rings, and the connecting line changes along. Solid, hollow, and text weight carry the state together.
- When a narrow screen can’t fit them, show only “Step 2 of 3” and the current step’s name.
- When the root element is `lang="en"`, the numerals switch to Newsreader automatically; write them as Arabic numerals.
- When the window is narrower than 600px, only the current step shows its name; the rest are bare numbers, and a screen reader still reads every step’s name.
- The line between steps is solid once passed and stitched (dashed) for what lies ahead, the same idea as the “thread” in progress.
