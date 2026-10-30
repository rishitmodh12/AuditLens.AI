import os
import json
import time
import httpx
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from backend.sample_data import SAMPLE_DOCUMENTS

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")

# List of models for automatic failover during traffic spikes
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
        "content": {"parts": [{"text": text}]},
        "outputDimensionality": 768
    }
    resp = httpx.post(url, json=payload, timeout=15.0)
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

def call_gemini(prompt: str, system_instruction: str = "") -> str:
    """Call Gemini LLM with automatic model failover and retry logic."""
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
                resp = httpx.post(url, json=payload, timeout=20.0)
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
    Complete Track 2 RAG Pipeline:
    1. Embed query
    2. MongoDB Vector Search
    3. Multi-source evidence synthesis
    4. Exact citations linking
    5. Discrepancy / Conflict detection
    6. Out-of-scope / Unanswerable handling
    """
    # Step 1: Embed query
    query_vector = get_embedding(query)

    # Step 2: Retrieve from MongoDB Vector Search
    retrieved_chunks = db.vector_search(query_vector, limit=limit)
    if not retrieved_chunks:
        return {
            "query": query,
            "is_answerable": False,
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
        "You are AuditLens AI, an enterprise-grade policy, contract, and SLA auditor. "
        "Your task is to analyze cross-document evidence retrieved from MongoDB Atlas Vector Search.\n\n"
        "RULES:\n"
        "1. STRICT GROUNDING: Answer ONLY using the provided retrieved context. Never assume or invent facts.\n"
        "2. MULTI-SOURCE SYNTHESIS: When information spans multiple documents or sections, explicitly synthesize them together into a coherent briefing.\n"
        "3. CITATIONS: Attribute every key fact with the exact Document Name, Section, and verbatim excerpt.\n"
        "4. CONFLICT DETECTION: Actively check if any two documents disagree or impose contradictory obligations (e.g. allowed downtime differences, liability limits, or notice windows). If so, report them in the 'conflicts_detected' array.\n"
        "5. UNANSWERABLE HANDLING: If the query asks for information not contained in the context (or if evidence is insufficient), set 'is_answerable': false and provide a polite, professional explanation in 'summary'. Do NOT guess.\n\n"
        "OUTPUT FORMAT (STRICT JSON ONLY):\n"
        "{\n"
        '  "is_answerable": true/false,\n'
        '  "summary": "1-2 sentence executive summary of findings",\n'
        '  "detailed_findings": ["Bullet point finding 1", "Bullet point finding 2"],\n'
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
        '      "risk_analysis": "Practical business or legal impact"\n'
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

    # Attach raw retrieval telemetry for judge inspection
    parsed["retrieved_evidence_count"] = len(retrieved_chunks)
    parsed["unique_documents_referenced"] = list(unique_sources)
    parsed["retrieved_passages"] = retrieved_chunks

    return parsed
