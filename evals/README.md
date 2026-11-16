# Evals

Three fixed briefs used by `prompts/improve-the-skills.md`. Each improvement pass designs them with the skills only, reviews them with agency-grade-review in Full mode, and records the scores here. A rule change is only worth keeping if the next pass scores higher on the item it was written for.

## Briefs

- A. A Dutch neobank app for freelancers, calm and precise. iOS, Dutch.
- B. A luxury eyewear e-commerce site, editorial and quiet. Web, English and German.
- C. A kids' public-broadcaster video app, loud and safe. Android, Dutch.

Each product: the ten decisions as a matrix across three directions, one hero screen, one dense working screen, one sheet or overlay, one loud brand moment (from the second pass on) and one marketing section, as an HTML prototype with real content.

## Scores

Scale 1 to 5 per bar item of agency-grade-review. A 2 anywhere blocks Pre-ship.

### 2026-11-15, before the rule changes

| Bar item | A Apart | B Halewyn | C Kabaal |
| --- | --- | --- | --- |
| 1 Clarity of purpose | 4 | 4 | 4 |
| 2 Hierarchy | 4 | 4 | 4 |
| 3 Typographic precision | 4 | 4 | 3 |
| 4 Spatial discipline | 4 | 4 | 4 |
| 5 Colour with intent | 4 | 4 | 3 |
| 6 Real content | 4 | 3 | 3 |
| 7 Completeness | 2 | 3 | 3 |
| 8 Identity | 4 | 4 | 4 |
| 9 Motion that explains | 2 | 2 | 2 |
| 10 Platform fluency | 3 | 4 | 4 |
| 11 Accessibility | 3 | 3 | 3 |
| 12 Production readiness | 2 | 2 | 2 |
| 13 Finish | 3 | 3 | 3 |
| 14 Restraint | 4 | 5 | 4 |
| 15 Presentation | 4 | 4 | 4 |

Weakest: motion and production readiness, 2 on all three. Source study for this pass: motion (Apple HIG Motion, Material 3 motion, Emil Kowalski, Rauno Freiberg) and flow completeness (shipped flows of Uber, Google Pay, KOHO and Headspace on Mobbin).

Measured in this pass, from the rendered pages: text sizes, weights, line heights, tracking, off-grid spacing, radii, contrast per text node in both themes and every state, sampled contrast for text over imagery, hit targets, characters per line, straight quotes.

### Audit, 2026-11-15, the same prototypes before the rule changes

Counts from `skills/agency-grade-review/scripts/audit.py`. An advisory is a question, not a failure.

| | A Apart | B Halewyn | C Kabaal |
| --- | --- | --- | --- |
| Blocker | 0 | 3 | 5 |
| Major | 9 | 4 | 5 |
| Minor | 9 | 5 | 10 |
| Advisory | 6 | 9 | 6 |

What the audit found that the first review missed: Halewyn's busy state dims the whole checkout form to 2.3:1 and 3.5:1 without marking it busy; Kabaal has a link without a name, a heading jump from h1 to h3, capitals set with negative tracking and a heading with equal space above and below; on all three the type is in px and does not follow the reader's text size, and selection and caret are left on browser defaults. What it confirmed: Kabaal's dimmed locked setting (1.8:1 and 2.5:1) and dark snackbar action (1.2:1), the straight apostrophe, Apart's 20-high site links, Halewyn's side-striped banner. What it corrected: Halewyn's story paragraph has 47 to 54 characters per line, not the 40 reported.

Generic tells it asks about: all three products set a spent typeface (DM Sans; Newsreader and Instrument Sans; Roboto on the web page). Halewyn's hero is an italic serif at display size with a tracked-caps eyebrow. Apart's hatching is flagged as stripes and stays: it carries data.
