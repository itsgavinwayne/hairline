A table for comparing many records side by side on wide screens.

`.hao-table-wrap` wraps the `<table class="hao-table">`. Headers use `<th scope="col">`; number columns take `hao-num` (right-aligned, tabular figures); minor columns take `hao-muted`. You supply the data.

- The table sits in a rounded `surface` container, with horizontal `hairline` rules only—no vertical lines, no zebra stripes.
- Text aligns left, numbers right, and each header matches the alignment of its column.
- The first column is the record’s name, in `ink`; the other columns stay as quiet as they can.
- Show status with a `Tag`, never color alone.
- No tables on narrow screens: the same data becomes a `ListGroup`, one row per record, with minor information moved into the subtitle.
- Past twenty rows, paginate or load as needed.
- Beneath the header runs the thick-and-thin double rule (文武线)—one thick rule above, one thin below—the way book-page borders are drawn. It is the only place in the table that uses it; rows are still separated by `hairline`.

**Accessibility**

- Keep a native `<table>`: the rounded container is `.hao-table-wrap`’s business, and the row-and-column mapping a screen reader relies on comes from the table structure. Don’t break it into a `<div>` grid.
- `hao-num` and `hao-muted` change only alignment, color, and type size—never the semantics of a cell.
