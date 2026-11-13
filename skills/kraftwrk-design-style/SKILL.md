---
name: kraftwrk-design-style
description: Marc Luijkx's (Kraftwrk Studio) personal design signature, applied on top of product-design-foundations, product-brand-identity and the client's design system. Use for any UI, screen, component, prototype, mockup, design direction or critique Marc asks for.
---

# Kraftwrk design style

Marc's signature: what stays the same across every client while design systems change. This skill assumes product-design-foundations (the technical baseline), product-brand-identity (identity work) and agency-grade-review (the gate) are available and does not repeat them. Where the client system or the foundations leave several acceptable options, this skill decides.

## Stack

1. Client design system: the vocabulary. Wins on token values and components.
2. product-design-foundations: the baseline.
3. product-brand-identity: the product's identity.
4. kraftwrk-design-style: the signature (this skill).
5. agency-grade-review: the gate, run before showing anything.

Motion: Emil Kowalski's skills (emil-design-eng, animate, animate-expo, review-animations, choreograph, gestures) when installed; otherwise the motion baseline in the foundations.

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
- Separation by spacing and subtle tints before borders, borders before shadows, never all three.
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
- Generic AI copy ("Unlock your potential", "Seamlessly", "Elevate").
- Em dashes anywhere, in UI copy or in text written for Marc.

## Working with Marc

- Before designing: confirm the job, user, primary action, platform and design system in one line each. Ask once if something is unclear and decisive; otherwise state the assumption.
- Design order: structure and hierarchy, then layout, type, colour, motion. Decoration last, if at all.
- Present: the work, then a short rationale (key decisions and trade-offs), open questions, and proposed design system additions. Keep it brief.
- Corrections become rules. When Marc corrects something, propose adding it to this skill (taste) or to the relevant foundation skill (baseline) as a rule with its reason, in one line.

## Output expectations

- HTML and React prototypes: semantic markup, real interactive states, CSS variables for every value, motion per Emil's skills or the foundations baseline, reduced motion handled.
- Figma: auto layout throughout, variables, component properties for variants and states, layer names matching code names.
- Specs for engineering: states, spacing as tokens, motion values (duration, easing or spring), behaviour and edge cases written out.

## Fallback defaults (only when no client system exists)

- 4pt base spacing, mostly multiples of 8.
- One neo-grotesk (Inter, Geist or similar) with a 5 to 6 step type scale.
- Neutral ramp tinted to the brand hue, one accent, the standard semantic set.
- Small, consistent radii and at most one subtle elevation style.
