---
name: product-design-foundations
description: Technical baseline for any digital product UI on web, iOS, Android or React Native. Layout, spacing, grid, typography, colour, components and states, content and edge cases, accessibility, platform conventions, motion basics, design tokens and handoff. Use whenever designing, building, prototyping, specifying or reviewing screens, components, flows or design systems, before any brand or personal style layer is applied.
---

# Product design foundations

## What this skill is

The floor, not the ceiling. These are the rules that make a product UI technically mature: what agencies at the level of Work & Co, MetaLab, Framna and Clay get right by default, before taste enters. Every screen, component and prototype must meet them. Identity, style and signature come from other skills layered on top.

The rules are written to be checkable. Where a rule gives a number, treat the number as the default and any deviation as something to state and justify.

Values follow Google's Material Design 3 and Apple's Human Interface Guidelines: the major second type scale, the 4px grid, platform text styles, the Material shape scale, platform component metrics and state layers. Break out only when a specific case really requires it, and write the exception down with its reason. Platform values move with each release: these were checked against both guidelines in November 2026 (Material 3 Expressive, iOS 26 Liquid Glass). Where a value here and the current guideline disagree, the guideline wins and the value here gets updated.

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

Strategy and structure: when Intent is installed, it works before and after this stack and is never copied into it. Intent owns what is built and why: the project context (intent), the problem (strategize, investigate), flows and navigation (journey, organize), wireframes (wireframe), words (articulate), the state inventory (fortify), the usability review (evaluate) and the handoff package (specify). These skills own how it looks, moves and is built. Order: Intent's context, journey and wireframe first; this stack on top of the wireframes, which are structure only and never a look to keep; agency-grade-review and Intent's evaluate as two reviews in one findings table; Intent's specify for the handoff, with the specification from this file inside it. Where both have a rule (states, flows, accessibility, localisation), Intent's artefact is the plan and the values here are the floor it has to meet. Without Intent, the sections here apply as written.

Intent overrides, when Intent is installed:
- Values: where Intent and this skill both give a number, this skill is the floor. Touch targets 44pt on iOS, 48dp on Android, 44 for web navigation. Large text for contrast starts at 24px (Intent's reference says 18px, which is wrong). WCAG 2.2 AA. Progress shows after 1 second, not 3. Plan for 40 percent text expansion. UI motion under 300ms, sheets up to 400ms. Navigation has 3 to 5 tabs. Radii come from the Material scale. No centre action button or FAB by default. Intent's indigo #4338ca is never an accent.
- Intent's visual output (wireframes, blueprints, journey diagrams, the default deck theme of present) is internal structure. It is never shown to a client in Intent's look and never restyled into the visual design: once the structure is agreed, rebuild it in this stack.
- When Marc steers style inside a wireframe, the steer wins. Treat it as the start of visual design and do not refuse it.
- Intent's no-narrator rule covers Intent's own artefacts only. Rationale, stand-in marks and honest risks stay in visual work and case studies.
- Severity: critical becomes Blocker, high or major becomes Major, medium or minor becomes Minor, low or cosmetic becomes Polish. A contrast failure is always a Blocker. evaluate and include write into the single findings table of agency-grade-review, not into evaluation files of their own.
- specify lists the visual specification from this skill as its own artefact in the handoff contents, despite its line that a handoff holds no visual design.
- decisions.md lives at the project root. design-decision-log promotes only the entries Marc decided. Entries Intent logs as agent default are never promoted.
- The writing rules of articulate apply to deliverables, not to conversation with Marc.

Routing, when a request fits more than one skill:
- Review, critique, rate, is it ready: agency-grade-review leads. evaluate adds usability and dark-pattern findings to the same table.
- Is this accessible: include runs the audit, with the values here as the floor.
- Wireframe, lay out, what goes where: wireframe for structure only, then product-ui-patterns and kraftwrk-design-style for the visual pass.
- Flow, onboarding, checkout: journey. Navigation, IA: organize for structure, this skill for component values.
- Copy, microcopy, errors: articulate, with the Never list of kraftwrk-design-style on top.
- Brand, identity, direction: product-brand-identity, never strategize. strategize writes the problem brief first, when there is one.
- Deck, case study: present for stakeholder and research decks, section 12 of agency-grade-review for case studies and portfolio work, pptx only to edit an existing file.
- Skip the /intent banner and its context interview unless Marc types /intent. Read context-<product>.md when it exists.

Other visual skill sets: these skills decide direction, type, colour, layout and review. If Impeccable is installed as well, use only its detector as a second opinion on web code and whatever Marc asks of it by name; the rules taken from it already live here (NOTICE.md), and a finding from its detector is an advisory until one of these skills has the rule.

Conflicts: the accessibility floor beats everything. The client system beats this skill on token values and component choice. This skill beats taste when a taste choice would break a rule here. Where Vercel's guidelines conflict with the product's own conventions (for example its case convention), the product wins.

Standards referenced throughout: Apple Human Interface Guidelines, Material Design 3, WCAG 2.2, the W3C Design Tokens format. When the two platforms differ, use the platform the product ships on; on the web, use Material's values with iOS conventions for touch targets.

## Before designing

Write one line for each, then proceed:

- The job: the one thing this screen or flow must do excellently.
- The user and the moment: who, where (phone on the move, desk), how often (daily tool or occasional).
- The primary action: exactly one per screen.
- The platform(s) and the design system in play.
- The content reality: realistic data ranges (shortest, typical, longest) and counts (0, 1, many, thousands).

If one of these is unknown and changes the result, ask once. Otherwise state the assumption and continue. Read before asking: Intent's project context (context-<product>.md) answers these lines when it exists, and a DESIGN.md at the root of a code project is the system to extend, not to replace.

## Layout and spacing

- The 4px grid (Material's 4dp grid, Apple's 4pt increments): every spacing value and component size is a multiple of 4. Layout spacing uses the 8 steps: 8, 16, 24, 32, 40, 48, 64; the 4 steps (4, 12, 20) are for inside components and optical corrections. No values off the grid except documented optical corrections.
- Rhythm: space inside a group < space between groups < space between sections, with at least a 2x step between levels (for example 8 inside, 16 between, 32 for sections). A heading belongs to what it introduces: at least twice as much space above it as below it (24 above and 12 below, 32 and 16).
- Layout per Material window size class: compact (under 600) 4 columns with 16 margins (20 on larger phones per HIG); medium (600 to 839) 8 columns with 24 margins; expanded (840 to 1199) 12 columns with 24 margins; large (1200 to 1599) and extra-large (1600 and up) keep 12 columns and cap the content width at 1200 to 1440 or add a pane. A reading column is sized in characters, not in columns (the widths are in typography-craft): a 720 column holds about 100 characters at 16 body. Design at 360, 768, 1024 and 1440 as the representative widths.
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
- Line height: Material's per-style values on Android and web (roughly 1.5 for body, 1.3 for titles, 1.1 to 1.2 for display); iOS text styles bring their own leading (Body 17/22, Large Title 34/41), which is not on the 4 grid and stays as Apple set it. Larger text gets tighter leading.
- Tracking: system faces keep their platform tracking. SF Pro adjusts it at every size (in mockups apply Apple's table, for example 17 at -0.43 and 34 at +0.40); Roboto uses Material's per-style letter spacing (body large +0.5, label large +0.1, headlines 0). For a brand typeface: 0 for body, -0.01em to -0.02em for headlines of 24px and above, +0.04 to +0.08em for all-caps labels, never below 11px.
- Weights: 2 in UI (regular 400 and medium 500 or semibold 600). A third weight only for display; light and thin weights only at 28 and above. Hierarchy comes from size and spacing before weight, and from weight before colour.
- Line length: 45 to 75 characters for reading text, counted in the render (the widths that give it are in typography-craft). UI labels aim for one line, with the truncation rule defined.
- Numbers: tabular figures wherever numbers align in columns or change in place (prices, counters, timers). Proportional figures in running text.
- Hero figure: the one number or headline a screen exists for (balance, ETA, total, score, event title) is set 2 to 3 times the body size (Material headline large 32 to display small 36, iOS Large Title 34), with its unit, currency or label small beside or beneath it in secondary colour. One hero figure per screen; everything else steps down. When the hero figure is one of the carriers the identity pushes to an extreme, it goes to 45 or 57 on the same scale, written down as the product's type exception; on iOS it stays a Dynamic Type size.
- Observed mobile scale in agency work, which the platform roles cover: headlines 24 to 32, hero figures 32 to 36, body 16 to 17, meta 12 to 13, tab labels 10 to 12 or icons only.
- Case: one convention per product. Sentence case is the default for UI; Title Case only when the platform or brand requires it. Apply the convention everywhere, including buttons and menus.
- Details: real ellipsis character, curly quotes, non-breaking space between number and unit, balanced headlines without orphans.
- Typeface selection: full character set for the markets served, tabular figures, a true italic or none, weights that render well at 14px, variable font where possible, a defined loading strategy and a fallback with matched metrics.

## Colour

- Define roles, not just swatches: background (canvas, surface, surface raised), foreground (primary, secondary, tertiary, disabled), border (subtle, strong), accent (default, hover, pressed, subtle), semantic (success, warning, danger, info, each with foreground, background and border), inverse (surface, text and action, for snackbars, toasts and tooltips) and on-image (text and action on imagery or a fixed brand ground, which never flip with the theme). A strong border meets 3:1 against its surface (inputs, radios, switches). An accent is never reused on an inverse or on-image surface without measuring it in both themes.
- Neutral ramp: 10 to 12 steps, tinted slightly towards the brand hue unless the brand demands pure grey. Build light and dark themes from the same hues. Build ramps in a perceptual space (OKLCH on the web, Material's tonal palettes on Android): even lightness steps, chroma reduced towards white and black.
- One accent. Additional hues only when the information model needs them (categories, chart series), and then from a defined categorical set.
- Contrast: 4.5:1 for text under 24px, 3:1 for text 24px and above, 3:1 for component boundaries and meaningful icons. Check every text and background pair in both themes. Disabled text may fail contrast but must read as disabled by other means. When a setting is locked, only its control dims; the label and the sentence that explains why keep their contrast.
- Never meaning by colour alone: pair colour with an icon, text or position.
- Dark mode is designed, not inverted: desaturate accents, express elevation by surface lightness instead of shadows, soften pure white text to around 90% opacity equivalents, re-check all contrast.
- Dark mode values that hold up, and that match the platforms: canvas between #0A0A0A and #121212 (iOS system background is pure black, Material 3 surface is a near-black tinted to the brand hue), or a brand-tinted dark (navy, deep green) when the brand has a hue; surfaces 2 to 3 steps lighter than the canvas (Material surface container levels, iOS secondary and tertiary backgrounds); secondary text at 60 percent white (iOS secondary label), the lightest text anyone has to read; the 30 percent tertiary step measures about 2.4:1 and is for placeholders, disabled glyphs and decoration only; hairlines at 15 to 25 percent white; the accent on one element per screen; no drop shadows.
- Interaction states follow Material 3 state layers (hover 8 percent, focus 10 percent, pressed 10 percent, dragged 16 percent of the content colour) or iOS highlight conventions; disabled content at 38 percent, disabled containers at 12 percent.
- Text over photography sits on a gradient scrim (image fading into the canvas colour) and still meets 4.5:1 against the darkest or lightest part of the scrim; never on an unscrimmed photo. A flat pigment or brand-colour ground needs no scrim, only the measured 4.5:1. Secondary text on a coloured ground is a step of that ground's hue or the on-colour text at reduced opacity, never a neutral grey from the ramp, which reads washed out there.
- Elevation: one system. Material 3 elevation levels 0 to 5 with tonal surface colour (and shadows only where Material uses them); on iOS, system materials and background levels instead of shadows. Never shadow, border and tint together on one element.
- Radius comes from the Material 3 shape scale: none 0, extra small 4, small 8, medium 12, large 16, extra large 28, full (pill), plus the Material 3 Expressive steps large increased 20, extra large increased 32 and extra extra large 48; iOS uses continuous corners at comparable values. The brand picks one logic from this scale and holds it on everything the product draws (buttons, fields, cards, tiles, media, custom sheets) and on themable platform components (Material text fields, snackbars, menus). Containers the platform draws (the iOS tab bar, system sheets, alerts) keep the platform radius.
- Gradients and glass effects only as a documented brand decision from product-brand-identity, never as a default.

## Components and states

- Every interactive component defines: default, hover (pointer devices only), focus-visible, pressed, disabled, loading, selected or checked, error where it carries input, and read-only where relevant.
- Every screen or container defines: empty on first use, empty after filtering, loading (skeleton that matches the final layout), partial or paginated, error with a recovery action, offline, and success or confirmation. Each state changes everything that depends on it: counts, totals, badges and summaries in headers and tabs follow the empty, loading and error states.
- Sizes come from the platform metrics. Material: buttons 40 high (the default small size, 48 touch target), chips 32, text fields 56, list items 56 (one line) / 72 (two lines) / 88 (three lines), small app bar 64, navigation bar 64 (the flexible navigation bar; the original 80 bar is no longer recommended), FAB 56. iOS: buttons 44 to 50, table cells 44 minimum; bars and search fields are system components that size themselves (from iOS 26 they sit on Liquid Glass; the classic 44 navigation bar, 49 tab bar and 36 search bar apply to iOS 18 and earlier). A product's own size set (for example sm 32, md 40, lg 48) is built on these, with consistent padding and icon size per size. No ad-hoc heights.
- Hit targets: at least 44x44pt on iOS, 48x48dp on Android. On the web 24x24 CSS px is the legal floor, not the design value: navigation links, tabs, icon buttons and text links outside running text are at least 44 high at every width. The visual size may be smaller than the hit target.
- Icons: one family, one stroke weight, one optical size system (Material 20 and 24, SF Symbols scaled to the text style). Icons sit optically on the text baseline. Icon-only controls carry an accessible label and, on pointer devices, a tooltip.
- Forms: label above the field (or a floating label), helper text below, validation on blur, error text that says how to fix the problem, correct input types and keyboards, autocomplete attributes, no placeholder as the only label, submit stays enabled until the request starts and then shows progress.
- Buttons: one primary per view. Labels are verbs that name the result ("Save changes", "Send invoice"). A button that acts on a selection names the selection ("Reserve Comfort Electric"). The fact that limits the action sits directly above it (the available balance above Send, the time left above Play). Destructive actions look different and either confirm or offer undo.
- Task screens on mobile end in one full-width primary action pinned above the safe area (48 to 56 high; a pill or a bar, depending on the product's radius logic); secondaries are grey pills, hairline outlines or text links, never a second filled button.
- Sheets: bottom sheets carry a drag handle (Material 32x4, the system grabber on iOS), a top radius from the shape scale (Material extra large 28, or the product's large value), hairline rows inside, and a single primary action; they rest at the system detents on iOS (medium and large), track the finger and can be dismissed by drag.
- Media and product grids: 2 columns in compact, 4 in expanded, gaps of 12 or 16, no borders on tiles, metadata under the tile in two lines (title, then secondary in grey), price or status right-aligned or on its own line.
- Lists and tables: defined row height, alignment by column type (numbers right, text left), sort and filter states, selection and bulk actions, and a plan for 1000 rows.
- Navigation mirrors the platform. iOS: the system tab bar with up to 5 tabs, single-word labels and filled symbols; from iOS 26 it floats above content on Liquid Glass, content scrolls beneath it, and a search tab can sit at the trailing end (a 49pt full-width bar with 10pt labels on iOS 18 and earlier). Android: the flexible navigation bar (64dp, 3 to 5 destinations, 12sp labels, horizontal items at medium width; the original 80dp bar is no longer recommended), navigation rail from medium up. Web: sidebar or top bar. 3 to 5 top-level destinations with labels; icons only is an exception to write down, with accessible names. Current location is always visible. Headers stay minimal: a wordmark or title plus at most two icon buttons, and no custom bar background on iOS 26 and later; no hamburger menus in native apps.
- Feedback: every action responds within 100ms (pressed state). Anything longer than 1 second shows progress. Success is confirmed where it is not self-evident.
- Content handling: a truncation rule per element (1-line clamp, 2-line clamp, middle truncation for file names), wrapping for long words, min-width 0 on flex children.

## Content and edge cases

- Design with real content. Realistic names, numbers, dates and titles, including the long and awkward ones. Never lorem ipsum.
- Sample content is written at full fidelity and named as sample content in the notes. For a real product, claims are never invented: customer names and logos, testimonials, ratings, awards, press quotes, user numbers, benchmarks, prices and legal wording come from the client or stay a marked gap, with a list of what is still needed.
- Cover the data range: 0 items, 1 item, the typical count, the extreme count. Shortest and longest strings. Missing optional data.
- Localisation: text can grow 30 to 40%. Dates, numbers and currencies format per locale. Plan RTL where the market requires it. Checkout, consent and subscription buttons use the wording the market's law requires (Germany: "Zahlungspflichtig bestellen"); design the button for that string.
- Timestamps: relative for the recent past ("2 min ago"), absolute after about a week. Never "340 days ago".
- Pluralisation and zero states are handled ("1 member", "No members yet").
- Copy inside the product is short, specific, active and written for the moment. Errors say what happened and what to do next.

## Flows

- Design the flow, not the screen. A task flow has an entry, the input, a review, a named in-progress state, a success state with the next step, and a failure path. A deliverable that shows part of a flow says which steps are missing. When Intent is installed, its journey and fortify skills design the flow and the state inventory, and the rules in this section are the floor.
- In-progress states are named in the interface ("Gathering options", "Confirming your ride") and sit in the container that will hold the result, as a skeleton of the final layout.
- Partial failure stays local: a section that fails shows its own message and retry inside its container, and the rest of the screen keeps working.
- Success is proportional to the stakes: a toast for a small reversible change; a sheet or a full screen with the next step for money, orders and bookings.

## Accessibility (the floor)

- WCAG 2.2 AA minimum for everything that ships.
- Full keyboard operation on web and desktop: visible focus indicators, logical focus order, focus management in dialogs and after actions.
- Screen readers: semantic structure, labelled controls, announced state changes, headings in order.
- Text scaling: layouts survive 200% text on web and the largest accessibility sizes on mobile. Test it, do not assume it: web type is set in rem so it follows the reader's default size, and one screen per flow is shown at 200 percent or at the largest accessibility size.
- Reduced motion settings respected: keep opacity fades, remove movement.
- Colour independence and contrast as above. No flashing content.
- Hit targets as in Components.

## Platform conventions

- iOS: follow the Human Interface Guidelines. Native navigation patterns (push, modal sheet, tab bar), system gestures (back swipe), SF Pro or a brand face with matched metrics, Dynamic Type, haptics only for meaningful confirmations, safe areas, large titles where they fit. From iOS 26 the system's bars, sheets and controls render on Liquid Glass: use the system components and let them bring the material, never put Liquid Glass or imitation glass in the content layer, use it on custom controls only for the most important functional elements, and avoid custom bar backgrounds and tinted bar controls. Never Android patterns on iOS (hamburger menus, snackbars).
- Android: Material 3 behaviour (predictive back, system bars, edge to edge), ripple or an equivalent pressed feedback, the flexible navigation bar or navigation rail, Material spring motion. Brand may override the look, never the behaviour.
- React Native and Expo: native components for inputs, pickers, sheets and navigation wherever possible. Specify what is native and what is custom. Gestures and animations run on the UI thread (Reanimated). Handle the keyboard: avoiding view, safe area, scroll into view.
- Web: responsive from 360px, real breakpoints, URL reflects state (tabs, filters, pagination), links are links and buttons are buttons, native form elements styled rather than rebuilt where possible. The parts the browser draws take the product's tokens: color-scheme, text selection, the caret and accent colour of form controls, focus rings, scrollbars where they show, underline offset and thickness.
- Desktop apps and dense web tools: keyboard shortcuts, a command palette where it fits, resizable panes, layout state that persists.
- Mockups and prototypes: system components (status bar, tab bar, navigation bar, system sheet, keyboard) are drawn as the current OS draws them and named as system components in the notes, never restyled. Their metrics come from the platform's design kit; when the kit is not at hand, say which values are assumed.

## Motion baseline

Defer to Emil Kowalski's skills when installed. Otherwise:

- Movement animates transform and opacity only. Colour, background and border colour may cross-fade as a state effect. Never transition all properties, and never layout properties (width, height, top, left, margin, padding).
- Content is visible without script or animation: an entrance starts from a visible default, never from opacity 0 waiting for a handler. With animation switched off nothing is missing.
- Hover exists only on pointer devices (inside @media (hover: hover)). The hovered element never moves itself or its neighbours: a child carries the movement, and a preview opens after a short delay set on the hover state only, so leaving is immediate.
- UI motion stays under 300ms: micro feedback 100 to 160ms, popovers and menus 150 to 250ms. Sheets and full-screen modals are the exception and may take up to 400ms (iOS push and sheet transitions run about 350ms). Exits are faster than entrances.
- Easing: ease-out for entering and responding, ease-in-out for elements moving on screen, linear only for constant motion. Never ease-in for UI.
- Platform defaults are springs. iOS uses its system springs. Material 3 replaced easing and duration with spring tokens: spatial springs for position, size and shape, effects springs for colour and opacity, each in fast, default and slow. Use Material's standard scheme (minimal bounce) by default; its expressive scheme (overshoot) is a brand decision. Default speed for most motion, fast for small elements (switches, chips), slow for full-screen ones.
- Entrances start at scale 0.9 or higher with opacity, never from scale(0). An exit retraces its entrance: what slid up slides down, what grew from a trigger shrinks back to it.
- Nothing animates on keyboard-driven or very frequent actions, and functional data (amounts, charts, tables) appears in place.
- Press feedback on everything pressable: scale 0.97 or the platform state layer, within 100 to 160ms.
- Popovers originate from their trigger. Sheets and drawers track the finger from the first pixel and can be interrupted. Reversible actions may trigger during a gesture; destructive or committing ones only on release.
- Reduced motion: fades instead of movement.
- Every animation can name its purpose: feedback, spatial continuity, state change or explanation. Decorative motion only in rare or first-time moments, never the same reveal on every section. A loop runs only while it carries live information (loading, recording, live) and stops when hidden. Motion is never the only carrier of information.

## Design tokens and systems

- Three tiers: primitive (colour.blue.600, space.4), semantic (colour.bg.surface, colour.fg.primary, space.inset.md), component (button.bg.primary.hover). UI uses semantic and component tokens, never primitives directly.
- Name by role and intent, not appearance: fg.secondary, not grey.600.
- Every component is documented with anatomy, variants, sizes, states, content rules, accessibility notes, do and don't examples, and token mapping.
- Figma: auto layout throughout, variables for every value, component properties for variants and states, slots for content, layer names that match code names.
- Code: CSS variables or platform token files generated from one source. Light, dark and high-contrast are theme layers over semantic tokens.
- In a code project the system is also written to DESIGN.md at the repo root, in the open DESIGN.md format (tokens in the frontmatter, the identity decisions and the do and don't as prose), so every agent and tool reads one system. It is written after the first build, from what was built, and updated when a decision changes it.
- Extend a system in its own language. Propose additions explicitly ("new token: colour.bg.warning.subtle") instead of hard-coding a value.

## Specification and handoff

A design is finished when an engineer can build it without guessing. When Intent is installed, its specify skill assembles the package and the list below is the visual specification inside it. Specify:

- Layout: grid, spacing as tokens, alignment, responsive behaviour per breakpoint.
- Type and colour as tokens.
- Components: variant, size and state, and any deviation from the system.
- Behaviour: tap, hover, focus, error, timeout and success; loading and empty states; keyboard behaviour.
- Motion: a table with one row per transition: trigger, element, property, duration and easing or spring, origin, reduced-motion fallback. Any prototype with an overlay, a state change or a navigation step carries it.
- Content: real copy, truncation rules, limits.
- Edge cases: 0, 1, many and too many; shortest and longest; offline; permissions denied.

## Anti-patterns (fix on sight)

- Spacing off the 4px grid, mixed row heights, more than 2 alignment edges per region.
- Sizes off the major second scale, more than 7 text sizes in use, 3 or more weights in UI, body text under 14px, large brand-face headlines without tightened tracking.
- Platform metrics ignored (36px buttons on touch, custom heights where a platform value exists) or superseded ones used (redrawn opaque iOS bars or imitation glass on iOS 26 and later, the original 80 Material navigation bar) without a written reason.
- Pure grey neutrals next to a tinted palette, accent used as decoration, meaning carried by colour alone.
- Card inside card; border, shadow and tint on the same element; a thick coloured border on one side of a card or alert; dividers and whitespace doing the same job; bordered media grids; lists built as stacks of cards.
- A mid-grey canvas chosen by default; an accent spread over tab bars, headers, cards and buttons at once; two filled buttons competing on one screen; text on unscrimmed photos.
- Placeholder as the only label, submit disabled before the request, errors that only say "Something went wrong".
- Happy path only, one screen presented as a flow, lorem ipsum, perfectly short fake names, invented testimonials, logos or numbers presented as real.
- Mixed icon families or weights, emoji as icons, icon-only controls without labels.
- Hover states on touch, UI motion over 300ms, ease-in, transitions on all or on layout properties, scale(0) entrances, content that waits for script to become visible, the same reveal on every section.
- Web or Android patterns on iOS and the reverse.
- Raw hex values or primitive tokens in component code, one-off components that duplicate existing ones.

## Self-review before showing anything

Run this list, fix failures first, then run agency-grade-review when it is available.

1. One job, one primary action, nothing that could be removed without loss?
2. All spacing on the 4px grid, rhythm correct, at most 2 alignment edges per region, separation by spacing and hairlines before boxes?
3. Type on the major second scale mapped to platform roles, correct leading and tracking, tabular numbers where needed, one case convention, one hero figure per screen at 2 to 3 times body?
4. Colour roles used, contrast passes in both themes, no colour-only meaning?
5. Every component state and every screen state present, with the chrome following each state, and the flow's steps shown or listed as missing?
6. Real content including long, short, zero and many, with localisation headroom?
7. Hit targets, keyboard, focus, screen reader labels handled, and text scaling shown at 200 percent or the largest accessibility size?
8. Platform conventions respected?
9. Motion durations, easing or springs, interruptibility and reduced motion correct, and the motion table present?
10. Tokens only, system extended in its own language, additions flagged?
11. Spec complete enough to build without guessing?
12. Every value traceable to Material 3, Apple HIG or a written exception?
