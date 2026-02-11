from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.qa_check import QACheck


class QACheckDisplay(BaseNodeDisplay[QACheck]):
    node_id = UUID("bd94e252-454a-4d38-bb08-be6b40600883")
    attribute_ids_by_name = {
        "medical_note": UUID("b63175e9-97bc-4f31-a297-3278f7ee0021"),
        "cdi_queries": UUID("bff1b374-2d5f-4fa8-b9dd-158ee1cf2af6"),
        "billing_support": UUID("dcb3a587-e0e9-47e7-863d-d1bfa05ddae1"),
        "phi_safe_mode": UUID("84ea153c-2dc6-48ff-8293-92c7345c2bd1"),
        "missing_core_elements": UUID("44ba5f02-680b-4e5f-8bb6-4ba3a079fb3a"),
        "phi_risk_hint": UUID("cebeff1a-135e-4d8b-ac04-ada67cfc58f2"),
    }
    output_display = {
        QACheck.Outputs.qa_status: NodeOutputDisplay(id=UUID("f8ff10df-23aa-445a-91e0-f2159827a636"), name="qa_status"),
        QACheck.Outputs.compliance_ok: NodeOutputDisplay(
            id=UUID("777ace71-443d-43a9-95dc-d2337dab129d"), name="compliance_ok"
        ),
        QACheck.Outputs.issues: NodeOutputDisplay(id=UUID("d2803f46-e4cf-4f33-91a7-1f5ff40a85dd"), name="issues"),
        QACheck.Outputs.contradictions: NodeOutputDisplay(
            id=UUID("c0e4d441-5a73-4baa-aade-307a00e92831"), name="contradictions"
        ),
        QACheck.Outputs.missing_elements: NodeOutputDisplay(
            id=UUID("b86fd4b2-ac29-4bf6-a967-0f43b8998404"), name="missing_elements"
        ),
        QACheck.Outputs.phi_risks: NodeOutputDisplay(id=UUID("9ca0ad53-7348-4567-b4ac-dfd7d830cdd2"), name="phi_risks"),
        QACheck.Outputs.recommended_fixes: NodeOutputDisplay(
            id=UUID("f0f9a88a-cfa0-4488-8aae-ce296c03394f"), name="recommended_fixes"
        ),
        QACheck.Outputs.flagged_summary: NodeOutputDisplay(
            id=UUID("95dc4d18-5b92-4e35-98c2-0dd309ce5d60"), name="flagged_summary"
        ),
    }
    port_displays = {QACheck.Ports.default: PortDisplayOverrides(id=UUID("308f6d53-5503-4f98-a44e-b384f2b811f4"))}
