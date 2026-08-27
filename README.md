# Action Boundary Brief

**A model-neutral pre-action skill for making AI-enabled work legible before it receives meaningful access or execution rights.**

An Action Boundary Brief helps a person or team write down the outcome, resource envelope, requested decision right, accountable human, interruption condition, and minimum review record for a proposed AI-enabled action. It is designed to make ambiguity visible early.

> It does **not** grant authority, approve a system, establish legal compliance, perform a security review, or determine whether a use is safe.

## Why this exists

High-level AI risk and security guidance repeatedly emphasizes context, human oversight, documentation, and limits on unchecked action. The practical gap is often a small shared artifact that can be completed before a workflow moves from analysis into an operational change. The Action Boundary Brief is that artifact, informed by NIST’s voluntary AI RMF and Generative AI Profile, Article 14’s description of human oversight for high-risk AI systems, and OWASP’s treatment of excessive agency and overreliance. Read the precise source notes and boundaries in [`references/source-notes.md`](references/source-notes.md).

## Use it when

| Trigger | Example boundary question |
|---|---|
| An AI workflow may read non-public material | What data can it access, what is out of scope, and who owns the limit? |
| A model output could be sent outside the team | Can it draft only, or can it send? Who reviews the recipient and content? |
| A workflow may alter a live system | What exact change is permitted, what stops it, and how is it contained? |
| A recommendation could affect money, schedules, people, or other rights | Which judgment remains with a responsible person? |

## Use the skill

Copy [`templates/action-boundary-brief.md`](templates/action-boundary-brief.md), complete every field using only sanitized information, and keep the status at `draft`, `proposed`, `reviewed`, or `retired`. Then validate the structure:

```bash
python3 scripts/validate_boundary_brief.py your-brief.md
```

The validator is dependency-free and only checks whether the brief carries the required format. A passing result is not an operational approval.

## Repository map

| Path | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Compact instructions for an AI assistant or human collaborator. |
| [`templates/action-boundary-brief.md`](templates/action-boundary-brief.md) | The reusable brief template. |
| [`scripts/validate_boundary_brief.py`](scripts/validate_boundary_brief.py) | Dependency-free structural validator. |
| [`references/source-notes.md`](references/source-notes.md) | Source basis and non-compliance boundary. |
| [`research/discovery.md`](research/discovery.md) | Evidence-led selection record for this public utility. |
| [`index.html`](index.html) | Portable public showcase and walkthrough. |

## Contribute and report concerns

Open an issue to improve the template, identify a factual error, or propose a new sanitized example. Do not file private security disclosures, credentials, personal data, customer information, or real production incident details in public issues. See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md).

## License

This project is available under the [Apache License 2.0](LICENSE). It is an implementation aid, not professional, legal, regulatory, security, safety, or compliance advice.

