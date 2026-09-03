# action-boundary-brief

A small pre-action record for defining what a workflow may access, change, decide, and do before it crosses a meaningful boundary.

The Action Boundary Brief helps a team make the important parts of a proposed action visible before access turns into authority. It records the intended outcome, the resources involved, the exact decision right being requested, the person responsible for exceptions, the condition that stops normal progress, and the minimum record another reviewer would need later.

It is deliberately narrow.

It does not approve an action, grant permission, perform a security review, establish legal compliance, or decide whether a use is safe.

## The problem it solves

Many failures begin with an ambiguous sentence such as:

> Let the system handle it.

That sentence can hide several different permissions.

Can the workflow read the data?

Can it summarize the data?

Can it recommend an action?

Can it prepare a draft?

Can it send the draft?

Can it change a live system?

Can it spend money, alter access, schedule work, or make a commitment for someone else?

Those are not the same decision.

The Action Boundary Brief separates them before the work proceeds.

## What the brief records

Every brief preserves six sections.

### 1. Intended outcome

State what should happen for the user or operation. Describe the result, not the capability of a tool.

### 2. Resource envelope

List the material things the workflow could touch, such as:

- data
- tools
- people
- time
- money
- communications
- production systems

For each one, record the intended use, owner, named limit, and anything that could change that limit.

### 3. Decision rights

Choose the narrowest right the workflow actually needs:

```text
observe
summarize
recommend
draft without sending
execute within a named limit
```

Then state the permitted action, prohibited action, and the condition that ends that right.

Access is not treated as permission to act.

### 4. Accountable escalation and interruption

Name the person or role responsible when the normal path no longer applies.

Define:

- the condition that pauses or escalates the work
- who resolves the exception
- how the action can be stopped or contained

A boundary is not useful if nobody knows what happens when it is crossed.

### 5. Minimum review record

Preserve enough context for another person to reconstruct what happened later:

- source and context
- candidate output or proposed action
- human decision or exception
- final action and result
- unresolved questions

The goal is not exhaustive logging. It is enough evidence to understand the decision.

### 6. Review state and next step

A brief may be:

```text
draft
proposed
reviewed
retired
```

The status describes the state of the record. It does not authorize the action.

The brief should always end with the next responsible action and who owns it.

## When to use it

Use an Action Boundary Brief before a workflow may:

| Situation | Boundary to clarify |
|---|---|
| Read non-public information | Which data is permitted, what is excluded, and who owns the limit? |
| Communicate outside the team | May it draft only, or may it send? Who reviews recipients and content? |
| Change a production system | Which exact change is allowed, what ends that permission, and how can the change be contained? |
| Commit money or resources | What amount, scope, duration, or vendor boundary applies? |
| Affect another person's access, schedule, work, or rights | Which judgment must remain with a responsible person? |
| Act from a model recommendation | Is the system observing, recommending, drafting, or executing? |

For ordinary low-consequence work, this may be unnecessary. The brief earns its place when a mistake would be difficult to ignore, reverse, explain, or assign responsibility for.

## Quick start

Copy the template:

[`templates/action-boundary-brief.md`](templates/action-boundary-brief.md)

Fill every section. If something important is unknown, write that it is unknown rather than removing the field.

Use fictional, public, or sanitized information in records intended for this repository. Do not place credentials, personal data, private customer information, secrets, or sensitive incident details in a public brief.

Then run the structural check:

```bash
python3 scripts/validate_boundary_brief.py path/to/brief.md
```

A successful result confirms that the required structure is present.

It does not mean the action is approved.

## Example decision

Suppose a workflow is being considered for customer support email.

A vague instruction might say:

```text
Use the model to handle support replies.
```

A useful boundary is more precise:

```text
Outcome:
Reduce the time required to prepare routine support replies.

Requested right:
Draft without sending.

Permitted:
Read the assigned support thread and prepare a response draft.

Prohibited:
Send messages, issue refunds, change account access, or make commitments.

Pause trigger:
The request involves billing disputes, security, account ownership, or an unsupported claim.

Accountable person:
The support agent assigned to the thread.
```

The workflow becomes easier to review because the important choices are no longer implied.

## What the validator checks

[`scripts/validate_boundary_brief.py`](scripts/validate_boundary_brief.py) is dependency-free.

It checks for:

- required frontmatter
- an allowed status
- all six required sections
- required decision and interruption fields
- the resource-envelope table
- the minimum-review-record table
- unsupported assurance language such as claims that the brief itself certified or authorized the action

It checks format only.

It does not inspect whether the limits are sensible, whether the accountable person has authority, whether the action is secure, or whether applicable obligations have been met.

## Repository structure

```text
.
├── SKILL.md
├── templates/
│   └── action-boundary-brief.md
├── scripts/
│   └── validate_boundary_brief.py
├── references/
│   └── source-notes.md
├── research/
├── index.html
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

### `SKILL.md`

Compact instructions for using the method with a human collaborator or software assistant.

### `templates/`

The reusable record itself.

### `scripts/`

A local structural check with no third-party runtime dependencies.

### `references/`

The public sources that informed the method and, equally important, the claims the method does not make.

### `index.html`

A portable public explanation and walkthrough.

## Method limits

The Action Boundary Brief is an implementation aid, not a governance framework.

It can help expose missing scope, unclear ownership, excessive decision rights, or an absent interruption path. It cannot determine whether a proposed use is lawful, secure, safe, appropriate, or compliant.

The method was informed by public guidance from NIST, the EU AI Act, and OWASP around context, oversight, traceability, excessive agency, and intervention. The exact source notes and limits are documented in [`references/source-notes.md`](references/source-notes.md).

Use qualified legal, security, privacy, safety, or compliance review when the situation requires it.

## Relationship to ai-change-record

`action-boundary-brief` is used **before** a consequential action.

[`ai-change-record`](https://github.com/virtualmase/ai-change-record) is used **after** a material change to preserve what changed, why, what was checked, what should be monitored, and how to recover.

They solve different problems:

```text
before action                  after change

boundary brief  →  decision  →  change record
```

One makes the intended boundary visible. The other preserves the change that actually occurred.

## Contributing

Useful contributions include:

- clearer field wording
- better sanitized examples
- validator improvements
- corrections to source notes
- cases where an important boundary is currently hard to express

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

Do not publish credentials, personal information, customer material, private incident details, or sensitive security information in issues or examples. Use [`SECURITY.md`](SECURITY.md) for security reporting guidance.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).

---

**virtualmase**

*build quietly.*