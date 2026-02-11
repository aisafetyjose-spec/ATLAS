from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.merge_text_source import MergeTextSource


class MergeTextSourceDisplay(BaseNodeDisplay[MergeTextSource]):
    node_id = UUID("246c2fe6-98e2-4770-bbb4-40452305cfee")
    attribute_ids_by_name = {
        "pdf_text": UUID("16e9990c-7ff3-4d87-bf91-68d9d6724682"),
        "direct_text": UUID("ee6548aa-6c3b-4f3a-8102-5e8660d4f6d2"),
        "has_pdf": UUID("9a0e3c14-f7c1-4ed3-b733-d23f58c530c9"),
    }
    output_display = {
        MergeTextSource.Outputs.clinical_text: NodeOutputDisplay(
            id=UUID("e26fed27-c0e3-46b7-a59b-e5a4d16f9e47"), name="clinical_text"
        )
    }
    port_displays = {
        MergeTextSource.Ports.default: PortDisplayOverrides(id=UUID("fd0087c5-73ea-45c7-b79f-0253dd4c3595"))
    }
