An area for picking files or dragging them in.

Inside `.hao-upload` go a `<strong>` line of instruction, a line of limits, and a `hao-btn--tinted` button (the real `<input type="file">` hides behind it). When a drag hovers over it, add `hao-upload--over`. You supply the text.

- The button is required: drag and drop is a shortcut for mouse users, while touch and keyboard both rely on the button.
- State the format and size limits up front; don’t wait for a failed upload to mention them.
- During the upload, use the `Progress` bar, one row per file; when it’s done, list the file names in a `ListGroup`, where they can be deleted.
- When an upload fails, that row explains why and what to do (“Over 10 MB—compress it and try again”).
- The border is a ring of stitches—short dashes with rounded ends, the same line as the stitch pattern. On drag over, the stitches turn `tint`.

**Behavior** (when the behavior script is loaded)

- When files are dragged over, the area switches to its “dragged over” state; on drop, it fires a `hao-files` event carrying the file list.
- Put a hidden `<input type="file">` inside; tapping the button opens the system file picker. The upload itself and its progress are yours to wire up.
