from typing import Optional

from vellum.workflows import BaseNode
from vellum.workflows.types.core import MergeBehavior

from .document_router import DocumentRouter
from .extract_text_from_pdf import ExtractTextFromPDF


class MergeTextSource(BaseNode):
    pdf_text: Optional[str] = ExtractTextFromPDF.Outputs.text.coalesce("")
    direct_text: str = DocumentRouter.Outputs.direct_text
    has_pdf: bool = DocumentRouter.Outputs.has_pdf

    class Outputs(BaseNode.Outputs):
        clinical_text: str

    class Trigger(BaseNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ANY

    class Display(BaseNode.Display):
        x = 1494
        y = 333
        z_index = 21
        icon = "vellum:icon:merge"
        color = "teal"

    def run(self) -> Outputs:
        if self.has_pdf and self.pdf_text:
            return self.Outputs(clinical_text=self.pdf_text)
        return self.Outputs(clinical_text=self.direct_text)
