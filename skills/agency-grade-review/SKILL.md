---
name: agency-grade-review
description: Critique and quality gate for product design at the level of top agencies (Work & Co, MetaLab, Fantasy, AKQA, Clay, Framna). Use when asked to review, critique, audit, rate or improve a screen, flow, prototype, component, design system or design deliverable, when asked whether something is good enough or ready, before shipping or presenting, and as the mandatory self-review after generating any UI.
---

# Agency-grade review

## What this skill is

A structured critique that measures the distance between a design and agency-grade work, and says exactly how to close it. Two modes:

- Review mode: critiquing work (the designer's, a client's or Claude's) with findings, fixes and, when asked, scores.
- Gate mode: the mandatory self-review Claude runs on its own UI output before showing it. Fix first, then show, then report what was fixed.

Depends on product-design-foundations (the baseline), typography-craft (type), product-ui-patterns (the pattern library), product-brand-identity (identity), the active personal style skill (for Marc: kraftwrk-design-style), Emil Kowalski's review-animations for motion and Vercel's web-design-guidelines for web code, when those are installed. Findings that Marc overrides are signals for design-decision-log.

Two reviews, one table: when Intent is installed, its evaluate skill reviews usability, task success and manipulative patterns, and this skill reviews craft, identity and platform. Report both in one findings table; Intent's critical, major, minor and cosmetic are this skill's Blocker, Major, Minor and Polish.

The measured part of this review is a script: scripts/audit.py beside this file (see its README). It reads the render and reports contrast in every theme and state, counts, grid, targets, text scaling, a motion inventory and the generic tells, with values. Where the script is not at hand, measure the same things with a script written for the purpose. Never estimate.

## The bar: what agency-grade means

Agency-grade work has all of these at once:

1. Clarity of purpose: the one job is obvious within 3 seconds and the primary action is unmistakable.
2. Hierarchy that survives greyscale, a blur and a glance.
3. Typographic precision: scale, leading, tracking, alignment and rhythm are deliberate. Nothing is a default.
4. Spatial discipline: one spacing scale, consistent alignment edges, intentional density.
5. Colour with intent: a clear stance, roles not swatches, accent only where it means something, contrast passes in both themes.
6. Real content: realistic data, long and short, zero and many, copy written for the moment.
7. Completeness: every component and screen state exists and the flow has no dead ends.
8. Identity: unmistakably itself (passes the swap test), coherent across surfaces, loud and quiet in the right places.
9. Motion that explains: purposeful, fast, interruptible, with one consistent character.
10. Platform fluency: feels native, uses conventions users already know.
11. Accessibility by default: WCAG 2.2 AA, keyboard, screen reader, text scaling.
12. Production readiness: tokens, components, specs. An engineer can build it without guessing.
13. Finish: nothing accidental. Optical alignment, consistent radii and strokes, pixel-fit icons, balanced headlines, correct punctuation.
14. Restraint: no noise. Nothing stays that nobody would miss, and nothing goes that a user would describe to a friend. Decoration only as a documented brand decision.
15. Presentation: the work is shown with context, decisions and rationale, in realistic frames, with states and motion, not as a single hero shot.
16. Invention: each key screen has one thing no template would have given, an interaction, a device or a way of showing the data, and it does a job. The steal test: would another designer want to take it? The job test: is the task faster or clearer with it, or the brand idea carried by it? A screen that is only correct scores 3.

Generic work, the level this skill lifts from, typically shows: default fonts and sizes, random spacing, cards everywhere, blue 600 everywhere, lorem ipsum or perfectly short fake data, happy path only, hover-only states, bouncy or slow motion, no dark mode, a logo-only identity, and a single centred hero shot as presentation.

## Visual tells (what agency-grade screens look like, from the case studies)

A quick scan before the full protocol. Observed across the published product work of Work & Co, MetaLab, Clay, Fantasy, AKQA, Framna and Wolff Olins.

| Agency-grade | Generic |
| --- | --- |
| Canvas is a decision: warm cream, near-black, white, or the brand gradient on hero screens | Mid-grey canvas chosen by default |
| One accent on action, selection, status or progress; roughly 5 percent of the screen or less; luxury uses none | Accent on tab bar, header, cards and buttons at once |
| A display type voice plus a neutral workhorse; one hero figure per screen at 2 to 3 times body | Everything at similar sizes and weights; three typefaces |
| Spacing and hairlines separate content; single-purpose cards; borderless media grids | Card soup, nested cards, bordered tiles, shadows everywhere |
| One radius logic held constant on the Material shape scale (sharp 0 to 4, friendly 8 to 12, soft 16 to 28) | Mixed radii across buttons, cards and inputs |
| Imagery art-directed; chrome goes monochrome when imagery is the colour; text on gradient scrims | Stock photos, text on unscrimmed images, imagery competing with UI colour |
| 3 to 5 bottom tabs, minimal header, sheets with grabbers, one full-width primary at the bottom | Hamburger menus in native apps, two filled buttons, floating action buttons by default |
| Brand loud at launch, login, onboarding and success; quiet and monochrome in tables, carts, settings | Illustration and brand colour inside forms and tables |
| Dark mode designed (near-black or brand-tinted canvas, lighter surfaces, 60 to 70 percent secondary text, no shadows) | Inverted light mode with grey cards and shadows |
| Copy with personality in small moments; plain verbs on controls | Jokes on buttons, generic verbs ("Submit", "OK") everywhere |
| Dense screens designed and shown | Only hero screens exist |
| One or two carriers pushed to an extreme, the rest on platform defaults; one recurring brand device | Everything at medium intensity, or everything loud; no device, or a logo used as one |
| Type does the identity work: a chosen voice, display tracking tuned (tightened on brand faces, platform tracking on system faces), tabular hero figures, real punctuation | Default font at default sizes, untuned display tracking, straight quotes, jumping numbers |
| A face, a canvas and a layout with a reason from this product | The reflexes of generated work: a spent typeface, a warm off-white ground by default, an italic serif hero, a tracked-caps eyebrow over every heading, a thick coloured border on one side of a card, gradient text, coloured glows, an icon in a rounded square over every feature heading, the same reveal on every section |

## Review protocol

Work through the sections in order. List findings before fixes. Only Quick mode skips sections. Judge before measuring: answer sections 1 to 7 from the render first, then read the audit; a clean audit is a floor, not proof. Before judging a screenshot, confirm it shows what its name says (fonts loaded, motion settled, the right theme, state and language).

### 0. Context

State in one line each: platform, audience, the job, the design system in play, which skills apply, and the mode requested (Quick, Full or Pre-ship).

### 1. Purpose and structure

- Can the job and primary action be identified in 3 seconds?
- Is anything competing with the primary action? Is anything removable without loss?
- Does the flow offer an obvious next step at every point? Are back and cancel paths present?
- Does the layout mirror the information architecture (most important is most visible)?

### 2. Layout, patterns and spacing

- Which pattern from product-ui-patterns does each screen use? Is its anatomy complete and are its values on the platform metrics? A layout invented where a pattern exists, or two patterns mixed for one job, is a finding.
- Are spacing values on the 4px grid? Is the rhythm correct (inside < between < section)?
- Count the vertical alignment edges per region. More than 2 is a finding.
- Is density consistent across screens? Are grid and margins consistent per breakpoint?
- Do containers earn their place? Flag card-in-card, redundant dividers and box soup.

### 3. Typography

- Run the typography review in typography-craft (12 checks). The counts below are the minimum.
- Count sizes and weights. More than 7 sizes, sizes off the major second scale, or 3 or more weights in UI text, is a finding.
- Are leading and tracking correct for each size? Brand-face headlines tightened, system faces on platform tracking, caps tracked out?
- Are reading line lengths between 45 and 75 characters? Are truncation rules defined?
- Are numbers tabular where they align or change? Is the case convention consistent? Are typographic details right (ellipsis, quotes, non-breaking spaces)?

### 4. Colour

- Is the stance clear? Are roles used? Is the accent reserved for meaning?
- Measure contrast for every text and background pair in both themes. Report the ratios that fail.
- Is any meaning carried by colour alone? Are semantic colours harmonised with the brand?
- Is dark mode designed (elevation by lightness, desaturated accents) rather than inverted?

### 5. Components and states

- For each component: are all states present and visually distinct?
- For each screen: first-use empty, filtered empty, loading, partial, error, offline, success?
- Do sizes come from the size set? Are hit targets at or above the floor?
- Forms: labels, helper text, inline errors with fixes, correct keyboards and autocomplete?

### 6. Content

- Real content? Long, short, zero and many? Localisation headroom?
- Is copy specific to the moment? Do buttons name the result? Do errors say what to do?
- Are timestamps, pluralisation and number formatting handled?

### 7. Identity

Run the tests from product-brand-identity: ten decisions, default count, intensity, device, swap, one-author, moments and idea tests. Flag trend used as identity, brand as decoration, and a generic SaaS look where a bespoke identity was asked for.

### 8. Motion

Use review-animations when installed. Otherwise check: purpose stated, UI motion under 300ms, correct easing or springs, interruptible, origin-aware, reduced motion handled, consistent character. Read the motion inventory from the audit: every transition has a row in the motion table, nothing is invisible with animation off, hover is guarded and never moves its own target, loops carry live information.

### 9. Platform and accessibility

- Platform conventions respected (navigation, gestures, system components)?
- Platform currency: do bars, sheets, controls and motion match the current guidelines (iOS 26 and later: system Liquid Glass bars, no glass in the content layer; Material 3: the flexible navigation bar, spring motion)?
- Keyboard, focus, screen reader labels, text scaling, safe areas?

### 10. Production readiness

- Tokens instead of raw values? Components reused rather than duplicated? System extended in its own language with additions flagged?
- Is the spec complete: behaviour, states, motion values, edge cases?

### 11. Finish

Optical alignment of icons and text, consistent radii and stroke weights, pixel-fit icons, correctly cropped images, balanced headlines without orphans, consistent punctuation.

### 12. Presentation (for deliverables, case studies and portfolio work)

The conventions the agencies use when they show product work:

- Context first (problem, audience, constraints), then decisions and why, then the work.
- Flat device frames on flat colour fields, in 3-up or 4-up rows. The field follows the product's personality: black for sport, gaming and entertainment; cream or a pale tint for lifestyle and finance; the brand colour for identity work.
- One angled 3D device for the hero at most; everything else flat. 3D is rationed, never the default.
- Component close-ups: one component cropped huge on a neutral field (a card, a chip set, a row) to show the craft.
- System sheets: type sample, colours or gradients with names, a token table, an icon sheet, or a bento mosaic of system elements with construction lines.
- Context photography when scale and use matter: the product in a hand, on a table, in a room.
- Short captioned loops (3 to 10 seconds) for motion and interaction; one line of caption per loop.
- Real content at correct scale, multiple states, and the dense and ugly screens (list, table, cart, settings) alongside the heroes.
- Web screens at compact (390) and expanded (1440) side by side. Prototypes carry switches for theme, state, the longest language and text size, marked up so the audit can drive them: data-screen and data-platform on each screen, data-set on each switch, data-system on drawn system chrome.
- Before and after where there was a before. Outcomes in numbers where known.
- The typography and layout of the presentation itself meet this bar.

## Tests

Run the relevant ones and report results, not impressions.

- 3-second test: what is this and what should I do?
- Greyscale test: is the hierarchy intact without colour?
- Squint test: are the structure and colour stance still readable?
- Swap test: logo replaced by a competitor's. If it still looks right there is no identity.
- Count test: distinct font sizes, weights, colours, radii and spacing values, read from the render (computed styles), per surface (app and site count separately). Report the counts.
- Canvas and accent test: name the canvas decision in one line, then estimate the share of a working screen covered by the accent. No nameable canvas, or more than roughly 5 percent accent outside a brand moment, is a finding.
- Hero figure test: on each screen, name the one element set at 2 to 3 times body size. None, or more than one, is a finding.
- Default count test: count the ten identity decisions sitting on the generic default. More than six is no identity; agency-grade work has at least four non-default decisions traceable to the brand idea.
- Intensity test: name the one or two carriers pushed to an extreme. None is timid, more than two is noise.
- Worst-case data test (use break-ui when installed): longest name, 1-letter name, 0 items, 10,000 items, a 99+ badge, slow network, offline.
- Remove-one test: remove the least necessary element. Did anything break? Repeat until something does.
- Consistency test: 6 screens side by side. One author?
- Contrast test: measured, never estimated, in both themes and in every state. Text on flat grounds is computed; text over imagery, gradients or shapes is sampled from a render (hide the text, read the pixels under its box).
- State test: switch every state with the whole screen in view. Headers, counts, totals and badges that contradict the state are a Blocker.
- Flow test: check the task against the flow steps in product-design-foundations. Steps neither shown nor listed as missing are a Major.
- Thumb test (mobile): primary actions reachable one-handed, destructive actions away from habitual tap zones. Platform conventions win: a trailing navigation-bar action on iOS is not a finding, a custom placement is.
- Tells test: list the generic tells the audit reports. Each is answered with a fix or with the reason it is this product's decision (Apart's hatching is stripes that carry data, so it stays). A tell without a reason is a Minor.

## Scoring (Full and Pre-ship modes)

Rate each of the 16 bar items from 1 to 5:
5 agency-grade, nothing to fix. 4 minor polish. 3 competent but generic. 2 clear problems. 1 missing or broken.

Report the three lowest scores first; they decide the next iteration. Never average: a 2 anywhere blocks Pre-ship.

## Output format

Findings table, ordered by impact:

| # | Finding | Where | Why it matters | Fix (specific values, tokens, copy) | Severity |

Severity is Blocker, Major, Minor or Polish. Blocker: a contrast failure in any theme or state, a missing empty, loading or error state on a dense screen, a state the chrome contradicts, placeholder content, an invented claim presented as real, happy path only. Major: a hit target below the platform floor, a control without an accessible name, type that does not follow the reader's text size, motion without a reduced-motion rule, no motion table for an overlay or transition, a web screen shown at one width, flow steps missing without saying so, no brand moment in an identity direction, stand-in imagery not marked, a key screen with no invention of its own, one device carrying every screen, an interaction that exists only in a table and not live in the prototype, a bespoke part of an existing product removed without the designer's decision. Minor: a single off-grid value, an orphan, a stray weight, a generic tell without a reason. Polish: taste within the rules. A rule-break that the project's decision record lists as an exception, with its reason, is reported as an exception and is not a finding.

Then the three changes that would move the work furthest, one line each. Then scores when in Full or Pre-ship mode.

Be direct and specific. No praise padding. A short note on what is working is useful when it tells the designer what to keep.

## Gate mode: self-review of generated UI

Before showing any UI Claude produced:

1. Run sections 1 to 11 silently. Fix every Blocker and Major. Fix Minors when cheap. A fix never deletes an invention: where the two collide, keep the part and write the exception, or ask.
2. Run the audit on the rendered output (scripts/audit.py, or the same measurements by script): count, contrast, state and worst-case data tests in both themes, every state and the longest language. No Blocker or Major is left, and every advisory has its answer.
3. Show the work. Then list in 3 to 6 lines what the self-review changed and any remaining known gaps or assumptions.

Never show a first draft that fails a Blocker: missing states, contrast failures, lorem ipsum, off-scale spacing, happy path only.

## Modes

- Quick (about 5 minutes): the visual tells table, sections 1, 2, 3, 5 and 7, plus the 3-second, squint, count and canvas-and-accent tests. Top 5 findings.
- Full: all sections, all relevant tests, scores. A Full or Pre-ship review of work Claude made is run by a fresh reviewer when the tool allows it (a subagent that gets the brief, the files and this skill, not the conversation that built the work); otherwise the report says it is a self-review.
- Pre-ship: Full, plus accessibility measured, every state present, spec checked, platform QA on real devices noted. Any Blocker means not ready.

## Anti-patterns in reviewing

- Vague feedback ("make it pop", "feels off"). Every finding names the element, the rule and the fix.
- Taste disguised as rule. Separate "violates the baseline" from "I would choose differently", and label the second.
- Reviewing only the hero. Always ask for the dense and ugly screens.
- Scores without evidence: unmeasured contrast, uncounted sizes.
