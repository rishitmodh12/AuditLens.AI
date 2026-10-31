# Testing & Validation Report: AuditLens AI
**UNCHARTED 2026 | Track 2: RAG Engine**  
**Team Elite (SVNIT Surat): Rishit Modh, Bhavya Juneja, Sugandh Jha**  
**Evaluation Date:** 31 October 2026  
**Live Endpoint:** `https://auditlens-ai-13xs.onrender.com/api/evaluate`

---

## 1. Executive Summary

To satisfy the rigorous evaluation standards of UNCHARTED 2026 (Track 2: RAG Engine), Team Elite designed and implemented an automated **Empirical Evaluation Benchmark Harness**. 

Rather than relying on qualitative impressions or subjective ratings, AuditLens AI subjects its retrieval pipeline to **8 standardized test queries (T1–T8)** that assess:
1. **Dense vs Exact Token Retrieval:** Precision in fetching specific clauses (`§4.2`, `§3.2`) and currency figures (`₹75,000`).
2. **Multi-Source Synthesis:** Synthesizing evidence across disparate agreements (SLA + Security Policy + Vendor MSA).
3. **Out-of-Scope Refusal Accuracy:** Detecting ungrounded queries (commercial drone surveillance) and cleanly refusing them without hallucination.
4. **Programmatic Grounding Verification:** Verifying that citation excerpts exist verbatim in raw MongoDB Atlas chunks.

### Benchmark Scorecard
| Metric | Target Standard | Achieved Result | Evaluation Verdict |
|---|---|---|---|
| **Recall@1** | $\ge 80\%$ | **100% (7/7 Positive Queries)** | 🏆 Perfect Top-Rank Retrieval |
| **Recall@3** | $\ge 90\%$ | **100% (7/7 Positive Queries)** | 🏆 Perfect Top-3 Retrieval |
| **Out-of-Scope Refusal Accuracy** | $100\%$ | **100% (1/1 Negative Query)** | 🏆 Zero Hallucination Triggered |
| **Verbatim Quote Verification** | $\ge 95\%$ | **100% Verbatim Match** | 🏆 Fully Grounded |
| **Average End-to-End Latency** | $< 2.5\text{s}$ | **~1.2 seconds** | ⚡ High Performance |

---

## 2. Standardized Benchmark Test Suite (T1–T8)

The table below documents the empirical evaluation suite executed natively against MongoDB Atlas:

| ID | Test Query | Expected Document & Section | Top Hybrid Score | Outcome Status |
|---|---|---|---|---|
| **T1** | *"What is the penalty for a 2-hour SLA outage in INR?"* | `Customer_Enterprise_SLA_2026.pdf` (§4.2) | **0.802** | ✅ **PASS (Exact Hit Rank 1)** |
| **T2** | *"What is the mandatory CERT-In statutory incident reporting timeline?"* | `Customer_Enterprise_SLA_2026.pdf` (§2.4) | **0.903** | ✅ **PASS (Exact Hit Rank 1)** |
| **T3** | *"What is the internal Sev-1 escalation deadline for the CISO?"* | `Internal_Security_Incident_Policy_v4.pdf` (§3.2) | **0.906** | ✅ **PASS (Exact Hit Rank 1)** |
| **T4** | *"What is the emergency mitigation patch deployment timeline for Mumbai staging?"* | `Internal_Security_Incident_Policy_v4.pdf` (§5.1) | **0.914** | ✅ **PASS (Exact Hit Rank 1)** |
| **T5** | *"How many days must audit logs be retained under Indian IT Act?"* | `Internal_Security_Incident_Policy_v4.pdf` (§7.4) | **0.893** | ✅ **PASS (Exact Hit Rank 1)** |
| **T6** | *"What is the cloud vendor permitted maintenance window duration?"* | `Cloud_Vendor_Master_Services_Agreement.pdf` (§4.1) | **0.896** | ✅ **PASS (Exact Hit Rank 1)** |
| **T7** | *"What is the cloud vendor maximum liability cap in INR?"* | `Cloud_Vendor_Master_Services_Agreement.pdf` (§8.5) | **0.860** | ✅ **PASS (Exact Hit Rank 1)** |
| **T8** | *"What is the policy for commercial drone surveillance over data centers?"* | **REFUSAL (Out-of-Scope Ungrounded Request)** | **0.584** | 🛡️ **PASS (Correctly Refused)** |

---

## 3. In-Depth Analysis of Key Test Scenarios

### 3.1 Arithmetic Reconciliation Verification (Test T1)
- **Input:** 2.0-hour outage on Indian banking payment gateway.
- **Contract Language (`Customer_Enterprise_SLA_2026.pdf`, §4.2):**  
  *"For unscheduled downtime exceeding 1.0 cumulative hour in a billing month, Provider shall credit Customer at the rate of ₹75,000 per billable hour. Billable downtime is calculated as: $\text{Total Outage Hours} - \text{Permitted Allowance (1.0 hr)}$."*
- **Mathematical Validation:**  
  $$\text{Billable Hours} = 2.0 - 1.0 = 1.0\text{ hr}$$  
  $$\text{Total Penalty} = 1.0 \times ₹75,000 = \mathbf{₹75,000}$$
- **Verification:** The model accurately outputs ₹75,000 in its headline summary, factual findings, and citation annotations. The previous calculation discrepancy (₹1,50,000, which applies to a 3-hour outage) is completely reconciled.

---

### 3.2 Dual-Track Statutory Notification Clocks (Test T2 & T3)
- **Legal Context:** Organizations confuse internal escalation targets with statutory regulatory reporting windows.
- **Verification:**
  1. **Internal Escalation:** `Internal_Security_Incident_Policy_v4.pdf` (§3.2) explicitly mandates notification to CISO and Legal Counsel within **thirty (30) minutes**.
  2. **Customer Notice:** `Customer_Enterprise_SLA_2026.pdf` (§2.4) mandates customer advisory within **forty-five (45) minutes**.
  3. **Statutory External Directive:** `Customer_Enterprise_SLA_2026.pdf` (§2.4) cites the Indian **CERT-In Directions (2022)** mandating external notification to `incident@cert-in.org.in` within **six (6.0) hours**.
- **Result:** AuditLens AI cleanly segregates all three notification clocks in its verified findings.

---

### 3.3 Negative Constraint / Safe Refusal (Test T8)
- **Query:** *"What is the policy for commercial drone surveillance over data centers?"*
- **System Behavior:**
  - Evaluates similarity: dense vector score falls to ~0.58, and lexical match is 0.0.
  - Multi-tier subject defense detects `drone` as an ungrounded topic.
  - System suppresses speculative generation and returns a formal audit refusal:
    > *"Refusal / Out-of-Scope: The query cannot be answered based on indexed contracts. In accordance with strict audit guardrails, speculative answers are suppressed."*
- **Verdict:** 100% adherence to Track 2's negative path constraint.

---

## 4. Grounding & Substring Verification Test

To verify our code-level citation verifier, 50 LLM-generated citations were tested against raw text chunks retrieved from MongoDB Atlas:
- **Total Citations Evaluated:** 50
- **Verbatim Matches Confirmed:** 50 (100%)
- **Hallucinated / Fabricated Quotes:** 0 (0%)

Every citation displayed on the frontend carries the verified badge:
`🛡️ Verbatim Verified from Atlas Source`.

---

## 5. Performance & Telemetry Benchmarks

| Component | Average Execution Time |
|---|---|
| **Sentence-Transformers Embedding Generation (Local CPU)** | ~45 ms |
| **MongoDB Atlas `$vectorSearch` Execution** | ~82 ms |
| **Hybrid Lexical Token Match & Rescoring** | ~3 ms |
| **Google Gemini 1.5 Flash Structured Synthesis** | ~1,020 ms |
| **Programmatic Quote Verification & Health Score Calculation** | ~4 ms |
| **Total End-to-End Latency** | **~1,154 ms (~1.15 seconds)** |

The live system delivers instantaneous, production-grade responses while maintaining complete grounding integrity.
