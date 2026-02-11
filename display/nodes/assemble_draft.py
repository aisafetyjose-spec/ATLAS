from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.assemble_draft import AssembleDraft


class AssembleDraftDisplay(BaseNodeDisplay[AssembleDraft]):
    node_id = UUID("d9e7d3ac-c563-4fa5-aae5-f49f35bf3cc5")
    attribute_ids_by_name = {
        "note_type": UUID("82cfe357-b85d-4d67-bded-7ce499b4c025"),
        "setting": UUID("3ea08f98-ae73-40f9-b55d-c8b21e30b5d7"),
        "specialty": UUID("03999861-1fbc-4d1c-864b-f42080378c8c"),
        "payer": UUID("78edb923-4c1b-4247-90ac-fd981760958c"),
        "output_language": UUID("1ffc7fc5-bf84-41ef-bbdb-5f5232ef6443"),
        "phi_safe_mode": UUID("206dcea7-ffd0-493b-8045-a15db89ecd87"),
        "medical_note": UUID("0d5f4995-1ce0-46f2-a61c-712d48a440bb"),
        "cdi_queries": UUID("8158e1a4-229b-4a37-9ffa-c64086dd22a1"),
        "billing_support": UUID("f27298b3-f634-4a8d-96c8-6e1f7babe971"),
        "qa_status": UUID("b07ebc81-2c5c-4c98-860f-7709f76c0d62"),
        "compliance_ok": UUID("0a0bbf0e-ebc4-4d59-b406-abe6bc652580"),
        "flagged_summary": UUID("c0dabba9-4473-4ef1-801a-124790312acf"),
        "flag_banner": UUID("6a491ec7-c083-469d-876f-99de8ed4d148"),
    }
    output_display = {
        AssembleDraft.Outputs.complete_draft: NodeOutputDisplay(
            id=UUID("7a8c89a3-a83d-4a54-beaa-68cf67347449"), name="complete_draft"
        ),
        AssembleDraft.Outputs.ready_for_review: NodeOutputDisplay(
            id=UUID("b710b62a-358c-478a-9ef7-e852757bab79"), name="ready_for_review"
        ),
    }
    port_displays = {AssembleDraft.Ports.default: PortDisplayOverrides(id=UUID("1585b756-1fdc-4180-adbd-944196f3b135"))}
