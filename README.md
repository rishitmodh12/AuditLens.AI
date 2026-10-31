# 🔍 AuditLens AI — Enterprise Policy & Contract Intelligence RAG Engine

> **Built for UNCHARTED 2026 Hackathon (Track 2: RAG Engine)**  
> **Team:** Team Elite — SVNIT Surat  
> **Organized by:** NEXUS — Official DoCSE & DoAI Cell, SVNIT Surat × **MongoDB** × **n8n**  
> **Live Deployment:** [https://auditlens-ai-13xs.onrender.com](https://auditlens-ai-13xs.onrender.com)  
> **Repository:** [https://github.com/rishitmodh12/AuditLens.AI](https://github.com/rishitmodh12/AuditLens.AI)

---

## 🌟 Executive Summary

**AuditLens AI** is an enterprise-grade cross-document compliance, contract, and Service Level Agreement (SLA) intelligence engine built natively on **MongoDB Atlas Vector Search** (`$vectorSearch`) and **Google Gemini**.

When companies sign dozens of vendor agreements, customer SLAs, and regulatory playbooks, cross-referencing obligations during an audit or incident takes hours of manual legal labor. AuditLens AI automates this with mathematical rigor and deep evidentiary proof:

1. **Native Hybrid Search ($vectorSearch + Lexical Fusion)**: Combines 768-dimensional semantic embeddings with exact lexical keyword matching for clause numbers (e.g. `Section 4.2`, `Clause 3.2`), Indian Rupee penalties (`₹75,000`), and regulatory entities (`CERT-In`, `Sev-1`, `DPDP Act 2023`).
2. **Multi-Source Evidence Synthesis**: Simultaneously retrieves and synthesizes facts across disparate documents into an actionable executive brief.
3. **Verbatim Quote Verification (Strict Grounding in Code)**: Every citation returned by the LLM is programmatically checked by the backend server against the raw source chunk in MongoDB Atlas (`quote in chunk_text`). Verified citations are tagged with `🛡️ Verbatim Verified from Atlas Source`.
4. **Deterministic Compliance Health Score**: Replaces subjective guessing with a traceable mathematical scoring formula:
   $$\text{Compliance Score} = 100 - (20 \times \text{High Conflicts}) - (10 \times \text{Med Conflicts}) - (10 \times \text{Unverified Quotes})$$
5. **Threshold-Gated Refusal Guardrails**: Automatically detects and refuses out-of-scope queries (e.g., drone surveillance over data centers) when semantic similarity falls below the confidence threshold, suppressing speculation.
6. **Cross-Contract Contradiction Detection**: Dynamically inspects all stored contracts in MongoDB Atlas and surfaces direct legal contradictions (e.g., Customer SLA 1.0-hour downtime allowance vs. Vendor 4.0-hour maintenance window; ₹75,000/hr SLA penalty vs. Vendor ₹50,000 liability cap).

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          USER BROWSER / EVALUATOR UI                            │
│  - Modern MongoDB Green & White Theme (Tailwind CSS, Non-Blocking Tour)         │
│  - One-Click Indian Enterprise Evaluation Scenarios                             │
│  - Clickable Inline Citations [1], [2] with Smooth Scroll to Evidence Cards     │
│  - Live Pipeline Inspector (Vector Similarity + Lexical Token Match Scores)     │
│  - Dynamic Cross-Contract Contradiction Matrix                                  │
│  - Evaluation Benchmark Harness Viewer (Recall@1: 100%, Recall@3: 100%)         │
│  - Markdown Executive Brief Exporter (.md) in Indian Standard Time (IST)        │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ REST API (JSON)
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       BACKEND CORE (Python 3.10+ / FastAPI)                     │
│  - Sliding-Window Chunking (800 chars with 120-char / 15% overlap)             │
│  - Google Gemini Embeddings (`gemini-embedding-001` @ 768 dims)                 │
│  - Hybrid Fusion: (0.70 × VectorScore) + (0.30 × LexicalKeywordScore)           │
│  - Threshold-Gated Refusal Engine (Suppresses ungrounded topics)                │
│  - Verbatim Substring Grounding Verifier (Code-level validation)                │
│  - Deterministic Algorithmic Compliance Health Scorer                           │
│  - Multi-Model Failover: gemini-3.5-flash -> gemini-3.1-flash-lite -> backoff   │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│          MongoDB Atlas Cluster        │ │           Google Gemini API           │
│  - Database: `auditlens_db`           │ │  - `gemini-3.5-flash`                 │
│  - Collection: `documents`            │ │  - `gemini-3.1-flash-lite`            │
│  - Index: `vector_index` (Cosine, 768)│ │  - Temperature: 0.1 (Strict Grounding)│
│  - Native Pipeline: `$vectorSearch`   │ │  - Strict JSON Schema Output Mode     │
│  - Collections: `users`, `history`    │ └───────────────────────────────────────┘
└───────────────────────────────────────┘
```

---

## 📊 Track 2 Formal Evaluation Benchmark

Track 2 explicitly requires evaluation of retrieval accuracy. AuditLens AI includes a formal benchmark harness accessible via the live UI and the `GET /api/evaluate` endpoint.

### Retrieval Metrics Table (Evaluated over MongoDB Atlas)

| Test ID | Evaluation Query | Target Document & Section | Top Hybrid Score | Retrieval Status | Result |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **T1** | SLA downtime penalty for a 2.0-hour outage in INR | `Customer_Enterprise_SLA_2026.pdf` (§4.2) | **0.802** | Exact Top-1 Hit | **PASS** ✅ |
| **T2** | Mandatory CERT-In statutory incident reporting timeline | `Customer_Enterprise_SLA_2026.pdf` (§2.4) | **0.903** | Exact Top-1 Hit | **PASS** ✅ |
| **T3** | Internal Sev-1 escalation deadline for the CISO | `Internal_Security_Incident_Policy_v4.pdf` (Cl 3.2) | **0.906** | Exact Top-1 Hit | **PASS** ✅ |
| **T4** | Emergency mitigation patch timeline for Mumbai staging | `Internal_Security_Incident_Policy_v4.pdf` (Cl 5.1) | **0.914** | Exact Top-1 Hit | **PASS** ✅ |
| **T5** | Audit log retention under Indian IT Act 2000 | `Internal_Security_Incident_Policy_v4.pdf` (Cl 7.4) | **0.893** | Exact Top-1 Hit | **PASS** ✅ |
| **T6** | Cloud vendor permitted maintenance window duration | `Cloud_Vendor_Master_Services_Agreement.pdf` (Art 4.1) | **0.896** | Exact Top-1 Hit | **PASS** ✅ |
| **T7** | Cloud vendor maximum liability cap in INR | `Cloud_Vendor_Master_Services_Agreement.pdf` (Art 8.5) | **0.860** | Exact Top-1 Hit | **PASS** ✅ |
| **T8** | Commercial drone surveillance policy over data centers | *None (Out-of-Scope Negative Test Query)* | **0.674** | Correctly Refused | **PASS** ✅ |

### Benchmark Summary Statistics
- **Total Test Queries:** 8
- **Recall@1:** **1.0 (100%)**
- **Recall@3:** **1.0 (100%)**
- **Refusal Accuracy on Negative Path:** **1.0 (100%)**
- **Overall Precision:** **1.0 (100%)**

---

## 🇮🇳 Realistic Indian Business & Regulatory Context

All seed documents, examples, and calculations are adapted specifically to Indian enterprise operations:

### 1. Customer Enterprise Master SLA (`Customer_Enterprise_SLA_2026.pdf`)
- **Uptime Target:** 99.90% monthly availability across Indian banking networks; 1.0 hour cumulative monthly allowance (§1.1).
- **Service Credit Penalty Arithmetic (§4.2):**
  - Outage within permitted allowance (≤ 1.0 hr): **₹0 penalty**.
  - Outage exceeding allowance: **₹75,000 for each full hour beyond 1.0 hr**.
  - **2.0-hour outage:** $2.0 - 1.0 = 1.0\text{ billable hour} = \mathbf{₹75,000}$.
  - **3.0-hour outage:** $3.0 - 1.0 = 2.0\text{ billable hours} = \mathbf{₹1,50,000}$.
  - Maximum monthly liability cap: **₹3,75,000**.
- **Incident Notification (§2.4):** Dual-track reporting:
  - External Statutory: Mandatory reporting to **CERT-In** (`incident@cert-in.org.in`) within **6.0 hours** under CERT-In Directions 2022.
  - Customer Notice: Formal advisory to customer contacts within **45 minutes**.

### 2. Internal Security Incident Policy (`Internal_Security_Incident_Policy_v4.pdf`)
- **Sev-1 Escalation (Clause 3.2):** SRE Commander must notify CISO and VP Engineering within **30 minutes**.
- **Emergency Patch (Clause 5.1):** Mitigation deployed to AWS Mumbai (`ap-south-1`) staging within **2.0 hours**.
- **Evidence Preservation (Clause 7.4):** 365-day tamper-evident log retention complying with the **Indian Information Technology Act, 2000**.

### 3. Cloud Vendor MSA (`Cloud_Vendor_Master_Services_Agreement.pdf`)
- **Permitted Maintenance (Article 4.1):** Up to **4.0 hours** maintenance window with zero vendor liability. *(Direct operational conflict with Customer SLA max 1.0 hour)*.
- **Data Sovereignty (Article 6.3):** Full compliance with the **Digital Personal Data Protection (DPDP) Act, 2023**; data must strictly reside in AWS Asia-Pacific Mumbai (`ap-south-1`).
- **Liability Cap (Article 8.5):** Vendor total aggregate liability is capped at **₹50,000 total**. *(Direct financial conflict with Customer SLA penalty of ₹75,000/hr and cap of ₹3,75,000)*.
- **Jurisdiction (Article 11.2):** Commercial arbitration seated in Mumbai under the **Indian Arbitration and Conciliation Act, 1996**.

> *Transparency Disclosure: The pre-loaded contracts are synthetic Indian enterprise agreements engineered specifically for stressful due-diligence demonstration, multi-source synthesis, and contradiction discovery.*

---

## ⚡ Quick Demo Queries for Evaluators

1. **🌐 Multi-Source Synthesis & Exact Arithmetic:**  
   *Query:* `"If an outage reaches 2.0 hours on our Indian banking payment gateway, what is the customer SLA penalty under Section 4.2, and what are the respective deadlines for internal CISO escalation and statutory CERT-In reporting?"`  
   *Response:* Cites Customer SLA §4.2 (1 penalty hour = ₹75,000), Security Policy Clause 3.2 (CISO escalation within 30 minutes), and SLA §2.4 (CERT-In reporting within 6 hours).
2. **⚠️ Cross-Contract Contradiction Detection:**  
   *Query:* `"Are there contradictory terms between our Customer Enterprise SLA and Cloud Vendor Agreement regarding permitted maintenance downtime and liability caps?"`  
   *Response:* Surfaces high-risk conflict between Customer SLA (1-hr allowed downtime, ₹75,000/hr penalty) and Vendor MSA (4-hr maintenance window, ₹50,000 liability cap).
3. **🛡️ Hallucination Guardrail (Negative Path Refusal):**  
   *Query:* `"What is the policy for commercial drone surveillance over data centers?"`  
   *Response:* Safely refuses with mathematical threshold proof (out of scope for indexed contracts).

---

## 🚀 Local Setup & Installation

### Prerequisites
- Python 3.10+
- MongoDB Atlas Cluster with Vector Search enabled
- Google Gemini API Key

### 1. Clone the Repository
```bash
git clone https://github.com/rishitmodh12/AuditLens.AI.git
cd AuditLens.AI
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
GEMINI_MODEL="gemini-3.5-flash"
EMBEDDING_MODEL="gemini-embedding-001"
```

### 4. Configure Atlas Vector Search Index
In MongoDB Atlas -> **Atlas Search & Vector Search** -> **Create Search Index** -> **JSON Editor**:
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

### 5. Launch the Application
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
Open **`http://127.0.0.1:8000`** in your browser.

---

## 👥 UNCHARTED 2026 — Team Elite
- **Institution:** Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat
- **Track:** Track 2 — RAG Engine
- **Technologies:** MongoDB Atlas Vector Search (`$vectorSearch`), Google Gemini API, FastAPI, Tailwind CSS, Python 3.10+
