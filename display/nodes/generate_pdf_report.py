from uuid import UUID

from vellum_ee.workflows.display.nodes import BaseNodeDisplay
from vellum_ee.workflows.display.nodes.types import NodeOutputDisplay, PortDisplayOverrides

from ...nodes.generate_pdf_report import GeneratePDFReport


class GeneratePDFReportDisplay(BaseNodeDisplay[GeneratePDFReport]):
    node_id = UUID("a3b697a8-30c1-4acb-be0f-56e33c787c3f")
    attribute_ids_by_name = {"complete_draft": UUID("8ab80cfe-5891-44d0-a216-6d269e374bc6")}
    output_display = {
        GeneratePDFReport.Outputs.pdf_document: NodeOutputDisplay(
            id=UUID("fb781db2-3b70-48c0-b72d-6b7eac2c45c4"), name="pdf_document"
        ),
        GeneratePDFReport.Outputs.pdf_url: NodeOutputDisplay(
            id=UUID("ea16bf61-0bef-486c-8b15-621463608464"), name="pdf_url"
        ),
    }
    port_displays = {
        GeneratePDFReport.Ports.default: PortDisplayOverrides(id=UUID("1e1ca7a0-fcdc-4fc7-ba7e-31c97919240b"))
    }
