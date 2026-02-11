from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayComment, NodeDisplayData
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.generate_cdi_queries import GenerateCDIQueries


class GenerateCDIQueriesDisplay(BaseInlinePromptNodeDisplay[GenerateCDIQueries]):
    node_id = UUID("f4edef18-f31e-479f-854c-6521e3a84d66")
    output_id = UUID("c7c76d48-c222-45bf-82c5-5bce49ad76fa")
    array_output_id = UUID("8cdafd32-2bee-4ff6-908d-cc71ca6f4f8d")
    target_handle_id = UUID("593749b3-38d0-4330-bddc-709143a79ea9")
    node_input_ids_by_name = {
        "prompt_inputs.compliance_context": UUID("5a17e0c0-601a-429b-8665-7ac1c40477a3"),
        "prompt_inputs.dictation": UUID("00623349-d8e5-41af-b20c-e22676637fa9"),
        "prompt_inputs.setting": UUID("078bb771-0ba4-4a1d-84b3-810cde15f55b"),
        "prompt_inputs.payer": UUID("afb26d0e-164e-42b7-adc7-9909432cdf39"),
        "prompt_inputs.missing_elements": UUID("5fc9428a-0737-4f7d-95df-3c59b639e474"),
        "prompt_inputs.time_minutes": UUID("0040d408-c97c-473a-a114-06aef9e8fc54"),
        "prompt_inputs.language": UUID("53a08df4-bd57-4ac9-810d-1aa05732acfa"),
    }
    attribute_ids_by_name = {
        "ml_model": UUID("8471b621-fb97-4890-9c14-dd374c56816c"),
        "blocks": UUID("721a4697-2e99-4fed-9ca4-62197f367bb3"),
        "prompt_inputs": UUID("583ae8de-6dea-4a21-bec9-22480d62f195"),
        "parameters": UUID("ddd3c776-100e-4db8-9584-b8d63f686f1f"),
        "functions": UUID("1e7db995-23b6-403d-a8d8-8e16cd2893b8"),
    }
    output_display = {
        GenerateCDIQueries.Outputs.text: NodeOutputDisplay(
            id=UUID("c7c76d48-c222-45bf-82c5-5bce49ad76fa"), name="text"
        ),
        GenerateCDIQueries.Outputs.results: NodeOutputDisplay(
            id=UUID("8cdafd32-2bee-4ff6-908d-cc71ca6f4f8d"), name="results"
        ),
        GenerateCDIQueries.Outputs.json: NodeOutputDisplay(
            id=UUID("7ef0222c-539a-4a11-b2d6-11f9d427c217"), name="json"
        ),
    }
    port_displays = {
        GenerateCDIQueries.Ports.default: PortDisplayOverrides(id=UUID("34f7d4fa-6422-4456-be7c-51e4d7682d11"))
    }
    display_data = NodeDisplayData(
        comment=NodeDisplayComment(
            expanded=True,
            value="Generates CDI (Clinical Documentation Integrity) queries.\n\nCRITICAL RULES:\n- Queries must be NEUTRAL and NON-LEADING\n- Focus on clinical specificity, NOT billing optimization\n- Never suggest diagnoses - only ask for clarification\n- Include evidence from dictation for each query\n",
        )
    )
