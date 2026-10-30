import os
import io
import json
import time
import httpx
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from pypdf import PdfReader
from backend.sample_data import SAMPLE_DOCUMENTS

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip('"').strip("'")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001").strip('"').strip("'")

# Multi-model fallback list for zero-downtime reliability
FALLBACK_MODELS = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
    "gemini-3.8-flash"
]

def get_embedding(text: str) -> List[float]:
    """Generate 768-dimensional vector embedding using Google Gemini."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{EMBEDDING_MODEL}:embedContent?key={GEMINI_API_KEY}"
    payload = {
        "model": f"models/{EMBEDDING_MODEL}",
        "content": {"parts": [{"text": text[:2000]}]},
        "outputDimensionality": 768
    }
    resp = httpx.post(url, json=payload, timeout=20.0)
    if resp.status_code != 200:
        raise RuntimeError(f"Embedding API error: {resp.status_code} - {resp.text}")
    return resp.json()["embedding"]["values"]

def seed_database(db) -> Dict[str, Any]:
    """Embed and load all pre-curated sample documents into MongoDB Atlas."""
    db.clear_all()
    all_chunks = []
    chunk_counter = 1

    for doc in SAMPLE_DOCUMENTS:
        for sec in doc["sections"]:
            full_text = f"{doc['doc_name']} - {sec['section']}: {sec['text']}"
            embedding = get_embedding(full_text)
            chunk = {
                "chunk_id": f"chunk_{chunk_counter}",
                "doc_id": doc["doc_id"],
                "doc_name": doc["doc_name"],
                "category": doc["category"],
                "section": sec["section"],
                "text": sec["text"],
                "embedding": embedding
            }
            all_chunks.append(chunk)
            chunk_counter += 1

    inserted_count = db.insert_chunks(all_chunks)
    return {
        "status": "success",
        "documents_loaded": len(SAMPLE_DOCUMENTS),
        "chunks_indexed": inserted_count
    }

def process_and_index_file(file_bytes: bytes, filename: str, category: str, db) -> Dict[str, Any]:
    """Extract text from uploaded PDF/TXT/MD, split into semantic chunks, embed, and store in MongoDB Atlas."""
    extracted_text = ""
    if filename.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(file_bytes))
        for page_idx, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            if page_text.strip():
                extracted_text += f"\n[Page {page_idx+1}]\n" + page_text
    else:
        extracted_text = file_bytes.decode("utf-8", errors="ignore")

    if not extracted_text.strip():
        raise ValueError("No readable text could be extracted from the file.")

    # Semantic paragraph chunking
    raw_paragraphs = [p.strip() for p in extracted_text.split("\n\n") if len(p.strip()) > 30]
    if not raw_paragraphs:
        raw_paragraphs = [p.strip() for p in extracted_text.split("\n") if len(p.strip()) > 30]

    doc_id = filename.lower().replace(" ", "_").replace(".", "_")
    chunks = []
    for idx, para in enumerate(raw_paragraphs):
        sec_title = f"Section {idx+1}"
        # If paragraph starts with heading-like text
        first_line = para.split("\n")[0][:60]
        if ":" in first_line or "Section" in first_line or "Clause" in first_line or "Article" in first_line:
            sec_title = first_line

        full_content = f"{filename} - {sec_title}: {para}"
        embedding = get_embedding(full_content)
        chunks.append({
            "chunk_id": f"chunk_{doc_id}_{idx+1}",
            "doc_id": doc_id,
            "doc_name": filename,
            "category": category or "User Upload",
            "section": sec_title,
            "text": para,
            "embedding": embedding
        })

    inserted = db.insert_chunks(chunks)
    return {
        "status": "success",
        "doc_name": filename,
        "chunks_indexed": inserted
    }

def call_gemini(prompt: str, system_instruction: str = "") -> str:
    """Call Gemini LLM with automatic multi-model failover."""
    contents = []
    if system_instruction:
        contents.append({"role": "user", "parts": [{"text": system_instruction}]})
        contents.append({"role": "model", "parts": [{"text": "Understood. I will strictly follow your instructions, ground all claims, and output structured JSON."}]})
    contents.append({"role": "user", "parts": [{"text": prompt}]})

    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "application/json"
        }
    }

    last_error = ""
    for model in FALLBACK_MODELS:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
        for attempt in range(2):
            try:
                resp = httpx.post(url, json=payload, timeout=25.0)
                if resp.status_code == 200:
                    candidates = resp.json().get("candidates", [])
                    if candidates:
                        return candidates[0]["content"]["parts"][0]["text"]
                elif resp.status_code == 503:
                    time.sleep(1.0)
                    continue
                else:
                    last_error = f"{model}: {resp.status_code} - {resp.text}"
                    break
            except Exception as e:
                last_error = str(e)
                time.sleep(0.5)

    raise RuntimeError(f"All Gemini models exhausted. Last error: {last_error}")

def query_rag_engine(query: str, db, limit: int = 5) -> Dict[str, Any]:
    """
    Complete Track 2 Enterprise RAG Pipeline:
    1. Embed query
    2. MongoDB Vector Search
    3. Multi-source evidence synthesis
    4. Exact citations linking
    5. Cross-document discrepancy & contradiction detection with risk rating
    6. Compliance health score
    7. Out-of-scope / Unanswerable handling
    """
    # Step 1: Embed query
    query_vector = get_embedding(query)

    # Step 2: Retrieve from MongoDB Vector Search
    retrieved_chunks = db.vector_search(query_vector, limit=limit)
    if not retrieved_chunks:
        return {
            "query": query,
            "is_answerable": False,
            "compliance_score": 100,
            "summary": "No relevant documents found in the database. Please index or seed documents first.",
            "detailed_findings": [],
            "citations": [],
            "conflicts_detected": [],
            "retrieved_passages": []
        }

    # Step 3: Prepare context for LLM
    context_blocks = []
    unique_sources = set()
    for idx, c in enumerate(retrieved_chunks, 1):
        unique_sources.add(c["doc_name"])
        context_blocks.append(
            f"[Source {idx}] Document: '{c['doc_name']}' | Section: '{c['section']}' | Similarity: {round(c.get('score', 0), 4)}\nExcerpt: {c['text']}"
        )
    formatted_context = "\n\n".join(context_blocks)

    system_instruction = (
        "You are AuditLens AI, an enterprise-grade policy, contract, and SLA auditor used by Legal, DevOps, and Compliance officers. "
        "Your task is to analyze cross-document evidence retrieved from MongoDB Atlas Vector Search.\n\n"
        "RULES:\n"
        "1. STRICT GROUNDING: Answer ONLY using the provided retrieved context. Never assume or invent facts.\n"
        "2. MULTI-SOURCE SYNTHESIS: When information spans multiple documents or sections, explicitly synthesize them together into an actionable briefing.\n"
        "3. CITATIONS: Attribute every key fact with the exact Document Name, Section, and verbatim excerpt.\n"
        "4. CONFLICT DETECTION: Actively check if any two documents disagree or impose contradictory obligations (e.g. allowed downtime differences, liability caps, or notification windows). "
        "If a conflict exists, classify its risk_level as 'HIGH', 'MEDIUM', or 'LOW', and provide an executive remediation_recommendation.\n"
        "5. COMPLIANCE SCORE: If conflicts or high operational risks exist, assign an audit compliance score between 50-85. If fully aligned, assign 95-100.\n"
        "6. UNANSWERABLE HANDLING: If the query asks for information not contained in the context (or if evidence is insufficient), set 'is_answerable': false and provide a polite, professional explanation in 'summary'. Do NOT guess.\n\n"
        "OUTPUT FORMAT (STRICT JSON ONLY):\n"
        "{\n"
        '  "is_answerable": true/false,\n'
        '  "compliance_score": integer between 0 and 100,\n'
        '  "summary": "1-2 sentence executive summary of findings",\n'
        '  "detailed_findings": [\n'
        '    {"point": "Finding text", "risk": "HIGH"|"MEDIUM"|"LOW"|"INFO"}\n'
        '  ],\n'
        '  "citations": [\n'
        '    {\n'
        '      "doc_name": "exact file name",\n'
        '      "section": "exact section name",\n'
        '      "quote": "short relevant quote verbatim",\n'
        '      "claim_supported": "what this proves"\n'
        '    }\n'
        '  ],\n'
        '  "conflicts_detected": [\n'
        '    {\n'
        '      "title": "Short title of contradiction",\n'
        '      "doc_a": "First document name",\n'
        '      "doc_a_clause": "What doc A states",\n'
        '      "doc_b": "Second document name",\n'
        '      "doc_b_clause": "What doc B states",\n'
        '      "risk_level": "HIGH"|"MEDIUM"|"LOW",\n'
        '      "risk_analysis": "Practical business or legal impact",\n'
        '      "remediation_recommendation": "Concrete action required to resolve"\n'
        '    }\n'
        '  ]\n'
        "}"
    )

    prompt = f"USER AUDIT QUERY: {query}\n\nRETRIEVED CONTEXT FROM MONGODB VECTOR SEARCH:\n{formatted_context}"

    raw_response = call_gemini(prompt, system_instruction)
    
    try:
        parsed = json.loads(raw_response)
    except Exception:
        cleaned = raw_response.strip().replace("```json", "").replace("```", "")
        parsed = json.loads(cleaned)

    parsed["retrieved_evidence_count"] = len(retrieved_chunks)
    parsed["unique_documents_referenced"] = list(unique_sources)
    parsed["retrieved_passages"] = retrieved_chunks

    return parsed
