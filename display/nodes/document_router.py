from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.document_router import DocumentRouter


class DocumentRouterDisplay(BaseNodeDisplay[DocumentRouter]):
    node_id = UUID("efdc8553-191d-4172-82f8-9b72fd26d7a6")
    attribute_ids_by_name = {
        "clinical_document": UUID("59ebac22-251c-4ef8-8c2e-88920be72e85"),
        "clinical_dictation": UUID("9aa749b8-0c47-4db0-b1a7-5572c66c7125"),
    }
    output_display = {
        DocumentRouter.Outputs.has_pdf: NodeOutputDisplay(
            id=UUID("7db81055-9d50-4a83-81d2-df6d43bf4c54"), name="has_pdf"
        ),
        DocumentRouter.Outputs.direct_text: NodeOutputDisplay(
            id=UUID("bead77f2-6754-4ae1-97c2-c8072293182d"), name="direct_text"
        ),
    }
    port_displays = {
        DocumentRouter.Ports.pdf_path: PortDisplayOverrides(id=UUID("0cd1d2f5-9713-4f8f-b019-7ea9dd325e0b")),
        DocumentRouter.Ports.text_path: PortDisplayOverrides(id=UUID("a2562a5d-f494-44f4-b6e1-77a1571acc21")),
    }
