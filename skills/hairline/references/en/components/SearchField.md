# SearchField · Search field

A search field in a capsule shape, with a magnifier on the left.

Inside `<label class="hao-search">` go the magnifier icon and an `<input type="search">`. You supply the placeholder and the `aria-label`; write the same words in both.

- At the right end of the field sits one cloud scroll in a thin, faint line; it fades once you type. It is the control’s own shape, not a scene: one cloud only, never a field of them.
- Make the placeholder say what is being searched (“Search notes”), not just “Search”.
- Show results as the person types; with no results, use an empty state and put the search term in its title.
- On narrow screens, place it under the large title, where it scrolls away with the page; on wide screens, at the right of the top navigation.

## Markup

### English

```html
<label class="hao-search" style="width:340px;max-width:100%"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="Search notes" aria-label="Search notes"></label>
```

### Chinese

```html
<label class="hao-search" style="width:340px;max-width:100%"><i class="hao-icon hao-icon--search" aria-hidden="true"></i><input type="search" placeholder="搜索札记" aria-label="搜索札记"></label>
```
