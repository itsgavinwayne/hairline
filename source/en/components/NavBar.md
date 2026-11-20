The navigation bar at the top of a page: it says where you are, how to get back, and what this page’s one main action is.

Inside `<header class="hao-nav">` goes a `.hao-nav__bar` in three parts: back on the left (`.hao-nav__action`, with a left arrow and the previous page’s name), `.hao-nav__title` in the middle, and one action on the right. Top-level pages like the home page use `hao-nav--large`: below the bar goes `.hao-nav__large`, holding the large Song typeface title, with an optional small seal on the right. You provide the title, the back target, and the action.

- The standard bar uses `material` frosted glass, with content scrolling underneath; the large-title bar is transparent and sits directly on `bg`.
- Only one action on the right. Confirmation actions (Done, Save) take `hao-nav__action--strong`. More actions go into a sheet.
- The back button says the previous page’s name, never “Back”. A title that runs too long is cut with an ellipsis—no wrapping, no shrinking the type.
- The in-bar title uses the sans-serif `headline`; the Song typeface appears only in the large title.
- Patterns and title slips don’t go in the nav bar. The small seal beside a large title is the screen’s only cinnabar.

**Accessibility**

- The actions on the left and right are real links and real buttons, 44px tall, reachable by Tab; on focus, a `focus`-colored edge is drawn.
- The back arrow icon takes `aria-hidden="true"` as in the preview; the button’s name is the words beside it.
- Write the page title as a heading element (in the preview, `.hao-nav__title` is an `<h1>`), so a screen reader can jump to the page by heading.
- The small seal in the large-title bar is decoration and takes `aria-hidden="true"` as in the preview.
