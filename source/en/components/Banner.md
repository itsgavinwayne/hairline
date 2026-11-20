A notice inside the page that says what happened and what to do next.

`.hao-banner` holds a 20px icon and a run of text, with the title in `<strong>`. Tint classes: default (information), `hao-banner--jade` (success), `hao-banner--amber` (warning), `hao-banner--seal` (error). You provide the icon, the title, and the message.

- Each tint has its fixed icon: `hao-icon--info`, `hao-icon--success`, `hao-icon--warning`, `hao-icon--error`. Icon and title carry the state together, not the background alone.
- The title gives the outcome (“Published”); the message gives the effect or the next step. No apologies, no exclamation marks.
- Use `role="alert"` for errors and `role="status"` for everything else.
- At most one per screen; when several messages arrive, they take their turn.
