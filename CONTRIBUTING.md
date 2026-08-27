# Contributing

Contributions should make the Action Boundary Brief more useful without enlarging its authority.

Propose a change with a concrete reason, preserve the distinction between preparation and approval, use fictional or sanitized examples, and update the relevant source note when a factual claim changes. Do not add model-vendor lock-in, telemetry, account requirements, personal data, customer stories, performance claims, certification language, or automated authorization behavior.

Run both validators before opening a pull request:

```bash
python3 scripts/validate_boundary_brief.py templates/action-boundary-brief.md
node scripts/validate-static.mjs
```

An issue or pull request is a discussion record; it does not grant someone authority over a real-world action.

