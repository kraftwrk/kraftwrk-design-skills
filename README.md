# Kraftwrk design skills

Agent skills that make Claude (and other coding agents) design digital products at the level of top product design agencies, with Marc Luijkx's personal signature on top.

A skill is a folder with a `SKILL.md` file: rules an agent loads when the task matches the skill's description. These four stack on top of each other and on top of whatever client design system is in play.

## The stack

```
5. agency-grade-review        the gate: critique and self-review before anything is shown
4. kraftwrk-design-style      Marc's signature: the choices that stay the same across clients
3. product-brand-identity     the product's bespoke identity, or a client brand translated into UI
2. product-design-foundations the technical baseline: layout, type, colour, states, a11y, platforms, tokens
1. client design system       the vocabulary: tokens, components, brand assets (per client, not in this repo)
```

Motion is handled by Emil Kowalski's skills (installed separately, see below). Web code review by Vercel's web-design-guidelines.

| Skill | Use it when |
| --- | --- |
| `product-design-foundations` | Designing, building, prototyping or specifying any screen, component, flow or design system |
| `product-brand-identity` | A product needs an identity or direction, a brand has to show up in UI, or work looks generic |
| `agency-grade-review` | Reviewing, critiquing, rating or shipping design work; also runs automatically as self-review |
| `kraftwrk-design-style` | Any design work Marc asks for (loads on top of the three above) |

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

## Keeping the skills alive

Every time you have to correct the agent on a design matter, that is a missing rule. Add it:

- Taste (how Marc would do it): `kraftwrk-design-style`
- Technical baseline (true for any product): `product-design-foundations`
- Identity: `product-brand-identity`
- Review criteria: `agency-grade-review`

In Claude Code, run Emil's `learn-taste` skill at the end of a design session. It collects the corrections you made and proposes them as rules with their reasons.

Write rules strictly: values, tokens, "always" and "never". Prefer a check over a sentence where possible.

## What these skills are based on

The agency level the skills aim at comes from the published work and writing of Work & Co, MetaLab, Clay, Fantasy, AKQA, Framna and Wolff Olins, plus Apple's Human Interface Guidelines, Material 3, WCAG 2.2, Emil Kowalski's design engineering rules and Vercel's Web Interface Guidelines. Agency case studies show results rather than internal standards, so the rules here are a synthesis of what their work consistently gets right, written as checkable rules.

## Layout

```
skills/
  product-design-foundations/SKILL.md
  product-brand-identity/SKILL.md
  agency-grade-review/SKILL.md
  kraftwrk-design-style/SKILL.md
```

Companion skills (not included, install from their own repos):

- Emil Kowalski's skills: https://github.com/emilkowalski/skills (MIT)
- Vercel agent skills: https://github.com/vercel-labs/agent-skills (MIT)
