from uuid import UUID

from vellum_ee.workflows.display.editor import NodeDisplayComment, NodeDisplayData
from vellum_ee.workflows.display.nodes import BaseInlinePromptNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.extract_text_from_pdf import ExtractTextFromPDF


class ExtractTextFromPDFDisplay(BaseInlinePromptNodeDisplay[ExtractTextFromPDF]):
    node_id = UUID("ef6ccba4-3935-42ad-a8a1-51cab6322371")
    output_id = UUID("0e31a5ee-5e9d-4152-83a9-0d740215184f")
    array_output_id = UUID("c496eba3-ec04-45f2-99a9-2cd4e2a48a28")
    target_handle_id = UUID("9d70fb6b-97cf-44aa-a210-887962dfc778")
    node_input_ids_by_name = {"prompt_inputs.document": UUID("e86b88d6-c881-4228-b01e-2dc38405bdc5")}
    attribute_ids_by_name = {
        "ml_model": UUID("8ddc7180-2673-41bb-b4fd-ce4ee39d80ad"),
        "blocks": UUID("48ea3907-60c5-4e6e-937d-3a31b766e4b6"),
        "prompt_inputs": UUID("5e220802-cf2d-4874-8eef-2c086ab02053"),
        "parameters": UUID("4fbafa8a-5a4f-4a92-8e3a-24f8184cb14f"),
        "functions": UUID("d94cc9c1-2c32-4dc7-8bf1-36ee6323ad1b"),
    }
    output_display = {
        ExtractTextFromPDF.Outputs.text: NodeOutputDisplay(
            id=UUID("0e31a5ee-5e9d-4152-83a9-0d740215184f"), name="text"
        ),
        ExtractTextFromPDF.Outputs.results: NodeOutputDisplay(
            id=UUID("c496eba3-ec04-45f2-99a9-2cd4e2a48a28"), name="results"
        ),
        ExtractTextFromPDF.Outputs.json: NodeOutputDisplay(
            id=UUID("dbcb90be-33dd-41c6-9419-c6ce8586e606"), name="json"
        ),
    }
    port_displays = {
        ExtractTextFromPDF.Ports.default: PortDisplayOverrides(id=UUID("7a7844d1-541c-4c0e-86f4-5afec9adf621"))
    }
    display_data = NodeDisplayData(
        comment=NodeDisplayComment(
            expanded=True,
            value="Extrae texto de un documento PDF usando un LLM con visión.\n\nSi se proporciona clinical_dictation directamente, lo usa sin procesar.\nSi se proporciona clinical_document (PDF), extrae el texto del documento.\n",
        )
    )
