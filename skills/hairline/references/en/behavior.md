# Behavior and scripts

A stylesheet decides how components look; one script decides how they behave. The script is a single file with no framework or library dependencies, kept at `components/bundle.js` and shipped with the stylesheet.

## How to use it

- Load the stylesheet, then this script, and that’s all. On load the script finds the components in the page and takes over; for content added later, call `Hairline.init(container)` once.
- Behavior is declared through attributes on the markup—no scripting needed. Attributes all start with `data-hao-`.
- **Without the script, components still look right**; they just don’t move. So write markup that holds up static: dialogs and menus carry `hidden` by default, and the calendar container can hold a static month first.
- Switches, radios, checkboxes, segmented controls, selects, and accordions ride on native browser controls and never needed a script.

## Attributes at a glance

| Attribute | Where | What it does |
| --- | --- | --- |
| `data-hao-open="id"` | A button | Opens that dialog or sheet |
| `data-hao-modal` | `.hao-scrim` | Marks a true modal layer, covering the full screen |
| `data-hao-close` | A button inside a dialog | Closes the dialog it sits in |
| `data-hao-initial` | A button inside a dialog | Takes focus when the dialog opens |
| `data-hao-menu="id"` | A button | Opens that menu |
| `data-hao-calendar` | `.hao-cal` | Renders a month calendar you can page through |
| `data-hao-toggle` | Filter chips, bookmarks | Toggles selected on click |
| `data-hao-chips="single"` | Container of a filter chip group | Only one in the group can be selected |
| `data-hao-checkall="group"` | The “select all” checkbox | Controls the checkbox group of the same name |
| `data-hao-tip="text"` | Any element | Shows a tooltip on hover or focus |
| `data-hao-toast="text"` | A button | Pops a toast on click |
| `data-hao-stamp="id"` | A button | Replays the stamp inside that container |
| `data-min` `data-max` `data-step` | `.hao-stepper` | Range and step of the stepper |

Each component’s notes cover its own details.

## What you can call on the script

| Call | What it does |
| --- | --- |
| `Hairline.init(container)` | Takes over content added to the page later |
| `Hairline.dialog.open(element)`, `.close()` | Opens and closes a dialog or sheet |
| `Hairline.menu.open(menu, button)`, `.close()` | Opens and closes a menu |
| `Hairline.toast(text, options)` | Pops a toast; options are `ok`, `action`, `onAction`, `duration` |
| `Hairline.calendar.create(element)` | Turns a container into a month calendar and returns its control object |
| `Hairline.calendar.lunar(date)` | Looks up the lunar date for a day |
| `Hairline.calendar.terms` | Swap in your own solar term data source |
| `Hairline.calendar.source` | Swap in your own lunar calendar data source |
| `Hairline.stamp(container)` | Replays the stamp |

## Events

When a component changes, it fires an event on itself; the event bubbles, so you can listen at any level.

| Event | Fired by | Payload |
| --- | --- | --- |
| `hao-open`, `hao-close` | Dialogs, sheets | None |
| `hao-select` | Menu items | None |
| `hao-change` | Tabs, the month calendar, filter chips, bookmarks, steppers, ratings, list single-select | The new value |
| `hao-files` | The upload area | Files dropped in |

## What’s done for accessibility

- **Focus management**: when a dialog or sheet opens, focus is trapped, the rest of the page is made inert and stops scrolling with it; on close, focus returns to what triggered it. Menus do the same.
- **Keyboard**: menus, tabs, the month calendar, ratings, and list single-select implement arrow keys, Home, and End by the usual conventions; overlays add Esc. A grouped control takes a single Tab stop.
- **Semantics**: the script fills in the state attributes that matter (expanded, selected, pressed, current date); the month calendar is a full table structure, and every day reads out complete.
- **Announcement**: toasts go into a polite live region and never steal focus.
- **Motion**: with Reduce Motion on, entrance animations don’t play.

## How accurate the calendar data is

- The lunar calendar uses the browser’s built-in data. Almost every day is right, but the rare day whose new moon falls around midnight can be off by one (in testing, the 2027 Lunar New Year was off by a day).
- Solar terms use an approximation; odd years can be off by a day, and only 2001 through 2100 are covered.
- Both leave hooks to swap in authoritative data: `Hairline.calendar.source` and `Hairline.calendar.terms`. Any date in a product that can’t be wrong should be swapped.

## What’s not done

- Gestures like pull-to-refresh and the drag-down-to-dismiss sheet.
- Table sorting and filtering, paged data loading, upload progress: these touch data, so the product using the system wires them up.
- Custom select panels. Selects always use the native control.
- This script is for the web. In native iOS apps, system controls provide these behaviors.
