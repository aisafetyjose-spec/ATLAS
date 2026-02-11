from vellum import ChatMessagePromptBlock, JinjaPromptBlock, PromptParameters
from vellum.workflows.nodes.displayable import InlinePromptNode
from vellum.workflows.types.core import MergeBehavior

from .input_validator import InputValidator


class GenerateCDIQueries(InlinePromptNode):
    """Generates CDI (Clinical Documentation Integrity) queries.

    CRITICAL RULES:
    - Queries must be NEUTRAL and NON-LEADING
    - Focus on clinical specificity, NOT billing optimization
    - Never suggest diagnoses - only ask for clarification
    - Include evidence from dictation for each query
    """

    ml_model = "claude-sonnet-4-5-20250929"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                JinjaPromptBlock(
                    template="""\
You are ATLAS™ CDI Specialist. Generate compliant CDI queries to improve clinical documentation specificity.

{{ compliance_context }}

=== CLINICAL DICTATION ===
{{ dictation }}

=== CONTEXT ===
Setting: {{ setting }}
Payer: {{ payer }}
Missing Elements Identified: {{ missing_elements | join(\', \') if missing_elements else \'None\' }}

=== CDI QUERY RULES ===
1. Queries must be NEUTRAL and NON-LEADING
2. Focus on clinical specificity, NOT billing optimization
3. Target documentation gaps:
   - Etiology (cause/due to)
   - Acuity (acute vs chronic)
   - Severity/Stage
   - Laterality (R/L/Bilateral)
   - Type/Classification
   - Complications
   - POA status (if inpatient)
   - Causal relationships
4. Use evidence from dictation to justify each query
5. Never suggest diagnoses - only ask for clarification
6. Maximum 10 queries, prioritized High/Medium/Low
7. Include \"Unable to determine\" or \"Clinically undetermined\" as options

=== OUTPUT FORMAT (for each query) ===

**QUERY [#] - [PRIORITY: HIGH/MEDIUM/LOW]**
- **Topic:** [Clinical topic]
- **Evidence from Dictation:** \"[Quote or observation from dictation]\"
- **Query:** [The actual question - neutral, non-leading]
- **Options (if applicable):**
  - [ ] Option A
  - [ ] Option B
  - [ ] Unable to determine / Clinically undetermined
- **Why It Matters:** [Documentation integrity rationale - NOT billing]

=== REQUIRED QUERIES ===
{% if \'Confirm note type\' in (missing_elements | join(\',\')) %}
- Include query to confirm note type
{% endif %}
{% if not time_minutes %}
- If time-based E/M may apply: \"If documenting time-based E/M, please provide total minutes on date of encounter\"
{% endif %}

=== EVIDENCE QUOTES ===
Include 2-3 short quotes from dictation that triggered your queries.

Output in {{ language }} language.\
"""
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[JinjaPromptBlock(template="""Analyze the dictation and generate prioritized CDI queries now.""")],
        ),
    ]
    prompt_inputs = {
        "compliance_context": InputValidator.Outputs.compliance_context,
        "dictation": InputValidator.Outputs.normalized_dictation,
        "setting": InputValidator.Outputs.normalized_setting,
        "payer": InputValidator.Outputs.normalized_payer,
        "missing_elements": InputValidator.Outputs.missing_core_elements,
        "time_minutes": InputValidator.Outputs.normalized_time_spent_minutes,
        "language": InputValidator.Outputs.output_language,
    }
    parameters = PromptParameters(
        stop=[],
        temperature=None,
        max_tokens=64000,
        top_p=None,
        top_k=None,
        frequency_penalty=None,
        presence_penalty=None,
        logit_bias=None,
        custom_parameters={
            "json_mode": False,
        },
    )

    class Display(InlinePromptNode.Display):
        x = 3052
        y = 638
        z_index = 26
        icon = "vellum:icon:clipboard"
        color = "purple"

    class Trigger(InlinePromptNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES
