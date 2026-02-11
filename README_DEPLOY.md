# ATLAS Vercel Deployment Guide

## Overview
This is a FastAPI wrapper for the ATLAS clinical workflow, configured for serverless deployment on Vercel.

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export VELLUM_API_KEY="your-api-key-here"
```

4. Run locally:
```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## Testing Locally

### Health Check
```bash
curl -s http://127.0.0.1:8000/
```

Expected response:
```json
{
  "ok": true,
  "service": "ATLAS",
  "routes": ["/atlas/run"],
  "version": "1.0.0"
}
```

### Run Workflow
```bash
curl -s -X POST http://127.0.0.1:8000/atlas/run \
  -H "Content-Type: application/json" \
  -d '{
    "clinical_dictation": "Patient presents with chest pain and shortness of breath. History of hypertension.",
    "note_type": "SOAP",
    "specialty": "Cardiology",
    "output_language": "en",
    "phi_safe_mode": true
  }'
```

## Vercel Deployment

### Option A: GUI Deployment

1. Push code to GitHub:
```bash
git init
git add .
git commit -m "ATLAS Vercel wrapper"
git remote add origin https://github.com/YOUR_USERNAME/atlas-vercel.git
git push -u origin main
```

2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Configure environment variables:
   - `VELLUM_API_KEY`: Your Vellum API key
6. Click "Deploy"

### Option B: CLI Deployment

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

4. For production:
```bash
vercel --prod
```

## Environment Variables

The following environment variables must be configured in Vercel:

| Variable | Description | Required |
|----------|-------------|----------|
| `VELLUM_API_KEY` | Vellum API authentication key | Yes |

## API Endpoints

### GET /
Health check endpoint.

**Response:**
```json
{
  "ok": true,
  "service": "ATLAS",
  "routes": ["/atlas/run"],
  "version": "1.0.0"
}
```

### POST /atlas/run
Execute the ATLAS workflow.

**Request Body:**
```json
{
  "clinical_dictation": "string (optional)",
  "clinical_document": "string (optional, base64 encoded)",
  "note_type": "string (default: SOAP)",
  "setting": "string (optional)",
  "specialty": "string (optional)",
  "payer": "string (optional)",
  "encounter_context": "string (optional)",
  "time_spent_minutes": "number (optional)",
  "phi_safe_mode": "boolean (default: true)",
  "output_language": "string (default: en)",
  "clinician_role": "string (default: Physician)"
}
```

**Response:**
```json
{
  "event_name": "workflow_complete",
  "response": "string (complete draft)",
  "pdf_report": "string (base64 encoded PDF)",
  "pdf_url": "string (signed URL to PDF)",
  "error": null
}
```

## Troubleshooting

### Timeout Issues
If you experience timeouts on Vercel (>30 seconds), consider:
- Migrating to Render.com or Fly.io for longer execution times
- Optimizing the workflow for faster execution
- Using async processing with a job queue

### Missing API Keys
If you see errors about missing `VELLUM_API_KEY`:
1. Go to Vercel project settings
2. Navigate to "Environment Variables"
3. Add `VELLUM_API_KEY` with your Vellum API key
4. Redeploy the project

### Import Errors
Ensure the ATLAS package is properly structured:
- `ATLAS/__init__.py` exists
- `ATLAS/workflow.py` contains the Workflow class
- `ATLAS/inputs.py` contains the Inputs class
- `ATLAS/nodes/` directory contains all node implementations

## Files Created

- `app.py` - FastAPI application wrapper
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel configuration
- `.python-version` - Python version specification
- `README_DEPLOY.md` - This file

## Support

For issues with:
- **ATLAS workflow**: Check the original workflow implementation
- **Vellum API**: Visit [vellum.ai](https://vellum.ai)
- **Vercel deployment**: Visit [vercel.com/docs](https://vercel.com/docs)
