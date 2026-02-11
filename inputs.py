from typing import Any, Optional, Union

from vellum.client.types.vellum_document import VellumDocument
from vellum.workflows.inputs import BaseInputs


class Inputs(BaseInputs):
    clinical_document: Optional[VellumDocument] = None
    clinical_dictation: Optional[str] = None
    note_type: Optional[str] = "SOAP"
    setting: Optional[str] = None
    specialty: Optional[str] = None
    payer: Optional[str] = None
    encounter_context: Optional[str] = None
    time_spent_minutes: Optional[Union[float, int, None]] = None
    phi_safe_mode: Optional[Any] = True
    output_language: Optional[str] = "en"
    clinician_role: Optional[str] = "Physician"
