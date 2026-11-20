A run of events in time order, each node a phase of the moon.

An `<ol class="hao-timeline">`; each `<li>` holds a `.hao-moon`, the `.hao-timeline__title`, the `.hao-timeline__meta`, and an optional `.hao-timeline__body`. The current item takes `aria-current="step"`.

- The moon phase is the state: finished is a full moon (`--p:1` with `hao-moon--done`, in bamboo green), in progress a half moon (`--p:.5`), not started an empty moon (`--p:0`). When you know the exact progress, write the true value.
- The state also appears in the `meta` (“Done”, “In progress”), not just in the moon and the color.
- Newest on top or on bottom—settle on one across the product. Logs (an action history) put the newest on top; plans (project progress) put the earliest on top.
- Each item’s title is a noun phrase, its description at most two lines.
- A horizontal flow with only a few steps uses steps instead.
- After the date can come a small gold-ink line, `.hao-timeline__lunar`, holding the lunar date or the solar term (“十月初一”, “Minor Snow (小雪)”). Generate it from calendar data—never write it by hand. English interfaces leave it out.
