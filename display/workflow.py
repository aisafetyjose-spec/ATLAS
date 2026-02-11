from uuid import UUID

from vellum_ee.workflows.display.base import (
    EdgeDisplay,
    EntrypointDisplay,
    WorkflowInputsDisplay,
    WorkflowMetaDisplay,
    WorkflowOutputDisplay,
)
from vellum_ee.workflows.display.editor import NodeDisplayData, NodeDisplayPosition
from vellum_ee.workflows.display.workflows import BaseWorkflowDisplay

from ..inputs import Inputs
from ..nodes.assemble_draft import AssembleDraft
from ..nodes.compliance_router import ComplianceRouter
from ..nodes.document_router import DocumentRouter
from ..nodes.error_output import ErrorOutput
from ..nodes.extract_text_from_pdf import ExtractTextFromPDF
from ..nodes.flag_issues import FlagIssues
from ..nodes.generate_billing_support import GenerateBillingSupport
from ..nodes.generate_cdi_queries import GenerateCDIQueries
from ..nodes.generate_medical_note import GenerateMedicalNote
from ..nodes.generate_pdf_report import GeneratePDFReport
from ..nodes.input_validator import InputValidator
from ..nodes.merge_text_source import MergeTextSource
from ..nodes.qa_check import QACheck
from ..nodes.validation_router import ValidationRouter
from ..workflow import Workflow


class WorkflowDisplay(BaseWorkflowDisplay[Workflow]):
    workflow_display = WorkflowMetaDisplay(
        entrypoint_node_id=UUID("63884a7b-c01c-4cbc-b8d4-abe0a8796f6b"),
        entrypoint_node_source_handle_id=UUID("eba8fd73-57ab-4d7b-8f75-b54dbe5fc8ba"),
        entrypoint_node_display=NodeDisplayData(position=NodeDisplayPosition(x=-30, y=333), z_index=18),
    )
    inputs_display = {
        Inputs.clinical_document: WorkflowInputsDisplay(
            id=UUID("efa96b84-5983-4e2a-a642-44d123fc4c78"), name="clinical_document"
        ),
        Inputs.clinical_dictation: WorkflowInputsDisplay(
            id=UUID("a32f0228-e225-4a3c-93be-c078b4b6f800"), name="clinical_dictation"
        ),
        Inputs.note_type: WorkflowInputsDisplay(id=UUID("e4d86e20-30a0-4c4f-9489-6c492c36f2db"), name="note_type"),
        Inputs.setting: WorkflowInputsDisplay(id=UUID("eb000099-f983-4b6c-b89c-df5d3e75e439"), name="setting"),
        Inputs.specialty: WorkflowInputsDisplay(id=UUID("98bbaa4d-bdaa-4141-9c73-c40efa96e7c3"), name="specialty"),
        Inputs.payer: WorkflowInputsDisplay(id=UUID("47bb14ad-eaf6-4819-b62c-f676dceb1b6f"), name="payer"),
        Inputs.encounter_context: WorkflowInputsDisplay(
            id=UUID("16691a2b-2ba8-49c8-857d-71797cab2146"), name="encounter_context"
        ),
        Inputs.time_spent_minutes: WorkflowInputsDisplay(
            id=UUID("a66d355c-8b3a-4147-b0ee-6ceda94ab9a7"), name="time_spent_minutes"
        ),
        Inputs.phi_safe_mode: WorkflowInputsDisplay(
            id=UUID("89b1ce6d-3575-4d0c-8ded-e18655d55e26"), name="phi_safe_mode"
        ),
        Inputs.output_language: WorkflowInputsDisplay(
            id=UUID("3b7e0765-0e91-442d-bd3d-4483e7ecb54d"), name="output_language"
        ),
        Inputs.clinician_role: WorkflowInputsDisplay(
            id=UUID("6b9fe420-c511-447d-97a5-10f23500c91a"), name="clinician_role"
        ),
    }
    entrypoint_displays = {
        DocumentRouter: EntrypointDisplay(
            id=UUID("63884a7b-c01c-4cbc-b8d4-abe0a8796f6b"),
            edge_display=EdgeDisplay(id=UUID("8e12b9d1-2252-40db-bb7b-c32335a5ba57")),
        )
    }
    edge_displays = {
        (DocumentRouter.Ports.pdf_path, ExtractTextFromPDF): EdgeDisplay(
            id=UUID("e45b0dff-e64f-408f-b805-45763fb72391"), z_index=1
        ),
        (DocumentRouter.Ports.text_path, MergeTextSource): EdgeDisplay(
            id=UUID("ed3e12dd-b9bf-47a5-aa38-22d4d4a0bc3a"), z_index=2
        ),
        (ExtractTextFromPDF.Ports.default, MergeTextSource): EdgeDisplay(
            id=UUID("7e6d206c-72b6-4ada-b492-67aa389e8315"), z_index=3
        ),
        (MergeTextSource.Ports.default, InputValidator): EdgeDisplay(
            id=UUID("be22bf23-aeb4-4784-891e-f1a371bc7db8"), z_index=4
        ),
        (InputValidator.Ports.default, ValidationRouter): EdgeDisplay(
            id=UUID("011eb565-5426-410e-b532-3882d2a4f466"), z_index=5
        ),
        (ValidationRouter.Ports.valid, GenerateMedicalNote): EdgeDisplay(
            id=UUID("ee1f9563-28ba-40c8-a0b3-fd7df9db45c4"), z_index=6
        ),
        (ValidationRouter.Ports.valid, GenerateBillingSupport): EdgeDisplay(
            id=UUID("da4aa989-932b-46e6-b2f5-3e0b1cbfff94"), z_index=7
        ),
        (ValidationRouter.Ports.valid, GenerateCDIQueries): EdgeDisplay(
            id=UUID("56006082-e84f-465f-9922-e05c7f8b2c4e"), z_index=8
        ),
        (GenerateBillingSupport.Ports.default, QACheck): EdgeDisplay(
            id=UUID("843d138e-4f95-47c7-a8d2-8d38f8ef4e6d"), z_index=9
        ),
        (GenerateMedicalNote.Ports.default, QACheck): EdgeDisplay(
            id=UUID("50df1b88-78f6-4380-93e2-84056714fe7d"), z_index=10
        ),
        (GenerateCDIQueries.Ports.default, QACheck): EdgeDisplay(
            id=UUID("87c77518-b597-4b7a-9690-5806bab29b7a"), z_index=11
        ),
        (QACheck.Ports.default, ComplianceRouter): EdgeDisplay(
            id=UUID("52077ca0-3bc8-4450-9706-dcfdbfdaf407"), z_index=12
        ),
        (ComplianceRouter.Ports.failed, FlagIssues): EdgeDisplay(
            id=UUID("5c516f6a-7b37-4ecf-8cdd-dadea92a05e4"), z_index=13
        ),
        (ComplianceRouter.Ports.passed, AssembleDraft): EdgeDisplay(
            id=UUID("b5c10a6e-bbc0-4502-aede-6c6b04ce5c0c"), z_index=14
        ),
        (FlagIssues.Ports.default, AssembleDraft): EdgeDisplay(
            id=UUID("763af18e-8722-4357-9db7-39cdd3b54d13"), z_index=15
        ),
        (AssembleDraft.Ports.default, GeneratePDFReport): EdgeDisplay(
            id=UUID("8a3723f8-2a24-438e-b019-720d5d8ee51a"), z_index=16
        ),
        (ValidationRouter.Ports.invalid, ErrorOutput): EdgeDisplay(
            id=UUID("21fa4d09-c7e2-4ad6-a35f-91635db7fbb3"), z_index=17
        ),
    }
    output_displays = {
        Workflow.Outputs.response: WorkflowOutputDisplay(
            id=UUID("6e81b6d7-e90d-4593-8082-2dd0b655f255"), name="response"
        ),
        Workflow.Outputs.pdf_report: WorkflowOutputDisplay(
            id=UUID("b5498d15-7934-4a4b-9cce-158a94d4928a"), name="pdf_report"
        ),
        Workflow.Outputs.pdf_url: WorkflowOutputDisplay(
            id=UUID("62310c52-656e-41ce-8966-d8664665a705"), name="pdf_url"
        ),
    }
