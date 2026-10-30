# 🔍 AuditLens AI — Cross-Document Policy & Contract RAG Engine

> **Built for UNCHARTED 2026 Hackathon (Track 2: RAG Engine)**  
> Organized by **NEXUS — Official DoCSE & DoAI Cell, SVNIT Surat**  
> In collaboration with **MongoDB** and **n8n**.

---

## 🌟 Executive Summary

**AuditLens AI** is an enterprise-grade cross-document compliance, contract, and Service Level Agreement (SLA) intelligence engine. Built natively on **MongoDB Atlas Vector Search** and **Google Gemini**, AuditLens solves the critical challenges of multi-document due diligence:

1. **Multi-Source Evidence Synthesis**: Simultaneously retrieves and synthesizes facts across disparate documents (e.g., combining Customer SLAs with Internal Security Playbooks and Vendor Master Agreements).
2. **Verbatim Grounded Citations**: Every claim is linked to its exact document name, clause title, and verbatim excerpt.
3. **Automated Conflict & Contradiction Detection**: Automatically detects and alerts on legal and operational contradictions between contracts (e.g., Customer SLA 1-hour allowed downtime vs. Vendor 4-hour permitted maintenance).
4. **Hallucination Shield (Unanswerable Guardrail)**: Safely identifies out-of-scope queries and refuses to guess, providing clear explanations when required information is absent.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       USER BROWSER                          │
│     Modern Responsive UI (Tailwind CSS + Glassmorphism)     │
│  - One-Click Judge Demo Scenarios                           │
│  - Document Ingestion & Chunk Viewer                        │
│  - Grounded Answer View + Verbatim Citation Cards           │
│  - Cross-Document Contradiction & Risk Analysis Alert Box   │
└──────────────────────────────┬──────────────────────────────┘
                               │ REST API
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (Python FastAPI)                 │
│  - Document Processing & Chunking                           │
│  - Gemini Embeddings (`gemini-embedding-001` @ 768 dims)    │
│  - Multi-Model Resilience & Automatic Failover Engine       │
│  - Multi-Source Synthesis & Grounded Citations Generator    │
└──────────────────────────────┬──────────────────────────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
┌──────────────────────────────┐ ┌───────────────────────────┐
│     MongoDB Atlas Cluster    │ │      Google Gemini API    │
│  - Database: `auditlens_db`  │ │  - `gemini-3.5-flash`     │
│  - Collection: `documents`   │ │  - `gemini-3.1-flash-lite`│
│  - Index: `vector_index`     │ │  - Structured JSON Output │
│  - Aggregation: $vectorSearch│ └───────────────────────────┘
└──────────────────────────────┘
```

---

## 🎯 Track 2 Challenge Brief Compliance

| Hackathon Requirement | AuditLens AI Implementation | Verified Status |
| :--- | :--- | :---: |
| **Focused collection of sources** | Pre-curated realistic enterprise contracts & policies with custom upload support | ✅ Complete |
| **Evidence from more than one source** | Seamlessly cross-references Customer SLA, Security Policy, and Vendor Agreements in a single response | ✅ Complete |
| **Citations for every important result** | Structured citation cards featuring exact file name, section, and verbatim quotation | ✅ Complete |
| **Difficult / Unanswerable request handling** | Built-in Hallucination Guard detects missing context and returns structured out-of-scope response | ✅ Complete |
| **Conflicting request handling** | Dedicated contradiction analyzer flags conflicting clauses (e.g., SLA downtime vs Vendor maintenance) | ✅ Complete |
| **MongoDB Atlas Vector Search** | Native `$vectorSearch` aggregation pipeline indexing 768-dimensional cosine similarity embeddings | ✅ Complete |
| **Compulsory Live Deployment** | Publicly accessible URL ready for judge evaluation | ✅ Complete |

---

## ⚡ Quick Demo Scenarios for Judges

AuditLens AI comes pre-loaded with curated enterprise documents and one-click demo pills:

1. **🌐 Multi-Source Synthesis**:  
   *Query*: `"If an outage exceeds 2 hours, what is our customer liability and what is the internal mitigation deadline?"`  
   *Output*: Combines liability penalty (\$1,000/hr) from `Customer_Enterprise_SLA_2026.pdf` with the 2-hour patch deadline from `Internal_Security_Incident_Policy_v4.pdf`.
2. **⚠️ Conflict Detection**:  
   *Query*: `"Are there any contradictory terms between our Customer SLA and Cloud Vendor Agreement regarding allowed downtime?"`  
   *Output*: Flags the direct contradiction between SLA Section 1.1 (max 1.0 hour downtime) and Vendor Article 4.1 (permitting up to 4.0 hours maintenance without penalty).
3. **🛡️ Unanswerable / Hallucination Guard**:  
   *Query*: `"What is the company policy regarding drone photography inside the server datacenter?"`  
   *Output*: Cleanly identifies that this topic is not covered in any indexed document without hallucinating.
4. **📍 Data Sovereignty & Compliance**:  
   *Query*: `"What are our data residency location restrictions and audit log retention requirements?"`  
   *Output*: Cross-references the AWS Mumbai (`ap-south-1`) data residency restriction from the Vendor Contract with the 365-day log retention rule from the Security Policy.

---

## 🚀 Local Setup & Installation

### Prerequisites
- Python 3.10+
- MongoDB Atlas Free Cluster with a Vector Search Index
- Google Gemini API Key

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/auditlens-ai.git
cd auditlens-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:
```env
MONGODB_URI="mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
GEMINI_API_KEY="your_gemini_api_key"
DATABASE_NAME="auditlens_db"
COLLECTION_NAME="documents"
INDEX_NAME="vector_index"
GEMINI_MODEL="gemini-3.1-flash-lite"
EMBEDDING_MODEL="gemini-embedding-001"
```

### 4. Create MongoDB Atlas Vector Search Index
In MongoDB Atlas -> **Search & Vector Search** -> **Create Search Index** -> **JSON Editor**:
```json
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 768,
      "similarity": "cosine"
    }
  ]
}
```

### 5. Run the Application
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```
Open **`http://localhost:8000`** in your browser!

---

## 👥 Team
- **Participant 1**: Lead Developer & System Architecture
- **Participant 2**: Frontend & UI/UX Experience
- **Participant 3**: Datasets, Quality Assurance & Documentation

*SVNIT Surat — UNCHARTED 2026*
