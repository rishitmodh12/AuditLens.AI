import os
import sys
import json
from typing import Dict, Any, Optional
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.database import db
from backend.rag_engine import (
    seed_database, 
    query_rag_engine, 
    get_embedding, 
    process_and_index_file,
    scan_all_contract_conflicts
)

app = FastAPI(
    title="AuditLens AI - Enterprise Policy & Contract Intelligence RAG Engine",
    description="Track 2: RAG Engine with MongoDB Atlas Vector Search and Gemini",
    version="3.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    limit: Optional[int] = 5
    user_email: Optional[str] = "guest"

class GoogleAuthRequest(BaseModel):
    credential: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    picture: Optional[str] = None

class ProfileUpdateRequest(BaseModel):
    email: str
    display_name: str

@app.get("/api/health")
def health_check():
    try:
        is_connected = db.ping()
        docs = db.get_all_documents() if is_connected else []
        total_chunks = sum(d.get("total_chunks", 0) for d in docs)
        return {
            "status": "healthy" if is_connected else "database_unreachable",
            "database": "auditlens_db",
            "mongodb_connected": is_connected,
            "indexed_documents_count": len(docs),
            "total_vector_chunks": total_chunks
        }
    except Exception as e:
        return {
            "status": "degraded",
            "mongodb_connected": False,
            "error": str(e)
        }

@app.post("/api/seed")
def seed_demo_data():
    """Seed the database with pre-curated enterprise policy documents."""
    try:
        result = seed_database(db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents")
def list_documents(user_email: Optional[str] = None):
    """Retrieve indexed documents in MongoDB."""
    return db.get_all_documents(user_id=user_email)

@app.delete("/api/documents/{doc_id}")
def delete_document(doc_id: str):
    """Delete an indexed document from MongoDB Atlas."""
    try:
        deleted = db.delete_document(doc_id)
        return {"status": "success", "chunks_deleted": deleted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload_file")
async def upload_file(
    file: UploadFile = File(...),
    category: str = Form("User Upload"),
    user_email: str = Form("guest")
):
    """Upload PDF, TXT, or Markdown documents, chunk them with 15% overlap, and store in MongoDB Vector Search."""
    try:
        file_bytes = await file.read()
        res = process_and_index_file(file_bytes, file.filename, category, db, user_id=user_email)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query")
def run_audit_query(req: QueryRequest):
    """Execute complete RAG pipeline with multi-source synthesis, citations, and risk detection."""
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    try:
        response = query_rag_engine(req.query, db, limit=req.limit, user_id=req.user_email)
        
        # Save to MongoDB Atlas audit history
        history_record = {
            "user_email": req.user_email or "guest",
            "query": req.query,
            "summary": response.get("summary"),
            "compliance_score": response.get("compliance_score", 95),
            "citations_count": len(response.get("citations", [])),
            "conflicts_count": len(response.get("conflicts_detected", [])),
            "created_at": datetime.utcnow().isoformat()
        }
        db.save_audit_history(history_record)

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/conflicts/scan")
def scan_conflicts():
    """Dynamically scan all documents currently stored in MongoDB Atlas for contractual contradictions."""
    try:
        conflicts = scan_all_contract_conflicts(db)
        return {"conflicts": conflicts, "total_found": len(conflicts)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/auth/config")
def get_auth_config():
    """Return public auth configuration."""
    client_id = os.getenv("GOOGLE_CLIENT_ID", "").strip('"').strip("'")
    return {
        "google_client_id": client_id,
        "is_configured": bool(client_id and client_id != "demo-client-id")
    }

@app.get("/api/user/history")
def get_audit_history(user_email: Optional[str] = "guest"):
    """Retrieve saved audit history from MongoDB Atlas."""
    return db.get_user_history(user_email=user_email, limit=25)

@app.delete("/api/user/history/{record_id}")
def delete_single_audit_history(record_id: str, user_email: Optional[str] = "guest"):
    """Permanently delete an individual audit history entry from MongoDB Atlas."""
    success = db.delete_single_history(record_id, user_email=user_email)
    if not success:
        raise HTTPException(status_code=404, detail="Audit history record not found or unauthorized.")
    return {"status": "success", "message": "Record permanently deleted."}

@app.delete("/api/user/history")
def clear_all_audit_history(user_email: Optional[str] = "guest"):
    """Permanently clear all audit history for this user from MongoDB Atlas."""
    deleted_count = db.clear_all_history(user_email=user_email)
    return {"status": "success", "records_deleted": deleted_count}

# GOOGLE AUTH & USER PROFILE ENDPOINTS
@app.get("/api/auth/config")
def get_auth_config():
    """Return Google OAuth configuration status."""
    return {
        "status": "success",
        "google_client_id": os.getenv("GOOGLE_CLIENT_ID", ""),
        "configured": bool(os.getenv("GOOGLE_CLIENT_ID")),
        "auth_mode": "direct_and_oauth"
    }

@app.post("/api/auth/google")
def auth_google(req: GoogleAuthRequest):
    """
    Authenticate user via Google OAuth credential or demo profile.
    Decodes Google JWT or accepts profile payload and stores in MongoDB 'users'.
    """
    try:
        email = req.email
        name = req.name or "Auditor"
        picture = req.picture or "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&h=120&q=80"

        # If standard Google JWT credential token is provided, decode payload
        if req.credential and not email:
            import base64
            parts = req.credential.split(".")
            if len(parts) >= 2:
                # Add padding if needed
                padded = parts[1] + "=" * ((4 - len(parts[1]) % 4) % 4)
                decoded = json.loads(base64.urlsafe_b64decode(padded).decode("utf-8"))
                email = decoded.get("email")
                name = decoded.get("name", name)
                picture = decoded.get("picture", picture)

        if not email:
            raise HTTPException(status_code=400, detail="Invalid Google authentication payload.")

        user_profile = {
            "email": email,
            "name": name,
            "picture": picture,
            "role": "Compliance Officer",
            "last_login": datetime.utcnow().isoformat()
        }
        saved = db.upsert_user(user_profile)
        return {"status": "success", "user": saved}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Authentication failed: {str(e)}")

@app.post("/api/user/profile")
def update_profile(req: ProfileUpdateRequest):
    """Update user's custom display name in MongoDB Atlas."""
    try:
        db.update_user_preferences(req.email, {"name": req.display_name})
        user = db.get_user(req.email)
        return {"status": "success", "user": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/reset")
def reset_database():
    """Clear all indexed documents."""
    db.clear_all()
    return {"status": "success", "message": "Database cleared."}

# Mount static frontend
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_index():
    index_file = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return HTMLResponse("<h2>AuditLens AI Backend Running! Frontend loading...</h2>")
