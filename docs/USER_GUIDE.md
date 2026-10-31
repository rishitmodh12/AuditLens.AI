# User Guide: AuditLens AI
**UNCHARTED 2026 | Track 2: RAG Engine**  
**Team Elite (SVNIT Surat): Rishit Modh, Bhavya Juneja, Sugandh Jha**  
**Live URL:** [https://auditlens-ai-13xs.onrender.com](https://auditlens-ai-13xs.onrender.com)

---

## 1. Quick Start Walkthrough

Welcome to AuditLens AI! When you first open the application, an **interactive step-by-step tutorial** will automatically guide you through the interface. You can follow the spotlights or click **"Skip Tutorial"** at any time.

### Logging In as an Auditor Persona
Click the **"Auditor Sign-In"** button in the top navigation bar. You can choose from three pre-configured demo personas:
1. **Lead Compliance Auditor (FinOps):** Evaluates service credit liabilities and SLA uptime compliance.
2. **Legal & Regulatory Counsel:** Evaluates cross-contract contradictions and statutory CERT-In adherence.
3. **SVNIT Hackathon Judge (Evaluation Profile):** Inspects technical RAG retrieval, pipeline telemetry, and empirical benchmark recall.

---

## 2. Tab 1: Audit & Search Console

The Audit & Search Console is your primary workspace for performing natural language legal queries.

### Using 1-Click Evaluation Scenarios
Below the header, three pre-configured scenarios let you immediately test Track 2 core capabilities:
- **Scenario 1: Multi-Source Synthesis (SLA + CERT-In)**
  - *Query:* `"If an outage reaches 2.0 hours on our Indian banking payment gateway, what is the customer SLA penalty under Section 4.2, and what are the respective deadlines for internal CISO escalation and statutory CERT-In reporting?"`
  - *Expected Result:* Reconciled penalty of **₹75,000** for 2.0 hours ($(2.0 - 1.0\text{ hr grace}) \times ₹75,000$). Explicit differentiation between internal 30-min CISO escalation, 45-min customer notice, and statutory 6.0-hour CERT-In reporting.
- **Scenario 2: Contract Contradiction (SLA vs Cloud MSA)**
  - *Query:* `"Are there contradictory terms between our Customer Enterprise SLA and Cloud Vendor Agreement regarding permitted maintenance downtime and liability caps?"`
  - *Expected Result:* Flags High-Severity contradiction: Customer SLA allows max 1.0 hr downtime/month, but Cloud Vendor MSA allows 4.0 hr maintenance windows with zero penalty.
- **Scenario 3: Hallucination Defense (Negative Test)**
  - *Query:* `"What is the policy for commercial drone surveillance over data centers?"`
  - *Expected Result:* Safe refusal with audit guardrails: confirms drone surveillance is ungrounded in indexed agreements and suppresses speculative generation.

### Reading Audit Results
When a query executes:
1. **Executive Summary Card:** Displays the synthesized finding, the **`🛡️ Verbatim Verified Grounding`** badge, the algorithmic **Compliance Health Score**, and the count of retrieved Atlas chunks.
2. **Verified Factual Findings:** Bulleted findings tagged with severity levels (`CRITICAL`, `HIGH RISK`, `MEDIUM RISK`, `LOW RISK`). Each finding includes clickable inline reference badges (e.g. `[1]`, `[2]`).
3. **Click-to-Highlight Citations:** Clicking an inline badge (`[1]`) smoothly scrolls down to the corresponding citation card and highlights it with a green border ring (`.ring-4`).
4. **Verifiable Source Cards:** Display exact verbatim quotes from the agreement, marked with the **`🛡️ Verbatim Verified from Atlas Source`** badge.
5. **MongoDB Atlas Pipeline Inspector:** Click to expand the accordion at the bottom to inspect raw cosine similarity scores, lexical token boost scores, and MongoDB chunk IDs.

---

## 3. Tab 2: Cross-Contract Conflict Matrix

Click the **"Cross-Contract Conflict Matrix"** tab in the navigation bar.

1. AuditLens AI automatically calls the `/api/conflicts/scan` endpoint to dynamically evaluate all indexed contracts in MongoDB Atlas.
2. The matrix displays identified discrepancies with:
   - **Discrepancy Title & Severity:** e.g., *Permitted Maintenance Window vs Customer Downtime (HIGH RISK)*.
   - **Document A vs Document B Comparison:** Side-by-side comparison of conflicting clauses with exact section references.
   - **Business Risk Analysis:** Explanation of financial and operational exposure.
   - **Remediation Recommendation:** Proposed contract amendment to harmonize terms prior to signing.

---

## 4. Tab 3: Knowledge Base & Document Upload

Click the **"Knowledge Base & Document Upload"** tab.

### Inspecting Indexed Contracts
View all enterprise documents currently indexed in MongoDB Atlas `auditlens_db`:
- Document title, category, total vector chunks, and indexing status.
- Each document card has a **Delete (🗑️)** button to remove its chunks from MongoDB Atlas.

### Uploading New Contracts
1. Drag and drop or browse to select any PDF, TXT, or Markdown contract (up to 10 MB).
2. The engine automatically:
   - Extracts and cleans the document text.
   - Segments clauses using 15% sliding window overlap chunking.
   - Generates 768-dimensional dense vector embeddings via `all-mpnet-base-v2`.
   - Inserts chunks into MongoDB Atlas collection `documents`.
3. The new document immediately becomes searchable in the Audit & Search Console.

---

## 5. Tab 4: Audit History

Click the **"Audit History"** tab to review previous queries run during your session:
- Displays each query, the compliance health score, timestamp formatted in **Indian Standard Time (IST, `Asia/Kolkata`)**, and total chunks evaluated.
- Click any past audit to re-populate the findings in the Audit Console.
- Click **"Clear History"** to reset your session log.

---

## 6. Live Evaluation Benchmark Modal

Click the **"📊 Recall Benchmark (100%)"** button in the top navigation bar.

1. AuditLens AI executes a live empirical evaluation test across 8 standardized queries (`GET /api/evaluate`).
2. The modal displays:
   - **Recall@1:** Exact top-rank retrieval precision (`100%`).
   - **Recall@3:** Top-3 retrieval coverage (`100%`).
   - **Refusal Accuracy:** Out-of-scope query defense (`100%`).
   - **Grounding Precision:** Verbatim citation validation (`100%`).
3. An itemized table displays each query ID (T1–T8), target clause, top hybrid score, and benchmark status (`PASS (Exact Hit)`).
4. Click **"Re-run Benchmark ↺"** at any time to re-test the live MongoDB Atlas cluster.

---

## 7. Exporting an Executive Audit Brief

Click the **"Export Brief"** button in the header.

AuditLens AI generates and downloads a professional, timestamped **Executive Audit Brief** in Markdown format (`.md`). The exported brief includes:
- Executive Summary & Compliance Health Score.
- Verified Factual Findings with Risk Levels.
- Cross-Contract Contradictions & Recommended Amendments.
- Grounded Legal Citations with Exact Quotes.
- Audit Metadata: Session User, Timestamp (IST), and MongoDB Atlas Vector Search telemetry.
