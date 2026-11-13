---
name: product-brand-identity
description: Give a digital product a bespoke identity, or translate an existing brand into product UI, the way Work & Co, MetaLab, Clay, Fantasy and AKQA do. Covers the brand idea, typography pairing, colour stance, shape language, iconography, imagery and illustration, motion signature, voice and tone, brand moments, and turning identity into tokens and component rules. Use when a product needs a visual identity or direction, when a brand has to show up in UI, when work looks generic or like every other SaaS product, or when reviewing whether a product feels like itself.
---

# Product brand identity

## What this skill is

Product branding: the bespoke identity of a digital product, designed together with the product. It is not corporate identity consultancy (positioning decks, logo systems for a holding company). The output is a product that is unmistakably itself on every screen while staying fully usable.

This skill works on top of product-design-foundations (the technical floor) and is checked by agency-grade-review. Where the client already has a brand, this skill translates it; where the product is new, this skill creates the identity.

## What the agencies do that this skill encodes

Drawn from their published work and writing. Take the principle, never copy the look.

- MetaLab (Slack, Suno, Clockwise, PlayerZero): brand, product and marketing site designed as one effort. Personality carried by colour, copy and interaction, in categories that are usually grey. Every line of copy, including loading and error states, treated as a brand moment.
- Work & Co (Aesop, Virgin America, Apple, IKEA, Mailchimp): an "ownable digital brand" that serves the product's one job. Brand expressed through typography, layout and restraint; the core flow is never sacrificed to the brand.
- Clay (Eden, Snapchat, Coinbase): identity systems built on type pairings rather than decoration, palettes derived from one concept, and type that carries the brand into the app without competing with the content.
- Fantasy (Vimeo): brand as product infrastructure. A modular system where a few brand principles drive the logo, tone of voice and design system at once, so marketing and product share one expression.
- AKQA (Louis Vuitton app, Nike): craft and atmosphere translated to screen through editorial imagery, cinematic motion and production guidelines that say exactly how things appear.
- Framna (PostNord, Swish): Nordic functional clarity. Brand expressed through trust, simplicity and motion that explains (showing a parcel's size before delivery).
- Wolff Olins (EE, Uber): identity as a behaving system built around an idea rather than a wordmark. Coherent rather than consistent, and able to disappear when it is in the way.

## Principles

1. Brand and product are one design. Decide identity and interface together. Never skin a finished UI.
2. One brand idea drives every carrier. If the idea cannot be said in one sentence, the identity will fragment.
3. Distinctive through few decisive choices: one signature typeface or pairing, one colour stance, one shape language, one motion signature. Everything else stays quiet. Three bold choices with discipline beat ten half-choices.
4. Coherent, not uniform. The product feels like one author across surfaces, with brand intensity varying by moment.
5. Brand serves the job. Where the user works (forms, tables, settings, payment), brand steps back into typography, spacing and tone. Where the user pauses (onboarding, empty states, success, app icon, marketing), brand steps forward.
6. Break one category convention on purpose and keep the rest. Users must recognise the category; the brand must be recognisable within it.
7. Identity has to survive production: screen-tested type, contrast-safe colour, token-ready values, motion that holds 60fps on a mid-range Android phone.

## Process

### 1. Brand brief (one page, before any visuals)

- Product job and audience, one line each.
- Brand idea: one sentence, the organising thought. Examples of the form: "a calm desk for chaotic money", "a confetti cannon in a grey office", "a Nordic post office that shows you the parcel".
- Personality: 3 attributes plus 1 tension. Each attribute gets a "this, not that" line (warm, not cute; precise, not cold). The tension is what makes it specific (playful but never silly).
- Category conventions: list 5. Mark the one you will break and why. Keep the other 4.
- References: 5 to 8, each with one sentence on what to take from it. Never "make it like X".
- Constraints: existing brand assets, platforms, accessibility, markets and languages, tech stack, imagery budget.

### 2. Directions (2 or 3, deliberately different)

Each direction contains: type choice, colour stance, shape language, one hero screen, one dense working screen, the app icon or logo lockup, and 3 lines of copy in its voice. Name each direction after its idea, not after its look. Judge directions on the dense screen as much as on the hero; a direction that only works on the hero is a poster, not a product identity.

### 3. System

Turn the chosen direction into the carriers below, then into tokens (primitive and semantic, light and dark) and component expression rules. Document do and don't with real screens.

### 4. Apply and test

Apply across the key flows, including the ugly ones (settings, errors, long lists). Run the review tests at the end of this file. Fix, then document.

## Brand carriers in a product

### Typography (the primary carrier)

- Choose for character and performance: full character set for the markets served, tabular figures, good rendering at 14px, variable weights, a licence that covers app and web.
- Pairing strategies: (a) one versatile grotesk doing everything through size and weight; (b) an expressive display face (serif, slab, geometric, humanist) for headlines plus a neutral workhorse for UI; (c) a mono accent for data-heavy or technical products. Never more than 2 families plus an optional mono.
- The display face appears only at display sizes and in brand moments. UI text always uses the workhorse.
- Define the typographic voice beyond the font name: size contrast (dramatic or even), case convention, tracking, leading feel, alignment habit. Two products can share a typeface and feel completely different through these.

### Colour (the stance)

- Pick one stance per product: neutral canvas plus one accent; saturated brand colour as canvas; dark-first with luminous accents; warm paper-like palette; duotone.
- Derive the whole system from the brand hues: tinted neutrals, the accent scale, and semantic colours harmonised with the brand (a brand red and an error red must not clash, so one of them moves).
- Write the signature colour rule: exactly where the accent appears (primary action, selection, focus, one brand surface) and where it never appears.
- Fix contrast at system level: create UI-safe variants of brand colours (text-safe, surface-safe) and document that the marketing hex and the UI token differ on purpose.
- Light and dark are both designed from the brand, never inverted.

### Shape and surface

- Radius language: sharp (0 to 4), soft (8 to 12) or round (16 and up, pills). One value per component tier (controls, containers, media) with consistent ratios between tiers.
- Separation method: pick the primary one (spacing and tints, borders, or shadows) and use the others sparingly.
- Density and whitespace are brand too: generous and editorial, or compact and tool-like. Decide, then keep it.

### Iconography

- One family whose stroke and geometry match the typeface (icon stroke weight visually equals text stroke weight at the same size). Custom icons only for the 5 to 10 brand-specific objects; everything else from one consistent set.
- Decide outline or filled, corner style and optical sizes. The app icon follows the same geometry.

### Imagery, illustration and 3D

- Decide the one approach: photography (with art direction rules for light, crop, colour treatment, people versus objects), illustration (style, line, palette subset, level of abstraction), 3D (materials, lighting, camera) or none (type-led).
- Write the art direction as rules someone else can follow and brief an artist or a generative tool with.
- Imagery never competes with content. In product UI it lives in brand moments; in commerce the product imagery is the hero and the brand recedes around it.

### Motion signature

- Define three things: the easing family (crisp, fluid or springy), the base durations, and one signature move that recurs (a reveal, a morph, a stagger, a transition).
- Motion still obeys the product baseline: UI motion under 300ms, interruptible, purposeful. Brand sets the character; it never buys slowness.
- Launch moment: a short launch animation (under 1 second) that resolves into the first screen. The same idea reappears, smaller, in loading and success states.
- When Emil Kowalski's skills are installed, use them to build and review the motion.

### Sound and haptics (mobile)

- Haptics for meaningful confirmations only, mapped to a small vocabulary (success, warning, selection). Sound off by default unless it is core to the product.

### Voice and tone

- Voice: the 3 attributes written as rules with examples per surface: button labels, empty states, errors, notifications, onboarding, marketing. Include a "never say" list.
- Tone shifts by moment: warmest in onboarding and success, plainest in errors, money and permissions.
- Personality lives in the small moments (empty states, confirmations, loading copy), not in every label.

### Logo and lockups in product

- The logo appears in the app icon, launch screen, about and auth screens, and marketing. It does not sit in every screen header unless the platform convention expects it (web top-left home link).
- Never stretch brand elements into UI decoration: logo shapes as backgrounds, brand pattern on every surface, mascots in forms.

## Brand moments map

For every product, mark where brand is loud, medium or quiet:

- Loud: app icon, launch, onboarding, first empty state, major success, marketing site, notification tone.
- Medium: navigation, home, dashboards, cards, section headers.
- Quiet: forms, tables, settings, payment and checkout, errors, dense data, permissions.

Rule: a user working in a quiet zone should be able to forget the brand and still feel it in the type, spacing and tone.

## Translating an existing corporate brand into product

- Keep: the idea, the type family (or its licensed screen companion), the primary hues, the voice.
- Adapt: UI-safe colour variants, a UI type scale, an icon set matched to the type, motion character, component expression. Document each adaptation and why.
- Protect: the usability floor from product-design-foundations. If a brand colour fails contrast as text, it becomes a surface or accent colour instead, and this is proposed to the brand owner with the measured ratios.
- Extend: most brand guidelines have no rules for product. Write the product brand sheet and offer it back as an addition to the guidelines.

## Deliverables

- Product brand sheet (1 to 2 pages): idea, attributes, type, colour stance, shape, icons, imagery, motion signature, voice, brand moments map.
- Tokens derived from the brand (primitive and semantic), light and dark.
- Component expression rules: how buttons, inputs, cards, navigation and empty states express the brand.
- Motion signature spec: easing, durations, the signature move, launch animation.
- Voice guide with examples per surface.
- Do and don't gallery on real screens.
- Production asset list: icon set, illustration kit, app icon variants, imagery treatments.

## Anti-patterns

- Brand as decoration: logo everywhere, brand colour on every element, brand pattern behind content.
- Identity that is only a logo: swap the logo and nothing changes.
- Trend as identity: default purple gradients, glassmorphism, 3D blobs, grainy gradients, "AI aesthetic" glows. A trend is allowed only as the deliberate convention-break, and only if it will age acceptably.
- Generic SaaS as identity: Inter, blue 600, 8px radius, cards with 1px borders, hero plus three feature tiles. Acceptable as a baseline, never as an identity.
- Too many choices: 3 typefaces, 4 accents, mixed radii, mixed icon sets.
- Loud brand in quiet zones: illustrations inside forms, animated logos in checkout, jokes in error states.
- Voice that changes personality between screens.
- Imagery from a different universe than the UI (stock photos next to geometric illustration).
- Marketing hex values used as UI text colours despite failing contrast.

## Review: does the product feel like itself?

- Swap test: replace the logo with a competitor's. If the screens still look right, there is no identity.
- Squint test: blurred, is the hierarchy still clear and the colour stance recognisable?
- One-author test: put 6 screens side by side (hero, list, form, empty, error, settings). Same type voice, spacing, radius, icon stroke and tone?
- Category test: show a dense screen to someone unfamiliar. Can they name the category in 3 seconds and two of the brand attributes in 10?
- Moments test: are loud moments actually loud and quiet zones actually quiet?
- Production test: contrast passes, fonts load with matched fallbacks, motion runs on a mid-range Android device, dark mode designed.
- Idea test: can every major choice be traced to the brand idea in one sentence?

When reviewing, output a table with Finding, Where, Why it matters and Fix, ordered by impact.
