import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AuditLens AI - Team Elite | UNCHARTED 2026</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
    
    @page {
      size: 16in 9in;
      margin: 0;
    }
    
    body {
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #f1f5f9;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    
    .slide {
      width: 16in;
      height: 9in;
      page-break-after: always;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
    }
    
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    .bg-mongo-navy { background-color: #001E2B; }
    .bg-mongo-forest { background-color: #00684A; }
    .bg-mongo-spring { background-color: #00ED64; }
    .text-mongo-spring { color: #00ED64; }
    .text-mongo-forest { color: #00684A; }
    .border-mongo-spring { border-color: #00ED64; }
    .bg-mongo-mint { background-color: #E6FEF3; }
  </style>
</head>
<body>

  <!-- ========================================== -->
  <!-- SLIDE 1: TITLE & PROJECT INTRODUCTION -->
  <!-- ========================================== -->
  <div class="slide bg-mongo-navy text-white p-16 justify-between">
    <div class="w-full h-2 bg-mongo-spring absolute top-0 left-0"></div>
    
    <div>
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-mongo-spring text-mongo-spring text-sm font-bold tracking-wider uppercase font-mono">
        UNCHARTED 2026 • TRACK 2: RAG ENGINE • TEAM ELITE
      </div>
      
      <div class="mt-8 flex items-baseline gap-4">
        <h1 class="text-7xl font-extrabold tracking-tight text-white">AuditLens<span class="text-mongo-spring">.AI</span></h1>
      </div>
      <p class="mt-4 text-3xl font-medium text-slate-300 max-w-4xl leading-snug">
        Real-Time Cross-Contract Due Diligence & Discrepancy Engine Grounded with MongoDB Atlas Native Vector Search
      </p>
    </div>

    <div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-8 backdrop-blur-md">
      <div class="text-xs font-mono text-mongo-spring uppercase tracking-widest font-bold mb-4">TEAM ELITE (SVNIT SURAT)</div>
      <div class="grid grid-cols-3 gap-6 text-sm">
        <div class="border-l-2 border-mongo-spring pl-4">
          <div class="font-bold text-base text-white">Rishit Modh</div>
          <div class="text-slate-400 text-xs mt-1">RAG Engine Architecture, Atlas $vectorSearch, Hybrid Fusion Pipeline</div>
        </div>
        <div class="border-l-2 border-emerald-500 pl-4">
          <div class="font-bold text-base text-white">Bhavya Juneja</div>
          <div class="text-slate-400 text-xs mt-1">Interactive Frontend, Telemetry Inspector, Evaluation Benchmark Modal</div>
        </div>
        <div class="border-l-2 border-teal-500 pl-4">
          <div class="font-bold text-base text-white">Sugandh Jha</div>
          <div class="text-slate-400 text-xs mt-1">Indian Legal Compliance Formulations, CERT-In Rules, Conflict Matrix</div>
        </div>
      </div>
      <div class="mt-6 pt-4 border-t border-slate-800 flex justify-between items-center text-xs font-mono text-slate-400">
        <div>Live Deployment: <span class="text-mongo-spring">https://auditlens-ai-13xs.onrender.com</span></div>
        <div>GitHub Repository: <span class="text-slate-300">rishitmodh12/AuditLens.AI</span></div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 2: PROBLEM STATEMENT & IMPORTANCE -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        Track 2 Problem Context
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">The Enterprise Contract Conflict Crisis</h2>
      <p class="text-base text-slate-500 mt-1">Why multi-source grounded due diligence is mission-critical for modern organizations</p>
    </div>

    <div class="grid grid-cols-2 gap-8 my-auto">
      <div class="bg-white rounded-2xl p-6 border border-slate-200 border-l-4 border-l-red-500 shadow-sm">
        <div class="text-xs font-mono text-red-600 font-bold uppercase">01 / Structural Contradiction</div>
        <h3 class="text-xl font-bold text-slate-900 mt-1">Multi-Document Disconnect</h3>
        <p class="text-sm text-slate-600 mt-2 leading-relaxed">
          Customer SLAs promise 99.9% uptime (max 1.0 hr downtime/month), while upstream Cloud Vendor MSAs allow 4.0 hr maintenance windows with zero penalty. Enterprises silently absorb catastrophic liabilities.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 border-l-4 border-l-amber-500 shadow-sm">
        <div class="text-xs font-mono text-amber-600 font-bold uppercase">02 / Regulatory Penalties</div>
        <h3 class="text-xl font-bold text-slate-900 mt-1">Statutory Indian Mandates (CERT-In)</h3>
        <p class="text-sm text-slate-600 mt-2 leading-relaxed">
          CERT-In Cyber Security Directions (2022) mandate external breach reporting within 6 hours. Companies face criminal penalties under IT Act §70B if internal (30-min CISO) and statutory notification clocks fall out of sync.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 border-l-4 border-l-emerald-600 shadow-sm">
        <div class="text-xs font-mono text-emerald-600 font-bold uppercase">03 / Financial Exposure</div>
        <h3 class="text-xl font-bold text-slate-900 mt-1">Service Credit Calculation Leakage</h3>
        <p class="text-sm text-slate-600 mt-2 leading-relaxed">
          Outage formulas are non-linear. A 2.0-hour banking gateway outage incurs ₹75,000 under Section 4.2. Without automated cross-document reconciliation, enterprises fail to claim vendor indemnities.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 border-l-4 border-l-blue-600 shadow-sm">
        <div class="text-xs font-mono text-blue-600 font-bold uppercase">04 / Hallucination Liability</div>
        <h3 class="text-xl font-bold text-slate-900 mt-1">LLM Fabrication in Legal Workflows</h3>
        <p class="text-sm text-slate-600 mt-2 leading-relaxed">
          Standard LLM chatbots hallucinate nonexistent clauses and miss numbers. In high-stakes legal audits, answers must carry 100% verbatim quotes verified directly against database records.
        </p>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 2 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 3: OUR PROPOSED SOLUTION -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        Product Overview
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">AuditLens AI: Automated Due Diligence Engine</h2>
      <p class="text-base text-slate-500 mt-1">Combining semantic vector search with programmatic legal verification</p>
    </div>

    <div class="grid grid-cols-12 gap-8 my-auto items-center">
      <div class="col-span-7 space-y-4">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div class="font-bold text-slate-900 text-lg flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-mongo-forest"></span>
            1. Multi-Source Conflict Detection
          </div>
          <p class="text-sm text-slate-600 mt-1.5 leading-relaxed">
            Simultaneously retrieves evidence from Customer SLAs, Cloud Vendor MSAs, and Security Incident Policies to spot conflicting downtime allowances, liability caps, and notice clocks.
          </p>
        </div>

        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div class="font-bold text-slate-900 text-lg flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span>
            2. Programmatic Verbatim Quote Verification
          </div>
          <p class="text-sm text-slate-600 mt-1.5 leading-relaxed">
            Eliminates LLM hallucination: citation quotes are checked at the code level against raw text stored in MongoDB Atlas. Verified citations earn a tamper-proof <span class="font-mono text-xs text-mongo-forest font-bold">🛡️ Verbatim Verified</span> badge.
          </p>
        </div>

        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
          <div class="font-bold text-slate-900 text-lg flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
            3. Strict Refusal on Out-of-Scope Queries
          </div>
          <p class="text-sm text-slate-600 mt-1.5 leading-relaxed">
            Fulfills Track 2's negative constraint requirement: queries outside the contract domain (e.g. drone surveillance) are strictly refused with clear audit guardrails.
          </p>
        </div>
      </div>

      <div class="col-span-5 bg-white p-5 rounded-2xl border border-slate-200 shadow-md">
        <img src="../assets/screenshots/01_dashboard.png" class="rounded-xl border border-slate-200 w-full object-cover shadow-sm">
        <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500 font-mono">
          <div class="font-bold text-slate-900 mb-1">Target Personas & Impact:</div>
          <div>• Legal Counsel: Audit conflicting warranties in seconds</div>
          <div>• FinOps & SREs: Reconcile outage penalties instantly</div>
          <div>• CISO & Compliance: Enforce CERT-In & DPDP Act readiness</div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 3 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 4: HOW OUR PLATFORM WORKS -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        System Workflow
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">End-to-End Audit & Verification Pipeline</h2>
      <p class="text-base text-slate-500 mt-1">Five stages from raw contract ingestion to verified compliance brief</p>
    </div>

    <div class="grid grid-cols-5 gap-4 my-auto">
      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-mongo-navy text-mongo-spring font-mono font-bold flex items-center justify-center text-sm mb-4">01</div>
          <h4 class="font-bold text-slate-900 text-base">Ingest & Overlap</h4>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">
            Uploads PDF/DOCX agreements. Text is cleaned and segmented into structural paragraphs with 15% sliding overlap to maintain clause continuity.
          </p>
        </div>
        <div class="text-[11px] font-mono text-mongo-forest mt-4 font-semibold">PyPDF + Smart Chunking</div>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-mongo-navy text-mongo-spring font-mono font-bold flex items-center justify-center text-sm mb-4">02</div>
          <h4 class="font-bold text-slate-900 text-base">Dense Vector Index</h4>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">
            Embeds chunks into 768-dimensional dense vectors using local Transformer model. Stores vectors + metadata in MongoDB Atlas.
          </p>
        </div>
        <div class="text-[11px] font-mono text-mongo-forest mt-4 font-semibold">all-mpnet-base-v2</div>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-mongo-navy text-mongo-spring font-mono font-bold flex items-center justify-center text-sm mb-4">03</div>
          <h4 class="font-bold text-slate-900 text-base">Hybrid Retrieval</h4>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">
            Combines Atlas $vectorSearch (70% semantic) with exact lexical token matching (30%) for clause numbers (§4.2, §3.2) and INR amounts.
          </p>
        </div>
        <div class="text-[11px] font-mono text-mongo-forest mt-4 font-semibold">Atlas $vectorSearch + BM25</div>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-mongo-navy text-mongo-spring font-mono font-bold flex items-center justify-center text-sm mb-4">04</div>
          <h4 class="font-bold text-slate-900 text-base">Dual-Track Reasoning</h4>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">
            Gemini 1.5 Flash cross-examines evidence across documents, identifies SLA discrepancies, calculates penalties, and formats JSON citations.
          </p>
        </div>
        <div class="text-[11px] font-mono text-mongo-forest mt-4 font-semibold">Gemini 1.5 Flash</div>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-mongo-navy text-mongo-spring font-mono font-bold flex items-center justify-center text-sm mb-4">05</div>
          <h4 class="font-bold text-slate-900 text-base">Verbatim Verify</h4>
          <p class="text-xs text-slate-600 mt-2 leading-relaxed">
            Backend string-matches citations against raw Atlas text, computes deterministic Compliance Health Score, and formats IST reports.
          </p>
        </div>
        <div class="text-[11px] font-mono text-mongo-forest mt-4 font-semibold">Algorithmic Verification</div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 4 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 5: TECHNICAL ARCHITECTURE & STACK -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        Technical Architecture
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">Cloud-Native Technology Stack</h2>
      <p class="text-base text-slate-500 mt-1">Built natively around MongoDB Atlas Vector Search</p>
    </div>

    <div class="grid grid-cols-2 gap-8 my-auto">
      <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-xl bg-mongo-mint text-mongo-forest flex items-center justify-center text-2xl font-bold font-mono">🍃</div>
          <div>
            <h3 class="font-bold text-slate-900 text-lg">Database & Vector Search</h3>
            <div class="text-xs font-mono text-mongo-forest font-semibold">MongoDB Atlas M0 (AWS Region)</div>
          </div>
        </div>
        <ul class="text-xs text-slate-600 mt-4 space-y-2 leading-relaxed">
          <li>• <strong class="text-slate-800">Native $vectorSearch Pipeline:</strong> 768 dimensions, cosine similarity.</li>
          <li>• <strong class="text-slate-800">Metadata Pre-Filtering:</strong> Query scoped by <code class="bg-slate-100 px-1 py-0.5 rounded">doc_id</code> and <code class="bg-slate-100 px-1 py-0.5 rounded">category</code>.</li>
          <li>• <strong class="text-slate-800">Single Source of Truth:</strong> Source files, chunks, embeddings, and audit history stored together.</li>
        </ul>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center text-2xl font-bold font-mono">⚡</div>
          <div>
            <h3 class="font-bold text-slate-900 text-lg">Backend & RAG Engine</h3>
            <div class="text-xs font-mono text-blue-700 font-semibold">FastAPI (Python 3.14) & Uvicorn</div>
          </div>
        </div>
        <ul class="text-xs text-slate-600 mt-4 space-y-2 leading-relaxed">
          <li>• <strong class="text-slate-800">Hybrid Search Fusion:</strong> 70% Dense Atlas Vector + 30% Lexical Token Match.</li>
          <li>• <strong class="text-slate-800">Deterministic Compliance Metric:</strong> Formula derived from detected conflict count.</li>
          <li>• <strong class="text-slate-800">Live Benchmark API:</strong> <code class="bg-slate-100 px-1 py-0.5 rounded">GET /api/evaluate</code> running 8 standardized queries.</li>
        </ul>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center text-2xl font-bold font-mono">🧠</div>
          <div>
            <h3 class="font-bold text-slate-900 text-lg">AI & Embedding Models</h3>
            <div class="text-xs font-mono text-amber-700 font-semibold">HuggingFace + Google Gemini 1.5</div>
          </div>
        </div>
        <ul class="text-xs text-slate-600 mt-4 space-y-2 leading-relaxed">
          <li>• <strong class="text-slate-800">all-mpnet-base-v2:</strong> 768-dim high-performance local embeddings with 0ms external API cost.</li>
          <li>• <strong class="text-slate-800">Gemini 1.5 Flash:</strong> Enforced strict JSON schema output for cross-document synthesis.</li>
          <li>• <strong class="text-slate-800">Refusal Trigger:</strong> Out-of-scope domain interceptor preventing hallucinations.</li>
        </ul>
      </div>

      <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm flex flex-col justify-between">
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center text-2xl font-bold font-mono">🌐</div>
          <div>
            <h3 class="font-bold text-slate-900 text-lg">Frontend & Production Hosting</h3>
            <div class="text-xs font-mono text-purple-700 font-semibold">Tailwind CSS + Render Docker Cloud</div>
          </div>
        </div>
        <ul class="text-xs text-slate-600 mt-4 space-y-2 leading-relaxed">
          <li>• <strong class="text-slate-800">Responsive UI:</strong> MongoDB Forest Green theme, telemetry inspector, live recall modal.</li>
          <li>• <strong class="text-slate-800">Interactive Walkthrough:</strong> Guided tutorial with non-blocking spotlight.</li>
          <li>• <strong class="text-slate-800">Render Container:</strong> Continuous deployment from GitHub with zero downtime.</li>
        </ul>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 5 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 6: KEY FEATURES & INNOVATION -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        Key Features & Innovation
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">What Differentiates Team Elite's AuditLens AI</h2>
      <p class="text-base text-slate-500 mt-1">Technical depth addressing every Judge Audit criterion</p>
    </div>

    <div class="grid grid-cols-3 gap-6 my-auto">
      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">01 / RETRIEVAL DEPTH</div>
        <h4 class="font-bold text-slate-900 text-base">Native Hybrid Search (70/30)</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Fuses dense Atlas vector similarity with exact token matching. Catches precise clause numbers (§4.2, §3.2) and ₹ INR amounts that pure semantic search overlooks.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">02 / ARITHMETIC RECONCILIATION</div>
        <h4 class="font-bold text-slate-900 text-base">Reconciled Outage Math</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Accurately applies SLA grace periods: (2.0 hrs - 1.0 hr grace) * ₹75,000 = ₹75,000 penalty. Fully harmonized across headline summaries, findings, and citation cards.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">03 / REGULATORY CLOCK</div>
        <h4 class="font-bold text-slate-900 text-base">CERT-In vs Internal Escalation</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Differentiates mandatory external 6.0-hour statutory CERT-In reporting (Cyber Security Directions 2022) from internal 30-minute CISO escalations and 45-minute customer notices.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">04 / ZERO HALLUCINATION</div>
        <h4 class="font-bold text-slate-900 text-base">Verbatim Quote Verification</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Code-level substring validation checks every LLM citation against raw Atlas chunks. Verified quotes receive the <code class="text-mongo-forest text-[10px] font-bold">🛡️ Verbatim Verified</code> badge.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">05 / OBJECTIVE METRICS</div>
        <h4 class="font-bold text-slate-900 text-base">Deterministic Compliance Score</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Derived via transparent mathematical formula: <br>
          <code class="text-xs text-slate-800 bg-slate-100 px-1 py-0.5 rounded font-mono">100 - (20×High) - (10×Med) - (10×Unverified)</code>. Zero arbitrary hallucinated scores.
        </p>
      </div>

      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm">
        <div class="text-mongo-forest font-mono text-xs font-bold uppercase mb-1">06 / EMPIRICAL RIGOR</div>
        <h4 class="font-bold text-slate-900 text-base">Automated Evaluation Suite</h4>
        <p class="text-xs text-slate-600 mt-2 leading-relaxed">
          Live <code class="text-xs text-slate-800 bg-slate-100 px-1 py-0.5 rounded font-mono">/api/evaluate</code> endpoint executing 8 standardized test queries directly in the UI, confirming 100% Recall and safe refusal.
        </p>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 6 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 7: RESULTS, VALIDATION & APPLICATIONS -->
  <!-- ========================================== -->
  <div class="slide bg-slate-50 text-slate-900 p-16 justify-between">
    <div>
      <div class="inline-block px-3 py-1 rounded-full bg-mongo-mint border border-emerald-300 text-mongo-forest text-xs font-bold font-mono uppercase">
        Empirical Validation
      </div>
      <h2 class="text-4xl font-extrabold text-slate-900 mt-3">Empirical Results & Indian Enterprise Applications</h2>
      <p class="text-base text-slate-500 mt-1">Live benchmark performance tested directly on the production cluster</p>
    </div>

    <div class="grid grid-cols-12 gap-8 my-auto items-center">
      <div class="col-span-5 space-y-3">
        <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
          <div class="w-16 h-16 rounded-xl bg-mongo-mint text-mongo-forest font-mono font-bold text-2xl flex items-center justify-center shrink-0">100%</div>
          <div>
            <div class="font-bold text-slate-900 text-sm">Recall@1 (Top Rank Precision)</div>
            <div class="text-xs text-slate-500">7 out of 7 positive test queries retrieved the exact target clause as the #1 result.</div>
          </div>
        </div>

        <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
          <div class="w-16 h-16 rounded-xl bg-mongo-mint text-mongo-forest font-mono font-bold text-2xl flex items-center justify-center shrink-0">100%</div>
          <div>
            <div class="font-bold text-slate-900 text-sm">Recall@3 (Top-3 Retrieval)</div>
            <div class="text-xs text-slate-500">All relevant legal evidence retrieved within top 3 Atlas vector search results.</div>
          </div>
        </div>

        <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
          <div class="w-16 h-16 rounded-xl bg-mongo-mint text-mongo-forest font-mono font-bold text-2xl flex items-center justify-center shrink-0">100%</div>
          <div>
            <div class="font-bold text-slate-900 text-sm">Out-of-Scope Refusal Accuracy</div>
            <div class="text-xs text-slate-500">Unanswerable drone surveillance query safely refused with zero hallucination.</div>
          </div>
        </div>

        <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-4">
          <div class="w-16 h-16 rounded-xl bg-mongo-mint text-mongo-forest font-mono font-bold text-2xl flex items-center justify-center shrink-0">100%</div>
          <div>
            <div class="font-bold text-slate-900 text-sm">Verbatim Quote Verification</div>
            <div class="text-xs text-slate-500">All citation snippets verified verbatim against raw MongoDB Atlas text.</div>
          </div>
        </div>
      </div>

      <div class="col-span-7 bg-white p-4 rounded-2xl border border-slate-200 shadow-md">
        <img src="../assets/screenshots/04_benchmark_modal_loaded.png" class="rounded-xl border border-slate-200 w-full object-cover">
        <div class="mt-3 text-xs font-mono text-slate-500 text-center">
          Live Endpoint: <code class="text-mongo-forest font-bold">GET /api/evaluate</code> | 8 Test Queries Evaluated in ~1.2s natively in Atlas
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 7 of 8</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 8: FUTURE SCOPE & CONCLUSION -->
  <!-- ========================================== -->
  <div class="slide bg-mongo-navy text-white p-16 justify-between">
    <div class="w-full h-2 bg-mongo-spring absolute top-0 left-0"></div>

    <div>
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-mongo-spring text-mongo-spring text-sm font-bold tracking-wider uppercase font-mono">
        ROADMAP & IMPACT
      </div>
      <h2 class="text-4xl font-extrabold text-white mt-4">Future Scope & Conclusion</h2>
      <p class="text-base text-slate-300 mt-1">Expanding AuditLens AI into enterprise legal operations</p>
    </div>

    <div class="grid grid-cols-3 gap-6 my-auto">
      <div class="bg-slate-900/80 border border-slate-700 rounded-2xl p-6">
        <div class="text-mongo-spring font-mono text-xs font-bold uppercase mb-2">INTEGRATION</div>
        <h3 class="text-lg font-bold text-white">n8n Workflow Automation</h3>
        <p class="text-xs text-slate-400 mt-2 leading-relaxed">
          Automated webhooks triggering incident management workflows in n8n, opening Jira tickets and alerting Slack channels when High-Severity contract discrepancies are flagged.
        </p>
      </div>

      <div class="bg-slate-900/80 border border-slate-700 rounded-2xl p-6">
        <div class="text-mongo-spring font-mono text-xs font-bold uppercase mb-2">NEGOTIATION</div>
        <h3 class="text-lg font-bold text-white">Multi-Party Clause Redlining</h3>
        <p class="text-xs text-slate-400 mt-2 leading-relaxed">
          Generative contract renegotiation assistant suggesting harmonized legal language to bridge customer SLAs and vendor agreements prior to contract signing.
        </p>
      </div>

      <div class="bg-slate-900/80 border border-slate-700 rounded-2xl p-6">
        <div class="text-mongo-spring font-mono text-xs font-bold uppercase mb-2">SCALABILITY</div>
        <h3 class="text-lg font-bold text-white">Atlas M10+ Dedicated Scaling</h3>
        <p class="text-xs text-slate-400 mt-2 leading-relaxed">
          Transitioning from M0 to dedicated Atlas clusters with multi-tenant sharding and real-time document sync via Atlas App Services.
        </p>
      </div>
    </div>

    <div class="bg-slate-900/90 border border-mongo-spring/50 rounded-2xl p-6 backdrop-blur-md">
      <div class="flex items-center justify-between">
        <div>
          <div class="text-mongo-spring font-mono text-xs font-bold uppercase">UNCHARTED 2026 • TEAM ELITE</div>
          <p class="text-sm text-slate-200 mt-1 max-w-3xl leading-relaxed">
            AuditLens AI transforms passive contract repositories into active, grounded, and mathematically reconciled compliance intelligence. Built natively with MongoDB Atlas Vector Search, tested with empirical benchmarks, and 100% deployed in production.
          </p>
        </div>
        <div class="text-right text-xs font-mono text-slate-400">
          <div class="text-white font-bold">Rishit Modh • Bhavya Juneja • Sugandh Jha</div>
          <div class="text-mongo-spring mt-1">https://auditlens-ai-13xs.onrender.com</div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-800 pt-3 text-xs font-mono text-slate-400 flex justify-between">
      <span>UNCHARTED 2026 | Team Elite</span>
      <span>Slide 8 of 8</span>
    </div>
  </div>

</body>
</html>
"""

with open("presentation/slide_deck.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved presentation/slide_deck.html")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_out = os.path.abspath(r"presentation/AuditLens_AI_Team_Elite_Deck.pdf")
html_in = os.path.abspath(r"presentation/slide_deck.html")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={pdf_out}",
    html_in
]

print("Rendering PDF via headless Edge...")
subprocess.run(cmd, check=True)
print(f"Successfully generated PDF deck at: {pdf_out}")
