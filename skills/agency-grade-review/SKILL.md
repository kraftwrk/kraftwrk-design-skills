---
name: agency-grade-review
description: Critique and quality gate for product design at the level of top agencies (Work & Co, MetaLab, Fantasy, AKQA, Clay, Framna). Use when asked to review, critique, audit, rate or improve a screen, flow, prototype, component, design system or design deliverable, when asked whether something is good enough or ready, before shipping or presenting, and as the mandatory self-review after generating any UI.
---

# Agency-grade review

## What this skill is

A structured critique that measures the distance between a design and agency-grade work, and says exactly how to close it. Two modes:

- Review mode: critiquing work (the designer's, a client's or Claude's) with findings, fixes and, when asked, scores.
- Gate mode: the mandatory self-review Claude runs on its own UI output before showing it. Fix first, then show, then report what was fixed.

Depends on product-design-foundations (the baseline), product-ui-patterns (the pattern library), product-brand-identity (identity), the active personal style skill (for Marc: kraftwrk-design-style), Emil Kowalski's review-animations for motion and Vercel's web-design-guidelines for web code, when those are installed. Findings that Marc overrides are signals for design-decision-log.

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
14. Restraint: nothing that could be removed without loss. Decoration only as a documented brand decision.
15. Presentation: the work is shown with context, decisions and rationale, in realistic frames, with states and motion, not as a single hero shot.

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

## Review protocol

Work through the sections in order. List findings before fixes. Only Quick mode skips sections.

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

- Count sizes and weights. More than 7 sizes, sizes off the major second scale, or 3 or more weights in UI text, is a finding.
- Are leading and tracking correct for each size? Headlines tightened, caps tracked out?
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

Run the tests from product-brand-identity: swap, one-author, moments and idea tests. Flag trend used as identity, brand as decoration, and a generic SaaS look where a bespoke identity was asked for.

### 8. Motion

Use review-animations when installed. Otherwise check: purpose stated, UI motion under 300ms, correct easing, interruptible, origin-aware, reduced motion handled, consistent character.

### 9. Platform and accessibility

- Platform conventions respected (navigation, gestures, system components)?
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
- Before and after where there was a before. Outcomes in numbers where known.
- The typography and layout of the presentation itself meet this bar.

## Tests

Run the relevant ones and report results, not impressions.

- 3-second test: what is this and what should I do?
- Greyscale test: is the hierarchy intact without colour?
- Squint test: are the structure and colour stance still readable?
- Swap test: logo replaced by a competitor's. If it still looks right there is no identity.
- Count test: distinct font sizes, weights, colours, radii and spacing values. Report the counts.
- Canvas and accent test: name the canvas decision in one line, then estimate the share of a working screen covered by the accent. No nameable canvas, or more than roughly 5 percent accent outside a brand moment, is a finding.
- Hero figure test: on each screen, name the one element set at 2 to 3 times body size. None, or more than one, is a finding.
- Worst-case data test (use break-ui when installed): longest name, 1-letter name, 0 items, 10,000 items, a 99+ badge, slow network, offline.
- Remove-one test: remove the least necessary element. Did anything break? Repeat until something does.
- Consistency test: 6 screens side by side. One author?
- Contrast test: measured, never estimated.
- Thumb test (mobile): primary actions reachable one-handed, destructive actions away from habitual tap zones.

## Scoring (Full and Pre-ship modes)

Rate each of the 15 bar items from 1 to 5:
5 agency-grade, nothing to fix. 4 minor polish. 3 competent but generic. 2 clear problems. 1 missing or broken.

Report the three lowest scores first; they decide the next iteration. Never average: a 2 anywhere blocks Pre-ship.

## Output format

Findings table, ordered by impact:

| # | Finding | Where | Why it matters | Fix (specific values, tokens, copy) | Severity |

Severity is Blocker, Major, Minor or Polish.

Then the three changes that would move the work furthest, one line each. Then scores when in Full or Pre-ship mode.

Be direct and specific. No praise padding. A short note on what is working is useful when it tells the designer what to keep.

## Gate mode: self-review of generated UI

Before showing any UI Claude produced:

1. Run sections 1 to 11 silently. Fix every Blocker and Major. Fix Minors when cheap.
2. Run the count test and the worst-case data test on the output.
3. Show the work. Then list in 3 to 6 lines what the self-review changed and any remaining known gaps or assumptions.

Never show a first draft that fails a Blocker: missing states, contrast failures, lorem ipsum, off-scale spacing, happy path only.

## Modes

- Quick (about 5 minutes): the visual tells table, sections 1, 2, 3, 5 and 7, plus the 3-second, squint, count and canvas-and-accent tests. Top 5 findings.
- Full: all sections, all relevant tests, scores.
- Pre-ship: Full, plus accessibility measured, every state present, spec checked, platform QA on real devices noted. Any Blocker means not ready.

## Anti-patterns in reviewing

- Vague feedback ("make it pop", "feels off"). Every finding names the element, the rule and the fix.
- Taste disguised as rule. Separate "violates the baseline" from "I would choose differently", and label the second.
- Reviewing only the hero. Always ask for the dense and ugly screens.
- Scores without evidence: unmeasured contrast, uncounted sizes.
