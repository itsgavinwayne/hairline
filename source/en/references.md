# References and trade-offs

This system did not invent general-purpose things from scratch. Mature design systems have already solved layout, states, and accessibility, so it borrows those solutions; its own ideas live only in the layer they don’t cover: where the colors come from, the type for titles, seals, patterns, white space, and the way it speaks.

The table below records what was borrowed from whom, and what was not. When you add something to this system, work the same way: see how a mature system solves the problem, take its structure, then redraw it with the tokens and principles here.

| Reference | What was borrowed | What was not |
| --- | --- | --- |
| Apple Human Interface Guidelines | The 44px touch target, large titles, grouped lists, the frosted-glass material, the bottom tab bar and sheets, native pickers | The system blue; practices from platforms other than SF |
| Material Design 3 | A three-step responsive layout by window width, the same content changing shape at different widths, the idea of tokens in two layers (“raw values” and “semantic”), full state lists for every control | The ripple, dynamic color, the floating action button, large blocks of color |
| IBM Carbon | Grid discipline, motion in two speeds that serves function only, the rules for tables and data display | Right angles, high density, an industrial feel |
| Ant Design | Typography habits for Chinese interfaces, how forms and tables combine in business settings | The density of enterprise admin panels, the default blue |
| GOV.UK Design System | How the copy is written: say it plainly, errors that say what to do, one thing per page; the structure of forms | The visual style |
| WAI-ARIA Authoring Practices | Keyboard operation and screen reader semantics for controls such as dialogs, tabs, switches, and progress | None |
| WCAG 2.2 | Text contrast of 4.5:1, 3:1 for controls and icons, never color alone to carry information, respect for Reduce Motion | None |
| Requirements for Chinese Text Layout (W3C) | Spacing between Chinese and Western text, punctuation, the rules for vertical setting | None |
| Chinese traditional crafts | The blue of azurite (the mineral pigment in Song dynasty blue-green landscapes), the red of cinnabar seal paste, the white of Xuan paper; the intaglio seal (白文) and relief seal (朱文) of seal carving, and the border; the flat stitch and cross-stitch of embroidery; the fret on bronzes and brocade; the wave pattern on court robes; the title slip of thread-bound books | Ink brushwork, auspicious-cloud graphics, dragons and phoenixes, imitation-age textures, heavy reds and golds |

## Systems referenced for structure

The table above covers the interface itself. The systems below were looked at for a different question: how a design system organizes itself, and how designs and code stay aligned. Their sites were checked on November 19, 2026; only what was on the pages that day is recorded here.

| Reference | What they do | What this system takes |
| --- | --- | --- |
| GitHub Primer | Split at the top into Product UI and Brand UI, each with its own foundations and components, and brand assets on a separate site. In Figma, base variables and components live in separate libraries, and components are asked to be “small and simple, use properties, not layers of nesting” | Organize by kind of output: task interfaces are discussed separately from brand and printed pieces, on one shared foundation |
| The IBM Design Language and Carbon | The design language (philosophy, type, color, photography, illustration, grid) is one site; Carbon (foundations, components, patterns, data visualization) is another, and the latter states that it is shaped by the former. The Figma foundation libraries are split by color, icons, pictograms, and type | The aesthetic standards and their sources stand in a section of their own, cited by the component specs rather than mixed in |
| Atlassian | Docs split into “Get started, foundations, components, tools”; logos and illustration sit under foundations, and brand assets live off-site. Tokens are called the single source of truth for design decisions, with a searchable token table | The token page as a table you can search; logos, seals, and icons filed under foundations |
| Microsoft Fluent 2 | Docs split into “design, development, components”. The Figma kit is layered: one design-language file holds the global and alias variables (with modes for light, dark, and brand), and the component libraries sit on top; components nest no more than two levels deep | If a Figma version happens, follow that layering: one file for variables, one for components, one for icons |
| Adobe Spectrum | Among the foundations is an “attention hierarchy”: only one element, or one group of elements, may dominate a page | It’s the same idea as “one touch of cinnabar”; the two back each other up |
| Douyin Semi Design | The docs have a “design collaboration” group (theme customization, design-to-code, dark mode, design resources) and a copy spec. Every color on the palette is labeled with a contrast level | The color token page labels every text color with its contrast |
| ByteDance Arco Design | The design side splits into “design values, design principles, style guide, component usage”; the Figma resources come in four sets: Web, mobile, admin templates, icons | Separate entries for the design guide and the developer guide |
| The Japan Digital Agency design system | Split into “get started, guidelines, basic design, components, resources”. Type styles are named with size, weight, and line height; the whole doc set can be downloaded as Markdown; Japanese body text keeps a line height of at least 1.5 and uses no italics | Offer a downloadable plain-text copy of the docs; the no-italics-for-Han rule is already in place here |

Not verified: the old Shopify Polaris site now redirects to the developer docs; for Tencent TDesign, only the values page could be read. Neither is in the table.

## How the pieces merge

- **Structure goes with the crowd; character stays its own.** What a control looks like and how it operates follows the habits people already have; what color it wears, what type it’s set in, and how much white space surrounds it are decided by this system.
- **Borrow the rules, not the skin.** What you take from another system is the “why” and the “how it’s divided”, not its hex values and corner radii.
- **Traditional elements need a source, and a reason why it’s this one.** Each time a pattern or a form is added, record where it originally belonged and what it maps to in the interface. If you can’t say, don’t add it.
- **Subtract first.** If something borrowed conflicts with “leave room, then write”, cut it.

## What fits and what doesn’t

Fits: reading, writing, notes, schedules, lifestyle, culture and education, personal brands, content-driven sites.

Fits less well: professional tools with very high information density (trading, operations, design software), games, and products for children. The density or the mood those scenes call for runs against this system’s white space and restraint.
