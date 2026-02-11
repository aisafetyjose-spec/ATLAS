from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayComment, NodeDisplayData
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.generate_billing_support import GenerateBillingSupport


class GenerateBillingSupportDisplay(BaseInlinePromptNodeDisplay[GenerateBillingSupport]):
    node_id = UUID("426d22b7-098a-4819-8757-21d03e1cd6b7")
    output_id = UUID("0c19c4ee-7f5c-4613-b9bd-3c8b2c4a0409")
    array_output_id = UUID("011b66b4-e13f-4bdf-bdbc-bda8bc087d50")
    target_handle_id = UUID("a8360896-7f79-4c33-972a-97cd7b31c1f0")
    node_input_ids_by_name = {
        "prompt_inputs.compliance_context": UUID("3e187ac0-3533-4df6-a7cb-724ab0a0581a"),
        "prompt_inputs.dictation": UUID("a9bb59a7-3ed5-4998-bb62-6cb851cd5b71"),
        "prompt_inputs.clinician_role": UUID("42a9eee3-241c-4484-a690-de7b106bcabd"),
        "prompt_inputs.time_minutes": UUID("e77645be-96ba-4193-a679-07f8b572e505"),
        "prompt_inputs.payer": UUID("83931c2e-7d3a-4980-a60a-273cd8571880"),
        "prompt_inputs.setting": UUID("b753ac1c-f76a-428d-9833-788ef72ef498"),
        "prompt_inputs.language": UUID("8fdb4a62-8b42-4274-999b-f615fc89c2e7"),
    }
    attribute_ids_by_name = {
        "ml_model": UUID("a522f137-1c2c-41c1-9af8-152455d80cfe"),
        "blocks": UUID("034d5681-def8-4ef5-aed5-f772350f1e65"),
        "prompt_inputs": UUID("ec787776-a1e6-4bc9-bf65-efec0b8c78ed"),
        "parameters": UUID("61f50fae-5df8-400d-bc92-086a735c350e"),
        "functions": UUID("21e6d325-6439-460c-b196-80abe7d5ab90"),
    }
    output_display = {
        GenerateBillingSupport.Outputs.text: NodeOutputDisplay(
            id=UUID("0c19c4ee-7f5c-4613-b9bd-3c8b2c4a0409"), name="text"
        ),
        GenerateBillingSupport.Outputs.results: NodeOutputDisplay(
            id=UUID("011b66b4-e13f-4bdf-bdbc-bda8bc087d50"), name="results"
        ),
        GenerateBillingSupport.Outputs.json: NodeOutputDisplay(
            id=UUID("a9dd2b3e-87c4-4ffe-af10-70797218a194"), name="json"
        ),
    }
    port_displays = {
        GenerateBillingSupport.Ports.default: PortDisplayOverrides(id=UUID("eb02d1ea-beee-4ba3-8fcc-a9a4b144c80b"))
    }
    display_data = NodeDisplayData(
        comment=NodeDisplayComment(
            expanded=True,
            value='Generates billing SUPPORT documentation (MDM/Time) - NOT coding.\n\nCRITICAL RULES:\n- This is DOCUMENTATION SUPPORT only - NOT coding\n- NEVER suggest CPT or ICD codes\n- NEVER inflate severity or complexity\n- If time not declared, state "Not provided by clinician"\n- Document ONLY what is explicitly stated\n',
        )
    )
