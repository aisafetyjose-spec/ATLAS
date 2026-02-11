from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.input_validator import InputValidator


class InputValidatorDisplay(BaseNodeDisplay[InputValidator]):
    node_id = UUID("fae1735f-c98a-4ecb-a42a-983c524bf451")
    attribute_ids_by_name = {
        "clinical_dictation": UUID("045ffe68-b4e7-4c3a-a44b-3af8c5462d80"),
        "note_type": UUID("3d31a07d-5677-4173-b0b4-96e52f019592"),
        "setting": UUID("220994ec-fe69-43a1-a44a-0d541160ce3a"),
        "specialty": UUID("dab32d58-b579-4e1b-8799-d4572bdc2f52"),
        "payer": UUID("604823b2-3526-48c5-bec1-a5b7be30e111"),
        "encounter_context": UUID("0289da81-9488-42bb-9639-32c27191e9c4"),
        "time_spent_minutes": UUID("0c8364d4-211a-4538-9b67-2dbb4e8d1874"),
        "phi_safe_mode": UUID("a7a25c16-b91d-4c18-9c65-73d45f2e4e65"),
        "output_language": UUID("87d03844-1f54-499a-a501-238762b4d3ef"),
        "clinician_role": UUID("9ba67196-f579-47a5-89b5-8335dccb4f7c"),
    }
    output_display = {
        InputValidator.Outputs.validation_passed: NodeOutputDisplay(
            id=UUID("e510d59a-8f6f-4933-a6ec-70e243902a71"), name="validation_passed"
        ),
        InputValidator.Outputs.error_message: NodeOutputDisplay(
            id=UUID("267b098d-7950-466b-b3e8-1f5753b40cf9"), name="error_message"
        ),
        InputValidator.Outputs.normalized_dictation: NodeOutputDisplay(
            id=UUID("63244c81-5b08-44c6-b181-aa153a9a1b68"), name="normalized_dictation"
        ),
        InputValidator.Outputs.normalized_note_type: NodeOutputDisplay(
            id=UUID("83b40304-c8aa-44a3-9e14-b37bfe23dbe9"), name="normalized_note_type"
        ),
        InputValidator.Outputs.normalized_setting: NodeOutputDisplay(
            id=UUID("aa39ae05-843d-4cfc-9d0a-fc5489982620"), name="normalized_setting"
        ),
        InputValidator.Outputs.normalized_specialty: NodeOutputDisplay(
            id=UUID("e02af9b1-c472-40d3-80ab-04e76b2f5f0b"), name="normalized_specialty"
        ),
        InputValidator.Outputs.normalized_payer: NodeOutputDisplay(
            id=UUID("531a7c7e-8205-4df6-bee4-0bb11390772d"), name="normalized_payer"
        ),
        InputValidator.Outputs.normalized_encounter_context: NodeOutputDisplay(
            id=UUID("0762d0eb-46fa-4e01-ac04-ffdabbb15c3e"), name="normalized_encounter_context"
        ),
        InputValidator.Outputs.normalized_time_spent_minutes: NodeOutputDisplay(
            id=UUID("0e73e64c-2c9c-4b4a-9971-857939152627"), name="normalized_time_spent_minutes"
        ),
        InputValidator.Outputs.phi_safe_mode: NodeOutputDisplay(
            id=UUID("a7a25c16-b91d-4c18-9c65-73d45f2e4e65"), name="phi_safe_mode"
        ),
        InputValidator.Outputs.output_language: NodeOutputDisplay(
            id=UUID("87d03844-1f54-499a-a501-238762b4d3ef"), name="output_language"
        ),
        InputValidator.Outputs.clinician_role: NodeOutputDisplay(
            id=UUID("9ba67196-f579-47a5-89b5-8335dccb4f7c"), name="clinician_role"
        ),
        InputValidator.Outputs.missing_core_elements: NodeOutputDisplay(
            id=UUID("98049bdd-a359-4ac1-a4a6-5e8d743d5eb1"), name="missing_core_elements"
        ),
        InputValidator.Outputs.compliance_context: NodeOutputDisplay(
            id=UUID("e784c396-0219-4dd9-a459-fa47a03f896f"), name="compliance_context"
        ),
        InputValidator.Outputs.phi_risk_hint: NodeOutputDisplay(
            id=UUID("3732732a-7988-42c5-a127-54059f0cd3d8"), name="phi_risk_hint"
        ),
    }
    port_displays = {
        InputValidator.Ports.default: PortDisplayOverrides(id=UUID("99083d90-59fc-4dcc-9ee4-b6c123883d15"))
    }
