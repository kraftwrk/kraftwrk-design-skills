---
name: design-decision-log
description: The learning loop for the Kraftwrk design skills. Captures the design decisions and corrections Marc makes during a project, keeps project-specific ones with the project, and turns general ones into rules in the right skill (kraftwrk-design-style, product-design-foundations, typography-craft, product-ui-patterns, product-brand-identity, agency-grade-review). Use at the end of any design session, when Marc says "remember this", "make this a rule", "log this decision", "we decided" or "from now on", after Marc corrects or overrides a design choice, and when a client decision contradicts a rule in the skills.
---

# Design decision log

## What this skill is

Every decision Marc makes in a project is either something about that project (its brand, its client, its constraints) or something about how Marc designs (which would hold on the next project too). The first kind is recorded with the project so it is not relitigated. The second kind becomes a rule in the skills, so the next session does not make the same mistake and Marc does not have to steer twice.

This skill does one thing: it writes decisions down in the right place, in a form the next agent can follow. It never changes design work itself, and it never adds a rule Marc did not make.

## Hard rules

1. Only Marc's decisions. A rule must trace to something Marc said, chose, edited or confirmed. Claude's own suggestions are not rules until Marc adopts them; then the rule is "going with X", not the reasoning Claude supplied.
2. Never invent a why. If Marc gave no reason, propose one marked "inferred" and confirm it before writing. A wrong reason spreads to cases it does not fit.
3. Propose, then write. Show the candidate decisions in a table and write only what Marc approves. A wrong rule repeats in every future session.
4. Class level, not instance level. "The pricing card gets no shadow" protects one card. "Raised surfaces separate by surface colour, never by shadow" protects every surface. "Never use shadows" breaks inputs. Pick the narrowest level that would have prevented the correction on a different screen.
5. Strict wording with values. Always and never, tokens, numbers, platform names. "Prefer" only when Marc framed it as a preference.
6. Project decisions never silently override general rules. A project that breaks a rule gets a recorded exception with its reason; the rule itself changes only when Marc says it applies everywhere.
7. Values policy: a decision that departs from Material 3 or Apple HIG is recorded as an exception with its reason, project-level by default. When the guidelines themselves change (a new Material or iOS release), the values in the skills are re-checked against the live guideline pages and updated with the date and the source, after Marc has seen the diff.

## When it runs

- Marc asks: "remember this", "make this a rule", "log this", "we decided", "from now on", "add that to the skill".
- Marc corrects or overrides a design choice, chooses one variant over another, reverts something, or edits a file Claude wrote.
- A client or project constraint contradicts a rule in the skills.
- Material Design or the Human Interface Guidelines changed, or a platform value in the skills looks out of date: re-check it against the live guideline page and propose the update.
- After an improvement pass (prompts/improve-the-skills.md): each finding the skills allowed becomes a candidate rule with the finding as its reason, proposed like any other decision.
- A rule is borrowed from another skill set (Impeccable, Intent, Emil Kowalski): write it in this skill's rule form with its source, propose it, and credit the source in NOTICE.md once Marc adopts it. Until then it is not a rule.
- The end of a design session: run a capture pass before closing.

## Signals to collect

Explicit corrections are the minority. Look for all of these in the session:

| Signal | Example | What it tells you |
| --- | --- | --- |
| Explicit correction | "No, hairlines, not cards" | The rule, often with the why |
| Silent edit | Marc changed a radius from 12 to 4 in a file Claude wrote | Claude's default was wrong; Marc's value is the rule |
| Repeated nudge | "Tighter." then "Still too loose." then "Good" | Record where it landed, not the steps |
| Revert or choice | "Undo that", picking direction B over A | What not to do; the why is usually missing, so ask |
| Confirmed non-obvious choice | "Yes, keep the logo off the home header" | Worth recording only if a fresh agent would plausibly do otherwise |
| Client constraint | "Their brand red fails contrast, so it is a surface colour only" | Project decision, maybe a general pattern |
| Adopted suggestion | Claude proposed, Marc said "go with that" | Record the gist as Marc's choice |

Skip what is not a decision: functional bugs, content for one screen, corrections to Claude's understanding of the task.

## Workflow

### 1. Collect

List every decision from the session with Marc's exact words (or the diff), what Claude had done, what Marc wanted instead, and any reason given.

### 2. Classify

Walk each decision through this tree:

- Would this hold on a different client's project?
  - No: project decision. Goes in the project's decision record.
  - Yes: general rule. Which skill?
    - Taste, preference, how Marc likes things: kraftwrk-design-style.
    - A number, a platform metric, a technical baseline: product-design-foundations.
    - Typeface choice, pairing, setting, numerals, micro-typography: typography-craft.
    - A reusable screen or component layout, or a variant of one: product-ui-patterns.
    - How identity is expressed (canvas, accent, type voice, radius logic, brand moments, voice): product-brand-identity.
    - A review criterion, a test, a severity: agency-grade-review.
- Does an existing rule already cover it?
  - Same thing: the rule failed. Rewrite it stricter (a value, a token, "never") instead of adding a duplicate.
  - Contradicts: show both and let Marc pick.
- Is it a departure from Material 3 or HIG? Record as an exception with the reason.

### 3. Write

Each rule is one line plus its reason:

```
- [always or never statement with values]. Reason: [Marc's words]. Source: [project, date].
```

Self-test before proposing: read only the rule and its reason, picture the original screen, and ask whether an agent that knows nothing else would now produce what Marc wanted. If it could still produce the wrong version, add the value, the token or the exception.

### 4. Propose

Show a table and wait for approval:

| # | Decision (Marc's words) | Scope | Goes to | Proposed rule | Reason | Confidence |
| --- | --- | --- | --- | --- | --- | --- |

Confidence is "stated" (Marc gave the reason) or "inferred" (Claude proposed the reason; confirm it).

### 5. Record

Project decisions:

- A project keeps one decision record. With Intent installed that is Intent's decisions.md, in its entry format (date and decision, decided by, why, rejected, rests on) with a "Departs from" line when a rule or a Material or HIG value is left. Without Intent it is DESIGN-DECISIONS.md at the root of the project's repo or connected folder: date, decision, reason, status (active, superseded), and the rule it departs from if any. Create the file if it does not exist. Never keep both.
- A kept invention that breaks a rule (a size off the scale, an eyebrow, a third weight, a convention left on purpose) is recorded as an exception: the part, the rule it departs from, the job it does. The review reports recorded exceptions as exceptions, not as findings.
- A decision that changes the system (a token, the radius logic, the type voice) also updates DESIGN.md when the project has one, so that file always describes the system as it stands. The reason stays in the decision record.
- When no project folder exists (chat only), write the decision into the project's memory area so the next session in that project sees it, and say so.

General rules:

- In Claude Code or any tool with the kraftwrk-design-skills repo checked out: edit the SKILL.md of the target skill, add a line to CHANGELOG.md (date, skill, rule), and commit with the message "rule: <short rule>". Push when Marc confirms.
- In Cowork, where the skills run as the kraftwrk-design-skills plugin: make the change in the repo copy, raise the plugin version, and give Marc the patch to apply and push; the plugin picks it up on update. Loose skills in the account (none of these seven) change through the skill review card.
- Rewrite a failed rule in place; never leave two versions.

### 6. Report

One line per written decision, where it went, and anything left unresolved (an inferred reason Marc did not confirm, a conflict Marc did not settle).

## End-of-session capture

Run this before closing a design session, unprompted:

1. Collect the signals above from the whole session.
2. Classify and write candidates.
3. Propose the table. If Marc is not there to answer, write project decisions (they are his words anyway) and park the general rules in the report for the next session; do not write them to the skills unconfirmed.

## Companion skills

- In Claude Code, Emil Kowalski's learn-taste does the same loop for code-level corrections (CSS values, animation props) and writes to DESIGN.md or a project skill. Run it first for code, then this skill for design decisions.
- kraftwrk-design-style points here from "Corrections become rules". agency-grade-review's findings that Marc overrides are signals for this skill.

## Example

Marc, during a client banking app: "Use 4 for everything, their whole brand is sharp. And never put the balance in the accent colour, it is not a button."

| # | Decision | Scope | Goes to | Proposed rule | Reason | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Radius 4 everywhere | Project | DESIGN-DECISIONS.md | Radius logic: sharp, 4 on all tiers | Their brand is sharp | stated |
| 2 | Balance never in the accent | General | product-brand-identity | The hero figure is never set in the accent colour; the accent marks actions and status only | It is not a button | stated |

After approval: decision 1 is appended to the project file; decision 2 is added under the hero figure decision in product-brand-identity, logged in CHANGELOG.md, committed as "rule: hero figure never in the accent colour".
