from vellum import ChatMessagePromptBlock, JinjaPromptBlock, PromptParameters
from vellum.workflows.nodes.displayable import InlinePromptNode
from vellum.workflows.types.core import MergeBehavior

from .input_validator import InputValidator


class GenerateBillingSupport(InlinePromptNode):
    """Generates billing SUPPORT documentation (MDM/Time) - NOT coding.

    CRITICAL RULES:
    - This is DOCUMENTATION SUPPORT only - NOT coding
    - NEVER suggest CPT or ICD codes
    - NEVER inflate severity or complexity
    - If time not declared, state "Not provided by clinician"
    - Document ONLY what is explicitly stated
    """

    ml_model = "claude-sonnet-4-5-20250929"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                JinjaPromptBlock(
                    template="""\
You are ATLAS™ Billing Documentation Specialist. Generate billing SUPPORT documentation only.

{{ compliance_context }}

=== CLINICAL DICTATION ===
{{ dictation }}

=== CONTEXT ===
Clinician Role: {{ clinician_role }}
Time Declared by Clinician: {% if time_minutes %}{{ time_minutes }} minutes{% else %}NOT PROVIDED - DO NOT INVENT{% endif %}
Payer: {{ payer }}
Setting: {{ setting }}

=== CRITICAL RULES ===
1. This is DOCUMENTATION SUPPORT only - NOT coding
2. NEVER suggest CPT or ICD codes
3. NEVER inflate severity or complexity
4. If time not declared, state \"Time: Not provided by clinician\"
5. Document ONLY what is explicitly stated
6. Focus on medical necessity through accurate documentation

=== OUTPUT SECTIONS ===

**1. MEDICAL NECESSITY SUMMARY**
- Why the encounter was needed (from dictation)
- Clinical rationale for services provided
- Evidence quotes supporting necessity

**2. MDM SUMMARY (Medical Decision Making)**
Based ONLY on what is documented:

*Problems Addressed:*
- [Problem 1] - [Complexity indicator if evident]
- [Problem 2] - [Complexity indicator if evident]
(ONLY from dictation - do not invent)

*Data Reviewed/Ordered:*
- Labs: [if documented, else \"Not documented\"]
- Imaging: [if documented, else \"Not documented\"]
- Records: [if documented, else \"Not documented\"]
- Tests ordered: [if documented, else \"Not documented\"]

*Risk Assessment:*
- Medications: [changes/new Rx if documented]
- Procedures: [if documented]
- Comorbidities impacting care: [if documented]

**3. TIME STATEMENT**
{% if time_minutes %}
- Total time on date of encounter: {{ time_minutes }} minutes (clinician-declared)
- Typical activities included: review of records, examination, counseling, care coordination, documentation
{% else %}
- Time: NOT PROVIDED/DECLARED BY CLINICIAN
- Note: If time-based E/M is intended, clinician must document total minutes spent
{% endif %}

**4. DOCUMENTATION CHECKLIST (CMS/Medicare/Medicaid Alignment)**
- [ ] Chief complaint documented
- [ ] Medical necessity established
- [ ] Assessment linked to plan
- [ ] Each plan item tied to a problem
- [ ] Follow-up specified
- [ ] Return precautions documented (if applicable)
- [ ] Medications reconciled (if applicable)

**5. DOCUMENTATION GAPS/RISKS**
- [List any gaps that could affect documentation integrity]
- [Note any areas needing clinician clarification]

**EVIDENCE QUOTES** (2-3 quotes from dictation supporting billing documentation):
1. \"[quote]\"
2. \"[quote]\"

Output in {{ language }} language.\
"""
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[
                JinjaPromptBlock(template="""Generate billing support documentation now based on the dictation.""")
            ],
        ),
    ]
    prompt_inputs = {
        "compliance_context": InputValidator.Outputs.compliance_context,
        "dictation": InputValidator.Outputs.normalized_dictation,
        "clinician_role": InputValidator.Outputs.clinician_role,
        "time_minutes": InputValidator.Outputs.normalized_time_spent_minutes,
        "payer": InputValidator.Outputs.normalized_payer,
        "setting": InputValidator.Outputs.normalized_setting,
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
        y = 210
        z_index = 28
        icon = "vellum:icon:file-lines"
        color = "gold"

    class Trigger(InlinePromptNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES
