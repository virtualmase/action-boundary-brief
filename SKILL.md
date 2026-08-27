---
name: action-boundary-brief
description: Create a model-neutral Action Boundary Brief before an AI-enabled workflow receives sensitive resources, sends external communications, changes a system, or executes within a named limit. Use when a team needs to separate intended outcomes from requested decision rights, name an accountable human, define an interruption path, and prepare a review record without treating the result as approval, legal advice, or a compliance assessment.
license: Apache-2.0
---

# Action Boundary Brief

Create a short, inspectable pre-action record that makes a proposed AI-enabled action legible to the people responsible for it. Use the skill to clarify a boundary, not to decide whether an action is permitted.

## Use when

Use this skill before a workflow is allowed to access material resources or cross an execution boundary. Typical triggers include a request to retrieve non-public data, contact someone outside a team, change a production configuration, create a financial commitment, schedule work for another person, publish content, or execute an action based on a model output.

Do not use it as a substitute for legal review, security review, incident response, a risk classification, or a production approval. Escalate instead when the requested work touches regulated decisions, safety-critical systems, personal data without an approved handling basis, money movement, employment, access control, or irreversible external commitments.

## Workflow

1. **State the proposed outcome.** Describe the user or operational outcome in one sentence. Do not describe a tool capability as an outcome.
2. **Map the resource envelope.** List the data, tools, people, time, money, communications, and downstream systems the workflow could touch. Name the owner and a concrete limit for each material resource.
3. **Separate the decision right.** Choose the narrowest requested right: observe, summarize, recommend, draft without sending, or execute within a named limit. State prohibited actions separately. Never infer authority from access.
4. **Name the accountable human and interruption trigger.** Identify who resolves an exception. Define the condition that pauses the workflow, and a way to stop or contain an action if the condition occurs.
5. **Specify the review record.** Record the sources, scope, candidate output or action, authorization context, final action, result, and unresolved question necessary for another reviewer to reconstruct the decision.
6. **Hand off without an approval claim.** Mark the brief `draft`, `proposed`, `reviewed`, or `retired`. A named owner—not this skill—decides whether the work may proceed.

## Output

Start from [`templates/action-boundary-brief.md`](templates/action-boundary-brief.md). Preserve every heading even when the answer is “not known” or “not applicable”; missing information is itself a review signal. Use fictional or sanitized examples. Do not put credentials, personal data, private customer information, or secrets into a brief.

Run the dependency-free check before sharing:

```bash
python3 scripts/validate_boundary_brief.py path/to/brief.md
```

The validator checks format and required fields only. A passing result is **not** an approval, safety finding, security review, or compliance determination.

## Handoff rules

| Condition | Required next step |
|---|---|
| Resource, right, owner, limit, or interruption trigger is unknown | Keep the brief in `draft` and ask the responsible person for the missing fact. |
| Requested action exceeds a named limit | Pause the workflow and route the exception to the accountable person. |
| Output would communicate externally, commit funds, change access, or affect another person’s rights | Require an explicit human decision in the record before the action. |
| The brief exposes a security, privacy, legal, or safety concern | Stop and use the organization’s appropriate review or incident process. |

## Sources

Read [`references/source-notes.md`](references/source-notes.md) for the source basis and precise limits of the method. The method is informed by, but does not claim conformity with, NIST AI RMF, NIST’s Generative AI Profile, the EU AI Act, or OWASP guidance.

