import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_official_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Official Template Colors
    C_NAVY = RGBColor(11, 30, 51)        # #0b1e33
    C_TEAL = RGBColor(0, 180, 180)       # #00b4b4
    C_ORANGE = RGBColor(230, 126, 34)    # #e67e22
    C_BG_LIGHT = RGBColor(248, 249, 250) # #f8f9fa
    C_CARD_BG = RGBColor(248, 250, 252)  # #f8fafc
    C_BORDER = RGBColor(226, 232, 240)   # #e2e8f0
    C_TEXT_DARK = RGBColor(15, 23, 42)   # #0f172a
    C_TEXT_MUTED = RGBColor(100, 116, 139) # #64748b
    C_WHITE = RGBColor(255, 255, 255)
    C_YELLOW_TAG = RGBColor(234, 179, 8) # #eab308

    def add_notes(slide, text):
        tf = slide.notes_slide.notes_text_frame
        tf.text = text

    def add_top_bar(slide, cat_num, cat_title, subtitle, page_num):
        # White background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_LIGHT
        bg.line.fill.background()

        # Navy header banner
        hbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = C_NAVY
        hbar.line.fill.background()

        # Teal dividing strip
        strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(13.333), Inches(0.06))
        strip.fill.solid()
        strip.fill.fore_color.rgb = C_TEAL
        strip.line.fill.background()

        # Category Tag (e.g. 01 PROBLEM)
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf_cat = t_box.text_frame
        p_c = tf_cat.paragraphs[0]
        p_c.text = cat_num.upper()
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = C_TEAL

        # Slide Main Title
        m_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.5), Inches(0.6))
        tf_m = m_box.text_frame
        p_m = tf_m.paragraphs[0]
        p_m.text = cat_title
        p_m.font.size = Pt(24)
        p_m.font.bold = True
        p_m.font.color.rgb = C_WHITE

        # Subtitle italic line under header
        s_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.35))
        tf_s = s_box.text_frame
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.size = Pt(11)
        p_s.font.italic = True
        p_s.font.color.rgb = C_TEXT_MUTED

        # Footer
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
        tf_f = f_box.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = f"Team Elite  |  UNCHARTED 2026{' '*140}{page_num}"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 1: TITLE & PROJECT INTRODUCTION
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.fill.background()

    # Vertical Teal Accent Bar
    vbar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(0.12), Inches(2.7))
    vbar.fill.solid()
    vbar.fill.fore_color.rgb = C_TEAL
    vbar.line.fill.background()

    # Content Box
    cbox1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(5.2))
    tf1 = cbox1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "UNCHARTED 2026"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = C_TEAL

    p1 = tf1.add_paragraph()
    p1.text = "AuditLens.AI"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Real-Time Cross-Contract Due Diligence & Discrepancy Engine Grounded with MongoDB Atlas Vector Search"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(203, 213, 225)
    p2.space_after = Pt(28)

    p3 = tf1.add_paragraph()
    p3.text = "Team: Team Elite  |  Track: Track 2 (RAG Engine)"
    p3.font.size = Pt(12)
    p3.font.bold = True
    p3.font.color.rgb = C_YELLOW_TAG

    p4 = tf1.add_paragraph()
    p4.text = "Members: Rishit Modh (Lead), Bhavya Juneja, Sugandh Jha"
    p4.font.size = Pt(12)
    p4.font.color.rgb = C_WHITE

    p5 = tf1.add_paragraph()
    p5.text = "Contact: u25me108@med.svnit.ac.in"
    p5.font.size = Pt(12)
    p5.font.color.rgb = C_YELLOW_TAG

    add_notes(s1, "Welcome judges and organizers! We are Team Elite from SVNIT Surat, presenting AuditLens AI for Track 2. In enterprise operations, organizations sign hundreds of contracts with customers, cloud vendors, and regulators that silently contradict one another. AuditLens AI eliminates this exposure by turning complex contracts into grounded, mathematically verified compliance intelligence using native MongoDB Atlas Vector Search.")

    # =========================================================================
    # SLIDE 2: 01 PROBLEM
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_top_bar(s2, "01 PROBLEM", "Problem", "What problem are you solving and for whom? Keep it to 2-3 lines.", 2)

    # Card 1: The Problem (Orange accent)
    card1_y = Inches(1.8)
    card1_h = Inches(2.2)
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card1_y, Inches(11.733), card1_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD_BG
    c1.line.color.rgb = C_BORDER
    c1.line.width = Pt(1)

    bar1 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), card1_y, Inches(0.12), card1_h)
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = C_ORANGE
    bar1.line.fill.background()

    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = Inches(0.4)
    tf_c1.margin_top = Inches(0.2)
    p_c1_t = tf_c1.paragraphs[0]
    p_c1_t.text = "The Problem"
    p_c1_t.font.size = Pt(14)
    p_c1_t.font.bold = True
    p_c1_t.font.color.rgb = C_TEXT_DARK

    p_c1_b = tf_c1.add_paragraph()
    p_c1_b.text = "Enterprise customer SLAs promise 99.9% uptime (max 1.0 hr downtime/month) with ₹75,000/hr penalties, while upstream cloud vendor MSAs allow 4.0-hour maintenance windows with zero penalty. Furthermore, under CERT-In Directions (2022), statutory breach reports are required within 6 hours, while internal CISO notification takes 30 minutes. Uncoordinated contracts create severe financial leakage and statutory regulatory penalties under IT Act §70B."
    p_c1_b.font.size = Pt(11.5)
    p_c1_b.font.color.rgb = C_TEXT_MUTED

    # Card 2: Who Is Affected (Orange accent)
    card2_y = Inches(4.3)
    card2_h = Inches(2.2)
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card2_y, Inches(11.733), card2_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD_BG
    c2.line.color.rgb = C_BORDER
    c2.line.width = Pt(1)

    bar2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), card2_y, Inches(0.12), card2_h)
    bar2.fill.solid()
    bar2.fill.fore_color.rgb = C_ORANGE
    bar2.line.fill.background()

    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = Inches(0.4)
    tf_c2.margin_top = Inches(0.2)
    p_c2_t = tf_c2.paragraphs[0]
    p_c2_t.text = "Who Is Affected"
    p_c2_t.font.size = Pt(14)
    p_c2_t.font.bold = True
    p_c2_t.font.color.rgb = C_TEXT_DARK

    p_c2_b = tf_c2.add_paragraph()
    p_c2_b.text = "Enterprise Legal Counsel, FinOps Teams, SRE Incident Commanders, and CISO Compliance Officers in Indian IT, fintech, and SaaS companies. Without automated cross-document intelligence, organizations spend hundreds of manual legal hours per incident, fail to recover vendor liabilities, and risk criminal compliance citations."
    p_c2_b.font.size = Pt(11.5)
    p_c2_b.font.color.rgb = C_TEXT_MUTED

    add_notes(s2, "Track 2 challenges us to turn source material into grounded, useful results. In enterprise IT operations, contracts don't exist in silos. If your AWS vendor takes a 3-hour downtime window, but your Customer SLA penalizes you after 1 hour at ₹75,000/hr, you lose money. Furthermore, under Indian CERT-In guidelines, failing to report within 6 hours invites statutory fines. Traditional search can't catch these contradictions, and standard LLMs hallucinate.")

    # =========================================================================
    # SLIDE 3: 02 SOLUTION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_top_bar(s3, "02 SOLUTION", "Solution", "Explain your idea simply, and what makes it different.", 3)

    # Card 1: What We Built (Teal accent)
    c3_1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card1_y, Inches(11.733), card1_h)
    c3_1.fill.solid()
    c3_1.fill.fore_color.rgb = C_CARD_BG
    c3_1.line.color.rgb = C_BORDER
    c3_1.line.width = Pt(1)

    bar3_1 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), card1_y, Inches(0.12), card1_h)
    bar3_1.fill.solid()
    bar3_1.fill.fore_color.rgb = C_TEAL
    bar3_1.line.fill.background()

    tf_c3_1 = c3_1.text_frame
    tf_c3_1.word_wrap = True
    tf_c3_1.margin_left = Inches(0.4)
    tf_c3_1.margin_top = Inches(0.2)
    p_31_t = tf_c3_1.paragraphs[0]
    p_31_t.text = "What We Built"
    p_31_t.font.size = Pt(14)
    p_31_t.font.bold = True
    p_31_t.font.color.rgb = C_TEXT_DARK

    p_31_b = tf_c3_1.add_paragraph()
    p_31_b.text = "AuditLens AI: An automated cross-contract due diligence and discrepancy engine. It concurrently indexes customer SLAs, vendor agreements, and incident response policies into MongoDB Atlas Vector Search, automatically reconciling service credit penalties (e.g. ₹75,000 for a 2-hour outage under Section 4.2), flag-checking notification clocks, and scanning for cross-contract contradictions."
    p_31_b.font.size = Pt(11.5)
    p_31_b.font.color.rgb = C_TEXT_MUTED

    # Card 2: What Makes It Unique (Teal accent)
    c3_2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card2_y, Inches(11.733), card2_h)
    c3_2.fill.solid()
    c3_2.fill.fore_color.rgb = C_CARD_BG
    c3_2.line.color.rgb = C_BORDER
    c3_2.line.width = Pt(1)

    bar3_2 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), card2_y, Inches(0.12), card2_h)
    bar3_2.fill.solid()
    bar3_2.fill.fore_color.rgb = C_TEAL
    bar3_2.line.fill.background()

    tf_c3_2 = c3_2.text_frame
    tf_c3_2.word_wrap = True
    tf_c3_2.margin_left = Inches(0.4)
    tf_c3_2.margin_top = Inches(0.2)
    p_32_t = tf_c3_2.paragraphs[0]
    p_32_t.text = "What Makes It Unique"
    p_32_t.font.size = Pt(14)
    p_32_t.font.bold = True
    p_32_t.font.color.rgb = C_TEXT_DARK

    p_32_b = tf_c3_2.add_paragraph()
    p_32_b.text = "1. Native 70/30 Hybrid Search combining Atlas dense vector search with exact lexical token matching for clause numbers (§4.2) and ₹ amounts.\n2. Code-level verbatim quote verification: Every citation is substring-checked against Atlas raw text (🛡️ Verbatim Verified badge).\n3. Deterministic compliance health scoring: 100 - (20×High) - (10×Med) - (10×Unverified).\n4. Strict hallucination defense & safe refusal on out-of-scope queries (e.g. drone surveillance)."
    p_32_b.font.size = Pt(11)
    p_32_b.font.color.rgb = C_TEXT_MUTED

    add_notes(s3, "AuditLens AI solves this dilemma through three technical pillars: First, multi-source conflict detection across disparate legal agreements. Second, code-level verbatim quote verification where every citation is string-checked against the raw text in MongoDB Atlas to eliminate hallucinations. Third, strict refusal guardrails that identify out-of-scope requests. This turns hours of tedious contract review into seconds.")

    # =========================================================================
    # SLIDE 4: 03 FEATURES
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_top_bar(s4, "03 FEATURES", "Key Features & Demo", "List up to 3 features and add a screenshot.", 4)

    # Left: 3 Numbered Features
    features_y = [Inches(1.8), Inches(3.4), Inches(5.0)]
    f_data = [
        ("1", "Multi-Source Conflict & Liability Matrix", "Automatically identifies contradictory uptime terms between customer SLAs and vendor MSAs, computing exact outage liabilities (₹75,000 for 2.0 hrs)."),
        ("2", "Verbatim Quote Verification & Grounding", "Code-level substring validation checks every LLM citation against MongoDB Atlas chunks with tamper-proof '🛡️ Verbatim Verified' badges."),
        ("3", "Empirical Evaluation Benchmark Harness", "Live /api/evaluate endpoint executing 8 standardized queries with 100% Recall@1, 100% Recall@3, and 100% safe refusal on out-of-scope queries.")
    ]

    for idx, (num, f_title, f_desc) in enumerate(f_data):
        y = features_y[idx]
        
        # Circle badge
        circ = s4.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), y + Inches(0.05), Inches(0.55), Inches(0.55))
        circ.fill.solid()
        circ.fill.fore_color.rgb = C_TEAL
        circ.line.fill.background()
        tf_circ = circ.text_frame
        p_circ = tf_circ.paragraphs[0]
        p_circ.text = num
        p_circ.font.size = Pt(13)
        p_circ.font.bold = True
        p_circ.font.color.rgb = C_WHITE
        p_circ.alignment = PP_ALIGN.CENTER

        # Text Box
        tbox = s4.shapes.add_textbox(Inches(1.5), y, Inches(4.8), Inches(1.3))
        tf_t = tbox.text_frame
        tf_t.word_wrap = True
        p_t0 = tf_t.paragraphs[0]
        p_t0.text = f_title
        p_t0.font.size = Pt(12)
        p_t0.font.bold = True
        p_t0.font.color.rgb = C_TEXT_DARK

        p_t1 = tf_t.add_paragraph()
        p_t1.text = f_desc
        p_t1.font.size = Pt(10)
        p_t1.font.color.rgb = C_TEXT_MUTED

    # Right: Screenshot Mockup Frame
    img_path = r"c:\Users\DELL\Desktop\UNcharted\assets\screenshots\06_query_scenario1.png"
    if os.path.exists(img_path):
        s4.shapes.add_picture(img_path, Inches(6.6), Inches(1.8), Inches(5.9), Inches(4.7))
    else:
        # Fallback frame
        sbox = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.6), Inches(1.8), Inches(5.9), Inches(4.7))
        sbox.fill.solid()
        sbox.fill.fore_color.rgb = C_CARD_BG
        sbox.line.color.rgb = C_BORDER

    add_notes(s4, "Here is our live interface. On the left are our three core innovations: multi-source conflict detection, programmatic quote verification, and our empirical evaluation benchmark. On the right is an actual execution of Scenario 1: for a 2-hour outage, it calculates ₹75,000 penalty, displays verified citations from Section 4.2 and Clause 3.2, and differentiates the 6-hour CERT-In deadline.")

    # =========================================================================
    # SLIDE 5: 04 TECH & IMPACT
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_top_bar(s5, "04 TECH & IMPACT", "Tech Stack & Impact", "What you built it with, and the impact it can have.", 5)

    col_w = Inches(5.6)
    col_h = Inches(4.7)

    # Column 1: Tech Stack (Teal accent)
    col1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), col_w, col_h)
    col1.fill.solid()
    col1.fill.fore_color.rgb = C_CARD_BG
    col1.line.color.rgb = C_BORDER
    col1.line.width = Pt(1)

    bar5_1 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(0.12), col_h)
    bar5_1.fill.solid()
    bar5_1.fill.fore_color.rgb = C_TEAL
    bar5_1.line.fill.background()

    tf_col1 = col1.text_frame
    tf_col1.word_wrap = True
    tf_col1.margin_left = Inches(0.4)
    tf_col1.margin_top = Inches(0.25)

    p_51_t = tf_col1.paragraphs[0]
    p_51_t.text = "Tech Stack"
    p_51_t.font.size = Pt(14)
    p_51_t.font.bold = True
    p_51_t.font.color.rgb = C_TEXT_DARK

    stack_bullets = [
        ("[Frontend]", "Vanilla JS, Tailwind CSS (MongoDB Green theme), Telemetry Inspector, Live Benchmark Modal"),
        ("[Backend / APIs]", "FastAPI (Python 3.14), Uvicorn, REST endpoints, Pydantic validation schemas"),
        ("[Data / AI]", "MongoDB Atlas Vector Search ($vectorSearch), sentence-transformers/all-mpnet-base-v2 (768-dim), Google Gemini 1.5 Flash"),
        ("[Cloud / Tools]", "Render Containerized Web Service (Docker), MongoDB Atlas M0 (AWS), Git/GitHub CI/CD")
    ]
    for tag, val in stack_bullets:
        p_tag = tf_col1.add_paragraph()
        p_tag.text = tag
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_TEXT_DARK
        p_tag.space_before = Pt(8)

        p_val = tf_col1.add_paragraph()
        p_val.text = val
        p_val.font.size = Pt(10)
        p_val.font.color.rgb = C_TEXT_MUTED

    # Column 2: Impact & Next Steps (Orange accent)
    col2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.933), Inches(1.8), col_w, col_h)
    col2.fill.solid()
    col2.fill.fore_color.rgb = C_CARD_BG
    col2.line.color.rgb = C_BORDER
    col2.line.width = Pt(1)

    bar5_2 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.933), Inches(1.8), Inches(0.12), col_h)
    bar5_2.fill.solid()
    bar5_2.fill.fore_color.rgb = C_ORANGE
    bar5_2.line.fill.background()

    tf_col2 = col2.text_frame
    tf_col2.word_wrap = True
    tf_col2.margin_left = Inches(0.4)
    tf_col2.margin_top = Inches(0.25)

    p_52_t = tf_col2.paragraphs[0]
    p_52_t.text = "Impact & Next Steps"
    p_52_t.font.size = Pt(14)
    p_52_t.font.bold = True
    p_52_t.font.color.rgb = C_TEXT_DARK

    impact_bullets = [
        ("[Expected impact]", "Eliminates SLA dispute losses, enforces statutory CERT-In breach compliance under IT Act §70B, and reduces multi-contract audit cycles from hours to under 2 seconds."),
        ("[How it can scale]", "Dedicated MongoDB Atlas M10+ multi-tenant sharding and real-time Change Stream indexing for enterprise document repositories."),
        ("[What you will build next]", "n8n automated webhook workflows to trigger Jira tickets and Slack alerts on high-risk conflicts, plus generative multi-party clause redlining.")
    ]
    for tag, val in impact_bullets:
        p_tag = tf_col2.add_paragraph()
        p_tag.text = tag
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_TEXT_DARK
        p_tag.space_before = Pt(12)

        p_val = tf_col2.add_paragraph()
        p_val.text = val
        p_val.font.size = Pt(10)
        p_val.font.color.rgb = C_TEXT_MUTED

    add_notes(s5, "Our technical architecture is built natively around MongoDB Atlas Vector Search. For embeddings, we chose all-mpnet-base-v2 running locally, providing 768-dimensional accuracy without API latency or cost. Google Gemini 1.5 Flash provides fast, grounded reasoning with structured JSON schemas. The impact is immediate: eliminating SLA penalty leakage and ensuring statutory compliance.")

    # =========================================================================
    # SLIDE 6: LINKS & SUBMISSION
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = C_NAVY
    bg6.line.fill.background()

    # Title & Subtitle
    t_box6 = s6.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.733), Inches(1.2))
    tf6 = t_box6.text_frame
    tf6.word_wrap = True
    p6_0 = tf6.paragraphs[0]
    p6_0.text = "Links & Submission"
    p6_0.font.size = Pt(36)
    p6_0.font.bold = True
    p6_0.font.color.rgb = C_WHITE

    p6_1 = tf6.add_paragraph()
    p6_1.text = "Make sure every link is public and opens without login."
    p6_1.font.size = Pt(13)
    p6_1.font.italic = True
    p6_1.font.color.rgb = RGBColor(148, 163, 184)

    # 3 Wide Link Cards
    links_data = [
        ("GitHub Repository", "https://github.com/rishitmodh12/AuditLens.AI"),
        ("Demo Video (2-3 min)", "https://auditlens-ai-13xs.onrender.com (Live Demo - Video link to be inserted in form)"),
        ("Live Prototype / App", "https://auditlens-ai-13xs.onrender.com")
    ]

    for idx, (label, link) in enumerate(links_data):
        y = Inches(2.2 + idx * 1.3)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(1.0))
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(15, 41, 56)
        card.line.color.rgb = RGBColor(30, 64, 85)

        # Teal left accent
        lbar = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y, Inches(0.12), Inches(1.0))
        lbar.fill.solid()
        lbar.fill.fore_color.rgb = C_TEAL
        lbar.line.fill.background()

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.4)
        tf.margin_top = Inches(0.2)

        p_lbl = tf.paragraphs[0]
        p_lbl.text = label
        p_lbl.font.size = Pt(13)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = C_WHITE

        p_lnk = tf.add_paragraph()
        p_lnk.text = link
        p_lnk.font.size = Pt(11)
        p_lnk.font.color.rgb = C_TEAL

    # Thank you footer
    t_box_end = s6.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
    tf_end = t_box_end.text_frame
    p_end = tf_end.paragraphs[0]
    p_end.text = "Thank you! Team Elite"
    p_end.font.size = Pt(18)
    p_end.font.bold = True
    p_end.font.color.rgb = C_TEAL

    output_path = r"c:\Users\DELL\Desktop\UNcharted\presentation\AuditLens_AI_Official_Template.pptx"
    prs.save(output_path)
    print(f"Successfully generated official template deck at: {output_path}")

if __name__ == "__main__":
    build_official_deck()
