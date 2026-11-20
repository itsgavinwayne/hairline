# Aesthetic standards and sources

“An East Asian sensibility” is too broad—anything fits inside. This section narrows it into five standards you can test against, then says where the standards come from.

Three layers, each changing at its own pace:

| Layer | Content | How often it changes |
| --- | --- | --- |
| Position | One line: The restraint of iOS, with an East Asian sensibility | Barely changes |
| Standards | plain (素), empty (空), pale (淡), fine (细), off-center (偏)—five of them | Rarely changes |
| Sources | Where the standards come from, works you can compare against | Grows at any time |

To judge whether something belongs, look only at the second layer. If it meets the standards, use it even if it isn’t from the Song dynasty; if it doesn’t, don’t use it even if it is.

## The five standards

Each standard comes with a question that takes a yes or a no. If the answer isn’t yes, revise it—or leave it out.

| Standard | Meaning | Ask | Examples in the system |
| --- | --- | --- | --- |
| **plain (素)** | No decoration without a use; shape and proportion do the talking | Take it away—does the function survive? If yes, take it away. | Graphics are fine lines and flat fills, no texture, no aging |
| **empty (空)** | One subject per screen, white space around it | Is there really only one subject on this screen? | “One scene per screen”; sections separated by blank space |
| **pale (淡)** | Low-saturation color, one heavy color at most | Besides that one touch of cinnabar, is there any other loud color? | A moon white ground, `tint` doing the work, “one touch of cinnabar” |
| **fine (细)** | Thin lines, shallow layering | Are the lines between 1 and 1.5px? Any heavy borders or thick shadows? | `hairline` dividers, three faint shadows |
| **off-center (偏)** | The subject leans to one side; not everything dead center | Has the subject given up one side of the frame? | The moon sits upper right in the empty-state vignette; the opening screen of the docs site |

“Off-center” governs scenes, covers, posters, and display pages. Task interfaces—forms, lists, dialogs—follow iOS habits and center what should be centered.

The five standards govern texture. The three rules govern count: one red, one scene. Use them together.

## Sources

The five come mostly from the Song dynasty, and from its plainer strain in particular. They are listed so you can match a feeling, not to make a scholarly case.

| Standard | Drawn from | Compare with |
| --- | --- | --- |
| plain (素) | Monochrome glazes in Song ceramics: no painted flowers, glaze color and vessel shape only | The celadons of the Ru (汝) and Guan (官) kilns |
| empty (空) | The white space of Southern Song landscape painting | The small landscapes of Ma Yuan (马远) and Xia Gui (夏圭), later called “One-Corner Ma” (马一角) and “Half-Edge Xia” (夏半边) |
| pale (淡) | Ink wash and light color; the composure of mineral pigments in blue-green landscape | The azurite and malachite in Wang Ximeng’s (王希孟) “A Thousand Li of Rivers and Mountains” (千里江山图) |
| fine (细) | The layout of Song printed books; the lines of outline drawing (白描) | The column rules (界行), fishtail marks (鱼尾), and thick-thin rule pairs (文武线) of woodblock books; the water patterns in Ma Yuan’s “Water” album (水图) |
| off-center (偏) | Corner composition | Same as “empty” |

The system’s colors follow the same story: `tint` is named for azurite (石青), `jade` for malachite (石绿), `gold` for gold ink (泥金), `seal` for cinnabar (朱砂), `ink` for ink (墨), `bg` for moon white (月白). The names changed; the values didn’t.

## Three notes

- **What’s taken is the aesthetic, not an imitation of the Song.** No faux-antique interfaces, and nothing has to trace back to the Song dynasty. The form of the seal and the Song typeface both settled later; we use them anyway.
- **The Song dynasty holds things that fail these five too.** Meticulous heavy-color painting (工笔重彩) and all-over brocade patterns are all good; they just don’t point where this system points.
- **Pale color, but never low contrast.** Glazes like sky blue (天青) and pale celadon (粉青) may appear in photos and illustrations, but never as text or interaction colors. Contrast for text and controls follows the “Color” section.

## Adding sources

When a new comparable work comes to mind, add it straight to the table above; that doesn’t count as changing the spec. If the five standards themselves ever change, first work out which existing components would fail as a result.
