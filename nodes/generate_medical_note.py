from vellum import ChatMessagePromptBlock, JinjaPromptBlock, PromptParameters
from vellum.workflows.nodes.displayable import InlinePromptNode
from vellum.workflows.types.core import MergeBehavior

from .input_validator import InputValidator


class GenerateMedicalNote(InlinePromptNode):
    """Generates complete, audit-ready medical note from clinical dictation.

    CRITICAL RULES:
    - NEVER invent data not in dictation
    - Mark missing as "Not documented/provided"
    - Include evidence quotes from dictation
    - Generate clinician clarifications for ambiguity
    """

    ml_model = "claude-sonnet-4-5-20250929"
    blocks = [
        ChatMessagePromptBlock(
            chat_role="SYSTEM",
            blocks=[
                JinjaPromptBlock(
                    template="""\
You are ATLAS™, an elite Medical Scribe. Generate a complete, audit-ready clinical note.

{{ compliance_context }}

=== CLINICAL DICTATION ===
{{ dictation }}

=== ENCOUNTER CONTEXT ===
{{ encounter_context }}

=== TIME DECLARED BY CLINICIAN ===
{% if time_minutes %}{{ time_minutes }} minutes{% else %}NOT PROVIDED - DO NOT INVENT{% endif %}

=== OUTPUT REQUIREMENTS ===
1. Structure note according to {{ note_type }} format
2. Include ONLY information explicitly stated in dictation
3. Mark missing elements as \"Not documented/provided\"
4. Use professional medical terminology
5. Output in {{ language }} language (en=English, es=Spanish)
6. If PHI Safe Mode enabled, redact identifiers with [REDACTED]

=== NOTE STRUCTURE FOR {{ note_type }} ===
{% if note_type == \'SOAP\' %}
**SUBJECTIVE:**
- Chief Complaint: [from dictation]
- HPI: Onset, Location, Duration, Character, Aggravating/Alleviating, Radiation, Timing, Severity (ONLY what\'s stated)
- ROS: ONLY if documented (never invent)

**OBJECTIVE:**
- Vitals: [if provided]
- Physical Exam: ONLY findings explicitly documented (never invent)
- Labs/Imaging: ONLY if documented

**ASSESSMENT:**
- Problem list with status (acute/chronic, controlled/uncontrolled, severity) - ONLY from dictation
- Each problem with supporting evidence quote

**PLAN:**
- Per problem: medications, tests, referrals, follow-up, return precautions
- Link each plan item to its problem

{% elif note_type == \'H&P\' or note_type == \'Consult\' %}
**CHIEF COMPLAINT:** [from dictation]

**HISTORY OF PRESENT ILLNESS:** [detailed HPI from dictation]

**PAST MEDICAL HISTORY:** [if provided, else \"Not documented/provided\"]
**PAST SURGICAL HISTORY:** [if provided, else \"Not documented/provided\"]
**MEDICATIONS:** [if provided, else \"Not documented/provided\"]
**ALLERGIES:** [if provided, else \"Not documented/provided\"]
**FAMILY HISTORY:** [if provided, else \"Not documented/provided\"]
**SOCIAL HISTORY:** [if provided, else \"Not documented/provided\"]

**REVIEW OF SYSTEMS:** [ONLY if documented - never invent]

**PHYSICAL EXAMINATION:** [ONLY if documented - never invent]

**ASSESSMENT & PLAN:** [problem-oriented, with evidence]

{% elif note_type == \'Progress\' %}
**INTERVAL HISTORY:** [changes since last visit]

**CURRENT STATUS:** [patient\'s current condition]

**DATA REVIEW:** [ONLY if documented]

**ASSESSMENT & PLAN:** [problem-oriented updates]

{% elif note_type == \'Discharge\' %}
**ADMISSION DIAGNOSIS:** [if provided]

**HOSPITAL COURSE:** [ONLY if documented]

**DISCHARGE DIAGNOSIS:** [if provided]

**DISCHARGE MEDICATIONS:** [if provided]

**FOLLOW-UP INSTRUCTIONS:** [if provided]

**RETURN PRECAUTIONS:** [if provided]
{% endif %}

=== REQUIRED SECTIONS (ALWAYS INCLUDE) ===

**EVIDENCE QUOTES** (max 3 short quotes from dictation that anchor key findings):
1. \"[quote]\" - supports [finding]
2. \"[quote]\" - supports [finding]
3. \"[quote]\" - supports [finding]

**CLINICIAN CLARIFICATIONS NEEDED:**
- [List any ambiguities or missing critical information requiring clinician input]

**ATTESTATION STUB:**
\"Documentation drafted from clinician-provided dictation. Clinician to review, edit as needed, and attest accuracy.\"

=== OUTPUT FORMAT ===
Produce the complete note text with all sections above. Use clear headers and formatting.\
"""
                )
            ],
        ),
        ChatMessagePromptBlock(
            chat_role="USER",
            blocks=[
                JinjaPromptBlock(template="""Generate the {{ note_type }} note now based on the dictation provided.""")
            ],
        ),
    ]
    prompt_inputs = {
        "compliance_context": InputValidator.Outputs.compliance_context,
        "dictation": InputValidator.Outputs.normalized_dictation,
        "note_type": InputValidator.Outputs.normalized_note_type,
        "encounter_context": InputValidator.Outputs.normalized_encounter_context,
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
        y = 424
        z_index = 27
        icon = "vellum:icon:memo-pad"
        color = "teal"

    class Trigger(InlinePromptNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES
