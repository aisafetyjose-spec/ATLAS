import base64
import io
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from vellum import VellumDocument
from vellum.client.types.vellum_document import VellumDocument
from vellum.workflows import BaseNode
from vellum.workflows.types.core import MergeBehavior

from .assemble_draft import AssembleDraft


class GeneratePDFReport(BaseNode):
    complete_draft: str = AssembleDraft.Outputs.complete_draft

    class Outputs(BaseNode.Outputs):
        pdf_document: VellumDocument
        pdf_url: str

    class Trigger(BaseNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES

    class Display(BaseNode.Display):
        x = 5610
        y = 440
        z_index = 19
        icon = "vellum:icon:file-lines"
        color = "purple"

    def run(self) -> Outputs:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
        )
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Heading1"],
            fontSize=18,
            spaceAfter=20,
            textColor=colors.HexColor("#1a365d"),
            alignment=1,
        )
        header_style = ParagraphStyle(
            "CustomHeader",
            parent=styles["Heading2"],
            fontSize=14,
            spaceBefore=15,
            spaceAfter=10,
            textColor=colors.HexColor("#2c5282"),
        )
        body_style = ParagraphStyle(
            "CustomBody",
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            spaceBefore=5,
            spaceAfter=5,
        )
        story = []
        story.append(Paragraph("ATLAS™ CDI ANALYSIS REPORT", title_style))
        story.append(Spacer(1, 10))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        story.append(Paragraph(f"<b>Generated:</b> {timestamp}", body_style))
        story.append(Spacer(1, 20))
        sections = self._parse_sections(self.complete_draft)
        for section_title, section_content in sections:
            if section_title:
                story.append(Paragraph(section_title, header_style))
            cleaned_content = self._clean_content(section_content)
            for line in cleaned_content.split("\n"):
                if line.strip():
                    safe_line = (
                        line.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                    )
                    story.append(Paragraph(safe_line, body_style))
            story.append(Spacer(1, 10))
        doc.build(story)
        pdf_bytes = buffer.getvalue()
        buffer.close()
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_data_url = f"data:application/pdf;base64,{pdf_base64}"
        pdf_doc = VellumDocument(
            src=pdf_data_url,
            metadata={
                "filename": f"ATLAS_CDI_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            },
        )
        uploaded_doc = pdf_doc.upload(vellum_client=self._context.vellum_client)
        pdf_url = uploaded_doc.get_signed_url(vellum_client=self._context.vellum_client)
        return self.Outputs(pdf_document=uploaded_doc, pdf_url=pdf_url)

    def _parse_sections(self, content: str) -> list[tuple[str, str]]:
        """Parse the draft into sections."""
        sections = []
        current_title = ""
        current_content = []
        for line in content.split("\n"):
            if (
                line.startswith("📋")
                or line.startswith("📝")
                or line.startswith("❓")
                or line.startswith("💼")
                or line.startswith("���")
                or line.startswith("⚠️")
            ):
                if current_content:
                    sections.append((current_title, "\n".join(current_content)))
                current_title = line.strip()
                current_content = []
            elif "=" * 10 in line:
                continue
            else:
                current_content.append(line)
        if current_content:
            sections.append((current_title, "\n".join(current_content)))
        return sections

    def _clean_content(self, content: str) -> str:
        """Clean content for PDF rendering."""
        lines = [line.rstrip() for line in content.split("\n")]
        cleaned = []
        prev_empty = False
        for line in lines:
            if not line.strip():
                if not prev_empty:
                    cleaned.append("")
                prev_empty = True
            else:
                cleaned.append(line)
                prev_empty = False
        return "\n".join(cleaned)
