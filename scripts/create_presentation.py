import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    C_NAVY = RGBColor(0, 30, 43)        # #001E2B
    C_FOREST = RGBColor(0, 104, 74)     # #00684A
    C_SPRING = RGBColor(0, 237, 100)    # #00ED64
    C_BG_LIGHT = RGBColor(248, 250, 252)# #F8FAFC
    C_CARD_BG = RGBColor(255, 255, 255) # White
    C_BORDER = RGBColor(226, 232, 240)  # #E2E8F0
    C_TEXT_DARK = RGBColor(15, 23, 42)  # Slate 900
    C_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    C_WHITE = RGBColor(255, 255, 255)
    C_RED = RGBColor(220, 38, 38)
    C_MINT = RGBColor(230, 254, 243)

    def add_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, tag, title, subtitle):
        # Header Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(4.5), Inches(0.35))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_MINT
        badge.line.color.rgb = C_SPRING
        badge.line.width = Pt(1)
        tf = badge.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_FOREST
        p.alignment = PP_ALIGN.LEFT

        # Slide Title
        tbox = slide.shapes.add_textbox(Inches(0.8), Inches(0.9), Inches(11.7), Inches(0.7))
        tf_t = tbox.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        # Subtitle
        sbox = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.4))
        tf_s = sbox.text_frame
        tf_s.word_wrap = True
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = C_TEXT_MUTED

    def add_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: TITLE & PROJECT INTRODUCTION
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, C_NAVY)

    # Decorative top bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_SPRING
    bar.line.fill.background()

    # Track Tag Badge
    badge1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.2), Inches(5.8), Inches(0.4))
    badge1.fill.solid()
    badge1.fill.fore_color.rgb = RGBColor(2, 52, 48)
    badge1.line.color.rgb = C_SPRING
    tf1_b = badge1.text_frame
    p1_b = tf1_b.paragraphs[0]
    p1_b.text = "UNCHARTED 2026  •  TRACK 2: RAG ENGINE  •  TEAM ELITE"
    p1_b.font.size = Pt(11)
    p1_b.font.bold = True
    p1_b.font.color.rgb = C_SPRING

    # Project Title
    t1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(1.2))
    tf1_t = t1.text_frame
    p1_t = tf1_t.paragraphs[0]
    p1_t.text = "AuditLens AI"
    p1_t.font.size = Pt(44)
    p1_t.font.bold = True
    p1_t.font.color.rgb = C_WHITE

    # Tagline
    tag1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.9), Inches(11.3), Inches(0.8))
    tf1_tag = tag1.text_frame
    p1_tag = tf1_tag.paragraphs[0]
    p1_tag.text = "Real-Time Cross-Contract Due Diligence & Discrepancy Engine\nGrounded with MongoDB Atlas Native Vector Search ($vectorSearch)"
    p1_tag.font.size = Pt(18)
    p1_tag.font.color.rgb = RGBColor(203, 213, 225)

    # Team Card
    tcard = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.2), Inches(11.3), Inches(1.8))
    tcard.fill.solid()
    tcard.fill.fore_color.rgb = RGBColor(15, 41, 56)
    tcard.line.color.rgb = RGBColor(30, 64, 85)
    tf1_tc = tcard.text_frame
    tf1_tc.word_wrap = True

    p_h = tf1_tc.paragraphs[0]
    p_h.text = "TEAM ELITE (SVNIT SURAT)"
    p_h.font.size = Pt(12)
    p_h.font.bold = True
    p_h.font.color.rgb = C_SPRING

    p_m = tf1_tc.add_paragraph()
    p_m.text = "• Rishit Modh (RAG Engine Architecture, MongoDB Atlas Vector Search, Hybrid Fusion)\n• Bhavya Juneja (Frontend Application, Telemetry Inspector, Evaluation Benchmark UI)\n• Sugandh Jha (Compliance Rule Formulation, Indian Regulatory Datasets, Conflict Matrix)"
    p_m.font.size = Pt(12)
    p_m.font.color.rgb = C_WHITE

    p_l = tf1_tc.add_paragraph()
    p_l.text = "Live Deployment: https://auditlens-ai-13xs.onrender.com  |  GitHub: https://github.com/rishitmodh12/AuditLens.AI"
    p_l.font.size = Pt(10)
    p_l.font.color.rgb = RGBColor(148, 163, 184)

    add_speaker_notes(s1, "Welcome judges and organizers! We are Team Elite from SVNIT Surat, presenting AuditLens AI for Track 2. In enterprise operations, organizations sign hundreds of contracts with customers, cloud vendors, and regulators that silently contradict one another. AuditLens AI eliminates this exposure by turning complex contracts into grounded, mathematically verified compliance intelligence using native MongoDB Atlas Vector Search.")

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT & ITS IMPORTANCE
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2, C_BG_LIGHT)
    add_header(s2, "Track 2 Problem Context", "The Enterprise Contract Conflict Crisis", "Why multi-source grounded due diligence is vital for modern Indian organizations")

    # 4 Problem Cards Layout
    cards_data = [
        ("Multi-Document Disconnect", "Customer SLAs promise 99.9% uptime (max 1 hr downtime/month), while upstream Cloud Vendor MSAs allow 4-hour maintenance windows with zero penalty. Enterprises silently absorb catastrophic liabilities.", RGBColor(239, 68, 68)),
        ("Statutory Indian Mandates", "CERT-In Cyber Security Directions (2022) mandate external reporting within 6 hours. Companies face penal action under IT Act §70B if internal and statutory notification clocks fall out of sync.", RGBColor(245, 158, 11)),
        ("Financial Penalty Leakage", "Service credit formulas are complex. A 2.0-hour banking gateway outage incurs ₹75,000 under Section 4.2. Without automated cross-document reconciliation, enterprises fail to recover vendor dues.", RGBColor(16, 185, 129)),
        ("LLM Hallucination Risk", "Standard RAG models hallucinate clauses, invent penalties, and conflate internal 30-min CISO escalation with external 6-hour CERT-In rules. Enterprise compliance demands 100% verifiable quotes.", RGBColor(59, 130, 246))
    ]

    for idx, (title, desc, accent) in enumerate(cards_data):
        x = Inches(0.8 + (idx % 2) * 5.9)
        y = Inches(2.2 + (idx // 2) * 2.3)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.0))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        # Accent bar
        abar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(0.1), Inches(2.0))
        abar.fill.solid()
        abar.fill.fore_color.rgb = accent
        abar.line.fill.background()

        tf = card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = f"  {title}"
        p0.font.size = Pt(14)
        p0.font.bold = True
        p0.font.color.rgb = C_TEXT_DARK

        p1 = tf.add_paragraph()
        p1.text = f"  {desc}"
        p1.font.size = Pt(11)
        p1.font.color.rgb = C_TEXT_MUTED

    add_speaker_notes(s2, "Track 2 challenges us to turn source material into grounded, useful results while cross-referencing multiple sources and handling negative queries. In modern IT and fintech companies, contracts don't exist in silos. If your AWS vendor takes a 3-hour downtime window, but your Customer SLA penalizes you after 1 hour at ₹75,000/hr, you lose money. Furthermore, under Indian CERT-In guidelines, failing to report within 6 hours invites statutory fines. Traditional search can't catch these contradictions, and standard LLMs hallucinate.")

    # =========================================================================
    # SLIDE 3: OUR PROPOSED SOLUTION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3, C_BG_LIGHT)
    add_header(s3, "Product Overview", "AuditLens AI: Automated Cross-Document Due Diligence", "A production-grade RAG engine combining semantic vector retrieval with strict legal grounding")

    # Left: 3 Pillars
    pillars = [
        ("1. Multi-Source Conflict Detection", "Simultaneously indexes Customer SLAs, Vendor MSAs, and Security Incident Policies. Cross-examines clauses to detect mismatched liability caps, conflicting notification clocks, and downtime loopholes."),
        ("2. Verbatim Quote Verification (Zero Hallucination)", "Every citation returned by Gemini Flash is checked at code level against the source chunk stored in MongoDB Atlas. Only 100% verbatim matches receive the '🛡️ Verbatim Verified' badge."),
        ("3. Strict Refusal on Out-of-Scope Queries", "Negative queries (such as drone surveillance over data centers) trigger our multi-layered ungrounded subject defense and similarity thresholding, returning a clear refusal rather than speculative text.")
    ]

    for idx, (title, desc) in enumerate(pillars):
        y = Inches(2.2 + idx * 1.55)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(6.8), Inches(1.4))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tf = card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = C_FOREST

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = C_TEXT_MUTED

    # Right: Screenshot Card
    rcard = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(2.2), Inches(4.6), Inches(4.6))
    rcard.fill.solid()
    rcard.fill.fore_color.rgb = C_CARD_BG
    rcard.line.color.rgb = C_BORDER
    
    # Try inserting screenshot if available
    img_path = r"c:\Users\DELL\Desktop\UNcharted\assets\screenshots\01_dashboard.png"
    if os.path.exists(img_path):
        s3.shapes.add_picture(img_path, Inches(8.0), Inches(2.3), Inches(4.4), Inches(2.8))

    cap_box = s3.shapes.add_textbox(Inches(8.0), Inches(5.2), Inches(4.4), Inches(1.5))
    tf_cap = cap_box.text_frame
    tf_cap.word_wrap = True
    p_c0 = tf_cap.paragraphs[0]
    p_c0.text = "Target Personas & Impact:"
    p_c0.font.size = Pt(11)
    p_c0.font.bold = True
    p_c0.font.color.rgb = C_TEXT_DARK
    p_c1 = tf_cap.add_paragraph()
    p_c1.text = "• Legal Counsel: Audit conflicting warranties in seconds\n• FinOps & SREs: Reconcile outage penalties instantly\n• CISO & Compliance: Enforce CERT-In & DPDP Act readiness"
    p_c1.font.size = Pt(10)
    p_c1.font.color.rgb = C_TEXT_MUTED

    add_speaker_notes(s3, "AuditLens AI solves this through three robust engineering pillars: First, multi-source conflict detection across disparate legal agreements. Second, code-level verbatim quote verification where every citation is string-checked against the raw text in MongoDB Atlas to eliminate hallucinations. Third, strict refusal guardrails that identify out-of-scope requests. This turns hours of tedious contract review into seconds.")

    # =========================================================================
    # SLIDE 4: HOW OUR PLATFORM WORKS
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4, C_BG_LIGHT)
    add_header(s4, "System Workflow", "End-to-End Audit & Verification Pipeline", "How documents are transformed into verifiable, cross-referenced intelligence")

    steps = [
        ("Step 1", "Multi-Document Ingestion", "Uploads enterprise contracts (PDF/DOCX/TXT). Preprocesses text, strips headers, and splits using structural paragraph awareness with 15% sliding window overlap."),
        ("Step 2", "Atlas Vector Search Indexing", "Generates 768-dimensional dense vector embeddings via sentence-transformers/all-mpnet-base-v2. Stores embeddings + rich metadata in MongoDB Atlas."),
        ("Step 3", "Hybrid Fusion Retrieval", "Combines Atlas $vectorSearch (70% semantic weight) with exact keyword token matching (30% weight) for clause numbers (§4.2, §3.2) and INR amounts."),
        ("Step 4", "Dual-Track LLM Reasoning", "Google Gemini 1.5 Flash cross-examines evidence across documents, identifies SLA discrepancies, calculates penalties, and formats JSON citations."),
        ("Step 5", "Verbatim Verification & Report", "Backend verifies citations against Atlas source chunks, calculates Algorithmic Compliance Health Score, and generates exportable IST briefs.")
    ]

    for idx, (step_num, step_title, step_desc) in enumerate(steps):
        x = Inches(0.8 + idx * 2.38)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.2), Inches(2.25), Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        # Step badge
        sbadge = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Inches(0.15), Inches(2.4), Inches(1.95), Inches(0.35))
        sbadge.fill.solid()
        sbadge.fill.fore_color.rgb = C_NAVY
        sbadge.line.fill.background()
        tf_b = sbadge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = step_num
        p_b.font.size = Pt(11)
        p_b.font.bold = True
        p_b.font.color.rgb = C_SPRING
        p_b.alignment = PP_ALIGN.CENTER

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.7)
        p0 = tf.paragraphs[0]
        p0.text = step_title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = C_TEXT_DARK

        p1 = tf.add_paragraph()
        p1.text = step_desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = C_TEXT_MUTED

    add_speaker_notes(s4, "Here is the complete user workflow. When contracts are uploaded, our chunking algorithm creates overlapping chunks to preserve clause boundaries. Embeddings are generated locally with all-mpnet-base-v2 and stored in MongoDB Atlas. On query execution, we run our native Hybrid Search pipeline, fusing vector cosine similarity with exact keyword matching. Gemini 1.5 Flash reasons across the retrieved evidence, and our backend performs verbatim string verification before displaying the final results.")

    # =========================================================================
    # SLIDE 5: TECHNICAL ARCHITECTURE & STACK
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5, C_BG_LIGHT)
    add_header(s5, "Technical Architecture", "Cloud-Native RAG Implementation", "Modular, scalable architecture built natively around MongoDB Atlas Vector Search")

    # Stack Grid: 4 Cards
    stack_items = [
        ("Database & Vector Search", "MongoDB Atlas (M0 AWS Cluster)\n• Native $vectorSearch pipeline\n• 768-dim Cosine similarity index\n• Metadata filters (doc_id, category)\n• Dynamic conflict matrix collection", C_FOREST),
        ("Backend & RAG Engine", "FastAPI (Python 3.14) & Uvicorn\n• Native Hybrid Search fusion (70/30)\n• Recursive smart overlap chunking\n• Programmatic quote verifier\n• Automated Evaluation Benchmark harness", C_NAVY),
        ("AI & Embedding Models", "Local Transformers + Gemini 1.5\n• all-mpnet-base-v2 (768-dim, 0ms API cost)\n• Google Gemini 1.5 Flash (Strict JSON)\n• Grounded hallucination guardrails\n• Refusal trigger for out-of-scope topics", RGBColor(14, 116, 144)),
        ("Frontend & Deployment", "Modern Web UI + Cloud Hosting\n• Vanilla JS + Tailwind CSS (MongoDB Green)\n• Interactive Onboarding Tutorial\n• Docker Container on Render (100% Live)\n• IST (Asia/Kolkata) audit timestamps", RGBColor(67, 56, 202))
    ]

    for idx, (title, desc, header_color) in enumerate(stack_items):
        x = Inches(0.8 + (idx % 2) * 5.9)
        y = Inches(2.2 + (idx // 2) * 2.3)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.05))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        # Header bar
        top_bar = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(0.4))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = header_color
        top_bar.line.fill.background()
        tf_h = top_bar.text_frame
        p_h = tf_h.paragraphs[0]
        p_h.text = f" {title}"
        p_h.font.size = Pt(11)
        p_h.font.bold = True
        p_h.font.color.rgb = C_WHITE

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.5)
        p0 = tf.paragraphs[0]
        p0.text = desc
        p0.font.size = Pt(10.5)
        p0.font.color.rgb = C_TEXT_DARK

    add_speaker_notes(s5, "Our technical architecture is designed for enterprise robustness. MongoDB Atlas is the foundation: it stores the documents, chunks, and runs native $vectorSearch. For embeddings, we chose all-mpnet-base-v2 running locally, providing 768-dimensional accuracy without API latency or cost. Google Gemini 1.5 Flash provides fast, grounded reasoning with structured JSON schemas. The backend is built on FastAPI, and the entire app is containerized with Docker and deployed live on Render.")

    # =========================================================================
    # SLIDE 6: KEY FEATURES & INNOVATION
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6, C_BG_LIGHT)
    add_header(s6, "Key Features & Innovation", "What Differentiates Team Elite's AuditLens AI", "Technical depth and purpose-built engineering addressing the Judge Audit")

    features = [
        ("1. Native Hybrid Search (Dense + Lexical)", "Combines Atlas $vectorSearch (70%) with exact token matching (30%). Catches precise legal clause numbers (§4.2, §3.2) and INR amounts that standard semantic search frequently misses."),
        ("2. Reconciled Contract Arithmetic", "Accurately calculates outage liabilities based on contracted monthly allowances: (2.0 hrs - 1.0 hr grace) * ₹75,000 = ₹75,000 penalty, preventing SLA dispute losses."),
        ("3. Dual-Track CERT-In vs Internal Escalation", "Clearly distinguishes statutory external CERT-In notifications (6.0 hours under Cyber Security Directions 2022) from internal CISO escalations (30 minutes) and customer notice (45 minutes)."),
        ("4. Dynamic Cross-Contract Conflict Matrix", "A real-time scanner (/api/conflicts/scan) that parses indexed agreements and maps out direct contradictions between customer uptime commitments and vendor maintenance windows."),
        ("5. Algorithmic Compliance Health Score", "Replaced hardcoded metrics with a deterministic formula: Score = 100 - (20 * High Conflicts) - (10 * Med Conflicts) - (10 * Unverified Quotes), providing transparent, objective audit metrics."),
        ("6. 100% Verbatim Quote Verification Badge", "Programmatically string-matches LLM citation excerpts against raw Atlas chunks. Only verified text receives the '🛡️ Verbatim Verified from Atlas Source' badge.")
    ]

    for idx, (title, desc) in enumerate(features):
        x = Inches(0.8 + (idx % 2) * 5.9)
        y = Inches(2.2 + (idx // 2) * 1.55)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(1.4))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        tf = card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = C_FOREST

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = C_TEXT_MUTED

    add_speaker_notes(s6, "What separates AuditLens AI from generic RAG wrappers is technical depth. First, our 70/30 hybrid search solves the classic RAG limitation with exact numbers and clause references. Second, we reconciled the arithmetic for SLA downtime: a 2-hour outage minus 1-hour grace equals ₹75,000. Third, we explicitly differentiated internal 30-minute CISO escalation from the 6-hour CERT-In statutory clock. And finally, our compliance score is 100% deterministic, calculated from detected conflicts.")

    # =========================================================================
    # SLIDE 7: RESULTS, VALIDATION & REAL-WORLD APPLICATIONS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7, C_BG_LIGHT)
    add_header(s7, "Results & Empirical Validation", "Track 2 Benchmark: 100% Recall & Safe Refusal", "Verifiable performance metrics tested live on the production deployment")

    # Left: Benchmark Metrics Cards
    metrics = [
        ("100%", "Recall@1 (Top Rank)", "7 out of 7 positive test queries retrieved the exact target clause as the #1 result."),
        ("100%", "Recall@3 (Top 3 Hits)", "All relevant legal evidence retrieved within top 3 Atlas vector search results."),
        ("100%", "Out-of-Scope Refusal", "Unanswerable query (drone surveillance) safely refused with zero hallucination."),
        ("100%", "Grounding Precision", "All citations programmatically verified verbatim against MongoDB Atlas chunks.")
    ]

    for idx, (num, label, desc) in enumerate(metrics):
        y = Inches(2.2 + idx * 1.15)
        mcard = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(5.6), Inches(1.0))
        mcard.fill.solid()
        mcard.fill.fore_color.rgb = C_CARD_BG
        mcard.line.color.rgb = C_BORDER

        # Number Box
        nbox = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), y + Inches(0.1), Inches(1.2), Inches(0.8))
        nbox.fill.solid()
        nbox.fill.fore_color.rgb = C_MINT
        nbox.line.color.rgb = C_SPRING
        tf_n = nbox.text_frame
        p_n = tf_n.paragraphs[0]
        p_n.text = num
        p_n.font.size = Pt(16)
        p_n.font.bold = True
        p_n.font.color.rgb = C_FOREST
        p_n.alignment = PP_ALIGN.CENTER

        tf_m = mcard.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = Inches(1.4)
        p0 = tf_m.paragraphs[0]
        p0.text = label
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = C_TEXT_DARK

        p1 = tf_m.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = C_TEXT_MUTED

    # Right: Screenshot Card of Benchmark Modal
    img_bench = r"c:\Users\DELL\Desktop\UNcharted\assets\screenshots\04_benchmark_modal_loaded.png"
    if os.path.exists(img_bench):
        s7.shapes.add_picture(img_bench, Inches(6.8), Inches(2.2), Inches(5.7), Inches(3.6))
        cbox = s7.shapes.add_textbox(Inches(6.8), Inches(5.9), Inches(5.7), Inches(0.9))
        tf_cb = cbox.text_frame
        tf_cb.word_wrap = True
        p_c = tf_cb.paragraphs[0]
        p_c.text = "Live Evaluation Endpoint: GET /api/evaluate  |  Runs full 8-query suite in ~1.2s natively against MongoDB Atlas."
        p_c.font.size = Pt(9.5)
        p_c.font.color.rgb = C_TEXT_MUTED

    add_speaker_notes(s7, "Judges can verify our evaluation benchmark live by clicking the Recall Benchmark button or hitting the /api/evaluate endpoint. We test 8 comprehensive queries covering SLA outage math, CERT-In compliance, CISO escalations, Mumbai staging patch windows, and IT Act log retention. The results: 100% Recall at 1, 100% Recall at 3, and 100% Refusal Accuracy on our unanswerable drone query. This fulfills the Track 2 testing requirement completely.")

    # =========================================================================
    # SLIDE 8: FUTURE SCOPE & CONCLUSION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8, C_NAVY)

    # Decorative top bar
    bar8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
    bar8.fill.solid()
    bar8.fill.fore_color.rgb = C_SPRING
    bar8.line.fill.background()

    # Header
    t8 = s8.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(0.8))
    tf8 = t8.text_frame
    p8 = tf8.paragraphs[0]
    p8.text = "Future Roadmap & Project Conclusion"
    p8.font.size = Pt(28)
    p8.font.bold = True
    p8.font.color.rgb = C_WHITE

    # 3 Future Roadmap Cards
    roadmap = [
        ("n8n Workflow Automation", "Automated webhooks triggering incident management workflows in n8n, opening Jira tickets and alerting Slack channels when High-Severity contract discrepancies are flagged."),
        ("Multi-Party Clause Redlining", "Generative contract renegotiation assistant suggesting harmonized legal language to bridge customer SLAs and vendor agreements prior to contract signing."),
        ("Atlas M10+ Dedicated Scaling", "Transitioning from M0 to dedicated Atlas clusters with multi-tenant sharding and real-time document sync via Atlas App Services.")
    ]

    for idx, (title, desc) in enumerate(roadmap):
        x = Inches(0.8 + idx * 3.95)
        rcard = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.8), Inches(2.4))
        rcard.fill.solid()
        rcard.fill.fore_color.rgb = RGBColor(15, 41, 56)
        rcard.line.color.rgb = RGBColor(30, 64, 85)
        tf = rcard.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = C_SPRING

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10.5)
        p1.font.color.rgb = RGBColor(203, 213, 225)

    # Closing Card
    close_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.4))
    close_card.fill.solid()
    close_card.fill.fore_color.rgb = RGBColor(2, 52, 48)
    close_card.line.color.rgb = C_SPRING
    tf_cl = close_card.text_frame
    tf_cl.word_wrap = True

    p_cl0 = tf_cl.paragraphs[0]
    p_cl0.text = "UNCHARTED 2026  •  TEAM ELITE"
    p_cl0.font.size = Pt(16)
    p_cl0.font.bold = True
    p_cl0.font.color.rgb = C_SPRING

    p_cl1 = tf_cl.add_paragraph()
    p_cl1.text = "AuditLens AI transforms passive contract repositories into active, grounded, and mathematically reconciled compliance intelligence. Built natively with MongoDB Atlas Vector Search, tested with empirical benchmarks, and 100% deployed in production."
    p_cl1.font.size = Pt(12)
    p_cl1.font.color.rgb = C_WHITE

    p_cl2 = tf_cl.add_paragraph()
    p_cl2.text = "Team Members: Rishit Modh  |  Bhavya Juneja  |  Sugandh Jha\nLive Application: https://auditlens-ai-13xs.onrender.com  |  Repository: https://github.com/rishitmodh12/AuditLens.AI"
    p_cl2.font.size = Pt(11)
    p_cl2.font.color.rgb = RGBColor(148, 163, 184)

    add_speaker_notes(s8, "To conclude, Team Elite has delivered an end-to-end, grounded RAG solution that solves a real enterprise problem in the Indian regulatory ecosystem. We have addressed every piece of feedback: hybrid search, verbatim verification, arithmetic reconciliation, CERT-In compliance, and an empirical evaluation harness. Thank you, judges, mentors, and the NEXUS SVNIT team! We are now open for your questions.")

    output_pptx = r"c:\Users\DELL\Desktop\UNcharted\presentation\AuditLens_AI_Team_Elite_Deck.pptx"
    prs.save(output_pptx)
    print(f"Successfully generated 8-slide PPTX deck at: {output_pptx}")

if __name__ == "__main__":
    create_presentation()
