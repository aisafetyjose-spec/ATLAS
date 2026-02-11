import re
from typing import Any, Optional, Union

from vellum.workflows import BaseNode

from ..inputs import Inputs
from .merge_text_source import MergeTextSource


class InputValidator(BaseNode):
    clinical_dictation: str = MergeTextSource.Outputs.clinical_text
    note_type: Optional[str] = Inputs.note_type
    setting: Optional[str] = Inputs.setting
    specialty: Optional[str] = Inputs.specialty
    payer: Optional[str] = Inputs.payer
    encounter_context: Optional[str] = Inputs.encounter_context
    time_spent_minutes: Optional[int] = Inputs.time_spent_minutes
    phi_safe_mode: bool = Inputs.phi_safe_mode
    output_language: str = Inputs.output_language
    clinician_role: str = Inputs.clinician_role

    class Outputs(BaseNode.Outputs):
        validation_passed: Any
        error_message: str
        normalized_dictation: str
        normalized_note_type: str
        normalized_setting: str
        normalized_specialty: str
        normalized_payer: str
        normalized_encounter_context: str
        normalized_time_spent_minutes: Union[float, int]
        phi_safe_mode: Any
        output_language: str
        clinician_role: str
        missing_core_elements: Any
        compliance_context: str
        phi_risk_hint: str

    class Display(BaseNode.Display):
        x = 1994
        y = 333
        z_index = 23
        icon = "vellum:icon:shield-check"
        color = "teal"

    def run(self) -> Outputs:
        errors = []
        missing = []
        phi_risk_hint = None
        dictation = (self.clinical_dictation or "").strip()
        if not dictation:
            errors.append(
                "Clinical dictation is empty or missing. Please provide the clinical narrative."
            )
        elif len(dictation) < 30:
            errors.append(
                f"Clinical dictation too brief ({len(dictation)} chars). Minimum 30 characters required for meaningful documentation."
            )
        placeholder_patterns = [
            "^[a-z]{1,10}$",
            "^(test|lorem|n/a|na|tbd|xxx|placeholder)$",
        ]
        for pattern in placeholder_patterns:
            if re.match(pattern, dictation.lower()):
                errors.append(
                    f"Dictation appears to be placeholder text ('{dictation}'). Provide real clinical content."
                )
                break
        note_type_map = {
            "soap": "SOAP",
            "progress": "Progress",
            "progress note": "Progress",
            "h&p": "H&P",
            "hnp": "H&P",
            "h and p": "H&P",
            "history and physical": "H&P",
            "consult": "Consult",
            "consultation": "Consult",
            "discharge": "Discharge",
            "discharge summary": "Discharge",
        }
        raw_type = (self.note_type or "SOAP").strip().lower()
        normalized_type = note_type_map.get(raw_type)
        if not normalized_type:
            normalized_type = "Progress"
            missing.append(
                "Confirm note type (received invalid value, defaulted to Progress)"
            )
        valid_settings = {"outpatient", "inpatient", "ed", "telehealth"}
        raw_setting = (self.setting or "").strip().lower()
        if raw_setting in valid_settings:
            normalized_setting = raw_setting.capitalize()
            if raw_setting == "ed":
                normalized_setting = "ED"
        else:
            normalized_setting = "Unspecified"
            if not self.setting:
                missing.append("Setting (outpatient/inpatient/ED/telehealth)")
        valid_payers = {
            "medicare",
            "medicare advantage",
            "medicaid",
            "commercial",
            "self-pay",
        }
        raw_payer = (self.payer or "").strip().lower()
        if raw_payer in valid_payers:
            normalized_payer = self.payer.strip()
        else:
            normalized_payer = "Unspecified"
            if not self.payer:
                missing.append("Payer type (Medicare/Medicaid/Commercial/Self-pay)")
        normalized_specialty = (self.specialty or "").strip() or "Unspecified"
        if not self.specialty:
            missing.append("Specialty")
        normalized_time = None
        if self.time_spent_minutes is not None:
            if self.time_spent_minutes <= 0:
                missing.append(
                    "Time spent appears invalid (<=0). Omitting from documentation."
                )
            elif self.time_spent_minutes > 480:
                missing.append(
                    f"Time spent ({self.time_spent_minutes} min) exceeds reasonable limit. Verify accuracy."
                )
                normalized_time = self.time_spent_minutes
            else:
                normalized_time = self.time_spent_minutes
        normalized_language = (
            self.output_language.lower() if self.output_language else "en"
        )
        if normalized_language not in ("en", "es"):
            normalized_language = "en"
        if self.phi_safe_mode:
            phi_patterns = [
                ("\\b\\d{3}-\\d{2}-\\d{4}\\b", "SSN pattern"),
                ("\\b\\d{9,10}\\b", "MRN pattern"),
                ("\\b\\d{2}/\\d{2}/\\d{4}\\b", "DOB pattern"),
                ("\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b", "Phone pattern"),
                (
                    "\\b[A-Z][a-z]+\\s+[A-Z][a-z]+\\b.*\\b(DOB|MRN|SSN)\\b",
                    "Name + identifier",
                ),
            ]
            detected_phi = []
            for pattern, desc in phi_patterns:
                if re.search(pattern, dictation, re.IGNORECASE):
                    detected_phi.append(desc)
            if detected_phi:
                phi_risk_hint = f"PHI patterns detected: {', '.join(detected_phi)}. Will require redaction."
        clone_patterns = [
            ("denies all", "Generic ROS denial"),
            ("all systems negative", "Templated ROS"),
            ("wnl throughout", "Generic WNL"),
            ("unremarkable exam", "Templated PE"),
            ("normal exam", "Generic PE"),
            ("all other systems reviewed and negative", "Templated ROS"),
        ]
        clone_warnings = []
        for pattern, desc in clone_patterns:
            if pattern in dictation.lower():
                clone_warnings.append(f"{desc} ('{pattern}')")
        compliance_context = f"""ATLAS COMPLIANCE CONTEXT\n========================\nNote Type: {normalized_type}\nSetting: {normalized_setting}\nSpecialty: {normalized_specialty}\nPayer: {normalized_payer}\nPHI Safe Mode: {self.phi_safe_mode}\nOutput Language: {normalized_language.upper()}\nClinician Role: {self.clinician_role}\n\nMANDATORY DOCUMENTATION RULES:\n1. NEVER invent diagnoses, findings, ROS, PE, labs, imaging, times, or procedures not explicitly stated.\n2. Mark missing information as "Not documented/provided" and generate clarification queries.\n3. Document ONLY what the clinician stated or is present in provided context.\n4. Maintain audit-ready specificity: acuity, severity, laterality, etiology ONLY when stated.\n5. NO upcoding language. Medical necessity through accurate documentation, not manipulation.\n6. If PHI Safe Mode=True, redact identifiers (names, DOB, MRN, addresses, phones) with [REDACTED].\n7. Include "Evidence Quotes" (max 3 short quotes from dictation) to anchor content.\n8. Generate "Clinician Clarifications Needed" for any ambiguity.\n\n{(f"TEMPLATE WARNINGS: {'; '.join(clone_warnings)}" if clone_warnings else '')}\n{(f"MISSING ELEMENTS TO QUERY: {', '.join(missing)}" if missing else '')}"""
        validation_passed = len(errors) == 0
        error_message = "; ".join(errors) if errors else None
        return self.Outputs(
            validation_passed=validation_passed,
            error_message=error_message,
            normalized_dictation=dictation,
            normalized_note_type=normalized_type,
            normalized_setting=normalized_setting,
            normalized_specialty=normalized_specialty,
            normalized_payer=normalized_payer,
            normalized_encounter_context=(self.encounter_context or "").strip()
            or "Not provided",
            normalized_time_spent_minutes=normalized_time,
            phi_safe_mode=self.phi_safe_mode,
            output_language=normalized_language,
            clinician_role=self.clinician_role or "Physician",
            missing_core_elements=missing,
            compliance_context=compliance_context,
            phi_risk_hint=phi_risk_hint,
        )
