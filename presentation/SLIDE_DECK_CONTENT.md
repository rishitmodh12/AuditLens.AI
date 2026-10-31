# AuditLens AI: Official 8-Slide Hackathon Presentation Deck
**UNCHARTED 2026 | Track 2: RAG Engine**  
**Team Elite (SVNIT Surat): Rishit Modh, Bhavya Juneja, Sugandh Jha**  
**Live URL:** https://auditlens-ai-13xs.onrender.com  
**GitHub:** https://github.com/rishitmodh12/AuditLens.AI  

---

## Slide 1: Title & Project Introduction
- **Project Name:** AuditLens.AI
- **Tagline:** Real-Time Cross-Contract Due Diligence & Discrepancy Engine Grounded with MongoDB Atlas Native Vector Search (`$vectorSearch`)
- **Event & Track:** UNCHARTED 2026 | Track 2: RAG Engine
- **Team Name:** Team Elite (SVNIT Surat)
- **Team Members & Responsibilities:**
  - **Rishit Modh:** RAG Engine Architecture, MongoDB Atlas `$vectorSearch`, Hybrid Search Fusion (Dense + Lexical)
  - **Bhavya Juneja:** Interactive Frontend, Telemetry Inspector, Evaluation Benchmark Harness UI
  - **Sugandh Jha:** Compliance Rule Formulation, Indian Regulatory Datasets (CERT-In, DPDP Act 2023), Cross-Contract Conflict Matrix
- **Key Links:**
  - Live Production Deployment: `https://auditlens-ai-13xs.onrender.com`
  - GitHub Repository: `https://github.com/rishitmodh12/AuditLens.AI`

### Slide 1 Speaker Notes:
> "Good evening, esteemed judges, mentors, and the NEXUS SVNIT organizing team! We are Team Elite, and we are thrilled to present AuditLens AI for Track 2. In modern enterprise operations, companies sign hundreds of overlapping agreements: customer SLAs, cloud vendor contracts, and regulatory security policies. These documents frequently contradict one another—creating millions of rupees in uncollected vendor credits or exposing the company to severe regulatory fines. AuditLens AI transforms static contract repositories into active, mathematically reconciled, and verifiable compliance intelligence powered by MongoDB Atlas Vector Search."

---

## Slide 2: Problem Statement & Its Importance
- **Track Context:** Track 2 (RAG Engine) requires turning source material into grounded, useful results, citing multiple sources, and cleanly handling unanswerable requests.
- **The Enterprise Crisis (4 Key Challenges):**
  1. **Multi-Document Disconnect:** Customer SLAs guarantee 99.9% uptime (max 1.0 hr monthly downtime), while upstream Cloud Vendor MSAs permit 4.0-hour maintenance windows with zero penalty. Enterprises silently absorb catastrophic SLA breach liabilities.
  2. **Statutory Indian Regulatory Mandates:** Under CERT-In's Cyber Security Directions 2022, security incidents must be reported externally within 6 hours. Companies risk criminal prosecution under IT Act §70B if internal and statutory notification clocks fall out of sync.
  3. **Financial Service Credit Leakage:** SLA penalty formulas are complex. A 2.0-hour payment gateway outage incurs ₹75,000 under Section 4.2. Without automated cross-document reconciliation, enterprises fail to claim vendor indemnities.
  4. **LLM Hallucination Risk:** Generic LLM chatbots hallucinate nonexistent clauses and miss numbers. In high-stakes legal audits, answers must carry 100% verbatim quotes verified directly against database records.

### Slide 2 Speaker Notes:
> "The Track 2 problem statement calls for multi-source evidence retrieval and grounded synthesis. In the real world, this is where enterprises suffer the most. When an IT outage occurs, legal and engineering teams waste hours searching disparate documents for breach obligations, maintenance allowances, and penalty formulas. Traditional keyword search misses semantic context, while standard LLMs hallucinate clauses or confuse internal 30-minute CISO escalation with external 6-hour CERT-In rules. AuditLens AI eliminates this exposure completely."

---

## Slide 3: Our Proposed Solution: AuditLens AI
- **Core Concept:** An end-to-end, enterprise-ready cross-contract discrepancy and due diligence engine.
- **Key Solution Pillars:**
  1. **Multi-Source Conflict Detection:** Concurrently scans customer SLAs, vendor agreements, and internal policies to identify contradictory clauses, mismatched liability caps, and divergent notification timelines.
  2. **Programmatic Verbatim Quote Verification:** Code-level substring validation that verifies every LLM citation against raw MongoDB Atlas text. Verified citations receive a tamper-proof `🛡️ Verbatim Verified from Atlas Source` badge.
  3. **Strict Ungrounded Query Refusal:** Fulfills Track 2's negative constraint: queries outside the contract domain (e.g. drone surveillance over data centers) trigger strict refusal with zero hallucination.
  4. **Deterministic Compliance Health Score:** Replaces arbitrary scores with a deterministic mathematical formula:  
     $$\text{Score} = 100 - (20 \times \text{High Conflicts}) - (10 \times \text{Med Conflicts}) - (10 \times \text{Unverified Quotes})$$
- **Target Personas:**
  - **Legal Counsel:** Rapidly audit vendor agreements before signing.
  - **FinOps & SRE Teams:** Accurately calculate and dispute outage liabilities.
  - **CISO & Compliance Officers:** Enforce CERT-In and DPDP Act 2023 compliance.

### Slide 3 Speaker Notes:
> "AuditLens AI solves this dilemma through three technical pillars: First, multi-source conflict detection across disparate legal agreements. Second, code-level verbatim quote verification where every citation is string-checked against the raw text in MongoDB Atlas to eliminate hallucinations. Third, strict refusal guardrails that identify out-of-scope requests. This turns hours of tedious contract review into seconds."

---

## Slide 4: How Our Platform Works: End-to-End Workflow
- **Step 1: Multi-Document Ingestion & Overlap Chunking**
  - Upload contracts in PDF, DOCX, or TXT format.
  - Text is extracted, cleaned, and segmented using paragraph awareness with 15% sliding window overlap to ensure legal conditions spanning paragraph breaks are never severed.
- **Step 2: Dense Vector Indexing in MongoDB Atlas**
  - Generates 768-dimensional dense vector embeddings using `sentence-transformers/all-mpnet-base-v2` locally (zero external API latency or cost).
  - Stores chunks, embeddings, and metadata (`doc_name`, `section`, `clause`, `category`) directly in MongoDB Atlas collection `documents`.
- **Step 3: Native Hybrid Search Fusion (70/30)**
  - Executes MongoDB Atlas `$vectorSearch` (70% semantic weight) fused with exact keyword token matching (30% weight) for clause numbers (`§4.2`, `§3.2`) and ₹ INR amounts.
- **Step 4: Dual-Track LLM Reasoning**
  - Google Gemini 1.5 Flash cross-examines evidence across documents, identifies SLA discrepancies, calculates penalties, and formats JSON citations.
- **Step 5: Verbatim Verification & Report Export**
  - Backend string-matches citations against raw Atlas text, computes deterministic Compliance Health Score, and formats IST reports.

### Slide 4 Speaker Notes:
> "Here is our end-to-end pipeline. Documents are chunked with sentence boundary awareness and 15% sliding overlap so legal conditions spanning paragraphs aren't lost. Vectors are stored in MongoDB Atlas. When an auditor runs an audit query, our hybrid retrieval pipeline scores candidates with both semantic embeddings and exact lexical tokens. Gemini 1.5 Flash reasons across the retrieved evidence, and our backend performs verbatim string verification before displaying the final results."

---

## Slide 5: Technical Architecture & Technology Stack
- **Database & Search:**
  - **MongoDB Atlas (AWS Region M0 Cluster):** Native `$vectorSearch` pipeline, 768-dimension cosine index, metadata filters (`doc_id`, `category`), and audit history storage.
- **Backend & RAG Engine:**
  - **FastAPI (Python 3.14) & Uvicorn:** Async REST endpoints, Pydantic validation schemas, PyPDF document ingestion.
  - **Hybrid Search Fusion:** Custom 70% dense + 30% lexical token weighting algorithm.
- **AI & Embedding Models:**
  - **Local Embeddings:** `sentence-transformers/all-mpnet-base-v2` (768-dim, local inference, zero API quota limitations).
  - **Generative Synthesis:** Google Gemini 1.5 Flash with strict JSON schema enforcement and ground-truth validation.
- **Frontend & UI/UX:**
  - **Tailwind CSS + Vanilla JS:** MongoDB-inspired forest green design palette, responsive tabs, telemetry inspector, non-blocking interactive tutorial walkthrough.
- **Production Hosting:**
  - **Render Cloud:** Dockerized container service running live with continuous Git deployment.

### Slide 5 Speaker Notes:
> "Our technical architecture is built for enterprise stability. MongoDB Atlas serves as both our document store and native vector search engine. By using all-mpnet-base-v2, we generate embeddings locally with zero latency, while Google Gemini Flash handles multi-document reasoning. The entire stack is containerized and running in production on Render."

---

## Slide 6: Key Features & Track 2 Innovation
- **1. Native Hybrid Search (Dense + Lexical 70/30 Fusion):**
  - Standard vector search struggles with exact legal numbers (`§4.2`, `₹75,000`). Our hybrid fusion solves this by combining cosine distance with exact token matching.
- **2. Reconciled Contract Outage Arithmetic:**
  - Accurately applies contractual grace periods: $(2.0\text{ hrs} - 1.0\text{ hr grace}) \times ₹75,000 = ₹75,000$ penalty. Eliminates calculation mismatches.
- **3. Dual-Track CERT-In vs Internal Escalation:**
  - Explicitly differentiates external statutory CERT-In reporting (**6.0 hours** under Cyber Security Directions 2022) vs internal Sev-1 CISO escalation (**30 minutes**) vs customer notice (**45 minutes**).
- **4. Dynamic Cross-Contract Conflict Matrix:**
  - Real-time scanner (`/api/conflicts/scan`) comparing multi-party contracts for downtime and liability cap mismatches.
- **5. Deterministic Compliance Health Score:**
  - Calculated mathematically from detected conflicts: $\text{Score} = 100 - (20 \times \text{High}) - (10 \times \text{Med}) - (10 \times \text{Unverified})$.
- **6. 100% Verbatim Quote Verification Badge:**
  - Programmatically verifies citation excerpts against source chunks; verified quotes receive `🛡️ Verbatim Verified from Atlas Source`.

### Slide 6 Speaker Notes:
> "What separates AuditLens AI from generic RAG wrappers is technical depth. First, our 70/30 hybrid search solves the classic RAG limitation with exact numbers and clause references. Second, we reconciled the arithmetic for SLA downtime: a 2-hour outage minus 1-hour grace equals ₹75,000. Third, we explicitly differentiated internal 30-minute CISO escalation from the 6-hour CERT-In statutory clock. And finally, our compliance score is 100% deterministic, calculated from detected conflicts."

---

## Slide 7: Results, Empirical Validation & Real-World Impact
- **Track 2 Evaluation Benchmark Results (Live at `/api/evaluate`):**
  - **Recall@1 (Top Rank Hit):** **100%** (7 out of 7 positive test queries retrieved the exact target clause as Rank 1).
  - **Recall@3 (Top-3 Retrieval):** **100%** (All relevant evidence retrieved in top 3 results).
  - **Out-of-Scope Refusal Accuracy:** **100%** (Commercial drone surveillance query safely refused with zero hallucination).
  - **Grounding Precision:** **100%** (All citations verified verbatim against MongoDB Atlas chunks).
  - **Average Latency:** **~1.2 seconds end-to-end**.
- **Real-World Indian Enterprise Use Cases:**
  - **FinTech & Digital Banking (UPI / Payment Gateways):** Automated SLA penalty claims when downstream cloud providers experience unscheduled downtime.
  - **CERT-In Statutory Readiness:** Enforcing mandatory 6.0-hour cyber incident reporting windows under Indian IT Act §70B.
  - **DPDP Act 2023 Compliance:** Cross-auditing vendor data processing agreements for data sovereignty and breach notifications.

### Slide 7 Speaker Notes:
> "Judges can verify our evaluation benchmark live by clicking the Recall Benchmark button or hitting the /api/evaluate endpoint. We test 8 comprehensive queries covering SLA outage math, CERT-In compliance, CISO escalations, Mumbai staging patch windows, and IT Act log retention. The results: 100% Recall at 1, 100% Recall at 3, and 100% Refusal Accuracy on our unanswerable drone query. This fulfills the Track 2 testing requirement completely."

---

## Slide 8: Future Scope & Conclusion
- **Future Product Roadmap:**
  1. **n8n Automated Incident Workflows:** Native webhook integration triggering automated incident tickets in Jira, notifying PagerDuty, and posting to Slack when High-Risk contract discrepancies are flagged.
  2. **Multi-Party Clause Redlining:** Generative contract renegotiation assistant suggesting harmonized legal language to bridge customer SLAs and vendor agreements prior to contract signing.
  3. **Dedicated MongoDB Atlas Scaling:** Sharded clusters on Atlas M10+ for multi-million document legal corpora with real-time change stream sync.
  4. **Enterprise SSO & RBAC:** Role-based document partition and active directory integration.
- **Conclusion:**
  - Team Elite delivered an end-to-end, fully deployed, 100% validated RAG engine built on MongoDB Atlas.
  - **Live Demo:** https://auditlens-ai-13xs.onrender.com
  - **GitHub Repository:** https://github.com/rishitmodh12/AuditLens.AI
  - **Team Elite:** Rishit Modh • Bhavya Juneja • Sugandh Jha (SVNIT Surat)

### Slide 8 Speaker Notes:
> "To conclude, Team Elite has delivered an end-to-end, grounded RAG solution that solves a real enterprise problem in the Indian regulatory ecosystem. We have addressed every piece of feedback: hybrid search, verbatim verification, arithmetic reconciliation, CERT-In compliance, and an empirical evaluation harness. Thank you, judges, mentors, and the NEXUS SVNIT team! We are now open for your questions."
