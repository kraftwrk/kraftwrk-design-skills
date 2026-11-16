# The measured gate

`audit.py` reads a rendered page and reports what it measures. agency-grade-review asks for counts, contrast, states and worst-case data to be measured and never estimated; this is the tool that does it. It reads the render (computed styles, boxes and pixels), not the source, and it never changes the page.

It is a floor, not a judgement. A clean report says nothing is measurably wrong. It does not say the design is good: purpose, hierarchy, identity and the flow are still reviewed by reading the screens.

## What it measures

| Area | Checks |
| --- | --- |
| Colour | Contrast of every text run in both themes, every state and every language. Text over imagery, gradients or shapes is sampled from the pixels under it. Neutral grey on a coloured ground. |
| Type | Sizes on the scale and their count, families, weights, line heights on the 4px grid, tracking bands, measure counted in characters, minimum sizes, heading steps, one-word last lines, straight quotes, three dots, long dashes. |
| Space and shape | Spacing off the 4px grid, radii off the shape scale, space above and below headings, containers inside containers, border with shadow with tint. |
| Controls | Hit targets against the platform floor, accessible names, labels on fields, alt on images, heading order, a focus style. |
| Text scaling | Doubles the reader's default size and checks that the text follows and nothing is cut off. |
| Motion | An inventory of every transition and animation (the start of the motion table), with properties, durations and easing checked, reduced motion, hover rules, content that is invisible with animation off. |
| Browser surfaces | color-scheme, selection, caret, accent colour, underline offset. |
| Generic tells | Spent typefaces, italic serif display, warm off-white ground, eyebrows over headings, side stripes, gradient text, glows, hard shadows, stripes, generic copy. |

Severity follows agency-grade-review: Blocker, Major, Minor. An Advisory is a question for the reviewer, answered with a fix or with the reason it stays (Apart's hatching is stripes that carry data, so it stays).

## What the page has to provide

- Screens: each screen root carries `data-screen="name"` and `data-platform="ios"`, `"android"` or `"web"`. Without them the whole page is measured as one web surface, or roots are passed with `--root "#home:ios"`.
- Switches: every element with `data-set="attribute=value"` and an optional `data-on="selector"` is a switch. `data-theme` switches the theme, `data-state` the state of a screen, `data-lang` the language. The tool finds them and measures every combination.
- System chrome: a status bar, home indicator or system keyboard drawn in a mockup carries `data-system` and is left out.
- Scale: screens render at their real size. If the presentation shrinks them with `zoom`, undo it with `--css`.

## Run it

In Cowork or Claude Code, ask Claude to run the audit on the page; it runs in the session and the report comes back in the conversation.

On your own computer, in Terminal:

1. Go to the folder of the skills repo. Type `cd ` (with a space after it), drag the `kraftwrk-design-skills` folder onto the Terminal window and press Enter. Nothing is printed; the prompt now shows the folder name.
2. Install the two libraries the tool uses (once): `python3 -m pip install playwright pillow`. Expect a few lines ending in "Successfully installed", or "Requirement already satisfied".
3. Install the browser the tool drives (once): `python3 -m playwright install chromium`. Expect a download bar; it takes about a minute.
4. Check that the tool works: `python3 skills/agency-grade-review/scripts/test_audit.py`. Expect one line that starts with "ok".
5. Run it on a page: `python3 skills/agency-grade-review/scripts/audit.py path/to/page.html --out report.json`. Expect a first line with four counts, then the findings grouped by severity, the motion inventory and one line per screen. The full report is also saved as `report.json` in the same folder.

The command ends with an error status when there is a Blocker, so it can stop a build.

## Options

- `--root "#selector:platform"`: a screen root, repeatable.
- `--themes light,dark`: the themes to measure (both by default).
- `--width 1440`: the window width. Run it again with `--width 390` for the compact layout of a web page.
- `--skip ".selector"`: left out of every measurement, besides `[data-system]`.
- `--allow 59`: extra spacing values that pass, for platform insets.
- `--css "..."`: CSS applied before measuring.

## Self-test

`fixtures/clean.html` must produce no findings. `fixtures/defects.html` has one planted defect per rule and must trip all of them. `test_audit.py` checks both. Run it after changing a rule or a threshold.

## Sources

The checks implement the rules in the skills. Several of the generic tells and their thresholds (the spent typefaces, the warm off-white ground, the eyebrow test, side stripes, content hidden at rest, heading rhythm, the 1.25 step) follow rules published in Impeccable by Paul Bakaus (Apache 2.0). They are written again here against Marc's rules; none of its code is used. See NOTICE.md.
