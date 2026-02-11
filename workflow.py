from vellum.workflows import BaseWorkflow
from vellum.workflows.state import BaseState

from .inputs import Inputs
from .nodes.assemble_draft import AssembleDraft
from .nodes.compliance_router import ComplianceRouter
from .nodes.document_router import DocumentRouter
from .nodes.error_output import ErrorOutput
from .nodes.extract_text_from_pdf import ExtractTextFromPDF
from .nodes.flag_issues import FlagIssues
from .nodes.generate_billing_support import GenerateBillingSupport
from .nodes.generate_cdi_queries import GenerateCDIQueries
from .nodes.generate_medical_note import GenerateMedicalNote
from .nodes.generate_pdf_report import GeneratePDFReport
from .nodes.input_validator import InputValidator
from .nodes.merge_text_source import MergeTextSource
from .nodes.qa_check import QACheck
from .nodes.validation_router import ValidationRouter


class Workflow(BaseWorkflow[Inputs, BaseState]):
    graph = (
        {
            DocumentRouter.Ports.pdf_path >> ExtractTextFromPDF,
            DocumentRouter.Ports.text_path,
        }
        >> MergeTextSource
        >> InputValidator
        >> {
            ValidationRouter.Ports.valid
            >> {
                GenerateMedicalNote,
                GenerateBillingSupport,
                GenerateCDIQueries,
            }
            >> QACheck
            >> {
                ComplianceRouter.Ports.passed,
                ComplianceRouter.Ports.failed >> FlagIssues,
            }
            >> AssembleDraft
            >> GeneratePDFReport,
            ValidationRouter.Ports.invalid >> ErrorOutput,
        }
    )

    class Outputs(BaseWorkflow.Outputs):
        response = AssembleDraft.Outputs.complete_draft
        pdf_report = GeneratePDFReport.Outputs.pdf_document
        pdf_url = GeneratePDFReport.Outputs.pdf_url
