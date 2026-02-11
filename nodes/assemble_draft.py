from typing import Any, Optional

from vellum.workflows import BaseNode
from vellum.workflows.types.core import MergeBehavior

from .flag_issues import FlagIssues
from .generate_billing_support import GenerateBillingSupport
from .generate_cdi_queries import GenerateCDIQueries
from .generate_medical_note import GenerateMedicalNote
from .input_validator import InputValidator
from .qa_check import QACheck


class AssembleDraft(BaseNode):
    note_type: str = InputValidator.Outputs.normalized_note_type
    setting: str = InputValidator.Outputs.normalized_setting
    specialty: str = InputValidator.Outputs.normalized_specialty
    payer: str = InputValidator.Outputs.normalized_payer
    output_language: str = InputValidator.Outputs.output_language
    phi_safe_mode: bool = InputValidator.Outputs.phi_safe_mode
    medical_note: str = GenerateMedicalNote.Outputs.text
    cdi_queries: str = GenerateCDIQueries.Outputs.text
    billing_support: str = GenerateBillingSupport.Outputs.text
    qa_status: str = QACheck.Outputs.qa_status
    compliance_ok: bool = QACheck.Outputs.compliance_ok
    flagged_summary: str = QACheck.Outputs.flagged_summary
    flag_banner: Optional[str] = FlagIssues.Outputs.flag_banner.coalesce("")

    class Outputs(BaseNode.Outputs):
        complete_draft: str
        ready_for_review: Any

    class Trigger(BaseNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES

    class Display(BaseNode.Display):
        x = 5110
        y = 440
        z_index = 31
        icon = "vellum:icon:folder"
        color = "blue"

    def run(self) -> Outputs:
        lang_label = "English" if self.output_language == "en" else "Español"
        phi_label = (
            "ENABLED - Identifiers Redacted" if self.phi_safe_mode else "DISABLED"
        )
        draft = f"\n{'=' * 70}\n                    ATLAS™ COMPLETE DOCUMENTATION DRAFT\n                    {self.note_type} | {self.setting} | {self.specialty}\n{'=' * 70}\n\n📋 DOCUMENT INFO\n────────────────────────────────────────────────────────────────────\n• Note Type: {self.note_type}\n• Setting: {self.setting}\n• Specialty: {self.specialty}\n• Payer: {self.payer}\n• Language: {lang_label}\n• PHI Safe Mode: {phi_label}\n• QA Status: {self.qa_status}\n\n"
        if self.flag_banner and self.flag_banner.strip():
            draft += self.flag_banner + "\n"
        draft += f"\n📝 CLINICAL NOTE\n{'─' * 70}\n{self.medical_note}\n\n{'─' * 70}\n\n❓ CDI QUERIES (Clinical Documentation Integrity)\n{'─' * 70}\n{self.cdi_queries}\n\n{'─' * 70}\n\n💼 BILLING SUPPORT (Documentation Only - No Coding)\n{'─' * 70}\n{self.billing_support}\n\n{'─' * 70}\n\n✅ QA & COMPLIANCE CHECK\n{'─' * 70}\n{self.flagged_summary}\n\n{'=' * 70}\n                    CLINICIAN REVIEW CHECKLIST\n{'=' * 70}\n[ ] Review and edit clinical note as needed\n[ ] Address CDI queries (answer or mark N/A)\n[ ] Verify billing support accuracy\n[ ] Review QA findings and correct any issues\n[ ] Sign/attest when complete\n\n{'=' * 70}\n                    READY FOR CLINICIAN REVIEW: {('✅ YES' if self.compliance_ok else '❌ NO - Address flagged issues first')}\n{'=' * 70}\n\n⚠️ DISCLAIMERS:\n• This is a DRAFT generated from clinician-provided dictation\n• Clinician must review, edit, and attest before finalizing\n• ATLAS does not diagnose, code, or make clinical decisions\n• No CPT/ICD codes provided - documentation support only\n• No information was invented; missing info surfaced as queries\n• Verify all PHI handling complies with HIPAA requirements\n\n{'=' * 70}\n"
        return self.Outputs(complete_draft=draft, ready_for_review=self.compliance_ok)
