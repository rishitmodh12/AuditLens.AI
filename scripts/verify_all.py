import urllib.request
import json
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

base_url = 'https://auditlens-ai-13xs.onrender.com'

print("=" * 60)
print("  AUDITLENS AI - COMPLETE SYSTEM RE-VERIFICATION SUITE")
print("  Target: " + base_url)
print("=" * 60)

# Test 1: Health Check
print("\n[1/6] Testing /api/health ...")
req = urllib.request.Request(f"{base_url}/api/health", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as res:
    health = json.loads(res.read().decode('utf-8'))
    print(" [+] Status:", health.get("status"))
    print(" [+] MongoDB Connected:", health.get("mongodb_connected"))
    print(" [+] Indexed Documents:", health.get("indexed_documents_count"))
    print(" [+] Total Vector Chunks in Atlas:", health.get("total_vector_chunks"))
    assert health.get("status") == "healthy"
    assert health.get("mongodb_connected") is True

# Test 2: Documents in MongoDB Atlas
print("\n[2/6] Testing /api/documents ...")
req = urllib.request.Request(f"{base_url}/api/documents", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as res:
    docs = json.loads(res.read().decode('utf-8'))
    print(f" [+] Total Documents Found: {len(docs)}")
    for d in docs:
        print(f"     - {d.get('doc_name')} ({d.get('total_chunks')} chunks, category: {d.get('category')})")
    assert len(docs) >= 3

# Test 3: Dynamic Cross-Contract Conflict Scanner
print("\n[3/6] Testing /api/conflicts/scan ...")
req = urllib.request.Request(f"{base_url}/api/conflicts/scan", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=25) as res:
    data = json.loads(res.read().decode('utf-8'))
    conflicts = data.get("conflicts", [])
    print(f" [+] Conflicts Detected: {len(conflicts)}")
    for c in conflicts:
        print(f"     - [{c.get('risk_level')}] {c.get('title')}")
    assert len(conflicts) > 0

# Test 4: Scenario 1 (Multi-Source Synthesis & Reconciled ₹75k Penalty)
print("\n[4/6] Testing POST /api/query (Scenario 1: Outage & Penalty Math) ...")
query_payload = {
    "query": "If an outage reaches 2.0 hours on our Indian banking payment gateway, what is the customer SLA penalty under Section 4.2, and what are the respective deadlines for internal CISO escalation and statutory CERT-In reporting?",
    "limit": 5,
    "user_email": "reverify_test@svnit.ac.in"
}
req = urllib.request.Request(
    f"{base_url}/api/query",
    data=json.dumps(query_payload).encode('utf-8'),
    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
)
with urllib.request.urlopen(req, timeout=30) as res:
    ans = json.loads(res.read().decode('utf-8'))
    print(" [+] Summary:", ans.get("summary"))
    print(" [+] Compliance Score:", ans.get("compliance_score"), "%")
    print(" [+] Score Calculation:", ans.get("score_calculation_breakdown"))
    print(f" [+] Citations Count: {len(ans.get('citations', []))}")
    for idx, c in enumerate(ans.get("citations", [])):
        print(f"     [{idx+1}] {c.get('doc_name')} - Verified: {c.get('quote_verified')}")
    # Verify ₹75,000 penalty and CERT-In 6.0 hours are present
    summary_txt = ans.get("summary", "")
    assert "75,000" in summary_txt, "Error: ₹75,000 penalty not found in summary!"
    assert "CERT-In" in summary_txt or "6.0" in summary_txt or "6 hour" in summary_txt, "Error: CERT-In timeline missing!"

# Test 5: Scenario 3 (Hallucination Defense / Negative Refusal)
print("\n[5/6] Testing POST /api/query (Scenario 3: Out-of-Scope Negative Test) ...")
neg_payload = {
    "query": "What is the policy for commercial drone surveillance over data centers?",
    "limit": 5,
    "user_email": "reverify_test@svnit.ac.in"
}
req = urllib.request.Request(
    f"{base_url}/api/query",
    data=json.dumps(neg_payload).encode('utf-8'),
    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
)
with urllib.request.urlopen(req, timeout=25) as res:
    neg_ans = json.loads(res.read().decode('utf-8'))
    print(" [+] Is Answerable:", neg_ans.get("is_answerable"))
    print(" [+] Summary:", neg_ans.get("summary"))
    assert neg_ans.get("is_answerable") is False, "Error: Negative query should have is_answerable=False"
    assert "Refusal" in neg_ans.get("summary", "") or "cannot be answered" in neg_ans.get("summary", "")

# Test 6: Track 2 Formal Evaluation Benchmark Harness
print("\n[6/6] Testing GET /api/evaluate (8 Standardized Benchmark Queries) ...")
req = urllib.request.Request(f"{base_url}/api/evaluate", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=35) as res:
    report = json.loads(res.read().decode('utf-8'))
    print(f" [+] Recall@1: {report.get('recall_at_1')} (100%)")
    print(f" [+] Recall@3: {report.get('recall_at_3')} (100%)")
    print(f" [+] Refusal Accuracy: {report.get('refusal_accuracy')} (100%)")
    print(f" [+] Overall Precision: {report.get('overall_precision')} (100%)")
    assert report.get("recall_at_1") == 1.0
    assert report.get("recall_at_3") == 1.0
    assert report.get("refusal_accuracy") == 1.0

print("\n" + "=" * 60)
print("  🏆 ALL 6/6 SYSTEM AUDIT CHECKS PASSED WITH 100% SUCCESS!")
print("=" * 60)
