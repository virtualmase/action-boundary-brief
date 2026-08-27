# Source Notes and Method Limits

The Action Boundary Brief is a small implementation aid, not a new governance framework. It makes a proposed action easier to inspect by asking for the outcome, resource envelope, decision right, accountable person, interruption path, and minimum review record.

| Source | Relevant point | How this skill uses it | What this skill does not claim |
|---|---|---|---|
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | The voluntary framework is designed to help organizations incorporate trustworthiness considerations into the design, development, use, and evaluation of AI systems, organizing work around Govern, Map, Measure, and Manage. | The skill records a narrow context and makes ownership and limits inspectable. | It does not implement, certify, or assess the AI RMF. |
| [NIST AI 600-1: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | The profile identifies governance, content provenance, pre-deployment testing, and incident disclosure as primary considerations, and emphasizes context-specific risk management. | The brief retains a context, source, decision, outcome, and unresolved question. | It does not quantify risk, test a system, or establish incident reporting. |
| [EU AI Act Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) | The Article describes proportionate human oversight for high-risk systems, including understanding limitations, monitoring, interpretation, override, intervention, and a safe halt. | The skill requires an accountable human, a pause trigger, and stop or containment path when relevant. | It does not determine whether the Act applies or establish legal compliance. |
| [OWASP GenAI LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | OWASP identifies excessive agency and overreliance as critical LLM-application risks; current development resides with the OWASP GenAI Security Project. | The brief separates recommendation, drafting, and execution, and requests independent human review where rights cross a material boundary. | It does not replace threat modeling, secure design review, or application security testing. |

## Research interpretation

The sources converge on a practical operational need: teams need ways to make scope, human oversight, and traceability concrete in a particular context. This skill responds with a deliberately narrow artifact. The artifact is useful when it surfaces ambiguity early; it should never be used to create a veneer of assurance around a decision that needs qualified review.

