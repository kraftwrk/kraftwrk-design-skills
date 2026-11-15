---
name: product-design-foundations
description: Technical baseline for any digital product UI on web, iOS, Android or React Native. Layout, spacing, grid, typography, colour, components and states, content and edge cases, accessibility, platform conventions, motion basics, design tokens and handoff. Use whenever designing, building, prototyping, specifying or reviewing screens, components, flows or design systems, before any brand or personal style layer is applied.
---

# Product design foundations

## What this skill is

The floor, not the ceiling. These are the rules that make a product UI technically mature: what agencies at the level of Work & Co, MetaLab, Framna and Clay get right by default, before taste enters. Every screen, component and prototype must meet them. Identity, style and signature come from other skills layered on top.

The rules are written to be checkable. Where a rule gives a number, treat the number as the default and any deviation as something to state and justify.

Values follow Google's Material Design 3 and Apple's Human Interface Guidelines: the major second type scale, the 4px grid, platform text styles, the Material shape scale, platform component metrics and state layers. Break out only when a specific case really requires it, and write the exception down with its reason.

## How skills stack

1. The client's design system (tokens, components, brand assets): the vocabulary. It wins on names and values.
2. product-design-foundations (this skill): the technical baseline.
3. typography-craft: how type is chosen, paired, set and reviewed.
4. product-ui-patterns: the pattern library (screens and components with their anatomy and values).
5. product-brand-identity: how the product gets or expresses its identity.
6. A personal or studio style skill (for Marc: kraftwrk-design-style): the signature.
7. agency-grade-review: the gate. Run it before showing work.
8. design-decision-log: the learning loop. Decisions made in a project become rules in these skills or a record in the project.

Motion: when Emil Kowalski's skills are installed (emil-design-eng, animate, animate-expo, review-animations, choreograph, gestures, animation-performance), they govern all motion work and take precedence over the motion section below. Web code review: use Vercel's web-design-guidelines skill when it is installed.

Conflicts: the accessibility floor beats everything. The client system beats this skill on token values and component choice. This skill beats taste when a taste choice would break a rule here. Where Vercel's guidelines conflict with the product's own conventions (for example its case convention), the product wins.

Standards referenced throughout: Apple Human Interface Guidelines, Material Design 3, WCAG 2.2, the W3C Design Tokens format. When the two platforms differ, use the platform the product ships on; on the web, use Material's values with iOS conventions for touch targets.

## Before designing

Write one line for each, then proceed:

- The job: the one thing this screen or flow must do excellently.
- The user and the moment: who, where (phone on the move, desk), how often (daily tool or occasional).
- The primary action: exactly one per screen.
- The platform(s) and the design system in play.
- The content reality: realistic data ranges (shortest, typical, longest) and counts (0, 1, many, thousands).

If one of these is unknown and changes the result, ask once. Otherwise state the assumption and continue.

## Layout and spacing

- The 4px grid (Material's 4dp grid, Apple's 4pt increments): every spacing value and component size is a multiple of 4. Layout spacing uses the 8 steps: 8, 16, 24, 32, 40, 48, 64; the 4 steps (4, 12, 20) are for inside components and optical corrections. No values off the grid except documented optical corrections.
- Rhythm: space inside a group < space between groups < space between sections, with at least a 2x step between levels (for example 8 inside, 16 between, 32 for sections).
- Layout per Material window size class: compact (under 600) 4 columns with 16 margins (20 on larger phones per HIG); medium (600 to 839) 8 columns with 24 margins; expanded (840 and up) 12 columns with 24 margins, content max width 1200 to 1440, reading column max 720. Design at 360, 768, 1024 and 1440 as the representative widths.
- Alignment: at most 2 vertical alignment edges per screen region, and everything snaps to them. Optical alignment beats mathematical alignment where icons and text meet.
- Group by proximity and alignment first. Add a container (card, divider, background) only when proximity cannot do the job. Never a card inside a card.
- Separation order: spacing, then a hairline, then a surface tint, then a border, then a shadow. Hairlines use the platform separator token (iOS separator, Material outline-variant); a custom hairline is 1px at 15 to 25 percent of the foreground colour on light and 15 to 25 percent white on dark. Grids of media tiles (products, covers, thumbnails) carry no borders; the gap does the work.
- Cards are single-purpose: a sheet, a tile, a stat card. A list is rows with hairlines, not a stack of cards.
- Density is one choice per product: compact (data tools, 32px rows), default (40px rows) or comfortable (consumer, 48 to 56px rows). Keep it consistent across screens.
- Left-align text and controls by default in LTR languages. Centre only short, isolated content: empty states, confirmations, hero moments.
- Responsive: content reflows across window size classes, it does not just scale. Text sizes and hit targets never drop below the floors in this file.
- Safe areas: respect notches, home indicators and system bars. Bottom actions sit above the home indicator. Full-bleed content uses inset-aware padding.
- Scrolling: one scroll container per screen unless a nested one is intentional (horizontal carousel, code block). Sticky headers compress; they do not vanish abruptly.

## Typography

The values are here; the craft (choosing and pairing faces, composing headlines and hero figures, numerals, micro-typography, rendering) is in typography-craft.

- The type scale is the major second (ratio 1.125) from the platform body size, rounded to whole pixels and snapped to Material 3's named sizes: 11, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 45, 57. A product uses 5 to 7 of these steps, mapped to the platform roles.
- Platform roles are the reference, not a custom scale. Material 3: display 57/45/36, headline 32/28/24, title 22/16/14, body 16/14/12, label 14/12/11 (sp), with the line heights Material specifies (for example body large 16/24, headline small 24/32, display small 36/44). iOS text styles at the default size: Large Title 34, Title 1 28, Title 2 22, Title 3 20, Headline 17 semibold, Body 17, Callout 16, Subheadline 15, Footnote 13, Caption 1 12, Caption 2 11 (pt), with Dynamic Type. Web follows the Material scale with 16px body.
- Body size: 16px on web, 17pt iOS body, 16sp Android body large. 12 and 11 are for captions and labels only, never body text.
- Line height: Material's per-style values on Android and web (roughly 1.5 for body, 1.3 for titles, 1.1 to 1.2 for display); iOS text styles bring their own leading. Larger text gets tighter leading.
- Tracking: 0 for body. Headlines of 24px and above: -0.01em to -0.02em. All-caps labels: +0.04 to +0.08em, never below 11px.
- Weights: 2 in UI (regular 400 and medium 500 or semibold 600). A third weight only for display. Hierarchy comes from size and spacing before weight, and from weight before colour.
- Line length: 45 to 75 characters for reading text (set max-width in ch). UI labels aim for one line, with the truncation rule defined.
- Numbers: tabular figures wherever numbers align in columns or change in place (prices, counters, timers). Proportional figures in running text.
- Hero figure: the one number or headline a screen exists for (balance, ETA, total, score, event title) is set 2 to 3 times the body size (Material headline large 32 to display small 36, iOS Large Title 34), with its unit, currency or label small beside or beneath it in secondary colour. One hero figure per screen; everything else steps down.
- Observed mobile scale in agency work, which the platform roles cover: headlines 24 to 32, hero figures 32 to 36, body 16 to 17, meta 12 to 13, tab labels 10 to 12 or icons only.
- Case: one convention per product. Sentence case is the default for UI; Title Case only when the platform or brand requires it. Apply the convention everywhere, including buttons and menus.
- Details: real ellipsis character, curly quotes, non-breaking space between number and unit, balanced headlines without orphans.
- Typeface selection: full character set for the markets served, tabular figures, a true italic or none, weights that render well at 14px, variable font where possible, a defined loading strategy and a fallback with matched metrics.

## Colour

- Define roles, not just swatches: background (canvas, surface, surface raised), foreground (primary, secondary, tertiary, disabled), border (subtle, strong), accent (default, hover, pressed, subtle), semantic (success, warning, danger, info, each with foreground, background and border).
- Neutral ramp: 10 to 12 steps, tinted slightly towards the brand hue unless the brand demands pure grey. Build light and dark themes from the same hues.
- One accent. Additional hues only when the information model needs them (categories, chart series), and then from a defined categorical set.
- Contrast: 4.5:1 for text under 24px, 3:1 for text 24px and above, 3:1 for component boundaries and meaningful icons. Check every text and background pair in both themes. Disabled text may fail contrast but must read as disabled by other means.
- Never meaning by colour alone: pair colour with an icon, text or position.
- Dark mode is designed, not inverted: desaturate accents, express elevation by surface lightness instead of shadows, soften pure white text to around 90% opacity equivalents, re-check all contrast.
- Dark mode values that hold up, and that match the platforms: canvas between #0A0A0A and #121212 (iOS system background is pure black, Material 3 surface is a near-black tinted to the brand hue), or a brand-tinted dark (navy, deep green) when the brand has a hue; surfaces 2 to 3 steps lighter than the canvas (Material surface container levels, iOS secondary and tertiary backgrounds); secondary text at 60 percent white (iOS secondary label), tertiary at 30 percent; hairlines at 15 to 25 percent white; the accent on one element per screen; no drop shadows.
- Interaction states follow Material 3 state layers (hover 8 percent, focus 10 percent, pressed 10 percent, dragged 16 percent of the content colour) or iOS highlight conventions; disabled content at 38 percent, disabled containers at 12 percent.
- Text over photography sits on a gradient scrim (image fading into the canvas colour) and still meets 4.5:1 against the darkest or lightest part of the scrim; never on an unscrimmed photo.
- Elevation: one system. Material 3 elevation levels 0 to 5 with tonal surface colour (and shadows only where Material uses them); on iOS, system materials and background levels instead of shadows. Never shadow, border and tint together on one element.
- Radius comes from the Material 3 shape scale: none 0, extra small 4, small 8, medium 12, large 16, extra large 28, full (pill); iOS uses continuous corners at comparable values. The brand picks one logic from this scale and holds it.
- Gradients and glass effects only as a documented brand decision from product-brand-identity, never as a default.

## Components and states

- Every interactive component defines: default, hover (pointer devices only), focus-visible, pressed, disabled, loading, selected or checked, error where it carries input, and read-only where relevant.
- Every screen or container defines: empty on first use, empty after filtering, loading (skeleton that matches the final layout), partial or paginated, error with a recovery action, offline, and success or confirmation.
- Sizes come from the platform metrics: Material buttons 40 high (48 touch target), chips 32, text fields 56, list items 56 (one line) / 72 (two lines) / 88 (three lines), top app bar 64, navigation bar 80, FAB 56; iOS buttons 44 to 50, table cells 44 minimum, navigation bar 44, tab bar 49, search bar 36. A product's own size set (for example sm 32, md 40, lg 48) is built on these, with consistent padding and icon size per size. No ad-hoc heights.
- Hit targets: at least 44x44pt on iOS, 48x48dp on Android, 24x24 CSS px on web with 44 recommended for touch. The visual size may be smaller than the hit target.
- Icons: one family, one stroke weight, one optical size system (Material 20 and 24, SF Symbols scaled to the text style). Icons sit optically on the text baseline. Icon-only controls carry an accessible label and, on pointer devices, a tooltip.
- Forms: label above the field (or a floating label), helper text below, validation on blur, error text that says how to fix the problem, correct input types and keyboards, autocomplete attributes, no placeholder as the only label, submit stays enabled until the request starts and then shows progress.
- Buttons: one primary per view. Labels are verbs that name the result ("Save changes", "Send invoice"). Destructive actions look different and either confirm or offer undo.
- Task screens on mobile end in one full-width primary action pinned above the safe area (48 to 56 high; a pill or a bar, depending on the product's radius logic); secondaries are grey pills, hairline outlines or text links, never a second filled button.
- Sheets: bottom sheets carry a drag handle (Material 32x4, iOS 36x5), a top radius from the shape scale (Material extra large 28, or the product's large value), hairline rows inside, and a single primary action; they track the finger and can be dismissed by drag.
- Media and product grids: 2 columns in compact, 4 in expanded, gaps of 12 or 16, no borders on tiles, metadata under the tile in two lines (title, then secondary in grey), price or status right-aligned or on its own line.
- Lists and tables: defined row height, alignment by column type (numbers right, text left), sort and filter states, selection and bulk actions, and a plan for 1000 rows.
- Navigation mirrors the platform: tab bar on iOS (49pt, 2 to 5 tabs, 10pt labels), navigation bar on Android (80dp, 3 to 5 destinations, 12sp labels, navigation rail from medium up), sidebar or top bar on web. 3 to 5 top-level destinations, labels or icons only with accessible names. Current location is always visible. Headers stay minimal: a wordmark or title plus at most two icon buttons; no hamburger menus in native apps.
- Feedback: every action responds within 100ms (pressed state). Anything longer than 1 second shows progress. Success is confirmed where it is not self-evident.
- Content handling: a truncation rule per element (1-line clamp, 2-line clamp, middle truncation for file names), wrapping for long words, min-width 0 on flex children.

## Content and edge cases

- Design with real content. Realistic names, numbers, dates and titles, including the long and awkward ones. Never lorem ipsum.
- Cover the data range: 0 items, 1 item, the typical count, the extreme count. Shortest and longest strings. Missing optional data.
- Localisation: text can grow 30 to 40%. Dates, numbers and currencies format per locale. Plan RTL where the market requires it.
- Timestamps: relative for the recent past ("2 min ago"), absolute after about a week. Never "340 days ago".
- Pluralisation and zero states are handled ("1 member", "No members yet").
- Copy inside the product is short, specific, active and written for the moment. Errors say what happened and what to do next.

## Accessibility (the floor)

- WCAG 2.2 AA minimum for everything that ships.
- Full keyboard operation on web and desktop: visible focus indicators, logical focus order, focus management in dialogs and after actions.
- Screen readers: semantic structure, labelled controls, announced state changes, headings in order.
- Text scaling: layouts survive 200% text on web and the largest accessibility sizes on mobile. Test it, do not assume it.
- Reduced motion settings respected: keep opacity fades, remove movement.
- Colour independence and contrast as above. No flashing content.
- Hit targets as in Components.

## Platform conventions

- iOS: follow the Human Interface Guidelines. Native navigation patterns (push, modal sheet, tab bar), system gestures (back swipe), SF Pro or a brand face with matched metrics, Dynamic Type, haptics only for meaningful confirmations, safe areas, large titles where they fit. Never Android patterns on iOS (hamburger menus, snackbars).
- Android: Material 3 behaviour (predictive back, system bars, edge to edge), ripple or an equivalent pressed feedback, bottom navigation or navigation rail, Material motion durations. Brand may override the look, never the behaviour.
- React Native and Expo: native components for inputs, pickers, sheets and navigation wherever possible. Specify what is native and what is custom. Gestures and animations run on the UI thread (Reanimated). Handle the keyboard: avoiding view, safe area, scroll into view.
- Web: responsive from 360px, real breakpoints, URL reflects state (tabs, filters, pagination), links are links and buttons are buttons, native form elements styled rather than rebuilt where possible.
- Desktop apps and dense web tools: keyboard shortcuts, a command palette where it fits, resizable panes, layout state that persists.

## Motion baseline

Defer to Emil Kowalski's skills when installed. Otherwise:

- Animate only transform and opacity. Never transition all properties.
- UI motion stays under 300ms: micro feedback 100 to 160ms, popovers and menus 150 to 250ms (Material short 2 to 4 and medium 1). Sheets and full-screen modals are the exception and may take up to 400ms (Material medium 4; iOS push and sheet transitions run about 350ms). Exits are faster than entrances.
- Easing: ease-out for entering and responding, ease-in-out for elements moving on screen, linear only for constant motion. Never ease-in for UI. Material 3's standard and emphasized curves and iOS springs are the defaults on their platforms.
- Nothing appears from scale(0). Nothing animates on keyboard-driven or very frequent actions.
- Popovers originate from their trigger. Sheets and drawers track the finger and can be interrupted.
- Reduced motion: fades instead of movement.
- Every animation can name its purpose: feedback, spatial continuity, state change or explanation. Decorative motion only in rare or first-time moments.

## Design tokens and systems

- Three tiers: primitive (colour.blue.600, space.4), semantic (colour.bg.surface, colour.fg.primary, space.inset.md), component (button.bg.primary.hover). UI uses semantic and component tokens, never primitives directly.
- Name by role and intent, not appearance: fg.secondary, not grey.600.
- Every component is documented with anatomy, variants, sizes, states, content rules, accessibility notes, do and don't examples, and token mapping.
- Figma: auto layout throughout, variables for every value, component properties for variants and states, slots for content, layer names that match code names.
- Code: CSS variables or platform token files generated from one source. Light, dark and high-contrast are theme layers over semantic tokens.
- Extend a system in its own language. Propose additions explicitly ("new token: colour.bg.warning.subtle") instead of hard-coding a value.

## Specification and handoff

A design is finished when an engineer can build it without guessing. Specify:

- Layout: grid, spacing as tokens, alignment, responsive behaviour per breakpoint.
- Type and colour as tokens.
- Components: variant, size and state, and any deviation from the system.
- Behaviour: tap, hover, focus, error, timeout and success; loading and empty states; keyboard behaviour.
- Motion: duration, easing or spring configuration, choreography order, reduced-motion fallback.
- Content: real copy, truncation rules, limits.
- Edge cases: 0, 1, many and too many; shortest and longest; offline; permissions denied.

## Anti-patterns (fix on sight)

- Spacing off the 4px grid, mixed row heights, more than 2 alignment edges per region.
- Sizes off the major second scale, more than 7 text sizes in use, 3 or more weights in UI, body text under 14px, large headlines without tightened tracking.
- Platform metrics ignored (undersized tab bars, 36px buttons on touch, custom heights where a platform value exists) without a written reason.
- Pure grey neutrals next to a tinted palette, accent used as decoration, meaning carried by colour alone.
- Card inside card; border, shadow and tint on the same element; dividers and whitespace doing the same job; bordered media grids; lists built as stacks of cards.
- A mid-grey canvas chosen by default; an accent spread over tab bars, headers, cards and buttons at once; two filled buttons competing on one screen; text on unscrimmed photos.
- Placeholder as the only label, submit disabled before the request, errors that only say "Something went wrong".
- Happy path only, lorem ipsum, perfectly short fake names.
- Mixed icon families or weights, emoji as icons, icon-only controls without labels.
- Hover states on touch, UI motion over 300ms, ease-in, transitions on all properties, scale(0) entrances.
- Web or Android patterns on iOS and the reverse.
- Raw hex values or primitive tokens in component code, one-off components that duplicate existing ones.

## Self-review before showing anything

Run this list, fix failures first, then run agency-grade-review when it is available.

1. One job, one primary action, nothing that could be removed without loss?
2. All spacing on the 4px grid, rhythm correct, at most 2 alignment edges per region, separation by spacing and hairlines before boxes?
3. Type on the major second scale mapped to platform roles, correct leading and tracking, tabular numbers where needed, one case convention, one hero figure per screen at 2 to 3 times body?
4. Colour roles used, contrast passes in both themes, no colour-only meaning?
5. Every component state and every screen state present?
6. Real content including long, short, zero and many, with localisation headroom?
7. Hit targets, keyboard, focus, screen reader labels and text scaling handled?
8. Platform conventions respected?
9. Motion durations, easing, interruptibility and reduced motion correct?
10. Tokens only, system extended in its own language, additions flagged?
11. Spec complete enough to build without guessing?
12. Every value traceable to Material 3, Apple HIG or a written exception?
