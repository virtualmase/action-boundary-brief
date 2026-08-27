#!/usr/bin/env python3
"""Format check for an Action Boundary Brief; not an approval or risk assessment."""
from __future__ import annotations
import re
import sys
from pathlib import Path

REQUIRED_META = {"id", "status", "created", "prepared_by", "accountable_person", "reviewer"}
ALLOWED_STATUS = {"draft", "proposed", "reviewed", "retired"}
REQUIRED_HEADINGS = ["## 1. Intended outcome", "## 2. Resource envelope", "## 3. Decision rights", "## 4. Accountable escalation and interruption", "## 5. Minimum review record", "## 6. Review state and next step"]
REQUIRED_LABELS = ["**Requested right:**", "**Permitted action:**", "**Prohibited action:**", "**Limit that ends the right:**", "**Accountable person:**", "**Pause or escalation trigger:**", "**Stop or containment path:**", "**Next responsible action:**"]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate_boundary_brief.py path/to/brief.md", file=sys.stderr); return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: file not found: {path}", file=sys.stderr); return 2
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter:
        errors.append("frontmatter is required"); metadata: dict[str, str] = {}
    else:
        metadata = dict(re.findall(r"^([a-z_]+):\s*(.+)$", frontmatter.group(1), re.MULTILINE))
        missing = REQUIRED_META - metadata.keys()
        if missing: errors.append(f"missing frontmatter fields: {', '.join(sorted(missing))}")
        if metadata.get("status") not in ALLOWED_STATUS: errors.append("status must be one of: draft, proposed, reviewed, retired")
    for heading in REQUIRED_HEADINGS:
        if heading not in text: errors.append(f"missing section: {heading}")
    for label in REQUIRED_LABELS:
        if label not in text: errors.append(f"missing required field: {label}")
    if not re.search(r"\|\s*Resource or affected party\s*\|", text): errors.append("resource-envelope table is required")
    if not re.search(r"\|\s*Record element\s*\|", text): errors.append("minimum-review-record table is required")
    if re.search(r"\b(certified|compliant|safe to deploy|authorized by this brief)\b", text, re.IGNORECASE): errors.append("remove unsupported assurance language")
    if errors:
        for error in errors: print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {path.name} contains the required Action Boundary Brief structure. This is a format result, not approval.")
    return 0

if __name__ == "__main__": raise SystemExit(main())

