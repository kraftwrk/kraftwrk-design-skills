---
name: typography-craft
description: Typography at the level of top product design agencies, for any screen, prototype, design system or document where text is set. Typeface selection and pairing, the major second scale on the 4px rhythm, headline composition, body and UI text, numerals and data, micro-typography, rendering and loading, localisation, type as the brand carrier, and a typography review. Use whenever choosing or pairing typefaces, setting a type scale or text styles, composing headlines or hero figures, laying out reading text, tables or labels, or reviewing typography.
---

# Typography craft

## What this skill is

In the agency work this skill set is built on, typography does most of the identity work and almost all of the hierarchy work. Aesop, Uber, Harrods, Brand New Day and LV are recognisable from their type alone. This skill makes that level of care repeatable: how to choose and pair typefaces, how to set the scale and rhythm, how to compose headlines and hero figures, how to handle numbers, and the small details that separate set type from typed text.

Values come from product-design-foundations (the major second scale mapped to Material 3 and Apple HIG text styles, the 4px grid). The voice comes from product-brand-identity (the type voice catalogue). This skill is the craft between the two.

## The bar

- Hierarchy is readable at a glance from size and spacing alone; weight and colour refine it.
- One typeface family carries the UI; at most one display face joins it for brand moments; a mono only for data or code.
- Every size, line height and tracking value is deliberate and on the scale. Nothing is a tool default.
- Numbers behave: aligned, tabular where they change, with units set small.
- Micro-typography is correct everywhere: quotes, apostrophes, ellipses, spaces, dashes, ligatures, kerning.
- Type is tested where it is read: on a mid-range phone at 14 and 16, in dark mode, at large accessibility sizes, in the longest language.

## Choosing typefaces

- Criteria before taste: a large x-height and open apertures for UI at 14 to 17; a full character set for the markets served (including diacritics, currency symbols, Cyrillic or Greek if needed); tabular and proportional figures; a true italic or none at all; at least regular and medium or semibold that stay distinct at 14; hinting and rendering checked on Windows and Android, not only on a Mac; a variable font where possible; a licence that covers app, web and the expected page views.
- Test with real strings before committing: the longest menu label, a price with a currency, a time, an email address, a name with diacritics, a 3-line headline, a paragraph at 16 with 65 characters per line, and the word "Illinois" (I, l and 1 must differ).
- Pairing: contrast of construction with shared proportions. A display face (serif, slab, condensed, rounded) carries headlines and hero figures; a neutral workhorse carries UI text; their x-heights and widths should sit close enough that 16px body and 16px label look like one system. Never pair two grotesks of similar flavour; never pair more than two families plus an optional mono.
- One family can do everything through size, weight and tracking (Uber, Gatorade, Instacart). Reach for a second face only when the brand idea asks for it (luxury, editorial, heritage, playful).
- Platform defaults are legitimate: SF Pro on iOS and Roboto on Android are tuned for their platforms; a brand face must match or beat them at 14 before it replaces them for UI text.

## Scale and rhythm

- Scale: major second (1.125) from the platform body size, snapped to the platform roles (Material 3 display, headline, title, body, label; iOS Large Title through Caption 2). A product uses 5 to 7 steps. See product-design-foundations for the values.
- Line heights land on the 4px grid: 16/24, 14/20, 20/28, 24/32, 28/36, 32/40, 36/44, 45/52, 57/64. Vertical spacing between text blocks is then a multiple of 4 and the rhythm holds without a baseline grid.
- Leading tightens as size grows: around 1.5 at body, 1.3 at titles, 1.15 at display. Below 1.1 only for a single-line hero figure.
- Tracking: 0 at body; -0.01em at 24 to 32; -0.02em at 36 and above; +0.04 to +0.08em for all caps at 11 to 14; never letter-space lower case.
- Measure: 45 to 75 characters for reading text (max-width around 60 to 65ch at body size); 35 to 50 for captions in narrow columns; headlines break by sense, not by width, at 2 to 3 lines maximum.
- Responsive type on the web: fluid between the compact and expanded values with a clamp (for example a headline from 32 to 48), never scaling below the platform body size; UI text does not scale with the viewport.
- Dynamic Type on iOS and font scaling on Android are designed for, not tolerated: layouts hold at the largest accessibility sizes, with truncation rules written per element.

## Headlines and hero figures

- Composition: size and weight carry the headline; colour and decoration do not. Sentence case unless the voice is caps. A headline at display size with tightened tracking, balanced line breaks and no orphans is the single most visible sign of care.
- Hero figures (balance, ETA, total, score): 2 to 3 times body, tabular lining figures, the unit or currency at label size beside or beneath in secondary colour, the baseline of unit and figure aligned optically. One per screen.
- Mixed sizes in one line are a signature move when controlled: a large time with a small am/pm (Uber), a large amount with a small currency (Brand New Day, STC). The small element sits at body or label size, never at a third arbitrary size.
- Display type over imagery sits on a gradient scrim, bottom-left, with the line length short enough to stay inside the scrim.
- Hanging punctuation and optical margin alignment at display sizes: quotes, bullets and the first letter align to the text edge optically.
- All-caps headlines (condensed voices) get tracking, never faux bold or faux condensed; small caps only if the font has real ones.

## Body and UI text

- Body at 16 (web, Android) or 17 (iOS), regular weight, 1.5 leading, measure 45 to 75; paragraphs separated by one line of space or 8 to 12, not both.
- Secondary text differs by colour first (secondary foreground), size second (one step down), weight never. Tertiary text is for timestamps and meta only.
- Labels, buttons and tabs at 14 to 17 medium; label text never below 11, caps labels never below 11 with +0.04em or more.
- Truncation rules per element: 1-line clamp with an ellipsis for titles in lists, 2-line clamp for cards, middle truncation for file names and addresses, no truncation for amounts and dates.
- Alignment: left for text, right for numbers in columns, centred only for isolated short moments. Label and value pairs share a baseline and one alignment edge.
- Links in running text are underlined or clearly coloured, never only bold. In UI, text buttons are verbs in the accent or foreground colour.
- No justified text in UI. Hyphenation off for UI text, on with limits (two consecutive lines maximum) for long reading on the web.

## Numerals and data

- Tabular lining figures wherever numbers align or change: prices, balances, counters, timers, tables, sports scores, charts. Proportional figures in running text; old-style figures only in editorial reading text if the face has them.
- Decimal alignment in columns; thousands and decimal separators per locale (1.234,56 in Dutch, 1,234.56 in English); negative numbers with a real minus sign, never a hyphen; percentages and units with a non-breaking space where the locale requires it.
- Currency: code or symbol per locale and product convention, set at label size beside a hero figure, at the same size inside tables.
- Monospaced or tabular setting for codes, IDs, IBANs and one-time passcodes, grouped in fours.
- Time and dates: locale-formatted, relative for the recent past and absolute after about a week, never "340 days ago".
- Charts inherit the type system: axis labels at label size in secondary colour, values tabular, titles at title size.

## Micro-typography

- Real quotation marks and apostrophes per language, a real ellipsis character, a real multiplication sign (×) and minus (−), prime marks for feet and inches, no straight quotes anywhere in shipped UI.
- Non-breaking spaces between a number and its unit, inside shortcut names, after short words in headlines where the language calls for it, and in brand names that must not break.
- Ranges and pauses in UI copy are written with words ("9 to 17", "from 12 to 18") or a short dash per the product's copy rules; the product's punctuation rules are written down once and applied everywhere.
- Ligatures on for display and reading text, off for code and IDs; contextual kerning on; optical kerning for display sizes when the font's own kerning is weak.
- Balanced headlines (text-wrap: balance) and pretty paragraphs (text-wrap: pretty) on the web; manual breaks in native where a headline would orphan a word.
- Icons sit on the text baseline optically, sized to the x-height plus ascenders (Material 20 or 24, SF Symbols scaled to the text style).

## Rendering, loading and dark mode

- Web: preload the primary font files, subset to the languages served, font-display swap with a size-adjusted fallback so layout does not shift, variable fonts over many static files, woff2 only.
- Check rendering at 14 and 16 on Windows (ClearType) and mid-range Android as well as macOS; a face that only looks good on a Retina Mac is not a UI face.
- Dark mode: light text on dark reads heavier; use the same weight and reduce tracking slightly or step the weight down for display sizes; secondary text at 60 percent white, not a lighter weight.
- Minimum sizes: 11 for captions and caps labels, 12 for labels, 14 for anything the user must read, 16 or 17 for body.

## Localisation and accessibility

- Text can grow 30 to 40 percent in German, Dutch, French and Finnish; headlines and buttons are designed for the longest language, not the English draft.
- Scripts with different metrics (CJK, Arabic, Devanagari) need fallbacks with matched x-height and line heights that still land on the grid; RTL mirrors layout, not glyphs.
- WCAG 2.2: 4.5:1 for text under 24, 3:1 at 24 and above; 1.5 line height for reading text; no all-caps paragraphs; text scalable to 200 percent on the web and the largest accessibility sizes on mobile without loss of content.

## Type as the brand carrier

- Pick the type voice from the catalogue in product-brand-identity and push it: the display face only in brand moments, the workhorse everywhere else, the hero figure as the loudest typographic moment on any screen.
- Signature moves seen in agency work: a huge light amount on a gradient canvas (Brand New Day); a bold grotesk headline bottom-left over a fading photograph (Gatorade); a serif with italic as the only decoration in a luxury store (Harrods); widely tracked geometric caps as the whole chrome (LV); condensed caps on every label (Joe & The Juice); type as image, a diagonal repeated word as a pattern (Gatorade Highlights).
- Two products can share a typeface and feel completely different through scale contrast, case, tracking, weight and measure. Decide those five before choosing a second face.

## Typography review

Run on any screen or system, report findings with values:

1. Scale: every size on the major second scale and mapped to a platform role? No more than 7 steps in use?
2. Rhythm: every line height a multiple of 4? Spacing between text blocks on the 4px grid?
3. Hierarchy: readable in greyscale from size and spacing alone? One hero figure per screen?
4. Families: at most one workhorse, one display face, one mono? Pairing contrasts in construction and matches in proportion?
5. Headlines: tracking tightened at display sizes, balanced breaks, no orphans, 2 to 3 lines maximum, sentence case unless the voice is caps?
6. Body: measure 45 to 75, leading 1.5, secondary text by colour not weight, no justified text?
7. Numbers: tabular where they align or change, decimals aligned, locale separators, real minus signs, units at label size?
8. Micro-typography: real quotes, apostrophes, ellipsis, non-breaking spaces, ligatures on for text and off for code?
9. Truncation and localisation: a rule per element, the longest language checked, Dynamic Type and font scaling survived?
10. Rendering: loading strategy with matched fallback, checked at 14 on Windows and Android, dark mode weight considered?
11. Accessibility: contrast ratios measured, minimum sizes respected, 200 percent scaling survived?
12. Voice: does the type alone say which product this is?

## Anti-patterns

- Default fonts at default sizes with default line heights; a sixth and seventh size introduced for one screen.
- Three families; two similar grotesks; a display face used for UI labels.
- Headlines at display size with 0 tracking and an orphan on the last line; centred multi-line headlines over a photograph without a scrim.
- Proportional figures in a table; prices that jump as they update; a hyphen as a minus sign; straight quotes.
- Secondary text made light weight instead of secondary colour; grey text at 40 percent that fails contrast.
- Letter-spaced lower case; faux bold; faux italic; faux small caps.
- Text that scales with the viewport at body size; layouts that break at the first accessibility size.
- A brand face loaded as six static files with layout shift on every page.
