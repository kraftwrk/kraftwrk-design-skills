---
name: product-ui-patterns
description: Pattern library for product UI, distilled from the screens of Work & Co, MetaLab, Clay, Fantasy, AKQA, Framna and Wolff Olins and sized to Material Design 3 and Apple HIG. Each pattern has an intent, anatomy, values, variants and things to avoid. Use when composing any screen, flow or component (home, list, detail, checkout, onboarding, dashboard, media grid, sheet, tab bar), when asked for the right pattern for a job, or when reviewing whether a screen uses a known pattern well.
---

# Product UI patterns

## What this skill is

The screen and component patterns that agency-grade product work keeps reusing, written so they can be applied and checked. Each pattern names its intent, its anatomy, its values on the Material 3 and Apple HIG metrics, its variants, what to avoid, and where it was observed. Patterns implement the baseline in product-design-foundations, the type rules in typography-craft and the identity decisions in product-brand-identity; they do not replace any of them.

How to use: name the job of the screen, pick the pattern that does that job, apply its anatomy with the product's tokens, then adapt only where the product's identity decisions say so. A screen that needs no known pattern is rare; say so explicitly when it happens.

## Guidelines the patterns share

1. One job per screen, one hero element, one primary action.
2. Canvas, accent, type voice and radius are decided once per product (product-brand-identity) and every pattern inherits them.
3. Separation by spacing and hairlines; cards only when single-purpose; media grids without borders.
4. Platform metrics first (Material 3, Apple HIG), custom values only with a written reason.
5. Brand loud in launch, onboarding and success patterns; quiet in list, table, cart and settings patterns.
6. Real content in every pattern: long names, zero and many, the worst case.
7. Every pattern ships with its states: empty, loading, error, selected, disabled.

## Screen patterns

### 1. Hero figure screen

- Intent: show the one number or fact the user came for, instantly.
- Anatomy: eyebrow label (secondary, 13 to 15), the figure (32 to 36 on mobile; Material headline large or display small, iOS Large Title), unit or currency small beside it, one or two supporting stats, one primary action, everything else quiet.
- Values: figure at 2 to 3 times body; tabular figures; figure and label share a left edge; 24 to 32 of space around the figure.
- Variants: light weight for calm (finance, wellbeing); bold for performance (sport, gaming); gradient text only as a success moment.
- Avoid: two competing figures; a chart above the figure; the accent on the figure in working screens.
- Seen in: Uber (ETA), STC Bank (balance), Brand New Day (amount), Gatorade (program progress), Aesop (cart subtotal).

### 2. Brand canvas screen (launch, login, onboarding)

- Intent: the brand moment where identity is loudest.
- Anatomy: full brand colour or gradient canvas, wordmark top-centre or top-left, one line of brand copy, one primary action (white, black or translucent per canvas), legal or secondary links small.
- Values: primary action 48 to 56 high, full width, pinned above the safe area; copy at title size; nothing else on the screen.
- Variants: photography with a gradient scrim instead of a flat colour; a short launch animation under 1 second that resolves into this screen.
- Avoid: forms on the brand canvas beyond one or two fields; illustration and copy competing; dark text on a saturated canvas that fails contrast.
- Seen in: Brand New Day (login), Gatorade (device connected), Penny (assistant home), Headspace (web hero).

### 3. Monochrome working screen (cart, table, settings, library)

- Intent: the user is working; the brand steps back into type, spacing and tone.
- Anatomy: canvas, text in two or three greys, hairline rows, numbers right-aligned and tabular, one text link or one primary action, no accent fills.
- Values: rows 56 (one line) or 72 (two lines) on Material, 44 minimum on iOS; hairline per platform separator token; totals as a hero figure at the bottom.
- Variants: dark panel for a cart drawer on a cream product; grouped inset lists on iOS.
- Avoid: illustration, brand pattern, coloured headers, cards per row.
- Seen in: Aesop (cart), Brand New Day (portfolio), Epic (library and browse), LV (catalog).

### 4. Editorial product page (commerce, desktop and tablet)

- Intent: sell one object with the calm of a magazine.
- Anatomy: two-column split; product image left (or a gallery), right column with name at title size, a short description, label and value rows separated by hairlines (size, finish, ingredients), one full-width primary action; below, alternating image and text blocks.
- Values: 12-column grid, 24 margins, reading column 560 to 720; label and value rows 48 high; primary action 48 to 56.
- Variants: mobile stacks the columns with the image full-bleed and the action pinned; luxury removes the accent entirely.
- Avoid: tabs that hide the facts; badges and urgency labels; a second filled button.
- Seen in: Aesop, Harrods, LV.

### 5. Immersive media screen

- Intent: the content is the hero; chrome is minimal.
- Anatomy: full-bleed image or video, gradient scrim fading into the canvas, headline bottom-left at headline size, one line of meta, one primary action, text-only or icon-only controls on the image.
- Values: scrim long enough that text meets 4.5:1; headline 24 to 32 with tightened tracking; controls at 44 minimum targets.
- Variants: a card rail at the bottom (TV); a product panel overlapping the image (fashion); a camera feed instead of an image (AR).
- Avoid: a solid bar behind the text; the accent on the image; more than three controls over the image.
- Seen in: Gatorade (program), Fubo (featured event), LV (campaign), Harrods (new season).

### 6. Camera-first overlay (AR, scan, capture)

- Intent: keep the camera feed clean while offering one decision.
- Anatomy: feed fills the screen; product or subject name centred at title size with a price or meta line; two pills (filled primary, translucent secondary); variant thumbnails above; a carousel of circular options at the bottom.
- Values: pills 48 high; thumbnails 40 to 48 with 8 to 12 radius; carousel items 56 to 64 circles.
- Avoid: a tab bar competing with the carousel; text without a scrim; more than one filled pill.
- Seen in: Snapchat (try-on), Gatorade (Highlights capture).

### 7. Ten-foot screen (TV)

- Intent: readable from the sofa, navigable with a remote.
- Anatomy: eyebrow label, large uppercase or bold title with logos, a horizontal card rail of 16:9 tiles, focus shown as a fill with the accent (never only an outline), a section label in small caps, a date or filter rail on one side.
- Values: title 48 to 57 on a 1080p canvas; tiles 16:9 with 24 gaps; focus scale no more than 1.05; dark charcoal canvas, one accent for live and focus.
- Avoid: hover-only states; small text under 24; more than one accent.
- Seen in: Fubo.

### 8. Dashboard home (summary plus entry points)

- Intent: orient, then route.
- Anatomy: minimal header (greeting or name, two icon buttons), segmented pill tabs or chips to switch context, a hero figure card, a short list of recent items with a "See all" text link, a row of entry points with icons and labels, tab bar.
- Values: card radius from the product's logic (16 to 28 soft, 8 to 12 friendly); entry points 56 to 64 wide; page dots when cards page horizontally.
- Avoid: more than one hero card; charts without a question they answer; coloured headers.
- Seen in: STC Bank (home), Brand New Day (investing), Uber (ride status sheet).

## Component patterns

### 9. Hairline list row

- Anatomy: optional leading avatar or icon (40), title at body size, subtitle at 14 or 15 in secondary, trailing value, chevron or a small grey pill; hairline separator inset to the text edge.
- Values: 56 one line, 72 two lines (Material); 44 minimum (iOS); 16 horizontal padding; title and subtitle 2 to 4 apart.
- Variants: transaction row (avatar, name, type; amount right in tabular figures with relative time beneath); selection row (checkmark or radio trailing); navigation row (chevron).
- Avoid: cards per row; two chevrons; coloured row backgrounds.
- Seen in: Uber, STC Bank, Aesop (cart), Brand New Day (portfolio).

### 10. Stat card

- Anatomy: header row with a small icon, label and chevron; one value at 24 to 32; one caption; nothing else.
- Values: padding 16 to 20; radius from the product's logic; frosted or tinted surface on a gradient canvas, surface container on a plain canvas.
- Variants: two values side by side with captions; sparkline under the value only when trend is the point.
- Avoid: three or more values; a button inside; icons that repeat the label.
- Seen in: Brand New Day, STC Bank (web), Penny (hotel cards).

### 11. Drag-handle sheet

- Anatomy: drag handle (Material 32x4, iOS 36x5), top radius (Material extra large 28 or the product's large value), optional title row, hairline rows or content, one primary action, dismiss by drag or close button.
- Values: detents at a half and a full height; content inset 16 to 24; scrim behind at 32 to 40 percent black.
- Variants: map sheet (status and destination rows over a map); action sheet (list of actions); form sheet (one or two fields).
- Avoid: tabs inside a sheet; two filled buttons; a sheet that cannot be dragged.
- Seen in: Uber, Brand New Day.

### 12. Bottom primary action

- Anatomy: one full-width button pinned above the safe area, label as a verb naming the result, optional helper line above it (price, count), secondaries as text links or grey pills above.
- Values: 48 to 56 high; 16 side margins or full bleed; pill or bar per radius logic; disabled at 38 percent only when truly unavailable.
- Avoid: two filled buttons; floating action buttons by default; a bar that covers list content without a scrim or inset.
- Seen in: Gatorade, Aesop, STC Bank, Brand New Day, Snapchat.

### 13. Borderless media grid

- Anatomy: tiles at a fixed aspect (3:4 portrait for games and products, 16:9 for video, 1:1 for photos), 2 columns compact and 4 expanded, metadata under each tile in two lines (title at body, secondary in grey), price or status right-aligned or on its own line, a small filled badge for discount or live.
- Values: gap 12 or 16; tile radius 4 to 8 (or 0 for editorial); badge 11 to 12 medium in a 4 radius rectangle.
- Variants: horizontal rail with a section title and "See all"; ranked rail with large numerals overlapping the tiles.
- Avoid: borders or shadows on tiles; metadata inside the image; mixed aspect ratios in one grid.
- Seen in: Epic Games, Fubo, NPO Zapp, Uber Eats.

### 14. Category chip set

- Anatomy: a wrapping row of pills, each with a short label, optionally a small coloured icon disc or emoji-like glyph; one colour per category when categories are the information, neutral otherwise; selected state filled.
- Values: chips 32 high (Material), 8 gap, 12 to 16 horizontal padding, label 14 medium.
- Variants: filter chips (multi-select with a check); choice chips (single select); category tiles (larger, with illustration) for onboarding.
- Avoid: more than eight colours; chips that wrap to three rows (use a sheet instead); chips as the only navigation.
- Seen in: Headspace, STC Bank, Penny.

### 15. Segmented tabs

- Anatomy: two to four labels in a row; selected shown as a filled dark pill or as an underline with the label in primary colour; unselected in secondary.
- Values: 40 to 48 high; label 14 to 16 medium; underline 2 thick in the accent or foreground.
- Avoid: five or more segments; segments that scroll; icons without labels.
- Seen in: STC Bank (pill), Brand New Day (underline), Joe & The Juice (underline).

### 16. Minimal header

- Anatomy: title or wordmark left (or centred on iOS), up to two icon buttons right (search, notifications), optional back button left; no hamburger in native apps.
- Values: iOS navigation bar 44, large title 34 collapsing to 17; Material top app bar 64, title 22; icon buttons 44 to 48 targets.
- Variants: transparent over imagery with a scrim; search field as the header on browse screens.
- Avoid: logos on every screen; three or more icons; a title that duplicates the tab label.
- Seen in: all 18 case studies.

### 17. Tab bar

- Anatomy: 3 to 5 destinations, icon plus label or icons only with accessible names, active state by colour (or a glow on dark entertainment products), no badge unless it counts something.
- Values: iOS 49 with 10 labels; Material 80 with 12 labels (rail from medium width); icons 24.
- Avoid: a centre action button by default; 6 destinations; labels in Title Case when the product uses sentence case.
- Seen in: Gatorade (4, uppercase labels), STC Bank (5), Snapchat (5), NPO Zapp (3, icons only), LV (text only).

### 18. Status tag and badge

- Anatomy: a small rectangle or pill with 11 to 12 medium text, filled with the accent for live, new or discount, neutral tint for everything else; placed top-left on tiles or inline before a price.
- Values: 20 to 24 high, 4 to 6 horizontal padding, radius 4 (or pill for friendly products).
- Avoid: more than one filled badge per tile; badges as decoration; red for anything that is not an error or a countdown.
- Seen in: Epic (discount), Fubo (live), NPO Zapp (tip), Snapchat (try-on).

### 19. Product panel over imagery

- Anatomy: a small white (or black) panel overlapping the lower part of an image: thumbnail, product name at 14 to 16, price, an underlined text link or a small arrow; a bookmark icon top-right.
- Values: panel 72 to 96 high, 16 padding, radius 0 to 8 per logic, no shadow (a hairline if the image is light).
- Avoid: a filled button inside the panel; two products per panel.
- Seen in: LV.

### 20. Quote or testimonial card

- Anatomy: oversized opening quote glyph in the accent, the quote at 24 to 28 with 1.25 line height, generous empty space, attribution in secondary at 14, one context line.
- Values: card padding 24 to 32; radius from the product's logic; one card per view, swipeable.
- Avoid: star ratings next to quotes; photos of the person unless real; more than 40 words.
- Seen in: Headspace.

### 21. Ranked rail

- Anatomy: a horizontal rail where each tile is preceded by a large numeral (outlined, neon or in the display face) overlapping the tile's left edge; title under the tile.
- Values: numeral 48 to 64 on mobile in the display voice; tiles 16:9 or 3:4; 12 gap plus the numeral's overlap.
- Avoid: numerals inside the tile; more than 10 items; ranks without a time frame label.
- Seen in: NPO Zapp.

### 22. State-encoding persona (assistants)

- Anatomy: one shape (orb, blob, mark) whose colour or motion encodes the assistant's state: idle, listening, talking, generating; the same shape appears small in the input field and large on the assistant screen; a pill input ("Ask ...") with a microphone.
- Values: four named states with named gradients or colours; transitions 200 to 300ms; the persona never covers content.
- Avoid: a chat bubble avatar as the only identity; animating the persona while the user types; more than one persona.
- Seen in: Priceline Penny.

### 23. Focus fill (TV and keyboard)

- Anatomy: the focused element fills with the accent (or inverts to white on dark) and its text turns to the contrasting colour; a slight scale (up to 1.05) is optional; no outline-only focus on TV.
- Values: fill transition 100 to 150ms; focus always visible on at least one element.
- Avoid: glow-only focus; focus that moves content.
- Seen in: Fubo.

### 24. Gradient scrim over imagery

- Anatomy: a vertical gradient from transparent to the canvas colour over the lower 40 to 60 percent of an image, so text and controls sit on the canvas colour.
- Values: text meets 4.5:1 at its position; gradient eased (several stops) so no hard edge appears.
- Avoid: a flat dark bar; text at 60 percent opacity on the image; scrims on both top and bottom unless controls sit at both.
- Seen in: Gatorade, Fubo, Harrods, LV.

### 25. Onboarding carousel with one idea per screen

- Anatomy: three to five screens, each with one illustration or photo, one headline at title size, one sentence, page dots, one primary action and a skip link.
- Values: headline 24 to 28; illustration within the top 55 percent; dots 6 to 8 with 8 gap; primary pinned.
- Avoid: permission requests inside the carousel; two sentences; value propositions the product does not show immediately after.
- Seen in: Penny, Headspace (web onboarding).

## Web and marketing patterns

### 26. Photo hero with uppercase nav

- Intent: open a product or brand site with one image and one line.
- Anatomy: full-bleed photograph or video with a gradient scrim, a thin header with the wordmark left and 4 to 6 small uppercase nav links plus one icon (search or cart) right, headline bottom-left at display size (2 lines maximum), one short line of support copy, one small pill or bar CTA; the next section starts with a brand-colour band or a tight grid.
- Values: nav links 12 to 13 at +0.06em caps; headline 45 to 57 on expanded, 32 to 36 on compact; CTA 40 to 48 high; scrim over the lower 50 percent.
- Variants: a looping video instead of a still; headline overlapping the image edge in a serif (editorial luxury).
- Avoid: a centred headline with two buttons; a hero carousel; text on an unscrimmed image; a hero taller than the viewport.
- Seen in: Gatorade.com, Harrods (new season), Headspace (web).

### 27. Feature section with a device in a brand frame

- Intent: explain one feature with the product itself as proof.
- Anatomy: two columns on expanded (text 5 columns, device 7, or the reverse), eyebrow label, headline at headline size, two to three lines of body, optional text link; the device sits inside a rounded panel in the brand colour or on the dark section canvas; sections alternate sides.
- Values: section padding 64 to 96 vertical; panel radius from the product's logic (16 to 28); device screenshot at real scale with real content; one feature per section.
- Variants: a row of category chips above the section; a floating stat card or two over the photo (collage) when the feature is about numbers.
- Avoid: three features per section in equal columns with icons; angled 3D devices in every section; placeholder screens.
- Seen in: STC Bank (web), Headspace (web), Gatorade.com.

### 28. Editorial story block

- Intent: tell one story (collection, article, guide) with magazine pacing.
- Anatomy: an image and a text block in a two-column relationship (image 7, text 5, or image bleeding to one edge), eyebrow in caps or small text, headline in the display voice (serif with italic for luxury), 60 to 90 words of body in a narrow column, one text link; blocks alternate image side down the page.
- Values: body measure 45 to 65 characters; headline 32 to 45; vertical gap between blocks 64 to 96; images at consistent aspect ratios.
- Variants: headline overlapping the image corner; three-up story cards with image, eyebrow, title and one line (Harrods "Latest trends"); a quote block with an oversized quote glyph.
- Avoid: cards with borders and drop shadows; more than one CTA per block; stock photography.
- Seen in: Harrods, Aesop, Headspace (article page).

### 29. Brand chart

- Intent: show a trend or comparison inside the product's identity, not a charting library's.
- Anatomy: a title at title size with a period selector (chip or dropdown) right, the chart, a legend only when more than one series, axis labels at label size in secondary colour; the chart palette is two or three brand colours, the first series in the accent or the foreground.
- Values: hairline gridlines only (or none); line weight 2 to 3; bar radius 2 to 4 or none per the product's radius logic; values tabular; one chart per card.
- Variants: sparkline inside a stat card (no axes); stacked bars in brand colours (STC web); two-series line with a legend (Brand New Day).
- Avoid: library default palettes; 3D or gradient fills; a chart without the question it answers in the title; more than four series.
- Seen in: STC Bank (merchant portal and homepage), Brand New Day (returns).

## Choosing a pattern

| Job of the screen | Pattern |
| --- | --- |
| Show the number or fact the user came for | 1 Hero figure screen |
| First impression, sign in, welcome | 2 Brand canvas screen, 25 Onboarding carousel |
| Manage, review, pay, configure | 3 Monochrome working screen, 9 Hairline list row, 12 Bottom primary action |
| Sell one object | 4 Editorial product page, 19 Product panel over imagery |
| Browse content or products | 13 Borderless media grid, 21 Ranked rail, 14 Category chip set |
| Watch or experience media | 5 Immersive media screen, 7 Ten-foot screen, 24 Gradient scrim |
| Capture or try on | 6 Camera-first overlay |
| Orient and route | 8 Dashboard home, 10 Stat card, 17 Tab bar, 16 Minimal header |
| Act on something in context | 11 Drag-handle sheet, 15 Segmented tabs, 18 Status tag |
| Talk to an assistant | 22 State-encoding persona |
| Open a product or brand site | 26 Photo hero with uppercase nav, 27 Feature section with a device in a brand frame |
| Tell a story, present a collection or article | 28 Editorial story block, 20 Quote card |
| Show a trend or comparison | 29 Brand chart, 10 Stat card |

## Pattern review

When reviewing a screen: name the pattern it uses (or should use), check its anatomy is complete, check its values against the platform metrics, check its states exist, and check the identity decisions (canvas, accent, type voice, radius) are applied as the product decided them. A screen that mixes two patterns for one job, or invents a layout where a pattern exists, is a finding.
