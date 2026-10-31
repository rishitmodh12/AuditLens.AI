# API Documentation: AuditLens AI
**UNCHARTED 2026 | Track 2: RAG Engine**  
**Team Elite (SVNIT Surat): Rishit Modh, Bhavya Juneja, Sugandh Jha**  
**Base URL (Live Production):** `https://auditlens-ai-13xs.onrender.com`  
**Base URL (Local Development):** `http://127.0.0.1:8000`

---

## 1. Overview

AuditLens AI exposes a structured RESTful API implemented using **FastAPI**. All data payloads are validated via **Pydantic** models. Endpoints adhere to standard HTTP status codes and return JSON responses with UTF-8 encoding.

---

## 2. API Endpoints

### 2.1 System Health
`GET /api/health`

Verifies that the FastAPI server is running and confirms active connectivity to the MongoDB Atlas cluster.

#### Response (200 OK)
```json
{
  "status": "healthy",
  "database": "auditlens_db",
  "mongodb_connected": true,
  "indexed_documents_count": 3,
  "total_vector_chunks": 12
}
```

---

### 2.2 Cross-Document Audit Query
`POST /api/query`

Executes the full Track 2 RAG pipeline:
1. Calculates 768-dimensional dense vector embeddings.
2. Runs native MongoDB Atlas Hybrid Search (`$vectorSearch` + Lexical token boost).
3. Evaluates evidence with Gemini 1.5 Flash.
4. Programmatically verifies citation quotes against raw Atlas chunks.
5. Derives deterministic Compliance Health Score.

#### Request Body
```json
{
  "query": "If an outage reaches 2.0 hours on our Indian banking payment gateway, what is the customer SLA penalty under Section 4.2, and what are the respective deadlines for internal CISO escalation and statutory CERT-In reporting?",
  "limit": 5,
  "user_email": "auditor@enterprise.in"
}
```

#### Response (200 OK)
```json
{
  "query": "If an outage reaches 2.0 hours on our Indian banking payment gateway, what is the customer SLA penalty under Section 4.2, and what are the respective deadlines for internal CISO escalation and statutory CERT-In reporting?",
  "is_answerable": true,
  "summary": "For a 2.0-hour outage, the customer SLA penalty is ₹75,000. Incident notification timelines require internal CISO escalation within 30 minutes, customer notice within 45 minutes, and statutory CERT-In reporting within 6.0 hours.",
  "compliance_score": 80,
  "score_calculation_breakdown": "Algorithmic Formula: 100 - (High Conflicts: 1 × 20) - (Med Conflicts: 0 × 10) - (Unverified Quotes: 0 × 10) = 80%",
  "detailed_findings": [
    {
      "severity": "MEDIUM RISK",
      "text": "A 2.0-hour outage results in a billable penalty of ₹75,000, calculated as (2.0 - 1.0) hours of excess downtime at a rate of ₹75,000 per hour [4].",
      "citations": [4]
    },
    {
      "severity": "HIGH RISK",
      "text": "The mandatory notification timeline for CERT-In is 6.0 hours [1], [2], while internal escalation to the CISO and VP Engineering must occur within 30 minutes [2], and customer outage notices must be issued within 45 minutes [1].",
      "citations": [1, 2]
    }
  ],
  "conflicts_detected": [
    {
      "title": "Liability and Maintenance Window Discrepancy",
      "doc_a": "Customer_Enterprise_SLA_2026.pdf",
      "doc_a_clause": "1.0 hour monthly downtime allowance with ₹3,75,000 liability cap",
      "doc_b": "Vendor MSA (Contextual Reference)",
      "doc_b_clause": "4.0 hour maintenance window with ₹50,000 liability cap",
      "risk_analysis": "The Vendor MSA provides a significantly lower liability cap and a longer maintenance window than the Customer SLA, creating a potential breach of contract if the Provider relies on MSA terms during a customer-facing outage.",
      "remediation_recommendation": "Amend the Vendor MSA to align with the Customer SLA liability caps and downtime thresholds to ensure consistency across all legal agreements.",
      "severity": "HIGH"
    }
  ],
  "citations": [
    {
      "ref_id": 1,
      "doc_name": "Customer_Enterprise_SLA_2026.pdf",
      "section": "Section 4.2: Service Credit Penalties & Liability",
      "quote": "a 2.0 hour outage incurs 1 penalty hour (2.0 - 1.0 = 1.0 hr) totaling ₹75,000",
      "quote_verified": true,
      "chunk_id": "Customer_Enterprise_SLA_2026.pdf_chunk_3"
    },
    {
      "ref_id": 2,
      "doc_name": "Internal_Security_Incident_Policy_v4.pdf",
      "section": "Clause 3.2: Incident Severity & Escalation",
      "quote": "SRE Incident Commander must notify the CISO, VP of Engineering, and Legal Counsel within thirty (30) minutes of alert confirmation.",
      "quote_verified": true,
      "chunk_id": "Internal_Security_Incident_Policy_v4.pdf_chunk_1"
    }
  ],
  "telemetry": {
    "hybrid_top_scores": [
      {
        "chunk_id": "Customer_Enterprise_SLA_2026.pdf_chunk_3",
        "doc_name": "Customer_Enterprise_SLA_2026.pdf",
        "section": "Section 4.2: Service Credit Penalties & Liability",
        "hybrid_score": 0.884,
        "vector_score": 0.834,
        "lexical_score": 1.0,
        "matched_tokens": ["4.2", "₹75,000"]
      }
    ]
  }
}
```

---

### 2.3 Dynamic Conflict Matrix Scanner
`GET /api/conflicts/scan`

Scans all active contracts stored in MongoDB Atlas, evaluates pairwise commitments, and outputs identified discrepancies.

#### Response (200 OK)
```json
{
  "scan_timestamp": "2026-10-31T17:42:00.000Z",
  "total_discrepancies": 3,
  "discrepancies": [
    {
      "id": "DISC-001",
      "title": "Permitted Maintenance Window vs Cumulative Monthly Downtime",
      "severity": "CRITICAL",
      "doc_a": {
        "name": "Customer_Enterprise_SLA_2026.pdf",
        "clause": "Section 1.1",
        "excerpt": "Total cumulative unscheduled downtime across any single calendar month shall not exceed 1.0 hour (60 minutes). Penalty of ₹75,000/hr applies thereafter."
      },
      "doc_b": {
        "name": "Cloud_Vendor_Master_Services_Agreement.pdf",
        "clause": "Article 4.1",
        "excerpt": "Vendor reserves the right to conduct scheduled infrastructure maintenance and emergency repairs for up to 4.0 hours per window with zero penalty."
      },
      "business_risk": "If the cloud vendor exercises a 3.0-hour maintenance window, the enterprise incurs a ₹1,50,000 customer SLA breach liability while recovering ₹0 from the vendor.",
      "remediation": "Amend Article 4.1 of the Vendor MSA to restrict maintenance to non-business hours (< 1.0 hour per window) or insert a pass-through downtime exclusion into the Customer SLA."
    }
  ]
}
```

---

### 2.4 Empirical Evaluation Benchmark Harness
`GET /api/evaluate`

Executes the automated 8-query empirical evaluation suite directly against MongoDB Atlas, reporting Recall@1, Recall@3, and Refusal Accuracy.

#### Response (200 OK)
```json
{
  "benchmark_timestamp": "2026-10-31T17:47:30.150Z",
  "total_test_queries": 8,
  "recall_at_1": 1.0,
  "recall_at_3": 1.0,
  "refusal_accuracy": 1.0,
  "overall_precision": 1.0,
  "results": [
    {
      "id": "T1",
      "query": "What is the penalty for a 2-hour SLA outage in INR?",
      "expected": "Customer_Enterprise_SLA_2026.pdf (Section 4.2)",
      "top_retrieved": "Customer_Enterprise_SLA_2026.pdf (Section 4.2: Service Credit Penalties & Liability)",
      "top_score": 0.802,
      "status": "PASS (Exact Hit)"
    },
    {
      "id": "T2",
      "query": "What is the mandatory CERT-In statutory incident reporting timeline?",
      "expected": "Customer_Enterprise_SLA_2026.pdf (Section 2.4)",
      "top_retrieved": "Customer_Enterprise_SLA_2026.pdf (Section 2.4: Outage Notification Protocol)",
      "top_score": 0.903,
      "status": "PASS (Exact Hit)"
    },
    {
      "id": "T8",
      "query": "What is the policy for commercial drone surveillance over data centers?",
      "expected": "REFUSAL (Out-of-Scope Ungrounded Request)",
      "top_retrieved": "SAFE_REFUSAL_TRIGGERED",
      "top_score": 0.584,
      "status": "PASS (Correctly Refused Out-of-Scope)"
    }
  ]
}
```

---

### 2.5 Knowledge Base Document Management

#### List Documents
`GET /api/documents`
Returns all indexed enterprise contracts with total chunk counts.

#### Upload New Document
`POST /api/upload_file`
Accepts `multipart/form-data`:
- `file`: PDF, TXT, or Markdown binary.
- `category`: String classification tag.
- `user_email`: Session identifier.

#### Delete Document
`DELETE /api/documents/{doc_id}`
Deletes all vector chunks and parent metadata for the specified document ID from MongoDB Atlas.

#### Re-Seed Default Data
`POST /api/seed_sample_data`
Resets the Atlas collection to the 3 standard Indian enterprise agreements (12 chunks).

---

### 2.6 Audit History Management

#### Get History
`GET /api/history?user_email={email}`
Returns user audit history with timestamps formatted in **IST (`Asia/Kolkata`)**.

#### Clear History
`DELETE /api/history?user_email={email}`
Deletes audit records for the specified user session.
