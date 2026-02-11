import re
from typing import Any, Optional

from vellum.workflows import BaseNode
from vellum.workflows.types.core import MergeBehavior

from .generate_billing_support import GenerateBillingSupport
from .generate_cdi_queries import GenerateCDIQueries
from .generate_medical_note import GenerateMedicalNote
from .input_validator import InputValidator


class QACheck(BaseNode):
    medical_note: str = GenerateMedicalNote.Outputs.text
    cdi_queries: str = GenerateCDIQueries.Outputs.text
    billing_support: str = GenerateBillingSupport.Outputs.text
    phi_safe_mode: bool = InputValidator.Outputs.phi_safe_mode
    missing_core_elements: list[Any] = InputValidator.Outputs.missing_core_elements
    phi_risk_hint: Optional[str] = InputValidator.Outputs.phi_risk_hint

    class Outputs(BaseNode.Outputs):
        qa_status: str
        compliance_ok: Any
        issues: Any
        contradictions: Any
        missing_elements: Any
        phi_risks: Any
        recommended_fixes: Any
        flagged_summary: str

    class Trigger(BaseNode.Trigger):
        merge_behavior = MergeBehavior.AWAIT_ATTRIBUTES

    class Display(BaseNode.Display):
        x = 3552
        y = 440
        z_index = 29
        icon = "vellum:icon:check"
        color = "grass"

    def run(self) -> Outputs:
        issues = []
        contradictions = []
        missing_elements = (
            list(self.missing_core_elements) if self.missing_core_elements else []
        )
        phi_risks = []
        recommended_fixes = []
        note_lower = (self.medical_note or "").lower()
        not_documented_count = len(
            re.findall("not documented[/\\s]provided", note_lower)
        )
        if not_documented_count >= 12:
            issues.append(
                f"CRITICAL: {not_documented_count} missing elements detected. Documentation severely incomplete."
            )
        elif not_documented_count >= 8:
            issues.append(
                f"WARNING: {not_documented_count} missing elements detected. Consider answering CDI queries."
            )
        template_patterns = [
            (
                "denies all",
                "Generic ROS denial - verify each system was actually reviewed",
            ),
            (
                "all systems negative",
                "Templated ROS - specify which systems were reviewed",
            ),
            ("wnl", "WNL without specifics - document actual findings"),
            ("within normal limits", "Generic WNL - specify what was examined"),
            ("unremarkable", "Vague term - specify what was examined and findings"),
            ("normal exam", "Generic PE - document specific findings"),
            (
                "all other systems reviewed and negative",
                "Templated language - verify accuracy",
            ),
        ]
        for pattern, warning in template_patterns:
            if pattern in note_lower:
                issues.append(f"TEMPLATE DETECTED: {warning}")
                recommended_fixes.append(
                    f"Replace '{pattern}' with specific documented findings"
                )
        if self.phi_safe_mode:
            phi_patterns = [
                (
                    "\\b[A-Z][a-z]+\\s+[A-Z][a-z]+\\b(?=.*\\b(patient|pt|yo|y/o|year old)\\b)",
                    "Potential patient name",
                ),
                ("\\b\\d{3}-\\d{2}-\\d{4}\\b", "SSN pattern detected"),
                ("\\b\\d{2}/\\d{2}/\\d{4}\\b", "Date pattern (possible DOB)"),
                ("\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b", "Phone number pattern"),
                ("\\bMRN[:\\s]*\\d+\\b", "MRN detected"),
                (
                    "\\b\\d{5,}\\s*(main|street|ave|road|dr|drive|blvd)\\b",
                    "Address pattern",
                ),
            ]
            for pattern, risk in phi_patterns:
                if re.search(pattern, self.medical_note, re.IGNORECASE):
                    phi_risks.append(risk)
            if self.phi_risk_hint:
                phi_risks.append(self.phi_risk_hint)
            if phi_risks:
                issues.append(
                    f"PHI RISK: {len(phi_risks)} potential PHI exposure(s) detected"
                )
                recommended_fixes.append("Review and redact all PHI with [REDACTED]")
        if "plan" in note_lower:
            if (
                "linked to" not in note_lower
                and "for" not in note_lower
                and ("due to" not in note_lower)
            ):
                issues.append(
                    "Medical necessity linkage may be weak - ensure plan items reference problems"
                )
                recommended_fixes.append(
                    "Link each plan item to its corresponding problem/diagnosis"
                )
        if "minutes" in note_lower and "not provided" not in note_lower:
            if (
                "clinician-declared" not in note_lower
                and "clinician declared" not in note_lower
            ):
                issues.append(
                    "Time mentioned but may not be clinician-declared - verify accuracy"
                )
        symptom_pairs = [
            ("denies chest pain", "chest pain"),
            ("denies sob", "shortness of breath"),
            ("denies dyspnea", "dyspnea"),
            ("no fever", "febrile"),
            ("afebrile", "fever"),
        ]
        for denial, positive in symptom_pairs:
            if denial in note_lower and positive in note_lower:
                contradictions.append(
                    f"Potential contradiction: '{denial}' vs '{positive}' - verify context"
                )
        billing_lower = (self.billing_support or "").lower()
        if "not provided" in billing_lower and "time:" in billing_lower:
            pass
        elif "minutes" in billing_lower and "not provided" not in billing_lower:
            if "clinician" not in billing_lower:
                issues.append(
                    "Billing time statement may not reflect clinician-declared time"
                )
        if not self.cdi_queries or len(self.cdi_queries) < 50:
            issues.append("CDI queries section appears incomplete or missing")
        critical_issues = [i for i in issues if "CRITICAL" in i or "PHI RISK" in i]
        warning_issues = [i for i in issues if "WARNING" in i or "TEMPLATE" in i]
        if critical_issues or len(phi_risks) >= 3 or contradictions:
            qa_status = "FAIL"
            compliance_ok = False
        elif warning_issues or len(issues) >= 3:
            qa_status = "WARN"
            compliance_ok = True
        else:
            qa_status = "PASS"
            compliance_ok = True
        flagged_summary = f"QA STATUS: {qa_status}\n{'=' * 50}\n\nISSUES ({len(issues)}):\n{(chr(10).join((f'• {i}' for i in issues)) if issues else '• None')}\n\nCONTRADICTIONS ({len(contradictions)}):\n{(chr(10).join((f'• {c}' for c in contradictions)) if contradictions else '• None')}\n\nMISSING ELEMENTS ({len(missing_elements)}):\n{(chr(10).join((f'• {m}' for m in missing_elements)) if missing_elements else '• None')}\n\nPHI RISKS ({len(phi_risks)}):\n{(chr(10).join((f'• {p}' for p in phi_risks)) if phi_risks else '• None')}\n\nRECOMMENDED FIXES:\n{(chr(10).join((f'• {r}' for r in recommended_fixes)) if recommended_fixes else '• None')}\n\nCOMPLIANCE: {('OK - Ready for clinician review' if compliance_ok else 'FAILED - Requires attention before review')}"
        return self.Outputs(
            qa_status=qa_status,
            compliance_ok=compliance_ok,
            issues=issues,
            contradictions=contradictions,
            missing_elements=missing_elements,
            phi_risks=phi_risks,
            recommended_fixes=recommended_fixes,
            flagged_summary=flagged_summary,
        )
