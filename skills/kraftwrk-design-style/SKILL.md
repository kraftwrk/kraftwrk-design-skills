---
name: kraftwrk-design-style
description: Marc Luijkx's (Kraftwrk Studio) personal design signature, applied on top of product-design-foundations, typography-craft, product-ui-patterns, product-brand-identity and the client's design system. Use for any UI, screen, component, prototype, mockup, design direction or critique Marc asks for.
---

# Kraftwrk design style

Marc's signature: what stays the same across every client while design systems change. This skill assumes product-design-foundations (the technical baseline), typography-craft, product-ui-patterns (the pattern library), product-brand-identity (identity work), agency-grade-review (the gate) and design-decision-log (the learning loop) are available and does not repeat them. Where the client system or the foundations leave several acceptable options, this skill decides.

## Stack

The order and who owns what are in product-design-foundations (How skills stack). In short: Intent for context, flows, words and handoff when it is installed; the client design system for the vocabulary; the foundations, typography-craft, product-ui-patterns and product-brand-identity for the work; this skill for the signature; agency-grade-review as the gate before anything is shown; design-decision-log at the end of every design session; Emil Kowalski's skills for motion when installed.

If the foundation skills are not installed, say so once and apply the usual industry baseline (Apple HIG, Material 3, WCAG 2.2 AA, full component and screen states, design tokens) before applying this signature.

## The signature

1. Subtraction first. Every element earns its place. Before adding, ask what can be removed. One primary action per screen.
2. Hierarchy through type and space, not decoration. Size, weight, spacing and alignment do the work. Boxes, borders, shadows and colour are the last resort.
3. Swiss discipline. Strong grid, few alignment edges, deliberate whitespace, restrained palette, typography as the main visual material, objectivity over ornament.
4. Systems thinking. Anything used twice is a pattern with variants and states, never a one-off.
5. Motion as craft. Fast, interruptible, physically plausible, and always explaining a change. Delight lives in small details (press feedback, a well-timed stagger), never in spectacle.
6. Production-ready. An engineer can build it without guessing.

## Default choices (when the brief or client system leaves them open)

- Left-aligned, with few alignment edges. Centre only isolated moments.
- Neutral-first palette with one accent. Colour always means something (action, selection, status, focus).
- Two weights. Hierarchy by size and space before weight, and by weight before colour.
- Sentence case.
- Tight, confident headline tracking, generous but deliberate whitespace, an editorial rhythm.
- Separation by spacing and hairlines before tints, tints before borders, borders before shadows, never all of them.
- Canvas chosen on purpose per product (cream, near-black or white), never mid-grey; one hero figure per screen.
- Dark neutral palettes done properly (Linear-like restraint) when the product suits them.
- Density matched to the job, never cluttered.
- Press feedback on everything pressable; sheets and gestures track the finger.

## Taste reference points (take the principle, never copy the look)

- Linear (app and marketing site): restraint, precise typography, dark neutral palettes, subtle detail, speed as a feeling.
- Rauno Freiberg: interaction details and micro-interactions that feel inevitable; craft in the smallest components.
- Emil Kowalski: motion that is fast, interruptible and purposeful; gesture-driven sheets and toasts.
- Basement Studio: bold, confident moments and technical craft, used sparingly in marketing or showcase contexts.
- Swiss design tradition: grid, typographic hierarchy, objectivity, white space.

## Never (Marc's list, on top of the foundations' anti-patterns)

- Purple or rainbow gradients, glassmorphism or glow effects as defaults.
- Emoji as icons. Card soup. Everything centred. A hero with a vague headline and two buttons.
- Bouncy overshoot, slow fades, decorative motion.
- Generic AI copy ("Unlock your potential", "Seamlessly", "Elevate"), and manufactured contrast ("Not a tool. A partner.") more than once on a page.
- The reflexes of generated work listed in agency-grade-review (visual tells), unless the brief gives the reason.
- Em dashes anywhere, in UI copy or in text written for Marc.

## Working with Marc

- Before designing: confirm the job, user, primary action, platform and design system in one line each. Ask once if something is unclear and decisive; otherwise state the assumption.
- Design order: structure and hierarchy, then layout, type, colour, motion. Decoration last, if at all.
- Present: the work, then a short rationale (key decisions and trade-offs), open questions, and proposed design system additions. Keep it brief. For case studies and client decks, follow the presentation conventions in agency-grade-review: flat frames on a flat field in rows, one angled hero at most, component close-ups, dense screens included.
- Steering words: a one-word steer changes only the element or screen Marc named and adds no new colour, face, radius or effect. Bolder: push the carrier the identity already pushes (size, canvas, device) further on that element and quiet what surrounds it. Quieter: remove before reducing; decoration first, then the accent, then one step of weight or size. Tighter and looser: one step on the 4px grid inside the named group, rhythm rule intact. Simpler: remove elements until the remove-one test fails. Polish: no redesign; alignment, rhythm, states, copy and finish only. Harden: worst-case data, every state, the longest language, text at 200 percent. A steer that cannot be done inside the system gets one question naming the addition it needs.
- Corrections become rules. When Marc corrects, overrides or chooses something, run design-decision-log: project-specific decisions go to the project's decision record, general ones are proposed as rules for this skill (taste), the foundations (values), the patterns, the brand skill or the review skill, each with its reason in Marc's words. Run the end-of-session capture before closing any design session.

## Output expectations

- HTML and React prototypes: semantic markup, real interactive states, CSS variables for every value, motion per Emil's skills or the foundations baseline, reduced motion handled, and the prototype switches listed in agency-grade-review.
- Figma: auto layout throughout, variables, component properties for variants and states, layer names matching code names.
- Specs for engineering: states, spacing as tokens, motion values (duration, easing or spring), behaviour and edge cases written out.

## Fallback defaults (only when no client system exists)

- The 4px grid with 8 steps for layout, as in the foundations.
- One neo-grotesk (Inter, Geist or similar) on the major second scale, 5 to 6 steps in use, mapped to the platform text styles. This is the workhorse of a product without an identity brief; in identity work the face is chosen with its reason in product-brand-identity.
- Neutral ramp tinted to the brand hue, one accent, the standard semantic set.
- Small, consistent radii from the Material shape scale (4 or 8) and at most one subtle elevation style.
