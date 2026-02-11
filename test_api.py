#!/usr/bin/env python
"""Quick test script for ATLAS API."""
import sys
import json

try:
    from app import app
    from fastapi.testclient import TestClient
    
    client = TestClient(app)
    
    # Test GET /
    print("Testing GET /...")
    response = client.get("/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        print("\n✓ GET / endpoint works!")
    else:
        print(f"\n✗ GET / failed with status {response.status_code}")
        sys.exit(1)
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
