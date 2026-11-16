# Prompt: improve the skills

Paste this into a session that has the kraftwrk-design-skills repo checked out (Claude Code) or the skills saved in the account (Cowork). Replace the briefs when you want to test a different kind of product.

---

Run an improvement pass on the kraftwrk-design-skills set: product-design-foundations, typography-craft, product-ui-patterns, product-brand-identity, kraftwrk-design-style, agency-grade-review and design-decision-log.

1. Test, do not theorise. Using only the skills, design three products from these briefs: (a) a Dutch neobank app for freelancers, calm and precise; (b) a luxury eyewear e-commerce site, editorial and quiet; (c) a kids' public-broadcaster video app, loud and safe. For each, produce the ten identity decisions as a matrix, one hero screen, one dense working screen, one sheet or overlay, one loud brand moment, and one marketing page section, as HTML prototypes with real content (long names, zero and many items, the longest language). Show me the prototypes.

2. Review your own output with agency-grade-review in Full mode, including the typography review from typography-craft and the identity tests from product-brand-identity (ten decisions, default count, intensity, device, swap). Run the audit (skills/agency-grade-review/scripts/audit.py) on every prototype and record its counts next to the scores in evals/README.md. Score all 16 bar items per product. In this unattended test the option round still runs: sketch the three ideas per key screen, pick one yourself and say which and why.

3. Every finding the skills allowed is a missing or vague rule. For each one, write the rule the way design-decision-log writes rules: class level, with values, always or never, with the reason. Mark where it belongs. Show me the proposed diffs per skill before changing anything; do not edit the skills until I approve.

4. For the weakest area in the scores, study three new sources and bring back only rules that pass the self-test ("would an agent that knows nothing else now produce what Marc wants?"). Candidates: Apple's WWDC design talks and the Human Interface Guidelines, the Material Design 3 guidelines, Erik Spiekermann and Tobias Frere-Jones on type, Rauno Freiberg's interface notes, Emil Kowalski's writing, Linear's design pages, the published product work of ustwo, Instrument, Huge and Dept, shipped flows on Mobbin when it is connected, and the playbooks and detector rules of Impeccable. Cite the source for each rule.

5. Constraints: values follow Material Design 3 and Apple HIG unless a specific case requires otherwise, and any exception is written down with its reason; re-check every platform value you touch against the live Material 3 and HIG pages, never from memory, because they change with each release; no em dashes anywhere; keep each SKILL.md under 300 lines, so condense before adding; never duplicate a rule across skills, point to it instead; keep the catalogues as options with the signal they send and where they were seen; do not weaken any rule to make the prototypes pass.

6. Finish with: the diffs, the three prototypes before and after the new rules, the review scores before and after, and a CHANGELOG entry. In Claude Code, commit as "rules: improvement pass <date>" once I approve. In Cowork, give me the patch to apply and push.
