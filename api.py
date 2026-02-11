"""FastAPI wrapper for ATLAS workflow - Vercel deployment.

This is the root-level entry point for Vercel.
It imports and wraps the ATLAS workflow package.
"""
import os
import traceback
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Import from ATLAS package
from workflow import Workflow
from inputs import Inputs

app = FastAPI(
    title="ATLAS CDI Workflow API",
    description="Medical note analysis and CDI query generation",
    version="1.0.0",
)


class AtlasRequest(BaseModel):
    """Request model for /atlas/run endpoint."""
    clinical_document: Optional[str] = Field(None, description="Base64 encoded PDF or document")
    clinical_dictation: Optional[str] = Field(None, description="Raw clinical dictation text")
    note_type: Optional[str] = Field("SOAP", description="Type of medical note")
    setting: Optional[str] = Field(None, description="Clinical setting (e.g., inpatient, outpatient)")
    specialty: Optional[str] = Field(None, description="Medical specialty")
    payer: Optional[str] = Field(None, description="Insurance payer")
    encounter_context: Optional[str] = Field(None, description="Additional encounter context")
    time_spent_minutes: Optional[float] = Field(None, description="Time spent on encounter")
    phi_safe_mode: Optional[bool] = Field(True, description="Enable PHI safe mode")
    output_language: Optional[str] = Field("en", description="Output language code")
    clinician_role: Optional[str] = Field("Physician", description="Role of clinician")


class AtlasResponse(BaseModel):
    """Response model for /atlas/run endpoint."""
    event_name: str
    response: Optional[str] = None
    pdf_report: Optional[str] = None
    pdf_url: Optional[str] = None
    error: Optional[str] = None


@app.get("/")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint."""
    return {
        "ok": True,
        "service": "ATLAS",
        "routes": ["/atlas/run"],
        "version": "1.0.0",
    }


@app.post("/atlas/run")
async def run_atlas(request: AtlasRequest) -> AtlasResponse:
    """
    Execute ATLAS workflow.
    
    Accepts clinical input and returns analysis with CDI queries and PDF report.
    """
    try:
        # Build Inputs object from request
        inputs = Inputs(
            clinical_dictation=request.clinical_dictation,
            note_type=request.note_type,
            setting=request.setting,
            specialty=request.specialty,
            payer=request.payer,
            encounter_context=request.encounter_context,
            time_spent_minutes=request.time_spent_minutes,
            phi_safe_mode=request.phi_safe_mode,
            output_language=request.output_language,
            clinician_role=request.clinician_role,
        )
        
        # Execute workflow
        workflow = Workflow()
        terminal_event = workflow.run(inputs=inputs)
        
        # Extract outputs
        response_text = getattr(terminal_event.outputs, "response", None)
        pdf_report = getattr(terminal_event.outputs, "pdf_report", None)
        pdf_url = getattr(terminal_event.outputs, "pdf_url", None)
        
        return AtlasResponse(
            event_name="workflow_complete",
            response=response_text,
            pdf_report=pdf_report,
            pdf_url=pdf_url,
        )
    
    except Exception as e:
        error_detail = f"{str(e)}\n{traceback.format_exc()}"
        raise HTTPException(
            status_code=500,
            detail=error_detail,
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
