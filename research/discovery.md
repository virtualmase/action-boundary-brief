# Public Skill Discovery Record: Action Boundary Brief

**Research date:** 2026-08-27  
**Candidate public need:** Help people turn a proposed AI-enabled action into a small, inspectable operating brief before they grant tools, data, authority, or execution rights.

## Evidence reviewed

| Source | What it establishes | Design implication |
|---|---|---|
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | NIST describes the AI RMF as a voluntary framework for incorporating trustworthiness considerations into AI design, development, use, and evaluation. Its public materials organize risk work around Govern, Map, Measure, and Manage. | A useful public tool should be practical but must not call itself a certification, audit, or conformity assessment. |
| [NIST AI 600-1: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | The profile frames governance, content provenance, pre-deployment testing, and incident disclosure as primary considerations, and explains that risk management depends on the particular lifecycle stage, system, use case, and context. | A reusable skill should capture a specific context rather than provide a universal score or generic “safe” label. |
| [EU AI Act, Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) | For high-risk systems, oversight should be proportionate to risks, autonomy, and context. Oversight users must be enabled, as appropriate, to understand limitations, monitor operation, interpret outputs, override or reverse outputs, and intervene or stop the system. | The skill should name a human decision point, stop condition, and reversal/containment path. It is not a statement of legal compliance. |
| [OWASP GenAI LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | OWASP identifies excessive agency and overreliance among important LLM-application risks. The active work has moved to the OWASP GenAI Security Project. | The skill should separate recommendation from execution and require a reviewer to state which outputs need independent checking. |

## Candidate comparison

| Candidate | Public value | Distinct from existing ARM work | Boundary risk | Selection |
|---|---|---|---|---|
| AI governance explainer | High general interest, but broad | Too close to existing AI Mastery and ARM teaching | Could overstate expertise | Not selected |
| “AI compliance checker” | Attractive framing | Potentially useful | Would imply legal or conformity assessment authority | Rejected |
| **Action Boundary Brief** | Gives a team or individual a usable pre-action artifact | Builds on ARM concepts without reproducing its reference content | Bounded if framed as preparation and review, not approval | **Selected** |
| Generic prompt library | Easy to publish | Low differentiation | Incentivizes model-specific, disposable content | Not selected |

## Selection rationale

The selected public utility is an **Action Boundary Brief**: a model-neutral workflow that asks a user to document five facts before an AI-enabled workflow is given meaningful access or execution rights: the intended outcome, the resources it could touch, the decision right requested, the accountable person and escalation trigger, and the minimum review record.

The missing practical artifact is not another list of high-level principles. It is a concise, portable brief that a product manager, operator, developer, reviewer, or AI assistant can complete together before an action crosses from advice into an operational change. The output should make ambiguity visible; it must not declare the action safe, compliant, approved, or deployable.

## Boundaries to preserve

The public skill must not provide legal advice, determine risk classification, grant authority, authorize an action, assess compliance, operate tools, ingest sensitive data, or retain user input. A qualified owner must decide whether any proposed action is permitted in their environment. The template should use fictional or sanitized examples only.

## Proposed repository role

The repository will be a standalone public utility and learning showcase. It will carry the skill package, templates, reference notes, a dependency-free validator, and a static site explaining the need, the method, the output, its boundaries, and how to use it. It will link to—but not copy or canonically merge with—the ARM reference and AI Mastery properties.
