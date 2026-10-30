import os
import sys
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.database import db
from backend.rag_engine import seed_database, query_rag_engine, get_embedding, process_and_index_file

app = FastAPI(
    title="AuditLens AI - Enterprise Policy & Contract Intelligence RAG Engine",
    description="Track 2: RAG Engine with MongoDB Atlas Vector Search and Gemini",
    version="2.0.0"
)

# Enable CORS for web clients
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

class CustomDocRequest(BaseModel):
    doc_name: str
    category: str
    section: str
    text: str

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
def list_documents():
    """Retrieve all indexed documents in MongoDB."""
    return db.get_all_documents()

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
    category: str = Form("User Upload")
):
    """Upload PDF, TXT, or Markdown documents, chunk them, and store in MongoDB Vector Search."""
    try:
        file_bytes = await file.read()
        res = process_and_index_file(file_bytes, file.filename, category, db)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query")
def run_audit_query(req: QueryRequest):
    """Execute complete RAG pipeline with multi-source synthesis, citations, and risk detection."""
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    try:
        response = query_rag_engine(req.query, db, limit=req.limit)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/add_document")
def add_custom_document(req: CustomDocRequest):
    """Add a custom document chunk, generate embedding, and store in MongoDB."""
    try:
        full_text = f"{req.doc_name} - {req.section}: {req.text}"
        embedding = get_embedding(full_text)
        chunk = {
            "chunk_id": f"chunk_custom_{os.urandom(4).hex()}",
            "doc_id": req.doc_name.lower().replace(" ", "_"),
            "doc_name": req.doc_name,
            "category": req.category,
            "section": req.section,
            "text": req.text,
            "embedding": embedding
        }
        db.insert_chunks([chunk])
        return {"status": "success", "message": f"Added section '{req.section}' to {req.doc_name}"}
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
