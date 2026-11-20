A five-point rating that uses a five-petal plum blossom in place of stars.

The motif comes from the dispelling-winter chart (九九消寒图): from the winter solstice on, you paint a branch of plain plum blossoms, one petal a day; when every petal is filled, spring has arrived. Here one blossom has five petals—fill in as many petals as the score.

- For display: one `<svg class="hao-plum">` with five petal `<circle>`s; filled ones get `class="on"`, and the last one, `class="hao-plum__c"`, is the pistil. One blossom says the whole score, in less space than five stars. `hao-plum--lg` is 40px.
- For rating: `.hao-rate` (`role="radiogroup"`) holds five buttons (`role="radio"`), a whole blossom in each; the chosen one and the ones before it get `hao-plum--on`.
- The petals fill clockwise, starting from straight up.
- Petals use `tint`; the pistil uses `gold`. Don’t fill them red: cinnabar belongs to seals alone.
- There is always text alongside (“4 of 5”), or an `aria-label` (“4 out of 5”).
- Use it only for five-point scales. Percentages and progress use the waxing moon.
- The five petals touch one another without overlapping, their centers on a circle of radius 6 (on a canvas of 24), petal radius 3.5. Draw to these proportions and it stays clean at any size.

**Behavior** (when the behavior script is loaded)

- The row of blossoms used for rating is tappable: tap any blossom and it, with every one before it, fills in. The left and right arrow keys move the score by one; the whole group is a single Tab stop; a change fires a `hao-change` event.
