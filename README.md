# Kraftwrk design skills

Agent skills that make Claude (and other coding agents) design digital products at the level of top product design agencies, with Marc Luijkx's personal signature on top, and that learn from the decisions Marc makes on real projects.

A skill is a folder with a `SKILL.md` file: rules an agent loads when the task matches the skill's description. These six stack on top of each other and on top of whatever client design system is in play.

## The stack

```
7. design-decision-log        the learning loop: project decisions become rules or project records
6. agency-grade-review        the gate: critique and self-review before anything is shown
5. kraftwrk-design-style      Marc's signature: the choices that stay the same across clients
4. product-brand-identity     the product's bespoke identity, or a client brand translated into UI
3. product-ui-patterns        the pattern library: screens and components with anatomy and values
2. product-design-foundations the technical baseline, with values from Material Design 3 and Apple HIG
1. client design system       the vocabulary: tokens, components, brand assets (per client, not in this repo)
```

Motion is handled by Emil Kowalski's skills (installed separately, see below). Web code review by Vercel's web-design-guidelines.

| Skill | Use it when |
| --- | --- |
| `product-design-foundations` | Designing, building, prototyping or specifying any screen, component, flow or design system |
| `product-ui-patterns` | Composing a screen or component; picking the right pattern for a job |
| `product-brand-identity` | A product needs an identity or direction, a brand has to show up in UI, or work looks generic |
| `agency-grade-review` | Reviewing, critiquing, rating or shipping design work; also runs automatically as self-review |
| `kraftwrk-design-style` | Any design work Marc asks for (loads on top of the skills above) |
| `design-decision-log` | End of a design session, "remember this", "make this a rule", or after a correction |

## Values

Numbers follow Google's Material Design 3 and Apple's Human Interface Guidelines: the major second type scale (1.125) mapped to the platform text styles, the 4px grid with 8 steps for layout, the Material shape scale for radius, platform component metrics, state layers and window size classes. The skills break out only when a specific case really requires it, and the exception is written down with its reason.

## Install

### Claude Code, Cursor, Codex and other agents (via skills.sh)

```bash
npx skills@latest add <your-github-user>/kraftwrk-design-skills
```

Then add the companion skills:

```bash
npx skills@latest add emilkowalski/skills
npx skills@latest add vercel-labs/agent-skills
```

### Claude.ai and Cowork

Skills in the Claude app live in your account, not in this repo. Upload each skill folder (zipped) once in Settings under Capabilities, then re-upload when you change it here. For motion, upload these from Emil's repo as well: `emil-design-eng`, `animate`, `animate-expo`, `review-animations`, `break-ui`.

## How the skills learn

`design-decision-log` runs at the end of every design session and whenever Marc corrects, overrides or chooses something. It collects the decisions, classifies them, and proposes where each one goes:

- Project-specific (this client's brand, constraints, exceptions): appended to `DESIGN-DECISIONS.md` in the project (template in `templates/`).
- General (would hold on the next project): a rule with its reason in the right skill. In Claude Code the skill edits the SKILL.md here, logs it in `CHANGELOG.md` and commits; in Cowork it proposes the update with the skill review card, and the same change is copied here so every tool stays in sync.

Rules are written strictly (values, tokens, always and never), at class level, and only from Marc's own decisions. In Claude Code, Emil's `learn-taste` does the same for code-level corrections; run it first, then `design-decision-log`.

## What these skills are based on

The agency level the skills aim at comes from the published work and writing of Work & Co, MetaLab, Clay, Fantasy, AKQA, Framna and Wolff Olins, plus Apple's Human Interface Guidelines, Material Design 3, WCAG 2.2, Emil Kowalski's design engineering rules and Vercel's Web Interface Guidelines. Agency case studies show results rather than internal standards, so the rules here are a synthesis of what their work consistently gets right, written as checkable rules.

The visual evidence is in `docs/agency-visual-patterns.md`: observations from the product screenshots and videos of 18 case studies (canvas, colour economy, type, hero figures, separation, radius, imagery, navigation, brand moments, motion signatures, dark mode, and how the agencies present work). `product-ui-patterns` turns those observations into pattern definitions; the doc keeps the evidence so rules can be checked and revised.

## Layout

```
skills/
  product-design-foundations/SKILL.md
  product-ui-patterns/SKILL.md
  product-brand-identity/SKILL.md
  agency-grade-review/SKILL.md
  kraftwrk-design-style/SKILL.md
  design-decision-log/SKILL.md
docs/
  agency-visual-patterns.md
templates/
  DESIGN-DECISIONS.md
CHANGELOG.md
```

Companion skills (not included, install from their own repos):

- Emil Kowalski's skills: https://github.com/emilkowalski/skills (MIT)
- Vercel agent skills: https://github.com/vercel-labs/agent-skills (MIT)
