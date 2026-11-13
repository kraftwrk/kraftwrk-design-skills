---
name: agency-grade-review
description: Critique and quality gate for product design at the level of top agencies (Work & Co, MetaLab, Fantasy, AKQA, Clay, Framna). Use when asked to review, critique, audit, rate or improve a screen, flow, prototype, component, design system or design deliverable, when asked whether something is good enough or ready, before shipping or presenting, and as the mandatory self-review after generating any UI.
---

# Agency-grade review

## What this skill is

A structured critique that measures the distance between a design and agency-grade work, and says exactly how to close it. Two modes:

- Review mode: critiquing work (the designer's, a client's or Claude's) with findings, fixes and, when asked, scores.
- Gate mode: the mandatory self-review Claude runs on its own UI output before showing it. Fix first, then show, then report what was fixed.

Depends on product-design-foundations (the baseline), product-brand-identity (identity), the active personal style skill (for Marc: kraftwrk-design-style), Emil Kowalski's review-animations for motion and Vercel's web-design-guidelines for web code, when those are installed.

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

## Review protocol

Work through the sections in order. List findings before fixes. Only Quick mode skips sections.

### 0. Context

State in one line each: platform, audience, the job, the design system in play, which skills apply, and the mode requested (Quick, Full or Pre-ship).

### 1. Purpose and structure

- Can the job and primary action be identified in 3 seconds?
- Is anything competing with the primary action? Is anything removable without loss?
- Does the flow offer an obvious next step at every point? Are back and cancel paths present?
- Does the layout mirror the information architecture (most important is most visible)?

### 2. Layout and spacing

- Are spacing values on the scale? Is the rhythm correct (inside < between < section)?
- Count the vertical alignment edges per region. More than 2 is a finding.
- Is density consistent across screens? Are grid and margins consistent per breakpoint?
- Do containers earn their place? Flag card-in-card, redundant dividers and box soup.

### 3. Typography

- Count sizes and weights. More than 7 sizes, or 3 or more weights in UI text, is a finding.
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

- Context first (problem, audience, constraints), then decisions and why, then the work.
- Real content in realistic device frames at correct scale. Multiple states. Motion shown as video or a sequence. Dense screens shown, not only heroes.
- Before and after where there was a before. Outcomes where known.
- The typography and layout of the presentation itself meet this bar.

## Tests

Run the relevant ones and report results, not impressions.

- 3-second test: what is this and what should I do?
- Greyscale test: is the hierarchy intact without colour?
- Squint test: are the structure and colour stance still readable?
- Swap test: logo replaced by a competitor's. If it still looks right there is no identity.
- Count test: distinct font sizes, weights, colours, radii and spacing values. Report the counts.
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

- Quick (about 5 minutes): sections 1, 2, 3, 5 and 7, plus the 3-second, squint and count tests. Top 5 findings.
- Full: all sections, all relevant tests, scores.
- Pre-ship: Full, plus accessibility measured, every state present, spec checked, platform QA on real devices noted. Any Blocker means not ready.

## Anti-patterns in reviewing

- Vague feedback ("make it pop", "feels off"). Every finding names the element, the rule and the fix.
- Taste disguised as rule. Separate "violates the baseline" from "I would choose differently", and label the second.
- Reviewing only the hero. Always ask for the dense and ugly screens.
- Scores without evidence: unmeasured contrast, uncounted sizes.
