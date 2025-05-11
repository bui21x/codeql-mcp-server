from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import subprocess
import os

app = FastAPI()

class CodeQLQuery(BaseModel):
    query: str
    language: str
    path: str

class CodeQLResult(BaseModel):
    results: List[dict]
    error: Optional[str] = None

@app.post('/analyze', response_model=CodeQLResult)
async def analyze_code(query: CodeQLQuery):
    try:
        # Run CodeQL analysis
        result = subprocess.run(
            ['codeql', 'database', 'analyze', query.path,
             '--language=' + query.language,
             '--format=json',
             query.query],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr)
            
        return CodeQLResult(results=result.stdout)
    except Exception as e:
        return CodeQLResult(results=[], error=str(e))

@app.get('/health')
async def health_check():
    return {'status': 'healthy'}