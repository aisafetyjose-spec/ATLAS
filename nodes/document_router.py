from typing import Optional

from vellum import VellumDocument
from vellum.workflows import BaseNode, Port
from vellum.workflows.ports import Port

from ..inputs import Inputs


class DocumentRouter(BaseNode):
    clinical_document: Optional[VellumDocument] = Inputs.clinical_document
    clinical_dictation: Optional[str] = Inputs.clinical_dictation

    class Outputs(BaseNode.Outputs):
        has_pdf: bool
        direct_text: str

    class Ports(BaseNode.Ports):
        pdf_path = Port.on_if(Inputs.clinical_document.is_not_null())
        text_path = Port.on_else()

    class Display(BaseNode.Display):
        x = 436
        y = 333
        z_index = 20
        icon = "vellum:icon:arrows-split-up-and-left"
        color = "purple"

    def run(self) -> Outputs:
        has_pdf = self.clinical_document is not None
        direct_text = (self.clinical_dictation or "").strip() if not has_pdf else ""
        return self.Outputs(has_pdf=has_pdf, direct_text=direct_text)
