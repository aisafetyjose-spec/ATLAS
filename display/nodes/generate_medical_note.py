from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayComment, NodeDisplayData
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.generate_medical_note import GenerateMedicalNote


class GenerateMedicalNoteDisplay(BaseInlinePromptNodeDisplay[GenerateMedicalNote]):
    node_id = UUID("65c93a3c-add2-4199-9fa0-4323ad122cba")
    output_id = UUID("88c7d2da-cbb8-4138-add8-c7dbda7732e2")
    array_output_id = UUID("8652af48-9f6a-4cb6-bc2d-62194091bb1e")
    target_handle_id = UUID("739b0bde-3b28-482d-9589-3f9f88f4f4f5")
    node_input_ids_by_name = {
        "prompt_inputs.compliance_context": UUID("c23067b8-d2ae-4989-ac43-e5f88e3bcb45"),
        "prompt_inputs.dictation": UUID("e7b12daf-f0fb-44ba-815c-9dfa2f3ffa29"),
        "prompt_inputs.note_type": UUID("80f6868b-66a4-4c85-bf79-c98f464e842a"),
        "prompt_inputs.encounter_context": UUID("172acf69-943e-4608-b496-5a55dbacd6fe"),
        "prompt_inputs.time_minutes": UUID("ce4ce719-69ef-4560-9123-d34ecfddb80c"),
        "prompt_inputs.language": UUID("a1aab1e8-0a33-4147-8cc0-d821e0a234ad"),
    }
    attribute_ids_by_name = {
        "ml_model": UUID("1966b2c9-025a-4e32-a7ab-fc1a059408c8"),
        "blocks": UUID("efe47202-9cc5-4f83-93f9-ed18c82d613b"),
        "prompt_inputs": UUID("1b92b90d-686e-4111-9347-93691bad7e74"),
        "parameters": UUID("92c991a1-4924-4adc-ac90-f10b24683e7d"),
        "functions": UUID("4d484b53-8255-4781-abea-e82e183f9c7b"),
    }
    output_display = {
        GenerateMedicalNote.Outputs.text: NodeOutputDisplay(
            id=UUID("88c7d2da-cbb8-4138-add8-c7dbda7732e2"), name="text"
        ),
        GenerateMedicalNote.Outputs.results: NodeOutputDisplay(
            id=UUID("8652af48-9f6a-4cb6-bc2d-62194091bb1e"), name="results"
        ),
        GenerateMedicalNote.Outputs.json: NodeOutputDisplay(
            id=UUID("3185679a-17b8-460e-ad81-b48d83fa77e9"), name="json"
        ),
    }
    port_displays = {
        GenerateMedicalNote.Ports.default: PortDisplayOverrides(id=UUID("d5d2b56e-750f-48e0-bffa-3ee1eb709a38"))
    }
    display_data = NodeDisplayData(
        comment=NodeDisplayComment(
            expanded=True,
            value='Generates complete, audit-ready medical note from clinical dictation.\n\nCRITICAL RULES:\n- NEVER invent data not in dictation\n- Mark missing as "Not documented/provided"\n- Include evidence quotes from dictation\n- Generate clinician clarifications for ambiguity\n',
        )
    )
